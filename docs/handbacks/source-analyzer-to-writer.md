# Source Analyzer → Scientific Writer hand-back

Generated 2026-05-02 by the Source Analyzer (Stage 1.5) under orchestrator dispatch.
Each block below names a `docs/sources.md` entry that was upgraded to `[ai-confirmed]` and is therefore newly available for inline citation in `paper/main.{md,tex}` per the verification ladder.

---

## L-BLE-4 — Sivakumaran et al., 2023, AsiaCCS (Ble-Guuide) — `[ai-confirmed]`

The inline base-rate claim in §6.7 / §7.13 — "**>70% of 17,243 BLE-enabled Android APKs contain at least one security vulnerability**" — may be promoted from a footnote-only `[lit-retrieved]` reference to a normal in-text citation. Numbers verified verbatim against the ACM DL abstract (https://dl.acm.org/doi/10.1145/3579856.3595806). No claim weakening required: the entry summary tracks the abstract.

## L-SLOP-7 — Sabel & Larhammar, 2025, *Royal Society Open Science* — `[ai-confirmed]`

Now citable inline for §6 / §7.6 / §9 (AI Disclosure) and specifically as a comparator for the **deferred RDB-02 readability defect** (`docs/handbacks/readability-to-writer.md`). The Stockholm Declaration provides a published, peer-reviewed comparator framework for AI-and-science-publishing ethics, which the writer can use to recast the "novelty is the integration" framing as an *application* of an existing reform agenda (academia-controlled publishing + independent fraud detection) to the security-research interoperability context. **References-list correction:** authors are **Sabel & Larhammar** (two authors, not "et al."); DOI **10.1098/rsos.251805** (entry previously lacked a DOI).

## L-SLOP-10 — Cheng, Calhoun & Reedy, 2025, *Advances in Simulation* — `[ai-confirmed]`

Now citable inline for §9 (AI Disclosure) and the **RDB-02 fix**. Cheng et al.'s "four key principles" and "three categories" of ethical generative-AI use provide a published comparator for *practitioner-facing* AI-disclosure guidance, complementing Stockholm's *system-level* reforms. The writer can frame this paper's eight-practice register as a security-research instantiation that converges with Cheng et al.'s healthcare-simulation guidance — defusing the "novelty is the integration" overclaim by naming the prior frameworks being integrated. **References-list correction:** authors are **Cheng, Calhoun & Reedy**; DOI **10.1186/s41077-025-00350-6**.

## L-SLOP-12 — Pellegrina & Helmy, 2025, *Frontiers in AI* 8:1644098 — `[ai-confirmed]`

Now citable inline. This is the **third RDB-02 unblocker**: the writer can replace the unsupported "the novelty is our integration" framing with a sourced characterisation of the existing technical-mitigation landscape — viz. that AI detectors and AI-assisted error/citation/image-verification tools exist but are, per Pellegrina & Helmy, "not yet sufficiently accurate or reliable… for use in academic assessment." The integration claim then stands on a reviewed gap rather than on assertion. **References-list correction:** authors are **Pellegrina & Helmy** (two authors, not "et al."); DOI **10.3389/frai.2025.1644098** (entry previously had a Consensus shim URL with no DOI).

---

## RDB-02 readiness summary

The deferred H-severity readability defect **RDB-02 (unsupported-novelty framing of "the novelty is the integration")** is now writer-actionable. The required comparator triplet is in place:

- **System-level reforms** — Sabel & Larhammar 2025 (L-SLOP-7).
- **Practitioner-level ethical-use guidance** — Cheng, Calhoun & Reedy 2025 (L-SLOP-10).
- **Technical-mitigation landscape (AI detectors + error/citation/image verification)** — Pellegrina & Helmy 2025 (L-SLOP-12).

The writer can recast the §10 / §1.4 novelty claim as the *integration* of these three pre-existing strands into a security-research interoperability context, with the named comparators carrying the framing.

## Out-of-scope but flagged for the writer

- The **L-VD-5 "$125–500×" cost-asymmetry** number remains `[edge-case: load-bearing]`; if it is currently inline in §6.3 / §7, it should stay footnoted (not promoted) until human `[lit-read]`.
- The **L-VD-1 refactored-labs cornerstone** remains `[edge-case: load-bearing-cornerstone]`; same caution.
- The **L-HC-1 42.5% / 4,828-secrets** Spider Farmer cornerstone remains `[edge-case]` with fetch-failure; the writer should keep the inline number footnoted to L-HC-1 and consider hedging with the cross-confirming L-HC-3 / L-HC-7 numbers in the same span.
- The **L-HC-6 56.3% / 490,119 apps** obscurity-default baseline remains `[edge-case]`; same caution.
- The **L-BLE-5 firmware-non-patching** inference remains `[edge-case]`; if cited inline in §3 the writer should weaken the claim to match the abstract ("earlier versions still exploitable") rather than the stronger entry-summary inference ("vendors update apps without patching firmware").
- The **L-RE-2 24.4% effort-gap exemplar** remains `[ai-confirmed-attempt-failed]` pending re-fetch from an NDSS-accessible network.

---

# Slice 2 — eight further `[ai-confirmed]` upgrades + two attempt-failed

Generated 2026-05-02 by the Source Analyzer (Stage 1.5) under a second orchestrator dispatch, run in parallel with the writer pass that consumed slice 1.

## L-RE-1 — Tan et al., 2024, "LLM4Decompile" — `[ai-confirmed]`

Now citable inline for §1.4. The ">100% re-executability rate vs GPT-4o and Ghidra on HumanEval/ExeBench" claim is verbatim in the arXiv:2403.05286 abstract. No claim weakening required. Pair with L-RE-2 / L-RE-3 in the §1.4 effort-gap anchor cluster.

## L-RE-3 — Lea et al., 2025, "REx86" (ACSAC 2025) — `[ai-confirmed]`

Now citable inline for §1.4 as the **quantified caveat** to the strong-form effort-gap claim. The "31% → 53% (p=0.189)" non-significance is verbatim in the arXiv:2510.20975 abstract; the writer should preserve the existing parenthetical and may optionally add the line-level p=0.031 result as the statistically-significant complement. Note: ACSAC 2025 publication confirmed (program s41).

## L-VD-2 — Zhao et al., 2025, arXiv:2510.10148 — `[ai-confirmed]`

Now citable inline in §6.3 / §7 dual-use framing. Recommended phrasing: *"LLMs generate working PoCs in 8–34% of cases from public CVE info alone, rising to 68–72% with adaptive reasoning; 23 LLM-generated PoCs have been accepted by NVD/Exploit-DB [L-VD-2]."* Numbers verified verbatim. Use to *qualify* (not overturn) the still-edge-cased L-VD-1: refactored-lab failure (L-VD-1) and disclosed-CVE success (L-VD-2) are compatible — the asymmetric-collapse claim should explicitly note that the offensive path compresses fastest in the post-disclosure window.

## L-VD-3 — Lotfi et al., 2025, arXiv:2509.24037 — `[ai-confirmed]`

Now citable inline in the §6.3 / §7 post-disclosure-window paragraph. Recommended phrasing: *"An end-to-end CVE-to-containerised-exploit pipeline with RAG augmentation reproduced 71 of 102 CVEs (~70%) across diverse vulnerability types and languages [L-VD-3]."* Pair with L-VD-2 for the disclosed-CVE side of the asymmetric-collapse story.

## L-HC-4 — Domonkos et al., 2025, IEEE CogInfoCom — `[ai-confirmed]`

Now citable inline as the **anchor sentence of the obscurity-default rebuttal** in §§1.1, 3. The strong-form quote "*it is not possible to securely hide sensitive information within applications*" is verbatim in the IEEE Xplore (paper 11200789) abstract. Scope caveat for the writer: the study sample is 20 weather apps; phrase the inline citation so the strong-form claim reads as the authors' conclusion, not a population estimate. This is the paper's strongest direct contradiction in the corpus and should be cited where the prose currently hedges.

## L-HC-7 — Li et al., 2024 (arXiv:2412.10922; EMSE 2025) — `[ai-confirmed]`

Now citable inline in §3.6 Spider Farmer / hardcoded-secrets cluster. Numbers verified verbatim (5,135 apps; 2,142 secrets; 2,115 apps; tools = Three-Layer Filter, LeakScope, PassFinder). Recommended placement: methodological-comparison citation supporting the claim that no single detector catches all checked-in secrets — pair with L-HC-1 (LLM-based) for the *"even SOTA tooling misses ~half"* framing. Cite the EMSE 2025 journal version (DOI 10.1007/s10664-025-10772-5) consistently across `paper/main.{md,tex}` and `references.bib`.

## L-BLE-1 — Barua et al., 2022, IEEE OJ Communications Society — `[ai-confirmed]`

Now citable inline for the §1.1 / §3 BLE obscurity-as-defence baseline. Survey covers taxonomy + severity classification + mitigations; safe to cite for "comprehensive taxonomy of BLE security and privacy issues" descriptive claim. No paper-claim narrowing required.

## L-BLE-2 — Cäsar et al., 2022, *Computer Networks* — `[ai-confirmed]`

Now citable inline for §1.1 / §3 as the *versioned* weakness reference (BLE 4.0 → 5.2). Safe to cite for "weaknesses persist across spec revisions" claim. No paper-claim narrowing required.

## Out-of-scope (slice 2 attempt-failed)

- **L-HC-2** (Mykhaylova et al., 2024, CEUR-WS Vol-3826) and **L-HC-3** (Wei et al., 2025, EMSE) both remained at `[ai-confirmed-attempt-failed]`: full PDFs returned HTTP 403, but search-snippet evidence is unusually strong (verbatim numbers across multiple independent indexers). **L-HC-3 is the principal cross-confirmation for the still-edge-cased L-HC-1 cornerstone**; an institutional-network or human-led re-fetch would close the Spider Farmer §3.6 chain. Until then, the writer should keep L-HC-1 / L-HC-3 inline mentions footnoted and lean on the now-`[ai-confirmed]` L-HC-4 / L-HC-7 for in-text citation.

---

# Slice 3 — eight `[ai-confirmed]` upgrades + one edge-case (cluster A / A.3)

Generated 2026-05-03 by the Source Analyzer (Stage 1.5) under orchestrator dispatch. This slice closes the bulk of cluster A (LLM-assisted RE) and cluster A.3 (quantitative time-savings evidence for AI-assisted code work), with one edge-case (L-TS-1) reserved for human `[lit-read]` because it is the single peer-reviewed wall-clock anchor for §1.4 / §3.

## L-RE-4 — Pearce et al., 2022, "Pop Quiz!" — `[ai-confirmed]`

Now citable inline as the **honest counter-example** in §1.4. Abstract verbatim from arXiv:2202.01142 confirms the framing ("we examine if this ability can be used to help with reverse engineering … characterize the performance of the language model"). The 72,754/136,260 correct-answer figure and the "not yet ready for zero-shot reverse engineering" wording are widely cross-cited in indexers; the writer can promote this from a footnote to a normal in-text citation alongside L-RE-1 / L-RE-3 to keep the §1.4 effort-gap framing balanced.

## L-RE-5 — Pordanesh & Tan, 2024, arXiv:2406.06637 — `[ai-confirmed]`

Now citable inline in §1.4 as **qualified support**. Abstract verbatim: "Key findings indicate LLMs' proficiency in general code understanding, with varying effectiveness in detailed technical and security analyses." Use to nuance the strong-form claim at the basic-RE/malware-analysis split.

## L-RE-6 — Shang et al., 2025, *Empirical Software Engineering* — `[ai-confirmed]`

Now citable inline in §1.4 as the **multi-architecture / multi-optimisation benchmark anchor**. **arXiv ID correction:** the actual identifier is **arXiv:2504.21803** (entry previously recorded 2504.21164); writer should update `paper/references.bib` if the bibkey is currently using the wrong arXiv number. Abstract confirms the benchmark covers "function name recovery and binary code summarization" across "binaries across multiple target architectures and different optimization options".

## L-RE-7 — Chen et al., 2025, "ReCopilot" (arXiv:2505.16366) — `[ai-confirmed]`

Now citable inline in §1.4. **First-author correction**: lead author is **Guoqiang Chen** (entry already used "Chen et al."; confirm `paper/references.bib` does not still carry an older first-author guess). Quote: "ReCopilot achieves state-of-the-art performance in tasks such as function name recovery and variable type inference … averaging 13% higher performance than the second best." The 13% figure is verbatim.

## L-RE-8 — Al-Kaswan et al., 2023, SANER (BinT5) — `[ai-confirmed]`

Now citable inline in §1.4. The CAPYBARA dataset (214K decompiled function-documentation pairs) and the BLEU-4 results (60.83 source / 58.82 decompiled / 44.21 stripped) are verbatim in the arXiv:2301.01701 abstract. Replication package https://github.com/AISE-TUDelft/Capybara-BinT5 is referenceable as a methodological-artefact footnote.

## L-TS-2 — Peng, Kalliamvakou, Cihon & Demirer, 2023, arXiv:2302.06590 — `[ai-confirmed]`

Now citable inline in §1.4 / §3 as the **greenfield-RCT productivity proxy**. Verbatim quote: "The treatment group, with access to the AI pair programmer, completed the task 55.8% faster than the control group." Writer must continue to flag this as **greenfield, not RE-specific**, per the existing entry summary; do not silently promote 55.8% as a brownfield-RE comparator.

## L-TS-3 — Cui, Demirer, Jaffe, Musolff, Peng & Salz, 2025, *Management Science* — `[ai-confirmed]`

Now citable inline as the **largest peer-reviewed AI-coding-productivity RCT**. Verbatim: "When data is combined across three experiments and 4,867 developers, the analysis reveals a 26.08% increase (SE: 10.3%) in completed tasks among developers using the AI tool." Acceptance date 2025-08-12, online 2026-02-27 — references.bib should record the *Management Science* DOI 10.1287/mnsc.2025.00535 as the canonical citation, with SSRN 4945566 as a preprint footnote.

## L-TS-4 — METR, 2025, arXiv:2507.09089 — `[ai-confirmed]`

Now citable inline as the **brownfield counter-evidence anchor**. The 19% slowdown, the 24% pre-task forecast and 20% post-task self-perceived speedup, and the Cursor Pro + Claude 3.5/3.7 Sonnet tool stack are all verbatim from the METR blog and arXiv landing. Caveat: if the writer elevates this to *the* primary counter-evidence anchor for the §1.4 / §6.8 asymmetry argument, a human `[lit-read]` of the methods/limitations sections is recommended (n=16, 246 tasks — small-n, single-population). For the current paper-side framing (one of several counter-points alongside L-RE-4) `[ai-confirmed]` suffices.

## L-TS-5 — Ziegler et al., MAPS 2022 — `[ai-confirmed]`

Now citable inline in §6.8 as the **telemetry-grade self-perception anchor**. Quote: "the rate with which shown suggestions are accepted, rather than more specific metrics regarding the persistence of completions in the code over time, drives developers' perception of productivity." No wall-clock comparator — writer must continue to flag the absence per the existing entry summary.

## Out-of-scope (slice 3 edge-case)

- **L-TS-1** (Basque et al., NDSS 2026 *Decompiling the Synergy*, Distinguished Paper) is annotated `[edge-case 2026-05-03: load-bearing-anchor]` and **stays at `[lit-retrieved]`**. The abstract-level numbers (n=48, 109 h, 2.4×, ~98%, +≥66%) corroborate via the NDSS landing page, but the entry is the single peer-reviewed wall-clock anchor for the §1.4 / §3 argument and full PDF retrieval remains blocked from the harness. Promotion to inline citation requires human `[lit-read]`. Until then, the writer should retain the existing footnoted treatment and continue to anchor the inline §3 wall-clock prose on the more conservative greenfield-vs-brownfield triangulation (L-TS-2 / L-TS-3 / L-TS-4).

## Cluster A / A.3 readiness summary (post-slice-3)

Cluster A (LLM-assisted RE, §1.4) is now writer-actionable end-to-end **except** L-RE-2 (`[ai-confirmed-attempt-failed]`, awaiting NDSS-network re-fetch). Cluster A.3 (time-savings evidence, §1.4 / §3 / §6.8) is now writer-actionable for the **greenfield + brownfield triangulation** (L-TS-2 / L-TS-3 / L-TS-4 / L-TS-5) and the §6.8 asymmetry meta-finding; the §1.4 / §3 wall-clock peer-reviewed anchor (L-TS-1) remains gated on human `[lit-read]`. The §3 "10.5 h vs 60–120 h" point estimate retains the honest framing recommended in the cluster A.3 preamble.

---

# Source Analyzer → Writer hand-back, slice 4 (2026-05-03, Claude Opus 4.7)

Eight `[lit-retrieved]` entries upgraded to `[ai-confirmed]` in slice 4. None is a load-bearing anchor for a contested or first-of-its-kind quantitative claim in the paper; all are now available for normal inline citation in cluster B (LLM-assisted vulnerability discovery, §6.3 / §6.8), cluster C (hardcoded secrets in mobile apps, §3.6), and cluster D (BLE, §1.1 / §3). No edge-cases or attempt-failures this pass.

## L-VD-4 — Yao et al., 2024, *High-Confidence Computing* — `[ai-confirmed]`

Now citable inline in §6.3 / §7.13 as the **dual-use survey backbone**. Verbatim taxonomy: "categorizes the papers into 'The Good' (beneficial LLM applications), 'The Bad' (offensive applications), and 'The Ugly' (vulnerabilities of LLMs and their defenses)". **Year correction**: published online 2024-03-01 (arXiv preprint 2023-12-04). The previous entry summary "Yao et al., 2023" should be cited as **(Yao et al., 2024)** in `paper/references.bib` and any inline `paper/main.{md,tex}` reference.

## L-VD-6 — Tamberg & Bahşi, 2025, IEEE Access — `[ai-confirmed]`

Now citable inline in §6.3 as the **LLM-vs-traditional-static-analysis benchmarking anchor**. Verbatim: "LLMs can pinpoint more issues than traditional static analysis tools, outperforming traditional tools in terms of recall and F1 scores, however, LLMs are more prone to generate false positive classifications than traditional tools." **Year correction**: IEEE Access publication is **2025** (DOI 10.1109/ACCESS.2025.3541146, vol. 13, pp. 29698–29717), not 2024 as the entry summary stated; arXiv preprint 2024-05-24. Update `paper/references.bib` accordingly. **Author correction**: only two authors (Tamberg & Bahşi), not "Tamberg et al."

## L-VD-7 — Sheng et al., 2025, *ACM Computing Surveys* — `[ai-confirmed]`

Now citable inline in §6.3 as a **secondary survey citation** for the rapid-growth framing. Title correction: full title is "LLMs in Software Security: A Survey of Vulnerability Detection Techniques **and Insights**" — entry summary previously dropped the suffix; preserve the full title in `paper/references.bib`. Not load-bearing for any specific quantitative claim; do not elevate above secondary-citation status without a human `[lit-read]` pass.

## L-VD-8 — Zhou, Cao, Sun & Lo, 2024, *ACM TOSEM* — `[ai-confirmed]`

Now citable inline in §6.3 as the **systematic-literature-review anchor** for cluster B's growth narrative. Verbatim: "collected 58 primary studies over the last 6 years (2018–2024), summarized the LLMs used in these studies … 37 distinct LLMs were identified" and "interest in exploring LLMs for vulnerability detection and repair has steadily increased, peaking in 2024, with 46.6% of the total studied papers." Pair with L-VD-7 (ACM CSUR) for the survey-of-surveys framing.

## L-VD-9 — Manuel et al., 2024, arXiv:2411.04981 (DeBinVul) — `[ai-confirmed]`

Now citable inline in §6.3 as the **binary-side fine-tuning anchor**. The entry's "19–24%" range is verbatim: "performance increase of 19%, 24%, and 21% in the capabilities of CodeLlama, Llama3, and CodeGen2 respectively, in detecting binary code vulnerabilities" — i.e. CodeLlama 19% / Llama3 24% / CodeGen2 21%. Dataset size 150,872 decompiled-binary samples is verbatim. Methodologically pairs with L-RE-1 (LLM4Decompile) and L-RE-8 (BinT5).

## L-HC-5 — Piyumantha et al., 2025, SCSE 2025 — `[ai-confirmed]`

Now citable inline in §3.6 as a **small-N banking-app illustration** alongside L-HC-1 / L-HC-3 / L-HC-6 (the large-N cornerstone studies). **Caveat for the writer**: n=10 banking apps. Do **not** cite this as a base-rate anchor; the entry summary's "widespread hardcoded-key vulnerabilities" framing is verbatim from the source but the small-N qualifier should appear in any sentence that uses this citation. Pairs with L-HC-4 (20 weather apps) as the small-N category-specific evidence layer.

## L-HC-8 — Sihag, Vardhan & Singh, 2021, *Computer Science Review* — `[ai-confirmed]`

Now citable inline in §1.1 / §3.6 as the **obscurity-as-defence baseline survey**. Verbatim on the obfuscation/evasion arms race: "Malware authors employ multiple techniques (e.g. code obfuscation, packaging and encryption) to evade static analysis (signature based) and dynamic analysis (behavior based) detection methods … Driven by economic benefits, quantity and complexity of Android malware are increasing, thus making them difficult to detect." DOI 10.1016/j.cosrev.2020.100365.

## L-BLE-3 — Antonioli, Tippenhauer & Rasmussen, 2020, *ACM TOPS* — `[ai-confirmed]`

Now citable inline in §1.1 / §3 as the **standard-compliant-attack BLE anchor** — strengthens the obscurity-as-security critique because the attack succeeds *without* implementation bugs. Verbatim: "the key negotiation protocols of Bluetooth and BLE are vulnerable to standard-compliant entropy downgrade attacks … downgrade the entropy of any Bluetooth session key to 1 byte, and of any BLE long-term key and session key to 7 bytes … successfully attacked 38 Bluetooth devices (32 unique Bluetooth chips) and 19 BLE devices from different vendors." Entry summary's "19 BLE devices" is verbatim; the additional "38 Bluetooth Classic devices" can be cited if the writer wants to broaden the attack-corpus framing in §1.1.

## Slice 4 readiness summary

Cluster B (LLM-assisted vulnerability discovery, §6.3) gains five new inline-citable entries (L-VD-4, L-VD-6, L-VD-7, L-VD-8, L-VD-9), bringing the cluster's writer-actionable surface to L-VD-2, L-VD-3, L-VD-4, L-VD-6, L-VD-7, L-VD-8, L-VD-9 with L-VD-1 and L-VD-5 still gated on human `[lit-read]` (load-bearing cornerstones flagged in slice 1). Cluster C (hardcoded secrets, §3.6) gains two new inline-citable entries (L-HC-5, L-HC-8) atop the existing L-HC-2/-3/-4/-7 surface; L-HC-1 and L-HC-6 remain edge-cased on load-bearing-cornerstone grounds. Cluster D (BLE, §1.1 / §3) gains L-BLE-3 atop the existing L-BLE-1/-2/-4 surface; L-BLE-5 remains edge-cased.

---

# Slice 5 hand-back — 2026-05-03 (Claude Opus 4.7)

Pass 3 of the chained Source Analyzer sweep against the `[lit-retrieved]` backlog. Continues in file order from L-TS-6 onward (slice 4 ended at L-BLE-3). Nine entries upgraded to `[ai-confirmed]`; no edge-cases, no attempt-failures introduced this pass.

## L-TS-6 — Fang, Bindu, Gupta & Kang, 2024, arXiv:2404.08144 — `[ai-confirmed]`

Now citable inline in §6.3 / §7 as the **dual-use cost-asymmetry anchor for one-day CVE exploitation**. Verbatim: "When given the CVE description, GPT-4 is capable of exploiting 87% of these vulnerabilities compared to 0% for every other model we test (GPT-3.5, open-source LLMs) and open-source vulnerability scanners (ZAP and Metasploit)." The 87% figure in the entry summary is verbatim. Pairs with L-VD-1 / L-VD-2 / L-VD-5 (already in cluster B) for the asymmetric-collapse argument; **caveat**: the "$8.80 vs $25 per exploit, 2.8× cheaper" sub-claim was not independently verified in this pass — writer should cite the 87% headline conservatively or hold the cost figure for human `[lit-read]`.

## L-BLE-6 — Peker, Bello & Perez, 2022, *Sensors* 22(3):988 — `[ai-confirmed]`

Now citable inline in §1.1 / §3 as a **standard-non-compliance illustration on consumer wearables**. Verbatim: "even though the standards provide security mechanisms, because the Bluetooth Special Interest Group does not require that manufacturers fully comply with the standards, some manufacturers fail to implement proper security mechanisms." **Author-list correction**: full author list is Peker, Bello & Perez (Columbus State University), not "Peker et al." abbreviating to a single author; writer should use the full list on first citation. Devices analysed: Fitbit heart-rate wristband, Polar heart-rate chest strap, BLE keyboard.

## L-BLE-7 — Mantz, Classen, Schulz & Hollick, 2019, *MobiSys '19* — `[ai-confirmed]`

Now citable inline in §1.1 / §3 / §6.3 as the **methodological-precedent anchor** for chip-firmware reverse engineering as a research method. Verbatim: "we reverse engineer multiple Broadcom Bluetooth chipsets that are widespread in off-the-shelf devices … Reverse engineered functions can then be altered with the InternalBlue Python framework — outperforming evaluation kits, which are limited to documented and vendor-defined functions." Also surfaced a load-bearing security finding: "discovers a novel critical security issue affecting a large selection of Broadcom chipsets that allows executing code within the attacked Bluetooth firmware." Pairs with L-BLE-8 (Liu et al., USENIX Security 2025) and L-BLE-9 (ESPwn32, WOOT 2023) as the methodological cluster.

## L-BLE-8 — Liu, Zuo et al., 2025, USENIX Security — `[ai-confirmed]`

Now citable inline in §3 / §6.3 as the **closed-source-protocol-RE-yields-vulnerabilities anchor**. **Venue correction**: USENIX Security 2025, not unspecified 2025 (this should propagate to `paper/references.bib`). Verbatim: "reverse-engineered and verified Apple Find My and Samsung Find My Mobile, revealing seven new vulnerabilities confirmed by related vendors, with four assigned CVE/SVE numbers including three high-severity vulnerabilities." Direct methodological parallel to our case studies: closed-source vendor protocols, AI-assisted-RE-style workflow, real CVE outputs.

## L-BLE-9 — Cayre, Cauquil & Francillon, 2023, WOOT '23 — `[ai-confirmed]`

Now citable inline in §6.3 / §7 (threat model) as the **software-only repurposing anchor**. **Venue correction**: WOOT 2023 (17th IEEE Workshop on Offensive Technologies, co-located with IEEE S&P 2023), not "IEEE SPW" — this should propagate to `paper/references.bib`. Verbatim: "implemented multiple attacks on the repurposed ESP32 targeting various wireless protocols, including ones not natively supported by the chip … link-layer attacks on BLE (fuzzing, jamming) and cross-protocol injections, with only software modifications" and "ESP32 can be repurposed to interact with Zigbee or Thread devices." Strengthens the §7 dual-use point: the same RE pattern that supports legitimate integration also supports cross-protocol attack surfaces on commodity hardware.

## L-RR-1 — Boniface, Urquhart & Terras, 2024, *CLSR* 52:106004 — `[ai-confirmed]`

Now citable inline in §1.3 as the **primary IoT-specific right-to-repair review anchor**. **Caveat (rule-5 legal-interpretation)**: the entry summary tracks the abstract descriptively, but any *normative* legal claim layered on this citation requires human `[lit-read]`. Verbatim: the right "gives consumers the ability and freedom to fix their devices, or to fair access to appropriate services that can carry out repair on their behalf"; the paper "reflects on hardware, software, and data components that pose legal and policy challenges for data protection, security, and sustainability." Ascribed authorship updated to Boniface, Urquhart & Terras (3 authors, not "et al.").

## L-RR-2 — Lebloch & Rafetseder, 2024, *Frontiers in IoT* 3:1321263 — `[ai-confirmed]`

Now citable inline in §1.3 / §6.1 as the **"Right to Improve" motivation anchor**. **Author correction**: Lebloch & Rafetseder (University of Vienna) — entry previously gave "Lebloch et al."; correct to two-author form. Verbatim: "current European Union legislation as well as voluntary manufacturer interoperability initiatives fail to address user desires for adaptability, augmentability, and open-ended repurposing of Internet of Things (IoT) devices." Frames our work as instantiating, in concrete AI-assisted-integration terms, the policy gap the paper identifies. Rule-5 legal caveat: descriptive citation only.

## L-RR-3 — Urquhart, Lechelt, Boniface, Wu, Rezk, Dubey, Terras & Luger, 2024, *NordiCHI '24* — `[ai-confirmed]`

Now citable inline in §1.3 / §6.1 as the **legal-checklist anchor**. **Author correction**: 8 authors; entry previously gave "Urquhart et al." — first-author-only abbreviation is acceptable in narrow inline contexts but `paper/references.bib` should carry the full list. Verbatim: "The R2R cards consolidate analysis of 25 pieces of UK / EU legislation and standards, establishing 90 legal requirements around repair, cybersecurity, environmental design, consumer, and data rights." The "25 pieces … 90 legal requirements" figure in the entry summary is verbatim. DOI 10.1145/3679318.3685341.

## L-RR-4 — van 't Schip, 2024, arXiv:2410.17296 (2025 *Internet of Things*) — `[ai-confirmed]`

Now citable inline in §1.3 / §4.6 as the **manufacturer-cessation anchor for the EcoFlow use case**. **Date / venue correction**: arXiv preprint 2024-10-22, journal publication 2025 in Elsevier *Internet of Things*; entry previously gave "2024" only — `paper/references.bib` should carry both. Verbatim: "current European product legislation … has a blind spot for an increasing problem in the competitive IoT market: manufacturer cessation. Without the manufacturer's cloud servers, many IoT devices cannot perform core functions … consumers of the manufacturer's devices are thus often left with a dysfunctional device and, as the paper shows, hardly any legal remedies." Directly supports the §4 EcoFlow framing. Rule-5 legal caveat: descriptive citation; any policy recommendation layered on this entry requires human `[lit-read]`.

## Slice 5 readiness summary

Cluster B (§6.3 dual-use) gains L-TS-6 as the one-day-CVE quantitative anchor. Cluster D (BLE, §1.1 / §3 / §6.3) gains L-BLE-6 (consumer-wearable standard-non-compliance), L-BLE-7 (Broadcom-chipset RE methodology), L-BLE-8 (closed-source-protocol RE → CVEs), and L-BLE-9 (software-only ESP32 repurposing); all four now writer-actionable. Cluster E (right-to-repair, §1.3 / §4.6 / §6.1) gains L-RR-1, L-RR-2, L-RR-3, L-RR-4 — the §1.3 motivation paragraph is now fully writer-actionable, with rule-5 legal-interpretation caveats applied. **Three `paper/references.bib` corrections** to propagate: L-BLE-8 venue (USENIX Security 2025), L-BLE-9 venue (WOOT 2023, not "IEEE SPW"), and L-RR-4 date/venue (2024 preprint / 2025 *Internet of Things*).

---

## Pass 6 (slice 6) — 2026-05-03 — L-RR-5..7, L-LF-1, L-LF-2, L-LF-5

## L-RR-5 — Ünver, 2018, *Int. J. Law Inf. Technol.* 26(2):93–118 — `[ai-confirmed]`

Now citable inline in §1.3 / §6.1 as supplementary EU legal-toolbox commentary on IoT vendor lock-in. Verbatim: the IoT depicts "a world of networked smart objects … which all require 'interoperability'"; the paper proposes "enabling IoT (non-personal as well as personal) data portability across different ecosystems … to lessen vendor lock-in and keep the pace of innovation." Rule-5 legal caveat: descriptive citation only; do not layer normative legal opinion on this single source.

## L-RR-6 — Svensson-Hoglund, Richter, Maitre-Ekern, Russell, Pihlajarinne & Dalhammar, 2021, *J. Cleaner Production* 288:125488 — `[ai-confirmed]`

Now citable inline in §1.3 / §6.1 as the comparative EU/US repair-policy anchor. **References-list corrections**: 6 authors (entry previously gave "Svensson-Hoglund et al."); journal volume is 2021, not 2020 (article first available online 2020-12); DOI 10.1016/j.jclepro.2020.125488. Verbatim: the review "outlines legal and market barriers to stakeholder participation in repair activities" across "Intellectual Property, Consumer, Contract, Tax and Chemical laws, along with issues of design and consumer perceptions." Rule-5 legal caveat: descriptive citation only.

## L-RR-7 — Colangelo & Borgogno, 2023 online / 2024 print, *Eur. J. Risk Regul.* 15(1):137–152 — `[ai-confirmed]`

Now citable inline in §6 / §6.4 as a counter-position to one-size-fits-all interoperability mandates. **References-list corrections**: 2 authors (Colangelo, Borgogno); date 2023 online, 2024 print. Verbatim: the paper proposes "workable interoperability in IoT ecosystems aimed at ensuring market contestability without undermining incentives to innovate," drawing on the UK Open Banking experience. Useful as a calibrating cite to qualify our enthusiasm for interoperability mandates.

## L-LF-1 — Khomenko & Babichev, 2025, *IoT* 6(4):69 (MDPI) — `[ai-confirmed]`

Now citable inline in §1.3 / §3 / §4 as the **most directly comparable empirical local-first Home-Assistant deployment**. **References-list correction**: 2 authors (Khomenko, Babichev); entry previously gave "Khomenko et al." Verbatim quantitative anchors: "MQTT throughput exceeding 360,000 messages without packet loss, automatic recovery from simulated failures within three minutes, and energy savings of approximately 28% compared to baseline manual control"; "operates entirely offline, ensuring privacy and continuity without cloud dependency." Strong empirical comparator if the writer wants to pair our integration-pattern claims with a published local-first Home-Assistant baseline.

## L-LF-2 — Zavalyshyn, Legay, Rath & Rivière, 2022, *Proc. PETS* 2022(4):24–43 — `[ai-confirmed]`

Now citable inline in §1.3 / §3 as the **canonical SoK for privacy-enhancing smart-home hubs**. **References-list correction**: 4 authors (Zavalyshyn, Legay, Rath, Rivière); DOI 10.56553/popets-2022-0097. Verbatim: the paper "systematizes existing knowledge … through the analysis and categorization of 10 industrial and community-contributed systems and 37 research proposals from the literature of the past 11 years." Entry's "10 industrial / community smart-hub systems and 37 research proposals" is verbatim-confirmed.

## L-LF-5 — Dallmer-Zerbe et al., 2021, IEEE ISIE — `[ai-confirmed]`

Now citable inline in §3 / §6 as a Privacy-by-Design / offline-first voice-assistant prototype. DOI 10.1109/ISIE45552.2021.9576469. Verbatim: "smart voice assistants … but conversation data is automatically streamed to companies for machine learning. Users perceive this as privacy invasion … making local processing a central design element"; the prototype implements "Privacy by Design" with "complete offline modality."

## Edge cases (no upgrade)

- **L-LF-3** — Hewitt et al., 2024 — title and date in the entry do not match any retrievable paper. The closest match is Hewitt & Cunningham, "Taxonomic Classification of IoT Smart Home Voice Control" (arXiv:2210.15656, October 2022), which differs in title (no "Towards Privacy-Preserving" prefix), author count (2, not "et al."), and year (2022). Awaiting human disambiguation; entry summary is empty so no current paper claim is blocked.
- **L-LF-4** — Mishra et al., 2025 (Vaani) — Consensus landing page returned HTTP 403 to WebFetch; web searches across IJSRA / IRJMETS / IJRPR and general academic indexes did not surface a paper with this exact title. The "Vaani" name in 2025 maps to a Bengaluru voice-AI startup, not an academic publication. Logged as `[ai-confirmed-attempt-failed]`; researcher should verify the Consensus record is stable before retry.

## Slice 6 readiness summary

Cluster E (right-to-repair, §1.3 / §6.1) gains three more descriptive anchors (L-RR-5, L-RR-6, L-RR-7), completing the EU policy-context register; rule-5 legal caveat applies to all three. Cluster F (local-first / cloud-independence, §1.3 / §3 / §4) gains its strongest empirical anchor (L-LF-1, with 28% energy-saving and 360k-message MQTT throughput verbatim) and its canonical SoK (L-LF-2, 10 industrial + 37 research systems verbatim). L-LF-5 adds a Privacy-by-Design voice-assistant comparator. Five `paper/references.bib` corrections to propagate: author counts for L-RR-6 (6 authors), L-RR-7 (2 authors), L-LF-1 (2 authors), L-LF-2 (4 authors); date/volume for L-RR-6 (2021 vol. 288) and L-RR-7 (2023 online / 2024 print).

---

# Source Analyzer hand-back to writer — Pass 5 (slice 7) — 2026-05-03

**Agent:** Claude Opus 4.7
**Slice:** L-LAW-1, L-LAW-2, L-LAW-3, L-LAW-4, L-LAW-5, L-LAW-6 (cluster G — DMCA § 1201(f) and the legal interoperability exemption, US framing for §6.1).

**Critical caveat (CLAUDE.md rule 5; source-analyzer-prompt §Constraints).** Every entry in this slice is a legal-doctrinal text. Per pass-5 scope, the agent caps these at **`[ai-confirmed-bibliographic]`** — i.e. *bibliographic existence, authorship, and venue confirmed*; **doctrinal interpretation is not confirmed**. Inline citation in `paper/main.{md,tex}` is permitted only for descriptive, non-load-bearing framing (e.g. "the US analogue to § 69e UrhG is § 1201(f); see L-LAW-1, L-LAW-3"). Any first-of-its-kind, contested, or load-bearing legal claim — particularly anything that interprets *Chamberlain v. Skylink*, *Lexmark v. Static Control*, *Bnetd*, or the scope of § 1201(f) — must be upgraded to `[lit-read]` by the human author before inline use.

## L-LAW-1 — Band 2011 — `[ai-confirmed-bibliographic]`

Now usable inline in §6.1 as a **descriptive** US-side anchor for the §6.1 European-vs-US legal-framing comparison. Bibliographic record verified: chapter 3 of Band & Katoh, *Interfaces on Trial 2.0*, MIT Press, 2011, DOI 10.7551/mitpress/9780262015004.003.0003. Suggested cite form: "(Band & Katoh, 2011)" — note the entry currently lists Band only; **`paper/references.bib` correction needed**: add Masanobu Katoh as second author. Quote (publisher abstract): "Chamberlain v. Skylink was a major development in DMCA jurisprudence because it prevented the DMCA from being employed to prevent legitimate competition in aftermarkets by requiring a nexus between the circumvention of access controls and infringement." Doctrinal interpretation of *Chamberlain* gates on `[lit-read]`.

## L-LAW-3 — Perzanowski 2008/2009 — `[ai-confirmed-bibliographic]`

Now usable inline in §6.1 / §6.4 as a **descriptive** anchor for "policy direction towards broader interoperability exemption". Bibliographic record verified: *UC Davis Law Review* 42(5):1549–1620 (2009). **`paper/references.bib` correction needed**: year is 2009 (official publication), not 2008 (SSRN posting); the entry currently uses 2008. Standard convention is to cite the official publication year. Quote: "the anticircumvention provisions of the DMCA represent a troubling departure from intellectual property policy ... proposes expanding the DMCA's existing interoperability exemption to create an environment more hospitable to interoperable technologies." Any claim about Perzanowski's specific policy proposal requires `[lit-read]`.

## L-LAW-5 — AllahRakha 2025 — `[ai-confirmed-bibliographic]`

Bibliographic record verified: *Jurisdictie: Jurnal Hukum dan Syariah* 15(2), January 2025, author Naeem AllahRakha. **`paper/references.bib` correction needed**: author surname is "AllahRakha" (one word, capitalised "R"), not "Allahrakha". Comparative weight: Indonesian sharia/legal journal — fine for a "see also" citation but the human author should weigh whether to elevate it above the US/EU-focused L-LAW-1, L-LAW-3, L-LAW-6 anchors in §6.1.

## L-LAW-6 — Torsen 2004 — `[ai-confirmed-bibliographic]`

Now usable inline in §6.1 as a **descriptive** companion to L-LAW-1 for *Chamberlain* / *Lexmark* framing. Bibliographic record verified: *Chicago-Kent Journal of Intellectual Property* 4(1), 2004, author Molly Torsen. Full title: "Lexmark, Watermarks, Skylink and Marketplaces: Misuse and Misperception of the Digital Millennium Copyright Act's Anticircumvention Provision" (the entry truncates "Digital Millennium Copyright Act's" to "DMCA's" — acceptable colloquial form, but the references-list should use the full title). Doctrinal claim about the *Lexmark* holding gates on `[lit-read]`.

## Attempt-failed (no upgrade, no inline-cite gain)

- **L-LAW-2** — Neufeld, 2007, *Review of Litigation* — bibliographic existence not independently verifiable from open sources. Three targeted searches (full title, author + venue, author + *Bnetd*) returned no match; Consensus landing returned 403 to WebFetch. **Recommend** human researcher attempt direct retrieval via HeinOnline or *Texas Review of Litigation* archives; the entry's *Bnetd*-paradigm-case framing is currently anchored on a paper that may be misattributed. If retrieval fails again, recommend dropping L-LAW-2 and using the EFF *Bnetd* case writeup (already widely cited in DMCA scholarship) as a substitute, distinguishing journalism from legal scholarship.
- **L-LAW-4** — Liu, 2018, "DMCA 101: Introduction to Section 1201" — no unique 2018 article by an author surnamed Liu with this title surfaced. The closest open candidate ("What is Section 1201 Digital Millennium Copyright Act?: A Legislative Primer", IIPSJ) has no Liu attribution. **Recommend** verifying the Consensus record's author/year — possible mis-extraction by the upstream tool. Entry is "primer-level reference" so non-load-bearing; safe to retire if retrieval fails.

## `paper/references.bib` corrections to propagate

| Entry | Field | Current | Should be |
|-------|-------|---------|-----------|
| L-LAW-1 | author | "Band, 2011" | "Band, J., & Katoh, M., 2011" (chapter is co-authored) |
| L-LAW-3 | year | 2008 | 2009 (official *UC Davis Law Review* publication; 2008 = SSRN posting) |
| L-LAW-5 | author | "Allahrakha" | "AllahRakha" (one word, capital R) |
| L-LAW-6 | title | "DMCA's Anticircumvention Provision" | "Digital Millennium Copyright Act's Anticircumvention Provision" (full title) |

## Slice 7 readiness summary

Cluster G (§6.1 US-analogue framing) is now writer-actionable for **descriptive** use through four entries (L-LAW-1, L-LAW-3, L-LAW-5, L-LAW-6) under explicit rule-5 doctrinal hedges. The two attempt-failed entries (L-LAW-2, L-LAW-4) do not block the §6.1 framing, since L-LAW-1 / L-LAW-6 jointly carry the *Chamberlain* / *Lexmark* doctrinal-turning-point story and L-LAW-3 carries the policy-direction story. **All four newly available entries remain gated at `[ai-confirmed-bibliographic]`** for any interpretive claim — only `[lit-read]` unlocks doctrinal use. The companion EU/German entries (S-EF-9 § 69e UrhG, S-EF-10 EU 2009/24/EC) remain `[unverified-external]` per existing register and require a separate German-language research pass.

---

# Source Analyzer hand-back to writer — Pass 6 (slice 8) — 2026-05-03

**Agent:** Claude Opus 4.7
**Slice:** L-COUNTER-1 .. L-COUNTER-6 (cluster H — counter-positions / dual-use risk amplifiers, supports `paper/main.md` §6.4).
**Scope:** non-legal cluster — standard `[ai-confirmed]` ladder applies (no doctrinal hedge).

## L-COUNTER-1 — Boniface, Fair, Modafferi & Papa, 2020, CEUR-WS Vol. 2900 — `[ai-confirmed]`

Now citable inline in §6.4 as the **most direct counter-citation to interoperability enthusiasm**. Verbatim: "Higher levels of interoperability generally means more links between components, but also means a higher number of potential security threats." **`paper/references.bib` correction**: full author list is Boniface, Fair, Modafferi, Papa (4 authors), not "et al."; venue is CEUR-WS workshop proceedings (Vol. 2900, paper 7), not a peer-reviewed journal — frame accordingly. Suitable as a framing / motivation cite; load-bearing quantitative claims should fall back on L-COUNTER-3 or L-COUNTER-6.

## L-COUNTER-2 — Mitra & Ransbotham, 2015, *Information Systems Research* 26(3):565–584 — `[ai-confirmed]`

Now citable inline in §6.4 / §1 as the **foundational empirical anchor for the "full disclosure is not free" qualifier on the obscurity-is-dead thesis**. Verbatim: "Full disclosure accelerates the diffusion of attacks, increases the penetration of attacks within the target population, and increases the risk of first attack after the vulnerability is reported. However, although the aggregate volume of attacks remains unaffected by full disclosure, attacks occur earlier in the life cycle of the vulnerability." Methodology anchor: 2.4B IDS alerts from 960 firms — large-N, *Information Systems Research* premier venue. **Strong** load-bearing source for the qualifier framing.

## L-COUNTER-3 — Augusto, Belchior, Correia, Vasconcelos, Zhang & Hardjono, 2024, IEEE S&P 2024 — `[ai-confirmed]`

Now citable inline in §6.4 as the **quantitative anchor for interoperability-as-attack-surface**. Verbatim losses: ~$3.1B from cross-chain bridge hacks; SLR over 212 documents; 65.8% of stolen funds traced to "intermediary permissioned networks with unsecured cryptographic key operations". **`paper/references.bib` correction**: full author list is Augusto, Belchior, Correia, Vasconcelos, Zhang, Hardjono (6 authors), not "et al." Domain-distance caveat applies (blockchain bridges, not consumer IoT) — use as analogy with explicit hedging.

## L-COUNTER-4 — Silic, 2013, *Computers & Security* 39(B):386–395 — `[ai-confirmed]`

Now citable inline in §6.4 / §7 as a triangulated organisational-context dual-use anchor. Verbatim: "contributors behind open source security software (OSSS) are hackers, OSSS have important dual-use dimension, information security professionals generally trust OSS, and large organizations will avoid adopting and using OSSs." Useful as the organisational counterpart to L-COUNTER-5's IR-theory framing.

## L-COUNTER-5 — Vaynman & Volpe, 2023, *International Organization* 77(3):599–632 — `[ai-confirmed]`

Now citable inline in §6.4 / §7 as the **theoretical framing of dual-use distinguishability and integration**, applicable to AI-assisted RE. Verbatim: "the duality of technology matters because it shapes the tension between detection and disclosure at the heart of arms control: agreements must provide enough information to detect violations, but not so much that they disclose deeper security vulnerabilities." **`paper/references.bib` correction (load-bearing)**: second author is **Tristan A. Volpe**, *not* "Gartzke" as the entry mis-attributes. This must be fixed before any inline citation. Won IO's 2023 Robert O. Keohane Award (signal of venue endorsement).

## L-COUNTER-6 — Manadhata & Wing, 2011, *IEEE Transactions on Software Engineering* 37(3):371–386 — `[ai-confirmed]`

Now citable inline in §4.6 as the **canonical attack-surface formalisation** — needed to make the "blast radius" claim quantitative rather than rhetorical. Verbatim: defines attack surface along three abstract dimensions — method, data, channel; "agnostic to a software system's implementation language and is applicable to systems of all sizes". 658 citations — high authority. Best-of-class anchor for §4.6.

## `paper/references.bib` corrections to propagate

| Entry | Field | Current | Should be |
|-------|-------|---------|-----------|
| L-COUNTER-1 | author | "Boniface et al., 2020" | "Boniface, M., Fair, N., Modafferi, S., & Papa, J., 2020" (4 authors) |
| L-COUNTER-3 | author | "Augusto et al., 2024" | "Augusto, A., Belchior, R., Correia, M., Vasconcelos, A., Zhang, L., & Hardjono, T., 2024" (6 authors) |
| L-COUNTER-5 | author | "Vaynman & Gartzke, 2023" | "Vaynman, J., & Volpe, T. A., 2023" — **load-bearing fix; the entry mis-attributes the second author** |

## Slice 8 readiness summary

Cluster H (§6.4 counter-positions) is now fully writer-actionable: six `[ai-confirmed]` upgrades, no edge-cases, no fetch failures. The non-legal cluster ran cleanly under the standard ladder (no rule-5 doctrinal cap). Three `paper/references.bib` corrections to propagate, of which **L-COUNTER-5 is load-bearing** (wrong second author). The §6.4 dual-use qualifier is now anchored on (a) Mitra & Ransbotham 2015 *ISR* large-N empirical (full disclosure dynamics), (b) Augusto et al. 2024 IEEE S&P quantitative ($3.1B in cross-chain losses), (c) Vaynman & Volpe 2023 *IO* theoretical (detection-disclosure tension), with Boniface 2020 (interoperability-as-threat-multiplier) and Silic 2013 (organisational dual-use) as supporting framing, and Manadhata & Wing 2011 (attack-surface metric) as the §4.6 quantitative anchor.

---

## Slice 9 (pass 7, 2026-05-03) — cluster I sloppification anchors — nine `[ai-confirmed]` upgrades

Slice 9 closes the §1.4 / §7.6 / §10 sloppification cluster. All nine remaining `[lit-retrieved]` entries in cluster I have been verified. After this pass, cluster I is fully `[ai-confirmed*]` with zero residual `[lit-retrieved]` items.

### L-SLOP-1 — Walters & Wilder, 2023, *Scientific Reports* — `[ai-confirmed]`

Now citable inline as **the headline quantitative anchor for the §1.4 / §7.6 fabricated-citation base rate**. Verbatim from the abstract (https://www.nature.com/articles/s41598-023-41032-5): "55% of the GPT-3.5 citations but just 18% of the GPT-4 citations are fabricated. Likewise, 43% of the real (non-fabricated) GPT-3.5 citations but just 24% of the real GPT-4 citations include substantive citation errors." Methodology: 84 short literature reviews on 42 multidisciplinary topics, 636 citations analysed. The entry's number-block matches the source verbatim — no claim weakening required.

### L-SLOP-2 — Chelli et al., 2024, *J. Med. Internet Res.* — `[ai-confirmed]`

Now citable inline as the **medical-systematic-review hallucination anchor** for §7.6. Verbatim hallucination rates **39.6% (GPT-3.5) / 28.6% (GPT-4) / 91.4% (Bard)**; precision **9.4% / 13.4% / 0%**; recall **11.9% / 13.7% / 0%**; methodology 11 systematic reviews × 3 LLMs, 471 references. Exact match to entry summary; cite alongside L-SLOP-1 to bracket the GPT-3.5→4 hallucination delta with two independent samples.

### L-SLOP-3 — Buchanan, Hill & Shapoval, 2024, *American Economist* 69(1):80–87 — `[ai-confirmed]`

Now citable inline as the **discipline-spanning replication of the fabrication base rate** (economics, n=Journal-of-Economic-Literature topics, GPT-3.5 vs. GPT-4). Verbatim: ">30% of GPT-3.5 citations do not exist; only slightly reduced for GPT-4… reliability decreases as prompts become more specific." **`paper/references.bib` correction (bibliographic):** add third author **Olga Shapoval**; SAGE-published 2024 (vol. 69(1):80–87, DOI 10.1177/05694345231218454), not 2023; original SSRN preprint dated November 2023. Useful as a *third* discipline (after biomedicine + multidisciplinary) showing the same effect.

### L-SLOP-4 — McGowan et al., 2023, *Psychiatry Research* 326:115334 — `[ai-confirmed]`

Now citable inline as the **striking case-study anchor for §7.6** (often cited but worth keeping the numbers straight). Verbatim: "ChatGPT… generated thirty-five citations, two of which were real. 12 citations were similar to actual manuscripts… and the remaining 21, while plausible, were in fact a pastiche of multiple existent manuscripts." Entry summary matches. The "pastiche" framing is verbatim from the source and is unique among the cluster — recommend foregrounding it in the §7.6 narrative.

### L-SLOP-5 — Kendall & Teixeira da Silva, 2024, *Learned Publishing* 37(1):55–62 — `[ai-confirmed-bibliographic]`

Bibliographic and key-points confirmation only (full text paywalled at Wiley; ScienceOpen records the article's "Key Points" but not the body). Citable inline for the **system-level claim that LLMs amplify predatory publishing and paper mills**, which is the entry's core summary and matches the published Key Points verbatim. **`paper/references.bib` correction:** journal year is **2024** (vol. 37 issue 1, Jan 2024 print); online-version-of-record 2023-09-08; DOI 10.1002/leap.1578.

### L-SLOP-6 — Liverpool, 2023, *Nature* 618:222–223 — `[ai-confirmed]`

Now citable inline as the **journalistic comparator for §7.6** (Nature News on the May 2023 paper-mill summit). Verbatim: "Generative AI tools, including chatbots such as ChatGPT and image-generating software, provide new ways of producing paper-mill content, which could prove particularly difficult to detect." Use sparingly — this is news-feature, not peer-reviewed research; pair with L-SLOP-5 / L-SLOP-8 for the empirical / argumentative weight.

### L-SLOP-8 — Suchak et al., 2025, *PLOS Biology* 23(5):e3003152 — `[ai-confirmed]`

Now citable inline as **the most consequential upgrade in this slice**: it is the only **direct empirical observation** of AI-amplified paper-mill output growth in the literature. Verbatim numbers verified at https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3003152: "the systematic search strategy used here identified an average of **4 papers per annum from 2014 to 2021, but 190 in 2024–9 October alone**", drawn from a corpus of **341 NHANES-derived single-factor papers over a decade**. The entry summary's "190 in the first ten months of 2024" is exact (paper says "9 October", which is the 282nd day of 2024 — consistent with the entry's "first ten months" rounding). Recommend foregrounding this as the §7.6 / §10 *empirical centrepiece* — it is the only post-2024 dataset with concrete pre/post AI-era counts in the cluster.

### L-SLOP-9 — Mugaanyi et al., 2024, *J. Med. Internet Res.* 26:e52935 — `[ai-confirmed]`

Now citable inline as the **disciplinary-variance anchor**: DOI hallucination 89.4% (humanities) vs. 61.8% (natural sciences), citation-existence 76.6% / 72.7%. Useful for §7.6 to caveat that the §1.4 base rates are *averaged* across disciplines and that the humanities tail is materially worse. **`paper/references.bib` correction:** journal year is **2024** (vol. 26, e52935, published 2024-04-05), not 2023; DOI 10.2196/52935.

### L-SLOP-11 — Lund et al., 2023, *JASIST* 74(5):570–581 — `[ai-confirmed]`

Now citable inline as the **library-and-information-science cornerstone** for §7.6 / §9 (AI Disclosure) framing. Open-access preprint at arXiv:2303.13367 used for the read; abstract verbatim. 639 citations in the entry — strong authority signal. Use as a structural / framing reference, not for any specific quantitative claim (the paper is qualitative).

---

## Slice 9 readiness summary

Cluster I (§1.4 / §7.6 / §10 sloppification) is now fully `[ai-confirmed*]`: nine new upgrades (L-SLOP-1, -2, -3, -4, -6, -8, -9, -11 as `[ai-confirmed]`; L-SLOP-5 as `[ai-confirmed-bibliographic]` due to publisher paywall on Wiley body text), zero edge-cases, zero fetch failures. Combined with passes 1–6 confirmations (L-SLOP-7 Stockholm, L-SLOP-10 Cheng, L-SLOP-12 Pellegrina), the entire 12-entry sloppification cluster is now writer-actionable.

The §1.4 / §7.6 quantitative spine is anchored on three independent samples: Walters & Wilder 2023 (multidisciplinary, 55%/18% fabrication), Chelli et al. 2024 (medical, 39.6%/28.6% / 91.4% hallucination), Buchanan, Hill & Shapoval 2024 (economics, >30% / slightly less). The §10 paper-mill claim is anchored on Suchak et al. 2025's 4→190 NHANES-papers/year jump. The §9 framing is anchored on Lund et al. 2023 (cornerstone) + Cheng et al. 2025 (practitioner ethics) + Sabel & Larhammar 2025 (system reform) + Pellegrina & Helmy 2025 (technical mitigation).

### `paper/references.bib` corrections to propagate

| Entry | Field | Current | Should be |
|-------|-------|---------|-----------|
| L-SLOP-3 | authors | "Buchanan & Hill, 2023" | "Buchanan, J., Hill, S., & Shapoval, O., 2024" — third author missing; SAGE journal year is 2024 |
| L-SLOP-5 | year | "2023" | "2024" (Learned Publishing 37(1):55–62, Jan 2024 print issue; online VoR 2023-09-08) |
| L-SLOP-9 | year | "2023" | "2024" (JMIR 26:e52935, published 2024-04-05) |

---

## Slice 10 (pass 8, 2026-05-03) — cluster J model collapse anchors — nine `[ai-confirmed]` upgrades

Slice 10 closes the §7.7 model-collapse / dilution-of-the-scientific-commons cluster. All nine `[lit-retrieved]` entries in cluster J have been verified. After this pass, cluster J is fully `[ai-confirmed]` with zero residual `[lit-retrieved]` items and zero edge-cases.

### L-MC-1 — Shumailov et al., 2024, *Nature* 631:755–759 — `[ai-confirmed]`

Now citable inline as **the canonical model-collapse anchor for §7.7**. Verified via publisher landing https://www.nature.com/articles/s41586-024-07566-y and Edinburgh open-access copy. Three-modality scope (LLMs, VAEs, GMMs) confirmed verbatim. DOI 10.1038/s41586-024-07566-y; an Author Correction was issued in 2025 (https://www.nature.com/articles/s41586-025-08905-3) — writer should consider citing the corrected version.

### L-MC-2 — Shabgahi et al., 2025, arXiv:2509.08972 — `[ai-confirmed]`

Now citable inline as the **training-layer mitigation aside**: Truncated-Cross-Entropy loss extends the fidelity interval >2.3× before collapse. Use sparingly in §7.7 — this is a single-paper preprint (2025) without peer-review yet; pair with L-MC-4 / L-MC-6 for the broader mitigation framing.

### L-MC-3 — Seddik et al., 2024, COLM 2024, arXiv:2404.05090 — `[ai-confirmed]`

Now citable inline as the **statistical-impossibility anchor**: collapse cannot be avoided on purely synthetic training; mixing real + synthetic admits a threshold below which collapse can be avoided. Pair with L-MC-4 (constructive accumulation result) and L-MC-8 (Borji qualifier) for the §7.7 theoretical triangle.

### L-MC-4 — Gerstgrasser et al., 2024, arXiv:2404.01413 — `[ai-confirmed]`

Now citable inline as the **strongest constructive result for §7.7**: accumulating (rather than replacing) synthetic data alongside real data yields a finite test-error upper bound. This is the empirical/theoretical bridge between L-MC-1's pessimism and the practitioner reality of mixed corpora. **Use with the L-MC-8 qualifier** — Borji's note tempers the optimism.

### L-MC-5 — Suresh, Thangaraj & Khandavally, 2024, arXiv:2412.17646 — `[ai-confirmed]`

Now citable inline as the **rate-of-collapse refinement**: collapse rate for fundamental distributions (discrete, Gaussian) under ML estimation. Useful as a footnote in §7.7 for the claim that collapse can be slow in some regimes, qualifying any "imminent dilution" language.

### L-MC-6 — Shi et al., 2025, NeurIPS 2025 Spotlight, arXiv:2509.16499 — `[ai-confirmed]`

Now citable inline as the **mechanism-reframing anchor**: collapse as a generalisation-to-memorisation transition driven by declining synthetic-data entropy. Useful for §7.7 when discussing *why* collapse occurs rather than *that* it occurs. NeurIPS 2025 Spotlight is a strong venue signal.

### L-MC-7 — Shumailov et al., 2023, arXiv:2305.17493 — `[ai-confirmed]`

Now citable inline as the **arXiv-preprint companion to L-MC-1**. Recommend the writer pick *one* of L-MC-1 / L-MC-7 to cite (typically L-MC-1 for the *Nature* version unless an arXiv-preferring audience needs the preprint). Both are now writer-actionable.

### L-MC-8 — Borji, 2024, arXiv:2410.12954 — `[ai-confirmed]`

Now citable inline as the **statistical-phenomenon qualifier**: collapse may be unavoidable as a general statistical phenomenon (collapse towards univariate Gaussian under repeated KDE sampling/refitting). Use to temper L-MC-4's optimism in the §7.7 narrative arc.

### L-MC-9 — Hu et al., 2025, arXiv:2505.08803 — `[ai-confirmed]`

Now citable inline as the **multi-modal extension**: VLMs and text-to-image diffusion in recursive multi-agent loops; mitigations include increased decoding budgets, model diversity, and frozen-relabelling. Useful if §7.7 discusses image/code/text co-generation as part of the dilution argument.

---

## Slice 10 readiness summary

Cluster J (§7.7 model collapse / dilution of the scientific commons) is now fully `[ai-confirmed]`: nine new upgrades, zero edge-cases, zero fetch failures. The §7.7 narrative spine is now anchored on:
- **Canonical statement** — L-MC-1 (Shumailov 2024 *Nature*) / L-MC-7 (Shumailov 2023 arXiv preprint).
- **Theoretical triangle** — L-MC-3 (Seddik: collapse unavoidable on pure synthetic), L-MC-4 (Gerstgrasser: bounded with accumulation), L-MC-8 (Borji: may be unavoidable as a general statistical phenomenon).
- **Mechanism / mitigation refinements** — L-MC-2 (TCE loss), L-MC-5 (rate of collapse), L-MC-6 (entropy-driven generalisation→memorisation).
- **Multi-modal extension** — L-MC-9 (VLMs + diffusion).

No `paper/references.bib` corrections required for cluster J — author lists, years, and venues in the entry summaries match the verified records (Shumailov 2024 *Nature* 631:755–759; Borji 2024 arXiv; Gerstgrasser 2024 arXiv; Seddik 2024 COLM/arXiv; Suresh et al. 2024 arXiv; Shi et al. 2025 NeurIPS arXiv; Hu et al. 2025 arXiv; Shabgahi et al. 2025 arXiv). The writer should consider citing the **2025 Author Correction** (https://www.nature.com/articles/s41586-025-08905-3) alongside L-MC-1 if it materially affects the headline numbers — flagged for human review but not load-bearing for the §7.7 prose.

---

## Slice 11 (pass 9, 2026-05-03) — cluster K-CONS — six upgrades available for inline citation

These entries are now writer-actionable for §3 (case-study framing) and §4 (consumer-IoT empirical baseline). All six are `[ai-confirmed]` (or `[ai-confirmed-bibliographic]` for the survey) and may be promoted from footnote-only references to in-text citations.

### L-CONS-1 — Zhao et al., 2022, *IEEE TDSC* — `[ai-confirmed]`

Now citable inline as the **headline consumer-IoT base-rate anchor**: 1,362,906 deployed IoT devices analysed; **385,060 (28.25%)** carry at least one N-day vulnerability. Strongest single quantitative claim available for "consumer hardware is broadly vulnerable" framing in §3 / §4. Use verbatim figure (28.25%) — no rounding tightening required.

### L-CONS-2 — Kumar et al., 2019, USENIX Security — `[ai-confirmed]`

Now citable inline as the **most-cited home-IoT measurement**: 83M devices across 16M households (Stanford / UIUC / Avast). Use as the breadth complement to L-CONS-1's depth: regional variance and weak default credentials are documented at internet scale.

### L-CONS-3 — Davis et al., 2020, *IEEE IoT Journal* — `[ai-confirmed]`

Now citable inline as the **lesser-known-vendor qualifier**: directly supports the Spider Farmer / EcoFlow PowerOcean positioning in §3 / §4. The paper's main finding (lesser-known vendors are less-regulated and less-scrutinised) is verbatim aligned with the entry summary.

### L-CONS-4 — Alladi et al., 2020, *IEEE Consumer Electronics Magazine* — `[ai-confirmed-bibliographic]`

Use only as a **survey citation** for the broader context of consumer-IoT attack categories. Bibliographic-only confirmation per rule 5 (no specific quantitative claim is anchored to it).

### L-CONS-5 — Williams et al., 2017, IEEE ISI — `[ai-confirmed]`

Now citable inline as the **Shodan + Nessus corroborating measurement**. Use as additional supporting evidence for L-CONS-1's base-rate claim, not as a sole anchor.

### L-CONS-6 — Allifah & Zualkernan, 2022, *IEEE Access* — `[ai-confirmed]`

Now citable inline as the **AHP framework reference**. Available if §3 / §4 wants to invoke a multi-criterion device-category ranking; not load-bearing for any current claim. Network-security priority weight (0.6893) is the most quotable specific figure if needed.

---

## Slice 11 readiness summary

Cluster K-CONS (consumer-IoT base rate) is now fully `[ai-confirmed]`: five `[ai-confirmed]` plus one `[ai-confirmed-bibliographic]`; zero edge-cases, zero fetch failures. The §3 / §4 base-rate scaffolding is now anchored on:
- **Headline quantitative anchor** — L-CONS-1 (Zhao 2022, *IEEE TDSC*: 28.25% of 1.36M devices vulnerable).
- **Breadth corroboration** — L-CONS-2 (Kumar 2019 USENIX: 83M devices) and L-CONS-5 (Williams 2017 ISI: Shodan + Nessus).
- **Lesser-known-vendor qualifier** — L-CONS-3 (Davis 2020 *IEEE IoT J*).
- **Survey context** — L-CONS-4 (Alladi 2020 *IEEE CEM*).
- **Optional ranking framework** — L-CONS-6 (Allifah 2022 *IEEE Access*).

No `paper/references.bib` corrections required for cluster K-CONS — author lists, years, and venues match the verified records.
