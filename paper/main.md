# AI-Assisted Hacking: Key to Interoperability or Security Nightmare?

## Abstract
This paper investigates how modern large language models collapse the traditional "effort gap" in reverse engineering. Through two empirical case studies — Spider Farmer BLE devices and EcoFlow PowerOcean energy systems — we show how AI-assisted analysis turns theoretical protocol knowledge into practical, replicable local integrations. We then assess whether this collapse is a force for interoperability and right-to-repair or a systemic security risk, and we propose a research methodology that treats AI conversation transcripts, vendor artifacts, and version history as first-class evidence.

---

## 1. Introduction and Motivation

### 1.1 The effort gap as a security model
The dominant security posture for consumer IoT is not cryptographic but economic: proprietary protocols, obfuscated APKs, and undocumented APIs raise the activation energy of integration high enough that a casual researcher gives up. We name this implicit defence the *effort gap* and argue that it has functioned as the de-facto interoperability barrier of the last decade.

### 1.2 Research question
> Is AI-assisted hacking primarily a means to unlock interoperability, or does it instead magnify security risk by making obscurity ineffective?

### 1.3 Motivation
- **User sovereignty.** Owners of energy and horticulture hardware are increasingly forced into vendor cloud silos for basic local control.
- **Right-to-repair and § 69e UrhG / EU 2009/24/EC.** European law explicitly permits decompilation for interoperability; AI assistance changes the *practical* — not the *legal* — accessibility of that right. (Legal framing to be sourced; see `docs/sources.md` S-EF-9, S-EF-10.)
- **Dual use.** The same workflow that yields a Home Assistant integration yields recovered MQTT credentials and live device write paths. The Spider Farmer case study contains a concrete instance of recovered live credentials (see §4.6).
- **Reproducibility crisis in security research.** Published "hacks" rarely ship with prompts, transcripts, or commit-pinned artifacts. We argue this is now a methodological defect, not a stylistic choice.

### 1.4 Thesis and contributions
We claim that the effort gap has *collapsed asymmetrically*: it has collapsed faster for interoperability work (where success is verifiable against a working integration) than for offensive work (which still requires target selection, persistence, and operational tradecraft). The paper contributes:

1. A definition of the effort gap and an operationalisation as measurable KPIs (`docs/methodology.md` §10).
2. Two empirical case studies with complete artifact provenance (`experiments/spider-farmer/`, `experiments/ecoflow-powerocean/`).
3. An auditable methodology that treats AI conversation transcripts as research artifacts, mapped to git history and vendor code (`experiments/*/provenance.md`).
4. A synthesis of interoperability gains versus dual-use risks, grounded in the verified evidence of both cases.

### 1.5 Scope and non-goals
- We do **not** publish weaponised exploit code; recovered credentials are flagged for redaction (`docs/logbook.md` 2026-05-01 audit entry).
- We do **not** offer legal advice; AI-generated legal opinions in transcripts are flagged as such in `docs/sources.md` and replaced with sourced commentary before any legal claim is made.
- We do **not** evaluate AI models comparatively; the unit of analysis is the *workflow*, not the model.

---

## 2. Methodology

The full operational methodology is maintained in `docs/methodology.md`. This section summarises it for the paper and pins the design decisions that distinguish the work.

### 2.1 Unit of analysis: the AI-assisted research workflow
A *workflow* is the tuple (vendor artifacts, AI conversation transcripts, integration code, git history, validation evidence). The case study, not the device or the model, is the experimental unit.

### 2.2 Artifact collection
For each case we vendor:
- Vendor binaries and documentation (APKs, PDFs, firmware where lawful).
- AI conversation transcripts (`raw_conversations (copy&paste, web)/`).
- Community reference implementations, embedded as plain files for direct citation (repo commit `ffdf60c`).
- The integration code under study, embedded under `original/` rather than referenced as a moving submodule.

### 2.3 Provenance mapping
Every technical claim is mapped, in a per-case `provenance.md`, to (a) the transcript that proposed it, (b) the file and line numbers in `original/` that confirm it, and (c) the commit SHA at which the mapping was verified. Source-register entries carry a verification status — `[repo-vendored]`, `[repo-referenced]`, `[unverified-external]`, or `[needs-research]` — so the paper can be honest about what has and has not been independently checked.

### 2.4 AI transparency and lege artis
Following the DFG Guidelines for Safeguarding Good Research Practice, every section discloses where AI assistance was used and where it was rejected, corrected, or contradicted by the underlying code. AI-generated legal analysis is never used as legal advice. The repository's AI policy is canonicalised in `CLAUDE_CODE_INSTRUCTIONS.md` and aliased in `.instructions.md` and `copilot-instructions.md`.

