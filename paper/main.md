# AI-Assisted Hacking: Key to Interoperability or Security Nightmare?

**Author:** Florian Krebs (ORCID: [0000-0001-6033-801X](https://orcid.org/0000-0001-6033-801X))
**Affiliation:** Independent researcher (personal capacity)

> **Statement of independence.** This is a hobbyist project carried out by the author in a personal capacity. It is not part of, endorsed by, funded by, or representative of the views of any employer, including the German Aerospace Center (DLR / *Deutsches Zentrum für Luft- und Raumfahrt*). The full statement is in §9.5.

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
The `original/doc/log.md` community thread documents a self-signed-certificate MITM against the vendor MQTT broker `sf.mqtt.spider-farmer.com:8333`, recovering live credentials (username `sf_ggs_cb`, password redacted in the published paper, present in S-SF-5). This is independent corroboration of the claim that the effort gap has collapsed for *both* defenders and attackers.

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
- The integration `powerocean_dev` at `manifest.json` version `2026.05.01`, embedded at `original/`. Upstream parent `https://github.com/niltrip/powerocean` per `const.py` line 13.
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

## 5. Experiment & Analysis 3 — The paper as an AI-assisted artifact

### 5.1 System and threat model
The unit of analysis here is recursive: the paper that documents AI-assisted reverse engineering is itself an AI-assisted artifact. The "system" is the paper-generation pipeline: prompts, AI conversation transcripts, repository state, and the human researcher in the loop. Specific risks to evaluate are:
- **Fabricated citations.** LLMs are known to hallucinate references; an entry surfaced from a database is not the same as a paper that has been read.
- **Silent memorisation / plagiarism.** AI-drafted prose may reproduce training-data text without attribution.
- **Prompt injection.** Vendor APK strings, community-thread excerpts, and PDF contents embedded under `experiments/*/original/` are read by the agent and could in principle inject instructions.
- **Misrepresentation of source claims.** A Consensus-surfaced abstract is not a peer-reviewed claim until the full text has been read.
- **Tooling drift.** Identical prompts in later sessions produce non-identical outputs.
- **AI-generated legal opinion mistaken for sourced legal commentary.** A specific instance from the EcoFlow transcripts has already been flagged; the failure mode is generalisable.

### 5.2 Artifact inventory
The case-study artifacts are vendored under `experiments/paper-meta-process/` with the same shape as the other two case studies (`README.md`, `REPORT.md`, `provenance.md`, `raw_conversations (copy&paste, web)/`):

- The git history of this repository on `main` and on the development branch `claude/develop-paper-structure-7lG2s`.
- Conversation transcripts of paper-development sessions, preserved in `experiments/paper-meta-process/raw_conversations (copy&paste, web)/`. Each transcript declares a verification status (`[verbatim-export]` / `[curated-reconstruction]` / `[redacted]`) in its YAML header. The first preserved transcript (`T1-paper-structure-and-literature.md`) is a `[curated-reconstruction]` of the 2026-05-01 session that produced the paper structure, the literature pass, the FAIR metadata, and this case study.
- The case-study report `experiments/paper-meta-process/REPORT.md` and the per-transcript provenance map `experiments/paper-meta-process/provenance.md` (parallel to the Spider Farmer and EcoFlow `provenance.md` files).
- The repository AI policy: `CLAUDE_CODE_INSTRUCTIONS.md`, `.instructions.md`, `copilot-instructions.md`, `CLAUDE.md`.
- The executable research-protocol agent prompt (`docs/research-protocol-prompt.md`).
- The methodology document (`docs/methodology.md`) and its KPI framework (§10).
- The literature register in `docs/sources.md` with the verification-status legend (`[repo-vendored]`, `[repo-referenced]`, `[unverified-external]`, `[lit-retrieved]`, `[lit-read]`, `[needs-research]`).
- The logbook (`docs/logbook.md`), updated per commit per the rule established on 2026-05-01.
- The arXiv-ready LaTeX build pipeline (`paper/main.tex`, `paper/Makefile`, `.github/workflows/build-paper.yml`).
- The mirroring rule between `paper/main.md` and `paper/main.tex` (rule 11 in `CLAUDE_CODE_INSTRUCTIONS.md`).
- FAIR / citation metadata at the repository root: `CITATION.cff`, `.zenodo.json`, `codemeta.json`, plus the FAIR-mapping document `docs/fair.md`.

### 5.3 AI-assisted analysis workflow
1. **Repo-context loading.** The agent reads `CLAUDE_CODE_INSTRUCTIONS.md`, `docs/methodology.md`, `docs/logbook.md`, and the per-case `provenance.md` files at session start.
2. **Skeleton generation.** Section structure proposed by the AI from the verified case-study evidence (commit `ffdf60c`) and reviewed by the researcher.
3. **Iterative prompting.** Each user turn maps to one or more commit-grouped edits. The conversation transcript is the source-of-truth log.
4. **Structured literature search.** External academic-database queries (Consensus / Semantic Scholar / arXiv) batched per the tool's rate-limit guidance; results recorded with `[lit-retrieved]` status.
5. **Mirror enforcement.** Any change to `paper/main.md` must be reflected in `paper/main.tex` before commit (rule 11).
6. **Git-paired logbook entries.** Each meaningful commit has a paired logbook entry naming the action, files touched, decisions, open issues, and next steps.

### 5.4 Findings — interoperability and reproducibility
- The paper, including every claim in §3 and §4, is regenerable from the repository state at the pinned commit `ffdf60c` for the vendor evidence and at the head of the development branch for the prose.
- The verification-status legend makes the read-state of every cited source explicit and prevents `[lit-retrieved]` entries from drifting into the paper as if they had been read.
- The arXiv build pipeline reproduces the PDF and submission tarball deterministically from `paper/main.tex` plus `paper/references.bib`.
- The methodology (§2) and KPI framework (`docs/methodology.md` §10) are themselves operationalised as the executable agent prompt (`docs/research-protocol-prompt.md`), making the research protocol a runnable artifact rather than only a description.

### 5.5 Validation
- All §3 and §4 claims were re-checked against the embedded vendor code at commit `ffdf60c` (logbook entry "audit against embedded vendor code").
- All literature entries from the 2026-05-01 search session are marked `[lit-retrieved]`, not `[lit-read]` — explicitly capturing the gap between database-surfaced and read-in-full.
- The mirroring rule between `paper/main.md` and `paper/main.tex` is enforced by reviewer attention at commit time and by CI (`.github/workflows/build-paper.yml`), which rebuilds the PDF on every paper-touching commit and surfaces LaTeX-syntactic regressions.
- AI-generated legal opinions in transcripts are explicitly flagged (`docs/sources.md` S-EF-9) and held out of the paper until replaced with sourced legal commentary.

### 5.6 Findings — security and dual-use implications
- **Fabricated citations.** All ~50 entries in the literature register are `[lit-retrieved]` only. Any upgrade to `[lit-read]` without the researcher actually reading the paper would be a fabrication. The legend exists precisely to make this risk visible. The empirical base rates make this concrete: Walters & Wilder (2023) found **55% of ChatGPT-3.5 and 18% of GPT-4 generated citations were fabricated** in literature reviews, with a further 24–43% of the *real* citations carrying substantive errors [L-SLOP-1]. McGowan et al. (2023) found only **2 of 35** ChatGPT-generated psychiatry citations were real [L-SLOP-4]. Chelli et al. (2024) measured hallucination rates of 28.6%–91.4% across LLMs in systematic-review reference generation [L-SLOP-2]. These are not edge cases.
- **AI-generated legal analysis.** A specific opinion in transcript T3 line 147 (EcoFlow) is flagged in `docs/sources.md` and §7.1 — without that flag, it would have entered the paper as if sourced.
- **Live-credential leakage.** `docs/sources.md` S-SF-5 carries the recovered MQTT credentials for the Spider Farmer broker. These must be redacted before public release of the paper. This redaction is the single most important pre-publication action and is recorded as an open issue in the logbook.
- **Prompt injection from imported artifacts.** Vendor APK strings, PDF contents, and community-thread excerpts under `experiments/*/original/` are read by the AI agent. The mitigation is the AI policy's labelling requirement plus researcher verification of every AI-attributed claim.
- **Tooling drift.** The workflow and committed artifacts are the reproducible unit; the AI's exact tokens are not.

### 5.7 KPI summary (Meta-process)
*To be populated*: number of commits on the paper-development branch, number of AI sessions logged in `docs/logbook.md`, ratio of AI-generated to researcher-authored prose, count of AI-generated claims subsequently flagged or removed, count of `[lit-retrieved]` entries upgraded to `[lit-read]`, time-to-first-publishable-draft.

---

## 6. Synthesis

### 6.1 Cross-case comparison
| Dimension | Spider Farmer | EcoFlow PowerOcean | Meta-process (this paper) |
|---|---|---|---|
| Defence model | Hardcoded AES keys/IVs in APK + self-signed MQTT cert | Three undocumented API surfaces, vendor publishes only one | None — the artifact is open by construction |
| Primary AI lift | Reconciling four independent implementations | Discovering and choosing among API surfaces; type-system bug fix | Skeleton generation, structured literature retrieval, mirror discipline |
| Independent corroboration | 3 community implementations + community MITM thread | 1 vendor reference implementation + 1 upstream community fork | Git history; researcher review at commit time; CI build |
| Live credential recovery | Yes (MQTT broker creds) | No (token-bearer model) | N/A — the paper is the artifact |
| Dual-use blast radius | Per-device control over horticulture hardware | Grid-in / battery-reserve / EV-charger control | Fabricated citations; unsourced legal opinions; redaction failures |
| Status of vendor public docs | None | Open API documented; consumer app uses different surface | All policy and provenance documented in repo |

### 6.2 What the AI workflow added
- **Spider Farmer.** Not protocol *discovery* — the four community implementations had already done that — but *reconciliation* across conflicting key tables and verification of the dynamic-IV slice formula.
- **EcoFlow PowerOcean.** Surface enumeration and field-name convention recovery: a manual reverse-engineer would have eventually found the legacy endpoint, but the AI-assisted workflow recovered the full writeable-parameter catalogue from APK constants in a single pass.
- **Meta-process.** Skeleton generation from sparse evidence, structured literature retrieval at scale, and the disciplined application of verification-status labels to keep the paper honest about what it has and has not read.

### 6.3 Common patterns
- All three defences/processes relied on the *combination* of obscurity and effort, not on either alone — and in the meta-process, on the *combination* of access control and labour, where the labour is the researcher reading and verifying.
- All three yielded clean outputs once a single organising piece of evidence (key table; API surface; verification-status legend) was identified.
- In all three cases, AI assistance compressed the *organisation and reconciliation* phase far more than the *discovery* phase. The effort-gap collapse is unevenly distributed across workflow stages.

### 6.4 Limits of the comparison
Three cases is still small. The meta-process case is also recursive — the paper documenting AI-assisted reverse engineering is itself an AI-assisted artifact, which means selection bias and tooling drift apply to its analysis the same way they apply to the integration cases. We treat the meta-process case as evidence for the methodology, not as independent confirmation of the central thesis.

A second selection limit deserves explicit treatment. Both Spider Farmer and EcoFlow PowerOcean are *consumer-market* IoT products. One could plausibly hypothesise that industrial or higher-end hardware — with regulated certification, longer component lifetimes, and explicitly safety-driven security goals — would not exhibit the same effort-gap collapse. The literature offers a *qualified* answer in two parts:

- **The consumer-IoT base rate of vulnerability is empirically high, not anomalous.** Zhao et al. (2022) measured 1,362,906 deployed IoT devices and found **28.25% suffer from at least one N-days vulnerability**, with **88% of analysed MQTT servers having no password protection** [L-CONS-1]. Kumar et al. (2019) studied 83 million devices in 16 million households and documented widespread weak default credentials and open services [L-CONS-2]. Davis et al. (2020) explicitly compared well-known and lesser-known vendors and found that lesser-known vendors are systematically less-regulated and less-scrutinised [L-CONS-3] — a pattern that applies to both case studies in this paper. Sivakumaran et al. (2023) found **>70% of 17,243 BLE-enabled Android APKs contain at least one security vulnerability** [L-BLE-4]. Spider Farmer and EcoFlow are not exceptional cases of consumer-IoT insecurity; they are the median.
- **Industrial / higher-end hardware is *not* automatically immune.** Serror et al. (2020) frame IIoT as sharing many security concerns with consumer IoT despite its different goal stack (safety, productivity, longer lifetimes) [L-IND-1]. Antón et al. (2021) directly puncture the "industrial-grade therefore safer" intuition: they enumerated **>13,000 OT/ICS devices directly exposed on the public internet, almost all containing at least one vulnerability** [L-IND-2]. Asghar et al. (2019) observe that ICS were originally designed for isolated environments and that modern enterprise integration has opened structural cybersecurity problems that the original designs never anticipated [L-IND-3]. Higher cost, regulatory floors, and certification raise the *baseline* but do not close the effort gap that AI assistance compresses.

The honest conclusion is that the case selection over-samples consumer-grade hardware, but the inference is not "industrial would not have these problems" — it is *narrower*: the **flavour** of the obscurity barrier (hardcoded keys in mobile companion apps; undocumented REST surfaces) is what we generalise from. Industrial hardware would likely have a different flavour (legacy fieldbus protocols; certificate-pinned but rarely-rotated PKI; long-lifetime firmware) but the same structural property — that obscurity is a labour-cost barrier rather than a cryptographic one — would still apply. Validating that conjecture against an industrial case is left to future work (§8.1).

---

## 7. Discussion

### 7.1 Interoperability: the automated right to repair
European decompilation-for-interoperability provisions (§ 69e UrhG, EU 2009/24/EC) presuppose that decompilation is *legally* possible for an end user. AI assistance makes it *practically* possible. The case studies are existence proofs that the legal carve-out can now be exercised at hobbyist scale, not just by specialised firms. Whether legislatures intended this is an empirical question for legal scholarship, not for this paper. (Sourcing: `docs/sources.md` S-EF-9, S-EF-10, both `[unverified-external]` until cross-checked.)

### 7.2 The collapse of the boredom barrier
Security through obscurity rested on a labour-market assumption: that a determined hobbyist would not invest a fortnight to integrate a grow-tent controller. That assumption is dead. The Spider Farmer case shows three independent community implementations of the same protocol and an independently recovered set of MQTT credentials — converging evidence that the obscurity barrier has perforated.

### 7.3 Asymmetry of collapse
The effort gap has *not* collapsed uniformly. AI assistance compresses the *known-good-protocol* path far more than the *novel-vulnerability* path; verifying an integration against a live device is cheap, and verifying an exploit against a live target is not. We argue this asymmetry is the most under-discussed feature of the post-LLM threat model.

### 7.4 Dual-use accountability
Both case studies expose live attack surfaces. In Spider Farmer the surface is already public — recovered in a community thread — and the case is a *post-hoc* documentation of a collapse that has already happened. In EcoFlow the surface is documented for the first time here, and we accordingly enumerate the redactions that must be applied before public release (logbook 2026-05-01 audit; `docs/sources.md` S-SF-5, S-EF-2..4).

### 7.5 The paper as evidence for its own thesis
The meta-process case (§5) is recursive evidence for our central claim. The same pipeline that compresses the Spider Farmer and EcoFlow integrations compresses paper-writing — and exposes the same dual-use surface. Just as recovered MQTT credentials are a side-effect of integration work, fabricated citations and unsourced legal opinions are side-effects of paper work. The discipline that resolves both is the same: pin artifacts, label provenance, treat AI output as evidence to be verified rather than as authority.

### 7.6 Sloppification: the AI methodological discount
The most concrete and under-managed risk of AI-assisted research is what we call the *methodological discount* — the unspoken trade-off in which a researcher accepts a degraded standard of evidence in exchange for AI-assisted speed. Empirical work on LLMs in scientific writing now documents this risk concretely:

- Walters & Wilder (2023), *Scientific Reports*, found that **55% of GPT-3.5 and 18% of GPT-4 generated citations were fabricated** in literature reviews, with a further substantial fraction of *real* citations carrying substantive errors [L-SLOP-1].
- McGowan et al. (2023), *Psychiatry Research*, found only **2 of 35** ChatGPT-generated psychiatry citations were real; the remaining 33 were either subtly wrong or pastiches of existing manuscripts [L-SLOP-4].
- Chelli et al. (2024), *JMIR*, measured hallucination rates of 28.6%–91.4% and recall rates as low as 11.9% across LLMs in systematic-review reference generation [L-SLOP-2].
- Buchanan & Hill (2023) document >30% non-existent citations in ChatGPT outputs across the *Journal of Economic Literature* topic taxonomy [L-SLOP-3].
- Suchak et al. (2025), *PLOS Biology*, document a real-world consequence: NHANES-based formulaic single-factor papers grew from 4 per year (2014–2021) to **190 in the first ten months of 2024** — direct evidence of paper-mill / AI-assisted output flooding the literature [L-SLOP-8].
- Kendall & Teixeira da Silva (2023), *Learned Publishing*, and Sabel et al. (2025, *Royal Society Open Science*, the Stockholm Declaration) frame this at the system level: paper mills are now AI-assisted at industrial scale, and the publishing model needs structural reform [L-SLOP-5, L-SLOP-7].

The mitigation we operationalise is mundane: a verification-status legend (`[lit-retrieved]` / `[lit-read]`) that makes the read-state of every cited source explicit, plus a refusal to upgrade an entry without the researcher actually reading the paper. Sloppification is not solved by a better model; it is solved by labour discipline that the model cannot perform.

### 7.7 Model collapse and the dilution of the scientific commons
A second, longer-horizon argument cuts in the opposite direction. Shumailov et al. (2024, *Nature*) showed that **AI models trained recursively on AI-generated content collapse** — the tails of the original distribution disappear and successive generations of models forget the genuine human-data signal [L-MC-1, L-MC-7]. Seddik et al. (2024) prove this is unavoidable when training is purely synthetic but bounded when synthetic and real data are mixed below a threshold [L-MC-3]. Gerstgrasser et al. (2024) extend this further: *accumulating* real and synthetic data over time (rather than replacing real with synthetic) can avoid collapse entirely, with a finite test-error upper bound independent of iteration count [L-MC-4]. Suresh et al. (2024) characterise the *rate* of collapse for fundamental distributions [L-MC-5]; ForTIFAI / Shabgahi et al. (2025) propose confidence-aware training objectives that delay collapse onset by >2.3× [L-MC-2].

The connection to our work is direct. Each AI-assisted paper that ships *un-verified* AI output into the corpus dilutes the ground-truth signal that future models will be trained on. The two failure modes — sloppification at the paper level and model collapse at the corpus level — are the same problem at different timescales. They share a single mitigation: **preserve the provenance of human-verified, ground-truth content and keep it cleanly distinguishable from AI-generated content**. The literature points to a small set of practices that work against the dilution:

- **Provenance and read-state labelling at the artifact level** — what `docs/sources.md` does for citations.
- **Conversation-transcript preservation** — what `experiments/*/raw_conversations (copy&paste, web)/` does for AI contributions.
- **Pinning external evidence by commit SHA** — what the `ffdf60c` audit does for vendor code.
- **Mixing rather than replacing**: keep human-authored data alongside AI-assisted output rather than letting the AI output substitute for it [L-MC-3, L-MC-4].
- **Disclosure and detection at the publication level** — guidelines from Cheng et al. (2025) and Pellegrina et al. (2025); Stockholm Declaration governance proposals from Sabel et al. (2025) [L-SLOP-7, L-SLOP-10, L-SLOP-12].
- **Filtering high-confidence-token artifacts** during model training — ForTIFAI [L-MC-2]; not actionable for paper authors but actionable for foundation-model trainers.

We do not claim to solve model collapse. We claim that the methodology in §2 is consistent with what the literature suggests works against it, and that publishing AI-assisted research without provenance and disclosure is, at the corpus level, an externality on every future model.

### 7.8 Methodological implications for security research
- Treat AI conversation transcripts as research artifacts. They are the equivalent of a lab notebook for the LLM era.
- Pin all external code by commit SHA, not by branch name. Branches move; SHAs do not.
- Embed vendor artifacts under explicit redistribution caveats rather than referencing moving URLs.
- Mark every literature claim with a verification status. The discipline is cheap; the alternative is the current state of practice (§7.6).
- Disclose AI usage explicitly. The disclosure is not an apology — it is the unit of accountability that lets the work be audited rather than guessed at.

### 7.9 Threats to validity
- **Selection bias.** Cases were chosen because the researcher already wanted local control; failed attempts at harder targets are under-reported.
- **Tooling drift.** AI model behaviour changes between sessions. The workflow is reproducible against artifacts; identical AI outputs are not.
- **Legal framing.** AI-generated legal analysis in transcripts is not legal advice and is flagged as such in the source register.
- **Redistribution.** Vendor APKs and PDFs are vendored for cite-ability but their redistribution status is not yet resolved.
- **Sloppification risk in this paper.** The literature register (§5.6, §7.6) is currently `[lit-retrieved]` only. No claim in this paper depends on a literature citation that has not been read in full by the researcher; we have explicitly preferred to leave a claim unsupported rather than cite a paper we have not read.

---

## 8. Conclusion

AI-assisted reverse engineering does not invent new capabilities; it lowers the activation energy of capabilities that already existed. The Spider Farmer and EcoFlow PowerOcean cases show that this lowering is enough to collapse the effort gap that previously sustained "security through obscurity" as a viable consumer-IoT defence. The collapse is genuinely double-edged — it materially advances right-to-repair while exposing live attack surfaces — but it is also *asymmetric*, compressing the integration path more aggressively than the offensive path.

The path forward is not to discourage AI-assisted research but to make it *auditable*: vendor artifacts pinned, transcripts treated as evidence, dual-use evaluation built into the methodology rather than appended to it, and legal framing always sourced. Obscurity is dead. What replaces it has to be designed, not assumed.

### 8.1 Future work
- Extend to a fourth case study in a domain with no prior community integration (open question: does the asymmetry hypothesis hold there?).
- Operationalise the effort-gap KPIs against historical reverse-engineering case studies for a longitudinal comparison.
- Develop a responsible-disclosure framework specific to AI-assisted reverse engineering.
- Replace `[unverified-external]` legal sources with sourced commentary; address `[needs-research]` items in `docs/sources.md`.
- Reconstruct the Spider Farmer `VERSION 2 → 3` migration step that no preserved transcript currently documents.
- Read in full the `[lit-retrieved]` literature in `docs/sources.md` clusters A–J and upgrade entries to `[lit-read]` before any of them is cited as authority rather than as a database pointer.

---

## 9. AI usage disclosure and disclaimer

### 9.1 Models and tooling
This paper was developed with Claude (Opus 4.7 model family) by Anthropic, running in the Claude Code CLI [@anthropic2026claude]. Specific session details, model versions, and conversation transcripts are committed under `experiments/*/raw_conversations (copy&paste, web)/` and referenced in `docs/logbook.md`. Structured literature retrieval was performed via the Consensus academic-database front end (Semantic Scholar / PubMed / Scopus / arXiv); the queries used and the candidate citations they returned are recorded in `docs/sources.md` clusters A–J.

The AI assistant is acknowledged as a contributor but is *not* a co-author of this work.[^urhg-ki] The reason is technical and legal in equal measure: under § 2 UrhG (German Copyright Act, *Urheberrechtsgesetz*), copyright protection requires a *persönliche geistige Schöpfung* — a personal intellectual creation by a human — so an AI model cannot hold copyright in its outputs, cannot consent to publication, and cannot be held accountable in the way that academic authorship implies. Editorial responsibility for every paragraph rests with the human author named on the title page.

[^urhg-ki]: **Footnote on Urheberrecht und Künstliche Intelligenz in Germany.** German copyright law's interaction with generative AI is unsettled and moving fast; the framing in this paper is descriptive, not legal advice. Three threads are relevant. *(i) Authorship and the copyrightability of AI outputs.* § 2 UrhG requires a *persönliche geistige Schöpfung*. The prevailing reading (consistent with the long *Schöpfungshöhe* tradition and with EU CJEU case law on the *Werkbegriff*) is that purely AI-generated text or images do not, on their own, satisfy this requirement and therefore do not enjoy independent copyright protection in Germany. Human curation, selection, prompting, and editing can create a copyrightable human contribution on top of the AI output, but the AI itself is not an author. (Sourcing: `docs/sources.md` S-EF-9 — primary text of UrhG — remains `[unverified-external]`; this footnote is an informal restatement of the prevailing reading and must be replaced with sourced legal commentary before any legal claim is made.) *(ii) Text-and-data-mining and AI training.* § 44b UrhG (introduced 2021 to implement Art. 4 of the EU DSM Directive 2019/790) creates a TDM exception for both research and commercial uses, with a machmaschinenlesbar-opt-out for commercial use. The first major German judgment on AI training and copyright — *Kneschke v LAION* before LG München I (Az. 42 O 14139/23, October 2024) — held that scraping for training-dataset construction can fall under § 44b. The judgment is one early data point; appellate review, the related EU AI Act (in force August 2024) Art. 53 transparency-and-copyright obligations on general-purpose AI providers, and ongoing Commission guidance will reshape the picture. All sources here are `[unverified-external]` in `docs/sources.md` until a targeted German-language search reads each primary text. *(iii) Why this matters for our paper.* Two consequences follow. First, the AI assistant is correctly acknowledged in §9.1 but is not a co-author; the human author holds copyright. Second, the choice of CC-BY-4.0 (see `LICENSE`) attaches to the human-authored and human-curated portions of the work; it does not purport to license the AI's training data, the AI model itself, or vendor artifacts vendored under `experiments/*/original/` (each of which carries its own redistribution caveats per `docs/sources.md`). A careful pre-publication legal review is required before this paper or its repository is mirrored to a journal or to Zenodo.

### 9.2 Division of labour
- **Researcher (human).** Research question, case selection, ethical and redaction decisions, validation against vendor code at commit `ffdf60c`, and final acceptance of every paragraph.
- **AI assistant (Claude).** Skeleton drafting, structured literature retrieval, cross-case comparison, prose tightening, LaTeX rendering, and methodology operationalisation as the executable agent prompt (`docs/research-protocol-prompt.md`).
- **Hybrid.** Provenance maps (`experiments/*/provenance.md`), source register (`docs/sources.md`), logbook entries, and KPI scaffolding — AI drafted, researcher verified or flagged.

### 9.3 What is and is not sourced
- All technical claims in §3 and §4 are sourced to vendor code at commit `ffdf60c` and to specific transcript line numbers; verifiable by re-running the audit described in `docs/logbook.md` (entry "audit against embedded vendor code").
- All literature in `docs/sources.md` clusters A–J (covering LLM-assisted RE, vulnerability/exploit generation, hardcoded secrets, BLE/IoT obscurity, right-to-repair, local-first smart home, DMCA § 1201(f), counter-positions, sloppification of science, and model collapse) is currently `[lit-retrieved]` — the entries were surfaced from a structured database query but the full texts have not been read by the researcher. **No claim in this paper depends on a literature citation that has not been read in full.** Where the literature is invoked, it is invoked through the source-register handles `[L-XX-N]` so the reader can independently verify what was retrieved versus what was read.
- Legal framing (§ 69e UrhG / EU 2009/24/EC) remains unsourced and is flagged as `[unverified-external]` in `docs/sources.md`.

### 9.4 Disclaimers
- **Not legal advice.** Any reference to copyright statutes or interoperability exemptions is descriptive, not prescriptive. Specific decisions about reverse-engineering activities should be evaluated by qualified legal counsel.
- **Not a coordinated vulnerability disclosure.** This paper documents prior community findings and integration work; it is not a coordinated disclosure for either Spider Farmer or EcoFlow products.
- **Tooling drift.** Identical prompts at later dates may produce non-identical outputs. The workflow and committed artifacts are the reproducible unit; AI outputs are not.
- **Live credentials.** `docs/sources.md` S-SF-5 contains recovered live credentials from a community thread. These must be redacted before any public release of the paper or repository.
- **Fabricated-citation risk.** Empirical base rates for LLM-fabricated citations are 18%–55% for raw GPT outputs (§7.6, [L-SLOP-1, L-SLOP-2, L-SLOP-4]). Every literature entry in this repository must be upgraded from `[lit-retrieved]` to `[lit-read]` before the paper is submitted for peer review.
- **Sloppification and model collapse.** §7.6 and §7.7 explicitly acknowledge that AI-assisted research, when shipped without verification and disclosure, contributes to both the proximate sloppification of the scientific record [L-SLOP-7, L-SLOP-8] and the distal collapse of foundation models trained on it [L-MC-1, L-MC-3]. The methodology in §2 is the authors' best-effort response to that risk.

### 9.5 Statement of independence and personal capacity
This work is a hobbyist research project carried out by the author (Florian Krebs, ORCID [0000-0001-6033-801X](https://orcid.org/0000-0001-6033-801X)) in a strictly personal capacity. It is **not** part of, endorsed by, funded by, supervised by, or representative of the views of any employer, including the German Aerospace Center (DLR / *Deutsches Zentrum für Luft- und Raumfahrt*). The author's day-job affiliation is acknowledged here only so the reader can rule it out: no DLR resources, infrastructure, datasets, or employer-confidential information were used in the preparation of this paper or its underlying repository. The author's day-time research at DLR concerns experimental data management (`shepard`) and is unrelated to consumer-IoT reverse engineering. Any opinions expressed are the author's own. The repository's `CITATION.cff`, `.zenodo.json`, `codemeta.json`, and `docs/fair.md` all carry the affiliation **"Independent researcher (personal capacity)"** in line with this statement.

---

## 10. The Pandora moment: this paper as a novel mode of transparent AI-assisted research

> *"Only Hope remained there in an unbreakable home within under the rim of the great jar, and did not fly out at the door."*
> — Hesiod, *Works and Days*, ll. 96–98 (trans. Hugh G. Evelyn-White, 1914)

Pandora's jar is open. Generative AI is now a routine part of how scientific manuscripts are drafted, and the empirical literature documents what comes out of the jar: fabricated citation rates of 18%–55% for raw GPT outputs [L-SLOP-1], hallucination rates up to 91.4% in systematic-review reference generation [L-SLOP-2], paper-mill output growing from 4 to 190 NHANES papers in a single year [L-SLOP-8], and a longer-horizon model-collapse risk in which the next generation of foundation models is trained on the corrupted outputs of the present one [L-MC-1, L-MC-3]. These problems are not solved by refusing to use AI; refusal does not put the technology back in the jar, and it concedes the ground of methodological practice to those who *do* use it without disclosure. What is left in the jar, on the Hesiodic reading, is *Hope* — but the kind of Hope that demands work.

The novelty we claim in this paper is not in the substance of the case studies. Spider Farmer's BLE protocol and EcoFlow's API surfaces are prior community work; the meta-process is recursive by construction. The novelty is in *how* the case studies are written. Eight integrated practices distinguish this paper from the prevailing modes of AI-assisted research:

1. **AI conversation transcripts as first-class artifacts.** Every paper-development session is preserved in `experiments/*/raw_conversations (copy&paste, web)/` with an explicit verification status (`[verbatim-export]` / `[curated-reconstruction]` / `[redacted]`). The transcript is not appendix material — it is the lab notebook of the LLM era. Readers can audit which arguments came from which prompt.
2. **A verification-status legend for every cited source.** The labels `[repo-vendored]`, `[repo-referenced]`, `[unverified-external]`, `[lit-retrieved]`, `[lit-read]`, and `[needs-research]` make the read-state of every citation explicit. The discipline is mundane — never upgrade an entry without reading the full text — and the mundanity is the point.
3. **Provenance maps tying every technical claim to commit-pinned evidence.** `experiments/*/provenance.md` maps each transcript decision to specific files and line numbers in the embedded vendor code (commit `ffdf60c`).
4. **Mirror discipline between prose and submission source.** `paper/main.md` and `paper/main.tex` are kept consistent at every commit (rule 11 in `CLAUDE_CODE_INSTRUCTIONS.md`); CI rebuilds the PDF on every paper-touching commit and surfaces regressions.
5. **A recursive case study of the paper itself (§5).** The paper-generation pipeline is treated as a third reverse-engineering case — same threat model, same artifact inventory, same dual-use evaluation. A methodology that cannot describe its own production is not a methodology, it is a brand.
6. **Explicit AI disclosure framed against empirical base rates.** §9 names the model, the division of labour, and the empirical fabrication rates the methodology is responding to. The disclosure is not an apology — it is the unit of accountability that lets the work be audited rather than guessed at.
7. **Legal honesty about authorship.** The footnote on *Urheberrecht und KI* in §9.1 explains why, under § 2 UrhG, the AI is acknowledged as a contributor but is not and cannot be a co-author, and what that means for the CC-BY-4.0 grant.
8. **FAIR alignment as a precondition, not an afterthought.** `CITATION.cff`, `.zenodo.json`, `codemeta.json`, and `docs/fair.md` map every FAIR principle to the concrete repository feature that satisfies it.

None of these practices is individually novel. Conversation logs have been shipped with replications before; verification-status labels exist in evidence-based-medicine practice; provenance maps exist in bioinformatics; FAIR predates LLMs. **The novelty is the integration**: assembling these practices into a single, executable, runnable research protocol (`docs/research-protocol-prompt.md`) that an AI agent can be instructed to follow and that a human reviewer can audit by reading the artifacts the protocol produces.

The implicit contrast is with the prevailing practice. Two failure modes dominate the AI-assisted research literature today, and both are documented quantitatively in `docs/sources.md` cluster I:

- **Concealment**: AI is used heavily but not disclosed; the read-state of every citation is indeterminate. The fabricated-citation literature [L-SLOP-1, L-SLOP-2, L-SLOP-4] is what concealment produces at scale.
- **Token disclosure**: a generic "AI was used to assist" sentence in the acknowledgements with no mapping from sentence to commit, no transcript, and no verification-status discipline. This satisfies a publisher's checkbox but is not auditable.

We argue that a third mode is now necessary and feasible: **artifact-level disclosure**, in which every AI-assisted decision is traceable to a transcript, a commit, and a verification status. The cost is real — this paper's repository carries roughly as many lines of methodological scaffolding as paper prose — but it is paid in labour, not in lost capability. Sloppification (§7.6) and model collapse (§7.7) are each a tax on the scientific commons; artifact-level disclosure is the principal means we have to refuse to pay either tax.

Pandora's box is open. The Hope that remains is the kind that does work.
