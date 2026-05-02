# Layout Scrutinizer — Hand-back to Illustration Agent

Source: `docs/handbacks/layout-defect-registry.md` (PDF SHA-256
`ba538ea0d2df9a582889eb16de84d3cd1c6bcf5ae00e647549b7b68bcb2b9e4f`,
build 2026-05-02T14:53:23Z, 40 pages).

The illustrator is the owner of figure-asset geometry, embedded text
contrast, palette choices, and aspect ratio. Do not edit `paper/main.tex`
or `paper/main.md` — those are the writer's responsibility (see
`layout-to-writer.md`).

After remediation, regenerate the affected `*.pdf` figures from their
SVG / Python sources, rebuild via `make -C paper pdf`, and request a
Layout Scrutinizer re-run.

---

## LAY-05 — Figure 7 (verification-status pipeline) overflows `\textwidth` by 226 pt

- Page: 14 (full-page float)
- Source: figure environment at `main.tex:805–827`; asset
  `paper/figures/fig9-verification-pipeline.pdf`; script
  `paper/figures/fig9-verification-pipeline.py`
- Observed: log `Overfull \hbox (226.22418pt too wide) in paragraph at
  lines 808--827`. This is the largest geometric overflow in the
  document — the figure's bounding box is rendered ~7.97 cm wider than
  the printable area. `pdftotext` of page 14 confirms the inner
  two-track legend (literature track / artifact track, with the
  `[needs-research] → [lit-retrieved] → [lit-read]` and
  `[unverified-external] → [repo-referenced] → [repo-vendored]` rows)
  is rendered at a width that exceeds the page text block.
- Required action: re-render `fig9-verification-pipeline.pdf` from
  `fig9-verification-pipeline.py` at a tighter aspect ratio. Preferred
  options, in order:
  1. Stack the two tracks vertically (literature track on top, artifact
     track below) inside a square-ish bounding box; this preserves all
     content and halves the horizontal extent.
  2. Reduce the typeset size of the stage labels and the `gate`
     annotations and increase the inter-stage arrow length so the
     content fits in `\textwidth` (≈430pt) at the natural include size.
  3. As a last resort, mark the float `\begin{sidewaysfigure}` and
     re-emit at landscape proportions — coordinate with the writer
     (cross-ref `layout-to-writer.md`) before doing this.
  Do **not** paper over the overflow with `\resizebox{\textwidth}{!}`
  in `main.tex`; the embedded text becomes illegible.
- Severity: H

---

## LAY-06 — Figure 8 (difficulty taxonomy) sub-table overflow on page 19

- Page: 19 (upper-third heat-map, Figure 8 / `fig12-difficulty-taxonomy`)
- Source: include at `main.tex:1070–1096`; asset
  `paper/figures/fig12-difficulty-taxonomy.pdf`; script
  `paper/figures/fig12-difficulty-taxonomy.py`; data
  `paper/figures/data/difficulty-taxonomy.csv`
- Observed: log `Overfull \hbox (8.79628pt) at lines 1072–1073`
  ("Composite") and `(2.52565pt) at lines 1070–1096`. `pdftotext` of
  page 19 shows the heat-map rows split across what should be a single
  horizontal stripe per case ("Med High" wraps onto the EcoFlow row),
  and the "Composite" header overlaps the rightmost rating column.
- Required action: re-render at the requested 416.7pt × 252.5pt with
  cell labels in a smaller font and column separation widened by ≥6pt.
  Alternatively, separate the composite spread column into a stacked
  sub-panel below the four-axis heat-map. Verify against
  `paper/figures/data/difficulty-taxonomy.csv`.
- Severity: H

---

## LAY-12 — Logo placeholders (pending Gemini final artwork)

- Page: 36 (logo-obscurity-is-dead reference in §10 prose) and 37
  (logo-pandora-jar-intact image)
- Source: assets `paper/figures/logo-pandora-jar-intact.png` (included
  at `main.tex:2191`, log entry `id=1799, 343.28pt × 341.11pt`) and
  `paper/figures/logo-obscurity-is-dead.png` (referenced in §10 prose
  at `main.tex:2009–2028`); generation script
  `paper/figures/logo-placeholders.py`
- Observed: both logo PNGs are AI-authored placeholders pending the
  Google-Gemini-generated final artwork commissioned 2026-05-02. The §10
  prose explicitly labels them as placeholders per CLAUDE.md rule 1.
  This is **not** a content-quality, contrast, or visibility failure —
  it is a tracking entry so the illustrator pipeline replaces the PNGs
  once the Gemini deliverable arrives.
- Required action:
  1. When the Gemini-generated assets land, drop them in place at
     `paper/figures/logo-pandora-jar-intact.png` and
     `paper/figures/logo-obscurity-is-dead.png`.
  2. Update `paper/figures/README.md` Rule-14 metadata to mark the
     assets as final (and note the prompt / model / date used to
     generate them).
  3. Leave `paper/figures/logo-placeholders.py` in the tree (as the
     auditable record of what the placeholder was) — do not delete it.
  4. Trigger a Layout Scrutinizer re-run against the rebuilt PDF so the
     final assets are inspected for contrast and aspect-ratio fit.
- Severity: M (status: PLACEHOLDER-pending; not a defect of execution)

---

## LAY-13 — Embedded PDFs at version 1.7 vs. document target 1.5

- Page: 22 (Figure 11 — dual-use map) and 23 (Figure 12 — threat-models)
- Source: `paper/figures/fig6-dual-use.pdf` (included at `main.tex:1281`)
  and `paper/figures/fig7-threat-models.pdf` (included at `main.tex:1288`)
- Observed: `pdfTeX` warning twice: `PDF inclusion: found PDF version
  <1.7>, but at most version <1.5> allowed`. No reader-visible defect
  in the current build, but a stricter pdfTeX (or arXiv's build
  pipeline) may downgrade or reject these floats.
- Required action: re-export the SVG sources to PDF with
  `CompatibilityLevel=1.5`. Two equivalent recipes:
  - `rsvg-convert -f pdf -o fig6-dual-use.pdf fig6-dual-use.svg` then
    `gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -o fig6-dual-use.pdf -- fig6-dual-use.pdf`
  - Or `inkscape --export-type=pdf --export-pdf-version=1.5
    fig6-dual-use.svg`.
- Severity: M

---

## LAY-16 (joint, advisory) — Bibliography URL/path overflows

- Page: 39–40
- Source: `main.bbl` (auto-generated); upstream `references.bib` plus
  the vendored-archive paths under
  `experiments/spider-farmer/original/doc/`
- Observed: ~25 Underfull `\hbox` warnings in the bibliography for
  community-implementation entries (`p0rigth_spiderblebridge`,
  `noheton_pythonspider`, …). Cosmetic justification rivers caused by
  long unbreakable URLs.
- Required action: this is primarily a writer-owned `references.bib`
  fix (see `layout-to-writer.md#LAY-16`). The illustrator may be asked
  to provide a *short alias* for vendored-archive paths if a future
  bib style cannot wrap them — no current action required.
- Severity: L

---

## Summary for the illustrator

- **H:** LAY-05 (fig9-verification-pipeline regenerate at tighter
  aspect), LAY-06 (fig12-difficulty-taxonomy regenerate with widened
  columns).
- **M:** LAY-13 (re-export fig6-dual-use and fig7-threat-models at PDF
  1.5), LAY-12 (replace logo placeholders when Gemini assets arrive).
- **L:** LAY-16 (advisory only).
- All five floats are sourced under `paper/figures/`; no asset outside
  the figure directory is implicated.
