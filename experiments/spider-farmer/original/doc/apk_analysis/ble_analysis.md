# BLE Analysis — Spider Farmer GGS

**Status: Confirmed.** Cipher, packet framing, multiple KEY/IV pairs, and the full
connection flow have been verified across four independent implementations and
live firmware dumps.

---

## BLE Service & Characteristics

All UUIDs use the standard Bluetooth base UUID:
`xxxxxxxx-0000-1000-8000-00805f9b34fb`

| UUID | Role | Direction |
|------|------|-----------|
| `000000ff-0000-1000-8000-00805f9b34fb` | Service | — |
| `0000ff01-0000-1000-8000-00805f9b34fb` | **Notify** (CCCD enabled) | Device → App |
| `0000ff02-0000-1000-8000-00805f9b34fb` | **Write** (write-with-response) | App → Device |

> **Correction from earlier analysis:** The old document had ff01 and ff02 roles
> swapped. All four implementations confirm ff01=Notify, ff02=Write.

---

## Advertising / Device Name

BLE device names follow the pattern `SF-GGS-<TYPE>-<MAC_SUFFIX>`:

| Product | Advertising Name Example |
|---------|--------------------------|
| Grow Box Controller | `SF-GGS-CB-80F1B2B423C8` |
| Power Strip 5 | `SF-GGS-PS5-XXXXXXXXXXXX` |
| Power Strip 10 | `SF-GGS-PS10-XXXXXXXXXXXX` |
| LED Lamp | `SF-GGS-LC-XXXXXXXXXXXX` (or similar) |

The type suffix (`CB`, `PS5`, `PS10`, `LC`, …) is used by the app to select the
correct KEY/IV pair for that device category.

---

## Encryption

### Cipher

**AES-128 CBC, no padding (zero-padded plaintext to 16-byte boundary).**

- Library in app: **PointyCastle** (Dart) — confirmed by algorithm registry strings
  (`AES/`, `OFB-64`, `CBC_CMAC`, `/CBC`, `/CTR`, etc.) in `libapp.so`. These
  strings are PointyCastle's internal algorithm name registry entries and do not
  identify the mode actually used by the SF BLE code.
- Library on device: **mbedtls** (ESP32 / Arduino builds) or **PSA Crypto API**
  (ESPHome builds).
- Confirmed cipher: AES-128 **CBC** with no padding (plaintext zero-padded to
  the nearest 16-byte block boundary before encryption).

> **Correction from earlier analysis:** The earlier document suggested OFB or CTR
> mode based on the PointyCastle registry strings. All working implementations
> use CBC.

### Per-Device-Type Hardcoded KEY/IV Pairs

Each device type has a unique, hardcoded KEY+IV baked into the firmware. Keys
are NOT stored in NVS (verified by NVS dump after bonding — only `benutzeremail`
and `uid` appear there). The app contains all known pairs; the advertising name
selects which pair to use.

**Confirmed working pairs:**

| Device Type | KEY | IV | Source |
|-------------|-----|----|--------|
| CB Controller (FW 3.14) | `iVi6D24KxbrvXUuO` | `RnWokNEvKW6LcWJg` | Live HA BLE log decryption (April 2026) — brute-forced from APK candidate list against captured ciphertext |
| LED Lamp (FW ≥ 1.7) | `BkJu61kLt3afuogT` | `2AKVNUbU4mvU3Elt` | [REDACTED:maintainer-handle:SF-IMPL-2] firmware dump + [REDACTED:maintainer-handle:SF-IMPL-1] confirmation |
| Power Strip 10 (FW 3.14) | `lVIlATSlxaS1btfd` | `84Rf7SUkinfvxNlc` | [REDACTED:maintainer-handle:SF-IMPL-1] live decryption confirmed |

**Note:** LED lamps with FW < 1.7 used unencrypted BLE (msgtype 0x0001).
Encryption was introduced in FW 1.7.

**Full candidate list extracted from APK (`libapp.so`) by [REDACTED:maintainer-handle:SF-IMPL-1]:**

```
BkJu61kLt3afuogT   ← confirmed LED KEY
2AKVNUbU4mvU3Elt   ← confirmed LED IV
h411AfTnVVusvsjE
2pci13UbdjPR1ble
75YdgtITdMfiyS5x
84Rf7SUkinfvxNlc   ← confirmed PS10 IV
FIUz0N1xrmaaso61
J4G0M9dX1f1v3fXr   ← wrong CB candidate (APK static analysis — does not decrypt)
RnWokNEvKW6LcWJg
br3MSw3YDM0gRdEP
iVi6D24KxbrvXUuO
lVIlATSlxaS1btfd   ← confirmed PS10 KEY
mKli62mtym9j6Odi
v04Y436txRWeHd6w
```

**CB controller (SF-GGS-CB) key status:** Confirmed. `iVi6D24KxbrvXUuO` / `RnWokNEvKW6LcWJg`
verified by decrypting captured live BLE packets from a SF-GGS-CB running FW 3.14
(April 2026). The APK candidate `J4G0M9dX1f1v3fXr` was wrong. The correct pair was
found by trying all 14×14 permutations from the APK candidate list.

