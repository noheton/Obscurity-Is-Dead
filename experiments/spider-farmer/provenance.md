# Spider Farmer Case Study — Provenance Map

This document maps each preserved chat transcript and researcher-authored artifact in the Spider Farmer case study to (a) the technical claims it supports, (b) the source files in `experiments/spider-farmer/original/` it underpins, and (c) the sections of `REPORT.md` it relates to.

It addresses the open issue recorded in `docs/logbook.md` (entry "2026-05-01 (methodology review)") — *"Define concrete provenance mapping templates for transcripts."* — and the open item in `REPORT.md` §10 — *"Add a concrete provenance matrix mapping each raw transcript to analysis decisions and code changes."*

## Status notes

- All transcripts in `raw_conversations (copy&paste, web)/` are exports from a web chat UI. They are copy-paste captures and contain no embedded HTTP timestamps; ordering below is reconstructed from internal cross-references.
- `experiments/spider-farmer/original/` is now a **direct file copy** of the upstream integration repository (commit `ffdf60c` of this repo: *feat(experiments): embed vendor repos as plain files for agent access*). The earlier submodule pin (`8703f28`, commit `f1e3b1f`) has been replaced by the same content materialised as plain files. Provenance entries below now cite specific files in `original/` rather than only external repository names.
- The home-assistant log files referenced in transcripts T3, T4, and T5 (`home-assistant_spider_farmer_2026-04-25T04-32-35.346Z.log`, `…2026-04-25T05-06-18.665Z.log`, `…2026-04-26T11-31-51.573Z.log`) are **not** present in `original/`. These are the only artifacts named by the transcripts that remain absent.

## Transcript register

| ID | Filename | Lines | Phase (AI-generated analysis) |
|---|---|---|---|
| T1 | `Analyze Spider Farmer app structure and code.txt` | 113 | Discovery: APK extraction and `apk_analysis/` doc set |
| T2 | `Add BLE connection to spider_farmer component` | 88 | Build: HA BLE coordinator, passive discovery, config flow |
| T3 | `Fix BLE decryption failure issue.txt` | 50 | Debug: static-vs-dynamic IV bug |
| T4 | `Fix decryption failure in log processing.txt` | 92 | Debug: wrong CB key + config-entry migration |
| T5 | `Fix parameter setting in Spider Farmer integration.txt` | 63 | Debug: race condition, retry-after-disconnect, optimistic state |
| T6 | `Fix light fan and ventilator control in Home Assistant` | 906 | Dataset: live MQTT probe / response trace |
| T7 | `Add logo to integration and repository.txt` | 0 | Empty file — content not preserved (but the work was done; see notes) |

## Provenance matrix — verified against `original/`

