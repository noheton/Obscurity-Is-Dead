# Layout Defect Registry — paper/main.pdf

- **PDF SHA-256:** `db8774f125898ab4d0fd3d3450c39c4e5b3fc2f425fdc4c9a25af270f4d511d2`
- **PDF size:** 1,220,982 bytes; **53 pages** (was 49 in prior round-1 pass).
- **Build timestamp:** 2026-05-03T17:17:49Z (newer than `main.tex` 16:57:42Z).
- **Build commits since round 1:** `4987d9d` (tabularx + `\Description{}` + RDB-27/28), `b5162ee` carried, `370e792` (Mythos + ninth-practice), `d2858ac` (figure overhaul fig6/7/9/10/11/14).
- **Source under inspection:** `paper/main.tex` (~2,860 lines); mirrored in `paper/main.md`.
- **LaTeX log:** `paper/main.log` (50,652 bytes): **34 `Overfull \hbox`**, **61 `Underfull \hbox`**, **0 `Reference … undefined`**, **0 `Citation … undefined`**, **0 `??`**, **0 PDF-1.7-inclusion warnings**, only standard xcolor model substitutions and OT1/cmtt→OT1/lmtt font-shape fallbacks (cosmetic, on lines 34/38; not a regression).
- **Scrutinizer:** Stage 4 — Layout Scrutinizer, round 2, 2026-05-03 (Claude Opus 4.7).
- **Method note:** Pixel-level visual sweep is `viewer-blocked` (no PDF viewer MCP). Sweep performed via `paper/main.log` ground-truth (geometric overfulls cite source line ranges; cross-checked against `paper/main.tex`). Source-level confirmation of `\Description{}` macros, `tabularx` conversion, and `\cref` label integrity performed.

## Round-1 carry-over disposition

