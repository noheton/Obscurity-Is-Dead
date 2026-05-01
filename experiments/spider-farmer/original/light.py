"""Light platform for Spider Farmer (BLE-only).

Commands are sent exclusively via the active BLE connection.
"""
from __future__ import annotations

import logging

from homeassistant.components.light import ATTR_BRIGHTNESS, ColorMode, LightEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .coordinator import SpiderFarmerCoordinator

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    store = hass.data[DOMAIN][config_entry.entry_id]
    async_add_entities([
        SFLight(store, "light",  "Primary Light"),
        SFLight(store, "light2", "Secondary Light"),
    ])


class SFLight(LightEntity):
    _attr_has_entity_name          = True
    _attr_color_mode               = ColorMode.BRIGHTNESS
    _attr_supported_color_modes    = {ColorMode.BRIGHTNESS}

    def __init__(self, store: dict, key: str, name: str) -> None:
        self._store = store
        self._key   = key
        self._coord: SpiderFarmerCoordinator = store["coordinator"]
        pid = store["pid"]

        self._attr_name      = name
        self._attr_unique_id = f"{pid}_{key}_entity"
        self._attr_device_info = {
            "identifiers":  {(DOMAIN, pid)},
            "name":         f"Spider Farmer {pid}",
            "manufacturer": "Spider Farmer",
        }

    async def async_added_to_hass(self) -> None:
        self._coord.register_callback(self._on_update)

    async def async_will_remove_from_hass(self) -> None:
        self._coord.unregister_callback(self._on_update)

    @callback
    def _on_update(self) -> None:
        self.async_write_ha_state()

    # ------------------------------------------------------------------
    # State properties (read from coordinator)
    # ------------------------------------------------------------------

    @property
    def available(self) -> bool:
        return self._coord.available

    @property
    def is_on(self) -> bool:
        d = self._coord.data.get(self._key, {})
        if "on" in d:
            return d["on"] == 1
        return d.get("level", 0) > 0

    @property
    def brightness(self) -> int:
        d = self._coord.data.get(self._key, {})
        return int(d.get("level", 0) * 255 / 100)

    # ------------------------------------------------------------------
    # Commands
    # ------------------------------------------------------------------

    async def async_turn_on(self, **kwargs) -> None:
        bri   = kwargs.get(ATTR_BRIGHTNESS, self.brightness or 255)
        level = int(bri * 100 / 255)
        await self._send_cmd(on=True, level=level)

    async def async_turn_off(self, **kwargs) -> None:
        await self._send_cmd(on=False, level=0)

    async def _send_cmd(self, on: bool, level: int) -> None:
        # Only primary light has a BLE command (setLight); secondary is read-only via BLE
        if self._key != "light":
            _LOGGER.debug("Light cmd: no BLE command defined for %s", self._key)
            return

        ble = self._store.get("ble")
        if not ble or not ble.connected:
            _LOGGER.warning("Light cmd: BLE not connected — command dropped (on=%s level=%d)", on, level)
            return

        try:
            pkt, mid = ble.protocol.cmd_set_light(on, level)
            _LOGGER.debug("Light cmd: BLE setLight on=%s level=%d msgId=%s", on, level, mid)
            resp = await ble.send_command(pkt, mid)
            if resp is not None:
                self._coord.update({self._key: {"on": int(on), "level": level}})
        except Exception:
            _LOGGER.debug("Light BLE command failed", exc_info=True)
