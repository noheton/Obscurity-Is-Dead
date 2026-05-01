# Spider Farmer GGS-CB – Full Protocol Reference

> **Sources:** live MQTT captures · BLE reverse engineering (cr0ssn0tice) ·
> ESPHome component (smurfy) · schedule-4-real (EddiePiazza) ·
> Spider Farmer product manuals · `tools/mqtt_discover.py` probe sessions

---

## 1. Transport

| Parameter | Value |
|:---|:---|
| Broker (real) | `sf.mqtt.spider-farmer.com:8333` (MQTTS / TLS) |
| Broker (local intercept) | local EMQX, plain TCP 1883 |
| Status topic (device → broker) | `SF/GGS/CB/API/UP/{PID}` |
| Command topic (broker → device) | **unknown — see §4** |
| Username | `sf_ggs_cb` |
| Password | `euuavURS4Kp9bMUfYmvwl-` |

### Local intercept setup
Point `sf.mqtt.spider-farmer.com` to the local broker via DNS rewrite.
The broker must present `ca-sf.pem` + `emqx-sf.pem` + `emqx-sf.key`
(extracted from APK) to the device during TLS handshake.

### ⚠️ Critical finding — wrong command topic (phase-2 result)

Phase-2 probes sent every known command method (`setOnOff`, `setMode`,
`setDevSta`, `setLevel`) to `SF/GGS/CB/API/UP/{PID}` and **zero state
changes were observed** across 15 probes and ~55 seconds of `getDevSta`
monitoring. Every "response" in the probe log arrived within ~5 ms —
that is the broker echoing our own publish back to us (we subscribe to the
same topic), not a device acknowledgment.

**Conclusion:** `UP/{PID}` is uplink only (device→broker). The device does
not subscribe to it for incoming commands. A separate **downlink topic** is
used for commands. Phase-3 must identify it.

The phase-1 blower state change (on=1→off) was coincidental with the
grow-plan schedule (modeType:2 auto mode), not caused by `setOnOff`.

---

## 2. Message Envelope

Every message (inbound and outbound) shares the same outer structure:

```json
{
  "method": "<method>",
  "pid":    "<MAC without colons, e.g. 80F1B2B3B648>",
  "pcode":  1004,
  "uid":    "<user ID from Spider Farmer account>",
  "UTC":    1776881745,
  "code":   200,
  "msg":    "ok",
  "data":   { ... }
}
```

- `UTC` **must be the current Unix timestamp** on every outgoing command
  (replay protection — stale timestamps are silently rejected).
- `pcode` must be `1004`; omitting it causes silent rejection.
- `code` / `msg` appear on inbound messages only.

---

## 3. Inbound Messages (device → broker)

### 3.1 `getDevSta` — Device Status

Published every **~6 s**. Contains the full real-time state of all devices.

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
    "light":  { "on": 1, "level": 35 },
    "light2": { "level": 0 },
    "blower": { "modeType": 2, "on": 1, "level": 30 },
    "fan":    { "on": 1, "level": 1 },
    "heater": { "modeType": 3, "on": 1, "level": 7 }
  }
}
```

**Field notes:**
- `on` is **absent** when a device is off — do not rely on `on: 0`; treat
  absent `on` as off.
- `level == 0` also implies off for devices without an `on` field.
- `light2` never has an `on` field; infer from `level > 0`.
- `modeType` may be absent when the device is off.
- `sensor.isDaySensor` can be absent briefly after a reboot.

#### Device field ranges

| Device | Field | Range | Notes |
|:---|:---|:---|:---|
| `light` | `level` | 0–100 | percentage |
| `light` | `on` | 0/1 | absent when off |
| `light2` | `level` | 0–100 | no `on` field |
| `fan` | `level` | 0–10 | steps |
| `fan` | `on` | 0/1 | absent when off |
| `blower` | `level` | 0–100 | percentage (not 0–10) |
| `blower` | `on` | 0/1 | absent when off |
| `blower` | `modeType` | see §5 | absent when off in some modes |
| `heater` | `level` | 0–10 | steps |
| `heater` | `on` | 0/1 | absent when off |
| `heater` | `modeType` | see §5 | |

### 3.2 `getSysSta` — System Status

Published every **~10 s**.

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
      "wifi":      { "isConnect": 1, "rssi": -80 },
      "eth":       { "isConnect": 0 },
      "mqtt":      { "isConnect": 1, "connectTime": 878 },
      "bluetooth": { "isConnect": 1, "connectTime": 872 }
    }
  }
}
```

- `bluetooth.connectTime` is absent when `isConnect: 0`.

---

## 4. Outbound Commands (client → device)

> ⚠️ **Command topic unknown.** All probe sessions published to
> `SF/GGS/CB/API/UP/{PID}` and produced **zero device state changes**.
> The responses seen were broker self-echoes, not device ACKs. The device
> subscribes to a separate downlink topic for commands — phase-3 probes
> are needed to find it (see §7).
>
> Everything below describes the **message shape** for each method, confirmed
> by observing what the SF app sends via the real broker. The shapes are
> correct; the topic is wrong.

### 4.1 `setOnOff` — Power on / off

```json
{ "method": "setOnOff", "pid": "…", "pcode": 1004, "uid": "…", "UTC": <now>,
  "data": { "devType": "light", "on": 1 } }
```

| `devType` | Device |
|:---|:---|
| `"light"` | Main light |
| `"blower"` | Inline fan / blower |
| `"fan"` | Clip fan |
| `"heater"` | Heater |

`on: 1` = on, `on: 0` = off. Semantics are **set** (not toggle), confirmed
by phase-2 message shape analysis.