| ID | Round-1 status | Round-2 status | Note |
|----|----------------|----------------|------|
| LAY-01 | RESOLVED | RESOLVED | Zero undefined refs; new labels (`sec:ai-disclosure-models`) resolve. |
| LAY-02 | PARTIAL | PARTIAL (line shift) | §3.4 reconciliation-table prose preface still produces 32.16pt (`:479–483`) + 11.72pt (`:483–488`) — these are the `\enumerate{}` items in §1.6 contributions, line-shifted by Mythos integration. Tied to LAY-24 below. |
| LAY-03 | PARTIAL | PARTIAL | §5.2 path-bullet cluster shifted to `:920–933` (66.67pt; 12.76pt). Down from 168pt+ peak. Tied to LAY-09. |
| LAY-04 | PARTIAL | PARTIAL | §6.5 bullet-list region: 0.18pt residual at `:1379–1394` (negligible; effectively closable). |
| LAY-05 | RESOLVED | RESOLVED | Figure 7 float clean. |
| LAY-06 | PARTIAL | PARTIAL | Difficulty-taxonomy table residual: 8.80pt at `:1462–1463` + 2.53pt at `:1460–1486`. Figure-side closed; table-side `p{}` width pressure remains. |
| LAY-07 | RESOLVED | RESOLVED | No overfulls anchored on redaction tags. |
| LAY-08 | PARTIAL | PARTIAL | §4.4 region produces 12.07pt at `:625–627` + 66.39pt at `:657–660` (writeable-entity comma-list pressure). |
| LAY-09 | PARTIAL | PARTIAL | Cluster of 6 overfulls in `:1027–1054` (range 12.46–70.84pt); root cause = path bullets, same as LAY-03. |
| LAY-10 | PARTIAL | PARTIAL | §10 path-bullet cluster moved to `:2497–2552`: 50.18pt; **35.69pt** at 2530–2552. The prior 168.71pt single-line path overfull has *migrated* to a new location (see LAY-26 H below) — this is **not the same source-span** as round 1. |
| LAY-11 | RESOLVED | RESOLVED | Folded into LAY-06. |
| LAY-12 | PARTIAL | PARTIAL (unchanged) | Intact-jar Gemini deliverable still outstanding; placeholder honestly disclosed. |
| LAY-13 | RESOLVED | RESOLVED | Zero PDF-1.7 inclusion warnings. |
| LAY-14 | UNCHANGED | UNCHANGED-COSMETIC | OT1/cmtt → OT1/lmtt substitution at log lines 60/68 only (input lines 34/38, preamble). No T1/lmtt/bx/n substitution this build (different shape — cosmetic only, downgrade to L). |
| LAY-15 | UNCHANGED | RESOLVED-by-omission | No fresh `'h' float specifier changed to 'ht'` warnings emitted in this log. Closable. |
| LAY-16 | PARTIAL | PARTIAL | Bibliography underfull cluster persists (~25 entries, log lines 1149+). Auto-generated; long URLs. |
| **LAY-17** | REGRESSED-CONFIRMED | **RESOLVED** | Spider Farmer KPI now `tabularx{\linewidth}{l l X r}` at `main.tex:790–804`. Prior 55.48pt overflow at 713–728 is gone from the log. Three small residual 11.03/9.38/15.04pt overfulls keyed *inside* line 753 originate from `\texttt{84Rf7SUk\ldots}` cells inside the new tabularx — these are intra-cell, not whole-row, and are bookkept under LAY-27 below. Family-pattern fix successful. |
| LAY-18 | PARTIAL | PARTIAL | Underfull-badness cluster around `:1387–1486` persists; cosmetic rivers in difficulty-taxonomy and adjacent prose. |
| **LAY-19** | NEW H (226pt) | **RESOLVED** | Meta-process KPI converted to `tabularx{\linewidth}{l l X r}` at `main.tex:1197–1215`. The 226.22pt overflow at 1117–1136 has disappeared from the log. Largest geometric defect of round 1 is closed. EcoFlow KPI (the 113.47pt sibling) likewise converted at `main.tex:965–975` and clean. |
| LAY-20 | PARTIAL | PARTIAL | Underfull cluster still in §6.4 region (~`:1411–1427`); 30.26pt + 52.64pt + 23.06pt cluster — same wrap pressure as round 1. |
| LAY-21 | PARTIAL | PARTIAL | 52.64pt overfull at `:1413–1414` (was 1333–1334; line-shifted, same source). |
| LAY-22 | CONFIRMED + EXPANDED | PARTIAL-MUTATED | Trailing-matter overfulls survive: 37.70pt at `:2615–2619`, 70.91pt at `:2779–2787`, 32.31pt at `:2792–2797`, 16.08pt at `:2815–2820`. The 25.74pt at `:2163–2172` (trust-laundering item) persists. Mostly path-list / `\texttt{}` wrap pressure. |
| **FIG-01** | NEW H (alt-text-missing) | **RESOLVED** | All 18 `\includegraphics` calls are now followed by a `\Description{...}` macro (verified by source grep at `main.tex:355, 420, 605, 644, 882, 905, 1139, 1500, 1589, 1727, 1762, 1770, 2229, 2352, 2458, 2739, 2860`); preamble `\providecommand{\Description}{}` shim at `main.tex:32`. Accessibility blocker closed. Illustrator confirmation (descriptions match assets) tracked separately under FIG-10 below. |
| FIG-02 | M (CB palette) | PARTIAL → CLOSED-FOR-REWORKED-FIGURES | fig6/7/9/10/11/14 redone with Tol-bright / DLR_BLUE+GREEN / sequential blue palettes per illustrator hand-back. Residual remains for fig8 (red `#c0392b` legacy-surface — gated on author-decision), fig15 (borderline), fig16 (red exclusion ring). Filed forward as FIG-11. |
| FIG-03 | M (fig11 density) | EXPECTED-RESOLVED-VIEWER-BLOCKED | fig11 row labels raised 8.6 → 10.5 pt per illustrator script; CB-safe header palette; zebra rows; numbered badges. Closure expected but viewer-blocked. |
| FIG-04 | M (logo placeholder) | UNCHANGED | Gated on human Gemini deliverable. |
| FIG-05 | L (rule-14 advisory) | UNCHANGED-NARROWED | fig6 + fig7 promoted to scripted source (rule-14 compliant). fig2/3/4/5 remain manually drawn, exempt. |
| FIG-06 | L (structural-data exemption) | UNCHANGED | Bookkeeping; documented in `paper/figures/README.md`. |
| FIG-07 | M (fig12 caption-mismatch) | EXPECTED-RESOLVED-VIEWER-BLOCKED | Caption read at `main.tex:1500` describes 4×3 heat-map with three difficulty-axis columns — matches post-fix asset. Viewer-blocked for visual confirmation. Recommend close on next visual sweep. |
| FIG-08 | L (fig11 vs §10 prose) | PARTIAL | §10 prose enumeration kept (8 items at `main.tex:2611–2820`); ninth-practice now also added in prose between `:2822` and the section close. Caption at `main.tex:2860` carries P/S legend. Pending RDB-04 author decision. |
| FIG-09 | L (data-to-ink audit-incomplete) | UNCHANGED | Viewer-blocked. |

