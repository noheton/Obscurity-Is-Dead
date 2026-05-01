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
- **[lit-retrieved]** — surfaced through a structured academic-database query (Consensus / Semantic Scholar / Scopus / arXiv). Title, authors, abstract, venue, citation count, and DOI/URL have been recorded from the database, but the full text has not yet been read by the researcher.
- **[lit-read]** — full text has been read by the researcher and the entry's relation to a paper claim has been confirmed.
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

The literature register below was populated from a Consensus structured search session on 2026-05-01. Entries are marked **[lit-retrieved]** — the database returned matching titles, authors, abstracts, venue, citation counts, and direct URLs, but the full text has not yet been read. Each entry must be re-checked and upgraded to **[lit-read]** before its claim is used in the paper. Open issues at the bottom of this section list the literature gaps that remain.

The register is organised by paper claim. Inline IDs (`L-RE-1` etc.) are stable handles for cross-referencing from `paper/main.md`.

---

### Claim cluster A — LLM-assisted reverse engineering compresses the integration path
*Supports the "effort gap" framing in `paper/main.md` §1.1 and the asymmetry argument in §6.3.*

- **L-RE-1** [LLM4Decompile: Decompiling Binary Code with Large Language Models](https://consensus.app/papers/details/4839da33bde65e739f34bf48615a2a4a/?utm_source=claude_desktop) (Tan et al., 2024, 42 citations). **[lit-retrieved]**. Open-source 1.3B–33B LLMs outperform GPT-4o and Ghidra on HumanEval/ExeBench by >100% in re-executability rate. Supports: LLM tooling materially reduces decompilation effort.
- **L-RE-2** [DeGPT: Optimizing Decompiler Output with LLM](https://consensus.app/papers/details/069dc2908430571dbe8a97f63296c5ce/?utm_source=claude_desktop) (Hu et al., 2024, NDSS, 55 citations). **[lit-retrieved]**. Reports 24.4% reduction in cognitive burden of understanding decompiler output. Empirically anchors the "effort gap" claim.
- **L-RE-3** [REx86: A Local LLM for Assisting in x86 Assembly Reverse Engineering](https://consensus.app/papers/details/b7dec8058194576cbaf5a9b75fbb87f2/?utm_source=claude_desktop) (Lea et al., 2025). **[lit-retrieved]**. User study (n=43) where correct-solve rate rises from 31% → 53% with LLM assistance (p=0.189, not statistically significant at α=0.05). Quantitative anchor *and* a cautionary note for the magnitude of the effect.
- **L-RE-4** [Pop Quiz! Can a Large Language Model Help With Reverse Engineering?](https://consensus.app/papers/details/56ddc6b691095aefb3c188802f67f896/?utm_source=claude_desktop) (Pearce et al., 2022, 31 citations). **[lit-retrieved]**. Codex answered 72,754/136,260 questions correctly; concludes LLMs are "not yet ready for zero-shot reverse engineering". **Partially contradicts** the strong-form effort-gap claim; cite to keep the framing honest.
- **L-RE-5** [Exploring the Efficacy of LLMs (GPT-4) in Binary Reverse Engineering](https://consensus.app/papers/details/b3233d7b8b2557ccb821959c9a53e4d6/?utm_source=claude_desktop) (Pordanesh et al., 2024). **[lit-retrieved]**. Effective at general code understanding, weaker on technical/security analysis — qualified support.
- **L-RE-6** [An empirical study on the effectiveness of LLMs for binary code understanding](https://consensus.app/papers/details/524e60785850562b8ca74abdaf7c7004/?utm_source=claude_desktop) (Shang et al., 2025, *Empirical Software Engineering*). **[lit-retrieved]**. Multi-architecture, multi-optimisation benchmark.
- **L-RE-7** [ReCopilot: Reverse Engineering Copilot in Binary Analysis](https://consensus.app/papers/details/276e95e6b815565d9a5261fa202a130b/?utm_source=claude_desktop) (Chen et al., 2025). **[lit-retrieved]**. 13% improvement over prior LLMs/tools on function-name recovery and variable-type inference.
- **L-RE-8** [Extending Source Code Pre-Trained LMs to Summarise Decompiled Binaries (BinT5)](https://consensus.app/papers/details/36c5a9ca343755ce829365b31a96b69b/?utm_source=claude_desktop) (Al-Kaswan et al., 2023, SANER, 42 citations). **[lit-retrieved]**.

---

### Claim cluster B — LLM-assisted vulnerability discovery and exploit generation (asymmetry-of-collapse hypothesis)
*Tests `paper/main.md` §6.3: the integration path compresses faster than the offensive path.*

- **L-VD-1** [Good News for Script Kiddies? Evaluating LLMs for Automated Exploit Generation](https://consensus.app/papers/details/68f5ea4b57e252c1b2828b99affb7da6/?utm_source=claude_desktop) (Jin et al., 2025, IEEE SPW). **[lit-retrieved]**. **Directly supports the asymmetry hypothesis**: "no model successfully generates exploits for refactored labs" — LLMs are far more cooperative than competent at AEG. Strongest single citation for §6.3.
- **L-VD-2** [A Systematic Study on Generating Web Vulnerability PoCs Using LLMs](https://consensus.app/papers/details/ab41cf96d89b56b08d94d9fa5430db46/?utm_source=claude_desktop) (Zhao et al., 2025). **[lit-retrieved]**. 8–34% PoC success rate with public CVE info alone, rising to 68–72% with adaptive reasoning; 23 LLM-generated PoCs accepted by NVD/Exploit-DB. **Partially contradicts L-VD-1** — note the gap between refactored labs and disclosed CVEs.
- **L-VD-3** [Automated Vulnerability Validation and Verification: An LLM Approach](https://consensus.app/papers/details/15e2c0dbc2a55525acf3ee171ed5eb05/?utm_source=claude_desktop) (Lotfi et al., 2025). **[lit-retrieved]**. End-to-end CVE-to-containerised-exploit pipeline; relevant to the "post-disclosure window" argument.
- **L-VD-4** [A Survey on LLM Security and Privacy: The Good, the Bad, and the Ugly](https://consensus.app/papers/details/8fc0614195e850158590c5bd0ac4a4b4/?utm_source=claude_desktop) (Yao et al., 2023, 841 citations). **[lit-retrieved]**. Cornerstone survey for the dual-use framing.
- **L-VD-5** [Exploiting Programmatic Behavior of LLMs: Dual-Use Through Standard Security Attacks](https://consensus.app/papers/details/a596dd8dfa595bb2bc803d603a7cd104/?utm_source=claude_desktop) (Kang et al., 2023, IEEE SPW, 307 citations). **[lit-retrieved]**. Quantifies the cost asymmetry: LLMs produce malicious content $125–500× cheaper than human effort.
- **L-VD-6** [Harnessing LLMs for Software Vulnerability Detection: A Comprehensive Benchmarking Study](https://consensus.app/papers/details/12350d74c097598693fdfb4afa0ee740/?utm_source=claude_desktop) (Tamberg et al., 2024, IEEE Access). **[lit-retrieved]**. LLMs > traditional static analysis on recall/F1 but with more false positives.
- **L-VD-7** [LLMs in Software Security: A Survey of Vulnerability Detection Techniques](https://consensus.app/papers/details/5eb5b0fbb905556ab2a07612797aeab7/?utm_source=claude_desktop) (Sheng et al., 2025, *ACM Computing Surveys*). **[lit-retrieved]**.
- **L-VD-8** [LLM for Vulnerability Detection and Repair: Literature Review](https://consensus.app/papers/details/6d46f168f54a5557928be22b39728c7a/?utm_source=claude_desktop) (Zhou et al., 2024, *ACM TOSEM*, 57 citations). **[lit-retrieved]**.
- **L-VD-9** [Enhancing RE: Benchmarking LLMs for Vulnerability Analysis in Decompiled Binaries (DeBinVul)](https://consensus.app/papers/details/15fcaa0190795019be20b791aa10e5d0/?utm_source=claude_desktop) (Manuel et al., 2024). **[lit-retrieved]**. 19–24% performance increase after fine-tuning on decompiled binaries; relevant to the binary side of vulnerability discovery.

---

### Claim cluster C — Hardcoded secrets in mobile apps are systemic, not exceptional
*Supports the Spider Farmer §3.6 finding that recovered MQTT credentials are typical, not anomalous.*

- **L-HC-1** [Evaluating LLMs in detecting Secrets in Android Apps (SecretLoc)](https://consensus.app/papers/details/52233c9b10cd578992087c98a1ddf9d1/?utm_source=claude_desktop) (Alecci et al., 2025). **[lit-retrieved]**. **Strongest single citation for the Spider Farmer thesis**: of 5,000 Google Play apps, **42.5%** contain hardcoded secrets; 4,828 secrets missed by regex/static/ML methods recovered by LLMs. Authors explicitly name the dual-use risk: "if analysts can uncover these secrets with LLMs, so can attackers."
- **L-HC-2** [Hardcoded credentials in Android apps: Service exposure and category-based analysis](https://consensus.app/papers/details/6e0e942c75ef51138c637c504e7a5647/?utm_source=claude_desktop) (Mykhaylova et al., 2024). **[lit-retrieved]**. 6,165 APKs analysed via MobSF + Trufflehog.
- **L-HC-3** [How far are app secrets from being stolen? a case study on android](https://consensus.app/papers/details/26baf21595d454fabe121a5ec9294355/?utm_source=claude_desktop) (Wei et al., 2025, *Empirical Software Engineering*). **[lit-retrieved]**. 575 potential secrets from 14,665 popular apps; 3,711 distinct exploitable secrets harvested via automatic analysis.
- **L-HC-4** [Hardcoded Secrets Unveiled: Static Access Token Exploitation in Real-World Android Applications](https://consensus.app/papers/details/4c6dad2e8aff5aa1a76bda178ce8d206/?utm_source=claude_desktop) (Domonkos et al., 2025, IEEE CogInfoCom). **[lit-retrieved]**. 20 weather apps; concludes "it is not possible to securely hide sensitive information within applications" — direct contradiction of the obscurity-as-defence model.
- **L-HC-5** [DroidKey: A Practical Framework and Analysis Tool for API Key Security in Android Applications](https://consensus.app/papers/details/b4c46b096e055773a4aff4109dfec9b8/?utm_source=claude_desktop) (Piyumantha et al., 2025). **[lit-retrieved]**. Banking-app evaluation: widespread hardcoded-key vulnerabilities.
- **L-HC-6** [KeyDroid: A Large-Scale Analysis of Secure Key Storage in Android Apps](https://consensus.app/papers/details/3c6370250a425d3d85d1096dbc922c86/?utm_source=claude_desktop) (Blessing et al., 2025). **[lit-retrieved]**. 490,119 apps surveyed: **56.3% of apps self-reporting sensitive-data processing do not use trusted hardware at all**. Foundational evidence that the obscurity-default is the industry baseline.
- **L-HC-7** [Automatically Detecting Checked-In Secrets in Android Apps: How Far Are We?](https://consensus.app/papers/details/d1f7507b9aaa5cb49cad5701263d4d81/?utm_source=claude_desktop) (Li et al., 2024). **[lit-retrieved]**. Compares Three-Layer Filter, LeakScope, PassFinder on 5,135 apps; 2,142 secrets across 2,115 apps.
- **L-HC-8** [A survey of android application and malware hardening](https://consensus.app/papers/details/57c265748d615638945c3da0709b0d77/?utm_source=claude_desktop) (Sihag et al., 2021, *Comp Sci Rev*, 64 citations). **[lit-retrieved]**. Survey of obfuscation/hardening techniques and their evasion — provides the "obscurity-as-defence" baseline.

---

### Claim cluster D — Security through obscurity in consumer IoT and BLE
*Supports `paper/main.md` §1.1 (effort gap as security model) and §3 (Spider Farmer BLE protocol).*

- **L-BLE-1** [Security and Privacy Threats for BLE in IoT and Wearable Devices: A Comprehensive Survey](https://consensus.app/papers/details/9c6fb9cba9ab5492a39dbdba3a1d1019/?utm_source=claude_desktop) (Barua et al., 2022, *IEEE OJ Communications Society*, 97 citations). **[lit-retrieved]**. Most-cited recent BLE-IoT vulnerability survey.
- **L-BLE-2** [A survey on Bluetooth Low Energy security and privacy](https://consensus.app/papers/details/715f8ff204885de698417d8efd21ecc3/?utm_source=claude_desktop) (Cäsar et al., 2022, *Computer Networks*, 55 citations). **[lit-retrieved]**. Versioned weakness catalogue.
- **L-BLE-3** [Key Negotiation Downgrade Attacks on Bluetooth and BLE](https://consensus.app/papers/details/acf4526ad3f85ba38d70d9d4f86fcaea/?utm_source=claude_desktop) (Antonioli et al., 2020, *ACM TOPS*, 45 citations). **[lit-retrieved]**. Standard-compliant entropy-downgrade attacks against 19 BLE devices.
- **L-BLE-4** [Uncovering Vulnerabilities of BLE IoT from Companion Mobile Apps with Ble-Guuide](https://consensus.app/papers/details/2ca22ef2aae75e239b528ea6a0f50e1a/?utm_source=claude_desktop) (Sivakumaran et al., 2023, *AsiaCCS*). **[lit-retrieved]**. **>70% of 17,243 BLE-enabled Android APKs contain at least one security vulnerability.** Strong base-rate citation.
- **L-BLE-5** [Living in the Past: Analyzing BLE IoT Devices Based on Mobile Companion Apps in Old Versions](https://consensus.app/papers/details/12309b92f63459f490b8991573566da1/?utm_source=claude_desktop) (Du et al., 2023). **[lit-retrieved]**. Documents the exact pattern observed in Spider Farmer: vendors update companion APKs to raise the RE bar **without** patching the underlying device firmware. Direct support for the "obscurity, not security" critique.
- **L-BLE-6** [On the Security of BLE in Two Consumer Wearable Heart Rate Monitors / Sensing Devices](https://consensus.app/papers/details/710d2aef559b53a28c4df62784d89b0f/?utm_source=claude_desktop) (Peker et al., 2022, *Sensors*). **[lit-retrieved]**. Manufacturers fail to comply with BLE standard security mechanisms despite the standard providing them.
- **L-BLE-7** [InternalBlue — Bluetooth Binary Patching and Experimentation Framework](https://consensus.app/papers/details/5384b26bb3ce5a34900bb00c50df1ea0/?utm_source=claude_desktop) (Mantz et al., 2019, *MobiSys*, 53 citations). **[lit-retrieved]**. Methodologically relevant: reverse-engineered Broadcom Bluetooth chipsets as research artifact.
- **L-BLE-8** [A Thorough Security Analysis of BLE Proximity Tracking Protocols](https://consensus.app/papers/details/9d8c968da4d956c5b2ad12172c43f939/?utm_source=claude_desktop) (Liu et al., 2025). **[lit-retrieved]**. Reverse-engineering of closed-source BLE protocols (Apple Find My, Samsung Find My Mobile) reveals seven new vulnerabilities — methodological parallel to our case studies.
- **L-BLE-9** [ESPwn32: Hacking with ESP32 System-on-Chips](https://consensus.app/papers/details/995fa7b9157d5cbbbcbaa75e753c380c/?utm_source=claude_desktop) (Cayre et al., 2023, IEEE SPW). **[lit-retrieved]**. Software-only repurposing of ESP32 to attack BLE / ANT / Zigbee / Thread — relevant for the threat-model section.

---

### Claim cluster E — Right-to-repair and IoT interoperability (legal/policy)
*Supports `paper/main.md` §1.3 motivation and §6.1 ("automated right to repair").*

- **L-RR-1** [Towards a right to repair for the Internet of Things: A review of legal and policy aspects](https://consensus.app/papers/details/3754511a8dc954ffbadd7082fd5d0ec0/?utm_source=claude_desktop) (Boniface et al., 2024, *Computer Law & Security Review*, 15 citations). **[lit-retrieved]**. Most directly on-thesis review of right-to-repair specifically applied to IoT. Primary anchor for §1.3.
- **L-RR-2** [Laying foundations for a "Right to Improve"](https://consensus.app/papers/details/58b55375979a5498bb4573a464a0c668/?utm_source=claude_desktop) (Lebloch et al., 2024, *Frontiers in the Internet of Things*). **[lit-retrieved]**. Argues current EU legislation and voluntary interoperability initiatives fail to address modification/extension/repurposing of IoT devices — direct motivation for our work.
- **L-RR-3** [The Right to Repair (R2R) Cards: Aligning Law and Design For A More Sustainable Consumer IoT](https://consensus.app/papers/details/6cd97bd4e2da54a0ac6425c675d55b6d/?utm_source=claude_desktop) (Urquhart et al., 2024, *NordiCHI*). **[lit-retrieved]**. Consolidates 25 pieces of UK/EU legislation into 90 legal requirements — useful as a checklist of the legal landscape.
- **L-RR-4** [The Internet of Forgotten Things: European Cybersecurity Regulation and IoT Manufacturer Cessation](https://consensus.app/papers/details/c4128fe587b05cff84cc84692fc7989f/?utm_source=claude_desktop) (van 't Schip, 2024). **[lit-retrieved]**. Argues that current EU legislation has a blind spot for manufacturer cessation — directly supports the EcoFlow use case.
- **L-RR-5** [Turning the crossroad for a connected world: reshaping the European prospect for the IoT](https://consensus.app/papers/details/6663e907f44b54ab8fddd6cea72711ae/?utm_source=claude_desktop) (Ünver, 2018, *Int. J. Law Inf. Technol.*). **[lit-retrieved]**. EU legal toolbox analysis for IoT vendor lock-in.
- **L-RR-6** [Barriers, enablers and market governance: A review of the policy landscape for repair of consumer electronics in the EU and the U.S.](https://consensus.app/papers/details/635b82b4a83b581ba91efd7e3e5a21e5/?utm_source=claude_desktop) (Svensson-Hoglund et al., 2020, *Journal of Cleaner Production*, 95 citations). **[lit-retrieved]**. Comparative EU/US repair-market governance review.
- **L-RR-7** [Shaping Interoperability for the IoT: The Case for Ecosystem-Tailored Standardisation](https://consensus.app/papers/details/46708cd5eee45d6184e37089b94995d6/?utm_source=claude_desktop) (Colangelo et al., 2023, *European Journal of Risk Regulation*). **[lit-retrieved]**. Counter-argument to one-size-fits-all interoperability mandates — useful to qualify our enthusiasm.

---

### Claim cluster F — Local-first / cloud-independence in smart home
*Supports `paper/main.md` §1.3 motivation and §3/§4 (the integrations are local-first by construction).*

- **L-LF-1** [Modular IoT Architecture for Monitoring and Control of Office Environments Based on Home Assistant](https://consensus.app/papers/details/f740c3e94df1504e8c3c3072225ecb6e/?utm_source=claude_desktop) (Khomenko et al., 2025, *IoT*). **[lit-retrieved]**. Empirical Home-Assistant local-first deployment with throughput, fault-recovery, and energy-savings metrics. Most directly comparable to our integration target.
- **L-LF-2** [SoK: Privacy-enhancing Smart Home Hubs](https://consensus.app/papers/details/40d2e32b1739552d820198a99a734061/?utm_source=claude_desktop) (Zavalyshyn et al., 2022, *Proc. PETS*, 8 citations). **[lit-retrieved]**. Systematisation of 10 industrial / community smart-hub systems and 37 research proposals — the canonical SoK for this cluster.
- **L-LF-3** [Towards Privacy-Preserving Voice Control in Smart Home IoT: A Taxonomy](https://consensus.app/papers/details/5dc13423c0b8545f86b756f1c9373e25/?utm_source=claude_desktop) (Hewitt et al., 2024). **[lit-retrieved]**.
- **L-LF-4** [Voice-Based Personalized AI Assistant using Python and JavaScript (Vaani)](https://consensus.app/papers/details/5f1afb1c487153b28b7a51023ab1bffc/?utm_source=claude_desktop) (Mishra et al., 2025). **[lit-retrieved]**. Local-first voice assistant; complementary use case.
- **L-LF-5** [Adapting Smart Home Voice Assistants to Users' Privacy Needs using a Raspberry-Pi based and Self-Adapting System](https://consensus.app/papers/details/1ef6627f052751f9b9dbeac54c6e217e/?utm_source=claude_desktop) (Dallmer-Zerbe et al., 2021, IEEE ISIE). **[lit-retrieved]**.

---

### Claim cluster G — DMCA § 1201(f) and the legal interoperability exemption (US)
*Companion to S-EF-9 / S-EF-10 (§ 69e UrhG / EU 2009/24/EC, still `[unverified-external]`). Supports `paper/main.md` §6.1 — the European framing has a US analogue.*

- **L-LAW-1** [Interoperability under the DMCA](https://consensus.app/papers/details/be67520f7a8f59b0a23b2fb13add990f/?utm_source=claude_desktop) (Band, 2011). **[lit-retrieved]**. Legislative-history primer on § 1201(f); discusses *Chamberlain v. Skylink* as the doctrinal turning point.
- **L-LAW-2** [Circumventing the Competition: The Reverse Engineering Exemption in DMCA § 1201](https://consensus.app/papers/details/268991add3275dfca30a0d7fafafdd79/?utm_source=claude_desktop) (Neufeld, 2007, *Review of Litigation*). **[lit-retrieved]**. Analyses *Bnetd* — a paradigm case of community RE for interoperability.
- **L-LAW-3** [Rethinking Anticircumvention's Interoperability Policy](https://consensus.app/papers/details/2b2bcae967895dc4b0adadac5757c22f/?utm_source=claude_desktop) (Perzanowski, 2008). **[lit-retrieved]**. Argues for broadening the DMCA interoperability exemption — the policy direction our paper implicitly endorses.
- **L-LAW-4** [DMCA 101: Introduction to Section 1201](https://consensus.app/papers/details/9b935c604b015b8eb079b5432adc04e5/?utm_source=claude_desktop) (Liu, 2018). **[lit-retrieved]**. Primer-level reference.
- **L-LAW-5** [The Legality of Reverse Engineering and the Protection of Trade Secrets in the Software Industry](https://consensus.app/papers/details/df0faade099555e8a2a7f155c51bf469/?utm_source=claude_desktop) (Allahrakha, 2025). **[lit-retrieved]**. Doctrinal review with comparative context.
- **L-LAW-6** [Lexmark, Watermarks, Skylink and Marketplaces: Misuse and Misperception of the DMCA's Anticircumvention Provision](https://consensus.app/papers/details/86a591c9916955e48233dcd4661025f3/?utm_source=claude_desktop) (Torsen, 2004, *Chicago-Kent J. Intellectual Property*). **[lit-retrieved]**.

**Open**: § 69e UrhG (Germany) and EU 2009/24/EC remain **[unverified-external]** (S-EF-9, S-EF-10). A targeted German-language search is the next step.

---

### Claim cluster H — Counter-positions: interoperability and disclosure as risk amplifiers
*Direct dual-use counterweight to clusters E and F. Supports `paper/main.md` §6.4.*

- **L-COUNTER-1** [Security Implications of Interoperability](https://consensus.app/papers/details/2e40b4cc3e76531da3362c515e462256/?utm_source=claude_desktop) (Boniface et al., 2020). **[lit-retrieved]**. Frames interoperability explicitly as a security-cost optimisation problem; uses smart-manufacturing case study. **Most direct counter-citation to our enthusiasm for interoperability.**
- **L-COUNTER-2** [Information Disclosure and the Diffusion of Information Security Attacks](https://consensus.app/papers/details/d8de7afb60a25c61815a20f7fe282640/?utm_source=claude_desktop) (Mitra & Ransbotham, 2015, *Information Systems Research*, 83 citations). **[lit-retrieved]**. Foundational empirical study: full disclosure accelerates attack diffusion, increases penetration, and shortens time-to-first-attack. **Cite to qualify the "obscurity is dead" thesis** — full disclosure is not free.
- **L-COUNTER-3** [SoK: Security and Privacy of Blockchain Interoperability](https://consensus.app/papers/details/3f1ad25c63895e64924eddde8806abdb/?utm_source=claude_desktop) (Augusto et al., 2024, *IEEE S&P*, 63 citations). **[lit-retrieved]**. Cross-chain bridges accumulated ~$3.1B in losses; concrete instance of interoperability-as-attack-surface. Useful analogy even though the domain differs.
- **L-COUNTER-4** [Dual-use open source security software in organizations — Dilemma: Help or hinder?](https://consensus.app/papers/details/9da46e99b8735ad6b4f8d2a4795a68ad/?utm_source=claude_desktop) (Silic, 2013, *Computers & Security*, 24 citations). **[lit-retrieved]**. Triangulated study of the dual-use dilemma in organisational settings.
- **L-COUNTER-5** [Dual Use Deception: How Technology Shapes Cooperation in International Relations](https://consensus.app/papers/details/5f857faddeca5d45ad4d54e6fbfd263a/?utm_source=claude_desktop) (Vaynman & Gartzke, 2023, *International Organization*, 19 citations). **[lit-retrieved]**. Theoretical framing of dual-use distinguishability and integration — applicable to AI-assisted RE.
- **L-COUNTER-6** [An Attack Surface Metric](https://consensus.app/papers/details/027f6348256457f6957270659078f0fa/?utm_source=claude_desktop) (Manadhata & Wing, 2011, *IEEE TSE*, 658 citations). **[lit-retrieved]**. Foundational attack-surface formalisation; needed if we want to make the §4.6 (EcoFlow) "blast radius" claim quantitative rather than rhetorical.

---

### Coverage table — `[needs-research]` items resolved by this session

| Original `[needs-research]` item | Status after this session | Primary anchor(s) |
|---|---|---|
| "Effort gap" framing for AI-assisted RE | Candidates retrieved | L-RE-1, L-RE-2, L-RE-3, L-RE-4 (contradicts), L-RE-6 |
| "Security through obscurity" in consumer IoT / BLE | Candidates retrieved | L-BLE-1, L-BLE-4, L-BLE-5 |
| Right-to-repair literature in IoT and energy | Candidates retrieved | L-RR-1, L-RR-2, L-RR-4 |
| Local-first / cloud-independence in smart home | Candidates retrieved | L-LF-1, L-LF-2 |
| Legal interoperability carve-outs (DMCA § 1201(f)) | Candidates retrieved (US only) | L-LAW-1, L-LAW-2, L-LAW-3 |
| German / EU legal carve-outs (§ 69e UrhG, EU 2009/24/EC) | **Still open** | (none retrieved this session) |
| Hardcoded keys recovered from mobile apps | Candidates retrieved | L-HC-1, L-HC-3, L-HC-6 |
| AI-assisted vulnerability discovery / attacker effort | Candidates retrieved | L-VD-1, L-VD-2, L-VD-5 |
| Vendor-published positions on community RE | **Still open** | (no peer-reviewed vendor-position papers retrieved; will require grey-literature / corporate-statement sourcing) |
| Counter-positions: interoperability increases risk | Candidates retrieved | L-COUNTER-1, L-COUNTER-2, L-COUNTER-3 |

### Open questions and gaps
- All entries above are **[lit-retrieved]**, not **[lit-read]**. The first concrete paper claim that depends on any of these citations must wait until the entry is upgraded to `[lit-read]` after the researcher has read the full text.
- Two `[needs-research]` items remain unresolved:
  1. German / EU primary legal sources (§ 69e UrhG, EU 2009/24/EC). A targeted German-language and EUR-Lex search is the next step.
  2. Vendor-published positions on community reverse engineering. These are typically grey literature (vendor blog posts, statements to regulators, ToS clauses) and will need a different sourcing strategy than the academic-database approach used here.
- AI-generated legal analysis in transcripts must be replaced with sourced legal commentary before any legal framing appears in the paper. **AI-generated legal analysis is not legal advice.**
- The Consensus result lists were filtered to top-10 in this session; deeper reading should consult the full top-20 result sets via the database directly.

[Sign-up / upgrade notice from the literature search tool]: *Upgrade to Consensus Pro to return 20 results per search instead of 10, and include more data like study design and key takeaways for every result.* — https://consensus.app/pricing/?utm_source=claude_desktop
