# Layout Defect Registry — paper/main.pdf

- **PDF SHA-256:** `62e68f6a5208814d47a51a8124bc7c7a836e7c9f3104951bc40a5c8dfda81384`
- **PDF size:** 1,211,008 bytes; **42 pages** (was 40 pages in the prior pass)
- **Build timestamp:** rebuilt 2026-05-02T19:44:30Z by writer pass `537fae2`
  (`make -C paper pdf`, latexmk + pdfTeX 1.40.25). Newer than `paper/main.tex`
  (timestamp 2026-05-02T19:44:21Z) and `paper/main.md` (19:43:58Z).
- **Source under inspection:** `paper/main.tex` (2,519 lines), mirrored in
  `paper/main.md` (660 lines).
- **LaTeX log:** `paper/main.log` (1,313 lines; 33 `Overfull \hbox`,
  ~55 `Underfull \hbox`, 7 `pdfTeX warning: PDF version <1.7>` notices,
  one `Font shape T1/lmtt/bx/n not available` substitution warning,
  three `'h' float specifier changed to 'ht'` notices). **No `??` /
  `Reference … undefined` / `Citation … undefined` warnings** — the four
  new `\citep{}` calls (vasile, becker, botero, grand jtagulator) and the
  Papp 2015 inline citation in §6.8 all resolve cleanly, as does
  `\cref{sec:synthesis-evidence-asymmetry}` and the named-footnote reuse
  `\textsuperscript{\ref{fn:hwre-cluster}}`.
- **Scrutinizer:** Stage 4 — Layout Scrutinizer, 2026-05-02 (re-run after
  cluster A.2 + §6.8, commits `f3ce051` + `537fae2`).
- **Race-condition note:** while this scrutiny was in progress, a third
  writer commit `a104fa3` (`paper: add 2-page Executive Summary between
  abstract and §1`) landed on the branch, inserting +90 lines into
  `main.tex` (and a corresponding mirror into `main.md`) and rebuilding
  the local `paper/main.pdf` to a new SHA-256 `aa89604fdc616073e7bdd70ce
  858bea5090370eb3ab1aa23ad5afb44d66885ff`. The defect entries below are
  anchored on the **prior** PDF SHA `62e68f6a…` and the **prior**
  `main.tex` line numbering (2,519 lines). After Executive-Summary
  insertion all `main.tex` line ranges below shift by approximately
  +90 lines for every span past the new §0 block. The semantic content
  of every defect remains valid; only the line numbers move. A
  follow-up Stage 4 re-run against the post-`a104fa3` PDF is
  recommended (verdict updated below).
- **Method note:** the bundled PDF viewer again rejected the local path
  (`list_pdfs` returned `allowedDirectories: []`). Visual sweep performed
  via the LaTeX build log (geometric-overflow ground truth: pdfTeX's own
  `Overfull \hbox` measurements name source line ranges, which were
  cross-checked against `paper/main.tex` after the writer's two-commit
  insertion shifted line numbers by ~150 lines). Pages requiring
  pixel-level inspection (figure-internal contrast, kerning of new
  inline-cite renderings, footnote glyph cleanliness) carry a
  `viewer-blocked` note; a pixel-level re-sweep remains queued.

## Source-line shift since the prior pass

Two writer commits between the prior pass and this re-run inserted ~128
net lines into `paper/main.tex`:
- `f3ce051` — §1.4 cluster A.2 paragraph (lines 165–208) + new §6.8
  subsection at `\label{sec:synthesis-evidence-asymmetry}` (lines 1274–1326).
- `537fae2` — inline-citation promotions (lines 190, 194, 201, 204, 1288,
  1291, 1294, 1298, 1302); narrowed `fn:hwre-cluster` footnote
  (lines 177–187); `\fp{...}`→`\texttt{...}` fix in Figure 13 caption.

Old defect line ranges therefore read against the prior `main.tex`; new
line ranges in this registry read against the rebuilt `main.tex` at
2,519 lines. Where the prior registry's source span has moved without
otherwise changing, the new line range is given alongside the disposition.

## Defects (LAY-01..LAY-18 dispositions; LAY-19..LAY-22 new)

