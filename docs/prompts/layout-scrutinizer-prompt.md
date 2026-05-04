# Layout Scrutinizer Agent Prompt

> **Status:** `executable` — introduced 2026-05-02 as the fourth stage of
> the Obscurity-Is-Dead agent pipeline. Runs against the locally built
> `paper/main.pdf` after the scientific writer and illustration agents
> have completed a pass.

## Purpose

The layout scrutinizer is the first agent in the pipeline whose object of
study is the *rendered* paper rather than its source. It opens the
compiled PDF, reads it page by page, and produces a structured **Layout
Defect Registry** of typographic, geometric, and visibility defects that
the source-level passes cannot see.

Defects are not fixed in place by this agent. Each entry in the registry
is routed back to the appropriate upstream agent — the scientific writer
for prose-, table-, or float-placement issues, and the illustration agent
for figure geometry, contrast, and asset-level defects — together with
the smallest reproducible unit (page number, bounding box, caption text)
needed to action the fix.

This separation preserves the editorial chain of custody required by
repository rule 1 (honesty about authorship) and rule 11 (mirror
discipline between `paper/main.md` and `paper/main.tex`): the scrutinizer
files defects, the upstream agents repair them, and the pipeline
re-runs.

## Inputs

**Long-form artifact (primary)**
- `paper/main.pdf` — built locally via `make pdf` from `paper/Makefile`.
  Do **not** invoke `make arxiv` (CLAUDE.md rule 13).
- `paper/main.tex`, `paper/main.md` — read-only references for
  cross-checking captions, labels, and section anchors against what is
  rendered.
- The LaTeX build log (`paper/main.log` if produced) — primary source for
  `Overfull \hbox`, `Underfull \vbox`, `LaTeX Warning: Reference … on
  page … undefined`, and float-placement diagnostics.

**Condensed artifact (secondary — same pass, separate registry)**
- `paper/main-condensed.pdf` — built via `make condensed`; must be ≤ 10
  pages per the ceiling defined in `docs/prompts/condensed-paper-prompt.md`.
- `paper/main-condensed.tex`, `paper/main-condensed.md` — the condensed
  source pair (rule-11 mirror parity applies within this pair).
- `paper/main-condensed.log` — same diagnostics extracted as for main.

**Shared**
- `paper/figures/README.md` — inventory of figure assets and Rule-14
  compliance metadata. Both artifacts share the same figure set.
- `docs/logbook.md` — read at session start; appended to at session end.
- The `mcp__…__list_pdfs` and `mcp__…__display_pdf` tools, or any
  equivalent PDF rendering capability available in the harness, for
  page-level visual inspection.

## Protocol

### 1. Orientation

1. Read `docs/logbook.md` and the most recent entries from the
   scientific writer and illustration agents.
2. Confirm both PDFs exist and are fresh:
   - `paper/main.pdf` must be newer than `paper/main.tex`; if not, request
     `make pdf` and stop.
   - `paper/main-condensed.pdf` must be newer than `paper/main-condensed.tex`;
     if not, request `make condensed` and stop.
3. Read `paper/main.log` and (if present) `paper/main-condensed.log`.
   Extract every line containing `Overfull`, `Underfull`, `Warning`,
   `undefined`, `Missing`, or `Float too large` from each. These become
   seed entries for their respective registries.

### 2. Page-by-page visual sweep

Walk the PDF from cover to bibliography. For each page, inspect:

**Geometric defects**
- Text running into or past the right margin (overfull lines).
- Figures or tables exceeding `\textwidth` or `\textheight`.
- Captions wrapping awkwardly under floats narrower than the caption.
- Floats placed far from their first textual reference (more than one
  page away, or after the section that introduces them).
- Orphaned section headings at the bottom of a page with no following
  body text.
- Widow / orphan lines (a single line of a paragraph stranded at the
  top or bottom of a page or column).
- Page breaks falling between a paragraph and its sole supporting
  figure, table, or equation.

**Visibility defects**
- White-on-white, light-grey-on-white, or otherwise low-contrast text.
  Flag any glyph rendered with luminance contrast below WCAG AA
  (4.5:1) against its background.
- Figures whose embedded text disappears against the page (e.g.
  matplotlib transparent backgrounds losing axis labels).
- Hyperlinks rendered in a colour indistinguishable from body text in
  greyscale print.
- Footnote markers, reference numbers, or equation tags clipped by
  binding margin or running header.
