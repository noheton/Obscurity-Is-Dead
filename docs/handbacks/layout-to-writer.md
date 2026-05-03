# Layout Scrutinizer — Hand-back to Scientific Writer (2026-05-03)

Source: `docs/handbacks/layout-defect-registry.md` — PDF SHA-256 `04e818e993e2eea84cf05d5a5bc7045d80270d6a856a398cc04106ca7ac5cf99`, 49 pages, build commit `b5162ee`, build timestamp 2026-05-03T12:54:14Z. LaTeX log: `paper/main.log` (37 overfulls, 61 underfulls, zero undefined refs/cites, zero PDF-version-1.7 warnings — LAY-13 closed).

Items below are owned by the scientific writer and require source-level edits to `paper/main.tex` (mirrored in `paper/main.md` per rule 11). Do **not** edit figure scripts.

## LAY-19 — Meta-process KPI tabular overflows by 226.22pt (single largest defect)

- Page: KPI summary in §5.6 (Meta-process)
- Source: `main.tex:1117–1136`; mirrored at `main.md` §5.6 KPI region.
- Observed: `Overfull \hbox (226.22418pt too wide) in paragraph at lines 1117--1136`. Cause: `\begin{tabular}{llll}` with multi-clause "Key event" cells like `\texttt{dlr\_style.py}, \texttt{data/effort-gap.csv}, \texttt{fig1-effort-gap.py}; Rule-14 compliance`.
- Required action: convert to `tabularx` with fixed-narrow columns for Phase / Commit / Est. and `>{\raggedright\arraybackslash}X` for "Key event"; or split loaded rows on `\\[0.2ex]`. Do **not** `\resizebox`. Mirror in `main.md`.
- Severity: **H**

## LAY-17 — Spider Farmer + EcoFlow KPI tabulars (same family as LAY-19)

- Source: `main.tex:713–728` (Spider Farmer, 55.48pt); `main.tex:886–897` (EcoFlow, 113.47pt).
- Observed: same `llll` column definition. A single project-wide refactor closes LAY-17 + LAY-19 atomically.
- Required action: same `tabularx` / `X`-column conversion.
- Severity: M (treat as H if attacked as a unit with LAY-19)

## LAY-10 — §10 path-bullet cluster, 168.71pt overfull at `:2369–2380`

- Source: `main.tex:2348–2403`; mirrored in `main.md` §10.
- Observed: 50.18pt at 2348–2351, **168.71pt** at 2369–2380, 35.69pt at 2381–2403. Cause: the `experiments/paper-meta-process/raw_conversations (copy&paste, web)/T1-paper-structure-and-literature.md` path is unwrapped.
- Required action: wrap the path in `\fp{...}` or `\seqsplit{\texttt{...}}`. Apply to all four §10 transcript paths.
- Severity: M

## LAY-22 — Trailing-matter overfulls (§11/§12/appendix)

- Source: `main.tex:2466–2470` (37.70pt), `:2629–2637` (70.91pt), `:2642–2647` (32.31pt), `:2665–2670` (16.08pt); plus `:2017–2026` (25.74pt).
- Observed: same path/identifier wrap pattern as LAY-10.
- Required action: same `\fp{}` / `\seqsplit{}` wrap pass.
- Severity: M

## LAY-25 — §6.6 / §6.7 boundary cluster (NEW)

- Source: `main.tex:992–997` (43.53pt), `:1007–1010` (5.21pt), `:1028–1033` (61.91pt).
- Observed: identifier-list bullets push past margin.
- Required action: identifier wrap.
- Severity: M

## LAY-24 — §3.4 reconciliation table prose preface (NEW)

- Source: `main.tex:410–419` (32.16pt + 11.72pt).
- Observed: two overfulls in the prose immediately preceding the reconciliation table.
- Required action: rebreak the introductory sentence; do not touch the tabular.
- Severity: M

## LAY-03 / LAY-08 / LAY-09 — Residual margin overflow clusters

- Source: §5.2 cluster `main.tex:841–854`; §4.4 cluster `:555–589`; §5.2 cluster `:948–975`.
- Observed: 6+ overfulls in 12.46–70.84pt range; root cause = unwrapped path bullets and writeable-entity comma lists.
- Required action: continue the `\fp{}` / `\seqsplit{}` migration.
- Severity: L–M

## LAY-20 / LAY-21 — §6.4 underfull cluster + 52.64pt overfull

- Source: `main.tex:1330–1346` cluster (12 underfulls + 30.25pt overfull at 1331–1332); 52.64pt at 1333–1334.
- Observed: citation-pack `\citep{a, b, c, d}` paragraphs producing rivers and one tight overflow.
- Required action: split the longest `\citep{...}` pack across two calls separated by short prose, or move three keys into a "see also" footnote.
- Severity: M / L

## LAY-23 (continuation of LAY-14) — Font shape T1/lmtt/bx/n fallback

- Source: `main.tex:2265` (per log line 1082).
- Observed: `T1/lmtt/bx/n` substituted to `T1/lmtt/b/n`. Cosmetic.
- Required action: optional. If you want to silence it, reorder `\texttt{\textbf{...}}` so the fallback is unnecessary.
- Severity: L

## FIG-01 — Alt-text macros missing on every `\includegraphics` (joint with illustrator; writer-side action first)

- Source: 18 `\includegraphics` lines: `main.tex:287, 351, 535, 573, 804, 826, 1059, 1419, 1507, 1613, 1647, 1654, 2082, 2204, 2309, 2589, 2674` (and the logo include).
- Observed: zero `\Description{...}` macros, zero `pdftex` `/Alt` entries. PDF accessibility metadata absent.
- Required action: load `pdfcomment` or `tagpdf`, or define a simple `\Description` shim, and add a one-sentence alt-text per figure. Illustrator will then verify the text matches the asset.
- Severity: **H** (accessibility)

## FIG-07 — Caption-figure consistency for `fig:difficulty-taxonomy`

- Source: `main.tex:1419–1420` caption; mirrored at `main.md` §6.6.
- Observed: illustrator dropped the `Composite` column from `fig12-difficulty-taxonomy.svg` this cycle.
- Required action: re-read `main.tex:1420` and trim any reference to a 4th panel / composite axis. Mirror in `main.md`.
- Severity: M

## FIG-08 — Caption-figure consistency for `fig:eight-practices` vs §10 enumeration

- Source: `main.tex:2674` caption; §10 enumeration `:2348–2403`.
- Observed: §10 prose enumeration paraphrases the same eight practices the figure encodes. Pending human-author choice (a/b/c).
- Required action: pending human-author decision; if (b), have the caption explicitly defer to the figure.
- Severity: L
