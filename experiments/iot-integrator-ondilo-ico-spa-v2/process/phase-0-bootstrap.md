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

### Researcher answers (received 2026-05-02)

The researcher closed the five intake gaps in the Phase 0 → Phase 1 checkpoint
turn. Recorded verbatim and resolved as follows:

| Intake field | Researcher answer | Resolution for the protocol |
|--------------|-------------------|-----------------------------|
| Desired control surface | "read only in this case" | Read-only telemetry: temperature, ORP, pH, TDS, salt, battery, RSSI. No write, no actuation, no configuration, no OTA. Phase 2 weakness analysis must not produce write handles. |
| Privacy boundary | "as private as reasonable" + "prefer local" | Soft local-first boundary: prefer LAN/BLE-only paths; cloud allowed only with documented privacy cost and explicit per-call authorisation. mDNS/SSDP scoped to user's own device, no neighbour logging. No new vendor accounts beyond the one the researcher already operates. |
| Artifacts available | "initial artifact `https://apkpure.com/ico-%E2%80%93-smart-pool-spa-partner/fr.ondilo.ico.icomanager`" | Vendor app APK from APKPure (package `fr.ondilo.ico.icomanager`) is the seed artifact. Other artifacts (BLE captures, LAN PCAP, HA logs) deferred — researcher will be asked per-probe in Phase 2 before any local capture. |
| Device ownership status | "i own this device" | Confirmed. Researcher's own ICO Spa V2 is the only device class in scope. No third-party device, no second-hand-ownership ambiguity. |
| Cloud-touching probes | "escalate to public api after confirmation with user" | No vendor-cloud authenticated call in Phase 1. The Ondilo Customer API (cloud) is **available** as an escalation path, but each authenticated call must be re-confirmed at the moment it is needed in Phase 2 or Phase 3. |

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

- **Phase 0 closed** on 2026-05-02. Technique Inventory finalised; Target Intake
  resolved by the researcher's checkpoint reply.
- **Phase 1 unblocked.** Scope: read-only desk research, no live system or vendor
  cloud contacted. The seed artifact for Phase 2 will be the APKPure listing
  the researcher named (`fr.ondilo.ico.icomanager`); the package itself is
  *catalogued* in Phase 1, not downloaded.
- No new redaction markers introduced in Phase 0; `docs/redaction-policy.md`
  unchanged.

— end Phase 0 bootstrap —
