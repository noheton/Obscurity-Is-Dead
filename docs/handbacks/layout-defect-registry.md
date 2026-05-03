# Layout Defect Registry — paper/main.pdf

- **PDF SHA-256:** `04e818e993e2eea84cf05d5a5bc7045d80270d6a856a398cc04106ca7ac5cf99`
- **PDF size:** 1,170,691 bytes; **49 pages** (was 42 in prior pass).
- **Build timestamp:** 2026-05-03T12:54:14Z (newer than `main.tex` 12:54:06Z).
- **Build commit:** `b5162ee` (`paper(fix): remove spurious \begin{itemize} in §7.6 sloppification`).
- **Source under inspection:** `paper/main.tex` (2,797 lines); mirrored in `paper/main.md` (716 lines).
- **LaTeX log:** `paper/main.log` (1,342 lines): **37 `Overfull \hbox`**, **61 `Underfull \hbox`**, **0 `Reference … undefined`**, **0 `Citation … undefined`**, **0 `??`**, **0 `pdfTeX warning: PDF inclusion … version <1.7>`** (LAY-13 fix successful — PDF is now v1.5 throughout), 1 `Font shape T1/lmtt/bx/n` substitution (line 1082).
- **Scrutinizer:** Stage 4 — Layout Scrutinizer, 2026-05-03 (Claude Opus 4.7).
- **Method note:** PDF viewer MCP unavailable; sweep performed via `paper/main.log` ground-truth (geometric overfulls cite source line ranges; cross-checked against `paper/main.tex`). Pixel-level visual sweep of figure-internal text is `viewer-blocked` for fig2–fig7 (manually drawn SVGs; cannot inspect embedded font sizes from log alone). All `FIG-` entries below that depend on rendered visual inspection are flagged `viewer-blocked` — they reflect static analysis of the asset scripts and the `\includegraphics` widths only.

## Carry-over disposition (LAY-01..LAY-22 from prior pass)

