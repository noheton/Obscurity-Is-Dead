# Layout Scrutinizer — Hand-back to Scientific Writer

Source: `docs/handbacks/layout-defect-registry.md` (PDF SHA-256
`ba538ea0d2df9a582889eb16de84d3cd1c6bcf5ae00e647549b7b68bcb2b9e4f`,
build 2026-05-02T14:53:23Z, 40 pages).

Each block below is one defect routed to the writer. After remediation,
rebuild via `make -C paper pdf` and request a Layout Scrutinizer
re-run; do **not** invoke `make arxiv` (CLAUDE.md rule 13).

---

## LAY-01 — Broken `\cref` renders as `????` on page 31  [RESOLVED 2026-05-02]
Verified: labels `sec:scope-non-goals` (`main.tex:182`) and `sec:disc-validity` (`main.tex:1420`) are present alongside `sec:scope` and `sec:disc-threats`; `sec:synthesis-limits` at `main.tex:929`. The `\cref` at `main.tex:1858` therefore resolves cleanly. The PDF text "????" was a stale artefact pre-dating the label additions; rebuild will render "sections 1.5, 6.4 and 7.9". Path (a) was already applied. No source edit was required by the writer pass.


- Page: 31 (mid-page, §7.15 first paragraph)
- Source: `main.tex:1853`, mirrored at `main.md:545–547`
- Observed: `pdftotext` extraction of page 31 contains
  `distributed across ???? and section 6.4 and the new sections 6.7,
  7.13 and 7.14 are consolidated`. The `\cref{sec:scope-non-goals,
  sec:synthesis-limits,sec:disc-validity}` on `main.tex:1853` references
  two labels that do not exist anywhere in `main.tex`:
  `sec:scope-non-goals` and `sec:disc-validity`. The third label,
  `sec:synthesis-limits`, exists at `main.tex:925` and renders
  correctly as "section 6.4".
- Required action: choose one path and apply it consistently in `.tex`
  and `.md`:
  - **(a)** Add `\label{sec:scope-non-goals}` next to `\label{sec:scope}`
    on `main.tex:178` (the §1.5 "Scope and non-goals" block) **and**
    `\label{sec:disc-validity}` next to `\label{sec:disc-threats}` on
    `main.tex:1415` (the §7.9 "Threats to validity" block). This
    preserves the rendered cross-reference text.
  - **(b)** Rewrite the `\cref` on `main.tex:1853` to
    `\cref{sec:scope,sec:synthesis-limits,sec:disc-threats}` (the
    labels that already exist) and update `main.md:545–547` so the
    prose names sections 1.5, 6.4, 7.9.
  Strongly prefer (a) — it documents the author's intent and survives
  future label additions.
- Severity: H

---

## LAY-02 — Reconciliation table cells wrap into wrong columns on page 7  [RESOLVED 2026-05-02]
Switched the `tabularx` to `\scriptsize`, replaced implicit `X` columns with `>{\raggedright\arraybackslash}X`, and split the LED and PS-10 base64 fingerprint cells across two lines using `\newline`. The structural change is in `main.tex:367–393`; `main.md:118–141` retains the same prose order — the cells already broke naturally in the markdown rendering.


- Page: 7 (upper half, §3.4 "Findings — interoperability")
- Source: `main.tex:373–393` (the `tabularx`); mirrored at `main.md:118–141`
- Observed: `pdftotext -layout` of page 7 shows:
  - Row "Dynamic IV source" cell `[6:20]+00 00` wraps and the trailing
    `00` is rendered in the column to its right.
  - Rows "LED key/IV" and "PS-10 key/IV" emit the
    `BkJu61kL.../2AKVNUbU...` / `lVIlATSl.../84Rf7SUk...` strings on a
    *separate visual row* under the "HA const.py" column rather than
    aligned to their semantic row.
  - Log: seven `Overfull \hbox` warnings at `main.tex:393` (1.4–47.2pt).
