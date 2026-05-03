# Layout Scrutinizer — Hand-back to Scientific Writer

Source: `docs/handbacks/layout-defect-registry.md` (PDF SHA-256
`62e68f6a5208814d47a51a8124bc7c7a836e7c9f3104951bc40a5c8dfda81384`,
build 2026-05-02T19:44:30Z, 42 pages, rebuilt by writer pass `537fae2`).

This is the **second** Layout Scrutinizer pass on the paper. The first
pass (PDF SHA `ba538ea0…`, 40 pages) filed LAY-01..LAY-18; the writer
pass between the two filed `f3ce051` (cluster A.2 + §6.8 insertion) and
`537fae2` (inline-citation promotion + bib corrections + Figure 13
caption macro fix). Each block below is one defect routed to the writer.
After remediation, rebuild via `make -C paper pdf` and request a Layout
Scrutinizer re-run; do **not** invoke `make arxiv` (CLAUDE.md rule 13).

---

## Disposition of LAY-01..LAY-18 (writer-owned)

- **LAY-01 — `\cref` `??`** : **[RESOLVED]**. Labels `sec:scope-non-goals`
  (`main.tex:242`), `sec:synthesis-limits` (`:989`), `sec:disc-validity`
  (`:1534`) all present. No reader action required.
- **LAY-02 — reconciliation-table mis-alignment** : **[PARTIAL → M]**.
  `\scriptsize` + `\newline` inside cells fixed cross-row visual bleed.
  4 small overfulls remain at lines 388–391 and 457; cosmetic only.
- **LAY-03 — bullet-list margin overflow §5.2** : **[PARTIAL → M]**.
  `\fp{...}` partial conversion took worst overflow from 168.80pt to
  70.84pt (lines 705–732). Finish the wrap pass on the surviving
  parenthetical `\texttt{}` runs.
- **LAY-04 — bullet-list margin overflow §6.5** : **[PARTIAL → M]**.
  Worst overflow at lines 1053–1068 is now 0.18pt. Residual 52.64pt at
  1087–1088 is in the surrounding paragraph (see LAY-21).
- **LAY-07 — redaction-tag overflow** : **[PARTIAL → L]**.
  `\seqsplit{\texttt{[REDACTED:…]}}` wrap removed the previous
  40.73pt / 55.48pt overflows. Markers still literal (rule 12 ✓).
- **LAY-08 — §4.4 bullet overflow** : **[PARTIAL → L]**. Down from four
  overfulls (max 105.99pt) to two (66.67pt + 12.76pt at lines 598–611).
- **LAY-09 — §5.2 multi-bullet block** : **[PARTIAL → M]**. Tied to
  LAY-03; same root cause; closing LAY-03 closes LAY-09.
- **LAY-10 — §10 eight-practices list** : **[PARTIAL → M]**. Three
  residual overfulls at lines 2098–2150; the 168.71pt at 2116–2127 is
  the single worst surviving margin overflow in the document. Cause
  unchanged: `experiments/paper-meta-process/raw_conversations
  (copy&paste, web)/T1-paper-structure-and-literature.md` path is not
  yet wrapped. Same fix shape as LAY-03.
- **LAY-11 — §6.7 single-line overfull** : **[RESOLVED at original
  site]**. The `\fp{RESEARCH-PROTOCOL.md}` caption-macro fix in `537fae2`
  removed the 7.79pt overfull. (The new 8.80pt overfull at 1136–1137 is
  the difficulty-taxonomy header row and is folded into LAY-06.)
- **LAY-14 — author-block font fallback** : **[UNCHANGED — L]**.
- **LAY-15 — `[h]`→`[ht]` placement promotions** : **[UNCHANGED — L]**.
- **LAY-17 — KPI table column-width pressure** : **[REGRESSED → M]**.
  Spider Farmer (lines 494–509, 55.48pt) and EcoFlow (643–654,
  113.47pt) tables both retain their pre-existing overflow magnitude.
  Severity raised L→M because of the family pattern with new LAY-19.
- **LAY-18 — §5.7 underfull rivers** : **[PARTIAL — UNCHANGED — L]**.

---

## NEW defects requiring writer action

## LAY-19 — Meta-process KPI tabular: 226.22pt overfull (worst in document)
- Page: ~14 (the §5.6 Meta-process effort-gap timeline)
- Source: `main.tex:872–891` (the `\begin{tabular}{llll} … \end{tabular}`
  block), mirrored at `main.md` §5.6 (search `Effort-gap timeline`).
- Observed: `Overfull \hbox (226.22418pt too wide) in paragraph at lines
  872--891`. The third column (`Key event`) carries multi-clause
  sentences such as
  `7-section paper structure from scratch`,
  `arXiv-ready pipeline; mirrors \texttt{main.md}`,
  `\texttt{dlr\_style.py}, \texttt{data/effort-gap.csv},
  \texttt{fig1-effort-gap.py}; Rule-14 compliance`,
  `Citizen-science / democratisation paragraph; \S{}5.7 updated`.
  These overflow the implicit `l` column width by ~7.97 cm.