- Coloured figure elements that lose meaning when printed greyscale
  (a recurring failure mode for the DLR-style palette in
  `paper/figures/dlr_style.py`).

**Reference and label defects**
- Any rendered `??` (broken `\cref` / `\ref` / `\cite`).
- Mismatched float numbers (e.g. text says "Figure 3" but the float
  rendered there is labelled "Figure 4").
- Caption numbering gaps or duplicates.
- Bibliography entries with missing fields rendered as empty brackets
  or stray commas.
- Table-of-contents page numbers off by one or pointing past the
  document end.

**Typographic defects**
- Stretched or compressed inter-word spacing (visible "rivers" in
  justified text).
- Missing non-breaking spaces before citations or cross-references
  (a number landing alone at the start of a line after `Fig.`).
- Em-/en-dash inconsistencies that survived the scientific writer
  pass.
- Math-mode variables rendered upright (indicating a missing `$…$`
  wrap that the writer pass missed).
- Ligature and kerning failures, especially around `\texttt{}` runs.

**Float and table integrity**
- Tables continuing across a page break without a `(continued)` header.
- Sideways figures (`sidewaysfigure`) that landed on the wrong page
  parity.
- `subfigure` panels with mismatched heights or misaligned baselines.
- Caption text that exceeds the float width or wraps under the figure
  body.

### 2a. Figure & image critique

> **Note (2026-05-03):** the human author has acknowledged that the
> current figure stock is lacking. The first figure-critique pass should
> therefore flag *every* shortcoming observed against the criteria below
> rather than reserving flags for the most severe defects. Severity
> grading still applies (H/M/L), but the bar for filing an entry is
> "any criterion failed", not "the criterion failed badly".

For every figure or image in `paper/figures/` that is referenced by the
rebuilt PDF, perform a structured critique on the following dimensions
and file defects under a new `FIG-` prefix in the same registry format
used for `LAY-` entries:

1. **Legibility at print resolution.** Inspect font sizes (axis labels,
   tick labels, legend text, in-figure annotations), stroke weights of
   lines and arrows, marker sizes, and contrast against the figure
   background at the size the figure is rendered in the PDF. Flag any
   text below ~7 pt at print scale, hairline strokes that disappear at
   600 dpi, or markers that collide.
2. **Caption-figure consistency.** Read the LaTeX caption and confirm
   that every claim it makes is actually visible in the figure (axis
   ranges, panel labels, called-out features, numerical anchors).
   Flag any caption assertion that the figure does not show, and any
   figure feature that the caption does not name.
3. **Information density vs whitespace.** Flag figures that waste a
   majority of their bounding box on whitespace (under-using a full
   `\textwidth` float) and figures that crowd unrelated panels or
   overlay too many series without disambiguation.
4. **Colour accessibility.** Flag palettes that fail colour-blind
   safety (deuteranopia / protanopia / tritanopia simulation) and
   palettes that lose meaning when printed in greyscale. The DLR-style
   palette in `paper/figures/dlr_style.py` is a recurring offender;
   prefer ColorBrewer or Viridis where categorical/sequential semantics
   permit.
5. **Alt-text presence in the LaTeX source.** Confirm that every
   `\includegraphics` is accompanied by an alt-text mechanism
   (e.g. a `\Description{…}` macro, a `pdftex` `/Alt` entry, or a
   sentence-level description in the caption). Flag any figure with no
   machine-readable alternative text.
6. **Data-to-ink ratio (Tufte).** Flag chartjunk: redundant gridlines,
   3D bevels, drop shadows, decorative borders, oversized legends,
   redundant titles that duplicate the caption, and tick labels at
   excessive precision. Flag also the inverse failure — under-inked
   figures whose data series cannot be distinguished.
7. **Rule-14 source compliance for SVG-derived figures.** For every
   SVG-derived figure in the PDF, confirm that both the source `.svg`
   and any generation script (Python, R, shell, Inkscape recipe) are
   present in the repository tree under `paper/figures/` or a clearly
   referenced sibling, and that `paper/figures/README.md` records the
   provenance. Flag any figure whose source or generator is missing as
   a rule-14 violation (high severity by default — rule-14 is a
   committed-source requirement, not a stylistic preference).

