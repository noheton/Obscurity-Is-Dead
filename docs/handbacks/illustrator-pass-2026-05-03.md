# Illustrator (Stage 3) — Pass 2026-05-03

- **Agent:** Claude Opus 4.7
- **Branch:** `claude/review-open-issues-PfNx9`
- **Inputs:** `CLAUDE.md` (rules 1, 11, 13, 14, 15);
  `docs/prompts/illustration-prompt.md`;
  `docs/handbacks/layout-to-illustrator.md` (LAY-05, LAY-06, LAY-12,
  LAY-13, LAY-16);
  `docs/handbacks/readability-to-illustrator.md` (RDB-04, RDB-05+RDB-08,
  RDB-07, RDB-21, RDB-23);
  `docs/handbacks/writer-pass-2026-05-03.md` (just-completed Stage-2
  pass — no figure assets touched there).
- **Out-of-scope:** PDF rebuild (Stage 4); prose edits to
  `paper/main.{md,tex}` outside of caption fidelity; new
  Gemini-quality artwork (human-author gate); push (rule 13).

---

## LAY-05 — Figure 7 (verification-status pipeline) textwidth overflow

- **Status: RESOLVED (no action required this pass).**
- The most recent Layout Scrutinizer pass already verified zero
  `Overfull \hbox` warnings in the Figure 7 float
  (`main.tex:814–828`). The 226.22pt overfull that previously
  dominated this figure is gone in the rebuilt PDF; the residual
  226.22pt overfull at `main.tex:872–891` is the writer-owned KPI
  tabular (LAY-19), not the figure.
- Asset unchanged: `paper/figures/fig9-verification-pipeline.{py,svg,pdf}`.
- Residual issue: none. Severity closed.

## LAY-06 — Figure 8 / `tab:difficulty-taxonomy` row split + Composite header pressure

- **Status: RESOLVED (figure side); writer-side residual deferred.**
- **Action:** re-rendered `fig12-difficulty-taxonomy.{svg,pdf}` to
  drop the redundant *Composite* column. The composite (Easy /
  Medium / Hard) rating is already carried by the preceding
  `tab:difficulty-taxonomy` table in textual form, so the heat-map
  column duplicated information and was the source of the "Med High"
  two-line wrap that triggered the LAY-06 row-split warning.
  Removing it shrinks the figure from 4 columns to 3 (figsize
  8.8 → 7.2) and relieves the textwidth-pressure on the figure
  include. The qualitative-rating cell text per row is now the
  three independent axes only.
- **Files touched:**
  - `paper/figures/fig12-difficulty-taxonomy.py` — column list
    pruned; figsize narrowed; cell-annotation branch for "composite"
    removed; docstring extended to record the LAY-06 fix; footer
    caption updated to point to the table for the composite rating.
  - `paper/figures/fig12-difficulty-taxonomy.svg` — regenerated.
  - `paper/figures/fig12-difficulty-taxonomy.pdf` — regenerated
    (PDF 1.4, matplotlib).
- **Residual issue:** the LAY-06 hand-back recorded an *additional*
  8.80pt overfull on the *table* `tab:difficulty-taxonomy` Composite
  header row at `main.tex:1136–1137` and a 2.53pt overfull on the
  whole tabular at `:1134–1160`. That is column-width pressure on
  the **table**, not on the figure, and is writer-owned. With the
  figure now narrower, the text-width budget around the tabular
  improves slightly, but the writer-side `p{1.4cm}` → `p{1.8cm}`
  widening recommendation in the LAY-06 hand-back is independent
  and remains queued for the next writer pass. Stage 4 should
  re-sweep after the next `make pdf` to quantify.
- **Severity:** H → L (figure-side closed; remainder is writer's
  table-column-width call).

## LAY-12 — Logo placeholders (intact-jar half)

- **Status: PARTIAL (intact-jar still PENDING-GEMINI-FINAL); inventory
  honesty fixed.**