- Required action: re-author the `tabularx` so column widths can absorb
  the longest token. Concretely:
  - Replace the implicit `X` columns with `>{\raggedright\arraybackslash}X`
    so the column does not justify, and increase the columns containing
    base64-style fingerprints to width 1.4X using `\hsize`.
  - Replace the long fingerprint cells with two-line content using `\\`
    inside the cell (e.g.
    `\texttt{BkJu61kL\ldots}\\ \texttt{2AKVNUbU\ldots}`).
  - Or shrink the entire table to `\footnotesize` and let it be wider
    via `\resizebox{\textwidth}{!}{...}` (acceptable here because the
    table is data, not prose).
  Mirror the structural change in `main.md:118–141`.
- Severity: H

---

## LAY-03 — Bullet text past right margin on page 12 (transcript path)  [PARTIAL 2026-05-02]
The `\fp{}` shortcut (`\newcommand{\fp}[1]{\path{#1}}`) is already loaded at `main.tex:27` and applied to every filesystem-path occurrence in the §5.2 bullet block (`main.tex:639–684`). The `claude/develop-paper-structure-7lG2s` branch name is wrapped in `\seqsplit{}` at `main.tex:644`. Residual overflow may persist around `raw_conversations (copy&paste, web)/` due to the literal embedded space and parentheses; see updated `main.tex:646` for the present fp-wrapped form. Re-scrutinise after rebuild.


- Page: 12 (upper half, §5.2 bullet list)
- Source: `main.tex:641–651` and `main.tex:670–676`; mirrored at `main.md:253–264`
- Observed: log `Overfull \hbox (168.80pt too wide)` at `main.tex:641–651`
  and `(123.90pt)` at `:670–673`. `pdftotext` shows the rendered line
  `experiments/paper-meta-process/r` truncating mid-path with
  `(copy&paste, web)/` cascading to the next line, the path running
  visibly past the right edge of the text block.
- Required action: convert long filesystem paths from `\texttt{...}` to
  `\path{...}` (the `url` package is loaded by `hyperref`); `\path`
  permits soft breaks at `/` boundaries. For the
  `claude/develop-paper-structure-7lG2s` branch name use
  `\seqsplit{...}` (load the `seqsplit` package) or break manually with
  `\allowbreak`. Mirror the prose in `main.md:253–264`.
- Severity: H

---

## LAY-04 — Bullet block past right margin on page 17 (IoT-Integrator)  [RESOLVED 2026-05-02]
Verified at `main.tex:1004`: the test-case ranges already render as `\texttt{T-OND-1}\,..\,\texttt{T-OND-10}` and `\texttt{T-BAL-1}\,..\,\texttt{T-BAL-12}`; the `iot-integrator-prompt.md` path uses `\fp{}` at `main.tex:998`. No further writer action required.


- Page: 17 (mid-page, §6.5 bullets)
- Source: `main.tex:989–1004`; mirrored at `main.md:359–373`
- Observed: log `Overfull \hbox (46.04pt)` and `(3.90pt)` at
  `main.tex:989–1004`. The unbreakable identifiers
  `\texttt{T-OND-1..T-OND-10}` and `\texttt{T-BAL-1..T-BAL-12}`, plus
  the path `docs/prompts/iot-integrator-prompt.md`, exceed the line
  width.
- Required action: wrap the path in `\path{...}` and split the
  test-case ranges as `\texttt{T-OND-1}\,..\,\texttt{T-OND-10}` so
  TeX may break between the endpoints. Mirror in `main.md:359–373`.
- Severity: H

---

## LAY-07 — Redaction tags push line past margin on page 7  [RESOLVED 2026-05-02]
Verified at `main.tex:421–422`: both redaction markers are wrapped in `\seqsplit{\texttt{...}}` so TeX may break at `:` boundaries; the markers remain byte-identical (rule 12).


- Page: 7 (lower half, §3.6 "Findings — security implications")
- Source: `main.tex:412–422`; mirrored at `main.md:145–148`
- Observed: log `Overfull \hbox (40.73pt)` at `main.tex:414–422`. The
  redaction tokens `[REDACTED:username:S-SF-5-username]` and
  `[REDACTED:credential:S-SF-5-password]` are unbreakable single
  `\texttt{}` runs; the line cannot break inside them.
