# Layout Scrutiny — 2026-05-03 build

- **PDF:** `paper/main.pdf`, 1,151,391 bytes, 46 pages, built 2026-05-03 07:56 UTC
  (newer than `paper/main.tex` at 07:53 UTC).
- **LaTeX log:** `paper/main.log` (1,357 lines).
- **BibTeX log:** `paper/main.blg` — 4 warnings.
- **Scrutinizer:** Stage 4 — Layout Scrutinizer.
- **Method note:** PDF viewer (`mcp__…__list_pdfs`) not exercised this pass;
  scrutiny is log-driven (pdfTeX `Overfull`/`Underfull` measurements + bibtex
  warnings) and source-cross-checked against `paper/main.tex` and
  `paper/references.bib`. Pixel-level visual sweep remains queued.

## Honesty / Rule 1 reconciliation with the dispatch brief

The orchestrator brief that triggered this pass listed three large defect
classes drawn from a *prior* build state:

1. ~30+ undefined `\ref` targets (sec:independence, sec:sf-kpis, sec:ef-kpis,
   sec:synthesis-evidence-asymmetry, sec:case-spider-farmer, sec:case-ecoflow,
   sec:pandora, fig:eight-practices, fig:dual-use, fig:threat-models, …).
2. ~15 undefined citation keys (vasile2018breakingallthethings,
   becker2020hwreexploratory, botero2021hwretutorial, grand2013jtagulator,
   dfg2023, smurfy_esphome_sf, p0rigth_spiderblebridge,
   pythonspidercontroller, niltrip_powerocean, basque2026synergy,
   peng2023copilot, cui2025genai, metr2025productivity, papp2015embedded,
   anthropic2026claude).
3. Dozens of overfull/underfull hboxes around long monospace tokens, paths,
   `[REDACTED:…]` markers, and several wide tables.

Re-checking the *current* `paper/main.log` (the one rebuilt at 07:56 UTC and
named in the brief) against these three classes:

- **Class A — undefined `\ref` / `\cref` / `\label`:** **0 occurrences.**
  `grep -niE 'undefined|reference.*undefined|missing|^!|\?\?' paper/main.log`
  returns no rows. Spot-check of the 10 highest-impact labels named in the
  brief confirms all are defined in `main.tex`:
  `sec:case-spider-farmer` (line 434), `sec:sf-kpis` (578),
  `sec:case-ecoflow` (636), `sec:ef-kpis` (751),
  `sec:synthesis-evidence-asymmetry` (1389), `fig:dual-use` (1515),
  `fig:threat-models` (1522), `sec:independence` (2419),
  `sec:pandora` (2489), `fig:eight-practices` (2593).
- **Class B — undefined citations:** **0 `Citation … undefined` warnings.**
  `paper/main.blg` reports only four BibTeX warnings, all `Warning--empty
  year in …`, against keys that *are* present in `references.bib` and *are*
  cited from `main.tex` (verified — see Class B below). The 11 other keys
  named in the brief (`vasile2018breakingallthethings`, `becker2020…`,
  `botero2021…`, `grand2013jtagulator`, `dfg2023`, `basque2026synergy`,
  `peng2023copilot`, `cui2025genai`, `metr2025productivity`,
  `papp2015embedded`, `anthropic2026claude`) are not flagged by the current
  build.
- **Class C — overfull/underfull hboxes:** **97 lines** match
  `Overfull|Underfull` in `paper/main.log` (33 Overfull + 64 Underfull, by
  manual count of the trailing batch). These are real and itemised below.

**Disposition:** Per CLAUDE.md rule 1 (strict honesty) this pass declines to
fabricate (A) and (B) entries against a build that does not exhibit them.
Either the brief was assembled from a stale log, or an intervening rebuild
between `references.bib`/`main.tex` updates and the 07:56 UTC build resolved
them. Should the orchestrator wish to verify the brief's seed log, the
artefact path is required; otherwise treat (A) and (B) as **resolved upstream
of this scrutiny** and proceed to (C).

