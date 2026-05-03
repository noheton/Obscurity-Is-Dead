# DLR Corporate Design

Source of truth: `DLR-PPT-Master_1.31_EN.potx` (see `framework/templates/base-dlr-pptx/`).

## Theme reference

Every presentation's frontmatter must have:

```yaml
marp: true
theme: dlr
```

The theme is registered via `.vscode/settings.json` (Marp VS Code) and `package.json` (Marp CLI). **Never** use `theme: dlr-theme` (legacy name).

---

## Typography

All text uses **Arial, sans-serif** exclusively.

| Element | Size | Weight | Color |
|---------|------|--------|-------|
| Slide title (h1) | 28pt | bold | `#666666` gray |
| Cover title (h1 on `.title`) | 48pt | bold | `#000000` black |
| Sub-heading (h2) | 20pt | bold | accent color |
| Sub-sub-heading (h3) | 18pt | bold | `#464646` dark charcoal |
| Body text / bullet level 1 | 24pt | normal | `#000000` |
| Bullet level 2 | 20pt | normal | `#000000` |
| Bullet level 3 | 18pt | normal | `#000000` |
| Footer | 10pt | normal | `#666666` |
| Blockquote / citation | 20pt | italic | `#666666` |

---

## Color system

### Three presentation variants (A / B / C)

The DLR master template defines three color variants. **Colors may change between chapters, but not within a chapter.** There is no assignment of colors to research areas.

| Variant | Accent color | Use case |
|---------|-------------|----------|
| A (default) | Blue `#00658b` | Standard presentations |
| B | Green `#82a043` | Alternative chapter accent |
| C | Yellow `#d2ae3d` | Alternative chapter accent |

Apply a variant to a section-divider:
```markdown
<!-- _class: section-divider variant-b -->
# Chapter Title
```

Apply a variant to content slides within that chapter:
```markdown
<!-- _class: variant-b -->
# Slide Title
```

### Theme accent colors (from POTX `clrScheme`)

These map to CSS variables in `dlr.css`:

| Role | Hex | CSS variable |
|------|-----|-------------|
| Blue (primary accent) | `#00658b` | `--accent-color` |
| Blue mid | `#3b98cb` | `--accent-2` |
| Blue light | `#6cb9dc` | `--accent-3` |
| Blue pale | `#a7d3ec` | `--accent-4` |
| Blue tint | `#d1e8fa` | `--accent-5` |
| Teal | `#0094a8` | `--teal` |
| Sky blue | `#5f98cb` | `--sky-blue` |
| Dark charcoal | `#464646` | `--text-dark2` |
| Hyperlink blue | `#00b0f0` | `--link-color` |

### Full custom color palette (from POTX `custClrLst`)

Use these for charts, diagrams, and callouts. Use the DLR palette prompt when generating images.

**Blue scale**

| Name | Hex |
|------|-----|
| Blau 1 (primary) | `#00658b` |
| Blau 2 | `#3b98cb` |
| Blau 3 | `#6cb9dc` |
| Blau 4 | `#a7d3ec` |
| Blau 5 | `#d1e8fa` |

**Yellow scale**

| Name | Hex |
|------|-----|
| Gelb 1 | `#d2ae3d` |
| Gelb 2 | `#f2cd51` |
| Gelb 3 | `#f8de53` |
| Gelb 4 | `#fcea7a` |
| Gelb 5 | `#fff8be` |

**Green scale**

| Name | Hex |
|------|-----|
| Grün 1 | `#82a043` |
| Grün 2 | `#a6bf51` |
| Grün 3 | `#cad55c` |
| Grün 4 | `#d9df78` |
| Grün 5 | `#e6eaaf` |

**Gray scale**

| Name | Hex |
|------|-----|
| Grau 1 | `#666666` |
| Grau 2 | `#868585` |
| Grau 3 | `#b1b1b1` |
| Grau 4 | `#cfcfcf` |
| Grau 5 | `#ebebeb` |

---

## Layouts

Layouts are activated via `<!-- _class: <name> -->`. **Never use inline `<div>` + tailwind** — all layouts are defined in the theme CSS to survive PPTX export.

| Marp class | DLR template name | Use |
|------------|-------------------|-----|
| `title` | A/B/C Titel/Title | Cover slide (first slide) |
| `toc` | — | Table of contents |
| `section-divider` | A/B/C Kapitel/Chapter | Heavy accent slide between sections |
| `two-column` | A Inhalt/Content 3 | Two equal columns |
| `image-right` | A Inhalt/Content 2 | Bullets left, image right |
| `image-left` | A Inhalt/Content 2 | Image left, bullets right |
| `full-image` | Vollbild/Fullscreen Image | Full-bleed image, optional caption |
| `compare` | — | Side-by-side with colored header bands |
| `quote` | — | Centered pull-quote |
| `thanks` | — | Closing slide |
| (default) | A Inhalt/Content 1 | Title + body/bullets |

Combine with variant modifiers:
- `section-divider variant-b` — green chapter header
- `section-divider variant-c` — yellow chapter header
- `variant-b` or `variant-c` — shift content slide accent to match chapter

---

## Slide dimensions

**16:9 widescreen** — 33.87 cm × 19.05 cm (13.33 × 7.50 inches). This is the only supported format.

---

## Asset rules

- Project images: `projects/<name>/assets/`, referenced as `./assets/foo.png`
- Framework background assets (`title_back.png`, `slide_back.png`) are injected by the theme CSS — **never reference them from a deck directly**
- Charts and diagrams must use the approved DLR palette above
- All images must include an attribution in the imprint slide (see below)

---

## Image attribution

The default attribution for DLR images (required on the imprint/closing slide):

> All images "DLR (CC BY-NC-ND 3.0)" unless otherwise stated.

Third-party images must be individually attributed with source and license.

---

## Imprint slide

Every presentation requires a closing imprint slide. Minimum fields:

| Field | Example |
|-------|---------|
| Topic | Short description of the presentation |
| Date | 2025-01-01 (YYYY-MM-DD) |
| Author | First name Last name |
| Institute | Full institute name |
| Image sources | DLR (CC BY-NC-ND 3.0) unless otherwise stated |

---

## What not to do

- Do not override theme colors in individual decks with inline `style=` attributes
- Do not mix color variants within a chapter
- Do not assign color variants to specific research areas or topics
- Do not use fonts other than Arial
- Do not reference `framework/themes/dlr/assets/` images directly from a deck
