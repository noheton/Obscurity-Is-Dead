# Illustrator (Stage 3) — Design-consistency materialisation pass 2026-05-03

- **Agent:** Claude Opus 4.7 (`claude-opus-4-7`).
- **Branch:** `claude/review-open-issues-PfNx9` (parent-session edit; no
  fresh dispatch from the orchestrator — operator brief mid-run).
- **Trigger.** Human-author guidance mid-pipeline:
  *"achte aber auf Konsistenz im Design"* — design consistency across
  the figure set is non-negotiable. Concrete implications: single
  visual language across all figures, hard 9 pt body / 10.5 pt
  row-label floor, palette restricted to `dlr_style` + Tol-bright
  CB-safe accents, hatched fill paired with rose `#ee6677` whenever
  the rose carries a warning / adversarial / legacy / exclusion
  semantic, hero / visual-abstract `fig11-eight-practices` as the
  design anchor.
- **Inputs:** `CLAUDE.md`; `docs/prompts/illustration-prompt.md`;
  `docs/handbacks/illustrator-pass-2026-05-03-overhaul.md`;
  `docs/handbacks/illustrator-pass-2026-05-03.md`;
  `docs/handbacks/layout-to-illustrator.md` (round 3 — FIG-11
  carry-forward; deferred fig8 / fig15 / fig16 set);
  `docs/handbacks/readability-to-illustrator.md`;
  `paper/figures/dlr_style.py`;
  every `paper/figures/fig*.py` script's docstring.
- **Out of scope (rule 13):** `make pdf`, `make arxiv`, push.
- **Out of scope this pass:** prose edits to `paper/main.{md,tex}`;
  any Gemini-quality artwork generation; consolidation of
  `fig13` + `fig14` into a single integrator matrix (DEFERRED on
  human-author decision); creation of the `ILL-NN-promptinj-targets`
  4×3 matrix figure (DEFERRED on human-author decision).

---

## A. Cross-figure consistency audit

Read every script docstring + every `fontsize=` / `color=` / hex
literal across `paper/figures/fig*.py`. Compared against the design
anchor (`fig11-eight-practices`).

| Fig | Palette drift | Typography drift (under 9 pt body / 10.5 pt row floor) | Disposition |
|----|---------------|--------------------------------------------------------|-------------|
| 1 effort-gap | none | tick `7.5–8.5`, label `8`, legend `8.5` — under floor | **KEEP (author-accepted; rule: do not regress)** — drift logged but not edited |
| 2-5 (manual SVG) | n/a | n/a | KEEP — rule-14-exempt; manually drawn |
| 6 dual-use | none | OK | KEEP |
| 7 threat-models | none | OK | KEEP |
| 8 ecoflow-surfaces | none (rose `#ee6677` + hatched fill — matches anchor) | OK | KEEP |
| **9 verification-pipeline** | none | **stage-promotion arrow labels at 8.5 pt — under floor** | **REWORK — bumped 8.5 → 9.0** |
| **10 stage-effort** | none | **legend + rule-1 annotation at 8.5 pt — under floor** | **REWORK — bumped 8.5 → 9.0** |
| 11 eight-practices (HERO) | none (anchor) | OK (anchor) | KEEP |
| 12 difficulty-taxonomy | none | OK | KEEP |
| **13 pipeline-vulnerabilities** | none | **central-italic-sub `8`, outer-node sub `8.2`, footer `8.6` — under floor** | **REWORK — bumped to 9.0** |
| 14 malicious-integrator | none | OK | KEEP |
| **15 apk-mass-probing** | none (recoloured 2026-05-03 morning) | **stage-sub `8.2`, cost brackets `8` / `8.6`, panel body `8.4`, footer `8.6` — under floor** | **REWORK — bumped all to 9.0** |
| **16 scope-limitations** | none (already CB-safe) | **footer `8.6` — under floor** | **REWORK — bumped to 9.0** |
| logos | n/a | n/a | KEEP — intact-jar pending human Gemini deliverable |

### What was *not* drift

- Palette: every script imports from `dlr_style.py` (single source of
  truth) and uses only the brand colours plus the four
  CB-safe Tol-bright accents (`#4477aa`, `#228833`, `#aa7733`,
  `#ee6677`). No raw matplotlib defaults survive in any committed
  script. The rose `#ee6677` is consistently paired with a hatched
  fill across `fig8`, `fig14`, `fig16` — semantic of "warning /
  legacy / adversarial / named-exclusion" preserved.
- Stroke / arrowhead: every figure uses
  `FancyArrowPatch(..., arrowstyle="-|>", mutation_scale=12-14)` —
  consistent.
- Categorical glyphs: P/S shape-redundancy (introduced by `fig11`)
  is the only categorical encoding in the figure set; it does not
  recur elsewhere, so no re-application required.