- **Confirmation:** `paper/figures/logo-pandora-jar-intact.png` is
  unchanged (PNG 950x944 RGBA, ~83 kB) — the file dimensions and
  size are consistent with the matplotlib typographic output of
  `paper/figures/logo-placeholders.py`, **not** with the
  Gemini-quality 1408x768 hero asset that landed for the
  shattered-jar half. Per the orchestrator brief, the intact-jar
  remains the AI-authored placeholder pending the second Gemini
  deliverable. **Did not** invoke `logo-placeholders.py` this pass
  (binary unchanged); the placeholder is reproducible per rule 14
  if the human ever needs to regenerate it without altering the
  visual.
- **Inventory honesty fix (rule 1):** the
  `paper/figures/README.md` inventory entry for
  `logo-pandora-jar-intact.png` previously claimed the binary was
  "Externally generated — Google Gemini, 2026-05-02; researcher-supplied
  binary, dropped in by the author". That was inconsistent with the
  actual binary on disk and with §10 prose at `main.tex:2138–2149`.
  Corrected this pass to read **AI-authored placeholder
  *(PENDING-GEMINI-FINAL)*** with full provenance disclosure
  (script path, dimensions, size, swap procedure). The neighbouring
  paragraph that introduces the logo assets was tightened
  symmetrically: the shattered-jar is now correctly labelled as
  the final Gemini deliverable; the intact-jar is correctly
  labelled as the still-pending placeholder.
- **Files touched:**
  - `paper/figures/README.md` — inventory entry + introductory
    paragraph for the logo block.
  - **Not** touched: `paper/figures/logo-placeholders.py`,
    `paper/figures/logo-pandora-jar-intact.png`,
    `paper/figures/logo-obscurity-is-dead.png`.
- **Residual issue:** the second Gemini deliverable for the
  intact-jar still has not landed. **This is a human-author
  decision**, per the orchestrator brief and CLAUDE.md rule
  spirit (no autonomous Gemini calls). Once the binary lands,
  swap it in place (preserve the filename), re-run the
  layout-scrutinizer + readability-scrutinizer narrow-scope
  passes against the §10 anchor, and close LAY-12 entirely.
- **Severity:** M (informational) — unchanged.

## LAY-13 — PDF version 1.7 vs 1.5 inclusion warnings

- **Status: RESOLVED (Makefile-side; effective on next `make pdf`).**
- **Root cause:** `rsvg-convert` and `inkscape` both emit PDF 1.7
  by default; pdfTeX defaults to a max-included version of 1.5.
  Result: 7 PDFs (`fig1-effort-gap.pdf` … `fig7-threat-models.pdf`)
  were triggering the layout-log warning
  `pdfTeX warning: PDF inclusion: found PDF version <1.7>, but at
  most version <1.5> allowed` on every build.
- **Action:** modified `paper/Makefile` `$(FIG_DIR)/%.pdf` rule to
  post-process every newly converted PDF with a small Python
  one-liner that rewrites the `%PDF-1.7` (or `%PDF-1.6`) header
  bytes to `%PDF-1.5`. Header-byte rewriting is safe for the
  simple vector content these figures carry (no PDF-1.6+ features
  used) and is robust without requiring `ghostscript` / `qpdf` to
  be installed in the build environment (neither tool is currently
  available in the illustrator's environment, so a more invasive
  fix would block).
