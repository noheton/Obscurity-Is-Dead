# DLR Design System — Skill manifest

**When to load this skill** — any time the user asks for a design that should look, sound, or behave like work from **DLR (Deutsches Zentrum für Luft- und Raumfahrt / German Aerospace Center)**: an institute landing page, a research deck, a report cover, a chart in DLR house style, a flyer, an executive summary.

## Quick start

```html
<link rel="stylesheet" href="colors_and_type.css">
<html data-variant="a">  <!-- a=blue (default) · b=green · c=yellow -->
```

Then compose using:
- **HTML slides (web preview)** → start from `slides/index.html`. 10 templates, 1280×720, ready to duplicate.
- **Marp slides (Markdown → PPTX/PDF)** → the canonical authoring path. Use `ui_kits/marp/`: `npm run new -- <name>`, edit `presentation.md`, `npm run build`. Read `ui_kits/marp/CLAUDE.md` and `ui_kits/marp/framework/rules/corporate-design.md` first.
- **Website** → start from `ui_kits/website/index.html`. Header / nav / hero / cards / news / team / footer.
- **Python plots** → `import dlr_style` from `ui_kits/python_plots/dlr_style.py`. Theme is set on import.
- **Tokens** → CSS variables exposed in `colors_and_type.css`.

## House rules (skim before producing)

1. **One chapter, one accent.** A=blue, B=green, C=yellow. Never mix two accents in one section/chapter. Switch with `data-variant`.
2. **Frutiger 45 Light** is the Hausschrift for Drucksachen / Briefe / Broschüren (CD-Handbuch §10.1); **Arial** is mandated for E-Mail / Web / PowerPoint. Bold for headlines and Wortmarken. Four weights shipped under `fonts/`: Light · Roman · Regular · Bold.
3. **Slide H1 in `#666` mid-grey**, not black. Body in black.
4. **Square corners.** 0–2px max. The brand reads orthogonal and report-like.
5. **Logo top-right on every slide.** Slide footer is grey, thin, contains topic / date / page.
6. **Photography, not illustration.** No emoji, no isometric tech art, no gradient backgrounds.
7. **German number format**: `16,8 %`, `638.000`. Space before `%`. Date `5.10.2011` (de) / `5 October 2011` (en, British English; *German Aerospace Center* is the only US-spelling exception).
8. **Web-Adressen**: `DLR.de` in Versalien ohne `www.`; externe URLs mit `www.`.
9. **Impressum**: Herausgeber ist immer das DLR, nie eine Einzelperson. Vorlage: `preview/brand-impressum.html`. Quelle: https://www.dlr.de/de/service/impressum.
8. **Voice is institutional, not personal.** No "you" / "Du", no marketing verbs, no exclamation marks.
9. **Photo credit boilerplate**: *"DLR (CC BY-NC-ND 3.0) sofern nicht anders angegeben."*

## Token cheat sheet

| Token | Value |
|---|---|
| `--accent` (A · default) | `#00658b` |
| `--accent` (B) | `#82a043` |
| `--accent` (C) | `#d2ae3d` |
| Body | `#000000` |
| Slide H1 grey | `#666666` |
| Hairline border | `#cfcfcf` |
| Soft block | `#ebebeb` |
| Link | `#00b0f0` |
| Slide H1 size | 28pt |
| Cover title size | 48pt |
| Web H1 / H2 / body | 32 / 22 / 15 px |

## Picking the right surface

| Ask | Use |
|---|---|
| "Make me a deck for [research topic]" (final artefact = PPTX/PDF) | `ui_kits/marp/` — scaffold with `npm run new`, write Markdown, `npm run build` |
| "Show me a deck preview in the browser" / quick web mockup | `slides/index.html` (HTML deck templates) |
| "Build the institute landing page for [center]" | `ui_kits/website/index.html` as starter |
| "Style my matplotlib chart in DLR colours" | `ui_kits/python_plots/dlr_style.py` |
| "Render a flow/architecture diagram for the deck" | `ui_kits/marp/framework/skills/mermaid/SKILL.md` (mermaid + DLR config, pre-rendered to SVG) |
| "Recreate this PDF report cover" | Title-slide template, full-bleed photo + dark-band caption pattern |
| "What's the brand grey?" | Read README → Visual foundations → Color |

## Caveats — call these out when relevant

- **Photography is rights-managed**; use placeholder blocks, don't fake DLR imagery.
- **Lucide icons are a stand-in** for DLR's in-house set. Flag substitutions explicitly.
- **Frutiger** (Light / Roman / Regular / Bold) ships in `fonts/` for print/Drucksachen; Arial is the *mandated* face for E-Mail / Web / PowerPoint per CD-Handbuch §10.1.
- **CD-Handbuch chapters** in `uploads/*Kapitel*.htm` are intranet exports — authoritative spec source, do not redistribute. Cite chapter + section number when applying a rule.

## Author / affiliation

The project owner's identity, used by default in imprints unless overridden:

- **Florian Krebs** — https://www.linkedin.com/in/florian-krebs/
- ORCID `0000-0001-6033-801X` → https://orcid.org/0000-0001-6033-801X
- DLR is a member of the **Helmholtz-Gemeinschaft** (https://www.helmholtz.de/)
- Involved in **NFDI4Ing** (https://nfdi4ing.de/) and **HMC — Helmholtz Metadata Collaboration** (https://helmholtz-metadaten.de/de)
- Mitglied der Arbeitsgruppe **„Referenzarchitekturen, Standards und Normung"** der **Plattform Industrie 4.0** (seit März 2019) — https://www.plattform-i40.de/

When producing imprint slides or report colophons, include the ORCID line and a `Verbund:` line listing Helmholtz / NFDI4Ing / HMC where the topic touches research data, metadata, or Helmholtz-funded work. For decks on industrial interoperability, reference architectures, or standardisation, additionally surface the **Plattform Industrie 4.0 / AG „Referenzarchitekturen, Standards und Normung"** affiliation. Logos for these consortia sit alongside (not replacing) the DLR logo when work is co-branded.

## Where things live

```
README.md                       ← full long-form docs (voice, visuals, iconography)
SKILL.md                        ← this file
colors_and_type.css             ← all tokens
preview/                        ← design-system tab cards
assets/                         ← logos + placeholder backgrounds
slides/index.html               ← HTML deck templates (web preview)
ui_kits/marp/                   ← marp-dlr framework (Markdown → PPTX/PDF, canonical)
ui_kits/website/                ← web product
ui_kits/python_plots/           ← matplotlib + seaborn theme
```
