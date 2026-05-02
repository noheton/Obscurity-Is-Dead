# Phase 0 — Bootstrap and Target Intake

**Experiment:** `iot-integrator-ondilo-ico-spa-v2`
**Date opened:** 2026-05-02
**Branch:** `claude/iot-water-analyzer-integration-mIbFv`
**Author attribution:** AI-drafted (Claude Opus 4.7) under researcher direction; researcher review pending per `CLAUDE.md` rule 1.

This file is the Phase 0 deliverable required by `docs/prompts/iot-integrator-prompt.md` §Phase 0. It contains (a) the Technique Inventory bootstrapped from the three prior case studies, and (b) the Target Intake Summary for the Ondilo ICO Spa V2 connected water analyzer, with explicit gaps where the user has not yet declared scope.

---

## 0.1 Technique Inventory

Each entry traces to a specific section of a prior `REPORT.md` per the prompt's
"do not invent techniques" constraint. Source columns cite repository paths and
section numbers in the form required by `docs/prompts/iot-integrator-prompt.md`
§Output format.

| ID | Description (one sentence) | Source | Preconditions | Privacy cost | Failure modes |
|----|---------------------------|--------|---------------|--------------|---------------|
| `T-APK-STRINGS` | Static string and constant extraction from a vendor APK to recover endpoint names, action constants, and protocol vocabulary. | `experiments/ecoflow-powerocean/REPORT.md` §4 and §5.1; `experiments/spider-farmer/REPORT.md` §4. | A locally stored APK the user is licensed to inspect. | None at static-analysis time, provided the APK was obtained from a source the user is entitled to use. | Constants may be obfuscated; some action keys do not map 1:1 to runtime payload field names (EcoFlow §10). |
| `T-REST-WRITE-PROBE` | Identification of REST write surfaces and payload conventions (e.g. `setDeviceProperty`, camelCase property names) by cross-referencing APK constants with integration code. | `experiments/ecoflow-powerocean/REPORT.md` §5.1 and §5.2. | APK strings plus a reference HA integration or vendor docs; ideally a captured live request to validate. | Cloud probes contact vendor infrastructure; LAN-local REST probes do not. | Field names are provisional until a live capture confirms exact name/value pairs (EcoFlow §10). |
| `T-BEARER-LIFETIME` | Treat vendor bearer tokens as a first-class risk: model their acquisition path, lifetime, and blast radius before designing an integration. | `experiments/ecoflow-powerocean/REPORT.md` §8 and §11. | A documented or observed authentication flow. | Implicit: any token capture step touches the vendor cloud. | Lifetime/rotation often undocumented; revocation paths may not exist. |
| `T-REGIONAL-HOST-PROBING` | Probe regional vendor hosts (EU/US/CN) to map host coverage and avoid silently falling back to a non-EU jurisdiction. | `experiments/ecoflow-powerocean/REPORT.md` §5.4 and §10. | A list of candidate regional hostnames from APK strings or docs. | Touches vendor cloud DNS/HTTP; may leak the user's IP to a non-EU region. | Hosts gated by account region; some regions only accept tokens issued for that region. |
| `T-BLE-UUID-MAP` | Map BLE service / characteristic UUIDs and advertising-name conventions to functional roles (notify, write-with-response). | `experiments/spider-farmer/REPORT.md` §5.1. | BLE advertisements from the user's own device, optionally cross-referenced with APK GATT references. | None if scans are limited to the user's own device by allowlist; high if neighbour BLE is logged. | Vendor may rotate UUIDs across firmware revisions. |
| `T-IV-KEY-RECOVERY` | Recover hardcoded AES keys, IVs, and pad/CRC framing parameters from APK binaries and confirm them across implementations. | `experiments/spider-farmer/REPORT.md` §5.1, §5.2, §8. | APK + at least one independent reference implementation (ESPHome, Arduino, Python) for cross-check. | Static-analysis only at recovery time; dynamic confirmation needs LAN-local BLE traffic. | Keys may be device-class-specific; static IV reuse weakens confidentiality (Spider Farmer §7). |
| `T-PACKET-FRAMING` | Reconstruct application-layer packet framing (headers, fragment IDs, CRC16-Modbus) by aligning APK constants with captured frames. | `experiments/spider-farmer/REPORT.md` §5.1, §5.3. | APK plus a small set of captured frames whose semantics are known. | LAN/BLE-local; no external traffic. | Header field meanings may shift across firmware; `msgId` correlation required. |
| `T-MSGID-CORRELATION` | Use the protocol's own `msgId`/sequence field to pair requests with responses and to detect retries or out-of-order delivery. | `experiments/spider-farmer/REPORT.md` §5.3. | A protocol with an explicit correlation field. | None beyond the underlying capture. | Devices may reuse `msgId` after disconnect; resilience-sensitive (Spider Farmer §5.3). |
| `T-CROSS-IMPL-VALIDATION` | Validate any extracted protocol claim against ≥2 independent implementations (vendor app, HA logs, ESPHome, Arduino/Python ports) before publishing it. | `experiments/spider-farmer/REPORT.md` §4, §5.4, §8. | At least two independent code or capture sources. | None at analysis time. | Implementations themselves may share a common error source; HA logs alone are not independent. |
| `T-OBSCURITY-VS-AUTH` | Classify each protective measure as *authentication* vs *obscurity* and refuse to count obscurity as security in the integration's threat model. | `experiments/spider-farmer/REPORT.md` §7, §9. | A documented protective measure (e.g. "encrypted BLE", "signed firmware"). | None. | Easy to misread vendor marketing as cryptographic guarantee. |
| `T-DUAL-USE-MIRROR` | For every interoperability win, explicitly state the mirror attacker capability the same artifacts enable, per `CLAUDE.md` rule 5. | `experiments/spider-farmer/REPORT.md` §7, §9; `experiments/ecoflow-powerocean/REPORT.md` §8. | An identified weakness or integration handle. | None directly; reduces future privacy harm by surfacing risk early. | Tempting to omit when the win is small; rule-5 compliance is non-optional. |
| `T-PROVENANCE-MAPPING` | Map every analytical claim and code change to a specific raw transcript turn or APK artifact, recording the link in `provenance.md`. | `experiments/paper-meta-process/REPORT.md` §3, §5.1, §5.2; `experiments/spider-farmer/REPORT.md` §10. | A preserved transcript or artifact. | None. | Curated reconstructions are weaker than verbatim exports; upgrade as soon as practical (paper-meta §6). |
| `T-VERIFICATION-STATUS-LEGEND` | Tag every literature / vendor-doc citation with a verification status (`[lit-retrieved]` vs `[lit-read]`) and never elevate without researcher review. | `experiments/paper-meta-process/REPORT.md` §4, §5.2. | The legend in `docs/sources.md`. | None. | Pressure to upgrade tags without re-reading sources is the typical failure mode. |
| `T-CAPTURE-TIME-REDACTION` | Apply rule-12 redaction at the moment of capture, never retroactively, and register every marker in `docs/redaction-policy.md`. | `experiments/paper-meta-process/REPORT.md` §6 (live-credential redaction open issue) and `CLAUDE.md` rule 12. | Awareness of the sensitive-class taxonomy. | None directly; *prevents* privacy harm. | Retroactive cleanup leaves raw values in git history (Spider Farmer S-SF-* markers, redaction-policy). |
| `T-AI-RESEARCHER-ATTRIBUTION` | Attribute every artifact to AI-drafted vs researcher-verified contribution, per `CLAUDE.md` rule 1. | `experiments/paper-meta-process/REPORT.md` §4, §5.1. | Rule 1 awareness; an explicit attribution slot in each artifact. | None. | Silent AI authorship is the default failure mode; counter with explicit headers. |

