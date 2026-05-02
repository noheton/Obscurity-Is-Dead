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
- **[ai-confirmed]** — *(new tier, introduced 2026-05-02)* the Source Analyzer agent (`docs/prompts/source-analyzer-prompt.md`) has retrieved the full text, read the abstract / methods / results / limitations, and confirmed that the entry's summary matches the source within rounding. Annotation includes retrieval URL, retrieval date, agent identifier, and a quoted load-bearing passage. Inline citation in `paper/main.{md,tex}` is permitted from this tier onward, *except* for load-bearing or contested claims (e.g. first-of-its-kind, only quantitative anchor, legal interpretation), which remain gated on `[lit-read]`. Edge cases that fail the upgrade criteria are annotated `[edge-case: <reason>]` and stay at `[lit-retrieved]` for human review.
- **[lit-read]** — full text has been read by the human researcher and the entry's relation to a paper claim has been confirmed by a human. This is the only tier that can carry contested or first-of-its-kind claims. An entry can carry both `[ai-confirmed]` and `[lit-read]` once the human has confirmed the AI's read.
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

### S-SF-2 — `[REDACTED:repo-path:SF-IMPL-2]-master` (community implementation)
- Type: community open-source implementation (ESP32 → MQTT bridge).
- Path: `experiments/spider-farmer/original/doc/[REDACTED:repo-path:SF-IMPL-2]-master.zip`
- Status: **[repo-vendored]**.
- Relation to research: contains `BLEPairingManager.py` cited as ground truth in transcript T3. Cited as Implementation #2 in `implementations.md`.

### S-SF-3 — `[REDACTED:repo-path:SF-IMPL-3]-main` (community implementation)
- Type: community open-source implementation (Python + MQTT).
- Path: `experiments/spider-farmer/original/doc/[REDACTED:repo-path:SF-IMPL-3]-main.zip`
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
- Reference: `sf.mqtt.spider-farmer.com:8333`, username `[REDACTED:username:S-SF-5-username]`, password `[REDACTED:credential:S-SF-5-password]` (recovered via self-signed-cert MITM, documented in `experiments/spider-farmer/original/doc/log.md`).
- Status: **[repo-vendored]** (as an extracted/discovered constant).
- Relation to research: directly supports `REPORT.md` §7 (security implications). The credential-recovery method is documented in a community thread embedded in `original/doc/log.md`.
- **Redaction notice**: raw credentials replaced per `docs/redaction-policy.md` R-SF-1 and R-SF-2. Git history rewrite required before public release.

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
- Upstream parent: `https://github.com/[REDACTED:repo-path:EF-IMPL-1]` (per `original/custom_components/powerocean_dev/const.py` line 13).
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