---

## Packet Framing

Packets are used for both app→device commands and device→app responses/events.
Large payloads are split into multiple fragments, each carrying its own header.

### Wire Format (per fragment)

```
Offset  Size  Field
------  ----  -----
0       2     Magic: 0xAA 0xAA
2       2     Flags: 0x00 0x03  (constant in all observed packets)
4       2     outer_payload_len (big-endian) = inner_header_size(14) + block_data_size
              NOTE: does NOT include the 2-byte footer CRC
6      14     Inner header (see below)
20      N     Encrypted block data (N = block_size from inner header)
20+N    2     Footer CRC16-Modbus over entire packet including header
```

### Inner Header (14 bytes, big-endian)

```
Offset  Size  Field
------  ----  -----
0       2     msgtype: 0x0001=plaintext, 0x0002=AES-encrypted
2       2     block_crc: CRC16-Modbus of this block's data
4       4     total_payload_size: total encrypted bytes across ALL fragments
8       4     block_offset: byte offset of this block within the reassembled payload
12      2     block_size: number of encrypted bytes in this fragment (= N above)
```

### CRC16-Modbus

Polynomial `0xA001`, init `0xFFFF`. Computed over the entire packet bytes 0...(20+N+1),
i.e. including all headers and encrypted data. Both the per-block CRC in the inner
header and the footer CRC use this algorithm.

### Example — 560-byte payload in two fragments

```
Fragment 1: [AAAA][0003][0196][0002][e92f][00000230][00000000][0190] [400B data] [2B CRC]
            outer_payload_len = 0x0196 = 14+400 = 414

Fragment 2: [AAAA][0003][00AC][0002][xxxx][00000230][00000190][00A0] [160B data] [2B CRC]
            outer_payload_len = 0x00AC = 14+160 = 174
```

> **Important:** outer_payload_len (bytes 4-5) does NOT include the 2-byte footer
> CRC. The actual stream byte count per fragment is `6 + outer_payload_len + 2`.
> Parsers that compute `total_len = 6 + outer_payload_len` will leave 2 CRC bytes
> in the stream on every packet. The HA BLE coordinator (`coordinator.py`) has this
> bug — evidenced by repeated "Discarding 2 junk bytes before header" log entries.

---

## IV Strategy

Two IVs are used:

| IV type | When used | How derived |
|---------|-----------|-------------|
| **Static IV** | App → device commands (outgoing requests) | Hardcoded per device type (same value as the "IV" column in the KEY/IV table above) |
| **Dynamic IV** | Device → app responses and unsolicited events | 14 bytes of inner header (bytes 6–19 of raw packet) + `0x00 0x00` padding → 16 bytes |

**Dynamic IV extraction (reference):**
```python
dynamic_iv = bytearray(raw_packet[6:20])  # 14 inner header bytes
dynamic_iv.extend(b'\x00\x00')            # pad to 16 bytes
iv = bytes(dynamic_iv)
```

This matches [REDACTED:repo-path:SF-IMPL-2] `main.cpp`:
```c
memcpy(dynamic_iv, rxBuffer.data() + 6, 14);
dynamic_iv[14] = 0x00;
dynamic_iv[15] = 0x00;
```

> **Note:** The HA BLE component uses `raw_packet[6:22]` (16 bytes starting at
> offset 6), which includes 14 inner-header bytes PLUS the first 2 bytes of the
> encrypted data — not 14 bytes + two zeros. This is a divergence from the
> reference implementations.

---

## Connection / Activation Flow

All implementations follow the same sequence (mirrors `runActivationFlow` in
`main.cpp`):

```
1. BLE connect
2. getSysSta   → confirms link is live; device responds with system status
3. setDevTimezone  → sync time
4. setDevActive    → bind/activate (sends uid + uname)
5. Periodic getDevSta every ~30 s
6. Unsolicited device→app event packets decoded and merged into sensor data
```

`setDevActive` is sent only once per session. The `_activated`/`isBounded` flag
persists across reconnects so the activation flow is not repeated.

---

## BLE Payload Format (JSON)

All commands use the same envelope:

```json
{
  "method": "getSysSta",
  "params": {},
  "msgId": "1745678901234",
  "uid": "1000000"
}
```

- `msgId`: 13-digit millisecond epoch timestamp (used for request/response matching)
- `uid`: user ID string (default `"1000000"` in non-cloud mode)

**Known methods:**

| Method | Direction | Purpose |
|--------|-----------|---------|
| `getSysSta` | App→Dev | Get system status |
| `getDevSta` | App→Dev | Get full device status (all sensors) |
| `setDevTimezone` | App→Dev | Sync timezone & UTC time |
| `setDevActive` | App→Dev | Bind/activate device with uid+email |
| `setDevDeactive` | App→Dev | Unbind device |
| `setDevRestart` | App→Dev | Reboot device |
| `setDevReset` | App→Dev | Factory reset |
| `setDevRestore` | App→Dev | Restore defaults |
| `runUpgrade` | App→Dev | Start OTA firmware upgrade |
| `getOtaInfo` | App→Dev | Query OTA info |
| `getOtaVer` | App→Dev | Query OTA version |
| `setWifi` | App→Dev | Provision WiFi credentials |
| `setLight` | App→Dev | Set light level/schedule |
| `setFan` | App→Dev | Set fan level/mode |
| `setBlower` | App→Dev | Set blower level |