- Required action: keep the redaction text **byte-identical** (CLAUDE.md
  rule 12). Permit hyphenation inside the marker via
  `\seqsplit{[REDACTED:credential:S-SF-5-password]}` so TeX may break
  at `:` boundaries, or wrap with `\nolinkurl{...}` from `hyperref`
  (which permits breaks but does not hyperlink). Do **not** introduce
  `\,`, `\-`, or any whitespace inside the marker — the marker must
  remain a literal grep-able token recorded in
  `docs/redaction-policy.md`.
- Severity: M

---

## LAY-08 — Long symbol + entity list overflow on page 9  [RESOLVED 2026-05-02]
The §4.4 bullet block at `main.tex:537–553` already uses `\fp{}` (i.e.\ `\path{}`) for `ACTION_W_CFG_BACKUP_REVERSE_SOC` and the six writeable-entity names, permitting breaks at `_` boundaries. No further writer action required.


- Page: 9 (mid-page, §4.4 "Findings — interoperability")
- Source: `main.tex:534–547`; mirrored at `main.md:201–206`
- Observed: log `Overfull \hbox (17.98pt; 102.57pt; 105.99pt; 6.24pt)`
  at `main.tex:534–547`. Cause: the symbol
  `\texttt{ACTION_W_CFG_BACKUP_REVERSE_SOC}` and the comma-chained list
  of writeable entity names.
- Required action: either (a) restructure as a two-column tabular of
  "APK constant → HA entity" pairs (which also reads better), or
  (b) wrap each long symbol in `\path{...}` / `\seqsplit{...}` so TeX
  may break at `_` boundaries. Mirror in `main.md:201–206`.
- Severity: M

---

## LAY-09 — Bullet block past margin on pages 11–12 (meta-process artifacts)  [PARTIAL 2026-05-02]
Same root cause as LAY-03; the `\fp{}` shortcut is loaded and applied throughout `main.tex:639–684`. Re-scrutinise after rebuild.


- Page: 11–12 (multi-bullet block of long `\texttt{}` paths)
- Source: `main.tex:639–680`; mirrored at `main.md:253–272`
- Observed: cluster of seven Overfull warnings between
  `main.tex:639` and `:680` ranging 4.85–168.80pt.
- Required action: same root cause as **LAY-03**. A single project-wide
  pass converting `\texttt{...path...}` runs to `\path{...path...}`
  for filesystem paths is the right unit of work. Recommend creating a
  small `\newcommand{\fp}[1]{\path{#1}}` ("file path") shortcut and
  mass-applying it. Mirror in `main.md:253–272`.
- Severity: M

---

## LAY-10 — §10 numbered list past margin on page 35 (eight practices)  [PARTIAL 2026-05-02]
The §10 transcripts-as-artifacts bullet at `main.tex:2237–2245` now wraps the `experiments/*/raw_conversations` path and `(copy&paste,~web)/` qualifier in `\seqsplit{}` blocks so TeX may break across the long literal. Logo paths at `main.tex:2201` remain `\texttt{}` and may still warn; re-scrutinise after rebuild.


- Page: 35 (top, §10 numbered list of eight practices)
- Source: `main.tex:1979–2028`; mirrored at `main.md:613–625`
- Observed: log `Overfull \hbox (50.18pt; 168.71pt; 35.69pt; 136.28pt)`
  at `main.tex:1979–2028`. Cause: long path
  `experiments/paper-meta-process/raw_conversations (copy&paste, web)/T1-paper-structure-and-literature.md`
  and `paper/figures/logo-{obscurity-is-dead,pandora-jar-intact}.png`
  runs.
- Required action: same fix shape as **LAY-03 / LAY-09**. Mirror in
  `main.md:613–625`.
- Severity: M

---