- Required action: convert the four-column table from
  `\begin{tabular}{llll}` to
  `\begin{tabularx}{\textwidth}{l l >{\raggedright\arraybackslash}X r}`
  and let the `Key event` column wrap. Apply the same conversion to
  the LAY-17 sibling tables (Spider Farmer at 494–509 and EcoFlow at
  643–654) for consistency. **Do not** wrap with `\resizebox{\textwidth}{!}`.
  Mirror in `main.md`.
- Severity: **H**

## LAY-20 — §6.4 citation-pack underfull cluster + 52.64pt overfull
- Page: ~22
- Source: `main.tex:1078–1101`; mirrored at `main.md` §6.4 region.
- Observed: 12 underfull warnings (badness 1796–10000) within 24 source
  lines, plus an `Overfull \hbox (52.64pt too wide) at lines 1087--1088`.
  The paragraph is heavy on inline `\citep{a, b, c, d}` packs that drive
  both compression and stretching.
- Required action: rebreak the longest citation pack across two
  `\citep{...}` calls separated by a short prose phrase, OR downgrade
  three of the inline citations to a single-keyed `\citep{...}`
  followed by a "see also" footnote bundling the rest. Mirror in `.md`.
- Severity: **M**

## LAY-21 — §6.5 single-line overfull (bookkeeping for LAY-20)
- Page: ~17
- Source: `main.tex:1087–1088`.
- Observed: tied to LAY-20.
- Required action: a one-line rebreak should close it without disturbing
  the surrounding paragraph.
- Severity: **L**

## LAY-22 — Trailing-matter margin overflows (4 new occurrences)
- Pages: §11 / §12 / appendix tail (varies)
- Source: `main.tex:2213–2217 (37.70pt)`, `:2351–2359 (70.91pt)`,
  `:2364–2369 (32.31pt)`, `:2387–2392 (16.08pt)`.
- Observed: four overfull warnings in the trailing matter that were not
  previously flagged because the file was shorter (`f3ce051` insertion
  reflowed §10 + appendix onto pages where these overflows now matter).
  Worst is 70.91pt at 2351–2359.
- Required action: same shape as LAY-03 / LAY-10 — wrap long
  `\texttt{}`paths in `\fp{...}` (or `\seqsplit`); rebreak the long
  appendix-citation lines. Mirror in `.md`.
- Severity: **M**

---

## Cluster A.2 / §6.8 verification (no writer action — informational)

- All four new `\citep{}` calls in §1.4 (`vasile`, `becker`, `botero`,
  `grand`) plus the §6.8 `\citep{papp2015embedded}` resolve cleanly:
  zero `Citation … undefined` warnings in `main.log`.
- `\cref{sec:synthesis-evidence-asymmetry}` (target at `main.tex:1275`,
  references at `:208, :237`) resolves.
- `\textsuperscript{\ref{fn:hwre-cluster}}` (label at `:187`,
  reuses at `:198, :1285, :1296`) resolves.
- §1.4 cluster A.2 paragraph (`main.tex:165–208`) introduces **zero**
  new `\hbox` overruns despite the higher inline-citation density.
- Bibliography contains `papp2015embedded` (`main.bbl:94`).
  `vanwoudenberg2022hwhandbook` is bib-only-not-cited (intentional
  per the writer's footnote-not-inline policy for L-HW-RE-5);
  flagged here as a fact, not a defect.
- L-HW-RE-2 (ChipWhisperer) appears at `main.tex:175–177` as a
  `(L-HW-RE-2)\footnote{...}` reference and at `:1285` via
  `\textsuperscript{\ref{fn:hwre-cluster}}` reuse. No `\citep{}` call
  references the ChipWhisperer claim, consistent with its
  `[ai-confirmed-attempt-failed]` source-ladder status.

---

## Suggested writer remediation order (lowest-cost-of-fix first)

1. **LAY-19 + LAY-17 family** (one `tabularx` conversion repeated three
   times): closes the H-severity defect plus two M-severity defects.
2. **LAY-10 + LAY-22** (path-wrapping pass with `\fp{...}` /
   `\seqsplit`): closes the second-worst surviving cluster.
3. **LAY-03 + LAY-09** (residual `\texttt{}` parenthetical wrap):
   closes the §5.2 cluster.
4. **LAY-20 + LAY-21** (citation-pack rebreak): closes §6.4 rivers.
5. **LAY-04, LAY-08, LAY-18** (cosmetic): defer or batch with the above.

After remediation, rebuild via `make -C paper pdf` and request Stage 4
re-scrutiny. Constraint reminder: rule 11 mirror discipline applies to
every fix (mirror in `paper/main.md` in the same commit).
