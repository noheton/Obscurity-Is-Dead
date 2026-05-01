## SpiderFarmer SF-GGS-CB – MQTT Protocol Documentation

> Sources: live MQTT captures, BLE reverse engineering (cr0ssn0tice), ESPHome component (smurfy), schedule-4-real (EddiePiazza), Spider Farmer product manuals (GGS System, G-Series, Inline Fan, Clip Fan, Heater)

---

### 1. Connection

| Parameter | Value |
|:---|:---|
| Endpoint | `sf.mqtt.spider-farmer.com` |
| Port | `8333` (MQTTS / TLS) |
| Username | `sf_ggs_cb` |
| Password | `euuavURS4Kp9bMUfYmvwl-` |
| Topic | `SF/GGS/CB/API/UP/{PID}` (bidirectional) |

DNS rewrite required: point `sf.mqtt.spider-farmer.com` to local broker.  
Broker must present `ca-sf.pem` + `emqx-sf.pem` + `emqx-sf.key` (extracted from APK).

---

### 2. Message Envelope

Every message (inbound and outbound) shares the same outer structure:

```json
{
  "method": "<method>",
  "pid":    "<MAC address of controller, e.g. 80F1B2B3B648>",
  "pcode":  1004,
  "uid":    "<user ID from Spider Farmer account>",
  "UTC":    1776881745,
  "code":   200,
  "msg":    "ok",
  "data":   { ... }
}
```

- `UTC` **must be dynamic** on outgoing commands (replay protection).
- `pcode` must be `1004` – omitting it causes the device to silently reject commands.

---

### 3. Inbound Methods (device → broker)

#### 3.1 `getDevSta` – Device Status

Published every ~6 s. Contains the full state of all attached devices.

```json
{
  "method": "getDevSta",
  "data": {
    "alarmLast": { "id": 3, "epoch": 1776416472, "devType": 16, "alarmType": 3 },
    "oplogLast":  { "id": 1039, "epoch": 1776883501, "devType": 21, "opType": 1, "modeType": 2 },
    "plan": {
      "isPlanRun": 1, "stageId": 1776498625,
      "planedTotalDays": 5, "planedDays": 4,
      "planRemainDays": 1, "planProgress": 80
    },
    "sensor": {
      "temp": 20.8, "humi": 79.2, "vpd": 0.51,
      "isDayEnvTarget": 1, "isDaySensor": 1
    },
    "light":  { "on": 1, "level": 30 },
    "light2": { "level": 0 },
    "blower": { "modeType": 2, "on": 1, "level": 25 },
    "fan":    { "on": 1, "level": 3 },
    "heater": { "modeType": 3, "on": 1, "level": 7 }
  }
}
```

**Field notes:**
- `on` field is **absent** when a device is off (do not rely on `on: 0`; infer from `level == 0` instead).
- `light2` never has an `on` field; infer state from `level > 0`.
- `modeType` may be absent on some devices when off.
- `sensor.isDaySensor` can be absent during the first seconds after a controller reboot.

#### Device field ranges

| Device | Field | Range | Notes |
|:---|:---|:---|:---|
| `light` | `level` | 0 – 100 | percentage |
| `light` | `on` | 0 / 1 | absent when off |
| `light2` | `level` | 0 – 100 | no `on` field |
| `fan` | `level` | 0 – 10 | steps |
| `fan` | `on` | 0 / 1 | absent when off |
| `blower` | `level` | 0 – 100 | percentage (not 0–10!) |
| `blower` | `on` | 0 / 1 | absent when off |
| `blower` | `modeType` | see §5 | absent when off in some modes |
| `heater` | `level` | 0 – 10 | steps |
| `heater` | `on` | 0 / 1 | absent when off |
| `heater` | `modeType` | see §5 | |

#### 3.2 `getSysSta` – System Status

Published every ~10 s.

```json
{
  "method": "getSysSta",
  "data": {
    "sys": {
      "ver": "3.14", "hwcode": 1, "hwver": "2.7",
      "buildTime": "Jan 20 2026 14:21:28",
      "localtime": "2026-04-22 20:45:39 Wednesday CEST",
      "timezone": "Europe/Berlin",
      "upCount": 24, "upTime": 886, "mem": 1178,
      "UTC": 1776883539, "tzoff": 3600,
      "verUpdateNum": 45, "verUpdateTime": 1776882895,
      "wifi":      { "isConnect": 1, "rssi": -80 },
      "eth":       { "isConnect": 0 },
      "mqtt":      { "isConnect": 1, "connectTime": 878 },
      "bluetooth": { "isConnect": 1, "connectTime": 872 }
    }
  }
}
```

- `bluetooth.connectTime` may be absent when `isConnect: 0`.

---

### 4. Outbound Commands (broker → device)

Use method `setDevSta`. Only send the fields you want to change inside `data`.

#### Light on

```json
{ "method": "setDevSta", "pid": "…", "pcode": 1004, "uid": "…", "UTC": <now>,
  "data": { "light": { "on": 1, "level": 30 } } }
```

#### Light off

```json
{ "data": { "light": { "on": 0, "level": 0 } } }
```

#### Fan (level 0 – 10)

```json
{ "data": { "fan": { "on": 1, "level": 3 } } }
```

#### Blower – manual (level 0 – 100)

```json
{ "data": { "blower": { "modeType": 0, "on": 1, "level": 30 } } }
```