### 4.2 `setMode` — Change operating mode

```json
{ "data": { "devType": "blower", "modeType": 0 } }   ← manual
{ "data": { "devType": "blower", "modeType": 2 } }   ← auto / grow-plan
{ "data": { "devType": "heater", "modeType": 3 } }   ← temperature
```

See §5 for full modeType tables.

### 4.3 `setDevSta` — Set device state (level)

Used for level / brightness changes. Whether it also controls on/off is
unconfirmed — prefer `setOnOff` for power state.

```json
{ "data": { "blower": { "modeType": 0, "on": 1, "level": 30 } } }
{ "data": { "light":  { "on": 1, "level": 50 } } }
```

### 4.4 `setLevel` — Set level only

Alternative to `setDevSta` for level-only changes. Shape confirmed by
phase-2 probes:

```json
{ "data": { "devType": "blower", "level": 50 } }
{ "data": { "devType": "light",  "level": 50 } }
```

Effectiveness vs. `setDevSta` is untested until command topic is resolved.

### 4.5 `getConfigFile` — Read schedule/config

```json
{ "method": "getConfigFile", "data": {} }
```

The device is expected to respond with the grow-plan config. All responses
observed so far were broker self-echoes with empty `data`; the real response
likely arrives on the command topic when the correct topic is used.

### 4.6 `setDevTimezone` — Time synchronisation

```json
{ "method": "setDevTimezone", "data": ["Europe/Berlin", 3600, <utc_epoch>] }
```

3-element array: `[IANA_timezone, utc_offset_seconds, current_utc_epoch]`.

### 4.7 `setConfigFile` — Write schedule  ❓ SHAPE UNKNOWN

Exact `data` shape not yet captured. Likely mirrors the `getConfigFile`
response payload.

---

## 5. modeType Reference

### 5.1 Blower (`blower.modeType`)

| modeType | Name | Status |
|:---:|:---|:---|
| 0 | Manual | ✅ used with `setMode devType:blower modeType:0` |
| 1 | Time Slot | ✅ inline fan manual: "Time Period Mode" |
| 2 | Auto / Grow Plan | ✅ most common; controller manages on/off by schedule |
| 7 | Environment (Temp+Humi) | ❓ non-sequential — may be a feature-flag composite |
| 8 | Temperature | ❓ non-sequential |
| 13 | VPD | ❓ non-sequential |

### 5.2 Heater (`heater.modeType`)

| modeType | Name | Status |
|:---:|:---|:---|
| 0 | Manual | ✅ fixed power level |
| 1 | Timer | ✅ heater manual: countdown timer mode |
| 2 | Cycle (Day/Night) | ✅ heater manual: sun/moon auto-switching |
| 3 | Temperature | ✅ thermostat — holds target temperature |

### 5.3 Light (`light.modeType`)

| modeType | Name | Status |
|:---:|:---|:---|
| *(absent)* | Schedule / Manual | ✅ normal operating state |
| 1 | Transition? | ❓ seen briefly during light switching |

---

## 6. BLE Protocol (firmware < 3.14 only)

> ⚠️ Firmware 3.14 adds encryption/obfuscation to BLE. BLE direct control
> is broken on 3.14+.

BLE uses per-device method names:

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

## 7. Open Questions and Phase-3 Plan

### Primary blocker: command topic

All probe sessions used `SF/GGS/CB/API/UP/{PID}` and produced **zero device
state changes**. The device publishes status on this topic but subscribes to
a different topic for commands.

**Phase-3 goal: find the command topic.**

#### Step 1 — Query EMQX admin API for device subscriptions

The local EMQX broker exposes an HTTP management API. This will directly
show which topics the device has subscribed to:

```bash
# List all connected clients (find the device client ID)
curl http://192.168.1.60:18083/api/v5/clients

# List subscriptions for the device client
curl http://192.168.1.60:18083/api/v5/clients/<clientid>/subscriptions
```

Default EMQX credentials: `admin` / `public`.

#### Step 2 — Subscribe to wildcard and observe

If the EMQX API is not accessible, subscribe to `#` to capture any topic
the device publishes to in response to commands (some devices publish an
ACK on their command topic):

```bash
python tools/mqtt_discover.py --pid <PID> --uid <UID> --broker <ip> --phase3
```

Phase-3 probes publish to candidate downlink topics and listen on `#`
for any response that did not come from us:

| Candidate topic | Rationale |
|:---|:---|
| `SF/GGS/CB/API/DOWN/{PID}` | Symmetric to UP — most common IoT pattern |
| `SF/GGS/CB/API/DN/{PID}` | Abbreviated variant |
| `SF/GGS/CB/API/SET/{PID}` | Seen in some EMQX-based platforms |
| `SF/GGS/CB/{PID}` | Shorter root topic |
| `SF/GGS/CB/API/UP/{PID}/cmd` | Sub-topic of UP |

#### Step 3 — Capture real app traffic

Connect the SF app to the real cloud broker (temporarily disable the DNS
intercept), run `tcpdump` or `mitmproxy` to capture the TLS stream, and
identify which topic the app publishes commands to.

### Secondary open questions

| Question | How to resolve |
|:---|:---|
| `getConfigFile` actual response shape | Once command topic found, send it and capture response |
| Blower modeType 7 / 8 / 13 names | Cycle modes in app while running `--listen` on `#` |
| Does `light2` accept commands? | `setOnOff devType:"light2" on:1` on the correct command topic |
| `setConfigFile` data shape | Likely mirrors `getConfigFile` response |