## (A) Missing labels

**No defects.** All `\ref`/`\cref` calls in the current build resolve. No
hand-back to writer required for this class.

## (B) Missing / mismatched bib keys

**No `Citation … undefined` warnings.** Four soft BibTeX warnings remain,
all of the same shape (`Warning--empty year in <key>`). These do not
suppress citation rendering but do produce parenthetical `(?)` years in the
printed reference list, which is a citation-quality defect under rule 2
(origin of findings).

| ID     | Bib key                  | Bib line | Cited from                                                | Required action                                                           | Severity |
|--------|--------------------------|----------|-----------------------------------------------------------|---------------------------------------------------------------------------|----------|
| BIB-01 | `smurfy_esphome_sf`      | bib:1    | `main.tex:450, 474, 1049`                                 | Add `year = {YYYY}` (best-effort from upstream commit history of the repo). | M        |
| BIB-02 | `p0rigth_spiderblebridge`| bib:20   | `main.tex:451, 474, 1049`                                 | Add `year = {YYYY}` from upstream README / first-commit date.             | M        |
| BIB-03 | `pythonspidercontroller` | bib:31   | `main.tex:452, 474, 1049`                                 | Add `year = {YYYY}` from upstream commit history.                         | M        |
| BIB-04 | `niltrip_powerocean`     | bib:40   | `main.tex:663, 1050`                                      | Add `year = {YYYY}` from upstream commit history.                         | M        |

Hand-back: writer (the `references.bib` is the writer's territory under
rule 11 mirror discipline). All four are `@misc` community-software entries
where year can be sourced from the repo metadata; no library access needed.

## (C) Overfull / underfull hboxes

Grouped by root cause. Each row aggregates the log lines it covers; the
"Fix" column gives one suggested remediation per group, applied at all
listed source spans.

| ID     | Cause group                                       | Source spans (`main.tex`)                                                                                                                                                       | Worst overflow | Owner  | Suggested fix                                                                                                                                                                                                                                | Severity |
|--------|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| OVF-01 | Long file/repo paths in `\texttt{}` body text     | 302–306, 306–311, 447–449, 478–481, 712–716, 819–829, 829–834, 834–837, 837–839, 841–846 (×2), 863–868, 878–881, 899–904, 1167–1182, 2231–2242, 2243–2265, 2328–2332, 2476–2486, 2538–2546, 2551–2556, 2574–2579 | 168.71 pt (l. 2231–2242) | writer | Wrap every body-text path in `\path{...}` (from `url` package; already loaded via `hyperref`) **or** keep `\texttt{...}` and apply `\seqsplit{...}` to enable intra-token line breaks. The slash-padding hack `experiments / paper-meta-process / …` currently in the source (visible in the log as `experiments / paper-[]meta-[]process /`) should be removed once `\seqsplit` is in place. | H        |
| OVF-02 | `[REDACTED:…]` token cannot break                 | 1199–1200, 1201–1202, 1214–1215, 1882–1891                                                                                                                                       | 30.26 pt       | writer | Wrap every `[REDACTED:type:id]` marker with `\seqsplit{\texttt{[REDACTED:type:id]}}` (the colon-separated-token convention from `docs/redaction-policy.md`). Cluster fix; do not alter the marker text itself.                              | M        |
| OVF-03 | Wide `tabularx`/`tabular` tables                  | 547 (Spider Farmer KPI block, 3 over­fulls of 9.4–15.0 pt), 757–768 (113.47 pt), 986–1005 (226.22 pt), 1248–1274 (Difficulty taxonomy, 2.53 pt), 1882–1891 (25.75 pt)                          | 226.22 pt (l. 986–1005) | writer | Convert all four tables to `tabularx` with one `>{\raggedright\arraybackslash}X` column for the widest text cell; keep narrow numeric/label columns as `l` or `p{1.4cm}`. The Difficulty-taxonomy table at l. 1248 already uses `p{}`; widen the `Composite` column from `1.4cm` to `1.7cm` and reduce `Crypto barrier` from `3.3cm` to `3.1cm`. | H        |
| OVF-04 | Inline math with long underscored identifiers     | 712–716 (`POST /iot-devices/device/setDeviceProperty`), 719–725 (`backup_reserve_soc`, `number.fast_chg_max_soc`), 829–834 (`experiments / paper-meta-process / REPORT.md`)        | 70.84 pt       | writer | Move the route/identifier out of math mode (`$\texttt{…}$` → `\path{…}`); the `_` characters are forcing `_`-as-subscript spacing in math mode and the `/` characters are unbreakable in math mode.                                          | M        |
| OVF-05 | Float / display content too wide (caption-driven) | 584–599, 757–768 (figure body), 986–1005 (figure body), 1248–1274                                                                                                                | 226.22 pt      | writer | If OVF-03 alone does not close these, add `\small` inside the float and re-flow the caption to ≤ 2 lines; consider `[!htbp]` placement.                                                                                                       | M        |
| OVF-06 | Bibliography URL (no defect this build)           | —                                                                                                                                                                                | —              | —      | Spot-checked the JTAGulator entry referenced in the brief; not present in `references.bib` and no bib-side overfull was logged. No action.                                                                                                   | —        |
| UNF-01 | Underfull `\hbox` clusters in figure-caption / footnote paragraphs | 1041–1066, 1192–1215, 1254–1271, log block 1175–1316 (caption / footnote bodies in `main.md`-rendered preamble of cited blocks)                              | badness 10000  | writer | Cosmetic. Fix only as a side-effect of the OVF-01/02 path-wrapping pass, which restores normal interword spacing in the affected paragraphs.                                                                                                  | L        |

