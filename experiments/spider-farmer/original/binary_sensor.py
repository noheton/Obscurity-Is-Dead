"""Binary sensor platform for Spider Farmer (BLE-only).

All sensors read from the shared SpiderFarmerCoordinator populated by the
BLE connection loop.
"""
from __future__ import annotations

import logging

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .coordinator import SpiderFarmerCoordinator

_LOGGER = logging.getLogger(__name__)

# (unique_key_suffix, display_name, device_class, *data_path_to_bool_field)
# The last element of the path is the key whose value == 1 means "on".
_BINARY_DEFS: tuple[tuple, ...] = (
    ("sys_wifi_conn",  "WiFi Connected",       BinarySensorDeviceClass.CONNECTIVITY, "sys", "wifi",      "isConnect"),
    ("sys_eth_conn",   "Ethernet Connected",   BinarySensorDeviceClass.CONNECTIVITY, "sys", "eth",       "isConnect"),
    ("sys_bt_conn",    "Bluetooth Connected",  BinarySensorDeviceClass.CONNECTIVITY, "sys", "bluetooth", "isConnect"),
    ("sensor_day",     "Day Mode",             None,                                  "sensor", "isDaySensor"),
    ("plan_running",   "Growth Plan Running",  None,                                  "plan",   "isPlanRun"),
)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    store = hass.data[DOMAIN][config_entry.entry_id]
    coord: SpiderFarmerCoordinator = store["coordinator"]
    pid: str = store["pid"]

    async_add_entities([
        SFBinary(coord, pid, *defn)
        for defn in _BINARY_DEFS
    ])


class SFBinary(BinarySensorEntity):
    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: SpiderFarmerCoordinator,
        pid: str,
        uid_key: str,
        name: str,
        dev_class: BinarySensorDeviceClass | None,
        *path: str,
    ) -> None:
        self._coord    = coordinator
        self._path     = path   # full path; last element is the bool field
        self._attr_name         = name
        self._attr_device_class = dev_class
        self._attr_unique_id    = f"{pid}_{uid_key}_bin"
        self._attr_device_info  = {"identifiers": {(DOMAIN, pid)}}

    async def async_added_to_hass(self) -> None:
        self._coord.register_callback(self._on_update)

    async def async_will_remove_from_hass(self) -> None:
        self._coord.unregister_callback(self._on_update)

    @callback
    def _on_update(self) -> None:
        self.async_write_ha_state()

    @property
    def available(self) -> bool:
        return self._coord.available

    @property
    def is_on(self) -> bool:
        cur = self._coord.data
        for key in self._path:
            if not isinstance(cur, dict):
                return False
            cur = cur.get(key)
        return cur == 1
