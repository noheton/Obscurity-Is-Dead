# Todos for publication readiness

Live tracker for the steps that take this repository from
"layout + readability scrutinizers closed against tip `644d2e2`"
(2026-05-04) to "public-mirror-ready, Zenodo-deposited, arXiv-submitted".
Each row resolves to one of: `open`, `in-progress`, `done`, or
`deferred-on-human`.

The pipeline pass that produced the current publication-ready state is
preserved in the change log at the bottom of this file (entries from
2026-05-04). Everything above the change log describes the **forward
work** still required before the rule-13 / rule-14 distribution gates
can be released.

## Snapshot (2026-05-04, second pass)

| | |
|---|---|
| Working tree | clean on `claude/final-doc-update-R46EQ` after figure-data sync; long-form `paper/main.{md,tex}` unmodified |
| Layout scrutinizer (Stage 4) | `RE-SCRUTINY REQUIRED: no` against tip `644d2e2` (long-form + condensed) |
| Readability scrutinizer (Stage 5) | `RE-SCRUTINY REQUIRED: no` against tip `644d2e2` (long-form + condensed) |
| Aligner (Stage 6) | `ALN-01..ALN-13` closed (commit `668fa8d`); next pass triggered by any further writer / illustrator change |
| History rewrite | executed; tag `pre-publication-clean` |
| Public-mirror push, Zenodo, arXiv | gated on rule-13 + rule-14 explicit consent |

## Open items before public-mirror push (rule-14 gate)

Items the author must approve and the agent pipeline must execute (or
verify) before the project is moved to a public remote, deposited on
Zenodo, or submitted to arXiv. Order is approximately the order in
which they should be tackled.

| # | Item | Owner | Status | Notes |
|---|------|-------|--------|-------|
| Q1 | Refresh `[lit-retrieved] / [ai-confirmed] / [lit-read]` counts in §5.7 *Other KPIs* | writer (Stage 2) | open | Current §5.7 line cites "~70 across clusters A–K" with an explicit `as of 2026-05-01` anchor. The actual `docs/sources.md` state is 19 clusters (A through Q, plus A.2/A.3) and ~144 `L-` entries with ~140 already `[ai-confirmed]` and 18 `[lit-read]`. Add a second snapshot row anchored to `2026-05-04` so the historical claim and the pre-publication state both stand on the record (rule 1). Mirror in `paper/main.tex:1318–1319` (rule 12). |
| Q2 | Refresh "clusters A–J" range references in §8.5 and §9.3 | writer (Stage 2) | open | `paper/main.md:688` and `paper/main.md:713` still say "clusters A–J"; the register now extends to cluster Q. Update to "clusters A–Q" and mirror in `paper/main.tex:2752` and `paper/main.tex:2901`. |
| Q3 | Optional new figure: literature-verification distribution | illustrator (Stage 3) | deferred | Opportunity surfaced 2026-05-04: a stacked-bar / heat-map fig17 showing `[lit-retrieved]` → `[ai-confirmed]` → `[lit-read]` counts per cluster (A–Q). Would visualise the methodology's *applied* discipline alongside fig9 (the *abstract* ladder). Defer until Q1 closes — fig17 should read off the same refreshed numbers. |
| Q4 | Vendored zip carve-out decision (Spider Farmer) | human | open | Drop or caveat the three Spider Farmer vendored archives at the public-mirror cut-over. Decision recorded in `docs/redaction-policy.md`; execution still required. |
| Q5 | Upstream `noheton/spider_farmer` redaction pass | human + agent | open | Run the same H-* catalogue against the upstream before it is made public. Out of scope for this repo's pass. |
| Q6 | Upstream `noheton/powerocean-dev` redaction pass | human + agent | open | Same as Q5. The upstream `DISCLAIMER.md` and `doc/README.md` (2026-05-03) reduce but do not eliminate the pre-rewrite history exposure. |
| Q7 | R-AUDIT-12 client-secret literal grep | human | open | Confirm against the actual Cognito secret string fragment that the redaction marker substitution is exhaustive. |
| Q8 | Logbook readability re-check after in-place redaction | scrutinizer (Stage 5) | open | High marker density was introduced by the redaction-execution pass; surface in the next readability pass. |
| Q9 | Final aligner sweep | aligner (Stage 6) | open | Trigger after Q1 + Q2 land. Audit md ↔ tex parity for both the long-form and the condensed pair (rule 12 / rule 17), the verification-status updates, and the figure-data sync committed by this pass. |
| Q10 | `make all` clean rebuild + page-count snapshot | build | open | Confirm `paper/main.pdf` (target ≤60 pp post-rewrite) and `paper/main-condensed.pdf` (≤10 pp ceiling) after Q1–Q9 close. Record the PDF SHAs in the rule-14 gate handoff. |
| Q11 | Pandora-jar-intact final asset (Gemini) | human | open | Replace the typographic placeholder at `paper/figures/logo-pandora-jar-intact.png` with the second Gemini deliverable when supplied. Until then the placeholder is visible in the rendered PDF (rule 1). |