Counts: **(C)** 33 Overfull \hbox + 64 Underfull \hbox = **97** raw log
events, collapsed into **6** action groups.

## Top-3 highest-impact fixes

1. **OVF-03 — `tabularx` conversion of the four wide tables.** Closes the
   single largest overflow in the build (226.22 pt at l. 986–1005, the
   Meta-process KPI table) and three same-family overflows. One pass.
2. **OVF-01 — `\path{}` / `\seqsplit{}` wrap for body-text repo paths.**
   Closes ≥ 22 of the 33 Overfull events. The slash-padding hack
   (`a / b / c`) currently scattered through §6.x and §10 should be
   removed in the same edit.
3. **BIB-01..04 — populate `year` in the four community-software `@misc`
   entries.** Restores the citation-quality contract under rule 2 and
   silences all remaining BibTeX warnings; the data is recoverable from
   each repo's first-commit timestamp.

## Hand-back routing

- **Writer:** OVF-01, OVF-02, OVF-03, OVF-04, OVF-05, BIB-01..04. Append
  to `docs/handbacks/layout-to-writer.md` on next consolidation.
- **Illustrator:** none (no figure-asset defects identified this pass; pixel
  sweep queued).
- **Joint:** none.

## Mirror discipline (rule 11)

All OVF-* spans are in `main.tex`; mirror lines in `main.md` must be
updated in the same writer commit. The §6 / §10 path bullets correspond to
the `## Case studies` and `## Methodology and reproducibility` blocks of
`paper/main.md`; the writer should locate by heading rather than by line
number to avoid drift.

## Redaction (rule 12) check

Four `[REDACTED:repo-path:…]` markers appear as overfull tokens (OVF-02);
the redaction *content* is intact and policy-compliant. No live credential,
serial number, or private UID was rendered in the PDF.

## Rule 13 compliance

Local PDF only. `make arxiv` was NOT invoked.

## RE-SCRUTINY REQUIRED: yes

Rationale: OVF-03 (H, 226.22 pt overflow at l. 986–1005) and OVF-01 (H,
168.71 pt overflow at l. 2231–2242) are still present in the rendered PDF
and prevent a clean reading of headline KPIs and §10 path bullets. Re-run
Stage 4 after the writer pass + `make -C paper pdf`.