### 2.5 KPIs (effort-gap operationalisation)
Drawn from `docs/methodology.md` §10 and applied per case study:
- Process: artifact-acquisition completeness, prompt-iteration count, automation ratio.
- Experimental success: probe success rate, functional coverage, reproducibility score.
- Time and effort: time-to-first-working-integration, effort-gap metric (estimated manual hours vs AI-assisted hours).
- Problem characterisation: discovery density, candidate-space size, obscurity depth.

### 2.6 Validation and reproducibility
Each finding is reproduced against the embedded `original/` code at a pinned commit. Failed attempts are recorded in the logbook and (where applicable) in the per-case `provenance.md`. The KPI table at the end of each case study reports verified, not aspirational, numbers.

### 2.7 Ethics
The dual-use evaluation is part of the methodology, not a postscript. For each case we explicitly enumerate (a) what becomes easier for an integrator and (b) what becomes easier for an attacker. Live credentials, device serials, and broker IPs are flagged for redaction before any public release (`docs/logbook.md` 2026-05-01 audit).

---

## 3. Experiment & Analysis 1 — Spider Farmer

### 3.1 System and threat model
Spider Farmer GGS controllers, power strips, lamps, and grow tents communicate locally over BLE and remotely via an MQTT cloud broker. The vendor's defence is an AES-128-CBC scheme with hardcoded keys and IVs embedded in the Android APK, plus a self-signed-cert MQTT broker.

### 3.2 Artifact inventory
Source register entries S-SF-1 through S-SF-8. Primary artifacts:
- `original/doc/Spider Farmer_2.3.0_APKPure.zip`, `Spider Farmer_2.4.0_APKPure.zip`
- Three independent reference implementations (ESPHome, ESP32→MQTT bridge, Python+MQTT)
- `raw_conversations (copy&paste, web)/` (7 transcripts)
- The integration itself, embedded at `original/` (manifest version `3.0.0`, `config_flow.py` `VERSION = 3`).

### 3.3 AI-assisted analysis workflow
1. **APK static extraction** of strings, action fields, and constants.
2. **Cross-implementation comparison** across four independent reverse-engineering attempts, captured in `original/doc/apk_analysis/implementations.md`.
3. **AI-mediated reconciliation** of conflicting key/IV candidates (transcripts T1–T6).
4. **Code-level confirmation** against the integration's `const.py`, `ble_protocol.py`, `ble_coordinator.py`, and `__init__.py`.

### 3.4 Findings — interoperability
- BLE service `000000ff-…`, characteristics `0000ff01` (notify) and `0000ff02` (write-with-response).
- AES-128-CBC with zero padding; two-stage header with CRC16-Modbus.
- Static outgoing IVs per device type, dynamic incoming IVs derived from packet header — confirmed in `ble_protocol.py` lines 195-204.
- Corrected key/IV pairs for CB controller and friends, pinned in `const.py` lines 45-47.
- Concurrent-write safety via `asyncio.Lock` in `ble_coordinator.py` line 79.
- Migration framework `async_migrate_entry` in `__init__.py` line 95; the integration is now at `VERSION = 3` past the T4-era `1→2` migration (the `2→3` step is presently undocumented by any preserved transcript — recorded as an open issue).

### 3.5 Validation
Each constant and code path above was re-checked against `original/` at commit `ffdf60c` (logbook entry "audit against embedded vendor code"). The four independent implementations agree on the BLE protocol shape; minor disagreements on key tables were resolved in favour of the in-tree `const.py`.

### 3.6 Findings — security implications
The `original/doc/log.md` community thread documents a self-signed-certificate MITM against the vendor MQTT broker `sf.mqtt.spider-farmer.com:8333`, recovering live credentials (username `[REDACTED:username:S-SF-5-username]`, password redacted in the published paper, present in S-SF-5). This is independent corroboration of the claim that the effort gap has collapsed for *both* defenders and attackers.

### 3.7 KPI summary (Spider Farmer)
*To be populated from logbook and provenance evidence*: artifact-acquisition completeness, transcript count (7), independent-implementation count (3 + integration), time-to-first-working-integration, residual obscurity depth.

---

## 4. Experiment & Analysis 2 — EcoFlow PowerOcean

