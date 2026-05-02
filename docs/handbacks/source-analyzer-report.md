# Source Analyzer Report — 2026-05-02 (parallel run, slice 1)

**Agent:** Claude Opus 4.7 dispatched as five parallel sub-agents by Stage 0 (Orchestrator) per `docs/handbacks/orchestrator-dispatch.md` entry 2026-05-02T19:00:00Z.
**Scope:** 10 critical-path entries selected from the 129 `[lit-retrieved]` backlog in `docs/sources.md`. Selection prioritised entries inline-cited from `paper/main.md` and entries that unblock the deferred H-severity readability defect **RDB-02** (unsupported-novelty framing, per `docs/handbacks/readability-to-writer.md`).

## Per-entry decision table

| Entry | Decision | Reason | Critical-path? | Quote |
|-------|----------|--------|----------------|-------|
| L-RE-2 | `[ai-confirmed-attempt-failed]` | NDSS PDF + 3 mirrors returned HTTP 403 to fetch tool; abstract claim independently surfaced via search snippet but full text not read by agent | yes (§1.4 effort-gap exemplar) | "achieves a 24.4% reduction in the cognitive burden of understanding decompiler outputs" |
| L-VD-1 | `[edge-case: load-bearing-cornerstone]` | First-of-its-kind refactored-labs result; only partial cross-confirmation via L-VD-2 (which the entry itself flags as "partially contradicting"); full text 403 | yes (§6.3) | "no model successfully generated exploits for the five custom labs with refactored code" |
| L-VD-5 | `[edge-case: load-bearing]` | Abstract confirms qualitative dual-use + "cost likely lower than with human effort alone" framing, but the specific "$125–500×" figure is the first-of-its-kind quantitative anchor — criterion 3 requires `[lit-read]` | yes (§6.3, §7) | "this content can be generated economically and at cost likely lower than with human effort alone" |
| L-HC-1 | `[edge-case: load-bearing-cornerstone]` | Cornerstone for §3.6 Spider Farmer thesis (criterion 3) + full text not retrievable (criterion 1); abstract numbers (42.5%; 4,828 secrets) cross-checked from search snippet | yes | "5000 apps … detected secrets in 2124 apps (42.5%) … 4828 secrets … undetected by existing approaches" |
| L-HC-6 | `[edge-case: load-bearing-cornerstone]` | Cornerstone for the obscurity-default baseline; full text 403; abstract numbers (490,119 apps; 56.3%) match | yes | "490,119 Android apps … 56.3% … do not use Android's trusted hardware capabilities at all" |
| L-BLE-4 | **`[ai-confirmed]`** | All five criteria hold; numbers (17,243; >70%) match verbatim against ACM DL abstract; base-rate, not first-of-its-kind contested | yes (§6.7, §7.13) | "a large-scale analysis of 17,243 free, BLE-enabled Android APKs ... more than 70% of these APKs contain at least one security vulnerability" |
| L-BLE-5 | `[edge-case: load-bearing]` | Abstract supports "old versions exploitable" but does not verbatim assert vendor firmware-non-patching as the entry summary infers; load-bearing for §3 Spider Farmer analog | yes (§3) | "earlier versions of the companion apps can still be exploited to attack IoT devices" |
| L-SLOP-7 | **`[ai-confirmed]`** | Abstract enumerates the four planks the entry summarises; reputable venue (RSOS); narrow uncontested reform-agenda claim | yes (RDB-02 comparator) | "Academia should resume control of publishing using non-profit publishing models... merit quality, not quantity... independent of publishers" |
| L-SLOP-10 | **`[ai-confirmed]`** | Abstract and body confirm "four key principles" + "three categories" framing; open-access (Springer/BMC); narrow ethics-guidance claim | yes (RDB-02 comparator, §9) | "three categories of specific ways generative AI tools can be used in an ethically sound manner and offer four key principles" |
| L-SLOP-12 | **`[ai-confirmed]`** | Abstract + conclusion match entry summary verbatim (AI detectors + statistical / citation / image verification); narrow descriptive review | yes (RDB-02 comparator) | "these developments are not yet sufficiently accurate or reliable yet for use in academic assessment, they mark an early but promising steps toward scalable, AI-assisted quality control" |