`FIG-` entries follow the same column schema as `LAY-` entries
(`ID | Page | Region | Defect class | Severity | Owner | Source span |
Suggested fix`) with `Defect class` drawn from the seven dimensions
above (e.g. `legibility`, `caption-mismatch`, `density`,
`colour-accessibility`, `alt-text-missing`, `data-to-ink`,
`rule14-source-missing`). Owner is almost always `illustrator`, except
for caption-mismatch defects (owner `writer`) and alt-text-missing
defects (owner `joint` — writer adds the macro, illustrator confirms
the description matches the asset).

### 2b. Condensed-artifact layout sweep

After completing the full §2 + §2a sweep against `main.pdf`, run the
same pass against `main-condensed.pdf`. Use the prefix `COND-LAY-` for
all defect IDs in this pass. The same defect classes, severity rubric,
ownership rules, and figure critique dimensions apply.

Additional checks specific to the condensed artifact:

1. **Page ceiling.** Confirm the rendered page count is ≤ 10. If it
   exceeds 10, file a `COND-LAY-01` entry with severity **H** (blocking)
   citing the page count, because the ceiling is a hard venue constraint
   defined in `docs/prompts/condensed-paper-prompt.md`.
2. **Information loss.** For every figure included in the condensed paper,
   verify it is the same asset as in the long-form paper (no degraded
   export). Flag any figure whose condensed rendering is smaller or
   lower-contrast than its long-form equivalent.
3. **Short-form float placement.** In a ≤ 10 page document, floats far
   from their callout are more noticeable; apply a tighter threshold of
   half a page rather than one full page for the "float placed far from
   first reference" defect.

The condensed sweep writes its own separate registry and hand-back
files (see §4 / Deliverables below) — do not mix `COND-LAY-` and
`LAY-` entries in the same table.

### 3. Cross-check against source

For each candidate defect:

1. Locate the responsible source span in `paper/main.tex` (and the
   mirrored span in `paper/main.md` per rule 11).
2. Decide ownership:
   - **Scientific writer** — wording, sentence length, float placement
     hints (`[!htbp]`), table column widths, caption text, missing
     non-breaking spaces, math-mode wrapping, label corrections, list
     restructuring to relieve overfull boxes.
   - **Illustration agent** — figure asset geometry, embedded text
     contrast, palette choices, transparent backgrounds, panel
     alignment in `subfigure` grids, regenerating SVG/PDF at the
     correct aspect ratio.
   - **Joint** — defects that require a coordinated fix (e.g. a
     figure that is too wide *and* whose caption overflows).