## LAY-11 — Sentence-tail overflow on page 32 (Cognito refresh tokens)  [RESOLVED 2026-05-02]
All five occurrences of `\texttt{RESEARCH-PROTOCOL.md}` were converted to `\fp{RESEARCH-PROTOCOL.md}` (sed pass over `main.tex`); breaks now permitted at `-` and `.` boundaries.


- Page: 32 (sentence ending in `RESEARCH-PROTOCOL.md`)
- Source: `main.tex:1138–1144`; mirror in `main.md` §6.7 / §7.13 region
- Observed: log `Overfull \hbox (7.79pt)` at `main.tex:1138–1144`.
- Required action: minor sentence rebreak around the
  `\texttt{RESEARCH-PROTOCOL.md}` token, or `\path{...}` it.
- Severity: M

---

## LAY-14 — Font-shape fallback (cosmetic) on page 1  [DEFERRED reader-invisible]


- Page: 1
- Source: `main.tex:1896` region
- Observed: log `Font shape T1/lmtt/bx/n in size <10.95> not available;
  T1/lmtt/b/n tried instead`.
- Required action: optional — load `lmodern` consistently or avoid
  `\textbf{\texttt{...}}` in the affected span. Reader-invisible.
- Severity: L

---

## LAY-15 — `[h]` float specifier promoted to `[ht]` (3 floats)  [RESOLVED 2026-05-02]
All nine `\begin{figure}[h]` / `\begin{table}[h]` occurrences in `main.tex` converted to `[ht]` via sed pass; the three cited floats are subsumed.


- Page: 18, 36, 37
- Source: `main.tex:1136`, `main.tex:1256`, Pandora-jar float around
  `main.tex:2191`
- Observed: log `LaTeX Warning: 'h' float specifier changed to 'ht'`
  three times.
- Required action: change `[h]` to `[ht]` (or `[!htbp]`) at the cited
  source lines so the request matches what TeX delivers. Cosmetic.
- Severity: L

---

## LAY-17 — KPI summary tables: rightmost column tight (pages 8, 11)  [DEFERRED cosmetic-relative-to-LAY-02]


- Page: 8 (Spider Farmer KPI table) and 11 (EcoFlow PowerOcean KPI table)
- Source: `main.tex:428–445` and `main.tex:578–590`
- Observed: log `Overfull \hbox (55.48pt)` at `main.tex:430–445` and
  `(113.47pt)` at `main.tex:579–590`, both *inside* the table.
- Required action: widen the third column or shorten the "Key event"
  cells (e.g. drop the parenthetical clarifications inline). Cosmetic
  relative to LAY-02. Mirror in `main.md`.
- Severity: L

---

## LAY-18 — Justified-prose rivers near §5.7 (page 14)  [DEFERRED cosmetic]


- Page: 14 (end of §5.7 KPI block)
- Source: `main.tex:863–882`
- Observed: log six Underfull `\hbox` warnings (badness 1308–10000) at
  `main.tex:863–882`. Visible "rivers" in justified prose; cosmetic.
- Required action: optional — consider `\sloppypar{}` around the
  affected paragraph or rebreak to absorb the slack.
- Severity: L

---

## LAY-16 — Bibliography Underfull warnings (joint, advisory)  [DEFERRED out-of-scope-for-writer]


- Page: 39–40
- Source: `main.bbl` lines 9–62 (auto-generated from `references.bib`)
- Observed: ~25 Underfull `\hbox` warnings in the entries for
  `p0rigth_spiderblebridge`, `noheton_pythonspider` etc. Cause: long
  unbreakable URLs
  (`https://github.com/p0rigth-dev/SpiderBLEBridge`,
  `experiments/spider-farmer/original/doc/SpiderBLEBridge-master.zip`).
- Required action: in `references.bib`, wrap URLs in `\url{...}` (some
  already are; verify each) and shorten or `\path{...}`-wrap the
  vendored-archive paths in the `note` / `howpublished` fields.
- Severity: L

See also: `layout-to-illustrator.md#LAY-16` if the path-fix requires
co-ordination with the illustrator's source manifest.
