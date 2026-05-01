# Sources and Literature Review

This document tracks literature, scientific sources, and data analyses that underpin the paper.

## Purpose

- Document the provenance of academic, industry, and community sources.
- Verify the originality of the research question and claims.
- Capture supporting and contradictory evidence.
- Make literature analysis transparent and reproducible.

## Verification status legend

Each entry below carries one of:

- **[repo-vendored]** — the source is now present in this repository as a primary file (e.g. inside `experiments/<case>/original/`). It can be cited directly.
- **[repo-referenced]** — referenced by name in a repo file (transcript, `REPORT.md`, methodology) but not itself vendored. The reference is recorded; the underlying source has not necessarily been retrieved or read.
- **[unverified-external]** — pointer that originates outside the repo (URL or formal citation given in a chat transcript) and has not been independently retrieved, read, or verified by a researcher.
- **[needs-research]** — gap or open question that requires literature search before any claim depending on it can be made in the paper.

No external retrieval has been performed in this session. Entries marked `[unverified-external]` are recorded so they can be retrieved and verified in a subsequent session.

Many entries below were upgraded from `[repo-referenced]` (or `[unverified-external]`) to `[repo-vendored]` after repo commit `ffdf60c` ("feat(experiments): embed vendor repos as plain files for agent access") materialised both case-study `original/` directories as plain files.

---

## Source register — Spider Farmer case study

### S-SF-1 — `esphome-spiderfarmer_ble-encrypt` (community implementation)
- Type: community open-source implementation (ESPHome component for Spider Farmer BLE decryption)
- Path: `experiments/spider-farmer/original/doc/esphome-spiderfarmer_ble-encrypt.zip`
- Status: **[repo-vendored]**.
- Relation to research: one of four independent reference implementations cross-checked during BLE protocol discovery. Cited in `original/doc/apk_analysis/implementations.md` as Implementation #1.

### S-SF-2 — `SpiderBLEBridge-master` (community implementation)
- Type: community open-source implementation (ESP32 → MQTT bridge).
- Path: `experiments/spider-farmer/original/doc/SpiderBLEBridge-master.zip`
- Status: **[repo-vendored]**.
- Relation to research: contains `BLEPairingManager.py` cited as ground truth in transcript T3. Cited as Implementation #2 in `implementations.md`.

