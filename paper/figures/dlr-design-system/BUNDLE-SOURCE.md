# DLR Design System — bundle source and curation

This directory is a **curated subset** of a Claude Design handoff bundle
exported from `https://api.anthropic.com/v1/design/h/YCsRfEWCmYQvrknj0kuLNg`
on 2026-05-03.  The full upstream bundle is ~87 MB (456 files).  This
repository ships only the **specification surface** that the
illustration agent and the figure-generation Python scripts need.

## What is in this directory

- `README.md` — the upstream "CODING AGENTS: READ THIS FIRST" handoff note.
- `project/README.md` and `project/SKILL.md` — the long-form docs and the
  prescriptive skill manifest.  `SKILL.md` is the **authoritative spec**
  the illustration agent must read before producing any figure.
- `project/colors_and_type.css` — the CSS-token surface (variants A/B/C,
  brand colours, typography sizes).
- `project/ui_kits/python_plots/` — the upstream `dlr_style.py` reference
  copy, plus its `README.md` and `UPSTREAM_README.md`.  The actually-used
  copy lives at `paper/figures/dlr_style.py` (one directory up); see
  "Why two copies" below.
- `project/ui_kits/marp/framework/rules/corporate-design.md` — the marp
  framework's compact corporate-design rule sheet (text-only, marp-shaped).
- `project/assets/dlr-logo.svg`, `dlr-logo-white.svg`, `dlr-logo-stacked.png`
  — the brand-mark assets.
- `chats/chat1.md` — the upstream design-tool conversation transcript that
  produced this bundle.  Kept verbatim per CLAUDE.md rule 4
  (transcripts as first-class research artifacts).

## What is excluded and why

- **Frutiger fonts** (`*.ttf`, `Frutiger_Font_Family.zip`,
  `frutiger-light-1777639937-0.zip`).  Frutiger is the DLR Hausschrift but
  ships under a commercial licence.  Per `SKILL.md` "Caveats", Arial is
  the *mandated* face for E-Mail / Web / PowerPoint anyway; the figure
  scripts here use `dlr_style.py`'s graceful Frutiger → Arial → DejaVu Sans
  fallback so the build works without the licensed font.
- **DLR brand documents and PowerPoint masters** (`uploads/*.pdf`,
  `uploads/*.potx`, ~70 MB total).  These are reference reading; the
  illustration agent does not need to render them and they would dominate
  the repository's size budget.
- **HTML preview pages with embedded large background JPGs** (the
  bg-title-{blue,green,yellow}.jpg + master-bg-* family).  The CSS-token
  layer in `colors_and_type.css` is enough to recreate these surfaces
  without shipping the bitmaps.
- **Marp template binary assets** (`title_back.png` etc.).  Same rationale.

## Why two copies of `dlr_style.py`

`paper/figures/dlr_style.py` is the *adapted* version actually imported
by the paper's figure scripts.  Differences from the upstream copy in
this bundle:

- Removed intranet (`https://intranet.dlr.de/...`) URLs that are not
  resolvable from outside DLR.
- Added explicit Frutiger → Arial → DejaVu Sans font fallback so the
  paper builds without the licensed Frutiger fonts.
- Added named brand-colour convenience constants (`DLR_BLUE`, etc.)
  exported alongside the existing `dlr_colors` palette.
- Added a docstring labelling the file as AI-adapted from the upstream
  bundle (rule 1).

The upstream copy is preserved in this directory under
`project/ui_kits/python_plots/dlr_style.py` so the divergence is
auditable: a future reader can `diff` the two and see exactly what was
changed and why.

## Pre-publication note

Per CLAUDE.md rule 13, no part of this directory is to be redistributed
without confirming the licence terms of each constituent asset.  In
particular: the SVG logos are DLR brand marks and must not be used in
unrelated publications; the bundle as a whole was generated for a
specific Claude Design session and should be treated as scoped to this
project.  A pre-publication review must (a) re-confirm bundle licence,
(b) replace the SVG logos with placeholder marks if the paper is
re-released outside the DLR-affiliation context, and (c) re-fetch from
the upstream URL if the design system has been versioned forward.
