# MQTT Protocol

## Topic Structure

```
Subscribe (device → app):   SF/GGS/CB/API/UP/<PID>
Publish  (app → device):    SF/GGS/CB/API/UP/<PID>   (same topic, confirmed by phase-3 probes)
Offline LWT:                SF/Offline/<PID>
```

`<PID>` is the device's MAC address without colons, uppercase (e.g. `80F1B2B423C8`).

---

## Envelope Format

Every MQTT message is a JSON object with this top-level structure:

```json
{
  "method": "<method_name>",
  "pid":    "<DEVICE_PID>",
  "uid":    "<USER_ID>",
  "pcode":  1004,
  "UTC":    1713000000,
  "data":   { ... }
}
```

| Field | Type | Notes |
|-------|------|-------|
| `method` | string | See method table below |
| `pid` | string | Device MAC, no colons, uppercase |
| `uid` | string | Numeric user ID from API login |
| `pcode` | int | Observed value: `1004`. Purpose unknown — likely a protocol version or product code |
| `UTC` | int | Unix timestamp (seconds). **Must be current** — stale timestamps are rejected |
| `data` | object | Method-specific payload |

---

## Methods — Device → App (inbound)

| Method | Trigger | Description |
|--------|---------|-------------|
| `getDevSta` | Periodic (~5 s) | Full device state snapshot. Primary data source for all sensors and actuators |
| `getSysSta` | Periodic | System status: WiFi, MQTT, Ethernet, Bluetooth connectivity + uptime + memory |
| `getDeviceInfo` | On connect | Static device info: model, firmware version, serial number |
| `getGGSDev` | On connect | Sub-device / outlet enumeration |
| `getOtaInfo` | On firmware event | OTA update available notification |
| `getAlarmLog` | On alarm | Alarm event notification |
| `getConfigFile` | Response to request | Returns current configuration blob |
| `getConfigField` | Response to request | Returns a single config field |
| `getBasePltLst` | Response | System plant template list |
| `getCustPltLst` | Response | User's custom plant template list |

---

## Methods — App → Device (outbound / control)

### State read requests
| Method | `data` | Description |
|--------|--------|-------------|
| `getDevSta` | `{}` | Request immediate state snapshot |
| `getSysSta` | `{}` | Request system status |
| `getDeviceInfo` | `{}` | Request device info |
| `getGGSDev` | `{}` | Request sub-device list |
| `getOtaInfo` | `{}` | Request OTA status |
| `getAlarmLog` | `{}` | Request alarm history |
| `getConfigFile` | `{}` | Request full config blob |
| `getConfigField` | `{"field": "<name>"}` | Request single field |
| `getAll` | `{}` | Request all state in one shot |
| `getLocalTimezone` | `{}` | Request device timezone |
| `getDataTimeout` | `{}` | Request data timeout setting |

### Device power & lifecycle
| Method | `data` shape | Description |
|--------|-------------|-------------|
| `setOnOff` | `{"devType": "<key>", "on": 1\|0}` | Turn a device on or off. `devType` matches the data key (`"light"`, `"blower"`, `"fan"`, `"heater"`, `"outlet"`, etc.) |
| `setDevActive` | `{}` | Activate device (post-provisioning) |
| `setDevDeactive` | `{}` | Deactivate device |
| `setDevReset` | `{}` | Factory reset |
| `setDevTimezone` | `{"timezone": "<tz>", "tzoff": <offset_s>}` | Set device timezone |
| `setRoom` | `{"roomId": "<id>"}` | Assign device to room |
| `setLocation` | `{"location": "<name>"}` | Set location label |
| `setRunDays` | `{"runDays": <n>}` | Set grow-days counter |
| `setScreen` | `{"on": 1\|0}` | Toggle display screen |
| `setBuzz` | `{"on": 1\|0}` | Toggle audible alarm buzzer |
| `setEmail` | `{"email": "<addr>"}` | Set notification email |
| `setWiFi` / `setWifi` | `{"ssid": "<ssid>", "pwd": "<pass>"}` | Provision WiFi credentials |

### Light control
| Method | `data` shape | Description |
|--------|-------------|-------------|
| `setDevSta` | `{"light": {"on": 1\|0, "level": 0–100}}` | Set primary light on/off and brightness (0–100 %) |
| `setDevSta` | `{"light2": {"level": 0–100}}` | Set secondary light level |
| `setLight` | `{"on": 1\|0, "level": 0–100}` | Dedicated light command (exact shape TBD) |
| `setLhtCtl` | `{...}` | Light schedule / plan control |
| `setHldMod` | `{"on": 1\|0}` | Hold / manual-override mode |
| `setPlant` | `{...}` | Set active planting plan |
| `setPlantData` | `{...}` | Update plant plan data |
| `setPlantName` | `{"name": "<name>"}` | Rename plant plan |