## Counts

- Entries processed: 10
- Upgraded to `[ai-confirmed]`: 4 (L-BLE-4, L-SLOP-7, L-SLOP-10, L-SLOP-12)
- Edge-cased: 5 (L-VD-1, L-VD-5, L-HC-1, L-HC-6, L-BLE-5) — all five flagged either as load-bearing-cornerstone (criterion 3) or as load-bearing-with-fetch-failure (criteria 1+3)
- Fetch-failed: 1 (L-RE-2 — NDSS PDF + 3 mirrors returned 403; abstract content surfaced via search snippet but criterion 1 not satisfied)

## Most consequential upgrade

**L-SLOP-7 + L-SLOP-10 + L-SLOP-12 (joint).** Together these provide the comparator citations the writer needs to clear **RDB-02**: the deferred H-severity readability defect that requires the paper to recast its "the novelty is the integration" framing as an *application of an existing reform agenda* (Stockholm Declaration system-level reforms; Cheng et al. practitioner-level disclosure principles; Pellegrina & Helmy technical-mitigation review of AI detectors and AI-assisted error/citation/image verification). The next writer pass can promote each from `[lit-retrieved]` footnote to inline citation and reframe §10's novelty claim as integration-on-top-of-named-prior-work.

## Most consequential edge case

**L-HC-1 (Alecci et al., 2025, SecretLoc).** The entry is the strongest single citation for the §3.6 Spider Farmer thesis but (a) its specific "42.5% / 4,828 secrets" numbers are unique to it, no other entry cross-confirms them at that scale, and (b) full-text retrieval was blocked across arXiv/alphaXiv/SemanticScholar/ResearchGate with HTTP 403 from this harness. Until a human reads the paper or the agent re-runs from a network with arXiv access, the inline 42.5% number stays at `[lit-retrieved]` and cannot be promoted past `[ai-confirmed]`. This is the principal residual blocker for §3.6 inline citation upgrade.

## Provenance / methodology note

This run was **the parallel-dispatch variant** — Stage 0 (Orchestrator) launched five independent sub-agents, each scoped to two entries, with explicit instructions not to edit `docs/sources.md` directly (to avoid file-write races). Each sub-agent returned proposed status-line annotations, report-table rows, and writer hand-back blocks; the orchestrator merged them centrally into `docs/sources.md`, this report, and `docs/handbacks/source-analyzer-to-writer.md`.

A consequence of this dispatch pattern is that several full-text retrievals in this slice failed with HTTP 403 against the same set of academic-PDF mirrors (NDSS, arXiv, IEEE Xplore, SemanticScholar, ResearchGate). This is a harness-level constraint, not a per-paper signal. Re-running individual entries from a different network (or routing through an institutional proxy) is the recommended remediation. Five `[edge-case]` flags are *not* about the papers' quality — they are split between (a) the load-bearing-cornerstone rule (which by design preserves `[lit-retrieved]` until a human reads, regardless of fetch success) and (b) fetch-failure compounding the load-bearing flag.

## Files updated

- `docs/sources.md` — 10 entries' status lines updated (4 `[ai-confirmed]`, 5 `[edge-case]`, 1 `[ai-confirmed-attempt-failed]`).
- `docs/handbacks/source-analyzer-report.md` — this file (new).
- `docs/handbacks/source-analyzer-to-writer.md` — new, four upgraded entries delivered to the writer.
- `docs/logbook.md` — session entry appended.

Files left untouched (per scope discipline): `paper/main.md`, `paper/main.tex`, `paper/references.bib`, all figure assets, all scrutinizer registries.

## Re-analysis verdict

**`RE-ANALYSIS REQUIRED: yes`** — five critical-path entries (L-VD-1, L-VD-5, L-HC-1, L-HC-6, L-BLE-5) and one fetch-failed entry (L-RE-2) remain at `[lit-retrieved]` with `[edge-case]` or `[ai-confirmed-attempt-failed]` annotations and require either (a) human `[lit-read]` confirmation or (b) re-retrieval from an alternative network. The 119 unprocessed `[lit-retrieved]` entries in `docs/sources.md` also remain in scope for subsequent Source Analyzer passes.
