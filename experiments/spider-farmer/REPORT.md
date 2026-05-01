# Spider Farmer Case Study Report

## 1. Overview
This report documents the analysis performed for the Spider Farmer case study. The goal was to understand how AI-assisted reverse engineering and artifact analysis enabled local interoperability with Spider Farmer BLE devices, while documenting the security risks exposed by the revealed protocol.

## 2. Case Study Scope
- Device family: Spider Farmer GGS controllers, power strips, lamps, and growers.
- Primary integration target: local Home Assistant BLE integration.
- Artifact sources: APK binaries for `Spider Farmer_2.3.0_APKPure.zip` and `Spider Farmer_2.4.0_APKPure.zip`, ESPHome and Arduino bridge implementations, and Home Assistant BLE integration logs.
- AI-assisted documentation: raw conversation exports in `raw_conversations (copy&paste, web)/`.

## 3. Artifact Inventory
- `original/doc/Spider Farmer_2.3.0_APKPure.zip`
- `original/doc/Spider Farmer_2.4.0_APKPure.zip`
- `original/doc/esphome-spiderfarmer_ble-encrypt.zip`
- `original/doc/SpiderBLEBridge-master.zip`
- `original/doc/PythonSpiderController-main.zip`
- `original/doc/home-assistant_spider_farmer_2026-04-26T11-31-51.573Z.log`
- `raw_conversations (copy&paste, web)/` (7 transcripts)
- Analysis notes in `original/doc/apk_analysis/`, including `ble_analysis.md`, `mqtt_protocol.md`, `api_endpoints.md`, and `implementations.md`.

## 4. Methodology
- Static APK extraction and string analysis from the Flutter/Arduino binaries.
- Comparative analysis across four independent implementations and recorded HA logs.
- Use of raw conversation transcripts to capture analysis decisions, corrections, and validation steps.
- Cross-checks between APK-derived constants and live BLE packet captures.

## 5. Key Findings
### 5.1 BLE Protocol and Encryption
- BLE uses service UUID `000000ff-0000-1000-8000-00805f9b34fb` with characteristics:
  - `0000ff01-0000-1000-8000-00805f9b34fb` — Notify
  - `0000ff02-0000-1000-8000-00805f9b34fb` — Write-with-response
- Encryption is AES-128 CBC with zero padding.
- Packet framing uses a two-stage header format with fragment-level CRC16-Modbus.
- Static outgoing IVs are hardcoded per device type; dynamic incoming IVs are derived from the packet header.

### 5.2 Hardcoded Keys and IVs
- A finite set of KEY/IV candidates was recovered from the APK.
- Confirmed working pairs for specific device types (e.g., CB controller, LED lamp, Power Strip 10).
- The device advertising name encodes the device type and selects the correct key material.

### 5.3 Protocol Behavior
- Core commands include `getSysSta`, `setDevTimezone`, `setDevActive`, `getDevSta`, and hardware control methods such as `setLight`, `setFan`, and `setBlower`.
- The application uses a `msgId` field to correlate requests and responses.
- Pages of raw logs show repeated BLE write failures and connection retries, indicating sensitive timing and resilience issues in the custom BLE stack.

### 5.4 AI-Assisted Corrections
- Analysis notes record early misinterpretation of BLE UUID roles and encryption modes.
- The final validated protocol logically corrected those errors to match working implementations.
- Raw conversation exports reflect an iterative discovery process: BLE connection support, decryption failure fixes, and command mapping.

## 6. Interoperability Impact
- The analysis enabled a local integration path for Spider Farmer devices outside of the vendor app.
- Local BLE integration can provide direct control and sensor reporting without cloud dependency.
- The work also exposes the protocol sufficiently to support alternative bridges such as ESPHome and custom MQTT relays.

## 7. Security Implications
- Hardcoded AES keys and IVs are a serious weakness: possession of the APK plus captured traffic enables decryption and command injection.
- The use of known static IVs for outgoing commands, combined with the packet structure, reduces confidentiality.
- The same analysis that enables interoperability also reveals that the vendor's BLE security is largely obscurity-based, not cryptographically robust.

## 8. Validation and Evidence
- Confirmed findings across four independent implementations.
- Verified key/IV pairs with live HA BLE logs and firmware dump analysis.
- Documented corrections and convergence in `original/doc/apk_analysis/ble_analysis.md`.
- Every claim is tied to either an APK artifact, implementation source, or protocol log.

## 9. Risks and Recommendations
- Do not treat BLE encryption as authentication. An attacker with local BLE access and APK artifacts can impersonate the user.
- Future work should focus on message authentication, per-device session keys, and stronger pairing.
- The local integration should be careful with command retries and timeouts due to observed BLE instability.

## 10. Next Steps
- Add a concrete provenance matrix mapping each raw transcript to analysis decisions and code changes.
- Document the specific `msgId` and JSON command formats in the paper as examples of protocol reverse engineering.
- If possible, capture a live BLE packet trace for a complete packet-by-packet reproduction of the encryption/decryption flow.