### Fan / blower / heater
| Method | `data` shape | Description |
|--------|-------------|-------------|
| `setDevSta` | `{"fan": {"on": 1\|0, "level": 0–10}}` | Fan speed (1–10) |
| `setDevSta` | `{"blower": {"on": 1\|0, "level": 0–100, "modeType": 0\|2}}` | Blower speed + mode |
| `setDevSta` | `{"heater": {"on": 1\|0, "level": 0–10, "modeType": 0\|3}}` | Heater level + mode |
| `setFan` | `{...}` | Dedicated fan command |
| `setBlower` | `{...}` | Dedicated blower command |
| `setMode` | `{"devType": "<key>", "modeType": <int>}` | Change operating mode |

**`modeType` values (blower/heater):**

| Value | Meaning |
|-------|---------|
| `0` | Manual |
| `2` | Auto (humidity + temp both trigger — blower) |
| `3` | Temp-only (heater) |

### Environment / climate
| Method | `data` shape | Description |
|--------|-------------|-------------|
| `setTemp` | `{"target": <float>, "deadband": <float>}` | Temperature setpoint |
| `setHumi` | `{"target": <float>}` | Humidity setpoint |
| `setCo2` | `{"target": <int>, "deadband": <int>}` | CO₂ setpoint (ppm) |
| `setRange` | `{...}` | Set environment alarm range |
| `setTempUnit` | `{"unit": "C"\|"F"}` | Toggle temperature unit |
| `setSensorHeating` | `{"on": 1\|0}` | Enable sensor heating element |
| `setCustAD` | `{...}` | Custom alert/deadband config |

### Outlets / power strips
| Method | `data` shape | Description |
|--------|-------------|-------------|
| `setOutlet` | `{"index": <n>, "on": 1\|0}` | Control individual outlet |
| `setPS5` | `{...}` | PS5 power strip command |
| `setPS10` | `{...}` | PS10 power strip command |

### Irrigation / spray / drip
| Method | `data` shape | Description |
|--------|-------------|-------------|
| `setSpray` | `{"on": 1\|0, "mode": <int>}` | Spray/misting control |
| `setWtrPump` | `{"on": 1\|0}` | Water pump on/off |
| `setWtrSlt` | `{...}` | Water slot / schedule config |
| `setNutr` | `{"ec": <float>, "ph": <float>}` | Nutrient EC/pH targets |

### Configuration persistence
| Method | `data` shape | Description |
|--------|-------------|-------------|
| `setConfigFile` | `{...}` | Write full config blob |
| `setConfigField` | `{"field": "<name>", "value": <any>}` | Write single config field |

---

## `getDevSta` — Data Field Dictionary

The `data` object returned in a `getDevSta` message contains sub-objects
keyed by device/sensor type. Only keys present in firmware are included.

### `sensor` — Environmental sensor
| Key | Type | Description |
|-----|------|-------------|
| `temp` | float | Air temperature (°C or °F per `tempUnit`) |
| `humi` | float | Relative humidity (%) |
| `vpd` | float | Vapour pressure deficit (kPa) |
| `ppfd` | float | Photosynthetic photon flux density (µmol/m²/s) |
| `co2` | int | CO₂ concentration (ppm) |
| `isDaySensor` | 0\|1 | 1 = currently day period |
| `tempOffset` | float | Calibration offset for temperature |
| `humiOffset` | float | Calibration offset for humidity |
| `co2Offset` | int | Calibration offset for CO₂ |

### `soilSensor` — Soil probe
| Key | Type | Description |
|-----|------|-------------|
| `tempSoil` | float | Substrate temperature |
| `humiSoil` | float | Substrate moisture content (%) |
| `ecSoil` | float | Substrate EC (mS/cm) |
| `soilType` | string | `claySoil` \| `peatSoil` (calibration profile) |

### `light` — Primary light
| Key | Type | Description |
|-----|------|-------------|
| `on` | 0\|1 | Power state |
| `level` | 0–100 | Brightness % |
| `lightTemp` | float | Light-reported temp (some models) |
| `lightTempAlarm` | 0\|1 | Over-temperature alarm |

### `light2` — Secondary / side light
| Key | Type | Description |
|-----|------|-------------|
| `level` | 0–100 | Brightness % (no separate `on` key — level 0 = off) |