## Rule-13 + rule-14 gate (separate explicit consent required)

Before any of the following, surface a one-line plain-language
description and wait for the human author's explicit written consent:

- Public-mirror push to a new clean repository.
- Zenodo deposit.
- arXiv submission (`make arxiv`).
- Any externally visible link to the rendered PDF.

The build pipeline produces local artifacts only.

## Closed pipeline pass (preserved for history)

The 2026-05-04 layout / readability / aligner pass closed the
publication-readiness scrutinizer track against tip `644d2e2`:

- Stage 4 (layout) — `RE-SCRUTINY REQUIRED: no`. All round-1 H + M
  defects closed (LAY-32, LAY-31, LAY-10/-29 dispatched anchors).
  No new H/M defects introduced. Hand-back at
  `docs/handbacks/layout-scrutiny-2026-05-04-post-rewrite-r2.md`.
- Stage 5 (readability) — `RE-SCRUTINY REQUIRED: no`. All round-1
  H + M defects closed (RDB-37 §4.6 four-sentence split; RDB-39
  §5.6 three-sentence split; RDB-40 README five-row table → four
  rows + footnote). Anti-pattern flag honoured. Hand-back at
  `docs/handbacks/readability-scrutiny-2026-05-04-post-rewrite-r2.md`.
- Stage 6 (aligner) — `ALN-01..ALN-13` closed by commit `668fa8d`
  (rule-number normalisation, instruction-stub invariant, both PDFs
  as CI artifacts).
- Condensed paper (rule 17) — 8 pp build, well under the 10 pp
  ceiling; reuses fig1 / fig5 / fig11 only.

The standing carry-over M/L backlog (RDB-01 / -03..-11 / -26
prose-cluster; LAY-02/-24 / -06 / -08 / -09/-25 / -22
path-literal-cluster) predates this loop, was never load-bearing
for any round-1 brief, and is appropriate for a future polish pass
rather than for blocking publication.

## Change log

- 2026-05-04 — file created on branch `claude/history-rewrite-daDxQ`
  immediately after the history rewrite + integration commits.
- 2026-05-04 — P1..P6 all flipped to `done` (closed for publication
  readiness); Stage 4 + Stage 5 round-2 verdicts both
  `RE-SCRUTINY REQUIRED: no`; condensed paper at 8 pp.
- 2026-05-04 (second pass, branch `claude/final-doc-update-R46EQ`) —
  figure-data accuracy fix: `paper/figures/data/effort-gap.csv` had
  fallen behind §5.7 by two phases (DLR design + Democratisation §10);
  CSV updated to add the missing rows so the cumulative meta-process
  track terminates at 17.5 h matching the §5.7 KPI table; fig1 panel
  B hardcoded values corrected (5 % → 6 %, 15.5 h → 17.5 h) so the
  figure now reproduces the §5.7 / README / condensed-paper headline
  KPI; `fig.patch.set_facecolor("white")` added to fig1 to match the
  CI white-background convention used by fig7/fig9/fig10/fig11/fig14;
  all 12 programmatic figures re-executed for reproducibility (no
  substantive content drift, only matplotlib hash-ID + timestamp
  refresh). Open todos Q1..Q11 above are the remaining work before
  the rule-13 / rule-14 distribution gates can be released.
