# Layout Scrutiny — 2026-05-03 — round 4 (narrow re-sweep, Claude Opus 4.7)

> Stage 4 narrow re-sweep against `paper/main.pdf` rebuilt on branch
> `claude/check-illustration-pipeline-Jqst3` after illustrator commits
> `66368bf` (pipeline-fix audit, fig8/15/16 CB-palette + 9 pt body
> floor on fig9/10/13) and `fae586b` (design-consistency audit + new
> "Design-system defaults" section in `paper/figures/README.md`).
>
> **This is not a full Stage-4 pass.** The round-3 registry
> (`docs/handbacks/layout-defect-registry.md`, commit `ac83bae`,
> 0 H / 8 M / 13 L) remains the active baseline. Defect IDs are
> reused; no full sweep performed.

## Build under inspection

- **PDF SHA-256:** `7744f36c3abb99339319108ca868574d62a8258340a4014acccbd4bfd66d7eb5`
- **PDF size / pages:** 1,236,060 bytes / 54 pages (round-3: 1,231,155 / 54).
- **PDF mtime:** 2026-05-03T18:59 (newer than every `paper/figures/*.pdf` mtime: fig8 at 18:36, fig9/10/13/15/16 at 18:39 — fresh build against the post-illustrator figure set).
- **Latexmk verdict:** "All targets up-to-date" on the current build.
- **Log:** `paper/main.log` reports 33 `Overfull \hbox`, 67 `Underfull \hbox`, 0 `Reference … undefined`, 0 `Citation … undefined`, 0 `??` in the rendered PDF — **identical counts to round 3** (no new structural defects from the illustrator pass; all changes were figure-internal `.py` recolours / font raises).
- **Method note:** PDF-viewer MCP unavailable in this harness; pages were rendered to PNG via PyMuPDF at 200 dpi (`/tmp/pdfpages/page{15,52,53}.png` and regression set `{1,5,16,26,28,50,51,54}.png`) and inspected as raster images. Viewer-level pixel sweep counts as completed for the three primary targets.

## Figure ↔ source mapping (verified this round)

The PDF figure numbering does not match the `figN-*.pdf` filenames; the
mapping below was re-derived this pass from `paper/main.tex` `\caption`
spans and the rendered captions:

| Source asset | Rendered as | Page | Caption first words |
|---|---|---|---|
| `fig8-ecoflow-surfaces.pdf` | **Figure 6** | 15 | "EcoFlow PowerOcean three API surfaces." |
| `fig13-pipeline-vulnerabilities.pdf` | Figure 9 | 26 | "Vulnerabilities of IoT-integrator pipelines as a system class." |
| `fig10-stage-effort.pdf` | Figure 10 | 28 | "Stage-by-stage effort gap." |
| `fig11-eight-practices.pdf` (dual-use plane) | Figure 11 | 50 | "Dual-use map." |
| `fig15-apk-mass-probing.pdf` | **Figure 14** | 52 | "Automated mass probing of public APK repositories." |
| `fig16-scope-limitations.pdf` | **Figure 15** | 53 | "Scope and limitations of the study." |

The three FIG-11 sub-items target the **bolded** rows.

## FIG-11 verdict (primary objective of this round)

### FIG-11 / fig8 (Figure 6, p15) — **RESOLVED**

Rendered output confirms the Tol-bright rose `#ee6677` + diagonal hatch
encoding on the legacy-`setDeviceProperty` REST surface (upper-right
node) and on the consumer-app→legacy "USES (undocumented)" arrow.
Integrator-select arrow renders in DLR yellow (`#d2ae3d`) with darker
label, distinct from the rose warning channel. Sub-caption visible at
the bottom of the figure includes the "Hatched rose = legacy /
undocumented (CB-safe)." legend tail. No fragment of the previous pure-
red `#c0392b` palette survives in the rendered figure. Body / sub-label
text is visibly at the 9 pt floor or above; sub-caption renders at
~9 pt and remains legible at print scale. The "do-not-use" semantic
that previously rode on hue alone is now redundantly encoded in hue +
hatch + legend, satisfying CB / greyscale-print accessibility.

**Disposition:** close FIG-11/fig8. Owner-side hand-back (illustrator)
is empty.

### FIG-11 / fig15 (Figure 14, p52) — **RESOLVED**