### 4.1 System and threat model
The EcoFlow PowerOcean is a residential energy system — 12 kW inverter, two 5 kWh batteries, 11 kW PowerPulse charger (per `original/doc/equipment.md` and `REPORT.md` §9). It exposes three API surfaces: a legacy `setDeviceProperty` REST endpoint, the published Open API (`PUT /iot-open/sign/device/quota` with HMAC-SHA256), and an MQTT surface. The vendor publishes documentation for the Open API but the consumer app uses the legacy endpoint.

### 4.2 Artifact inventory
Source register entries S-EF-1 through S-EF-6. Primary artifacts:
- `original/doc/EcoFlow_6.13.8.2_APKPure/` — four APK split files plus manifest.
- `original/doc/ecoflow-open-demo.zip` — vendor reference Java implementation.
- `original/doc/powerocean.pdf`, `geninfo.pdf` — vendor documentation.
- `original/doc/apk.md` (327 lines), `apk-logs.md` (546 lines), `implementation.md` (434 lines), six raw extraction logs.
- The integration `powerocean_dev` at `manifest.json` version `2026.05.01`, embedded at `original/`. Upstream parent `https://github.com/[REDACTED:repo-path:EF-IMPL-1]` per `const.py` line 13.
- `raw_conversations (copy&paste, web)/` (3 transcripts).

### 4.3 AI-assisted analysis workflow
1. **APK string and action-field extraction** to enumerate writeable parameters.
2. **Three-surface reconciliation** — `apk.md` line 52 documents the choice to use the legacy endpoint over the Open API, resolving the prior open question.
3. **Type-system bug discovery** — the regex `(?<!st)(amp|current)$` (`types.py` line 90) corrects a misclassification that conflated current readings with the literal "st" suffix.
4. **Config-flow refactor** — three-step config flow (`config_flow.py`, 510 lines) with cross-domain `async_step_import` migration.

### 4.4 Findings — interoperability
- Write surface: `POST /iot-devices/device/setDeviceProperty` with payload `{"sn": "<device_sn>", "params": {"<camelCase_field>": <value>}}` — confirmed at `api.py` line 306.
- Field-name convention: predictable camelCase from APK constants (e.g., `ACTION_W_CFG_BACKUP_REVERSE_SOC` → `cfgBackupReverseSoc`).
- New writeable HA entities: `button.system_reboot`, `button.system_selfcheck`, `number.backup_reserve_soc`, `number.fast_chg_max_soc`, `number.charger_power_limit`, `number.grid_in_pwr_limit`.
- Domain `powerocean_dev` (`const.py` line 10), HACS/hassfest conformance per `REPORT.md` §5.3.

### 4.5 Validation
Every constant and endpoint above was re-checked against `original/` at commit `ffdf60c`. The three-surface model is documented in-tree, not inferred.

### 4.6 Findings — security implications
- The legacy endpoint accepts authenticated writes without the HMAC-SHA256 ceremony of the Open API. Any leaked session token grants the same write surface used by the consumer app.
- Writeable parameters include grid-in power limit, battery reserve SOC, and EV charger power. The dual-use surface is non-trivial: the same controls that enable local automation enable remote denial-of-availability against a residential energy system.
- Vendor APK and PDF redistribution status is flagged in `docs/sources.md` (S-EF-2, S-EF-3, S-EF-4) and must be resolved before public release.

### 4.7 KPI summary (EcoFlow PowerOcean)
*To be populated*: number of writeable parameters discovered, transcript count (3), API-surface count (3), residual obscurity depth, time-to-first-working-write.

---

## 5. Synthesis

### 5.1 Cross-case comparison
| Dimension | Spider Farmer | EcoFlow PowerOcean |
|---|---|---|
| Defence model | Hardcoded AES keys/IVs in APK + self-signed MQTT cert | Three undocumented API surfaces, vendor publishes only one |
| Primary AI lift | Reconciling four independent implementations | Discovering and choosing among API surfaces; type-system bug fix |
| Independent corroboration | 3 community implementations + community MITM thread | 1 vendor reference implementation + 1 upstream community fork |
| Live credential recovery | Yes (MQTT broker creds) | No (token-bearer model) |
| Dual-use blast radius | Per-device control over horticulture hardware | Grid-in / battery-reserve / EV-charger control |
| Status of vendor public docs | None | Open API documented; consumer app uses different surface |

### 5.2 What the AI workflow added
- **Spider Farmer.** Not protocol *discovery* — the four community implementations had already done that — but *reconciliation* across conflicting key tables and verification of the dynamic-IV slice formula.
- **EcoFlow PowerOcean.** Surface enumeration and field-name convention recovery: a manual reverse-engineer would have eventually found the legacy endpoint, but the AI-assisted workflow recovered the full writeable-parameter catalogue from APK constants in a single pass.

