# Spider Farmer APK Analysis — v2.3.0 / v2.4.0

**Source:** `Spider Farmer_2.3.0_APKPure.zip`, `Spider Farmer_2.4.0_APKPure.zip`  
**Package:** `com.sf.meizhi`  
**Framework:** Flutter (Dart, compiled to `libapp.so` — ARM64)  
**Extraction:** `unzip apk_zip_extracted/com.sf.meizhi.apk -d apk_extracted`; native lib from `config.arm64_v8a.apk`

Additional sources integrated:
- `esphome-spiderfarmer_ble-encrypt.zip` — ESPHome C++ component ([REDACTED:maintainer-handle:SF-IMPL-1])
- `[REDACTED:repo-path:SF-IMPL-2]-master.zip` — Arduino/ESP32 bridge ([REDACTED:maintainer-handle:SF-IMPL-2])
- `[REDACTED:repo-path:SF-IMPL-3]-main.zip` — Python + MQTT bridge
- `doc/spider_farmer_ble/` — Home Assistant BLE custom component
- `doc/discusson.md` — GitHub discussion (confirmed KEY/IV pairs)
- `doc/home-assistant_*.log` — Live HA BLE debug logs

---

## Documents

| File | Contents |
|------|----------|
| [infrastructure.md](infrastructure.md) | Cloud endpoints, MQTT broker, TLS certificates, Firebase |
| [mqtt_protocol.md](mqtt_protocol.md) | Topic structure, all methods, payload schema, field dictionary |
| [api_endpoints.md](api_endpoints.md) | All REST API endpoints extracted from `libapp.so` |
| [ble_analysis.md](ble_analysis.md) | BLE UUIDs, confirmed cipher (AES-128 CBC), all KEY/IV candidates, packet framing, IV strategy, known bugs |
| [implementations.md](implementations.md) | Cross-implementation comparison: commonalities, divergences, bugs, recommended fixes |

---

## Extraction Method

All findings were obtained by running `strings` and binary pattern searches against
`libapp.so` (the compiled Dart snapshot). Dart AOT compiles string literals directly into
the snapshot, so constant strings — including URL paths, JSON keys, MQTT method names,
and cipher parameters — are recoverable verbatim. No decompiler was required.

```
strings libapp.so | grep <pattern>
python3 binary_search.py   # regex + context window scans
```

No dynamic instrumentation was performed.