**Inventory size:** 15 techniques, all anchored in a prior `REPORT.md` section.

---

## 0.2 Target Intake Summary

### Declared (from researcher's session-opening turn)

- **Vendor:** Ondilo (French legal entity; full corporate details to be verified in Phase 1.2).
- **Product page (researcher-supplied URL):** `https://ondilo.com/de/produkt/ico-spa-v2-vernetzter-wasseranalysator/` (German-language product listing for the "ICO Spa V2 — vernetzter Wasseranalysator", i.e. connected water analyzer for hot tubs / spas).
- **Model under study:** Ondilo ICO Spa **V2**.
- **Device class:** Connected pool/spa water-quality analyzer. The first-generation Ondilo ICO is widely catalogued as a Wi-Fi + Bluetooth floating sensor reporting ORP, pH, water temperature, salinity (model-dependent), and battery state to a vendor cloud, with a Home Assistant cloud-polling integration in the HA core. Whether the "V2" hardware preserves this interface profile, and whether it adds local control, is itself an open question to be resolved in Phase 1.
- **Firmware version:** unknown.

### Gaps (the prompt §0.2 requires these before Phase 1 may start)

The prompt is explicit: *"If any of these are missing, stop and ask."* The
following intake fields have not been provided by the researcher and are
therefore left as gaps to be filled at the Phase 0 → Phase 1 user checkpoint.