## New defects this round (LAY-23..LAY-28; FIG-10..FIG-11)

| ID | Page | Region | Defect class | Severity | Owner | Source span | Suggested fix |
|----|------|--------|--------------|----------|-------|-------------|---------------|
| **LAY-23** | front-matter | preamble fonts | font-shape-cosmetic | L | writer | preamble lines 34/38 | Cosmetic OT1/cmtt → OT1/lmtt substitution noted in log lines 60/68. Pre-existing; harmless. Carry forward at L. |
| **LAY-24** | mid-doc | §1.6 contributions enumerate | overfull-prose | M | writer | `main.tex:479–488` (32.16pt; 11.72pt) | Two tight prose overflows on the contributions enumerate (paths `\texttt{docs/methodology.md}` and `\texttt{experiments/spider-farmer/}`). Rebreak with `\sloppy`-equivalent rewording, or wrap the long `\texttt{}` paths in `\seqsplit{}`. |
| **LAY-25** | mid-doc | §6.6 / §6.7 boundary | overfull-cluster | M | writer | `main.tex:1071–1112` (43.53pt + 5.21pt + 61.91pt); `:1027–1054` (6 entries, 12.46–70.84pt range) | Path-bullet cluster persists. Same shape as LAY-03/-09/-10. Apply `\seqsplit{}` to long `\texttt{}` paths or break the bullet content over two `\item`s. |
| **LAY-26** | §10.AI-disclosure (new prose) | §10.AI-disclosure-models paragraph | overfull-prose-path | **H** | writer | `main.tex:2518–2529` (**168.71pt**) | The path `\texttt{experiments/*/raw\_conversations (copy\&paste, web)/}` and its sibling `\texttt{experiments/paper-meta-process/raw\_conversations (copy\&paste, web)/T1-paper-structure-and-literature.md}` are unbreakable single tokens crossing 168 pt of right-margin. **This is the single largest geometric defect in the document, replacing the round-1 LAY-19 overflow at exactly the same magnitude.** Wrap each in `\seqsplit{}` (already loaded for redaction tags) or `\path{}` from the `url` package, or rewrite to fold the parenthetical "(copy\&paste, web)" out of the path. |
| **LAY-27** | §3.6 Spider Farmer KPI | tabularx intra-cell | overfull-intracell | L | writer | `main.tex:753` (3 entries: 11.03 / 9.38 / 15.04 pt) | The new `tabularx` correctly absorbs whole-row width but three `\texttt{84Rf7SUk\ldots}` literal-bytes cells overflow their `X` column. Cosmetic; consider raggedright-X or `\seqsplit{}` on those literals. Bookkeeping only — the round-1 H severity is gone. |
| **LAY-28** | §6.4 region (rounded) | underfull-cluster persistent | underfull-cosmetic | L | writer | `main.tex:1252–1486` (10+ underfull badness 1252–10000) | River pressure inside the difficulty-taxonomy preface and tables; cosmetic, no claim affected. |
| **FIG-10** | all 18 figure floats | `\Description{...}` text fidelity audit | alt-text-fidelity | L | illustrator | `main.tex:355, 420, 605, 644, 882, 905, 1139, 1500, 1589, 1727, 1762, 1770, 2229, 2352, 2458, 2739, 2860` | Writer authored alt-texts from caption + filename, not from pixels. Illustrator pass should confirm every `\Description{}` text matches what the rendered asset visually shows. (Distinct from FIG-01 which was the *presence* check.) |
| **FIG-11** | fig8 / fig15 / fig16 | residual CB-palette work | colour-accessibility | M | illustrator | `paper/figures/fig{8,15,16}-*.py` | fig8 red legacy-surface palette (gated on human-author "is the red semantic?" decision); fig15 borderline green; fig16 red exclusion ring + 7.8 pt cells under threshold. Carry-forward of FIG-02 residual. |

## Severity rollup (current open state)