| ID | Prior status | This pass | Note |
|----|--------------|-----------|------|
| LAY-01 | RESOLVED | RESOLVED | Labels `sec:scope-non-goals` (`main.tex:440`), `sec:synthesis-evidence-asymmetry` (`:1521`), `sec:disc-validity` (`:1782`) all present; zero undefined refs. |
| LAY-02 | PARTIAL | PARTIAL (line shift) | Reconciliation table region — 4 small overfulls in 410–419 / 555–557 / 586–589 (worst 66.39pt). Cosmetic; still M. |
| LAY-03 | PARTIAL | PARTIAL | §5.2 path-bullet cluster now at lines 841–854 (66.67pt; 12.76pt). Down from 168pt+ peak. Tied to LAY-09. |
| LAY-04 | PARTIAL | PARTIAL | §6.5 bullet list region: 0.18pt residual (negligible) + adjacent. Effectively closable. |
| LAY-05 | RESOLVED | RESOLVED | Figure 7 float clean. |
| LAY-06 | PARTIAL | PARTIAL | Difficulty-taxonomy table residual: 8.80pt at 1382–1383 + 2.53pt at 1380–1406. Figure-side closed by illustrator (`fig12-difficulty-taxonomy.{py,svg,pdf}` regenerated to drop Composite column); table-side `p{}` width pressure remains writer-owned. |
| LAY-07 | PARTIAL→L | RESOLVED | No overfulls anchored on redaction tags in this build. |
| LAY-08 | PARTIAL→L | PARTIAL | §4.4 region produces 12.07pt at 555–557 + 66.39pt at 586–589 (writeable-entity comma list pressure). |
| LAY-09 | PARTIAL | PARTIAL | Cluster of 6 overfulls in 948–975 (range 12.46–70.84pt); root cause = path bullets, same as LAY-03. |
| LAY-10 | PARTIAL | PARTIAL | §10 path-bullet cluster moved to 2348–2403: 50.18pt; **168.71pt** at 2369–2380 (single largest in document); 35.69pt at 2381–2403. T1 transcript path still unwrapped. |
| LAY-11 | RESOLVED-by-fold | RESOLVED | Folded into LAY-06. |
| LAY-12 | PARTIAL (intact-jar pending) | PARTIAL (unchanged) | Intact-jar Gemini deliverable still outstanding; placeholder honestly disclosed at `main.tex:2381–2402`. |
| LAY-13 | PARTIAL | **RESOLVED** | Zero `pdfTeX warning: PDF inclusion … version <1.7>` in this log. Makefile post-process worked. |
| LAY-14 | UNCHANGED | UNCHANGED | `T1/lmtt/bx/n` substitution still emitted (line 1082). Cosmetic. |
| LAY-15 | UNCHANGED | UNCHANGED | No fresh `'h' float specifier changed to 'ht'` warnings emitted in this log; downgrade to closable on next pass. |
| LAY-16 | PARTIAL | PARTIAL | Bibliography underfull cluster persists (~25 entries in `main.bbl`). Auto-generated; long URLs. |
| LAY-17 | REGRESSED | REGRESSED-CONFIRMED | Spider Farmer KPI tabular `llll` at `main.tex:713–728` still 55.48pt; EcoFlow KPI at `:886–897` still 113.47pt. Same family as LAY-19 below. |
| LAY-18 | PARTIAL | PARTIAL | Underfull badness cluster around `:1387–1402` persists; cosmetic rivers. |
| LAY-19 | NEW (H, 226pt) | **CONFIRMED H** | Meta-process KPI `\begin{tabular}{llll}` at `main.tex:1117–1136` (was 872–891) still overflows by **226.22pt**. Single largest geometric defect in the document. Same fix shape as LAY-17. |
| LAY-20 | NEW (M) | PARTIAL (line shift) | Underfull cluster still present in §6.4 region (now ~`:1330–1346`); 12+ underfulls + 30.25pt overfull at 1331–1332. |
| LAY-21 | NEW (L) | PARTIAL | 52.64pt overfull at 1333–1334 (was 1087–1088). |
| LAY-22 | NEW (M) | CONFIRMED + EXPANDED | Trailing-matter overfulls survive: 37.70pt at 2466–2470, 70.91pt at 2629–2637, 32.31pt at 2642–2647, 16.08pt at 2665–2670. Plus 25.74pt at 2017–2026 (newly visible after Executive Summary insertion). |

## New defects this pass (LAY-23..LAY-25; FIG-01..FIG-09)

| ID | Page | Region | Defect class | Severity | Owner | Source span | Suggested fix |
|----|------|--------|--------------|----------|-------|-------------|---------------|
| **LAY-23** | front-matter (p.1) | author block | font-shape-fallback (continued LAY-14) | L | writer | `main.tex:2265` (per log) | Cosmetic. `T1/lmtt/bx/n` substituted to `T1/lmtt/b/n`. Wrap the offending bold-tt token in `\texttt{\textbf{...}}` reordering or accept fallback. |
| **LAY-24** | mid-doc | §3.4 reconciliation table | overfull-prose-preface | M | writer | `main.tex:410–419` (32.16pt; 11.72pt) | Two tight prose overflows just before the cross-implementation table. Rebreak the introductory sentence; do not touch the tabular. |
| **LAY-25** | mid-doc | §6.6 / §6.7 zone | overfull-cluster | M | writer | `main.tex:992–997` (43.53pt); `:1007–1010` (5.21pt); `:1028–1033` (61.91pt) | Three previously-unenumerated overfulls in the §6.6/§6.7 boundary; cause is identifier-list bullets. Same path-wrap shape as LAY-03/-10. |

### Figure & image critique (FIG-01..FIG-09)

Per the 2026-05-03 prompt extension, every shortcoming is filed (severity still graded H/M/L). Owner = `illustrator` unless noted.

