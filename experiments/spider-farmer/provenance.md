# Spider Farmer Case Study — Provenance Map

This document maps each preserved chat transcript and researcher-authored artifact in the Spider Farmer case study to (a) the technical claims it supports, (b) external code or log files it references, and (c) the sections of `REPORT.md` it underpins.

It addresses the open issue recorded in `docs/logbook.md` (entry "2026-05-01 (methodology review)") — *"Define concrete provenance mapping templates for transcripts."* — and the open item in `REPORT.md` §10 — *"Add a concrete provenance matrix mapping each raw transcript to analysis decisions and code changes."*

## Status notes

- All transcripts in `raw_conversations (copy&paste, web)/` are exports from a web chat UI. They are copy-paste captures and contain no embedded HTTP timestamps; ordering below is reconstructed from internal cross-references.
- The `original/` directory is empty in this repository. Files referenced by the transcripts and `REPORT.md` (APKs, ESPHome zip, BLE bridge, Python controller, HA logs, `apk_analysis/*.md`) are **not currently vendored**. Their origin and storage location should be recorded once decided.
- The integration code itself lives in an external repository, referenced here as `github.com/noheton/spider_farmer` (transcript T4, line 21, "PR created: …/pull/9"). No commit SHAs from that repository are recorded in the chat exports.

## Transcript register

| ID | Filename | Lines | Phase (AI-generated analysis) |
|---|---|---|---|
| T1 | `Analyze Spider Farmer app structure and code.txt` | 113 | Discovery: APK extraction and `apk_analysis/` doc set |
| T2 | `Add BLE connection to spider_farmer component` | 88 | Build: HA BLE coordinator, passive discovery, config flow |
| T3 | `Fix BLE decryption failure issue.txt` | 50 | Debug: static-vs-dynamic IV bug |
| T4 | `Fix decryption failure in log processing.txt` | 92 | Debug: wrong CB key + config-entry migration |
| T5 | `Fix parameter setting in Spider Farmer integration.txt` | 63 | Debug: race condition, retry-after-disconnect, optimistic state |
| T6 | `Fix light fan and ventilator control in Home Assistant` | 906 | Dataset: live MQTT probe / response trace |
| T7 | `Add logo to integration and repository.txt` | 0 | Empty file — content not preserved |

## Provenance matrix

| Transcript | Repo evidence underpinned | External evidence referenced | Notes / gaps |
|---|---|---|---|
| T1 | `REPORT.md` §3 (artifact inventory), §5.1 (BLE UUIDs/cipher), §5.2 (key/IV pairs), §5.4 (corrections) | Creates `doc/apk_analysis/{README,infrastructure,api_endpoints,mqtt_protocol,ble_analysis}.md` in external repo. Mentions `Spider Farmer_2.4.0_APKPure.zip`, `esphome-spiderfarmer_ble-encrypt.zip`, `SpiderBLEBridge-master.zip`, `PythonSpiderController-main.zip`, `discussion.md`. Records gitignore of three 60 MB extracted APK directories. | None of the referenced doc files or zip artifacts are present in `experiments/spider-farmer/original/`. The UUID-role correction (`ff01` Notify, `ff02` Write) and cipher correction (OFB/CTR → CBC) are documented only inside this transcript. |
| T2 | `REPORT.md` §5.3 (commands, msgId), implicitly §9 (BLE instability) | Creates external files `coordinator.py`, `ble_protocol.py`, `ble_coordinator.py`, `manifest.json` (bluetooth match rules), `config_flow.py` (`async_step_bluetooth`). Documents two reference-implementation bugs fixed: (i) `outer_payload_len` excluding 2-byte footer CRC, (ii) dynamic IV slice = `raw[6:20] + 0x0000` rather than `raw[6:22]`. | No commit SHA, branch name, or PR number is recorded. Cannot pin to external repo state. |
| T3 | `REPORT.md` §5.4 (AI-assisted corrections) | Reads HA log `home-assistant_spider_farmer_2026-04-25T04-32-35.346Z.log` (not in repo). Cites reference implementation `BLEPairingManager.py` lines 84–98. Modifies external `ble_protocol.py` decrypt path. | The HA log file is not vendored. The reference `BLEPairingManager.py` likely belongs to one of the three community implementations (also not vendored). |
| T4 | `REPORT.md` §5.2 (confirmed CB key), §5.4, §10 next-step "concrete provenance matrix" | Creates external PR: `github.com/noheton/spider_farmer/pull/9`. Records key change `J4G0M9dX1f1v3fXr` → `iVi6D24KxbrvXUuO` and IV change `2AKVNUbU4mvU3Elt` → `RnWokNEvKW6LcWJg` in external `const.py`. Adds `async_migrate_entry` (config-entry `VERSION 1→2`) in external `__init__.py`. References HA log `home-assistant_spider_farmer_2026-04-25T05-06-18.665Z.log`. | PR URL is the only external pin — neither commit SHAs nor merge state are recorded here. The brute-force script that recovered the correct key is referenced in T1 line 106 but the script itself is not vendored. |
| T5 | `REPORT.md` §5.3 (control commands), §9 (resilience issues) | Reads HA log `home-assistant_spider_farmer_2026-04-26T11-31-51.573Z.log` (not in repo). Modifies external `ble_coordinator.py` (`asyncio.Lock`, post-write connection check) and `light.py`/`fan.py` (optimistic `coordinator.update()`). Identifies three concrete bugs with line-level evidence (log lines 997–999 cited). | Log not vendored. No commit SHA. |
| T6 | `REPORT.md` §3 (HA log artifact reference), §5.3 (msgId / JSON command formats) | The transcript itself **is** primary protocol data: 27 probes, full request/response JSON for `getConfigFile`, `setOnOff` (light, blower, fan), against MQTT topic `SF/GGS/CB/API/UP/80F1B2B3B648` from device `192.168.1.60:1883`. | Largely *self-evidencing*: this is the most reproducible piece of evidence in the case study because the JSON traffic is captured verbatim. Device serial `80F1B2B3B648` and broker IP appear in cleartext — note for any publication/anonymisation step. |
| T7 | none | none | Empty file. Either retrieve content from the original chat session or remove the placeholder. |

## Cross-references

- The exported HA log filenames referenced by T3, T4, and T5 (`home-assistant_spider_farmer_2026-04-25T04-32-35.346Z.log`, `2026-04-25T05-06-18.665Z.log`, `2026-04-26T11-31-51.573Z.log`) follow a consistent UTC-timestamp convention. If the logs are recovered, they should be placed in `experiments/spider-farmer/original/` with their original filenames and SHA-256 hashes recorded here.
- `REPORT.md` §3 lists the expected artifacts; this provenance file should be updated whenever any of them are added to or removed from `original/`.

## Open follow-ups

1. Pin external code state. Once `noheton/spider_farmer` PR #9 is merged, record the merge commit SHA and the post-merge tag (if any).
2. Restore or replace the empty T7 transcript (`Add logo to integration and repository.txt`).
3. Vendor or reference (with hashes) the three community reference implementations cited in T1.
4. Replace device-specific identifiers in T6 (serial `80F1B2B3B648`, broker `192.168.1.60:1883`) before any public release of this case study.
