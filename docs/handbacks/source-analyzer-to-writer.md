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