| ID | Page | Figure | Defect class | Severity | Owner | Source / asset | Suggested fix |
|----|------|--------|--------------|----------|-------|----------------|---------------|
| **FIG-01** | all 18 figure floats | every `\includegraphics` in `main.tex` | **alt-text-missing** | **H** | joint (writer adds macro; illustrator confirms text matches) | `main.tex:287, 351, 535, 573, 804, 826, 1059, 1419, 1507, 1613, 1647, 1654, 2082, 2204, 2309, 2589, 2674` | Zero `\Description{...}` macros, zero `pdftex` `/Alt` entries, and the captions are not formally tagged as alt-text. Add `\Description{...}` per `\includegraphics` (or load `pdfcomment` / `tagpdf`). Required for accessibility; rule-1-adjacent (honesty about who can read the document). |
| **FIG-02** | page hosting `fig:effort-gap`, `fig:stage-effort`, `fig:difficulty-taxonomy` | `fig1-effort-gap.svg`, `fig10-stage-effort.svg`, `fig12-difficulty-taxonomy.svg` | **colour-accessibility** | M | illustrator | `paper/figures/dlr_style.py` + the three scripts | DLR-style palette flagged in prior passes as failing deuteranopia simulation; no Viridis/ColorBrewer migration in this build. Confirm or migrate categorical/sequential figures to colour-blind-safe palette and add explicit greyscale fallback (line dashing / marker shape). `viewer-blocked`: not visually verified this pass. |
| **FIG-03** | wherever fig11 hero appears | `fig11-eight-practices.svg` (hero / visual abstract) | **density** | M | illustrator | `paper/figures/fig11-eight-practices.py` | 8 rows × 3 cols cell labels reportedly at fontsize ~8.6 (per illustrator hand-back). At full `\textwidth` print scale this is borderline below the 7pt-equivalent threshold once shrunk for arXiv letter PDF. Verify rendered point size; raise to 9 pt or split into two-row legend. `viewer-blocked`. |
| **FIG-04** | 4 logo / Pandora floats | `logo-pandora-jar-intact.png` (950×944, ~83 kB) | **legibility / placeholder-quality** | M | illustrator (gated on human Gemini delivery) | `paper/figures/logo-pandora-jar-intact.png`; `main.tex:2589` | Asset is the matplotlib typographic placeholder, not the final Gemini deliverable. At `width=0.55\linewidth` it occupies a meaningful share of §10 anchor page; the typographic stand-in degrades the visual rhetoric. **Awaiting human Gemini PNG**; tracking entry only — do not regenerate. |
| **FIG-05** | fig2–fig7 floats | `fig2-boredom-barrier.svg` … `fig7-threat-models.svg` | **rule14-source-script-absent** | L | illustrator (advisory) | `paper/figures/fig{2..7}-*.svg` | Manually drawn — explicitly exempt from rule 14 per `paper/figures/README.md` (CLAUDE_CODE_INSTRUCTIONS.md exemption clause). Filed as L for completeness so the registry shows the exemption was checked, not as a defect to fix. |
| **FIG-06** | fig8, fig9, fig11, fig13, fig14, fig15, fig16 | seven structural-diagram SVGs | **rule14-data-absent (structural exemption)** | L | illustrator | `paper/figures/fig{8,9,11,13,14,15,16}-*.py` | Generation scripts present, but no CSV / data file — these diagrams encode structural relationships, not numerical data. README documents the exemption. L-severity bookkeeping entry; no fix required. |
| **FIG-07** | fig12 caption | `fig12-difficulty-taxonomy.svg` (3-column post-fix) | **caption-figure-consistency** | M | writer | `main.tex:1419–1420` (caption span) | Illustrator dropped the `Composite` column from the heat-map this cycle. Caption text in `main.tex:1420` should be reviewed to confirm it does not still claim a 4-column / composite-rating panel. (Source-only check; viewer-blocked for visual confirmation.) |
| **FIG-08** | fig11 caption vs §10 prose | `fig11-eight-practices.svg` | **caption-figure-consistency** | L | writer | `main.tex:2674` figure caption + §10 enumeration `main.tex:2348–2403` | Pending the human-author decision on §10 enumeration vs Figure 11 collapse (writer hand-back options a/b/c). Until resolved, the §10 prose enumeration paraphrases the same eight practices the figure encodes — caption should defer explicitly to the figure. |
| **FIG-09** | every figure float | all `\includegraphics` calls | **data-to-ink ratio (per-figure audit not performed visually)** | L | illustrator | `paper/figures/*.py` | `viewer-blocked`. The prompt extension instructs flagging shortcomings against the seven dimensions; a full Tufte-style chartjunk audit requires pixel-level inspection of each rendered float. Filed as a single L bookkeeping entry to record that the audit dimension was checked but the harness viewer was unavailable; a follow-up pixel-level pass is recommended once the PDF viewer MCP is restored. |