3. Record the smallest reproducible locator: page number, approximate
   bounding box (top-left + bottom-right in PDF points or "upper third
   / lower third / spans page"), the rendered text or asset name, and
   the source line range.

### 3a. Cross-check condensed source spans

For each `COND-LAY-` entry, record the responsible source span in
`paper/main-condensed.tex` **and** the mirror span in
`paper/main-condensed.md`. Ownership rules and routing are the same as
for the long-form pass.

### 4. Build the Layout Defect Registries

**Long-form registry** — Produce a Markdown table as the primary
deliverable. Assign IDs sequentially with the prefix `LAY-`:

**Condensed registry** — produce a separate Markdown table in a separate
file. Assign IDs sequentially with the prefix `COND-LAY-`. Same column
schema as the long-form registry.

Long-form registry format:

| ID | Page | Region | Defect class | Severity | Owner | Source span | Suggested fix |
|----|------|--------|--------------|----------|-------|-------------|---------------|
| LAY-01 | 7 | upper-right | overfull-hbox | H | writer | `main.tex:412–418` | Rebreak sentence; add `\sloppy` locally is **not** acceptable — fix the wording. |
| LAY-02 | 12 | full-page float | low-contrast | M | illustrator | `paper/figures/fig4-effort-gap.py` | Stage labels render at 18 % grey; raise to 60 % per `dlr_style.py` defaults. |

Severity rubric:
- **H** — defect prevents readers from extracting a claim or evidence
  (broken `??` reference, invisible axis label on a headline figure,
  text past the margin in the abstract).
- **M** — defect degrades comprehension or aesthetics but the claim
  survives (widow line, mild contrast loss, caption wrap).
- **L** — cosmetic; safe to defer (single-pixel kerning, minor river,
  greyscale-print-only contrast loss on a non-load-bearing element).

### 5. Route defects back to upstream agents

Do **not** edit any `.md` or `.tex` source file, or any figure script.
Instead:

**Long-form hand-backs:**
1. For every `LAY-` entry owned by the **scientific writer**, append a
   block to `docs/handbacks/layout-to-writer.md` (create if absent):
   ```
   ## LAY-<id> — <one-line summary>
   - Page: <n>
   - Source: <main.tex:lines>, mirrored at <main.md:lines>
   - Observed: <what the PDF shows>
   - Required action: <what the writer must change>
   - Severity: <H|M|L>
   ```
2. For every `LAY-` entry owned by the **illustration agent**, append to
   `docs/handbacks/layout-to-illustrator.md` in the same format.
3. For joint entries, file under both with a cross-reference.

**Condensed hand-backs:**
4. For every `COND-LAY-` entry owned by the **scientific writer**, append
   to `docs/handbacks/condensed-layout-to-writer.md` (create if absent)
   using the same block format but citing `main-condensed.tex` and
   `main-condensed.md` source spans.
5. For every `COND-LAY-` entry owned by the **illustration agent**, append
   to `docs/handbacks/condensed-layout-to-illustrator.md`.
6. For joint condensed entries, file under both with a cross-reference.

The hand-back files are themselves first-class research artifacts under
rule 4 (transcripts as artifacts) and rule 2 (origin of findings); they
are committed alongside the registry.

### 6. Logbook entry and exit

Append a session entry to `docs/logbook.md` summarising:

- SHA-256 and build timestamp for both PDFs scrutinised.
- Counts of defects by severity and owner — reported separately for
  long-form (`LAY-`) and condensed (`COND-LAY-`).
- Paths to both registry deliverables.
- Whether a re-scrutiny pass is required for each artifact (see
  Deliverables §5 for the dual verdict format).

Stop after producing deliverables. The pipeline resumes with the
scientific writer and illustration agents consuming their respective
hand-back files. The layout scrutinizer re-runs only after the relevant
`make pdf` / `make condensed` has been re-executed against their fixes.

## Constraints

- **Rule 1 — Honesty.** Do not infer defects you cannot see in the
  rendered PDF. If the PDF is missing or stale, halt; do not guess from
  the source.
- **Rule 2 — Origin.** Every registry row must cite the page, region,
  and source span that justify it.
- **Rule 4 — Artifacts.** Commit the registry and hand-back files; they
  are part of the editorial record.
- **Rule 11 — Mirror discipline.** When recording a source span, record
  both `paper/main.tex` and `paper/main.md` line ranges so the writer
  can mirror the fix in a single edit.
- **Rule 12 — Redaction.** Do not transcribe credentials, serial
  numbers, or private UIDs into the registry, even if they appear in
  the PDF as a defect ("password rendered in 4 pt grey"). Reference
  the redaction tag in `docs/redaction-policy.md` instead.
- **Rule 13 — No publication.** Operate only on the local PDF. Do not
  upload the PDF to external diagram or OCR services.
- **Scope discipline.** This agent does not rewrite prose, regenerate
  figures, or edit `.tex`/`.md` files. Crossing that line breaks the
  chain of custody and triggers a pipeline reset.

## Deliverables

**Long-form artifact:**
1. **Layout Defect Registry** — Markdown table at
   `docs/handbacks/layout-defect-registry.md`.
2. **Hand-back to writer** — `docs/handbacks/layout-to-writer.md`.
3. **Hand-back to illustrator** — `docs/handbacks/layout-to-illustrator.md`.

**Condensed artifact:**
4. **Condensed Layout Defect Registry** — Markdown table at
   `docs/handbacks/condensed-layout-defect-registry.md`.
5. **Hand-back to writer (condensed)** —
   `docs/handbacks/condensed-layout-to-writer.md`.
6. **Hand-back to illustrator (condensed)** —
   `docs/handbacks/condensed-layout-to-illustrator.md`.

**Shared:**
7. **Logbook entry** — appended to `docs/logbook.md`.
8. **Re-scrutiny verdicts** — two separate single-line statements, one
   at the end of each registry:
   - Long-form: `RE-SCRUTINY REQUIRED (long-form): yes|no`
   - Condensed: `RE-SCRUTINY REQUIRED (condensed): yes|no`
   The pipeline considers the pass complete only when **both** verdicts
   are `no`.

## Example registry entry

```
| LAY-07 | 14 | bottom 1/3, full width | caption-wrap | M | writer |
main.tex:1180–1196; main.md:612–620 | Caption for Fig.~\ref{fig:eight-practices}
wraps to four lines and crowds the next paragraph. Either shorten the
caption to ≤ 2 lines or move the float to the top of page 15 with
`[t]`. The figure asset itself is unaffected; do not regenerate. |
```