- **L-RE-1** [LLM4Decompile: Decompiling Binary Code with Large Language Models](https://consensus.app/papers/details/4839da33bde65e739f34bf48615a2a4a/?utm_source=claude_desktop) (Tan et al., 2024, 42 citations). **[lit-retrieved]** **[ai-confirmed 2026-05-02 by Claude Opus 4.7; retrieved https://arxiv.org/abs/2403.05286 (also https://huggingface.co/papers/2403.05286); quote: "the resulting models significantly outperform GPT-4o and Ghidra on the HumanEval and ExeBench benchmarks by over 100% in terms of re-executability rate"]**. Open-source 1.3B–33B LLMs outperform GPT-4o and Ghidra on HumanEval/ExeBench by >100% in re-executability rate. Supports: LLM tooling materially reduces decompilation effort.
- **L-RE-2** [DeGPT: Optimizing Decompiler Output with LLM](https://consensus.app/papers/details/069dc2908430571dbe8a97f63296c5ce/?utm_source=claude_desktop) (Hu et al., 2024, NDSS, 55 citations). **[lit-retrieved]** **[ai-confirmed-attempt-failed 2026-05-02 by Claude Opus 4.7: NDSS PDF and three mirrors returned HTTP 403 to fetch tool; abstract claim "24.4% reduction in cognitive burden" surfaced via search snippet of https://www.ndss-symposium.org/ndss-paper/degpt-optimizing-decompiler-output-with-llm/ but full text not read by agent; re-attempt from NDSS-accessible network or human verifier]**. Reports 24.4% reduction in cognitive burden of understanding decompiler output. Empirically anchors the "effort gap" claim.
- **L-RE-3** [REx86: A Local LLM for Assisting in x86 Assembly Reverse Engineering](https://consensus.app/papers/details/b7dec8058194576cbaf5a9b75fbb87f2/?utm_source=claude_desktop) (Lea et al., 2025, ACSAC). **[lit-retrieved]** **[ai-confirmed 2026-05-02 by Claude Opus 4.7; retrieved https://arxiv.org/abs/2510.20975 (venue confirmation https://www.acsac.org/2025/program/final/s41.html and https://ieeexplore.ieee.org/document/11391932/); quote: "increased the correct-solve rate from 31% to 53% (p = 0.189), though the latter did not reach statistical significance"]**. User study (n=43) where correct-solve rate rises from 31% → 53% with LLM assistance (p=0.189, not statistically significant at α=0.05). Quantitative anchor *and* a cautionary note for the magnitude of the effect.
- **L-RE-4** [Pop Quiz! Can a Large Language Model Help With Reverse Engineering?](https://consensus.app/papers/details/56ddc6b691095aefb3c188802f67f896/?utm_source=claude_desktop) (Pearce et al., 2022, 31 citations). **[lit-retrieved]**. Codex answered 72,754/136,260 questions correctly; concludes LLMs are "not yet ready for zero-shot reverse engineering". **Partially contradicts** the strong-form effort-gap claim; cite to keep the framing honest.
- **L-RE-5** [Exploring the Efficacy of LLMs (GPT-4) in Binary Reverse Engineering](https://consensus.app/papers/details/b3233d7b8b2557ccb821959c9a53e4d6/?utm_source=claude_desktop) (Pordanesh et al., 2024). **[lit-retrieved]**. Effective at general code understanding, weaker on technical/security analysis — qualified support.
- **L-RE-6** [An empirical study on the effectiveness of LLMs for binary code understanding](https://consensus.app/papers/details/524e60785850562b8ca74abdaf7c7004/?utm_source=claude_desktop) (Shang et al., 2025, *Empirical Software Engineering*). **[lit-retrieved]**. Multi-architecture, multi-optimisation benchmark.
- **L-RE-7** [ReCopilot: Reverse Engineering Copilot in Binary Analysis](https://consensus.app/papers/details/276e95e6b815565d9a5261fa202a130b/?utm_source=claude_desktop) (Chen et al., 2025). **[lit-retrieved]**. 13% improvement over prior LLMs/tools on function-name recovery and variable-type inference.
- **L-RE-8** [Extending Source Code Pre-Trained LMs to Summarise Decompiled Binaries (BinT5)](https://consensus.app/papers/details/36c5a9ca343755ce829365b31a96b69b/?utm_source=claude_desktop) (Al-Kaswan et al., 2023, SANER, 42 citations). **[lit-retrieved]**.

---

### Claim cluster B — LLM-assisted vulnerability discovery and exploit generation (asymmetry-of-collapse hypothesis)
*Tests `paper/main.md` §6.3: the integration path compresses faster than the offensive path.*

- **L-VD-1** [Good News for Script Kiddies? Evaluating LLMs for Automated Exploit Generation](https://consensus.app/papers/details/68f5ea4b57e252c1b2828b99affb7da6/?utm_source=claude_desktop) (Jin et al., 2025, IEEE SPW). **[lit-retrieved]** **[edge-case 2026-05-02 by Claude Opus 4.7: load-bearing cornerstone for §6.3 asymmetric-collapse claim ("LLMs more cooperative than competent at AEG"); first-of-its-kind result on refactored security labs (arXiv:2505.01065); only partial cross-confirmation from L-VD-2; full text not retrieved (HTTP 403); awaiting human [lit-read]]**. **Directly supports the asymmetry hypothesis**: "no model successfully generates exploits for refactored labs" — LLMs are far more cooperative than competent at AEG. Strongest single citation for §6.3.
- **L-VD-2** [A Systematic Study on Generating Web Vulnerability PoCs Using LLMs](https://consensus.app/papers/details/ab41cf96d89b56b08d94d9fa5430db46/?utm_source=claude_desktop) (Zhao et al., 2025, arXiv:2510.10148). **[lit-retrieved]** **[ai-confirmed 2026-05-02 by Claude Opus 4.7; retrieved https://arxiv.org/abs/2510.10148; quote: "LLMs can automatically generate working PoCs in 8%–34% of cases using only public data … adaptive reasoning … improves success rates to 68%–72%; 23 newly generated PoCs have been accepted by NVD and Exploit DB"]**. 8–34% PoC success rate with public CVE info alone, rising to 68–72% with adaptive reasoning; 23 LLM-generated PoCs accepted by NVD/Exploit-DB. **Partially contradicts L-VD-1** — note the gap between refactored labs and disclosed CVEs.
- **L-VD-3** [Automated Vulnerability Validation and Verification: An LLM Approach](https://consensus.app/papers/details/15e2c0dbc2a55525acf3ee171ed5eb05/?utm_source=claude_desktop) (Lotfi et al., 2025, arXiv:2509.24037). **[lit-retrieved]** **[ai-confirmed 2026-05-02 by Claude Opus 4.7; retrieved https://arxiv.org/abs/2509.24037; quote: "evaluated 102 CVEs from 2020–2025 across multiple LLMs and reproduced 71 (approximately 70%) CVEs"]**. End-to-end CVE-to-containerised-exploit pipeline; relevant to the "post-disclosure window" argument.
- **L-VD-4** [A Survey on LLM Security and Privacy: The Good, the Bad, and the Ugly](https://consensus.app/papers/details/8fc0614195e850158590c5bd0ac4a4b4/?utm_source=claude_desktop) (Yao et al., 2023, 841 citations). **[lit-retrieved]**. Cornerstone survey for the dual-use framing.
- **L-VD-5** [Exploiting Programmatic Behavior of LLMs: Dual-Use Through Standard Security Attacks](https://consensus.app/papers/details/a596dd8dfa595bb2bc803d603a7cd104/?utm_source=claude_desktop) (Kang et al., 2023, IEEE SPW, 307 citations). **[lit-retrieved]** **[edge-case 2026-05-02 by Claude Opus 4.7: load-bearing for §6.3 cost-asymmetry / asymmetric-collapse claim; abstract (https://arxiv.org/abs/2302.05733) confirms qualitative dual-use and "cost likely lower than with human effort alone" framing, but the specific "$125–500×" figure is the first-of-its-kind quantitative anchor — criterion 3 requires [lit-read] human verification]**. Quantifies the cost asymmetry: LLMs produce malicious content $125–500× cheaper than human effort.
- **L-VD-6** [Harnessing LLMs for Software Vulnerability Detection: A Comprehensive Benchmarking Study](https://consensus.app/papers/details/12350d74c097598693fdfb4afa0ee740/?utm_source=claude_desktop) (Tamberg et al., 2024, IEEE Access). **[lit-retrieved]**. LLMs > traditional static analysis on recall/F1 but with more false positives.
- **L-VD-7** [LLMs in Software Security: A Survey of Vulnerability Detection Techniques](https://consensus.app/papers/details/5eb5b0fbb905556ab2a07612797aeab7/?utm_source=claude_desktop) (Sheng et al., 2025, *ACM Computing Surveys*). **[lit-retrieved]**.
- **L-VD-8** [LLM for Vulnerability Detection and Repair: Literature Review](https://consensus.app/papers/details/6d46f168f54a5557928be22b39728c7a/?utm_source=claude_desktop) (Zhou et al., 2024, *ACM TOSEM*, 57 citations). **[lit-retrieved]**.
- **L-VD-9** [Enhancing RE: Benchmarking LLMs for Vulnerability Analysis in Decompiled Binaries (DeBinVul)](https://consensus.app/papers/details/15fcaa0190795019be20b791aa10e5d0/?utm_source=claude_desktop) (Manuel et al., 2024). **[lit-retrieved]**. 19–24% performance increase after fine-tuning on decompiled binaries; relevant to the binary side of vulnerability discovery.

---

### Claim cluster C — Hardcoded secrets in mobile apps are systemic, not exceptional
*Supports the Spider Farmer §3.6 finding that recovered MQTT credentials are typical, not anomalous.*

- **L-HC-1** [Evaluating LLMs in detecting Secrets in Android Apps (SecretLoc)](https://consensus.app/papers/details/52233c9b10cd578992087c98a1ddf9d1/?utm_source=claude_desktop) (Alecci et al., 2025). **[lit-retrieved]** **[edge-case 2026-05-02 by Claude Opus 4.7: load-bearing-cornerstone for §3.6 Spider Farmer thesis; full-text retrieval blocked (HTTP 403 from arXiv:2510.18601 / alphaXiv / SemanticScholar / ResearchGate via this harness); abstract-level numbers (42.5%, 4,828 secrets) confirmed via search snippets matching the publisher landing page; awaiting human read]**. **Strongest single citation for the Spider Farmer thesis**: of 5,000 Google Play apps, **42.5%** contain hardcoded secrets; 4,828 secrets missed by regex/static/ML methods recovered by LLMs. Authors explicitly name the dual-use risk: "if analysts can uncover these secrets with LLMs, so can attackers."
- **L-HC-2** [Hardcoded credentials in Android apps: Service exposure and category-based analysis](https://consensus.app/papers/details/6e0e942c75ef51138c637c504e7a5647/?utm_source=claude_desktop) (Mykhaylova et al., 2024, CEUR-WS Vol-3826). **[lit-retrieved]** **[ai-confirmed-attempt-failed 2026-05-02 by Claude Opus 4.7: CEUR PDF (https://ceur-ws.org/Vol-3826/short8.pdf) and KUBG repo (https://elibrary.kubg.edu.ua/id/eprint/50158/) returned HTTP 403 to harness; entry's narrow factual claim "6,165 APKs via MobSF + Trufflehog" cross-confirmed verbatim via two independent search-result snippets of the CEUR landing page; recommend re-fetch from a CEUR-accessible network]**. 6,165 APKs analysed via MobSF + Trufflehog.
- **L-HC-3** [How far are app secrets from being stolen? a case study on android](https://consensus.app/papers/details/26baf21595d454fabe121a5ec9294355/?utm_source=claude_desktop) (Wei et al., 2025, *Empirical Software Engineering*, DOI 10.1007/s10664-024-10607-9). **[lit-retrieved]** **[ai-confirmed-attempt-failed 2026-05-02 by Claude Opus 4.7: Springer landing, arXiv:2501.07805 (abs + html), and themoonlight mirror all returned HTTP 403 to harness; entry numbers (14,665 apps; 575 potential secrets; 56.9% confirmed; 3,711 distinct exploitable) cross-confirmed verbatim across two independent search-result snippets; this is the principal cross-confirmation for L-HC-1 — a successful re-fetch closes the Spider Farmer cornerstone]**. 575 potential secrets from 14,665 popular apps; 3,711 distinct exploitable secrets harvested via automatic analysis.
- **L-HC-4** [Hardcoded Secrets Unveiled: Static Access Token Exploitation in Real-World Android Applications](https://consensus.app/papers/details/4c6dad2e8aff5aa1a76bda178ce8d206/?utm_source=claude_desktop) (Domonkos et al., 2025, IEEE CogInfoCom). **[lit-retrieved]** **[ai-confirmed 2026-05-02 by Claude Opus 4.7; retrieved https://ieeexplore.ieee.org/document/11200789/ (publisher abstract via search snippet; full PDF 403 to harness); quote: "illustrating that it is not possible to securely hide sensitive information within applications, and that API owners need to migrate to modern, dynamic authentication methods"]**. 20 weather apps; concludes "it is not possible to securely hide sensitive information within applications" — direct contradiction of the obscurity-as-defence model.
- **L-HC-5** [DroidKey: A Practical Framework and Analysis Tool for API Key Security in Android Applications](https://consensus.app/papers/details/b4c46b096e055773a4aff4109dfec9b8/?utm_source=claude_desktop) (Piyumantha et al., 2025). **[lit-retrieved]**. Banking-app evaluation: widespread hardcoded-key vulnerabilities.
- **L-HC-6** [KeyDroid: A Large-Scale Analysis of Secure Key Storage in Android Apps](https://consensus.app/papers/details/3c6370250a425d3d85d1096dbc922c86/?utm_source=claude_desktop) (Blessing et al., 2025). **[lit-retrieved]** **[edge-case 2026-05-02 by Claude Opus 4.7: load-bearing-cornerstone for the obscurity-default baseline (§§1.1, 3); full-text retrieval blocked (HTTP 403 from arXiv:2507.07927 / ResearchGate via this harness); abstract-level numbers (490,119 apps; 56.3%) confirmed via search snippets; awaiting human read]**. 490,119 apps surveyed: **56.3% of apps self-reporting sensitive-data processing do not use trusted hardware at all**. Foundational evidence that the obscurity-default is the industry baseline.
- **L-HC-7** [Automatically Detecting Checked-In Secrets in Android Apps: How Far Are We?](https://consensus.app/papers/details/d1f7507b9aaa5cb49cad5701263d4d81/?utm_source=claude_desktop) (Li et al., 2024; *Empirical Software Engineering* 2025, DOI 10.1007/s10664-025-10772-5). **[lit-retrieved]** **[ai-confirmed 2026-05-02 by Claude Opus 4.7; retrieved https://arxiv.org/abs/2412.10922 (also https://link.springer.com/article/10.1007/s10664-025-10772-5); quote: "evaluated three representative tools on 5,135 Android apps … revealed 2,142 checked-in secrets affecting 2,115 Android apps"]**. Compares Three-Layer Filter, LeakScope, PassFinder on 5,135 apps; 2,142 secrets across 2,115 apps.
- **L-HC-8** [A survey of android application and malware hardening](https://consensus.app/papers/details/57c265748d615638945c3da0709b0d77/?utm_source=claude_desktop) (Sihag et al., 2021, *Comp Sci Rev*, 64 citations). **[lit-retrieved]**. Survey of obfuscation/hardening techniques and their evasion — provides the "obscurity-as-defence" baseline.

---

### Claim cluster D — Security through obscurity in consumer IoT and BLE
*Supports `paper/main.md` §1.1 (effort gap as security model) and §3 (Spider Farmer BLE protocol).*

- **L-BLE-1** [Security and Privacy Threats for BLE in IoT and Wearable Devices: A Comprehensive Survey](https://consensus.app/papers/details/9c6fb9cba9ab5492a39dbdba3a1d1019/?utm_source=claude_desktop) (Barua et al., 2022, *IEEE OJ Communications Society*, 97 citations, DOI 10.1109/OJCOMS.2022.3149732). **[lit-retrieved]** **[ai-confirmed 2026-05-02 by Claude Opus 4.7; retrieved https://ieeexplore.ieee.org/document/9706334/ (also https://ui.adsabs.harvard.edu/abs/2022IOJCS...3..251B/abstract); quote: "we present a comprehensive taxonomy for the security and privacy issues of BLE"]**. Most-cited recent BLE-IoT vulnerability survey.
- **L-BLE-2** [A survey on Bluetooth Low Energy security and privacy](https://consensus.app/papers/details/715f8ff204885de698417d8efd21ecc3/?utm_source=claude_desktop) (Cäsar et al., 2022, *Computer Networks*, 55 citations, DOI 10.1016/j.comnet.2021.108712). **[lit-retrieved]** **[ai-confirmed 2026-05-02 by Claude Opus 4.7; retrieved https://www.sciencedirect.com/science/article/pii/S1389128621005697 (also https://dl.acm.org/doi/10.1016/j.comnet.2021.108712); quote: "a systematic overview of BLE security and privacy properties across different versions and features, including known weaknesses and attacks"]**. Versioned weakness catalogue.
- **L-BLE-3** [Key Negotiation Downgrade Attacks on Bluetooth and BLE](https://consensus.app/papers/details/acf4526ad3f85ba38d70d9d4f86fcaea/?utm_source=claude_desktop) (Antonioli et al., 2020, *ACM TOPS*, 45 citations). **[lit-retrieved]**. Standard-compliant entropy-downgrade attacks against 19 BLE devices.
- **L-BLE-4** [Uncovering Vulnerabilities of BLE IoT from Companion Mobile Apps with Ble-Guuide](https://consensus.app/papers/details/2ca22ef2aae75e239b528ea6a0f50e1a/?utm_source=claude_desktop) (Sivakumaran et al., 2023, *AsiaCCS*). **[lit-retrieved]** **[ai-confirmed 2026-05-02 by Claude Opus 4.7; retrieved https://dl.acm.org/doi/10.1145/3579856.3595806 (publisher abstract; PDF mirror at jorgeblascoalis.com 403 to harness, but ACM DL index cross-confirms); quote: "a large-scale analysis of 17,243 free, BLE-enabled Android APKs ... more than 70% of these APKs contain at least one security vulnerability"]**. **>70% of 17,243 BLE-enabled Android APKs contain at least one security vulnerability.** Strong base-rate citation.
- **L-BLE-5** [Living in the Past: Analyzing BLE IoT Devices Based on Mobile Companion Apps in Old Versions](https://consensus.app/papers/details/12309b92f63459f490b8991573566da1/?utm_source=claude_desktop) (Du et al., 2023). **[lit-retrieved]** **[edge-case 2026-05-02 by Claude Opus 4.7: load-bearing for §3 Spider Farmer analog; abstract (https://ieeexplore.ieee.org/document/10567010/) supports "earlier versions of the companion apps can still be exploited to attack IoT devices" but does not verbatim assert vendor firmware-non-patching as the entry summary infers; full text 403 across IEEE / CSDL / ResearchGate; awaiting human read]**. Documents the exact pattern observed in Spider Farmer: vendors update companion APKs to raise the RE bar **without** patching the underlying device firmware. Direct support for the "obscurity, not security" critique.
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

### Claim cluster I — Sloppification of science by generative AI
*Supports `paper/main.md` §5.6 (meta-process security implications) and §7.6 ("Sloppification: the AI methodological discount"). Empirical base rates for the fabricated-citation risk that the verification-status legend exists to manage.*

- **L-SLOP-1** [Fabrication and errors in the bibliographic citations generated by ChatGPT](https://consensus.app/papers/details/c5feb2bfe92c5dd5a79feb667ebfbd4a/?utm_source=claude_desktop) (Walters & Wilder, 2023, *Scientific Reports*, 219 citations). **[lit-retrieved]**. **The headline citation for the sloppification thesis**: 55% of ChatGPT-3.5 and 18% of GPT-4 generated citations are fabricated; 43% / 24% of *real* citations carry substantive errors. Across 84 short literature reviews on 42 multidisciplinary topics, 636 citations analysed.
- **L-SLOP-2** [Hallucination Rates and Reference Accuracy of ChatGPT and Bard for Systematic Reviews](https://consensus.app/papers/details/5cd8dd78481e561688e4712599e8078a/?utm_source=claude_desktop) (Chelli et al., 2024, *Journal of Medical Internet Research*, 162 citations). **[lit-retrieved]**. Hallucination rates **39.6% (GPT-3.5), 28.6% (GPT-4), 91.4% (Bard)**; precision rates 9.4–13.4% for GPT, 0% for Bard. Recall 11.9–13.7%. Across 11 systematic reviews and 471 references.
- **L-SLOP-3** [ChatGPT Hallucinates Non-existent Citations: Evidence from Economics](https://consensus.app/papers/details/5c98b404a34a55e3a797168696ab8ca2/?utm_source=claude_desktop) (Buchanan & Hill, 2023, *The American Economist*, 23 citations). **[lit-retrieved]**. >30% of GPT-3.5 citations don't exist; only slight reduction for GPT-4; reliability decreases as prompts become more specific.
- **L-SLOP-4** [ChatGPT and Bard exhibit spontaneous citation fabrication during psychiatry literature search](https://consensus.app/papers/details/83f7b9052b9d5d4c8c9340effac53fff/?utm_source=claude_desktop) (McGowan et al., 2023, *Psychiatry Research*, 94 citations). **[lit-retrieved]**. Of 35 ChatGPT-generated psychiatry citations, only 2 were real; 21 were pastiches of multiple existent manuscripts. Striking, often-cited illustration of the problem.
- **L-SLOP-5** [Risks of abuse of large language models, like ChatGPT, in scientific publishing](https://consensus.app/papers/details/500245d42d915ff8a1d156d4b6b5414b/?utm_source=claude_desktop) (Kendall & Teixeira da Silva, 2023, *Learned Publishing*, 61 citations). **[lit-retrieved]**. System-level argument: LLMs amplify the predatory-publishing and paper-mill industries.
- **L-SLOP-6** [AI intensifies fight against 'paper mills' that churn out fake research](https://consensus.app/papers/details/76aed8feb0ba5b4fac89964cf0b6620a/?utm_source=claude_desktop) (Liverpool, 2023, *Nature*, 54 citations). **[lit-retrieved]**. News-feature treatment in *Nature* — useful for the policy-implications framing.
- **L-SLOP-7** [Reformation of science publishing: the Stockholm Declaration](https://consensus.app/papers/details/d92b7e8ff97357588c420a4f21453cc0/?utm_source=claude_desktop) (Sabel & Larhammar, 2025, *Royal Society Open Science*, DOI 10.1098/rsos.251805). **[lit-retrieved]** **[ai-confirmed 2026-05-02 by Claude Opus 4.7; retrieved https://royalsocietypublishing.org/rsos/article/12/11/251805/234088/Reformation-of-science-publishing-the-Stockholm (also https://uu.diva-portal.org/smash/get/diva2:2013873/FULLTEXT01.pdf); quote: "Academia should resume control of publishing using non-profit publishing models... Adjust incentive systems to merit quality, not quantity... Implement mechanisms to prevent and detect fake publications and fraud which are independent of publishers."]**. Royal Swedish Academy of Sciences action plan: non-profit publishing, quality-not-quantity incentives, independent fraud detection, regulatory frameworks.
- **L-SLOP-8** [Explosion of formulaic research articles based on the NHANES US national health database](https://consensus.app/papers/details/78c7198f69cb51869f2c1bd99de71768/?utm_source=claude_desktop) (Suchak et al., 2025, *PLOS Biology*, 26 citations). **[lit-retrieved]**. **Direct empirical observation of AI-amplified paper-mill output**: NHANES-based formulaic single-factor papers grew from ~4 / year (2014–2021) to **190 in the first ten months of 2024**.
- **L-SLOP-9** [Evaluation of LLM Performance and Reliability for Citations and References in Scholarly Writing: Cross-Disciplinary Study](https://consensus.app/papers/details/107ed2efe9c05ef09c55aafca4d54a1e/?utm_source=claude_desktop) (Mugaanyi et al., 2023, *Journal of Medical Internet Research*, 29 citations). **[lit-retrieved]**. Disciplinary variance in citation accuracy (natural sciences vs.\ humanities); DOI hallucination rates up to 89.4%.
- **L-SLOP-10** [Artificial intelligence-assisted academic writing: recommendations for ethical use](https://consensus.app/papers/details/745e81333e085ad1b5a83d4835ffeb42/?utm_source=claude_desktop) (Cheng, Calhoun & Reedy, 2025, *Advances in Simulation*, 26 citations, DOI 10.1186/s41077-025-00350-6). **[lit-retrieved]** **[ai-confirmed 2026-05-02 by Claude Opus 4.7; retrieved https://link.springer.com/article/10.1186/s41077-025-00350-6 (open-access; also PMC12007126); quote: "we discuss three categories of specific ways generative AI tools can be used in an ethically sound manner and offer four key principles... to produce high-quality research outputs with the highest of academic integrity."]**. Concrete ethical-use guidelines — useful for §9 (AI Disclosure) framing.
- **L-SLOP-11** [ChatGPT and a new academic reality](https://consensus.app/papers/details/10c043e4c6ec5192a228843d35fc936d/?utm_source=claude_desktop) (Lund et al., 2023, *JASIST*, 639 citations). **[lit-retrieved]**. Cornerstone library-and-information-science treatment of AI in scholarly publishing.
- **L-SLOP-12** [AI for scientific integrity: detecting ethical breaches, errors, and misconduct in manuscripts](https://consensus.app/papers/details/0055733ed1c85c9a9e5ea2aa8ab21554/?utm_source=claude_desktop) (Pellegrina & Helmy, 2025, *Frontiers in Artificial Intelligence* 8:1644098, DOI 10.3389/frai.2025.1644098). **[lit-retrieved]** **[ai-confirmed 2026-05-02 by Claude Opus 4.7; retrieved https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1644098/full (also PMC12436494); quote: "these developments are not yet sufficiently accurate or reliable yet for use in academic assessment, they mark an early but promising steps toward scalable, AI-assisted quality control."]**. Reviews AI detectors and AI-assisted error/citation/image verification — the technical-mitigation landscape.

---

### Claim cluster J — Model collapse and the dilution of the scientific commons
*Supports `paper/main.md` §7.7 ("Model collapse and the dilution of the scientific commons"). The literature for the distal, corpus-level externality of un-verified AI-assisted output.*

- **L-MC-1** [AI models collapse when trained on recursively generated data](https://consensus.app/papers/details/66d2e766ffe95e54be8b0a5d38356fcd/?utm_source=claude_desktop) (Shumailov et al., 2024, *Nature*, **459 citations**). **[lit-retrieved]**. **The canonical model-collapse paper.** Indiscriminate use of model-generated content in training causes irreversible defects; the tails of the original distribution disappear. Demonstrated for LLMs, VAEs, and GMMs.
- **L-MC-2** [ForTIFAI: Fending Off Recursive Training Induced Failure for AI Model Collapse](https://consensus.app/papers/details/39d4af8eaaee583d8cb1ef27b584afd3/?utm_source=claude_desktop) (Shabgahi et al., 2025). **[lit-retrieved]**. Truncated-Cross-Entropy loss filters high-confidence (likely machine-generated) tokens during training; tolerates >2.3× more synthetic data before collapse. Concrete mitigation at the model-training layer.
- **L-MC-3** [How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse](https://consensus.app/papers/details/ea92f57f77d05c9fb8a9f9eb4955e097/?utm_source=claude_desktop) (Seddik et al., 2024, 56 citations). **[lit-retrieved]**. Proves model collapse is unavoidable for purely synthetic training and bounded for mixed real/synthetic below a threshold. The theoretical anchor for "preserve human-verified data".
- **L-MC-4** [Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data](https://consensus.app/papers/details/33818bbcb8f2542fa91e04028c297417/?utm_source=claude_desktop) (Gerstgrasser et al., 2024, 102 citations). **[lit-retrieved]**. **Strongest constructive result**: *accumulating* synthetic data alongside real data (rather than replacing) yields a finite test-error upper bound and avoids collapse. Confirmed for LLMs, diffusion models, and VAEs.
- **L-MC-5** [Rate of Model Collapse in Recursive Training](https://consensus.app/papers/details/1e4064583da35384a82de831acebd1f5/?utm_source=claude_desktop) (Suresh et al., 2024, 11 citations). **[lit-retrieved]**. Theoretical characterisation of collapse rate for fundamental distributions; surprisingly slow in some regimes.
- **L-MC-6** [A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective](https://consensus.app/papers/details/96b0ae36c3df5a2aa117a8e58aff7aad/?utm_source=claude_desktop) (Shi et al., 2025). **[lit-retrieved]**. Reframes collapse as a generalisation-to-memorisation transition driven by declining synthetic-data entropy; entropy-based data selection mitigates.
- **L-MC-7** [The Curse of Recursion: Training on Generated Data Makes Models Forget](https://consensus.app/papers/details/d75dbf63c6b8566882269d5f1674c222/?utm_source=claude_desktop) (Shumailov et al., 2023, ArXiv, 370 citations). **[lit-retrieved]**. The original arXiv preprint that became L-MC-1; useful for the ArXiv-citing community.
- **L-MC-8** [A Note on Shumailov et al. (2024)](https://consensus.app/papers/details/3e2a263b9c9158dda4224ccdf61aea18/?utm_source=claude_desktop) (Borji, 2024, 103 citations). **[lit-retrieved]**. Theoretical follow-up arguing collapse is a general statistical phenomenon and may be unavoidable absent intervention. Useful as a *qualifier*: tempers the optimistic L-MC-4 result.
- **L-MC-9** [Multi-modal Synthetic Data Training and Model Collapse](https://consensus.app/papers/details/c8a2696574a958e1ae6c542a63827d9f/?utm_source=claude_desktop) (Hu et al., 2025). **[lit-retrieved]**. Extends the analysis to VLMs and diffusion models in recursive multi-agent loops; mitigations include increased decoding budgets, model diversity, and frozen-relabelling.

---

### Claim cluster K — Consumer-IoT base-rate of vulnerability vs.\ industrial / more-expensive hardware
*Supports `paper/main.md` §6.4 ("Limits of the comparison"). Anchors the qualifier that the case selection over-samples consumer-grade hardware and that industrial / higher-end hardware may have a different — though not automatically better — security posture.*

#### Consumer-IoT base rate (supports: consumer hardware is broadly vulnerable)
- **L-CONS-1** [A Large-Scale Empirical Study on the Vulnerability of Deployed IoT Devices](https://consensus.app/papers/details/96ce1ba513cc5e1ea0d401872ec4cebd/?utm_source=claude_desktop) (Zhao et al., 2022, *IEEE TDSC*, 60 citations). **[lit-retrieved]**. **Headline statistic for the consumer-IoT base rate**: 1,362,906 IoT devices analysed; 385,060 (**28.25%**) have at least one N-days vulnerability; 12,740 (**88%**) of analysed MQTT servers have no password protection. This is direct quantitative anchor for "a lot of customer-market equipment is probably vulnerable".
- **L-CONS-2** [All Things Considered: An Analysis of IoT Devices on Home Networks](https://consensus.app/papers/details/7ad606e797c35fd5980a0dd177ae3cf9/?utm_source=claude_desktop) (Kumar et al., 2019, 180 citations). **[lit-retrieved]**. 83M devices across 16M households. Documents weak default credentials, regional variance, and open services. Most-cited large-scale home-IoT measurement.
- **L-CONS-3** [Vulnerability Studies and Security Postures of IoT Devices: A Smart Home Case Study](https://consensus.app/papers/details/59cd9de8fe195482a4d09872115f9c48/?utm_source=claude_desktop) (Davis et al., 2020, *IEEE IoT J*, 91 citations). **[lit-retrieved]**. **Directly relevant qualifier**: comparison between well-known and lesser-known vendors finds the lesser-known vendors are systematically worse-regulated and less-scrutinised. Spider Farmer and EcoFlow PowerOcean both fit the "lesser-known" pattern.
- **L-CONS-4** [Consumer IoT: Security Vulnerability Case Studies and Solutions](https://consensus.app/papers/details/c6db9afaffb752a08c414f883ca8a765/?utm_source=claude_desktop) (Alladi et al., 2020, *IEEE Consumer Electronics Magazine*, 264 citations). **[lit-retrieved]**. Survey of common attacks on consumer-IoT devices.
- **L-CONS-5** [Identifying vulnerabilities of consumer IoT devices: A scalable approach](https://consensus.app/papers/details/bd19e356a9615949adca4d8ad07ea80e/?utm_source=claude_desktop) (Williams et al., 2017, *IEEE ISI*, 97 citations). **[lit-retrieved]**. Shodan + Nessus large-scale assessment; significant fraction of internet-exposed consumer IoT vulnerable.
- **L-CONS-6** [Ranking Security of IoT-Based Smart Home Consumer Devices](https://consensus.app/papers/details/7e8fd857ebc851d59937fb0aa2d13324/?utm_source=claude_desktop) (AlLifah et al., 2022, *IEEE Access*, 52 citations). **[lit-retrieved]**. AHP-based ranking model of consumer-device categories; useful framework for the §3/§4 case-study positioning.

#### Industrial / IIoT / ICS posture (qualifier: industrial *may* be different but is not automatically immune)
- **L-IND-1** [Challenges and Opportunities in Securing the Industrial Internet of Things](https://consensus.app/papers/details/53953289a84e5c7fb6a65b89f321b5c5/?utm_source=claude_desktop) (Serror et al., 2020, *IEEE TII*, 247 citations). **[lit-retrieved]**. **Most directly relevant framing for the user's hypothesis**: argues that IIoT shares many similarities with consumer IoT but has *different* security goals (safety-driven, longer component lifetimes, larger network scale). Supports the *partial* form of the user's hypothesis: industrial requirements differ, sometimes for the better, but introduce their own challenges.
- **L-IND-2** [The Global State of Security in Industrial Control Systems: An Empirical Analysis of Vulnerabilities Around the World](https://consensus.app/papers/details/73a4bbc9a2d75cb389c2fa949558a928/?utm_source=claude_desktop) (Antón et al., 2021, *IEEE IoT J*). **[lit-retrieved]**. **Crucial counterweight to the user's hypothesis**: finds **>13,000 OT/ICS devices directly exposed on the public internet, almost all containing at least one vulnerability**. Industrial hardware is not automatically more secure once it is reachable. Demonstrates that the "industrial-grade therefore safer" intuition is empirically too strong.
- **L-IND-3** [Cybersecurity in industrial control systems: Issues, technologies, and challenges](https://consensus.app/papers/details/ad9e4141e1bc5013afd52e486896e910/?utm_source=claude_desktop) (Asghar et al., 2019, *Computer Networks*, 110 citations). **[lit-retrieved]**. Documents that ICS were designed for isolated environments and that modern IT/business integration introduces unanticipated cybersecurity challenges. Useful structural critique.
- **L-IND-4** [Cyber Threats to Industrial IoT: A Survey on Attacks and Countermeasures](https://consensus.app/papers/details/9fe92ca76354502d9c19578729d58a6c/?utm_source=claude_desktop) (Tsiknas et al., 2021, *IoT*, 132 citations). **[lit-retrieved]**. Survey of IIoT-specific attacks.
- **L-IND-5** [Industrial IoT, Cyber Threats, and Standards Landscape: Evaluation and Roadmap](https://consensus.app/papers/details/7ac2a8f0eab65334892ddebc58849df5/?utm_source=claude_desktop) (Dhirani et al., 2021, *Sensors*, 99 citations). **[lit-retrieved]**. Standards-landscape view; relevant for the "regulation and certification raise the floor" hypothesis.
- **L-IND-6** [Securing Industrial Control Systems: Components, Cyber Threats, and ML-Driven Defense](https://consensus.app/papers/details/897b343801955e27b7158083e6b6557d/?utm_source=claude_desktop) (Nankya et al., 2023, *Sensors*, 56 citations). **[lit-retrieved]**. ICS components and threat overview.

---

### Claim cluster L — Privacy as a user right reachable via local interoperability
*Supports `paper/main.md` §1.3 motivation ("Privacy and data sovereignty") and §7.12 ("Privacy as a user right: keeping the device, dropping the cloud"). The literature for the orthogonal claim that local-first, AI-assisted integrations let users continue to use the device as intended while opting out of vendor telemetry — and that the empirical baseline for cloud-bound consumer IoT privacy is severe.*

#### Empirical baseline — what cloud-bound IoT actually exports
- **L-PRIV-1** [Information Exposure From Consumer IoT Devices: A Multidimensional, Network-Informed Measurement Approach](https://consensus.app/papers/details/a282b9ca59d65ccf85248ddb70317a13/?utm_source=claude_desktop) (Ren et al., 2019, *Proc. IMC*, **273 citations**). **[lit-retrieved]**. **Cornerstone empirical anchor.** 81 devices in US/UK labs, 34,586 controlled experiments. Characterises destinations, encryption, inferable interactions, and unexpected exposures (including a recording device covertly transmitting video). Documents regional differences plausibly attributable to GDPR.
- **L-PRIV-2** [A Smart Home is No Castle: Privacy Vulnerabilities of Encrypted IoT Traffic](https://consensus.app/papers/details/f66bf1b6fb835bfaa63fd250a40c3ad3/?utm_source=claude_desktop) (Apthorpe et al., 2017, ArXiv, **336 citations**). **[lit-retrieved]**. Four representative IoT devices (Sense sleep monitor, Nest Cam Indoor, WeMo switch, Amazon Echo): even *encrypted* traffic rates reveal sensitive user interactions to a passive observer such as an ISP. Direct counter to the "encryption is sufficient" intuition.
- **L-PRIV-3** [Peek-a-boo: I See Your Smart Home Activities, Even Encrypted!](https://consensus.app/papers/details/dc3786721a9858b2aede91a9520990b5/?utm_source=claude_desktop) (Acar et al., 2018, *Proc. ACM WiSec*, **291 citations**). **[lit-retrieved]**. Multi-stage ML pipeline that achieves **>90% accuracy** identifying device states and ongoing user activities from passively-sniffed encrypted traffic across WiFi, ZigBee, and BLE. Strong evidence that local-network telemetry is leaky even before cloud egress.
- **L-PRIV-4** [Discovering Smart Home Internet of Things Privacy Norms Using Contextual Integrity](https://consensus.app/papers/details/5da7cacce757596bab7407ba6581aa7d/?utm_source=claude_desktop) (Apthorpe et al., 2018, *Proc. ACM IMWUT*, 170 citations). **[lit-retrieved]**. 1,731 US adults, 3,840 information flows tested. Empirically maps which smart-home information flows users find acceptable to first vs. third parties; supports the framing that vendor-cloud egress to third parties is *contrary to* user-held privacy norms, not just contrary to a regulatory ideal.
- **L-PRIV-5** [Are You Spying on Me? Large-Scale Analysis on IoT Data Exposure through Companion Apps](https://consensus.app/papers/details/0961dc1e65eb5930b835095bad79c947/?utm_source=claude_desktop) (Nan et al., 2023, 26 citations). **[lit-retrieved]**. **Strongest large-N empirical anchor.** Static analysis of **6,208 IoT companion apps**; identifies **1,973 apps** that expose user data without proper disclosure, covering devices from at least **1,559 unique vendors**. Sensitive categories include health status and home address, with cross-border third-party sharing.

#### Companion-app surface — the second telemetry path
- **L-PRIV-6** [A Multi-Dimensional Analysis of IoT Companion Apps: A Look at Privacy, Security and Accessibility](https://consensus.app/papers/details/690ac4c0f1215ca7b73feffed93ffadd/?utm_source=claude_desktop) (Tazi et al., 2025, *IEEE Transactions on Services Computing*). **[lit-retrieved]**. 455 IoT companion apps. Documents that apps systematically over-request permissions unrelated to their main goal, and that quality on one axis does not predict quality on another.
- **L-PRIV-7** [Let the Cat out of the Bag: Popular Android IoT Apps under Security Scrutiny](https://consensus.app/papers/details/af4e523ef68c5a50a846169b4bb528ae/?utm_source=claude_desktop) (Chatzoglou et al., 2022, *Sensors*, 17 citations). **[lit-retrieved]**. >40 chart-topping Android IoT apps from six categories; majority remain susceptible to a range of security-and-privacy issues including trackers, manifest data leaks, and shared-software vulnerabilities.
- **L-PRIV-8** [On the Data Privacy, Security, and Risk Postures of IoT Mobile Companion Apps](https://consensus.app/papers/details/06e53df1784e57129cda381b8df5ce33/?utm_source=claude_desktop) (Neupane et al., 2022, 13 citations). **[lit-retrieved]**. 455-app latitudinal study; documents over-requested permissions and that two of the analysed apps transmitted credentials in unencrypted form. Companion of L-PRIV-6.

#### Local-first as a privacy mitigation that preserves intended use
- **L-PRIV-9** [I just wanted to track my steps! Blocking unwanted traffic of Fitbit devices](https://consensus.app/papers/details/73a0a59bde1159f4a5159b1d3ee8694d/?utm_source=claude_desktop) (Kazlouski et al., 2022, *Proc. IoT*). **[lit-retrieved]**. **Most directly relevant existence proof for the "use as intended without telemetry" claim.** Disabling traffic to domains in well-maintained blocklists does *not* prevent Fitbit trackers from correctly reporting steps, workouts, sleep duration/quality; activity data also synchronise correctly across six partner apps. Each studied app contacted between 1 and 20 non-required third parties.
- **L-PRIV-10** [A mapping of IoT user-centric privacy preserving approaches to the GDPR](https://consensus.app/papers/details/669280af55fa576fa5d2d9ec6880a420/?utm_source=claude_desktop) (Kounoudes et al., 2020, *Internet of Things*, 53 citations). **[lit-retrieved]**. Systematisation of state-of-the-art IoT privacy approaches against GDPR requirements; useful framing for tying local-first integration to data-minimisation (Art. 5(1)(c)) and data-protection-by-design (Art. 25).

#### Counter-evidence — regulation alone is not the answer
- **L-PRIV-11** [Before and after GDPR: tracking in mobile apps](https://consensus.app/papers/details/8d56f687fd6e56ed8c03e58d455ef60b/?utm_source=claude_desktop) (Kollnig et al., 2021, ArXiv, 35 citations). **[lit-retrieved]**. **Crucial qualifier.** Nearly two million Android apps before/after GDPR; *limited change* in third-party tracking, with concentration among large gatekeepers persisting. Supports the framing that user-side technical alternatives (local integrations, network-level blocking) are necessary alongside regulation, not a substitute for it.
- **L-PRIV-12** [GDPR bypass by design? Transient processing of data under the GDPR](https://consensus.app/papers/details/1e0bf0e981645f59af78f0ebd38bb394/?utm_source=claude_desktop) (George et al., 2019, *International Data Privacy Law*, 16 citations). **[lit-retrieved]**. Argues that "transient" processing patterns can place activities outside GDPR scope altogether. A nuance for the data-minimisation framing: minimising processed data is both a Art. 5(1)(c) compliance route and (potentially) a route to escape regulatory oversight; the user-side benefit is the same in both cases.

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
| Sloppification of science by generative AI | Candidates retrieved | L-SLOP-1, L-SLOP-2, L-SLOP-4, L-SLOP-7, L-SLOP-8 |
| Model collapse and dilution of the scientific commons | Candidates retrieved | L-MC-1, L-MC-3, L-MC-4 |
| Consumer-IoT base rate of vulnerability vs.\ industrial / IIoT / ICS posture | Candidates retrieved | L-CONS-1, L-CONS-2, L-CONS-3 (consumer); L-IND-1, L-IND-2 (industrial qualifier) |
| Privacy as a user right reachable via local interoperability ("use device as intended without telemetry") | Candidates retrieved | L-PRIV-1, L-PRIV-2, L-PRIV-5 (baseline); L-PRIV-9 (existence proof of intended-use without third parties); L-PRIV-11 (regulation-alone qualifier) |

### Open questions and gaps
- All entries above are **[lit-retrieved]**, not **[lit-read]**. The first concrete paper claim that depends on any of these citations must wait until the entry is upgraded to `[lit-read]` after the researcher has read the full text.
- Two `[needs-research]` items remain unresolved:
  1. German / EU primary legal sources (§ 69e UrhG, EU 2009/24/EC). A targeted German-language and EUR-Lex search is the next step.
  2. Vendor-published positions on community reverse engineering. These are typically grey literature (vendor blog posts, statements to regulators, ToS clauses) and will need a different sourcing strategy than the academic-database approach used here.
- AI-generated legal analysis in transcripts must be replaced with sourced legal commentary before any legal framing appears in the paper. **AI-generated legal analysis is not legal advice.**
- The Consensus result lists were filtered to top-10 in this session; deeper reading should consult the full top-20 result sets via the database directly.

[Sign-up / upgrade notice from the literature search tool]: *Upgrade to Consensus Pro to return 20 results per search instead of 10, and include more data like study design and key takeaways for every result.* — https://consensus.app/pricing/?utm_source=claude_desktop

### Claim cluster M — Malicious LLM agents and adversarial agentic AI
*Supports `paper/main.md` §7.13 ("The malicious IoT-integrator agent"). The literature for the structural argument that the IoT-Integrator prompt is dual-use: the same self-augmenting four-phase protocol that produces a configuration-only Phase 3 outcome under researcher governance can be re-instantiated by an adversary. The cluster covers (i) autonomous offensive capability of LLM agents, (ii) prompt-injection / protocol-level attacks against agent ecosystems, and (iii) backdoor and memory-poisoning attacks that propagate adversarial techniques through the same self-augmenting loop the methodology uses.*

#### Autonomous offensive capability of LLM agents
- **L-AGT-1** [LLM Agents can Autonomously Exploit One-day Vulnerabilities](https://consensus.app/papers/details/b82960ecad7f57f4b111cd86ba3a122f/?utm_source=claude_desktop) (Fang et al., 2024, ArXiv, **103 citations**). **[lit-retrieved]**. Strongest single anchor for §7.13 "per-device exploit pipeline" bullet. Dataset of 15 one-day CVEs; **GPT-4 exploits 87%** of them given the CVE description versus **0% for GPT-3.5, open-source LLMs, ZAP, and Metasploit**; without the description, GPT-4 still exploits 7%. Direct empirical evidence that the differential between researcher-governed and adversarial use of frontier-LLM agents is governance, not capability.
- **L-AGT-2** [LLM Agents can Autonomously Hack Websites](https://consensus.app/papers/details/f12abb3a6553552c815c42d6396619ce/?utm_source=claude_desktop) (Fang et al., 2024, ArXiv, **80 citations**). **[lit-retrieved]**. Companion of L-AGT-1. GPT-4 autonomously performs blind database schema extraction and SQL injection without prior knowledge of the vulnerability; capability is unique to frontier tool-using models. Supports §7.13 "credential-and-token harvesting at integration time" bullet.

#### Prompt injection and protocol exploits against agent ecosystems
- **L-AGT-3** [From Prompt Injections to Protocol Exploits: Threats in LLM-Powered AI Agents Workflows](https://consensus.app/papers/details/4ab586bc9f9358f99651d024e232fe26/?utm_source=claude_desktop) (Ferrag et al., 2025, ArXiv, 6 citations). **[lit-retrieved]**. End-to-end threat model for LLM-agent ecosystems; **>30 attack techniques** across input manipulation, model compromise, system/privacy attacks, and protocol-level vulnerabilities. Concrete examples include Prompt-to-SQL injection and the "Toxic Agent Flow" exploit in GitHub MCP servers. Useful as the systematisation reference for §7.13's enumeration.
- **L-AGT-4** [The Dark Side of LLMs: Agent-based Attacks for Complete Computer Takeover](https://consensus.app/papers/details/dee4d701077a58a0a959761544d3acfc/?utm_source=claude_desktop) (Lupinacci et al., 2025, 5 citations). **[lit-retrieved]**. Evaluation of 18 state-of-the-art LLMs: **94.4% succumb to Direct Prompt Injection**, **83.3% to RAG Backdoor Attack**, **100% to Inter-Agent Trust Exploitation**. Direct anchor for §7.13 "trust laundering through a benign-looking artifact" bullet — adversarial corruption of an LLM-driven integrator pipeline crosses agent-to-agent trust boundaries that look benign at each hop.
- **L-AGT-5** [Sudo Rm -rf Agentic_security](https://consensus.app/papers/details/3a07afde65aa54839f45cd581f4a7209/?utm_source=claude_desktop) (Lee et al., 2025, ArXiv, 6 citations). **[lit-retrieved]**. The SUDO Detox2Tox framework iteratively bypasses refusal-trained safeguards in commercial computer-use agents; achieves **24.41% baseline → 41.33% with iterative refinement** attack-success rate against Claude for Computer Use. Empirical existence proof that vendor-side safety training is not a sufficient mitigation for the malicious-integrator threat.

#### Backdoor, memory-poisoning, and self-augmenting attacks
- **L-AGT-6** [AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases](https://consensus.app/papers/details/2a26815b60635f58ae3d20ba300016fe/?utm_source=claude_desktop) (Chen et al., 2024, ArXiv, **156 citations**). **[lit-retrieved]**. Strongest anchor for §7.13 "self-augmentation of attack capability" and "erosion of the governance baseline" bullets. Backdoor triggers are optimised in embedding space; **>80% attack success at <0.1% poison rate** across three real-world agent classes. Requires no fine-tuning. Maps directly onto the failure mode in which malicious-integrator output enters public corpora and contaminates the technique inventory of subsequent IoT-Integrator runs.
- **L-AGT-7** [Watch Out for Your Agents! Investigating Backdoor Threats to LLM-Based Agents](https://consensus.app/papers/details/55b643d0a6f15bc0a37dc3372a1c6b63/?utm_source=claude_desktop) (Yang et al., 2024, ArXiv, **113 citations**). **[lit-retrieved]**. Backdoor attacks on LLM-based agents can manipulate either the final output or only an intermediate reasoning step while keeping final output correct. Direct counter to the assumption that visible-output review (the researcher checkpoint) is sufficient — adversarial steps can be embedded in the reasoning trace itself.
- **L-AGT-8** [Agent Security Bench (ASB)](https://consensus.app/papers/details/855f0332a1cf58df9cca7ce9354d7b88/?utm_source=claude_desktop) (Zhang et al., 2024, ArXiv, **84 citations**). **[lit-retrieved]**. Benchmark of 27 attack/defence methods × 13 LLM backbones × 10 application scenarios. **84.30% average attack success**; current defences are limited. Useful as the systematisation reference for the §7.13 mitigation discussion.
- **L-AGT-9** [Breaking Agents: Compromising Autonomous LLM Agents Through Malfunction Amplification](https://consensus.app/papers/details/5fd5d38c8adf5ee18cb7ff552569c542/?utm_source=claude_desktop) (Zhang et al., 2024, ArXiv, **50 citations**). **[lit-retrieved]**. Failure-rate >80% from attacks that mislead an agent into repetitive or irrelevant actions. Anchors a different §7.13 failure mode: even a non-malicious agent can be steered into an attack-equivalent pattern by adversarial environmental input.
- **L-AGT-10** [BadAgent: Inserting and Activating Backdoor Attacks in LLM Agents](https://consensus.app/papers/details/de682b591bc455549e854d701047753c/?utm_source=claude_desktop) (Wang et al., 2024, **68 citations**). **[lit-retrieved]**. Backdoor robust even after fine-tuning on trustworthy data. Reinforces the §7.13 governance argument: capability-side defences (safety training, fine-tuning on trusted data) do not suffice, structural-side defences (checkpoints, redaction, dual-use mirror) are required.

### Claim cluster N — Mass probing of public APK repositories and Android-marketplace ecosystem
*Supports `paper/main.md` §7.14 ("Automated mass probing of public APK repositories"). The literature for the corpus-scale extension of the per-APK pipeline used in the Spider Farmer, EcoFlow, Ondilo, and Balboa case studies. Both empirical base-rate anchors (already in cluster D) and the canonical large-N marketplace-abuse studies belong here.*

#### Canonical large-N studies of repackaged / malicious apps on third-party marketplaces
- **L-APK-1** [Detecting repackaged smartphone applications in third-party android marketplaces (DroidMOSS)](https://consensus.app/papers/details/cd05553fed535ca7a7bef4499a57707b/?utm_source=claude_desktop) (Zhou et al., 2012, **664 citations**). **[lit-retrieved]**. **Foundational anchor.** Six popular third-party Android marketplaces; 5%–13% of apps hosted are repackaged. Establishes the field for §7.14 "trojaned-APK detection at scale, and its inverse" bullet.
- **L-APK-2** [Sweetening android lemon markets: measuring and combating malware in application marketplaces](https://consensus.app/papers/details/825f2d744be35010bd5a5fb8da84f454/?utm_source=claude_desktop) (Vidas & Christin, 2013, **58 citations**). **[lit-retrieved]**. **Canonical alt-marketplace measurement.** 41,057 apps from 194 alternative Android marketplaces in October 2011; some markets distribute almost exclusively repackaged malware. Direct anchor for §7.14 "APK-repository operator as gatekeeper" bullet — the operator-side mitigation is the leverage point.
- **L-APK-3** [Finding Unknown Malice in 10 Seconds: Mass Vetting for New Threats at the Google-Play Scale (MassVet)](https://consensus.app/papers/details/d6ef75f9d40c579bb1a6c13d4b039ad5/?utm_source=claude_desktop) (Chen et al., 2015, **207 citations**). **[lit-retrieved]**. **Strongest scale anchor.** 1.2 million apps across 33 markets; vets each app within 10 seconds; outperforms 54 VirusTotal scanners; captures >100,000 malicious apps including 20+ likely zero-day. Empirical existence proof that corpus-scale probing is not theoretical — the only thing AI assistance changes is the *kind* of features extractable per app.
- **L-APK-4** [APPraiser: A Large Scale Analysis of Android Clone Apps](https://consensus.app/papers/details/e8dc28ad294857868f592896e3793d4b/?utm_source=claude_desktop) (Ishii et al., 2017, *IEICE Trans.*, 8 citations). **[lit-retrieved]**. **1.3 million apps**; in third-party marketplaces, 76% of clones originating in Google Play are malware. Quantifies the asymmetric distribution of malicious vs. benign repackaging across marketplace tiers.

#### Corpus-scale vulnerability and lineage measurement (closer to the §7.14 thesis)
- **L-APK-5** [Large-scale Security Measurements on the Android Firmware Ecosystem (ANDSCANNER)](https://consensus.app/papers/details/593e8b15e21b5b429bb8c3fc8e92f98d/?utm_source=claude_desktop) (Hou et al., 2022, *Proc. ICSE*, 23 citations). **[lit-retrieved]**. Largest-known firmware dataset for security measurement: **6,261 firmware images from 153 vendors and 602 Android-related CVEs**; 38 newfound vulnerabilities, 32 with CVE/CNVD numbers. Direct precedent for the §7.14 corpus-wide "vendor-by-vendor weakness inventory" output of an AI-assisted pipeline.
- **L-APK-6** [Understanding the Evolution of Android App Vulnerabilities](https://consensus.app/papers/details/f6ed65486a365ab69be03bc21b54f460/?utm_source=claude_desktop) (Gao et al., 2021, *IEEE TR*, **44 citations**). **[lit-retrieved]**. **5 million app packages**; reconstructed 28,564 versioned app lineages with ≥10 versions each (≈465,037 APKs total). Vulnerability-finding tools applied at corpus scale; documents how vulnerabilities are introduced, located, and whether they foreshadow malware.
- **L-APK-7** [A Risk Estimation Study of Native Code Vulnerabilities in Android Applications](https://consensus.app/papers/details/844d03d3c4c1551daa8c54ee50ffd195/?utm_source=claude_desktop) (Sanna et al., 2024, ArXiv, 2 citations). **[lit-retrieved]**. **>100,000 apps** analysed (40% contain native code) against 15 popular vulnerable libraries. Concrete corpus-scale "many applications contain well-known vulnerabilities" finding; supports §7.14 "identity-provider enumeration" by analogy (same pipeline shape, different features extracted).

### Claim cluster O — IoT companion apps as the integrator-side weakness surface
*Supports `paper/main.md` §6.7 ("Vulnerabilities of IoT-integrator pipelines as a system class") and reinforces clusters L (privacy) and N (corpus-scale). The literature here is closer to the integrator-side framing than cluster L, which is privacy-centric: the same companion-app surface that reveals vendor-cloud destinations also encodes the cryptographic, network, and credential weaknesses that the IoT-Integrator pipeline reads in Phase 2.*

- **L-IOTAPP-1** [IoTFlow: Inferring IoT Device Behavior at Scale through Static Mobile Companion App Analysis](https://consensus.app/papers/details/914a1aea6a235af3a1d857dc81714d98/?utm_source=claude_desktop) (Schmidt et al., 2023, *Proc. ACM CCS*, 11 citations). **[lit-retrieved]**. **Strongest direct anchor for §6.7.** Static analysis of **9,889 manually verified companion apps**. Documented findings that map exactly onto §6.7 bullets: abandoned domains, hard-coded credentials, expired certificates, and sensitive personal information being shared. The IoTFlow framework is the closest published prior art to the IoT-Integrator Phase-2 weakness analysis.
- **L-IOTAPP-2** [Looking from the Mirror: Evaluating IoT Device Security through Mobile Companion Apps](https://consensus.app/papers/details/96ed375afe2f5cc1a33851f671f22331/?utm_source=claude_desktop) (Wang et al., 2019, *Proc. USENIX Security*, **61 citations**). **[lit-retrieved]**. **>4,700 IoT devices**; 324 from 73 vendors likely vulnerable through *shared* components. Anchors the §6.7 "vendor-cloud single point of failure" and §6.7 "operational-obscurity anti-pattern" bullets — vulnerability through shared-component reuse is precisely what the cross-implementation validation (`T-CROSS-IMPL-VALIDATION`) detects per case.
- **L-IOTAPP-3** [Understanding IoT Security from a Market-Scale Perspective (IoTSpotter)](https://consensus.app/papers/details/8de7b557eb7052c9acdce717362a9863/?utm_source=claude_desktop) (Jin et al., 2022, *Proc. ACM CCS*, **31 citations**). **[lit-retrieved]**. **37,783 mobile-IoT apps from Google Play** — the largest market-scale snapshot to date. Specific findings: **94.11% of 917 high-install apps with severe cryptographic violations**; 65 vulnerable IoT-specific libraries; 7,887 apps affected by Janus. Reinforces §6.7 "static-only weakness coverage" and §7.14 "sweep at corpus scale".
- **L-IOTAPP-4** [Through the Spyglass: Towards IoT Companion App Man-in-the-Middle Attacks](https://consensus.app/papers/details/f640edf3a7da5af5bcfe7d4a6e9dd59e/?utm_source=claude_desktop) (OConnor et al., 2021, *Proc. CSET*, **15 citations**). **[lit-retrieved]**. 20 popular smart-home vendors; 16 vulnerable to companion-app MITM; conceals device users, manipulates lock state, spoofs camera images, manipulates history logs. Direct anchor for the §6.7 "operational-obscurity anti-pattern" bullet — Balboa W-3 (`TrustAllStrategy` symbol on the classpath plus a documented broken intermediate-CA chain) is the same defect class as the OConnor finding at vendor scale.
- **L-IOTAPP-5** [A Study of Vulnerability Analysis of Popular Smart Devices Through Their Companion Apps](https://consensus.app/papers/details/55f4e8b28c785dcb8a952a5344f126c2/?utm_source=claude_desktop) (Mauro Junior et al., 2019, *Proc. IEEE SPW*, **18 citations**). **[lit-retrieved]**. **96 top-selling WiFi IoT devices** on Amazon; only 32 unique companion apps (component-reuse argument); 50% no proper encryption. Anchors §6.7 "companion-app permission creep" and reinforces L-IOTAPP-2's component-reuse finding.