Device→app responses echo the same `msgId` for correlation.

---

## BLE vs MQTT

| Aspect | BLE | MQTT |
|--------|-----|------|
| Transport | Direct, local | Cloud relay (`sf.mqtt.spider-farmer.com:8333`) |
| Encryption | AES-128 CBC, hardcoded KEY/IV | TLS (client cert bundled in APK) |
| Provisioning | Yes (setWifi sends WiFi password **unencrypted** pre-pairing) | No |
| Local control | Yes | Requires DNS rewrite to local broker |
| Sensor data | getDevSta response | MQTT publish to `GGS/<TYPE>/<MAC>/status` |
| Command | Encrypted JSON via ff02 | MQTT publish to `GGS/<TYPE>/<MAC>/cmd` |

---

## HA BLE Component — Known Issues (from Log Analysis)

From `home-assistant_2026-04-19T18-17-56.602Z.log`:

1. ~~**Wrong KEY for CB controller.**~~ **Fixed.** The correct CB key/IV
   (`iVi6D24KxbrvXUuO` / `RnWokNEvKW6LcWJg`) was confirmed by live BLE
   decryption in April 2026 (see confirmed pairs table above).

2. **Footer CRC not consumed from buffer.** `coordinator.py` computes
   `total_len = OUTER_HEADER_SIZE + outer_payload_len` (= 6 + outer_payload_len),
   which does not include the 2-byte footer CRC. These 2 bytes remain in
   `self._buffer` and appear as "Discarding 2 junk bytes before header" on every
   packet. Fix: `total_len = OUTER_HEADER_SIZE + outer_payload_len + FOOTER_CRC_SIZE`.

3. **Dynamic IV off by 2 bytes.** `protocol.py` uses `raw_packet[6:22]`
   (= 14 inner-header bytes + first 2 ciphertext bytes) instead of
   `raw_packet[6:20] + b'\x00\x00'` as all reference implementations do.

---

## Python Decrypt Reference

```python
from Crypto.Cipher import AES

# Per-device KEY and IV (ASCII strings, 16 bytes each)
KEY = b'lVIlATSlxaS1btfd'  # PS10 — replace with device-appropriate key
IV  = b'84Rf7SUkinfvxNlc'  # PS10 static IV

HEADER_MARKER    = b'\xaa\xaa'
OUTER_HEADER_SIZE = 6
INNER_HEADER_SIZE = 14
FOOTER_CRC_SIZE   = 2

def parse_packet(raw: bytes) -> bytes | None:
    """Extract encrypted block from a single fragment."""
    if not raw.startswith(HEADER_MARKER):
        return None
    # Encrypted bytes are between total header and footer CRC
    return raw[OUTER_HEADER_SIZE + INNER_HEADER_SIZE : -FOOTER_CRC_SIZE]

def decrypt_static(ciphertext: bytes, key: bytes = KEY, iv: bytes = IV) -> str:
    """Decrypt a command response using the static IV."""
    data = bytearray(ciphertext)
    if len(data) % 16:
        data += b'\x00' * (16 - len(data) % 16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plain = cipher.decrypt(bytes(data)).decode('utf-8', errors='ignore').strip('\x00')
    start, end = plain.find('{'), plain.rfind('}')
    return plain[start:end+1] if start != -1 else ''

def decrypt_dynamic(raw_packet: bytes, key: bytes = KEY) -> str:
    """Decrypt a device→app event using the dynamic IV."""
    dynamic_iv = bytes(raw_packet[6:20]) + b'\x00\x00'  # 14 inner-header + 2 zeros
    ciphertext = parse_packet(raw_packet)
    if ciphertext is None:
        return ''
    return decrypt_static(ciphertext, key, dynamic_iv)
```

---

## protobuf (BLE Channel Layer)

The file `bledata.proto` bundled in the APK defines the **flutter_reactive_ble**
GATT abstraction layer — not the Spider Farmer application protocol itself.
It describes how the Dart BLE library serialises GATT read/write/notify operations
into a method-channel message. The Spider Farmer BLE payload is the `value` bytes
field inside `WriteCharacteristicRequest` / `CharacteristicValueInfo`.

```protobuf
message WriteCharacteristicRequest {
    CharacteristicAddress characteristic = 1;  // ff02 (Write)
    bytes value = 2;                           // encrypted SF packet
}

message CharacteristicValueInfo {
    CharacteristicAddress characteristic = 1;  // ff01 (Notify)
    bytes value = 2;                           // encrypted SF response
    GenericFailure failure = 3;
}
```
