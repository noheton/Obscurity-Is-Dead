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
