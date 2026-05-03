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
