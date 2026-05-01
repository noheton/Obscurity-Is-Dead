# BLE Implementation Comparison

Cross-reference of four independent implementations of the Spider Farmer BLE
protocol. All were developed by reverse-engineering the same Android APK and/or
firmware dumps, without access to official documentation.

---

## Implementations Covered

| # | Name | Language | Author | Use case |
|---|------|----------|--------|----------|
| 1 | `spiderfarmer_ble` (ESPHome) | C++ | [REDACTED:maintainer-handle:SF-IMPL-1] | ESPHome component for HA |
| 2 | [REDACTED:repo-path:SF-IMPL-2] | C++ / Arduino | [REDACTED:maintainer-handle:SF-IMPL-2] | ESP32 → MQTT bridge |
| 3 | [REDACTED:repo-path:SF-IMPL-3] | Python | noheton/community | Standalone Python + MQTT |
| 4 | `spider_farmer_ble` (HA BLE) | Python | noheton | HA custom component (BLE) |

Source files:
- `doc/esphome-spiderfarmer_ble-encrypt.zip` → `components/spiderfarmer_ble/`
- `doc/[REDACTED:repo-path:SF-IMPL-2]-master.zip` → `src/main.cpp`, `BLEProtocol.h`, `BLEProtocol_v1.h`
- `doc/[REDACTED:repo-path:SF-IMPL-3]-main.zip` → `SpiderBLE/`
- `doc/spider_farmer_ble/` → `protocol.py`, `coordinator.py`, `sensor.py`

---

## Commonalities

All four implementations agree on:

| Aspect | Agreed Value |
|--------|-------------|
| Service UUID | `000000ff-0000-1000-8000-00805f9b34fb` |
| Notify UUID (device→app) | `0000ff01-0000-1000-8000-00805f9b34fb` |
| Write UUID (app→device) | `0000ff02-0000-1000-8000-00805f9b34fb` |
| Cipher | AES-128 CBC |
| Packet magic | `0xAA 0xAA 0x00 0x03` |
| Outer header size | 6 bytes |
| Inner header size | 14 bytes |
| Footer CRC size | 2 bytes |
| CRC algorithm | CRC16-Modbus (poly `0xA001`, init `0xFFFF`) |
| Static IV usage | Static IV for app→device commands |
| Dynamic IV usage | Dynamic IV for device→app events |
| Dynamic IV source | Inner header bytes (raw packet [6:20]) |
| Connection flow | getSysSta → setDevTimezone → setDevActive → periodic getDevSta |
| Poll interval | ~30 s |
| JSON payload envelope | `{"method":"...","params":{},"msgId":"<13-digit-ms>","uid":"..."}` |
| Encryption history | FW < 1.7 plaintext (msgtype 0x0001); FW ≥ 1.7 encrypted (0x0002) |

---

## Divergences

### 1. Key & IV Configuration

| Impl | Approach |
|------|----------|
| ESPHome | `set_aes_key()` / `set_aes_iv()` called from YAML config; validated at setup |
| [REDACTED:repo-path:SF-IMPL-2] | `SECRET_AES_KEY` / `SECRET_AES_IV` from `arduino_secrets.h` (compile-time) |
| [REDACTED:repo-path:SF-IMPL-3] | Per-device config in `devices.json`; runtime-loaded; supports multi-device |
| HA BLE | HA `config_flow` UI; stored in HA config entry; single device per entry |

### 2. Dynamic IV Derivation

All use 14 bytes from inner header + 2 padding bytes. The padding differs:

| Impl | Dynamic IV construction |
|------|------------------------|
| [REDACTED:repo-path:SF-IMPL-2] | `memcpy(iv, buf+6, 14); iv[14]=0x00; iv[15]=0x00;` |
| [REDACTED:repo-path:SF-IMPL-3] | `bytearray(packet[6:20]) + b'\x00\x00'` |
| ESPHome | Bytes 6–19 of raw packet (14 B) + two zero bytes (confirmed in comments) |
| HA BLE | `raw_packet[6 : 6+16]` = bytes 6–21 (14 inner-header + **first 2 ciphertext bytes**) |

**HA BLE divergence:** the HA component reads 16 consecutive bytes starting at
offset 6, which includes the first 2 bytes of the encrypted payload block — not
two zero bytes. This produces a different dynamic IV than all other implementations.

### 3. Plaintext Padding (before encryption)