| Transcript | Repo evidence underpinned | Verification against `original/` | Notes |
|---|---|---|---|
| T1 | `REPORT.md` §3, §5.1, §5.2, §5.4 | **Confirmed.** `original/doc/apk_analysis/` contains the five files T1 records creating: `README.md` (42 lines), `infrastructure.md` (77 lines), `api_endpoints.md` (141 lines), `mqtt_protocol.md` (331 lines), `ble_analysis.md` (342 lines), plus a later `implementations.md` (237 lines). The four community-implementation zips referenced are present at `original/doc/{esphome-spiderfarmer_ble-encrypt,[REDACTED:repo-path:SF-IMPL-2]-master,[REDACTED:repo-path:SF-IMPL-3]-main}.zip` and `original/doc/Spider Farmer_2.{3,4}.0_APKPure.zip`. The UUID-role correction (`ff01` Notify, `ff02` Write) is documented in `ble_analysis.md` at "Correction from earlier analysis" (line 22-23), and the cipher correction (OFB/CTR → CBC) at line 47-49. | T1's BLE-key candidate `J4G0M9dX1f1v3fXr` was later disproved (see T4); current `const.py` line 45 holds the corrected CB pair. |
| T2 | `REPORT.md` §5.3, §9 | **Confirmed.** `original/coordinator.py`, `ble_protocol.py`, `ble_coordinator.py`, `manifest.json` (with bluetooth match rules `SF-GGS-CB-*`, `SF-GGS-PS5-*`, `SF-GGS-PS10-*`, `SF-GGS-LC-*`, `SF-GGS-*`), and `config_flow.py` are all present. The two reference-implementation bug fixes T2 records are visible in code: footer-CRC accounting is documented in `ble_protocol.py` lines 1-6 docstring; dynamic-IV slice is `raw[BLE_OUTER_HDR : BLE_OUTER_HDR + BLE_INNER_HDR] + b'\x00\x00'` at line 152, with `BLE_OUTER_HDR=6` and `BLE_INNER_HDR=14` per `const.py`, matching T2's `raw[6:20] + 0x0000`. | — |
| T3 | `REPORT.md` §5.4 | **Confirmed.** The static-IV-first decrypt path is implemented in `ble_protocol.py` `decrypt()` lines 195-204: tries `self._iv` first, falls back to `dynamic_iv` if no JSON braces are produced. The accompanying log message at line 201 ("static IV produced no JSON, retrying with dynamic IV") matches T3's design. | The HA log T3 read (`…2026-04-25T04-32-35.346Z.log`) is not vendored. |
| T4 | `REPORT.md` §5.2, §5.4, §10 | **Confirmed in code; revised in scope.** `const.py` lines 45-47 hold the corrected pair: `cb` = `iVi6D24KxbrvXUuO` / `RnWokNEvKW6LcWJg`. `__init__.py` line 95-96 contains `async_migrate_entry()`. **Revision:** transcripts described a `VERSION 1→2` bump; in the current code `config_flow.py` line 87 declares `VERSION = 3`, indicating at least one further migration after T4 was exported. | The brute-force script T1 line 106 / T4 mentions is not visible in `original/`. PR #9 in `noheton/spider_farmer` is the merge vehicle; this repo no longer pins it externally because the content is now embedded. |
| T5 | `REPORT.md` §5.3, §9 | **Confirmed.** `ble_coordinator.py` line 79 declares `self._write_lock = asyncio.Lock()`. Post-write connection checks appear at lines 224, 228, 237. The disconnect-event integration at lines 344-377 (`_disconnected = asyncio.Event()`, `set_disconnected_callback`) is a stronger version of the simple "check `connected` after write" T5 describes. Optimistic state updates in `light.py`/`fan.py` are present (mirror calls into `coordinator.update`). | T5's HA log (`…2026-04-26T11-31-51.573Z.log`) is not vendored. |
| T6 | `REPORT.md` §3, §5.3 | **Self-evidencing dataset.** The 906-line probe trace is itself first-class evidence; no code lookup needed. Device serial `[REDACTED:serial:S-SF-device]` and broker `[REDACTED:ip:S-SF-device]:1883` are visible in cleartext within the transcript and should be redacted before any public release. | — |
| T7 | (none in this transcript) | **Work was completed even though the chat export is empty.** `original/logo.png` and `original/brand/icon.png` (and `icon@2x.png`) exist. The transcript file is 0 bytes, but the deliverable is on disk. | Either retrieve the original chat session for the empty file, or delete it and note completion in `REPORT.md`. |

## Newly-visible evidence not anticipated by the original audit

The embedded vendor copy contains material that was not derivable from transcripts alone:

- **`original/doc/log.md`** — community discussion thread documenting the MQTT-broker MITM. Records that the SF cloud broker uses self-signed certificates, the `[REDACTED:username:S-SF-5-username]` username, and the recovered password `[REDACTED:credential:S-SF-5-password]` (note trailing dash). This is independently strong evidence for the security claim in `REPORT.md` §7 and should be cited directly in the paper.
- **`original/doc/manuals/`** — five vendor user manuals as PDFs (`GGSSystemUserManual`, `GSeriesUserManual`, `SFInlineFanUserManual`, `SFHeaterUseManual03`, `ClipFanUserManual`) which were not referenced in any transcript.
- **`original/tools/mqtt_discover.py`** — a runnable probe tool that complements transcript T6's captured trace. Confirms that the `getConfigFile`, `getSysSta`, `getDevSta`, and `setOnOff` round-trips T6 captures are reproducible.
- **`original/doc/discusson.md`** *(sic)* — additional discussion notes on IVs and keys, referenced in T1 line 42.
- **Manifest version** — `original/manifest.json` reports `"version": "3.0.0"`. Combined with `config_flow.py` `VERSION = 3`, this indicates the integration has progressed past the T4-era state.

## Open follow-ups (revised)

1. ~~Pin external code state~~ — **resolved.** Code is embedded as of repo commit `ffdf60c`.
2. Replace or delete the empty T7 transcript (`Add logo to integration and repository.txt`).
3. Recover the three referenced HA logs (`…2026-04-25T04-32-35.346Z.log`, `…2026-04-25T05-06-18.665Z.log`, `…2026-04-26T11-31-51.573Z.log`) or document why they are not vendored.
4. Redact the device serial `[REDACTED:serial:S-SF-device]`, the broker IP `[REDACTED:ip:S-SF-device]`, and the recovered MQTT password before any public release.
5. Reconstruct the `VERSION 2 → 3` migration step (which transcript drove it?). The logbook should note this.
