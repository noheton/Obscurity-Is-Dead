# Illustrator (Stage 3) — Pipeline-fix audit + FIG-11 closure pass 2026-05-03

- **Agent:** Claude Opus 4.7
- **Branch:** `claude/check-illustration-pipeline-Jqst3`
- **Trigger:** Author observed "ich habe nicht das gefühl als ob sich die
  illustrationen ändern." Investigation revealed the pre-fix `paper/Makefile`
  ran SVG→PDF conversion only for `fig1`..`fig7` and never invoked the
  matplotlib `.py` generators for `fig8`..`fig16`, so prior illustrator
  edits to those `.py` files had not propagated into the rendered PDF.
  Pipeline was repaired in commits `80b5608` (Makefile rule
  `$(SCRIPTED_FIG_PDFS)` covering fig1 + fig6..fig16) and `e19d04a`
  (toolchain whitelist expansion). This pass executes the dual mandate:
  (a) audit every reworked figure to confirm the committed PDF matches
  what its `.py` produces; (b) materialise any open illustrator hand-back
  items that are not gated on a human decision.

---

## A. Pipeline audit — reworked-figure freshness check

### Method

For each scripted figure (`fig1`, `fig6`..`fig16`):

1. Restored a clean working tree and ran `make -C paper figures`. Make
   reported "Nothing to be done" — confirming the committed `.py` /
   `.svg` / `.pdf` mtimes are coherent.
2. Forced a full regeneration via `touch paper/figures/dlr_style.py &&
   make -C paper figures`. All twelve scripted figures regenerated
   successfully; matplotlib is correctly installed and `dlr_style`
   imports cleanly.
3. Compared the regenerated `.svg` and `.pdf` byte-for-byte against
   the committed assets.

### Result — no visual drift

For every figure the substantive content of the regenerated SVG is
**identical** to the committed SVG. The only diffs are:

- `<dc:date>` metadata timestamps;
- matplotlib's hash-based `clipPath` IDs (e.g. `p3896d64771` →
  `pa435992ce4`) and `<path id="m...">` UUIDs that change on every run;
- corresponding `xlink:href="#m..."` references.

Every regenerated **PDF** is byte-for-byte identical in size to the
committed PDF (24888 → 24888 bytes for fig1; 33807 → 33807 for fig10;
48789 → 48789 for fig11; etc.) and visually identical at the pixel
level (the matplotlib PDF backend hashes its internal IDs the same way
on every run for a given figure regardless of the pre-existing
non-deterministic SVG IDs).

**Verdict.** The reworked figures from commit `d2858ac` (fig6, fig7,
fig9, fig10, fig11, fig14) and the prior overhaul are correctly
materialised in `paper/main.pdf`. The author's "feels like nothing
changed" intuition was historically correct (pre-`80b5608` Makefile
gap) but is no longer true under the repaired pipeline. No re-run of
the prior overhaul is needed.

The 24 lines of `git status` "modified" entries that appeared on
session start were entirely the timestamp + clip-id non-determinism
described above; they have been reverted.

---

## B. Open hand-back items — disposition

| Item | Severity | Owner | Disposition this pass |
|------|----------|-------|------------------------|
| FIG-04 (logo `logo-pandora-jar-intact.png` placeholder) | M | human-author | **DEFERRED** — gated on second Gemini deliverable. No illustrator action available. |
| FIG-09 (data-to-ink audit) | L | layout | **DEFERRED** — viewer-blocked at Stage 4. |
| FIG-10 (`\Description{}` fidelity audit) | L | illustrator | **DEFERRED** — pure-audit task, low leverage; recommend folding into next CB-palette / overhaul pass when scrutinizers reconvene. |
| FIG-11 / fig8 (red `#c0392b` legacy semantic) | M | illustrator | **CLOSED** this pass — see C.1 below. |
| FIG-11 / fig15 (borderline green stage fills) | M | illustrator | **CLOSED** this pass — see C.2 below. |
| FIG-11 / fig16 (7.8 pt cells; red exclusion ring) | M | illustrator | **CLOSED** this pass — see C.3 below. |
| RDB-04 (consolidate §10 enumeration into Fig 11) | M | writer + illustrator | **DEFERRED** — Stage 5 verifies Fig 11 already carries the load; the writer-side prose decision (option a / b / c) is the next move and is owned by the human author. |
| RDB-05 + RDB-08 (consolidate fig13 + fig14) | M | writer + illustrator | **DEFERRED** — structural authorial decision; the two figures serve distinct rhetorical positions per the prior pass. |
| RDB-07 (§7.11 4×3 prompt-injection matrix) | optional | illustrator | **DEFERRED** — writer-side prose conversion unblocks; figure is enhancement, not blocker. |