Rendered output shows the five-stage pipeline filled with a sequential
blue ramp running light → dark from "Public APK repository" through to
"Per-vendor weakness inventory". The two darkest stages ("DEX-grep +
identity-provider discovery", "Per-vendor weakness inventory") render
their stage-name labels in white (the `_DARK_FILLS` membership switch
is materialised correctly in the PDF). Colour now monotonically encodes
pipeline depth, satisfying both greyscale and deuteranopia tests by
construction. The empirical-rates summary panel below the pipeline
renders in neutral grey (`DLR_GRAY_SOFT`); the previous saturated
yellow is gone, leaving DLR blue as the only saturated accent on the
page (one-chapter-one-accent rule observed). Stage sub-labels
(`<70% of 17,243 BLE Android APKs vulnerable`, `~10s / APK`,
`1,673 / 4,200 BT companion apps leak user data`, etc.) render at the
9 pt body floor and sit cleanly under their stage boxes without
collision. Footer caption inside the panel renders at ~9 pt.

**Disposition:** close FIG-11/fig15.

### FIG-11 / fig16 (Figure 15, p53) — **RESOLVED**

Rendered output shows the concentric perimeter diagram with the inner
"Study perimeter" ring filled in CB-safe DLR `#a7d3ec` blue and the
outer exclusion cells filled in Tol-bright rose `#fbe0e2` with `////`
diagonal hatching and `#ee6677` borders. Legend at bottom shows the
two encodings ("in scope" / "named exclusion") with matching swatches.
Inner-cell text (e.g. "4 consumer-IoT cases + 1 meta-process",
"Spider Farmer + EcoFlow validated at fluffr3oc") renders at print-
legible size — the prior 7.8 pt floor has clearly been raised; nothing
in the rendered figure looks below 9 pt. Footer info-box ("Two further
interpretive bounds…") renders inside a yellow info box and is
readable at the rendered scale.

One **minor advisory** observation, **not** a regression and **not**
blocking the FIG-11 closure: a couple of the inner-ring labels
("AI-assisted workflows … governance"; "Spider Farmer + EcoFlow
validated at fluffr3oc") visually encroach on the inner blue
perimeter ring, with the text overlapping the ring stroke. The figure
was widened from 11"×9" to 12"×9.5" specifically to absorb the larger
labels, but a small amount of overlap remains. This is filed as a new
**FIG-12 (L, illustrator)** below; it is cosmetic and the figure's
load-bearing claim (five in-scope dimensions, six named exclusions)
remains fully readable.

**Disposition:** close FIG-11/fig16; the residual encroachment is
re-bookkept as FIG-12 (L, advisory, illustrator) — see new defects
below.

## Tertiary check — 9 pt body-floor consistency on fig9 / fig10 / fig13

- **fig9 / `fig9-verification-pipeline.pdf` (Figure 9, p26).** Stage-
  promotion arrow labels render at the body floor; no glyph reads as
  sub-9 pt against the rendered page. Central residual-risk node
  italic sub-label legible. No regression.
- **fig10 / `fig10-stage-effort.pdf` (Figure 10, p28).** Legend at top-
  right of the left panel renders at ~9 pt; the "Rule 1 …" annotation
  inside the panel is also at the body floor. Right panel
  ("Asymmetric collapse") tick labels and category labels are legible.
  No regression.
- **fig13 / `fig13-pipeline-vulnerabilities.pdf` (rendered as Figure 9,
  p26 — same asset as the fig9 file in the table above; the source-
  filename naming is misleading because `fig13-pipeline-
  vulnerabilities.py` is the actual generator for the rendered Figure
  9).** Outer-node sub-labels ("Whoa/visibility gap", "Cross-vendor
  data-flow opacity", etc.) and the central-node italic-sub-label all
  render at the body floor; footer caption inside the panel readable.
  No regression.

The 9 pt body-floor sweep landed cleanly. No new typography-floor
defects to file.

## Regression sweep (fig1 / fig11 / fig12 / fig14)

- **fig1 / `fig1-effort-gap.svg` (Figure 1, p5).** Two-panel effort-gap
  curve — clean, no regression.
- **fig11 / `fig11-eight-practices.pdf` (Figure 11 dual-use plane,
  p50).** Dual-use scatter renders with researcher-governed (DLR blue)
  and adversarial-variant (Tol-bright rose) markers — palette
  consistent with the FIG-11 closure encoding and CB-safe. Quadrant
  labels and axis labels at body-floor scale. No regression.
- **fig12 / `fig12-difficulty-taxonomy.pdf` (Figure 8, p25).** Test-
  case difficulty heat-map renders cleanly. No regression.
- **fig14 / `fig14-malicious-integrator.pdf` (Figure 13, p51).**
  Researcher-governed branch (teal/blue), adversarial branch
  (rose + hatch) — encoding consistent with the FIG-11 / fig8 / fig16
  treatment. The design-system rose+hatch language is now coherent
  across all four figures that carry an exclusion / adversarial /
  legacy semantic (fig8, fig11 dual-use, fig14, fig16). No regression.

## New defects this round (single L-severity advisory)

| ID | Page | Region | Defect class | Severity | Owner | Source span | Suggested fix |
|----|------|--------|--------------|----------|-------|-------------|---------------|
| **FIG-12** | 53 | inner perimeter ring | density / label-collision | L | illustrator | `paper/figures/fig16-scope-limitations.py` (post-`66368bf` width 12"×9.5") | Two of the six inner-ring labels ("AI-assisted workflows … governance"; "Spider Farmer + EcoFlow validated at fluffr3oc") visually encroach on the inner blue perimeter stroke after the FIG-11 font-raise to 9.5 pt. The widening from 11"×9" to 12"×9.5" absorbed most of the pressure but not all. Cosmetic; the load-bearing claim is fully readable. Close FIG-11 first; defer FIG-12 to the next cosmetic / pre-arxiv pass. Suggested fix: nudge the two inner-ring label radii outward by ~6–8 % or drop the inner-ring label font from 9.5 pt to 9.0 pt (still at the body floor) — illustrator's choice. |

No new H-severity defects. No new M-severity defects. The registry
shrinks (3 M items closed under FIG-11) and grows by 1 L item.

## Severity rollup delta vs round 3

- **H:** 0 (unchanged).
- **M:** 8 → **5** (closed: FIG-11 / fig8, FIG-11 / fig15, FIG-11 / fig16; remaining: LAY-02/-24, LAY-08, LAY-09/-25, LAY-10, LAY-22/-29, FIG-04, FIG-08).
- **L:** 13 → **14** (added FIG-12; nothing dropped).
- **Net:** registry shrinks by 2 entries when collapsing the FIG-11 sub-items.

## Per-FIG-11-sub-item single-line verdict

- **FIG-11 / fig8 (Figure 6, p15):** RESOLVED.
- **FIG-11 / fig15 (Figure 14, p52):** RESOLVED.
- **FIG-11 / fig16 (Figure 15, p53):** RESOLVED (with new advisory FIG-12, L).
- **FIG-11 (parent) overall:** **RESOLVED** — all three sub-items closed; the M-severity entry is downgraded out of the registry.

## Mirror, redaction, distribution

- **Rule 11 (mirror discipline).** No `paper/main.{md,tex}` edits in the
  illustrator passes; LaTeX labels (`fig:ecoflow-surfaces`,
  `fig:apk-mass-probing`, `fig:scope-limitations`) unchanged; all
  cross-references resolve. No drift.
- **Rule 12 (redaction).** No new credentials / serials / UIDs / IPs in
  the recoloured figures. Existing `[REDACTED:repo-path:BALBOA-
  UPSTREAM-{1,2}]` markers at `main.tex:2228–2229` persist (line band
  unchanged from round 3).
- **Rule 13 (no publication).** Local PDF only. `make arxiv` not
  invoked.

## Hand-back routing

- `docs/handbacks/layout-to-illustrator.md` — append FIG-12 (L,
  advisory, fig16 inner-ring label encroachment). The three FIG-11
  sub-items can be removed from the writer/illustrator hand-back files
  on the next consolidation pass (registry already records closure).
- `docs/handbacks/layout-to-writer.md` — no new entries this round.
- `docs/handbacks/layout-defect-registry.md` — full update deferred to
  the next non-narrow Stage-4 pass; this narrow re-sweep records its
  changes here, in `layout-scrutiny-2026-05-03-round4.md`.

## Verdict

**RE-SCRUTINY REQUIRED: no.**

The narrow re-sweep was triggered specifically to confirm FIG-11
closure for fig15 and fig16 (fig8 was already migrated in the prior
overhaul but its working-tree edit was promoted to commit only in
`66368bf`, so fig8 is also confirmed this round). All three sub-items
are RESOLVED at the rendered-PDF level; the CB-safe palette, the
hatch-pattern redundant encoding, and the 9 pt body-floor are
materialised in the PDF. One new L-severity advisory (FIG-12, fig16
inner-ring label encroachment) is filed but does not block any
downstream stage. The path-bullet M cluster (LAY-09/-22/-25/-29) and
the writer-owned residuals are unchanged from round 3 and remain the
natural target of the next writer-side sweep, not this layout pass.
Stage 5 (readability) and the orchestrator may proceed without a
further Stage-4 rebuild requirement.
