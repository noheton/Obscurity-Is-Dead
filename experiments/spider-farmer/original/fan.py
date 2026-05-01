"""Fan platform for Spider Farmer (BLE-only): fan, blower, heater.

Commands are sent exclusively via the active BLE connection.
"""
from __future__ import annotations

import logging

from homeassistant.components.fan import FanEntity, FanEntityFeature
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .coordinator import SpiderFarmerCoordinator

_LOGGER = logging.getLogger(__name__)

PRESET_MANUAL = "Manual"
PRESET_AUTO   = "Auto"


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    store = hass.data[DOMAIN][config_entry.entry_id]
    async_add_entities([
        SFFan(store, "Fan",    "fan",    level_max=10),
        SFFan(store, "Blower", "blower", level_max=100, auto_mode=2),
        SFFan(store, "Heater", "heater", level_max=10,  auto_mode=3),
    ])


class SFFan(FanEntity):
    _attr_has_entity_name = True

    def __init__(
        self,
        store: dict,
        name: str,
        key: str,
        level_max: int,
        auto_mode: int | None = None,
    ) -> None:
        self._store     = store
        self._key       = key
        self._level_max = level_max
        self._auto_mode = auto_mode
        self._coord: SpiderFarmerCoordinator = store["coordinator"]
        pid = store["pid"]

        self._attr_name      = name
        self._attr_unique_id = f"{pid}_{key}_fan"
        self._attr_device_info = {"identifiers": {(DOMAIN, pid)}}

        base = (
            FanEntityFeature.SET_SPEED
            | FanEntityFeature.TURN_ON
            | FanEntityFeature.TURN_OFF
        )
        if auto_mode is not None:
            self._attr_supported_features = base | FanEntityFeature.PRESET_MODE
            self._attr_preset_modes       = [PRESET_MANUAL, PRESET_AUTO]
        else:
            self._attr_supported_features = base

    async def async_added_to_hass(self) -> None:
        self._coord.register_callback(self._on_update)

    async def async_will_remove_from_hass(self) -> None:
        self._coord.unregister_callback(self._on_update)

    @callback
    def _on_update(self) -> None:
        self.async_write_ha_state()

    # ------------------------------------------------------------------
    # State properties
    # ------------------------------------------------------------------

    @property
    def available(self) -> bool:
        return self._coord.available

    @property
    def percentage_step(self) -> float:
        return 100 / self._level_max

    @property
    def is_on(self) -> bool:
        d = self._coord.data.get(self._key, {})
        if "on" in d:
            return d["on"] == 1
        return d.get("level", 0) > 0

    @property
    def percentage(self) -> int:
        d     = self._coord.data.get(self._key, {})
        level = d.get("level", 0)
        return round(level * 100 / self._level_max)

    @property
    def preset_mode(self) -> str | None:
        if self._auto_mode is None:
            return None
        d = self._coord.data.get(self._key, {})
        return PRESET_MANUAL if d.get("modeType", 0) == 0 else PRESET_AUTO

    # ------------------------------------------------------------------
    # Commands
    # ------------------------------------------------------------------

    def _pct_to_level(self, pct: int) -> int:
        return round(pct * self._level_max / 100)

    def _build_data(self, level: int, manual: bool = True) -> dict:
        d: dict = {"on": 1 if level > 0 else 0, "level": level}
        if self._auto_mode is not None:
            d["modeType"] = 0 if manual else self._auto_mode
        return d

    async def _send_cmd(self, device_data: dict) -> None:
        ble = self._store.get("ble")
        if not ble or not ble.connected:
            _LOGGER.warning("Fan cmd: BLE not connected for %s — command dropped", self._key)
            return

        level = device_data.get("level", 0)
        on    = device_data.get("on", 1 if level > 0 else 0) == 1
        mode  = device_data.get("modeType", 0)

        try:
            if self._key == "fan":
                pkt, mid = ble.protocol.cmd_set_fan(on, level)
            elif self._key == "blower":
                pkt, mid = ble.protocol.cmd_set_blower(on, level, mode)
            elif self._key == "heater":
                pkt, mid = ble.protocol.cmd_set_heater(on, level, mode)
            else:
                return
            _LOGGER.debug(
                "Fan cmd: BLE %s on=%s level=%d mode=%d msgId=%s",
                self._key, on, level, mode, mid,
            )
            resp = await ble.send_command(pkt, mid)
            if resp is not None:
                self._coord.update({self._key: device_data})
        except Exception:
            _LOGGER.debug("Fan BLE command failed", exc_info=True)

    async def async_turn_on(
        self, speed=None, percentage=None, preset_mode=None, **kwargs
    ) -> None:
        manual = preset_mode != PRESET_AUTO
        if percentage is not None:
            level = self._pct_to_level(percentage)
        else:
            level = self._pct_to_level(self.percentage or 10)
        level = max(1, level)
        await self._send_cmd(self._build_data(level, manual))

    async def async_turn_off(self, **kwargs) -> None:
        await self._send_cmd(self._build_data(0))

    async def async_set_percentage(self, percentage: int) -> None:
        level  = self._pct_to_level(percentage)
        manual = (self.preset_mode != PRESET_AUTO)
        await self._send_cmd(self._build_data(level, manual))

    async def async_set_preset_mode(self, preset_mode: str) -> None:
        level  = self._pct_to_level(self.percentage or 10)
        level  = max(1, level)
        manual = (preset_mode != PRESET_AUTO)
        await self._send_cmd(self._build_data(level, manual))