| Impl | Padding scheme |
|------|---------------|
| [REDACTED:repo-path:SF-IMPL-2] v1 (`BLEProtocol_v1.h`) | PKCS7 (byte value = pad length) |
| [REDACTED:repo-path:SF-IMPL-2] final (`BLEProtocol.h`) | Zero bytes to next 16-byte boundary |
| [REDACTED:repo-path:SF-IMPL-3] | Zero bytes (skipped if already aligned) |
| HA BLE | Zero bytes (skipped if already aligned) |
| ESPHome | `PSA_ALG_CBC_NO_PADDING` — caller must pre-pad |

All final/current versions use zero-padding, not PKCS7. PKCS7 appeared only in
an intermediate [REDACTED:repo-path:SF-IMPL-2] prototype.

### 4. Fragment Reassembly

| Impl | Approach |
|------|----------|
| HA BLE | Stream buffer in `coordinator.py`; `_drain_buffer()` scans for magic, reads
outer_payload_len, reassembles fragment; each fragment decrypted independently |
| [REDACTED:repo-path:SF-IMPL-3] | Inline buffer accumulation within `send_with_retry()`; no explicit fragment merging — decrypts each fragment independently |
| [REDACTED:repo-path:SF-IMPL-2] | Fixed `rxBuffer`; accumulates BLE notification chunks; parses full packet when size known |
| ESPHome | Native GATT notification callback; handled at ESP-IDF level; each notification is one BLE MTU chunk |

### 5. Footer CRC Handling

| Impl | CRC consumed from stream? |
|------|--------------------------|
| [REDACTED:repo-path:SF-IMPL-2] | Yes — total_len includes footer CRC |
| [REDACTED:repo-path:SF-IMPL-3] | Yes — `total_size = payload_len + 8` (6 outer + 2 CRC) |
| HA BLE | **No** — `total_len = OUTER_HEADER_SIZE + outer_payload_len` excludes footer CRC |
| ESPHome | Handled by GATT layer (not a stream buffer) |

The HA BLE coordinator leaves 2 footer-CRC bytes in `self._buffer` after every
packet. These appear as "Discarding 2 junk bytes before header" in debug logs.

**Fix for `coordinator.py`:**
```python
# Current (buggy):
total_len = OUTER_HEADER_SIZE + outer_payload_len
# Fixed:
total_len = OUTER_HEADER_SIZE + outer_payload_len + FOOTER_CRC_SIZE
```

### 6. msgId / Response Correlation

| Impl | Strategy |
|------|----------|
| [REDACTED:repo-path:SF-IMPL-2] | No correlation — fire-and-wait with fixed timeout |
| [REDACTED:repo-path:SF-IMPL-3] | Stores `last_sent_id` from outgoing JSON; matches against `msgId` in received JSON |
| HA BLE | Stores `_pending_msg_id = str(int(time.time() * 1000))` independently of the actual msgId embedded in the packet; asyncio.Event for wakeup |
| ESPHome | No correlation — uses PollingComponent update cycle |

**HA BLE potential issue:** The `_make()` helper generates a fresh `time.time()*1000`
for `msg_id` tracking that may differ from the `msgId` embedded in the encrypted
packet (which was generated slightly earlier). If the device echoes the packet's
embedded `msgId` in its response, the match `msg_id == self._pending_msg_id` may
fail. The practical impact is low because responses typically arrive within the
timeout window, but a more robust approach would decrypt the outgoing packet to
extract its actual `msgId`.

### 7. Activation Flow Order

| Impl | Step sequence |
|------|---------------|
| [REDACTED:repo-path:SF-IMPL-2] | getSysSta → setDevTimezone → setDevActive |
| [REDACTED:repo-path:SF-IMPL-3] | **getDevSta** → setDevTimezone → setDevActive *(differs!)* |
| HA BLE | getSysSta → setDevTimezone → setDevActive |
| ESPHome | getSysSta → setDevTimezone → setDevActive |

[REDACTED:repo-path:SF-IMPL-3] starts with `getDevSta` instead of `getSysSta`. Both
appear to work in practice; `getSysSta` is used by the majority.

### 8. Sensor / Data Coverage

