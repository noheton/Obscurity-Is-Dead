# Layout Scrutinizer — Hand-back to Illustration Agent

Source: `docs/handbacks/layout-defect-registry.md` (PDF SHA-256
`62e68f6a5208814d47a51a8124bc7c7a836e7c9f3104951bc40a5c8dfda81384`,
build 2026-05-02T19:44:30Z, 42 pages, rebuilt by writer pass `537fae2`).

This is the **second** Layout Scrutinizer pass. Each block below is one
defect routed to the illustration agent. Re-export the affected figure
asset(s) and rebuild via `make -C paper pdf`; do **not** invoke
`make arxiv` (CLAUDE.md rule 13).

---

## Disposition of LAY-01..LAY-18 (illustrator-owned)

## LAY-05 — Figure 7 (verification-status pipeline) 226.22pt overfull
- **[RESOLVED]**.
- Verified: log shows zero `Overfull \hbox` warnings in the figure
  float environment at `main.tex:814–828`. The 226.22pt overfull that
  previously dominated the geometric-defect picture for this figure
  is gone in the rebuilt PDF.
- A separate 226.22pt overfull now appears at `main.tex:872–891`,
  but that is the writer-owned KPI tabular (LAY-19), **not** Figure 7.
  No illustrator action required.
- Page: 14 (was 14 in the prior pass)
- Source: `main.tex:814–828` (was `:805–827`)
- Asset: `paper/figures/fig9-verification-pipeline.pdf` /
  `paper/figures/fig9-verification-pipeline.py`
- Severity: H → 0 (closed)

## LAY-06 — Figure 8 / `tab:difficulty-taxonomy` heat-map row split
- **[PARTIAL → M]**.
- Verified: the heat-map row split (`Med High` wrapping onto the
  EcoFlow row in the prior pass) is no longer evidenced by the log
  warnings, and the figure is included at 0.92\linewidth.
- Residuals from the log: 8.80pt overfull at lines 1136–1137 (the
  "Composite" header row of the *table* `tab:difficulty-taxonomy`
  that precedes the figure include); 2.53pt overfull at 1134–1160
  (the whole tabular). These are column-width pressure on the
  Composite header. Owner could be either writer (table re-author)
  or illustrator (figure caption / panel re-render).
- Page: 19
- Source: `main.tex:1132–1184`
- Asset: `paper/figures/fig12-difficulty-taxonomy.pdf` /
  `paper/figures/fig12-difficulty-taxonomy.py`
- Severity: H → M
- Required action: either re-render the heat-map figure with the
  Composite column moved to a side sub-panel (reduces table width
  pressure on the header row), or hand back to the writer to widen
  the `Composite` `p{1.4cm}` column to `p{1.8cm}` and shorten the
  preceding columns proportionally.

## LAY-12 — Logo placeholders
- **[DEFERRED — by design]**.
- Per logbook 2026-05-02, the shattered-jar logo
  (`logo-obscurity-is-dead.png`) is now the final Gemini artwork; only
  the intact-jar companion (`logo-pandora-jar-intact.png`) remains an
  AI-authored placeholder pending the second Gemini deliverable. Prose
  at `main.tex:2138–2149` declares this explicitly per rule 1, so the
  placeholder presence is honest, not a defect.
- Tracking entry only; **do not edit `logo-placeholders.py`.** Replace
  `logo-pandora-jar-intact.png` once the Gemini deliverable arrives,
  and the Layout Scrutinizer will re-run against the final asset.
- Page: ~38–40 (was 36–38)
- Source: `main.tex:2138–2145, :2313`
- Severity: M (informational)

## LAY-13 — PDF version 1.7 vs 1.5 inclusion warnings
- **[PARTIAL — UNCHANGED → escalating count]**.
- Verified: log still reports `pdfTeX warning: PDF inclusion: found PDF
  version <1.7>, but at most version <1.5> allowed` for these figures,
  and the warning count has grown from 2 to 7 (`fig1-effort-gap.pdf`,
  `fig2-boredom-barrier.pdf`, `fig3-spider-farmer.pdf`,
  `fig4-ecoflow.pdf`, `fig5-methodology.pdf`,
  `fig6-dual-use.pdf`, `fig7-threat-models.pdf`).
- No reader-visible defect today; an arXiv-strict pdfTeX may eventually
  downgrade or reject these floats.
- Page: ~7, ~9, ~11, ~13, ~15, ~22, ~23
- Source: `main.tex:1399`, `:1406` (and the includes for fig1–fig5
  earlier in the document)
- Required action: re-export each of the 7 PDFs from the source SVG /
  matplotlib at PDF compatibility level 1.5
  (`gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -o out.pdf in.pdf`,
  or set explicit PDF-1.5 metadata in the `savefig` call where
  matplotlib supports it).
- Severity: M (unchanged)

## LAY-16 — Bibliography underfull rivers
- **[PARTIAL — UNCHANGED]**.
- ~25 Underfull `\hbox` warnings in `main.bbl`. Auto-generated from
  `references.bib`; same long-URL root cause. New bib entries added by
  writer pass `537fae2` (`papp2015embedded`,
  `vasile2018breakingallthethings`, `becker2020hwreexploratory`,
  `botero2021hwretutorial`, `grand2013jtagulator`) do not appear to have
  introduced fresh underfulls beyond the baseline.
- Page: 41–42 (was 39–40)
- Source: `main.bbl` (auto-generated)
- Required action: practical fix is to ensure long URLs in
  `references.bib` are wrapped in `\url{}` (already done partially);
  add a `BREAK` directive or `\seqsplit` for vendored-archive paths.
  Advisory-only; defer or batch with the next writer pass.
- Severity: L

---

## NEW illustrator-owned defects

None this pass. All four new defects (LAY-19..LAY-22) are writer-owned
(KPI tabular column-definition pattern + path-wrapping + citation-pack
density). The illustration assets did not regress between commits
`f3ce051` / `537fae2` and the prior PDF.

---

## Summary

- **Open illustrator-owned defects:** 3 (LAY-06 [partial → M],
  LAY-13 [partial → M], LAY-16 [partial → L]).
- **Closed:** 1 (LAY-05).
- **Deferred — by design:** 1 (LAY-12; placeholder pending Gemini).
- **No new defects** introduced by writer commits `f3ce051` / `537fae2`
  in the figure-asset layer.
