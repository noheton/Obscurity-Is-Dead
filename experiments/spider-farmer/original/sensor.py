"""Sensor platform for Spider Farmer (BLE-only).

Sensors read from the shared SpiderFarmerCoordinator which is populated by
the BLE connection loop.  Sensors that have no data yet (coordinator.data
empty or key absent) return None (unavailable).
"""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.core import HomeAssistant, callback
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .coordinator import SpiderFarmerCoordinator

_LOGGER = logging.getLogger(__name__)


def _get(data: dict, *path: str) -> Any:
    """Safe nested dict lookup — returns None when any key is missing."""
    cur = data
    for key in path:
        if not isinstance(cur, dict):
            return None
        cur = cur.get(key)
    return cur


# (unique_key_suffix, display_name, unit, device_class, *data_path)
_SENSOR_DEFS: tuple[tuple, ...] = (
    # Environmental
    ("temp",         "Temperature",      "°C",          SensorDeviceClass.TEMPERATURE,      "sensor", "temp"),
    ("humi",         "Humidity",         "%",           SensorDeviceClass.HUMIDITY,          "sensor", "humi"),
    ("vpd",          "VPD",              "kPa",         None,                                "sensor", "vpd"),
    # Extended environmental — reported by optional probes
    ("co2",          "CO₂",             "ppm",          SensorDeviceClass.CO2,               "sensor", "co2"),
    ("ppfd",         "PPFD",             "μmol/m²/s",   None,                                "sensor", "ppfd"),
    ("soilTemp",     "Soil Temperature", "°C",          SensorDeviceClass.TEMPERATURE,       "sensor", "soilTemp"),
    ("soilHumi",     "Soil Humidity",    "%",           SensorDeviceClass.HUMIDITY,          "sensor", "soilHumi"),
    ("soilEc",       "Soil EC",          "µS/cm",       None,                                "sensor", "soilEc"),
    # Growth plan
    ("planProgress", "Growth Progress",  "%",           None,                                "plan",   "planProgress"),
    # System — populated by getSysSta
    ("rssi",         "WiFi RSSI",        "dBm",         SensorDeviceClass.SIGNAL_STRENGTH,   "sys",    "wifi",   "rssi"),
    ("upTime",       "Uptime",           "s",           SensorDeviceClass.DURATION,          "sys",    "upTime"),
    ("mem",          "Free Memory",      "KB",          None,                                "sys",    "mem"),
    ("fwVer",        "Firmware Version", None,          None,                                "sys",    "ver"),
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
        SFSensor(coord, pid, *defn)
        for defn in _SENSOR_DEFS
    ])


class SFSensor(SensorEntity):
    _attr_has_entity_name  = True
    _attr_state_class      = SensorStateClass.MEASUREMENT

    def __init__(
        self,
        coordinator: SpiderFarmerCoordinator,
        pid: str,
        key: str,
        name: str,
        unit: str | None,
        dev_class: SensorDeviceClass | None,
        *path: str,
    ) -> None:
        self._coord    = coordinator
        self._path     = path
        self._attr_name                          = name
        self._attr_native_unit_of_measurement    = unit
        self._attr_device_class                  = dev_class
        self._attr_unique_id                     = f"{pid}_{key}"
        self._attr_device_info = {
            "identifiers":  {(DOMAIN, pid)},
            "name":         f"Spider Farmer {pid}",
            "manufacturer": "Spider Farmer",
        }
        # String sensors (fw ver) must not have measurement state class
        if unit is None and dev_class is None:
            self._attr_state_class = None

    async def async_added_to_hass(self) -> None:
        self._coord.register_callback(self._on_update)

    async def async_will_remove_from_hass(self) -> None:
        self._coord.unregister_callback(self._on_update)

    @callback
    def _on_update(self) -> None:
        self.async_write_ha_state()

    @property
    def native_value(self) -> Any:
        return _get(self._coord.data, *self._path)

    @property
    def available(self) -> bool:
        return self._coord.available