| ID | Page | Region | Defect class | Severity | Owner | Source span (current) | Disposition / Suggested fix |
|----|------|--------|--------------|----------|-------|-----------------------|-----------------------------|
| LAY-01 | 31 (was 31) | mid-page, §7.15 first paragraph | broken-cref (`??`) | H | writer | `main.tex:1972` (was `:1853`); mirrored at `main.md:545–547` | **[RESOLVED].** Labels `sec:scope-non-goals` (`main.tex:242`), `sec:synthesis-limits` (`:989`), `sec:disc-validity` (`:1534`) are all present. Log shows zero `??` / undefined-reference warnings. Path (a) was applied: `\label{sec:scope-non-goals}` adjacent to `\label{sec:scope}`, and `\label{sec:disc-validity}` adjacent to `\label{sec:disc-threats}`. |
| LAY-02 | ~7 | reconciliation table inside §3.4 | table-overflow + cell-wrap-misalignment | H→M | writer | `main.tex:419–457` (was `:373–393`); mirrored at `main.md:118–141` | **[PARTIAL].** Table is now `\scriptsize` and uses `\newline` to break the LED/PS-10 fingerprints inside their cells, which removes the cross-row visual misalignment that previously bled the trailing `00` into a neighbour column. Log retains 4 small overfulls in the table region (66.39pt at 388–391 prose preface; three at line 457, range 9.4–15.0pt). Severity drops from H to M; remaining work is cosmetic column-width pressure on the bottom rule. |
| LAY-03 | 12 | upper half, bullet list under §5.2 | margin-overflow | H→M | writer | `main.tex:705–732` (was `:641–651`); mirrored at `main.md:253–264` | **[PARTIAL].** Long `\texttt{...}` runs were converted to `\fp{...}` (path-aware breaking). Worst-case overflow dropped from 168.80pt to 70.84pt at lines 705–715, with three further mid-range overfulls (69.91pt at 720–723; 56.22pt at 727–732; 28.89pt at 727–732). Cause now: residual non-path `\texttt{}` content (paths inside parenthetical asides). Severity H→M; final clean-up is a one-line wrapping pass on the survivors. |
| LAY-04 | ~17 | mid-page, bullet list under §6.5 | margin-overflow | H→M | writer | `main.tex:1053–1068` (was `:989–1004`); mirrored at `main.md:359–373` | **[PARTIAL].** Log shows 0.18pt residual overfull at lines 1053–1068 and 52.64pt at 1087–1088. The 46pt overflow seen previously at the T-OND/T-BAL identifier list is gone; the residual 52.64pt is in the surrounding paragraph. Severity H→M. |
| LAY-05 | 14 | full-page float, Figure 7 (verification-status pipeline) | float-overflow | H | illustrator | `main.tex:814–828` (was `:805–827`); asset `paper/figures/fig9-verification-pipeline.pdf` | **[RESOLVED].** Log shows zero `Overfull \hbox` in the lines 814–828 range. The 226.22pt overflow that previously dominated the geometric-defect picture is gone. (Note: a separate 226.22pt overfull now appears at lines 872–891, but that is the `Meta-process KPI summary` `\begin{tabular}` — see new LAY-19 below — *not* the figure float.) |
| LAY-06 | 19 | upper-third, scoring sub-table inside Figure 8 / `tab:difficulty-taxonomy` | table-overflow inside float | H→M | illustrator | `main.tex:1132–1184` table+figure pair (was `:1070–1096`); script `paper/figures/fig12-difficulty-taxonomy.py` | **[PARTIAL].** Log retains two small overfulls in the difficulty-taxonomy table (8.80pt at 1136–1137 = "Composite" header row; 2.53pt at 1134–1160 = whole tabular). The previous heat-map row split ("Med High wraps onto EcoFlow row") is no longer evidenced by the log warnings, and the figure is now included at 0.92\linewidth. Severity drops H→M. Final clean-up is column-width pressure on the "Composite" header. |
| LAY-07 | 7 | redaction tags inline | redaction-rendering | M→L | writer | `main.tex:481–482` (was `:412–422`); mirrored at `main.md:145–148` | **[PARTIAL].** Both `[REDACTED:username:S-SF-5-username]` and `[REDACTED:credential:S-SF-5-password]` are now wrapped in `\seqsplit{\texttt{...}}`, which permits hyphenation inside the redaction tag. Log no longer reports overfulls anchored on the redaction tags; the prior 40.73pt and 55.48pt overflows are gone. Markers remain literal (rule 12 satisfied). Severity drops to L. |
| LAY-08 | 9 | mid-page bullet under §4.4 | margin-overflow | M→L | writer | `main.tex:598–611` (was `:534–547`); mirrored at `main.md:201–206` | **[PARTIAL].** Two residual overfulls: 66.67pt at 598–602 and 12.76pt at 605–611. Down from four (17.98 / 102.57 / 105.99 / 6.24pt). Severity drops to L; remaining work is wrapping the writeable-entity comma list. |
| LAY-09 | 11 | bullet block §5.2 | margin-overflow (multi-paragraph) | M | writer | `main.tex:705–767` (was `:639–680`); mirrored at `main.md:253–272` | **[PARTIAL].** Same root cause as LAY-03; partial conversion to `\fp{...}` reduced the cluster from ~11 overfulls (4.85–168.80pt) to ~8 overfulls (5.21–113.47pt at lines 643–767). The 113.47pt warning at 643–654 is the EcoFlow KPI tabular (see LAY-17). The remaining bullet-block overflows survive at 28.89–70.84pt. Tied to LAY-03; closing LAY-03 closes LAY-09. |
| LAY-10 | 35 (now ~37) | top, §10 numbered list of eight practices | margin-overflow | M | writer | `main.tex:2098–2150` (was `:1979–2028`); mirrored at `main.md:613–625` | **[PARTIAL].** Three residual overfulls: 50.18pt at 2098–2101; 168.71pt at 2116–2127 (worst single overfull surviving in the document); 35.69pt at 2128–2150. Cause unchanged: the `experiments/paper-meta-process/raw_conversations (copy&paste, web)/T1-paper-structure-and-literature.md` path has not yet been wrapped. Same fix-shape as LAY-03/-09. |
| LAY-11 | 32 (now ~34) | bottom of preceding page | margin-overflow | L→L | writer | `main.tex:1136–1137` ("Composite" header row of `tab:difficulty-taxonomy`; was at `:1138–1144` "Cognito refresh tokens" line); mirrored at `main.md` §6.6 region | **[REGRESSED-INTERPRETATION].** The original 7.79pt overfull at "RESEARCH-PROTOCOL.md" appears resolved (the `\fp{}` macro fix in commit `537fae2` removed an undefined-control-sequence-in-caption). The 8.80pt overfull at lines 1136–1137 is now the difficulty-taxonomy table header (LAY-06's header row); LAY-11's identity therefore folds into LAY-06. Disposition: **[RESOLVED at original site; log warning re-attached to LAY-06]**. |
| LAY-12 | 36–38 (now ~38–40) | front matter of §10 illustrations | placeholder-pending | M | illustrator | `main.tex:2138–2145, :2313` (was `:2009–2028, :2191`); script `paper/figures/logo-placeholders.py` | **[PARTIALLY RESOLVED 2026-05-03 — intact-jar half OPEN].** Shattered-jar half closed: `logo-obscurity-is-dead.png` re-encoded in place (1408x768 preserved, no crop, ~1.63 MB) and wired into `README.md` as the centred hero with Gemini provenance disclosed in alt-text per rule 1 (commits `7e1f297`, `062b1d3`); narrow-scope Stage 4/5 scrutiny `RE-SCRUTINY REQUIRED: no`. Intact-jar half still deferred — `logo-pandora-jar-intact.png` remains the AI-authored placeholder pending the second Gemini deliverable. Prose at lines 2138–2149 declares the placeholder state explicitly per rule 1, so its presence is honest, not a defect. Tracking entry only; do not edit `logo-placeholders.py`. |
| LAY-13 | ~22, ~23 | full-width figures (Figure 11 dual-use, Figure 12 threat-models) | pdf-version-incompatibility | M | illustrator | `main.tex:1399, :1406` (was `:1281, :1288`); assets `paper/figures/fig6-dual-use.pdf`, `paper/figures/fig7-threat-models.pdf` | **[PARTIAL — UNCHANGED].** Log still reports `pdfTeX warning: PDF inclusion: found PDF version <1.7>, but at most version <1.5> allowed` for these two assets (and now also for `fig1-effort-gap.pdf`, `fig2-boredom-barrier.pdf`, `fig3-spider-farmer.pdf`, `fig4-ecoflow.pdf`, `fig5-methodology.pdf` — total 7 occurrences). No reader-visible defect today; arXiv-strict pdfTeX may eventually downgrade. Re-export to PDF 1.5. Severity unchanged. |
| LAY-14 | 1 | author affiliation block | font-shape-fallback | L | writer | `main.tex` author block region (was `:1896`) | **[UNCHANGED].** Log still emits `Font shape T1/lmtt/bx/n in size <10.95> not available; T1/lmtt/b/n tried instead`. Cosmetic; no reader-visible failure. |
| LAY-15 | 18, ~38, ~39 | three floats | float-placement-relaxed | L | writer | `main.tex:1136`, `:1256`, Pandora-jar float | **[UNCHANGED].** Log still emits three `'h' float specifier changed to 'ht'`. Cosmetic. |
| LAY-16 | 41–42 (was 39–40) | bibliography | underfull-hbox (justification rivers) | L | illustrator/writer (joint, advisory) | `main.bbl` (auto-generated from `references.bib`) | **[PARTIAL — UNCHANGED].** ~25 Underfull `\hbox` warnings in `main.bbl`. Bibliography auto-generated; same long-URL root cause. New bib entries (`papp2015embedded`, `vasile2018breakingallthethings`, `becker2020hwreexploratory`, `botero2021hwretutorial`, `grand2013jtagulator`) do not appear to have introduced fresh underfulls beyond baseline. |
| LAY-17 | 8, 11 (now ~8, ~12) | KPI summary tables | table-no-toprule-anchor | L→M | writer | `main.tex:494–509` (Spider Farmer; was `:428–445`) and `main.tex:643–654` (EcoFlow; was `:578–590`); mirrored at `main.md` §3.6 / §4.4 | **[REGRESSED].** Spider Farmer table overfull is **unchanged** at 55.48pt (494–509). EcoFlow table overfull has **grown** from 113.47pt to 113.47pt (643–654 — value identical, line range shifted). This pair is now numerically the second-worst overfull cluster after LAY-10/-19. Severity raised L→M because the Meta-process KPI table at 872–891 (NEW, see LAY-19) is structurally identical and exhibits 226.22pt overflow — a project-wide pattern in the four-column `tabular` `llll` definition that needs a one-shot fix. |
| LAY-18 | 14 | end of §5.7 | KPI-table column-width pressure | L | writer | `main.tex:927–946` (was `:863–882`) | **[PARTIAL — UNCHANGED].** Underfull cluster of badness 1308–10000 still present in lines 927–946. Cosmetic "rivers" survive. |
| **LAY-19** | ~14 | KPI summary tabular in §5.6 (Meta-process) | table-overflow | **H** | writer | `main.tex:872–891`; mirrored at `main.md` §5.6 / Meta-process KPI region | **[NEW].** Log: **`Overfull \hbox (226.22418pt too wide) in paragraph at lines 872--891`** — now the *single largest geometric overflow in the document* (~7.97 cm past the printable area). Source: `\begin{tabular}{llll}` for the Meta-process effort-gap timeline; the third column ("Key event" — sentences like "DLR design + fig1 data" and "AI disclosure + FAIR" with multi-clause subtitle) plus narrow first column drive the right edge past `\textwidth`. **Same column-definition pattern as LAY-17 (`llll`).** Suggested fix: convert to `tabularx` with `>{\raggedright\arraybackslash}X` for the "Key event" column and explicit narrow widths for the other three; or split the most-loaded rows onto two visual lines via `\\[0.2ex]`; do *not* `\resizebox` the table. Mirror in `main.md`. |
| **LAY-20** | ~22 | citation-dense paragraph in §6.4 limits | underfull-hbox cluster (justification rivers) | M | writer | `main.tex:1078–1101`; mirrored at `main.md` §6.4 region | **[NEW].** Log emits a dense underfull cluster of badness 1796–10000 across lines 1078–1101 (12 underfull warnings within 24 source lines), plus an `Overfull \hbox (52.64pt too wide)` at 1087–1088. The paragraph is heavy on inline `\citep{}` packs (`\citep{a, b, c, d}` patterns) producing both compressed and stretched lines. Suggested fix: rebreak the longest citation pack across two `\citep{...}` calls separated by short prose, or downgrade three `\citep{...}` to a single-keyed citation followed by a "see also" footnote. Cosmetic but measurable; the visible "rivers" run for ~12 lines. |
| **LAY-21** | ~17 | §6.5 mid-page | margin-overflow | L | writer | `main.tex:1087–1088` | **[NEW — bookkeeping]**. Tied to LAY-20 above; a single 52.64pt overfull line inside the underfull-cluster region. Listed separately so a single one-line rebreak can close it without disturbing the rest of the paragraph. |
| **LAY-22** | varies (8 occurrences) | trailing matter — TODO list, tables | margin-overflow | M | writer | `main.tex:2213–2217 (37.70pt)`, `:2351–2359 (70.91pt)`, `:2364–2369 (32.31pt)`, `:2387–2392 (16.08pt)`; plus three pre-existing entries already accounted for under LAY-08/-10 | **[NEW].** Four further overfull warnings in the §11 / §12 / appendix tail of the rebuilt PDF that did not appear in the prior log because the file was shorter (the `f3ce051` insertion plus minor §10 revisions appear to have reflowed the trailing matter onto pages where overflow now matters). Worst is 70.91pt at lines 2351–2359. Source spans cover the AI-disclosure footnote and the appendix references. Suggested fix: same shape as LAY-03/-10 (path / identifier wrapping). |

## Cluster-A.2-specific verification (per task brief)

- **Four new `\citep{}` calls in §1.4 / §6.8 render correctly.** Verified via
  `main.bbl` and the absence of any `Citation … undefined` log line.
  Specifically: `\citep{vasile2018breakingallthethings}` (`main.tex:190, :1288`),
  `\citep{becker2020hwreexploratory}` (`:194, :1291`),
  `\citep{botero2021hwretutorial}` (`:201, :1302`),
  `\citep{grand2013jtagulator}` (`:204, :1298`),
  plus the new §6.8 `\citep{papp2015embedded}` (`:1294`). All five resolve.
- **`\cref{sec:synthesis-evidence-asymmetry}` resolves.** Target label
  present at `main.tex:1275`; log shows zero `??` / undefined warnings.
  Cross-references at `main.tex:208` and `main.tex:237`.
- **`\textsuperscript{\ref{fn:hwre-cluster}}` resolves.** Target label
  present at `main.tex:187` (inside the §1.4 footnote). The four reuse
  sites (`main.tex:198, :1285, :1296`) all resolve cleanly per the log.
- **§1.4 paragraph density does NOT introduce new `\hbox` overruns.**
  The cluster A.2 paragraph spans `main.tex:165–208`; the log reports
  zero overfull warnings inside that range. The first overfull after
  the §1.4 paragraph appears at lines 212–216 (the contributions
  enumerate, pre-existing).
- **Bibliography lists `papp2015embedded` and shows van Woudenberg as 2022.**
  `main.bbl:94` has `\bibitem[Papp et~al.(2015)…]{papp2015embedded}`.
  `references.bib:216` has `@book{vanwoudenberg2022hwhandbook, … year = {2022}, …}`.
  Note: this entry is **bib-only-not-cited** in the rendered paper —
  `vanwoudenberg2022hwhandbook` does not appear in `main.bbl` because no
  `\cite{}` call references it (it is referenced via the
  `fn:hwre-cluster` footnote prose only). This is consistent with the
  writer's deliberate footnote-not-inline policy for L-HW-RE-5; flagged
  here as a fact, not a defect.
- **L-HW-RE-2 (ChipWhisperer) appears as a footnote reference, not inline.**
  Verified: the only mention of ChipWhisperer is at `main.tex:175–177`
  inside the §1.4 prose with `(L-HW-RE-2)\footnote{...}`, and the
  reuse at `main.tex:1285` via `\textsuperscript{\ref{fn:hwre-cluster}}`.
  No `\citep{...}` call wraps the ChipWhisperer mention. Compliant
  with the verification-ladder rationale recorded in the
  `fn:hwre-cluster` footnote text itself.

## Summary

- **Total defect entries this pass:** 22 (LAY-01..LAY-22).
  - **[RESOLVED]:** 2 (LAY-01, LAY-05).
  - **[PARTIAL]:** 11 (LAY-02..LAY-04, LAY-06..LAY-09, LAY-13, LAY-16,
    LAY-17, LAY-18).
  - **[UNCHANGED]:** 2 (LAY-14, LAY-15).
  - **[DEFERRED — by design]:** 1 (LAY-12).
  - **[REGRESSED-INTERPRETATION]:** 1 (LAY-11 — folded into LAY-06).
  - **[REGRESSED]:** 1 (LAY-17 — severity raised L→M as part of the
    `tabular{llll}` family with new LAY-19).
  - **[NEW]:** 4 (LAY-19..LAY-22).
- **By severity (current state):** H = 2 (LAY-19 new; LAY-13 unchanged
  is M, not H — the H count is genuinely down from 6 to 2);
  M = 11; L = 9.
- **By owner (current state):** writer = 16; illustrator = 5
  (LAY-05 [resolved], LAY-06, LAY-12, LAY-13, LAY-16-shared);
  joint advisory = 1 (LAY-16); informational placeholder = 1 (LAY-12).
- **Most consequential defect:** **LAY-19** — the Meta-process KPI
  `tabular{llll}` overflows the printable area by 226.22pt
  (~7.97 cm). It is the single largest geometric overflow surviving
  the writer remediation pass. Same root cause as the unresolved
  Spider Farmer (LAY-17, 55.48pt) and EcoFlow (LAY-17, 113.47pt) KPI
  tables: the fixed-width-column `llll` definition cannot absorb
  multi-clause "Key event" cells. A single project-wide convert-to-
  `tabularx`-with-X-column pass closes all three.

## Mirror-discipline (rule 11) check

Every writer-owned entry above cites both `main.tex` line ranges and a
mirrored `main.md` region. The §1.4 cluster A.2 paragraph is mirrored
at `main.md:62–82` (the `## Effort gap (§1.4)` block); §6.8 is mirrored
at `main.md:472–509` (`### Evidence asymmetry between software-side and
hardware-side effort-gap compression`). No structural drift between
`.tex` and `.md` was discovered during the scrutiny: section count,
heading order, and inline / footnote citation discipline match.

## Redaction (rule 12) check

Page-7 redaction markers in the rebuilt PDF: `\seqsplit{\texttt{[REDACTED:
username:S-SF-5-username]}}` and `\seqsplit{\texttt{[REDACTED:credential:
S-SF-5-password]}}` at `main.tex:481–482` are rendered intact in the new
PDF (they are inside an `\seqsplit` wrap that permits intra-tag
hyphenation but does not alter the token text). No live credential
leakage in the rebuilt artifact. The defect filed under LAY-07 is
geometric, not redactional, and is now [PARTIAL → L].

## Rule 13 compliance

This pass operates only on the local PDF. No upload to external services
(viewer remained inert; `make arxiv` was NOT invoked).

## RE-SCRUTINY REQUIRED: yes — one H-severity entry (LAY-19, the Meta-process KPI tabular at 226.22pt overfull) plus the same-family LAY-17 EcoFlow / Spider-Farmer KPI tables and the §10 path-bullet cluster (LAY-10, 168.71pt) prevent a clean reading of headline KPIs. Additionally, writer commit `a104fa3` (Executive Summary, +90 lines, new on-disk PDF SHA `aa89604f…`) landed during this scrutiny and was not inspected; a follow-up Stage 4 pass against the new PDF should both verify the cluster A.2 / §6.8 content (whose line ranges have shifted by ~+90) and inspect the new Executive Summary block for fresh overfulls. A single tabularx conversion closes LAY-17 + LAY-19; a path-wrapping pass closes LAY-03/-09/-10/-22. Rebuild and re-sweep required.