### What *was* drift

A typography-floor drift across **five** figures (fig9, fig10,
fig13, fig15, fig16). All cases are body / sub-label / annotation
text below the 9 pt floor that `fig11` establishes. No palette
drift, no stroke-style drift, no categorical-encoding drift.

### What was logged but **not edited** (fig1)

`fig1-effort-gap.py` carries 7.5 / 8 / 8.5 pt labels in several
places. The author has explicitly accepted this figure; the prior
overhaul's "REWORK" disposition list excluded fig1; standing rule:
do not regress an author-accepted asset on a consistency pass. The
drift is logged here so the *next* round of design-consistency
work, if dispatched, has it on record. Recommend: only touch fig1
on explicit human-author request.

---

## B. Edits applied this pass

All edits are typography-floor only: font-size lifts to clear the
9 pt body / 10.5 pt row-label minimum that `fig11` sets. **No
palette change, no layout change, no caption change, no
LaTeX-label change.** All `\cref{...}` and `\ref{...}` calls in
`paper/main.{md,tex}` continue to resolve unchanged.

### fig9-verification-pipeline.py

- Line ~120 + ~155: stage-promotion arrow labels 8.5 → 9.0 pt
  (two occurrences; `replace_all`-style edit).
- Docstring extended with a short note recording the
  design-consistency motivation.
- Regenerated: `fig9-verification-pipeline.{svg,pdf}`.

### fig10-stage-effort.py

- Line ~100: `ax_a.legend(fontsize=8.5, ...)` → `9.0`.
- Line ~108: rule-1 annotation `fontsize=8.5` → `9.0`.
- Docstring extended.
- Regenerated: `fig10-stage-effort.{svg,pdf}`.

### fig13-pipeline-vulnerabilities.py

- Line ~66: central-node italic-sub-label `8` → `9.0`.
- Line ~88: outer-node sub-label `8.2` → `9.0`.
- Line ~103: footer caption `8.6` → `9.0`.
- Docstring extended (was previously laconic — now records what
  changed and why per CLAUDE.md rule 1).
- Regenerated: `fig13-pipeline-vulnerabilities.{svg,pdf}`.

### fig15-apk-mass-probing.py

- Stage `sub` label inside `stage()` helper: `8.2` → `9.0`.
- Five cost-tier annotations across the pipeline: `8` / `8.6` →
  `9.0` (uniform).
- Empirical-rates panel body (two `text` calls): `8.4` → `9.0`.
- Empirical-rates panel italic line: `8.4` → `9.0`.
- Footer mitigation note: `8.6` → `9.0`.
- Docstring extended.
- Regenerated: `fig15-apk-mass-probing.{svg,pdf}`.

### fig16-scope-limitations.py

- Footer caption: `8.6` → `9.0`.
- Docstring extended.
- Regenerated: `fig16-scope-limitations.{svg,pdf}`.

### `paper/figures/README.md`