| Sensor | ESPHome | [REDACTED:repo-path:SF-IMPL-2] | [REDACTED:repo-path:SF-IMPL-3] | HA BLE |
|--------|---------|-----------------|------------------------|--------|
| Temperature | ✓ | MQTT only | MQTT only | ✓ |
| Humidity | ✓ | MQTT only | MQTT only | ✓ |
| VPD | ✓ | MQTT only | MQTT only | ✓ |
| CO2 | ✓ | MQTT only | MQTT only | ✓ |
| PPFD | ✓ | MQTT only | MQTT only | ✓ |
| Soil temp/humi/EC | ✓ | MQTT only | MQTT only | ✓ |
| Light level | ✓ | MQTT only | MQTT only | ✓ |
| Fan level | ✓ | MQTT only | MQTT only | ✓ |
| Blower level | ✓ | MQTT only | MQTT only | ✓ |
| Power outlets (1–10) | ✓ (binary) | MQTT only | MQTT only | ✗ |
| Fan natural mode | ✓ | MQTT only | MQTT only | ✗ |
| Device ID / FW / HW | ✓ (text sensor) | MQTT only | MQTT only | ✗ |

### 9. Write (Control) Support

| Impl | Write commands implemented |
|------|---------------------------|
| ESPHome | Partial — outlet switch being added (per [REDACTED:maintainer-handle:SF-IMPL-1]) |
| [REDACTED:repo-path:SF-IMPL-2] | Only heartbeat/keep-alive; no control |
| [REDACTED:repo-path:SF-IMPL-3] | Framework ready (`setLight`, `setFan`, etc. in BLEPayloads); not wired |
| HA BLE | None — read-only at time of log capture |

---

## Key Finding: CB Controller Key Confirmed

Live HA logs (2026-04-25) confirm the correct SF-GGS-CB key/IV pair is
`iVi6D24KxbrvXUuO` / `RnWokNEvKW6LcWJg`. All 14×14 permutations were tried
against captured ciphertext (getDevSta and getSysSta packets from a CB running
FW 3.14); only this pair produces valid JSON. The LED pair and the previously
assumed candidate `J4G0M9dX1f1v3fXr` both fail.

**The script used to find the key (for reference):**

```python
from Crypto.Cipher import AES
import itertools

CANDIDATES = [
    b'BkJu61kLt3afuogT', b'2AKVNUbU4mvU3Elt', b'h411AfTnVVusvsjE',
    b'2pci13UbdjPR1ble', b'75YdgtITdMfiyS5x', b'84Rf7SUkinfvxNlc',
    b'FIUz0N1xrmaaso61', b'J4G0M9dX1f1v3fXr', b'RnWokNEvKW6LcWJg',
    b'br3MSw3YDM0gRdEP', b'iVi6D24KxbrvXUuO', b'lVIlATSlxaS1btfd',
    b'mKli62mtym9j6Odi', b'v04Y436txRWeHd6w',
]

# Replace with actual ciphertext from a captured getSysSta response
CIPHERTEXT = bytes.fromhex('...')

for key, iv in itertools.product(CANDIDATES, CANDIDATES):
    if key == iv:
        continue
    try:
        data = bytearray(CIPHERTEXT)
        if len(data) % 16:
            data += b'\x00' * (16 - len(data) % 16)
        plain = AES.new(key, AES.MODE_CBC, iv).decrypt(bytes(data))
        text = plain.decode('utf-8', errors='ignore').strip('\x00')
        if '{' in text and 'method' in text:
            print(f"KEY={key.decode()} IV={iv.decode()}: {text[:80]}")
    except Exception:
        pass
```

---

## Recommended Fixes for `doc/spider_farmer_ble/`

1. **`coordinator.py`** — add `FOOTER_CRC_SIZE` to `total_len`:
   ```python
   total_len = OUTER_HEADER_SIZE + outer_payload_len + FOOTER_CRC_SIZE
   ```

2. **`protocol.py`** — fix dynamic IV to use 14 inner-header bytes + two zeros:
   ```python
   dynamic_iv = raw_packet[IV_OFFSET_IN_PACKET:IV_OFFSET_IN_PACKET + 14] + b'\x00\x00'
   ```
   (Currently uses `raw_packet[6:22]` which incorrectly includes 2 ciphertext bytes.)

3. **`const.py`** — change `IV_LENGTH = 16` sentinel to `14` (or rename to
   `IV_HEADER_BYTES = 14`) to reflect actual inner-header span, and use the
   correct derivation in `protocol.py`.

4. **Key selection** — allow per-device KEY/IV in config flow; the current default
   is the LED key, which is wrong for CB controllers.