- **H:** 1 — LAY-26 (168.71pt path overfull in §10.AI-disclosure-models, `main.tex:2518–2529`).
- **M:** 8 — LAY-02, LAY-06, LAY-08, LAY-09, LAY-10, LAY-20, LAY-22, LAY-24, LAY-25, FIG-04, FIG-08, FIG-11. (12 entries total; 8 distinct M severity).
- **L:** 13 — LAY-03 (downgraded), LAY-04, LAY-14/-23, LAY-16, LAY-18, LAY-21, LAY-27, LAY-28, FIG-05, FIG-06, FIG-09, FIG-10.
- **RESOLVED this round:** LAY-15, LAY-17, LAY-19, FIG-01 (the two round-1 H items + LAY-17 family + LAY-15).

## Severity by class

- **Layout (LAY-*):** H=1, M=7, L=8. Net +3 entries (LAY-23..-28; -2 closed).
- **Figure (FIG-*):** H=0, M=3, L=4. Net +2 entries (FIG-10/-11; -1 closed FIG-01).

## Owner rollup

- **Writer:** LAY-02, -03, -04, -08, -09, -10, -14/-23, -16 (advisory), -18, -20, -21, -22, -24, **-26 (H)**, -25, -27, -28; FIG-08 caption-defer.
- **Illustrator:** LAY-06 figure-side closed; LAY-12 (Gemini gated); FIG-04 placeholder, FIG-05/-06 bookkeeping, FIG-09 audit-incomplete, **FIG-10 fidelity audit**, **FIG-11 residual CB palette**.
- **Joint:** none after FIG-01 closure.

## §10 ninth-practice + new prose spot-checks

- §10 enumerate at `main.tex:2611..2820` — eight `\item` entries intact; `\cref{fig:eight-practices}` resolves; `\cref{sec:case-meta}` resolves; `\cref{sec:ai-disclosure}` resolves.
- §10 ninth-practice block at `main.tex:2822..` (post-`\end{enumerate}` running prose) — no nested `\enumerate` at counter 9 in the source as inspected; the ninth-practice text is paragraph-style rather than list-continuation. No counter-9 `\setcounter{enumi}{8}` continuation observed; this is consistent with the writer's "logged for the next iteration … rather than added to Figure 11" framing. Caption-fidelity for fig11 unaffected.
- §7.3 Mythos paragraph and §7.4 band-aid sub-paragraph: source-level OK, no overfulls anchored on these spans in the log.
- Author's Note (now 8 paragraphs): no overfulls anchored on the Author's Note span in the log.
- All `\cref{...}` references parse without error (zero `??` in PDF, zero `Reference ... undefined` in log).

## Mirror discipline (rule 11) check

Writer pass `4987d9d` mirrored Job-3 (RDB-27/-28) prose splits across both files. Mythos integration `370e792` claims md/tex parity at every touched span (logbook entry). Heading order, section labels, and float sequence between `paper/main.md` and `paper/main.tex` match. No structural drift detected from log.

## Redaction (rule 12) check

`[REDACTED:repo-path:BALBOA-UPSTREAM-1]` and `[REDACTED:repo-path:BALBOA-UPSTREAM-2]` markers at `main.tex:2168–2169` survive the build. Their host bullet (`:2163–2172`) carries a 25.74pt overfull (LAY-22 family) — the redaction tag itself is wrapped in `\texttt{}` but not in `\seqsplit{}`; suggested fix: wrap in `\seqsplit{}` to relieve the line.

## Rule 13 compliance

This pass operates only on the local PDF. No upload to external services; `make arxiv` not invoked.

## RE-SCRUTINY REQUIRED: yes — One H-severity entry: **LAY-26** (168.71pt unbreakable `\texttt{}` path in §10.AI-disclosure-models at `main.tex:2518–2529`) replaces the now-closed round-1 LAY-19 at the same magnitude. Round-1 H items LAY-19 and FIG-01 are both confirmed RESOLVED via the writer's `tabularx` refactor and 18 `\Description{}` macros respectively. The path-bullet wrap pass (LAY-03/-09/-10/-22/-25) is not yet applied and accounts for the bulk of the remaining 33 overfulls; a single `\seqsplit{}` / `\path{}` / `\sloppypar` pass over `\texttt{}` paths in §1.6, §5.2, §6.6/§6.7, §10, and §10.AI-disclosure should close most of the M-severity registry in one writer loop. The figure overhaul has cleared FIG-02 / FIG-03 for the six reworked figures; FIG-04 (Gemini placeholder) and FIG-11 (fig8/15/16 residual) carry forward. Rebuild + re-sweep required after writer + illustrator hand-backs are consumed.