- New section **"Design-system defaults (apply to every figure)"**
  appended after the *Template for future data-driven figures*
  block. Records, in one place, the palette / typography /
  stroke / categorical-glyph / hatch convention so the next
  illustrator pass inherits the defaults (per the human author's
  brief item 3 — *"document the palette + typography defaults you
  established for that path"*). The section explicitly names
  `fig11-eight-practices` as the design anchor, calls out the
  9 pt body / 10.5 pt row-label floor, and lists the banned
  colours (pure red `#c0392b`, pink/red `#fadbd8`, raw matplotlib
  defaults, traffic-light pairings).

---

## C. Files touched

```
paper/figures/fig9-verification-pipeline.py        (docstring + 2 fontsize bumps)
paper/figures/fig9-verification-pipeline.svg       (regenerated)
paper/figures/fig9-verification-pipeline.pdf       (regenerated)
paper/figures/fig10-stage-effort.py                (docstring + 2 fontsize bumps)
paper/figures/fig10-stage-effort.svg               (regenerated)
paper/figures/fig10-stage-effort.pdf               (regenerated)
paper/figures/fig13-pipeline-vulnerabilities.py    (docstring + 3 fontsize bumps)
paper/figures/fig13-pipeline-vulnerabilities.svg   (regenerated)
paper/figures/fig13-pipeline-vulnerabilities.pdf   (regenerated)
paper/figures/fig15-apk-mass-probing.py            (docstring + 9 fontsize bumps)
paper/figures/fig15-apk-mass-probing.svg           (regenerated)
paper/figures/fig15-apk-mass-probing.pdf           (regenerated)
paper/figures/fig16-scope-limitations.py           (docstring + 1 fontsize bump)
paper/figures/fig16-scope-limitations.svg          (regenerated)
paper/figures/fig16-scope-limitations.pdf          (regenerated)
paper/figures/README.md                            (new design-system defaults section)
docs/handbacks/illustrator-pass-2026-05-03-design-consistency.md  (this file)
```

No edits to `paper/main.md`, `paper/main.tex`, `paper/references.bib`,
or any other paper-side artifact. All LaTeX labels preserved.

---

## D. Hand-back to other agents

- **Stage 4 (Layout Scrutinizer).** Rebuild `paper/main.pdf` and
  re-sweep the five regenerated figures. Expected delta: zero
  body-text below 9 pt across the regenerated set; FIG-11
  closure on fig15 / fig16 (all open items in the
  `layout-to-illustrator.md` round-3 carry-forward except the
  fig8 *"is the red semantic?"* gate, which was already moot —
  fig8 had already been migrated to rose+hatched in a prior
  pass and that has been audited and confirmed this pass).
  No layout-side overflow expected from font-size lifts of ~0.4–
  1.0 pt; the figures retain their bounding-box dimensions
  (no figsize change).
- **Stage 5 (Readability & Novelty Scrutinizer).** No new
  prose-readability defects expected; this pass is
  caption-text-neutral. Optional: confirm the fig13 /
  fig15 / fig16 captions in `paper/main.tex` still describe the
  rendered asset accurately (no caption text was rewritten;
  per-cell content is unchanged; only font sizes changed).
- **Writer.** No writer action required. The pass is
  caption-fidelity-preserving (rule-11 mirror discipline
  unaffected — no `paper/main.{md,tex}` edits).
- **Human author.** The four standing decisions from the prior
  illustrator passes carry forward unchanged:
  1. Logo deliverable for `logo-pandora-jar-intact.png`
     (Gemini second deliverable).
  2. fig8 *"is the red semantic?"* — already moot at the asset
     level (rose + hatched applied), but the human-author
     ratification of the rose-as-warning semantic is still on
     record as DEFERRED in earlier handbacks; this pass treats
     the migration as standing.
  3. Whether to consolidate `fig13` + `fig14` into a single
     integrator matrix.
  4. Whether to file `ILL-NN-promptinj-targets` for §7.11 as a
     new figure.

---

## E. Rule-1 / 11 / 13 / 14 / 15 check

- **Rule 1 (honesty).** Every regenerated script's docstring now
  records *what changed and why* in this pass. fig13's docstring
  in particular was previously laconic (just "AI-authored,
  2026-05-02"); it now records the design-consistency motivation
  for the three font-size bumps applied here.
- **Rule 11 (mirror discipline).** No `paper/main.{md,tex}`
  edits this pass. Mirror unchanged. All `\cref{fig:...}` /
  `\ref{fig:...}` references resolve identically.
- **Rule 13 (no publication).** No `make pdf`, no `make arxiv`,
  no push. Local-only edits; the figures-folder
  `make figures` was *not* run either — figures regenerated by
  direct `python3 fig<N>-<name>.py` invocation, which produces
  the SVG + PDF outputs without touching the LaTeX build chain.
- **Rule 14 (data + script committed).** Every regenerated figure
  has its script committed; no external data file was touched
  (fig10 reads `data/stage-effort.csv` unchanged; fig15 / fig16
  embed structure inline; fig13 embeds structure inline).
- **Rule 15 (README mirror).** No figure was added, replaced, or
  retired. The visual abstract (`fig11-eight-practices.svg`) is
  unchanged. The top-level `README.md` does not require update
  this pass. The figure-folder `paper/figures/README.md` *was*
  updated — the new design-system defaults section is additive
  documentation, not a content change.

---

## F. RE-ANALYSIS REQUIRED

`RE-SCRUTINY REQUIRED: yes` (Stage 4) — for the narrow purpose of
verifying the regenerated figures rebuild cleanly via `make pdf`
and that the FIG-11 carry-forward in
`docs/handbacks/layout-to-illustrator.md` can now be marked
RESOLVED for fig15 / fig16 (and confirmed RESOLVED for fig8
which had already been migrated). No new H-severity defects
expected.

`RE-SCRUTINY REQUIRED: no` (Stage 5) — caption-text-neutral pass.

Standing illustrator-coordination items unchanged:

- **fig1 typography drift** (7.5 / 8 / 8.5 pt labels): logged here
  but **not edited** because the human author has accepted fig1.
  Surface for explicit ratification only if the next consistency
  pass is dispatched against fig1.
- **fig13 / fig14 consolidation** (RDB-05+RDB-08): DEFERRED on
  human-author decision. No change this pass.
- **§7.11 prompt-injection 4×3 matrix** (RDB-07 / proposed
  `ILL-NN-promptinj-targets`): DEFERRED on human-author decision.
  No change this pass.
- **Logo intact-jar Gemini deliverable** (LAY-12, FIG-04): gated
  on human-author Gemini deliverable.