#### Blower – restore auto (grow-plan timer)

```json
{ "data": { "blower": { "modeType": 2, "on": 1, "level": 30 } } }
```

#### Heater – manual (level 0 – 10)

```json
{ "data": { "heater": { "modeType": 0, "on": 1, "level": 7 } } }
```

#### Heater – restore temperature mode

```json
{ "data": { "heater": { "modeType": 3, "on": 1, "level": 7 } } }
```

---

### 5. modeType Reference

> ⚠️ **Status: partially confirmed.** Values marked ✅ are confirmed by live captures or cross-referenced with multiple sources. Values marked ❓ are inferred – they need verification by switching modes in the app while recording MQTT.
>
> **To verify:** open the Spider Farmer app, change each mode on blower/heater one by one, and capture the resulting MQTT `getDevSta` message. The `modeType` value in the payload is the number for that mode.

#### 5.1 Blower (`blower.modeType`)

Observed values: `0, 1, 2, 7, 8, 13`

| modeType | Name | Status |
|:---:|:---|:---|
| 0 | Manual | ✅ (sent by HA for manual control) |
| 1 | Time Slot | ✅ inline fan manual lists "Time Period Mode" as second mode; matches briefly seen value |
| 2 | Auto / Grow Plan | ✅ most common; controller manages on/off by schedule |
| 7 | Environment (Temp+Humi) | ❓ seen when cycling modes in app; inline fan manual lists "Temperature First" and "Humidity First" as separate modes |
| 8 | Temperature | ❓ seen when cycling modes in app |
| 13 | VPD | ❓ seen when cycling modes in app; non-sequential numbers (7, 8, 13) suggest these may be feature-flag composites rather than simple indexes |

App mode list (from schedule-4-real reverse engineering): **Manual, Environment, Time Slot, Cycle, Trigger**.
Inline fan manual (SFInlineFanUserManual) lists 5 modes: **Manual, Time Period, Temperature First, Humidity First, Standby Speed** – exact numeric mapping for 7/8/13 needs verification by cycling each mode in the app while recording MQTT.

#### 5.2 Heater (`heater.modeType`)

Observed values: `0, 1, 2, 3`

| modeType | Name | Status |
|:---:|:---|:---|
| 0 | Manual | ✅ (sent by HA for manual control) |
| 1 | Timer | ✅ heater manual (SFHeaterUseManual03) shows a Timer button that activates countdown mode |
| 2 | Cycle (Day/Night) | ✅ heater manual shows Day mode (sun icon) / Night mode (moon icon) automatic switching |
| 3 | Temperature | ✅ most common; controller holds target temperature (thermostat mode) |

App mode list (from product docs): **Manual, Timer, Cycle, Temperature** – sequential 0–3 mapping confirmed by manual.

#### 5.3 Light (`light.modeType`)

Observed values: `1` (modeType absent = normal manual/schedule mode)

| modeType | Name | Status |
|:---:|:---|:---|
| *(absent)* | Schedule / Manual | ✅ normal operating state |
| 1 | Transition? | ❓ seen briefly during light switching; G-Series dimmer box has Manual/Auto/Linked modes – 1 may signal a mid-transition state |

App mode list: **Manual, Time Slot, PPFD Auto**
G-Series dimmer box modes (from GSeriesUserManual): **Manual** (direct knob), **Auto** (app schedule), **Linked** (daisy-chain follower).

---

### 6. BLE Protocol (firmware < 3.14 only)

> ⚠️ Firmware 3.14 adds encryption/obfuscation to BLE packets. BLE direct control is broken on 3.14+.

For firmware < 3.14, BLE uses separate method names per device:

```
setLight  → { "method": "setLight",  "data": { "modeType": 0, "on": 1, "level": 20 } }
setFan    → { "method": "setFan",    "data": { "on": 1, "level": 3 } }
setBlower → { "method": "setBlower", "data": { "modeType": 0, "on": 1, "level": 30 } }
```

BLE UUIDs:
| UUID | Role |
|:---|:---|
| `0000ff00-…` | Primary service |
| `0000ff01-…` | Notify (device → client) |
| `0000ff02-…` | Write (client → device) |

---

### 7. Open Questions

- Exact modeType → name mapping for blower modes 7, 8, 13 (non-sequential; may be composite feature flags)
- Exact modeType → name mapping for light mode 1 (seen briefly during switching)
- Does `light2` accept an `on` field in commands?
- Are there additional methods beyond `getDevSta` / `getSysSta` / `setDevSta`?

---

### 8. Reference Manuals

Stored in `doc/manuals/`:

| File | Device | Key info |
|:---|:---|:---|
| `GGSSystemUserManual.pdf` | GGS Controller, Power Strip | System overview, wiring |
| `GSeriesUserManual.pdf` | G-Series LED lights | Dimmer modes: Manual / Auto / Linked |
| `SFInlineFanUserManual.pdf` | Inline Fan (blower) | 5 modes: Manual, Time Period, Temp First, Humi First, Standby Speed |
| `ClipFanUserManual.pdf` | Clip Fan | 10 speed steps, Natural Breeze mode (no MQTT modeType) |
| `SFHeaterUseManual03.pdf` | Heater | 4 modes: Manual (0), Timer (1), Day/Night Cycle (2), Temperature (3) |