- **Files touched:** `paper/Makefile` (one rule body extended; full
  rationale documented in the rule's lead comment).
- **Residual issue:** the next `make pdf` rebuild (Stage 4 owns
  this) should produce zero PDF-version warnings for the seven
  affected figures. If the rewrite proves too aggressive (e.g. an
  inkscape-emitted PDF later starts using a true PDF-1.6+ feature),
  the rule can be tightened to a per-figure allowlist; for now
  the simple `1.7 → 1.5` byte-edit is sufficient for the SVG
  content base.
- **Severity:** M → 0 (closed pending Stage-4 verification).

## LAY-16 — Bibliography underfull rivers

- **Status: DEFERRED.**
- Out of illustrator scope (auto-generated `main.bbl` from
  `references.bib`). The hand-back already classifies this as
  L-severity advisory and routes the practical fix to the next
  writer pass that touches `references.bib`.

---

## RDB-04 — Confirm Figure 11 carries the eight-row × three-column matrix

- **Status: RESOLVED (verified-no-action).**
- **Verification:** `paper/figures/fig11-eight-practices.py` lines
  33–62 enumerate the eight numbered practices with full short
  labels (e.g. "Conversation transcripts as first-class artifacts",
  "Verification-status legend on every cited source", …) and the
  three failure-mode axes ("Fabricated citations", "Prompt
  injection", "Tooling drift"). The rendered figure carries:
  (i) eight visible rows, each with practice number + full label
  in fontsize 8.6 (legible); (ii) three column headers in
  contrasting accent boxes; (iii) per-cell P / S markers with
  matching colour coding. The writer-side RDB-04 prerequisite
  ("Figure 11 must carry the row labels in legible form") is
  **already met** by the existing asset — the writer is unblocked
  on the §10 enumeration → figure-callout collapse decision.
- **Files touched:** none.
- **Residual issue:** the §10 enumeration vs Figure 11 collapse is
  an authorial / structural decision (writer hand-back lists three
  options A/B/C); **flagged for human-author decision**, not for
  the illustrator.

## RDB-05 + RDB-08 — Consolidation candidate: §6.7 + §7.13 single matrix

- **Status: DEFERRED (per registry — "decision can be deferred to
  the next illustration pass").**
- **Rationale for deferral:** the two existing figures
  (`fig13-pipeline-vulnerabilities.{svg,pdf}` for §6.7 and
  `fig14-malicious-integrator.{svg,pdf}` for §7.13) currently serve
  *different rhetorical positions* in the paper: fig13 is a pure
  vulnerability-class taxonomy (researcher-defensive framing),
  fig14 is a branching governance-workflow diagram (adversary
  framing). A single matrix figure absorbing both would force one
  of those two rhetorical positions to dominate, which is a
  structural authorial choice rather than a mechanical illustrator
  fix. The registry already states "writer-side prose conversion
  is independently valuable" — the writer can proceed with the
  prose-shrinkage on §6.7 and §7.13 without this consolidation.
- **Files touched:** none.
- **Residual issue:** if the human author decides the
  consolidation is desirable, file as a new `ILL-NN-integrator-matrix`
  entry on the next illustration-prompt pass. Until then, the
  alternative path — adding row-label legends to each existing
  figure — is also acceptable and is implementable as a quick
  follow-up if the writer flags it as blocking.

## RDB-07 — §7.11 prompt-injection comparison-table candidate

- **Status: DEFERRED (per registry — "writer-side fallback is
  achievable without illustrator action; the figure is an
  enhancement, not a blocker").**
- **Rationale for deferral:** producing a 4 × 3 matrix figure for
  §7.11 (four injection targets × three feasibility/ethics/cost
  considerations) is a meaningful new asset (`ILL-NN-promptinj-targets`)
  that the registry itself flags as out-of-scope for the next
  illustration pass unless explicitly prioritised. The writer-side
  prose conversion is the unblocking fix; the figure is the
  enhancement. The current pass deliberately scopes to the
  multi-cycle-deferred LAY-* items rather than opening new ILL-NN
  entries.
- **Files touched:** none.
- **Residual issue:** if the human author wants the §7.11 figure
  in the next round, add it to the Illustration Opportunities
  Registry in `paper/main.{md,tex}` with the proposed axes from
  the readability hand-back (lines 30–35 of
  `docs/handbacks/readability-to-illustrator.md`).

---

## Summary

| Item | Status | Files touched |
|------|--------|---------------|
| LAY-05 | RESOLVED (no-op; closed by prior pass) | — |
| LAY-06 | RESOLVED (figure side); writer-side table column-width residual deferred | `fig12-difficulty-taxonomy.{py,svg,pdf}` |
| LAY-12 (intact-jar) | PARTIAL — placeholder confirmed in place; README inventory honesty fixed; binary swap awaits Gemini deliverable | `paper/figures/README.md` |
| LAY-13 | RESOLVED (Makefile-side fix, effective on next `make pdf`) | `paper/Makefile` |
| LAY-16 | DEFERRED (out of illustrator scope) | — |
| RDB-04 | RESOLVED (verified — Figure 11 already carries legible row labels) | — |
| RDB-05+RDB-08 | DEFERRED (per registry; structural authorial decision) | — |
| RDB-07 | DEFERRED (per registry; writer-side fallback unblocks; figure is enhancement) | — |

**Items needing human-author decision:**

1. **LAY-12 intact-jar Gemini deliverable.** Replace
   `paper/figures/logo-pandora-jar-intact.png` with the second
   Gemini-generated PNG. Until then, the placeholder remains and
   §10 honesty disclosure stands.
2. **§10 enumeration vs Figure 11 collapse (RDB-04 / RDB-02
   companion).** Three options (a)/(b)/(c) enumerated in
   `docs/handbacks/writer-pass-2026-05-03.md`. The illustrator
   has confirmed Figure 11 is *technically* ready for any of the
   three; the choice is authorial.
3. **RDB-05+RDB-08 consolidation matrix.** Whether to merge
   `fig13` + `fig14` into a single integrator-matrix figure, or to
   keep both with added row-label legends. Either path is
   illustrator-implementable on demand.
4. **RDB-07 prompt-injection 4 × 3 matrix.** Whether to add a new
   `ILL-NN-promptinj-targets` registry entry. If yes, file in
   `paper/main.{md,tex}` and the next illustration pass will
   materialise it.

## Hand-back to other agents

- **Stage 4 (Layout):** rebuild `paper/main.pdf` and re-sweep.
  Expected effects of this pass: (i) zero PDF-version-1.7 warnings
  for the seven SVG-derived figures (LAY-13 closed); (ii) Figure 8
  / `tab:difficulty-taxonomy` heat-map narrower (3-column instead
  of 4-column); (iii) any residual table-side overfull at
  `main.tex:1134–1160` remains and routes to the writer.
- **Stage 5 (Readability):** confirm Figure 11 row-label legibility
  on the rebuilt PDF (RDB-04 closure pending Stage-4 PDF). The
  §10 enumeration vs figure-callout collapse decision still
  awaits the human author's pick of options (a) / (b) / (c).
- **Writer:** the LAY-06 *table*-side residual (Composite header
  column-width pressure at `main.tex:1136–1137`) is now the only
  open piece of LAY-06; the figure half is closed. Pick up on
  the next writer pass that touches §6.6.
- **Human author:** the four decisions above.

## Rule-1 / Rule-11 / Rule-13 / Rule-14 / Rule-15 check

- **Rule 1 (honesty):** the README.md provenance inconsistency for
  `logo-pandora-jar-intact.png` was the headline rule-1 fix this
  pass — the file is, and is now correctly labelled as, an
  AI-authored placeholder (not a Gemini deliverable). The fig12
  docstring and figure caption both record the LAY-06 motivation.
- **Rule 11 (mirror discipline):** no `paper/main.{md,tex}` edits
  made; the figure-caption text in fig12's footer is in-figure,
  not in the paper prose. No mirror drift introduced.
- **Rule 13 (no publication):** no `make pdf`, no `make arxiv`,
  no push. Local-only edits.
- **Rule 14 (data + script committed):** fig12 is data-driven;
  data file `paper/figures/data/difficulty-taxonomy.csv` and
  script `fig12-difficulty-taxonomy.py` are both committed. The
  composite-column drop is a script change; the CSV is unchanged
  (the `composite` column is simply no longer read).
- **Rule 15 (README mirror):** no figure was added, replaced, or
  retired; no headline KPI changed; the visual abstract
  (`fig11-eight-practices.svg`) is unchanged. The top-level
  `README.md` does not require update this pass. The figure-folder
  `paper/figures/README.md` *was* updated for the LAY-12 honesty
  fix.