| Intake field | Status | Question to researcher |
|--------------|--------|------------------------|
| Desired control surface | **Open** | Read-only sensor exposure (pH, ORP, temperature, salinity, battery) only? Or also write/actuation (e.g. recommended-treatment dispatch, set-point thresholds, calibration triggers) and/or device configuration / OTA control? |
| Privacy boundary | **Open** | Hard "no traffic to Ondilo cloud" (LAN/BLE-only)? Or "cloud accepted but with documented telemetry minimisation"? Are mDNS/SSDP broadcasts of device names containing the household identifier acceptable? Is any third-party analytics SDK in the vendor app a hard blocker? |
| Artifacts available | **Open** | Which of the following can the researcher legally and ethically supply: (a) Ondilo Android/iOS app APK/IPA the researcher has downloaded for their own device; (b) BLE advertisements from the researcher's *own* ICO Spa V2; (c) packet captures of the device's traffic on the researcher's own LAN; (d) HA debug logs from the existing Ondilo HA integration if installed; (e) any vendor-published API/SDK documentation? |
| Device ownership status | **Open** | Confirm the researcher owns the device under study (rule 5 / refuse third-party access path constraint). |
| Cloud-touching probes | **Open** | Is the researcher authorising any cloud-touching probe in Phase 2 (e.g. authenticated call to the documented Ondilo public API on the researcher's own account), or is the boundary strictly LAN/BLE-local? |

### Non-targets (ruled out at intake)

Per `CLAUDE.md` rule 12 and the prompt's "Capture-time redaction discipline":

- No ingestion of credentials, tokens, MAC addresses, BLE addresses, IPs, or
  geolocation belonging to **other** Ondilo users, household members who have
  not consented, or neighbour BLE devices (use `[DROPPED:third-party:<reason>]`).
- No vendor-cloud access path the researcher is not legally entitled to use
  (no credential stuffing, no token replay against another user's account).
- No firmware redistribution: vendor firmware blobs, if encountered, are
  `[REDACTED:secret-asset:...]` and stay out of the public commit set.

### Provisional privacy-relevance heuristic

A spa water analyzer floats in a private body of water at the user's home. Even
read-only telemetry can leak presence (when is the spa used?), occupancy
patterns, and — combined with weather data — household routine. This raises the
floor on the privacy boundary: even a "read-only sensors" scope is not a
"low-stakes" integration. This heuristic is recorded here to ensure Phase 1
research does not silently treat the device as innocuous.

---

## 0.3 Status and next step

- **Phase 0 work product complete** for the parts that do not depend on
  researcher input: the Technique Inventory is closed and traced to prior
  REPORTs.
- **Phase 0 is blocked** on the five Target Intake gaps above. Per the prompt's
  user-checkpoint rule, Phase 1 may not start until the researcher has
  acknowledged this summary and supplied (or explicitly deferred) each open
  intake field.
- No live system, vendor cloud, or third-party artifact has been touched in
  Phase 0. No new redaction markers were introduced; `docs/redaction-policy.md`
  is unchanged by this phase.

— end Phase 0 bootstrap —