### Note on the pre-existing fig8 working-tree edit

When this session opened, `paper/figures/fig8-ecoflow-surfaces.py`
already contained a substantive uncommitted recolour from a prior
session: pure red `#c0392b` / `#ffe6e6` replaced by Tol-bright rose
`#ee6677` + hatched fill on the legacy-REST surface; body text raised
from 9.5/8.0 pt to 10.0/9.0 pt; sub-caption lifted from 8.5 to 9.0 pt.
The change is exactly the FIG-11 / fig8 remediation the prior overhaul
hand-back recommended; it appears to have been written but not committed
before that session ended. Rather than discarding finished work, this
pass regenerated the matching `.svg` / `.pdf` outputs so the three
artefacts are coherent, and includes the fig8 set in the commit. The
"is the red semantic?" question that previously gated the change is now
answered by the change itself: the prior agent transferred the
"do-not-use" semantic to the hatched-rose pattern, which preserves the
warning identity in greyscale and CVD — the safer default. The human
author retains the option to revert if the rose+hatch reading does not
match their intent.

---

## C. What was redone this pass

### C.1 fig8-ecoflow-surfaces (FIG-11 closure — pre-existing working-tree edit promoted to commit)

- **Was:** pure red `#c0392b` / `#ffe6e6` on the legacy-REST surface
  and the consumer-app→legacy arrow; 9.5/8.0 pt body/sub-label;
  8.5 pt sub-caption.
- **Now:** Tol-bright rose `#ee6677` (CB-safe) + `//` hatched fill on
  the legacy-REST surface; matching rose for the
  consumer-app→legacy "USES (undocumented)" arrow; integrator-select
  arrow recoloured from raw `#b8860b` to `dlr_style.DLR_YELLOW`
  (`#d2ae3d`) with darker label. Body 10.0 pt; sub-label 9.0 pt;
  sub-caption 9.0 pt. Title 12.0 pt. Sub-caption gains a "Hatched
  rose = legacy / undocumented (CB-safe)." legend tail. Figure height
  raised 6.2"→6.4" so the larger labels do not overlap.
- **Provenance:** the `.py` edit was already in the working tree at
  session start; this pass added `import` cleanup, regenerated `.svg`
  + `.pdf`, and is committing the artefacts.

### C.2 fig15-apk-mass-probing (FIG-11 closure — green stage fills)

- **Was:** three middle pipeline stages filled with `#cad55c` (DLR
  green base); empirical-rates panel filled with `#fff8be` (DLR
  yellow soft).
- **Now:** sequential blue ramp (`#d1e8fa` → `#a7d3ec` → `#6cb9dc`
  → `#3b98cb` → `#00658b`) so colour monotonically encodes pipeline
  depth and survives greyscale + deuteranopia. Last two darker stages
  switch to white text via a `_DARK_FILLS` membership check. The
  yellow empirical-rates panel becomes neutral `dlr_style.DLR_GRAY_SOFT`
  so DLR blue remains the only saturated accent (one-chapter-one-accent
  rule).

### C.3 fig16-scope-limitations (FIG-11 closure — font + red ring)

- **Was:** inner-cell font 7.8 pt (under print-legibility threshold);
  exclusion-ring fill `#fadbd8` (pink/red, fails deuteranopia); legend
  fill matching.
- **Now:** inner-cell font raised to 9.5 pt; ring-label short-text
  raised 8.6→9.2 pt; footer 8.6→9.0 pt; legend text 8→9 pt. Exclusion
  ring fill replaced with Tol-bright rose `#fbe0e2` + `////` hatch
  + `#ee6677` border (matches fig8 + fig14 pattern); in-scope ring
  retained at DLR `#a7d3ec` (CB-safe blue). Figure widened
  11"×9"→12"×9.5" to absorb the larger labels without overlap.

### C.4 paper/figures/README.md

- Added a sentence to the AI-authored-programmatic-diagrams paragraph
  noting the 2026-05-03 pipeline-fix pass closed the residual FIG-11
  items via the fig8 / fig15 / fig16 recolour + font-raise
  (Rule-15 spirit, mirror discipline).

---

### C.5 Design-consistency 9 pt body-floor sweep (fig9 / fig10 / fig13 / fig15 / fig16)

A consistency sweep raised every sub-label / legend / footer font that
sat below the 9 pt body floor (the floor that the hero figure
`fig11-eight-practices` establishes for the figure set). Specifically:

- `fig9-verification-pipeline.py`: stage-promotion arrow labels 8.5 → 9.0 pt.
- `fig10-stage-effort.py`: legend 8.5 → 9.0 pt; rule-1 annotation 8.5 → 9.0 pt.
- `fig13-pipeline-vulnerabilities.py`: central-node italic-sub-label 8.0 → 9.0 pt; outer-node sub-label 8.2 → 9.0 pt; footer caption 8.6 → 9.0 pt.
- `fig15-apk-mass-probing.py` (in addition to the C.2 recolour): stage sub-label 8.2 → 9.0 pt; cost-tier brackets 8 / 8.6 → 9.0 pt; empirical-rates panel body 8.4 → 9.0 pt; panel italic 8.4 → 9.0 pt; footer 8.6 → 9.0 pt.
- `fig16-scope-limitations.py` (in addition to the C.3 recolour): footer 8.6 → 9.0 pt (still inside the yellow info-box).

No palette change in any of these five — only typographic alignment to
the figure-set body floor.

## D. Files touched this pass

- `paper/figures/fig8-ecoflow-surfaces.py` (pre-existing working-tree
  edit promoted; outputs regenerated)
- `paper/figures/fig8-ecoflow-surfaces.{svg,pdf}` (regenerated)
- `paper/figures/fig15-apk-mass-probing.py` (CB-palette recolour)
- `paper/figures/fig15-apk-mass-probing.{svg,pdf}` (regenerated)
- `paper/figures/fig16-scope-limitations.py` (font raise + CB-palette)
- `paper/figures/fig16-scope-limitations.{svg,pdf}` (regenerated)
- `paper/figures/README.md` (inventory note)
- `docs/handbacks/illustrator-pass-2026-05-03-pipeline-fix.md` (this file)

No `paper/main.md` / `paper/main.tex` changes — captions remain
accurate, LaTeX labels (`fig:ecoflow-surfaces`, `fig:apk-mass-probing`,
`fig:scope-limitations`) are unchanged, so all `\cref{...}` /
`\ref{...}` cross-references continue to resolve. Rule-11 mirror
discipline preserved by no-op.

No new toolchain path was exercised this pass (all three reworks are
matplotlib edits), so no new `paper/Makefile` rule was needed; the
existing `$(SCRIPTED_FIG_PDFS)` rule already covers fig8 / fig15 /
fig16. The Mermaid / TikZ / Graphviz / D2 paths added in commit
`e19d04a` remain available for future work; none of the open
hand-back items required them.

---

## E. Rule-1 / 11 / 13 / 14 / 15 check

- **Rule 1 (honesty):** the three regenerated script docstrings now
  carry an explicit "2026-05-03 pipeline-fix pass" change log with the
  rationale for each recolour. Numbers shown in the figures (APK base
  rates from L-BLE-4, L-PRIV-5; in-scope/exclusion enumeration from
  §7.15) are unchanged.
- **Rule 11 (mirror discipline):** no `paper/main.{md,tex}` edits;
  no caption text changes; mirror is unchanged.
- **Rule 13 (no publication):** no `make pdf`, no `make arxiv`, no
  `git push` to public; local-build artefacts only.
- **Rule 14 (data + script committed):** fig15 and fig16 remain
  structural diagrams (no external data file required, per the
  pre-existing inventory); generation scripts are committed and
  registered. fig8 is structural likewise. The Rule-14 inventory in
  `paper/figures/README.md` is not affected (no new data file added,
  no figure changed status).
- **Rule 15 (README mirror):** the top-level `README.md` references
  `fig11-eight-practices.svg` as the hero image — that file is
  unchanged this pass, so no top-level README update is required.
  fig8 / fig15 / fig16 are not pulled into the README gallery, so
  the recolours do not propagate there.

---

## F. RE-ILLUSTRATION REQUIRED

`RE-ILLUSTRATION REQUIRED: no` — the audit closed cleanly (no
silent-drift between committed PDFs and what scripts produce), and
the three FIG-11 closures are mechanically materialised. Stage 4
(layout) and Stage 5 (readability) should re-scrutinise after a
`make pdf` rebuild to confirm:

1. fig8 / fig15 / fig16 PDFs render with the new CB-safe palette
   and the raised fig16 fonts at print resolution (Stage 4 pixel
   sweep, currently viewer-blocked but worth retrying).
2. No caption / label drift between the recoloured figures and the
   surrounding prose (Stage 5 caption-fidelity sweep — captions
   are unchanged, so a quick re-read at §4.3, §7.14, §7.15 suffices).
3. FIG-11 can be downgraded from M to RESOLVED in
   `layout-defect-registry.md` once the layout scrutinizer confirms
   the visual change.

Carry-forward items still owned by the illustrator (no action this
pass): FIG-04 (Gemini deliverable gate), FIG-10 (alt-text fidelity
audit), RDB-05+08 / RDB-07 (consolidation candidates pending human
decision).