### 5.3 Common patterns
- Both defences relied on the *combination* of obscurity and effort, not on either alone.
- Both yielded clean local integrations once a single piece of evidence (key table; API surface) was identified.
- In both cases, AI assistance compressed the *reconciliation* phase more than the *discovery* phase. The effort-gap collapse is unevenly distributed across workflow stages.

### 5.4 Limits of the comparison
Two cases is two cases. We cannot generalise from horticulture BLE and residential energy storage to "all IoT". The case selection over-samples categories where a public Home Assistant integration was already plausible; the inference to harder targets (e.g. closed industrial protocols) is open.

---

## 6. Discussion

### 6.1 Interoperability: the automated right to repair
European decompilation-for-interoperability provisions (§ 69e UrhG, EU 2009/24/EC) presuppose that decompilation is *legally* possible for an end user. AI assistance makes it *practically* possible. The case studies are existence proofs that the legal carve-out can now be exercised at hobbyist scale, not just by specialised firms. Whether legislatures intended this is an empirical question for legal scholarship, not for this paper. (Sourcing: `docs/sources.md` S-EF-9, S-EF-10, both `[unverified-external]` until cross-checked.)

### 6.2 The collapse of the boredom barrier
Security through obscurity rested on a labour-market assumption: that a determined hobbyist would not invest a fortnight to integrate a grow-tent controller. That assumption is dead. The Spider Farmer case shows three independent community implementations of the same protocol and an independently recovered set of MQTT credentials — converging evidence that the obscurity barrier has perforated.

### 6.3 Asymmetry of collapse
The effort gap has *not* collapsed uniformly. AI assistance compresses the *known-good-protocol* path far more than the *novel-vulnerability* path; verifying an integration against a live device is cheap, and verifying an exploit against a live target is not. We argue this asymmetry is the most under-discussed feature of the post-LLM threat model.

### 6.4 Dual-use accountability
Both case studies expose live attack surfaces. In Spider Farmer the surface is already public — recovered in a community thread — and the case is a *post-hoc* documentation of a collapse that has already happened. In EcoFlow the surface is documented for the first time here, and we accordingly enumerate the redactions that must be applied before public release (logbook 2026-05-01 audit; `docs/sources.md` S-SF-5, S-EF-2..4).

### 6.5 Methodological implications for security research
- Treat AI conversation transcripts as research artifacts. They are the equivalent of a lab notebook for the LLM era.
- Pin all external code by commit SHA, not by branch name. Branches move; SHAs do not.
- Embed vendor artifacts under explicit redistribution caveats rather than referencing moving URLs.
- Mark every literature claim with a verification status. The discipline is cheap; the alternative is the current state of practice.

### 6.6 Threats to validity
- **Selection bias.** Cases were chosen because the researcher already wanted local control; failed attempts at harder targets are under-reported.
- **Tooling drift.** AI model behaviour changes between sessions. The workflow is reproducible against artifacts; identical AI outputs are not.
- **Legal framing.** AI-generated legal analysis in transcripts is not legal advice and is flagged as such in the source register.
- **Redistribution.** Vendor APKs and PDFs are vendored for cite-ability but their redistribution status is not yet resolved.

---

## 7. Conclusion

AI-assisted reverse engineering does not invent new capabilities; it lowers the activation energy of capabilities that already existed. The Spider Farmer and EcoFlow PowerOcean cases show that this lowering is enough to collapse the effort gap that previously sustained "security through obscurity" as a viable consumer-IoT defence. The collapse is genuinely double-edged — it materially advances right-to-repair while exposing live attack surfaces — but it is also *asymmetric*, compressing the integration path more aggressively than the offensive path.

The path forward is not to discourage AI-assisted research but to make it *auditable*: vendor artifacts pinned, transcripts treated as evidence, dual-use evaluation built into the methodology rather than appended to it, and legal framing always sourced. Obscurity is dead. What replaces it has to be designed, not assumed.

### 7.1 Future Work
- Extend to a third case study in a domain with no prior community integration (open question: does the asymmetry hypothesis hold there?).
- Operationalise the effort-gap KPIs against historical reverse-engineering case studies for a longitudinal comparison.
- Develop a responsible-disclosure framework specific to AI-assisted reverse engineering.
- Replace `[unverified-external]` legal sources with sourced commentary; address `[needs-research]` items in `docs/sources.md`.
- Reconstruct the Spider Farmer `VERSION 2 → 3` migration step that no preserved transcript currently documents.
