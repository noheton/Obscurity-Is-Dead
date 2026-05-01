# Sources and Literature Review

This document tracks literature, scientific sources, and data analyses that underpin the paper.

## Purpose

- Document the provenance of academic, industry, and community sources.
- Verify the originality of the research question and claims.
- Capture supporting and contradictory evidence.
- Make literature analysis transparent and reproducible.

## Verification status legend

Each entry below carries one of:

- **[repo-verified]** — referenced by name in a primary repo file (transcript, `REPORT.md`, methodology, etc.). The reference itself is recorded; the underlying source has not necessarily been retrieved or read.
- **[unverified-external]** — pointer that originates outside the repo (URL or formal citation given in a chat transcript) but has not been independently retrieved, read, or verified by a researcher in this session.
- **[needs-research]** — gap or open question that requires literature search before any claim depending on it can be made in the paper.

No external retrieval has been performed in this seeding pass. Entries marked `[unverified-external]` are recorded so they can be retrieved and verified in a subsequent session.

---

## Source register — Spider Farmer case study

### S-SF-1 — `esphome-spiderfarmer_ble-encrypt` (community implementation)
- Type: community open-source implementation (ESPHome component for Spider Farmer BLE decryption)
- Reference: filename `esphome-spiderfarmer_ble-encrypt.zip` cited in `experiments/spider-farmer/REPORT.md` §3 and in the transcript `Analyze Spider Farmer app structure and code.txt` (T1).
- URL: not recorded in repo.
- Status: **[repo-verified]** as a referenced artifact; source repository URL needs to be added.
- Relation to research: one of three independent reference implementations cross-checked during the BLE protocol discovery phase.

### S-SF-2 — `[REDACTED:repo-path:SF-IMPL-2]-master` (community implementation)
- Type: community open-source implementation.
- Reference: `[REDACTED:repo-path:SF-IMPL-2]-master.zip` cited in `REPORT.md` §3 and transcript T1.
- URL: not recorded in repo.
- Status: **[repo-verified]**.
- Relation to research: cross-implementation comparison; cited as a source of the `BLEPairingManager.py` reference logic in `Fix BLE decryption failure issue.txt` (T3).

### S-SF-3 — `[REDACTED:repo-path:SF-IMPL-3]-main` (community implementation)
- Type: community open-source implementation.
- Reference: `[REDACTED:repo-path:SF-IMPL-3]-main.zip` cited in `REPORT.md` §3 and transcript T1.
- URL: not recorded in repo.
- Status: **[repo-verified]**.
- Relation to research: third independent reference implementation in the four-way comparison.

### S-SF-4 — `noheton/spider_farmer` PR #9
- Type: pull request on an external GitHub repository.
- Reference: `https://github.com/noheton/spider_farmer/pull/9` cited in transcript `Fix decryption failure in log processing.txt` (T4) line 21.
- Status: **[unverified-external]**.
- Relation to research: contains the CB-key correction (`J4G0M9dX1f1v3fXr` → `iVi6D24KxbrvXUuO`), the IV correction, and the HA config-entry migration (`VERSION 1→2`) that resolved the BLE decryption failure.

### S-SF-5 — Spider Farmer cloud MQTT endpoint
- Type: vendor service identifier extracted from APK.
- Reference: `sf.mqtt.spider-farmer.com:8333` cited in `Analyze Spider Farmer app structure and code.txt` (T1) line 14.
- Status: **[repo-verified]** as an extracted constant; not a literature source.
- Relation to research: documents the cloud component of the architecture for completeness; informs the security discussion (TLS cert files extracted from APK).

---

## Source register — EcoFlow PowerOcean case study

### S-EF-1 — EcoFlow Open Platform API (Java demo)
- Type: vendor-published reference implementation.
- Reference: `ecoflow-open-demo.zip` cited in `experiments/ecoflow-powerocean/REPORT.md` §3 and `Add parameter setting support to EcoFlow integration.txt` (T1). Java files named: `HttpUtil.java`, `MyMapUtil.java`, `EncryptUtil.java`.
- URL: vendor developer portal `developer.ecoflow.com` referenced in `Fix PowerPulse settable entities hierarchy.txt` (T3) line 166.
- Status: **[unverified-external]**.
- Relation to research: documents the official Open API write surface (`PUT /iot-open/sign/device/quota`) and HMAC-SHA256 signing algorithm. Should be retrieved or referenced by canonical URL.

### S-EF-2 — EcoFlow PowerOcean device documentation
- Type: vendor PDF documentation.
- Reference: `powerocean.pdf` cited in `REPORT.md` §3, §9 and T1 line 102. Source unspecified.
- Status: **[repo-verified]** as a referenced artifact; not present on disk.
- Relation to research: vendor protocol/parameter documentation referenced as ground truth for the device equipment database (12 kW inverter, two 5 kWh batteries, 11 kW PowerPulse charger).

### S-EF-3 — EcoFlow general info documentation
- Type: vendor PDF documentation.
- Reference: `geninfo.pdf` cited in `REPORT.md` §3 and T1 line 103.
- Status: **[repo-verified]** as a referenced artifact; not present on disk.

### S-EF-4 — HACS integration publishing guide
- Type: open-source community documentation.
- Reference: `https://hacs.xyz/docs/publish/integration/` cited verbatim in `Refactor integration to modern Home Assistant standards.txt` (T2) line 2.
- Status: **[unverified-external]**.
- Relation to research: governs the HACS/hassfest conformance work documented in `REPORT.md` §5.3. Source for "HACS is the priority" rule applied during the modernization pass.

### S-EF-5 — Open Charge Point Protocol (OCPP)
- Type: open standard for EV-charging communication.
- Reference: `https://de.wikipedia.org/wiki/Open_Charge_Point_Protocol` cited in `Fix PowerPulse settable entities hierarchy.txt` (T3) line 169.
- Status: **[unverified-external]**.
- Relation to research: candidate framing for a follow-up case study or for paper Future Work — bridges the EV charger entities documented in `REPORT.md` §5.2 to a public standard.

### S-EF-6 — § 69e UrhG (German Copyright Act, decompilation for interoperability)
- Type: primary legal text — Bundesrepublik Deutschland.
- Reference: cited in transcript `Fix PowerPulse settable entities hierarchy.txt` (T3) line 147.
- URL: not recorded in repo.
- Status: **[unverified-external]** for the primary text; **the legal opinion that accompanies this citation in T3 is AI-generated and is not legal advice**.
- Relation to research: forms the backbone of the publishability discussion for both case studies. Must be cross-checked against the canonical primary text and a qualified commentary source before any legal framing appears in `paper/main.md`.

### S-EF-7 — EU Software Directive 2009/24/EC
- Type: primary legal text — European Union.
- Reference: cited in transcript T3 line 147 alongside § 69e UrhG.
- URL: not recorded in repo.
- Status: **[unverified-external]**.
- Relation to research: the EU-level instrument implemented by § 69e UrhG. Same caveat as S-EF-6.

---

## Cross-cutting and methodological references

### S-X-1 — Repository AI policy and methodology
- Reference: `.instructions.md`, `copilot-instructions.md`, `CLAUDE_CODE_INSTRUCTIONS.md`, `docs/methodology.md`.
- Status: **[repo-verified]**.
- Relation to research: governs how AI-generated outputs in the case studies are labelled, stored, and cross-referenced.

### S-X-2 — Project logbook
- Reference: `docs/logbook.md`.
- Status: **[repo-verified]**.
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