## Severity rollup (current open state)

- **H:** 2 — LAY-19 (226pt KPI tabular), FIG-01 (alt-text-missing across all 18 figures).
- **M:** 11 — LAY-02, LAY-06, LAY-08, LAY-09, LAY-10 (168pt path bullet, hardware overflow but cosmetic), LAY-12, LAY-17, LAY-20, LAY-22, LAY-24, LAY-25, FIG-02, FIG-03, FIG-04, FIG-07.
- **L:** 11 — LAY-03 (downgraded), LAY-04, LAY-14/-23, LAY-15, LAY-16, LAY-18, LAY-21, FIG-05, FIG-06, FIG-08, FIG-09.

## Severity by class

- **Layout (LAY-*):** H=1, M=10, L=8 (24 entries across carry-over + 3 new).
- **Figure (FIG-*):** H=1, M=4, L=4 (9 entries).

## Owner rollup

- **Writer:** LAY-02, -03, -04, -07 (closable), -08, -09, -10, -14/-23, -15, -17, -18, -19, -20, -21, -22, -24, -25; FIG-07 caption-mismatch; FIG-08 caption-defer; FIG-01 (writer adds `\Description{}` macro). ~17 writer items.
- **Illustrator:** LAY-06 figure-side (closed by prior illustrator pass; table residual = writer); LAY-12 (Gemini deliverable gated on human); LAY-13 (closed); LAY-16 (advisory); FIG-02 colour, FIG-03 density, FIG-04 placeholder, FIG-05/-06 bookkeeping, FIG-09 audit-incomplete; FIG-01 illustrator confirms description text matches asset.
- **Joint:** FIG-01 (alt-text mechanism is jointly writer + illustrator).

## Mirror discipline (rule 11) check

The §1.4 cluster A.2 paragraph split (writer pass 2026-05-03) is reflected in both files; §6.8 splits ditto. Heading order, section labels, and float sequence between `paper/main.md` (716 lines) and `paper/main.tex` (2,797 lines) match. No structural drift detected.

## Redaction (rule 12) check

Page-7 redaction markers (`\seqsplit{\texttt{[REDACTED:username:S-SF-5-username]}}` and `\seqsplit{\texttt{[REDACTED:credential:S-SF-5-password]}}` at `main.tex` mid-400s) render intact and produce no overfulls in this build. No live credentials, serial numbers, or local IPs detected in scan of figure captions or KPI tables.

## Rule 13 compliance

This pass operates only on the local PDF. No upload to external services; `make arxiv` not invoked.

## RE-SCRUTINY REQUIRED: yes — Two H-severity entries: (1) **LAY-19** Meta-process KPI `tabular{llll}` at `main.tex:1117–1136` still overflows by **226.22pt** (the largest geometric defect in the document); same family-pattern as LAY-17 (Spider Farmer 55.48pt; EcoFlow 113.47pt) — a single `tabularx`-with-`X`-column conversion closes the family. (2) **FIG-01** zero `\Description{}` / `/Alt` alt-text across all 18 `\includegraphics` calls — accessibility blocker. Path-bullet wrap pass closes LAY-03/-09/-10/-22/-25. The figure stock requires substantial illustrator work (FIG-02 colour-blind palette migration, FIG-03 fig11 fontsize verification at print scale, FIG-04 intact-jar Gemini final, FIG-09 deferred pixel-level Tufte audit) — the human author's earlier acknowledgement that the figure stock is currently lacking is endorsed by this pass. Rebuild + re-sweep required after writer + illustrator hand-backs are consumed.