### `fan` — Inline fan
| Key | Type | Description |
|-----|------|-------------|
| `on` | 0\|1 | Power state |
| `level` | 0–10 | Speed step (1–10) |

### `blower` — Exhaust / inline blower
| Key | Type | Description |
|-----|------|-------------|
| `on` | 0\|1 | Power state |
| `level` | 0–100 | Speed % |
| `modeType` | int | 0=manual, 2=auto |

### `heater` — Heater
| Key | Type | Description |
|-----|------|-------------|
| `on` | 0\|1 | Power state |
| `level` | 0–10 | Heat level |
| `modeType` | int | 0=manual, 3=temp-controlled |

### `dehumidifier`
| Key | Type | Description |
|-----|------|-------------|
| `on` | 0\|1 | Power state |
| `dehumiValue` | float | Current humidity reading |
| `dehumiWaterFull` | 0\|1 | Water tank full alarm |

### `humidifier`
| Key | Type | Description |
|-----|------|-------------|
| `on` | 0\|1 | Power state |
| `humidifierLacksWater` | 0\|1 | Low water alarm |

### `co2` — CO₂ controller
| Key | Type | Description |
|-----|------|-------------|
| `on` | 0\|1 | CO₂ injection active |
| `co2Target` | int | Setpoint (ppm) |
| `dayCo2` | int | Day target |
| `nightCo2` | int | Night target |
| `deadbandCo2` | int | Deadband |
| `co2Mode` | int | Operating mode |
| `co2Flag` | 0\|1 | Alarm flag |

### `spray` / `drip` — Irrigation
| Key | Type | Description |
|-----|------|-------------|
| `on` | 0\|1 | Active state |
| `sprayMode` | int | Operating mode |

### `waterPump`
| Key | Type | Description |
|-----|------|-------------|
| `on` | 0\|1 | Pump running |
| `waterLeak` | 0\|1 | Leak detected |
| `lowWater` | 0\|1 | Low water alarm |

### `outlet` — Smart outlet / power strip
| Key | Type | Description |
|-----|------|-------------|
| `on` | 0\|1 | Socket state |
| `modeType` | int | 0=manual, other=auto |

### `plan` — Grow plan
| Key | Type | Description |
|-----|------|-------------|
| `isPlanRun` | 0\|1 | Plan is currently running |
| `planProgress` | 0–100 | Plan completion % |
| `planRemainDays` | int | Days remaining |
| `plantedDays` | int | Days elapsed |
| `planedTotalDays` | int | Total plan duration |
| `plantingStage` | string | Current stage name |
| `stageIndex` | int | Stage index |

---

## `getSysSta` — System Status Fields

Inside `data.sys`:

| Key | Type | Description |
|-----|------|-------------|
| `upTime` | int | Uptime (seconds) |
| `mem` | int | Free memory (KB) |

Inside `data.sys.wifi`:

| Key | Type | Description |
|-----|------|-------------|
| `isConnect` | 0\|1 | WiFi connected |
| `rssi` | int | Signal strength (dBm) |
| `wifiName` | string | Connected SSID |

Inside `data.sys.mqtt`:

| Key | Type | Description |
|-----|------|-------------|
| `isConnect` | 0\|1 | MQTT broker connected |

Inside `data.sys.eth`:

| Key | Type | Description |
|-----|------|-------------|
| `isConnect` | 0\|1 | Ethernet connected |

Inside `data.sys.bluetooth`:

| Key | Type | Description |
|-----|------|-------------|
| `isConnect` | 0\|1 | BLE connected |

---

## Alarm Codes

Alarm events arrive as `getAlarmLog` messages. Field `alarmType` values observed:

| Key observed | Description |
|-------------|-------------|
| `lightOffline` | Light lost communication |
| `fanOffline` | Fan lost communication |
| `blowerOffline` | Blower lost communication |
| `heaterOffline` | Heater lost communication |
| `dehumiOffline` | Dehumidifier offline |
| `humiOffline` | Humidifier offline |
| `lightTempAlarm` | Light over-temperature |
| `tempAlarm` | Air temperature out of range |
| `humiAlarm` | Humidity out of range |
| `co2Alarm` | CO₂ out of range |
| `ppfdAlarm` | PPFD out of range |
| `vpdAlarm` | VPD out of range |
| `humiSoilAlarm` | Soil moisture out of range |
| `tempSoilAlarm` | Soil temperature out of range |
| `waterLeak` | Water leak detected |
| `lowWater` | Low water level |
| `dehumidifierWaterMaxAlarm` | Dehumidifier tank full |
| `humidifierWaterMinAlarm` | Humidifier low water |
| `deviceOffline` | Controller offline (LWT) |