### S-SF-3 — `PythonSpiderController-main` (community implementation)
- Type: community open-source implementation (Python + MQTT).
- Path: `experiments/spider-farmer/original/doc/PythonSpiderController-main.zip`
- Status: **[repo-vendored]**.
- Relation to research: third reference implementation in the four-way comparison (Implementation #3 in `implementations.md`).

### S-SF-4 — Spider Farmer Android APK (versions 2.3.0 and 2.4.0)
- Type: vendor binary (Android application package).
- Path: `experiments/spider-farmer/original/doc/Spider Farmer_2.3.0_APKPure.zip`, `Spider Farmer_2.4.0_APKPure.zip`
- Status: **[repo-vendored]**.
- Relation to research: primary vendor artifact from which BLE keys/IVs, MQTT credentials, and protocol constants were extracted. Provenance source reported as APKPure (mirror) — the canonical vendor distribution channel should be recorded if known.
- **Redistribution caveat**: APK files may carry vendor-imposed restrictions; verify before any public release.

### S-SF-5 — Spider Farmer cloud MQTT endpoint and credentials
- Type: vendor service identifier and recovered credentials.
- Reference: `sf.mqtt.spider-farmer.com:8333`, username `sf_ggs_cb`, password `euuavURS4Kp9bMUfYmvwl-` (recovered via self-signed-cert MITM, documented in `experiments/spider-farmer/original/doc/log.md`).
- Status: **[repo-vendored]** (as an extracted/discovered constant).
- Relation to research: directly supports `REPORT.md` §7 (security implications). The credential-recovery method is documented in a community thread embedded in `original/doc/log.md`.
- **Caution**: the recovered password is a live credential. Redact before public release.

### S-SF-6 — Spider Farmer integration code (Home Assistant component)
- Type: community-developed integration code (subject of the case study).
- Path: `experiments/spider-farmer/original/` (root of the embedded vendor copy).
- Status: **[repo-vendored]**. Embedded as of repo commit `ffdf60c`.
- Relation to research: contains the corrected key/IV pairs (`const.py` lines 45-47), the static-IV-first decrypt logic (`ble_protocol.py` lines 195-204), the `asyncio.Lock` in `ble_coordinator.py` line 79, and the migration framework in `__init__.py` line 95. `manifest.json` reports version `3.0.0`, and `config_flow.py` declares `VERSION = 3`.

### S-SF-7 — Spider Farmer APK analysis notes
- Type: AI-assisted analysis documents (researcher-curated).
- Path: `experiments/spider-farmer/original/doc/apk_analysis/{README,api_endpoints,ble_analysis,implementations,infrastructure,mqtt_protocol}.md` (1170 total lines).
- Status: **[repo-vendored]**.
- Relation to research: encodes the protocol-level findings and the cross-implementation comparison.

### S-SF-8 — Spider Farmer vendor user manuals
- Type: vendor PDF documentation.
- Path: `experiments/spider-farmer/original/doc/manuals/{GGSSystemUserManual,GSeriesUserManual,SFInlineFanUserManual,SFHeaterUseManual03,ClipFanUserManual}.pdf`
- Status: **[repo-vendored]**.
- Relation to research: not yet referenced in any case-study output. Candidate baseline for "what the vendor documents publicly" in the paper's interoperability framing.

---

## Source register — EcoFlow PowerOcean case study

### S-EF-1 — EcoFlow Open Platform API (Java demo)
- Type: vendor-published reference implementation.
- Path: `experiments/ecoflow-powerocean/original/doc/ecoflow-open-demo.zip`
- Status: **[repo-vendored]**.
- Relation to research: documents the official Open API write surface (`PUT /iot-open/sign/device/quota`) and HMAC-SHA256 signing algorithm. Cited but **not** ultimately implemented by the integration — see `original/doc/apk.md` and `original/custom_components/powerocean_dev/api.py` line 306, which uses the legacy `setDeviceProperty` endpoint instead.
- External source: vendor developer portal `developer.ecoflow.com` referenced in transcript T3 line 166. **[unverified-external]**.

### S-EF-2 — EcoFlow PowerOcean device documentation
- Type: vendor PDF documentation.
- Path: `experiments/ecoflow-powerocean/original/doc/powerocean.pdf`
- Status: **[repo-vendored]**.
- Relation to research: vendor protocol/parameter documentation referenced as ground truth for the device equipment database (12 kW inverter, two 5 kWh batteries, 11 kW PowerPulse charger per `REPORT.md` §9).
- **Redistribution caveat**: vendor PDFs may carry usage restrictions; verify before public release.

### S-EF-3 — EcoFlow general info documentation
- Type: vendor PDF documentation.
- Path: `experiments/ecoflow-powerocean/original/doc/geninfo.pdf`
- Status: **[repo-vendored]**.
- Relation to research: general EcoFlow Open API documentation. Same redistribution caveat as S-EF-2.

### S-EF-4 — EcoFlow Android APK (version 6.13.8.2)
- Type: vendor binary (Android application package).
- Path: `experiments/ecoflow-powerocean/original/doc/EcoFlow_6.13.8.2_APKPure/` — contains `com.ecoflow.apk`, `H5OfflineAssetPack.apk`, `config.xxhdpi.apk`, `config.arm64_v8a.apk`, plus a manifest and icon.
- Status: **[repo-vendored]**.
- Relation to research: primary vendor artifact from which the three API surfaces and the writeable-parameter catalogue were extracted. **Redistribution caveat as above.**

### S-EF-5 — EcoFlow APK analysis (researcher-authored)
- Type: AI-assisted analysis documents.
- Path: `experiments/ecoflow-powerocean/original/doc/apk.md` (327 lines), `original/doc/apk-logs.md` (546 lines), `original/doc/implementation.md` (434 lines), `original/doc/equipment.md` (15 lines), and six raw extraction logs in `original/doc/logs/`.
- Status: **[repo-vendored]**.
- Relation to research: `apk.md` line 52 explicitly reconciles three API surfaces (legacy `setDeviceProperty`, Open API, and MQTT), resolving the open question raised in the prior audit.

### S-EF-6 — EcoFlow PowerOcean integration code (Home Assistant component)
- Type: community-developed integration code (subject of the case study).
- Path: `experiments/ecoflow-powerocean/original/`.
- Upstream parent: `https://github.com/niltrip/powerocean` (per `original/custom_components/powerocean_dev/const.py` line 13).
- Status: **[repo-vendored]**. Embedded as of repo commit `ffdf60c`.
- Relation to research: contains the `setDeviceProperty` write path (`api.py` line 306), the `(?<!st)(amp\|current)$` regex fix (`types.py` line 90), the 3-step config flow (`config_flow.py`, 510 lines), the cross-domain migration via `async_step_import`, and version `2026.05.01` in `manifest.json`.

### S-EF-7 — HACS integration publishing guide
- Type: open-source community documentation.
- URL: `https://hacs.xyz/docs/publish/integration/`
- Status: **[unverified-external]**.
- Relation to research: governs the HACS/hassfest conformance work documented in `REPORT.md` §5.3.

### S-EF-8 — Open Charge Point Protocol (OCPP)
- Type: open standard for EV-charging communication.
- URL: `https://de.wikipedia.org/wiki/Open_Charge_Point_Protocol` (cited in transcript T3 line 169).
- Status: **[unverified-external]**.
- Relation to research: candidate framing for a follow-up case study or paper Future Work.

### S-EF-9 — § 69e UrhG (German Copyright Act, decompilation for interoperability)
- Type: primary legal text — Bundesrepublik Deutschland.
- Reference: cited in transcript T3 line 147.
- URL: not recorded in repo.
- Status: **[unverified-external]** for the primary text; **the legal opinion that accompanies this citation in T3 is AI-generated and is not legal advice**.
- Relation to research: forms the backbone of the publishability discussion. Must be cross-checked against the canonical primary text and qualified commentary before any legal framing appears in `paper/main.md`.

### S-EF-10 — EU Software Directive 2009/24/EC
- Type: primary legal text — European Union.
- Reference: cited in transcript T3 line 147 alongside § 69e UrhG.
- URL: not recorded in repo.
- Status: **[unverified-external]**.
- Relation to research: the EU-level instrument implemented by § 69e UrhG. Same caveat as S-EF-9.

---

## Cross-cutting and methodological references

### S-X-1 — Repository AI policy and methodology
- Reference: `.instructions.md`, `copilot-instructions.md`, `CLAUDE_CODE_INSTRUCTIONS.md`, `docs/methodology.md`.
- Status: **[repo-vendored]**.
- Relation to research: governs how AI-generated outputs in the case studies are labelled, stored, and cross-referenced.

### S-X-2 — Project logbook
- Reference: `docs/logbook.md`.
- Status: **[repo-vendored]**.
- Relation to research: operational record; logbook entries are pinned to commit SHAs from `git log`.

---

## Literature Review Notes

### Research question originality check
- **[needs-research]** Locate prior peer-reviewed or industry treatments of the "effort gap" framing for AI-assisted reverse engineering.
- **[needs-research]** Locate prior treatments of "security through obscurity" specifically in the context of consumer IoT and BLE-based protocols.

### Key arguments for interoperability (to be sourced)
- **[needs-research]** Right-to-repair literature in the IoT and energy-management context.
- **[needs-research]** Local-first / cloud-independence arguments in smart-home integration ecosystems (Home Assistant, ESPHome).
- **[needs-research]** Legal interoperability carve-outs beyond § 69e UrhG (e.g. analogous provisions in other jurisdictions; DMCA § 1201(f) in the United States).

### Key arguments for security risk (to be sourced)
- **[needs-research]** Empirical work on the consequences of recovering hardcoded keys from mobile applications.
- **[needs-research]** Work on AI-assisted vulnerability discovery and the rate at which it lowers attacker effort.

### Conflicting positions (to be sourced)
- **[needs-research]** Vendor-published positions on community reverse engineering for interoperability.
- **[needs-research]** Counterpositions arguing that interoperability *increases* aggregate risk (e.g. supply-chain or "many hands" arguments).

### Open questions and gaps
- The repository currently contains no peer-reviewed citations. The first concrete paper claim that depends on prior literature should not be drafted until at least the originality-check items above have been filled in.
- AI-generated legal analysis in transcripts must be replaced with sourced legal commentary before any legal framing appears in the paper. **AI-generated legal analysis is not legal advice.**
