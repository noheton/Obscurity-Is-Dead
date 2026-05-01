"""Spider Farmer grow-box integration — BLE only.

Setup creates one SpiderFarmerCoordinator (shared data store) and starts a
BLECoordinator.  Platform files read from the coordinator; they never interact
with BLE directly.

Debug logging
-------------
Enable debug logging in configuration.yaml to trace the raw protocol:

    logger:
      default: warning
      logs:
        custom_components.spider_farmer: debug

This will log:
  - Every BLE wire packet (hex dump, msgtype, fragment info)
  - Every decrypted BLE JSON payload
  - Command packets sent via BLE
  - Connection lifecycle events (connect, disconnect, activation steps)
  - Coordinator data merges (what changed after each update)
"""
from __future__ import annotations

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import (
    DOMAIN,
    CONF_BLE_ADDRESS,
    CONF_BLE_KEY,
    CONF_BLE_IV,
    CONF_BLE_USER_ID,
    CONF_BLE_USER_EMAIL,
    BLE_DEVICE_TYPES,
)
from .coordinator import SpiderFarmerCoordinator

_LOGGER = logging.getLogger(__name__)

PLATFORMS = ["light", "sensor", "fan", "binary_sensor"]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    ble_address = entry.data.get(CONF_BLE_ADDRESS, "").strip()
    if not ble_address:
        _LOGGER.error(
            "Spider Farmer entry %s has no BLE address — cannot set up BLE-only integration",
            entry.entry_id,
        )
        return False

    pid = ble_address.replace(":", "").upper()
    coord = SpiderFarmerCoordinator()

    _LOGGER.debug(
        "Setting up Spider Farmer entry %s: ble_address=%s pid=%s",
        entry.entry_id, ble_address, pid,
    )

    ble_coord = await _setup_ble(hass, entry, coord, ble_address)
    if ble_coord is None:
        _LOGGER.error(
            "Spider Farmer BLE could not start for %s — check key/IV and that bleak is installed",
            ble_address,
        )
        return False

    _LOGGER.info("Spider Farmer BLE started for %s", ble_address)

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = {
        "coordinator": coord,
        "ble":         ble_coord,
        "pid":         pid,
    }

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    _LOGGER.debug("Spider Farmer entry %s setup complete", entry.entry_id)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if ok:
        store = hass.data[DOMAIN].pop(entry.entry_id, {})
        ble = store.get("ble")
        if ble is not None:
            await ble.stop()
            _LOGGER.debug("BLE: stopped for entry %s", entry.entry_id)
    return ok


async def async_migrate_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Migrate config entries to the current VERSION.

    Version 3: BLE-only.  Drop MQTT fields (pid, uid, mqtt_topic) and derive
    pid from the BLE address.  Also carry forward the v1→v2 CB key fix.
    """
    _STALE_CB_KEY = "J4G0M9dX1f1v3fXr"

    if entry.version < 3:
        new_data = dict(entry.data)

        # Fix stale CB key if still present (v1 issue)
        if new_data.get(CONF_BLE_KEY, "").strip() == _STALE_CB_KEY:
            cb = BLE_DEVICE_TYPES["cb"]
            new_data[CONF_BLE_KEY] = cb["key"]
            new_data[CONF_BLE_IV]  = cb["iv"]
            _LOGGER.info(
                "Migrated Spider Farmer entry %s: replaced stale CB key",
                entry.entry_id,
            )

        # Drop legacy MQTT-only fields
        for field in ("uid", "mqtt_topic"):
            new_data.pop(field, None)

        # Ensure pid is derived from BLE address
        ble_addr = new_data.get(CONF_BLE_ADDRESS, "")
        if ble_addr:
            new_data["pid"] = ble_addr.replace(":", "").upper()
        else:
            # No BLE address in old entry — migration cannot proceed
            _LOGGER.error(
                "Cannot migrate Spider Farmer entry %s to v3: no BLE address stored",
                entry.entry_id,
            )
            return False

        hass.config_entries.async_update_entry(entry, data=new_data, version=3)
        _LOGGER.info("Migrated Spider Farmer entry %s to version 3 (BLE-only)", entry.entry_id)

    return True


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

async def _setup_ble(
    hass: HomeAssistant,
    entry: ConfigEntry,
    coord: SpiderFarmerCoordinator,
    address: str,
) -> "BLECoordinator | None":   # type: ignore[name-defined]
    try:
        from .ble_protocol import BLEProtocol
        from .ble_coordinator import BLECoordinator
    except ImportError:
        _LOGGER.error("BLE modules could not be imported")
        return None

    raw_key = entry.data.get(CONF_BLE_KEY, "")
    raw_iv  = entry.data.get(CONF_BLE_IV,  "")
    key = _parse_ble_secret(raw_key)
    iv  = _parse_ble_secret(raw_iv)

    _LOGGER.debug(
        "BLE: parsing key=%r → %s bytes  iv=%r → %s bytes",
        raw_key, len(key) if key else "INVALID",
        raw_iv,  len(iv)  if iv  else "INVALID",
    )

    if not key or not iv:
        _LOGGER.warning(
            "BLE key/IV for %s is invalid — must be 16 ASCII chars or 32 hex chars",
            address,
        )
        return None

    try:
        user_id    = entry.data.get(CONF_BLE_USER_ID,    "000000")
        user_email = entry.data.get(CONF_BLE_USER_EMAIL, "user@example.com")
        _LOGGER.debug(
            "BLE: creating protocol key=%s iv=%s uid=%s",
            key.hex(), iv.hex(), user_id,
        )
        protocol  = BLEProtocol(key, iv, user_id)
        ble_coord = BLECoordinator(hass, address, protocol, coord, user_email)
        await ble_coord.start()
        return ble_coord
    except Exception:
        _LOGGER.exception("Failed to start BLE coordinator for %s", address)
        return None


def _parse_ble_secret(s: str) -> bytes | None:
    """Accept 16-char ASCII or 32 hex-chars (spaces optional) → 16 bytes."""
    if not s:
        return None
    enc = s.strip().encode("ascii", errors="ignore")
    if len(enc) == 16:
        return enc
    clean = s.replace(" ", "")
    if len(clean) == 32:
        try:
            return bytes.fromhex(clean)
        except ValueError:
            pass
    return None
