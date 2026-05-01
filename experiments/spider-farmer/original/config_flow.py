"""Config flow for Spider Farmer (BLE-only).

Step 1  (user / ble_device)   — Pick a discovered BLE device or enter MAC manually.
                                Pre-selects known KEY/IV based on advertising name.
Step 2  (ble_credentials)     — Confirm / override the KEY, IV and user credentials.

Auto-discovery:
  When HA's Bluetooth integration spots an SF-GGS-* device it calls
  async_step_bluetooth, which skips step 1 and goes straight to step 2
  since the BLE address is already known.

Options flow:  re-configure BLE credentials in-place without removing the entry.
"""
from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.components.bluetooth import (
    BluetoothServiceInfoBleak,
    async_discovered_service_info,
)
from homeassistant.data_entry_flow import FlowResult

from .const import (
    CONF_BLE_ADDRESS,
    CONF_BLE_IV,
    CONF_BLE_KEY,
    CONF_BLE_USER_ID,
    CONF_BLE_USER_EMAIL,
    DOMAIN,
    BLE_DEVICE_TYPES,
    BLE_DEVICE_TYPE_NAMES,
)

_LOGGER = logging.getLogger(__name__)

# Map advertising-name prefix → device-type key
_NAME_TO_TYPE: dict[str, str] = {
    "SF-GGS-CB":   "cb",
    "SF-GGS-PS10": "ps10",
    "SF-GGS-PS5":  "ps10",   # same key family
    "SF-GGS-LC":   "led",
}

_CB = BLE_DEVICE_TYPES["cb"]

# One-liner summary of all presets shown in the credentials form
_PRESET_LINES = "\n".join(
    f"  {BLE_DEVICE_TYPE_NAMES[k]}:\n    KEY={v['key']}  IV={v['iv']}"
    for k, v in BLE_DEVICE_TYPES.items()
)


def _parse_secret(s: str) -> bytes | None:
    """Accept 16-char ASCII or 32 hex-chars (spaces OK) → 16 bytes."""
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


def _type_from_name(name: str) -> str:
    """Return a device-type key ('cb', 'led', 'ps10') from an advertising name."""
    for prefix, dtype in _NAME_TO_TYPE.items():
        if name.startswith(prefix):
            return dtype
    return "cb"   # default to CB (most common device using this integration)


def _pid_from_address(address: str) -> str:
    """Derive a PID (MAC without colons, uppercase) from a BLE address."""
    return address.replace(":", "").upper()


class SpiderFarmerConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 3

    def __init__(self) -> None:
        self._ble_address: str  = ""
        self._ble_name:    str  = ""
        self._ble_type:    str  = "cb"

    # ------------------------------------------------------------------
    # Passive BLE discovery entry-point (HA calls this automatically)
    # ------------------------------------------------------------------

    async def async_step_bluetooth(
        self, discovery_info: BluetoothServiceInfoBleak
    ) -> FlowResult:
        """Handle a device discovered via the HA Bluetooth integration."""
        await self.async_set_unique_id(discovery_info.address)
        self._abort_if_unique_id_configured()

        self._ble_address = discovery_info.address
        self._ble_name    = discovery_info.name or "SF-GGS"
        self._ble_type    = _type_from_name(self._ble_name)

        self.context["title_placeholders"] = {
            "name":    self._ble_name,
            "address": self._ble_address,
        }

        _LOGGER.debug(
            "BLE discovery: name=%s address=%s → type=%s",
            self._ble_name, self._ble_address, self._ble_type,
        )

        # BLE address already known — go straight to credential confirmation
        return await self.async_step_ble_credentials()

    # ------------------------------------------------------------------
    # Step 1 — BLE device selection (manual flow)
    # ------------------------------------------------------------------

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Show discovered SF-GGS-* devices; user picks one or enters MAC."""
        errors: dict[str, str] = {}

        if user_input is not None:
            chosen = (user_input.get(CONF_BLE_ADDRESS) or "").strip()
            if not chosen:
                errors[CONF_BLE_ADDRESS] = "ble_address_required"
            else:
                # chosen may be "MAC  (name)" from the dropdown — extract MAC
                mac = chosen.split("  ")[0].strip().upper()
                self._ble_address = mac
                for info in async_discovered_service_info(self.hass):
                    if info.address.upper() == mac:
                        self._ble_name = info.name or ""
                        self._ble_type = _type_from_name(self._ble_name)
                        break
                await self.async_set_unique_id(self._ble_address)
                self._abort_if_unique_id_configured()
                return await self.async_step_ble_credentials()

        # Build a dict of discovered devices
        already_configured = {
            e.data.get(CONF_BLE_ADDRESS, "").upper()
            for e in self._async_current_entries()
        }
        discovered: dict[str, str] = {}
        for info in async_discovered_service_info(self.hass):
            if (info.name or "").startswith("SF-GGS") and info.address.upper() not in already_configured:
                label = f"{info.address}  ({info.name})"
                discovered[label] = label

        if discovered:
            schema = vol.Schema({
                vol.Required(CONF_BLE_ADDRESS): vol.In(discovered),
            })
            hint = f"Found {len(discovered)} nearby Spider Farmer device(s). Select one to continue."
        else:
            schema = vol.Schema({
                vol.Required(CONF_BLE_ADDRESS): str,
            })
            hint = "No nearby devices found. Enter BLE MAC address manually (e.g. AA:BB:CC:DD:EE:FF)."

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
            errors=errors,
            description_placeholders={"hint": hint},
        )

    # ------------------------------------------------------------------
    # Step 2 — confirm / override BLE KEY, IV, user credentials
    # ------------------------------------------------------------------

    async def async_step_ble_credentials(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        errors: dict[str, str] = {}
        preset = BLE_DEVICE_TYPES.get(self._ble_type, _CB)

        if user_input is not None:
            key = _parse_secret(user_input.get(CONF_BLE_KEY, ""))
            iv  = _parse_secret(user_input.get(CONF_BLE_IV,  ""))
            if not key:
                errors[CONF_BLE_KEY] = "invalid_key"
            if not iv:
                errors[CONF_BLE_IV]  = "invalid_iv"

            if not errors:
                pid = _pid_from_address(self._ble_address)
                title = self._ble_name or f"Spider Farmer {self._ble_address}"
                return self.async_create_entry(
                    title=title,
                    data={
                        "pid":               pid,
                        CONF_BLE_ADDRESS:    self._ble_address.upper(),
                        CONF_BLE_KEY:        user_input[CONF_BLE_KEY].strip(),
                        CONF_BLE_IV:         user_input[CONF_BLE_IV].strip(),
                        CONF_BLE_USER_ID:    user_input.get(CONF_BLE_USER_ID,    "000000"),
                        CONF_BLE_USER_EMAIL: user_input.get(CONF_BLE_USER_EMAIL, "user@example.com"),
                    },
                )

        device_hint = (
            f"Device: {self._ble_name} ({self._ble_address})  "
            f"Type detected: {BLE_DEVICE_TYPE_NAMES.get(self._ble_type, self._ble_type)}"
        ) if self._ble_address else "Enter BLE encryption credentials."

        return self.async_show_form(
            step_id="ble_credentials",
            data_schema=vol.Schema({
                vol.Required(CONF_BLE_KEY,        default=preset["key"]):            str,
                vol.Required(CONF_BLE_IV,         default=preset["iv"]):             str,
                vol.Optional(CONF_BLE_USER_ID,    default="000000"):                 str,
                vol.Optional(CONF_BLE_USER_EMAIL, default="user@example.com"):       str,
            }),
            errors=errors,
            description_placeholders={
                "device_hint":  device_hint,
                "preset_lines": _PRESET_LINES,
            },
        )

    # ------------------------------------------------------------------
    # Options flow — update BLE credentials in-place
    # ------------------------------------------------------------------

    @staticmethod
    def async_get_options_flow(
        config_entry: config_entries.ConfigEntry,
    ) -> "SpiderFarmerOptionsFlow":
        return SpiderFarmerOptionsFlow(config_entry)


class SpiderFarmerOptionsFlow(config_entries.OptionsFlow):
    def __init__(self, entry: config_entries.ConfigEntry) -> None:
        self._entry = entry

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        errors: dict[str, str] = {}
        d = self._entry.data

        if user_input is not None:
            if not _parse_secret(user_input.get(CONF_BLE_KEY, "")):
                errors[CONF_BLE_KEY] = "invalid_key"
            if not _parse_secret(user_input.get(CONF_BLE_IV, "")):
                errors[CONF_BLE_IV]  = "invalid_iv"
            if not errors:
                updated = dict(d)
                updated.update({
                    CONF_BLE_KEY:        user_input[CONF_BLE_KEY].strip(),
                    CONF_BLE_IV:         user_input[CONF_BLE_IV].strip(),
                    CONF_BLE_USER_ID:    user_input.get(CONF_BLE_USER_ID,    "000000"),
                    CONF_BLE_USER_EMAIL: user_input.get(CONF_BLE_USER_EMAIL, "user@example.com"),
                })
                self.hass.config_entries.async_update_entry(self._entry, data=updated)
                return self.async_create_entry(title="", data={})

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Required(CONF_BLE_KEY,        default=d.get(CONF_BLE_KEY,        _CB["key"])):        str,
                vol.Required(CONF_BLE_IV,         default=d.get(CONF_BLE_IV,         _CB["iv"])):         str,
                vol.Optional(CONF_BLE_USER_ID,    default=d.get(CONF_BLE_USER_ID,    "000000")):          str,
                vol.Optional(CONF_BLE_USER_EMAIL, default=d.get(CONF_BLE_USER_EMAIL, "user@example.com")): str,
            }),
            errors=errors,
            description_placeholders={"preset_lines": _PRESET_LINES},
        )
