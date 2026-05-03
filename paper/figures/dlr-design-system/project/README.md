# DLR Design System

A faithful translation of the **DLR — Deutsches Zentrum für Luft- und Raumfahrt** corporate design (PPT-Master 1.31 EN) into web tokens, slide templates, and a website UI kit.

## Use it

```html
<!-- Tokens: variables, type scale, accent vars -->
<link rel="stylesheet" href="colors_and_type.css">
```

```html
<!-- Switch chapter accent: A blue (default) · B green · C yellow -->
<html data-variant="b">
```

The token sheet exposes:
- `--accent` (chapter accent — switches via `data-variant`)
- DLR colour ramps `--dlr-blau-1..5`, `--dlr-gruen-1..5`, `--dlr-gelb-1..5`, `--dlr-grau-1..5`
- Type scale `--type-cover-title`, `--type-h1`, `--type-h2`, `--type-body`, `--type-small`
- Font stack `--font-sans` — Frutiger (Hausschrift) → Arial fallback

## Folder map

```
README.md                  ← this file (full system documentation)
SKILL.md                   ← Claude Skill manifest — load when designing for DLR
colors_and_type.css        ← Tokens (colours · type · spacing · radii)
assets/                    ← Logos, background plates
preview/                   ← Design-system tab cards (one per token group)
slides/index.html          ← 10-slide HTML template deck (1280×720)
ui_kits/
  website/                 ← www.dlr.de institute page recreation
  marp/                    ← marp-dlr framework (Markdown → PPTX/PDF, canonical)
  python_plots/            ← matplotlib + seaborn theme module
fonts/                     ← Frutiger.ttf · Frutiger_bold.ttf (DLR Hausschrift)
```

## What's covered

| Surface | Where | Notes |
|---|---|---|
| **Tokens** (color/type/spacing) | `colors_and_type.css` + `preview/*` cards | Three chapter variants (A blue / B green / C yellow) |
| **HTML slide deck** | `slides/index.html` | Title · Section divider · Content · Two-col · Image-right · Quote · Full-image · Data table · Imprint |
| **Marp slide framework** | `ui_kits/marp/` | Authoritative `marp-dlr` snapshot — Markdown source, 11 class-based layouts, exports PPTX + PDF, mermaid skill, source-verification rules |
| **Website** | `ui_kits/website/index.html` | Utility bar, header, nav, breadcrumbs, hero, sidebar, facts strip, cards, news, team, footer |
| **Python charts** | `ui_kits/python_plots/` | matplotlib + seaborn theme (`dlr_style.py`, palette + Frutiger/Arial defaults) |

## Brand essentials (TL;DR)

**Voice** — Precise, factual, institutional. German is primary; formal "Sie" implicit; no second person, no emoji, no marketing verbs. Numbers in German format (`16,8 %`, `638.000`). Acronyms spelled out on first use. Photo credit boilerplate: *"DLR (CC BY-NC-ND 3.0) sofern nicht anders angegeben."*

**Type** — **Frutiger 45 Light** is the canonical DLR-Hausschrift (per CD-Handbuch §10.1) for all Drucksachen, Briefe und Broschüren. **Arial** is the substitute for elektronischer Dokumentenaustausch (E-Mail, Web, PowerPoint). Frutiger Bold for headlines and Wortmarken. Slide H1 in mid-grey `#666666`. 28pt slide H1, 48pt cover, 18pt body for slides; 32 / 22 / 15 px on web.

**Color** — Three chapter variants, lock within a chapter:
- A · `#00658b` (Blau) — default
- B · `#82a043` (Grün)
- C · `#d2ae3d` (Gelb)

Each has a 5-step tint ramp. Neutrals: `#666 → #ebebeb`. Hyperlink `#00b0f0`. Body text true black.

**Layout** — White backgrounds, generous whitespace, strict left edge, hairline `#cfcfcf` borders, **square corners (0–2px max)**, no gradients in chrome, no shadows on print, photography is the imagery (no illustration, no icon-led layouts).

**Logo** — Always top-right on slides. `assets/dlr-logo.svg` primary, `assets/dlr-logo-white.svg` for dark photography.

**Iconography** — Photography-led brand. Functional monoline icons only (1.5px stroke, `currentColor`); ⚠ Lucide is a stand-in for DLR's in-house set.

> Full Voice / Visual / Iconography sections — including Don'ts, examples, hover/press behaviour, and caveats — are below in the **Long-form documentation** section. Skim that before significant new work.

---

## Long-form documentation

### Sources

| Resource | Path / Link |
|---|---|
| DLR website | https://www.dlr.de/de |
| DLR Impressum | https://www.dlr.de/de/service/impressum |
| DLR in numbers | https://www.dlr.de/de/das-dlr/ueber-uns/das-dlr-in-zahlen |
| **CD-Handbuch (DLR-Intranet)** — primary canonical source | `uploads/Richtlinien-CD-Handbuch.htm` + `uploads/*Kapitel*.htm` |
| Standorte (DLR locations + 2-letter codes) | `uploads/standorte.htm` |
| Helmholtz-Gemeinschaft (parent association) | https://www.helmholtz.de/ |
| NFDI4Ing — Engineering research-data consortium | https://nfdi4ing.de/ |
| HMC — Helmholtz Metadata Collaboration | https://helmholtz-metadaten.de/de |
| Corporate design PPT master | `DLR-PPT-Master_1.31_EN.potx` |
| Logo | `assets/dlr-logo.svg` |
| Sample documents | `uploads/*.pdf` |

**CD-Handbuch chapters covered** (see `uploads/`):
1. Identitätselemente — Logo, Wortmarken, Farben, Typografie, Bildsprache
2. Geschäftspapierausstattung — Briefbogen, E-Mail-Signatur, Visitenkarte, Briefumschläge, Grußkarte, Vermerk, Protokoll
3. Digitale Medien — Standardfoliensatz (PowerPoint), Newsletter
4. Printmedien — Druckqualität, Konstruktionsprinzip, Layoutraster, Tabellen/Diagramme, Infografiken
5. Motion-CI
6. Interne Organisationsmittel — Formulare, Projektdokumentation, Urkunden, Ausweise
7. Messe- und Veranstaltungsausstattung — Roll-ups, Hintergrundwände
8. Textildesign und Außenkennzeichnung
9. Förderlogos Ministerien
10. **Wording** — Corporate Wording, Imagetext, Impressum, Autorennennung
11. Anwendung — Umsetzung, Aktualisierungen, Hilfestellung / Kontakte (`dlr-cd@dlr.de`)

### Institutional context

DLR is a member of the **Helmholtz-Gemeinschaft Deutscher Forschungszentren** — Germany's largest research association, the publisher and accreditor of much of the corporate framing this design system inherits from. Slide imprints, report colophons, and Open-Science-page footers should acknowledge this affiliation when the topic is Helmholtz-funded.

Two Helmholtz initiatives are relevant when producing research-data, software, or metadata communications from this system:

- **NFDI4Ing** (Nationale Forschungsdateninfrastruktur für die Ingenieurwissenschaften) — DLR contributes to the engineering-sciences node of the German NFDI. Cite as *"NFDI4Ing — DFG-funded research-data infrastructure for engineering sciences"* on first use.
- **HMC — Helmholtz Metadata Collaboration** — cross-Helmholtz initiative on FAIR metadata. Cite as *"Helmholtz Metadata Collaboration (HMC)"* on first use.

When producing communications connected to either initiative, surface their logos alongside (not replacing) the DLR logo in the imprint, and link the consortium homepage in the footer.

### Author / identity boilerplate

Use this block on the closing imprint slide when the deck is authored by the project owner:

```
Autor:    Florian Krebs
ORCID:    0000-0001-6033-801X
LinkedIn: linkedin.com/in/florian-krebs
Institut: DLR Zentrum für Leichtbauproduktionstechnologie (ZLP), Augsburg
Verbund:  Helmholtz-Gemeinschaft · NFDI4Ing · HMC (Helmholtz Metadata Collaboration)
Gremien:  Plattform Industrie 4.0 — AG „Referenzarchitekturen, Standards und Normung" (seit 03/2019)
Kontakt:  florian.krebs@dlr.de
```

ORCID is rendered as `https://orcid.org/0000-0001-6033-801X` (resolvable URL) on web surfaces, and as the bare iD on print/slide imprints to keep the line short. The Plattform-Industrie-4.0 line should appear when the deck topic touches industrial interoperability, reference architectures (RAMI 4.0 / Asset Administration Shell), standardisation, or interoperability across the German industrial-internet ecosystem; otherwise omit it to keep the imprint compact.

The AG „Referenzarchitekturen, Standards und Normung" works on a *lingua franca* for the industrial internet — developing the conceptual groundwork that future standards build on.

### What DLR is

- **Type**: National research center under public-law foundation, headquartered in Cologne.
- **Scale**: ~11,000 employees across 30+ German sites; ~55 institutes.
- **Domains**: Aeronautics, Space (incl. the Deutsche Raumfahrtagentur im DLR), Energy, Transport, Security, Digitalisation.
- **Outputs in this system**: Public website, long-form reports, brochures/flyers, slide decks (in 3 colour variants).

### Content fundamentals

DLR's voice is **precise, factual, and institutionally calm** — the voice of a German national research center, not a startup.

- Primary corpus is German (formal "Sie" implicit; brand rarely uses second person).
- Title Case is uncommon; sentence case is the norm with German nouns capitalised. Slide titles often "Topic — qualifier" with em-dash.
- Acronyms spelled out on first use.
- Numbers: thousands `.`, decimal `,`, space-separated `%`.
- Subjects are usually the institution or the work, not "we" / "you". When self-referential, "Das DLR".
- No exclamation marks, no marketing hype, no emoji.
- Photo credit: *"DLR (CC BY-NC-ND 3.0) sofern nicht anders angegeben."*

**Don't**
- Don't address the reader as "you" / "Du".
- Don't use emoji, casual contractions, rhetorical questions.
- Don't use marketing verbs ("revolutionize", "supercharge", "unlock").
- Don't invent statistics; cite institute, study, year.

### Visual foundations

**Type** — Frutiger is the Hausschrift, four weights shipped under `fonts/`:
- `Frutiger_light.ttf` — **Frutiger 45 Light** (300) — body, Fließtext, the DLR canonical face per CD-Handbuch §10.1
- `Frutiger_roman.ttf` — **Frutiger 55 Roman** (400) — emphasis body, captions
- `Frutiger.ttf` — Frutiger Regular (500, legacy) — kept for the existing Marp/PPTX referenced files
- `Frutiger_bold.ttf` — **Frutiger Bold** (700) — headlines, Wortmarken, Institutsnamen

Stack `"Frutiger", Arial, "Helvetica Neue", Helvetica, "Liberation Sans", system-ui, sans-serif`. Arial is mandated for E-Mail / Web / PowerPoint per CD-Handbuch §10.1; Frutiger for everything else. No italics except blockquotes/citations. Slide H1 in `#666666`.

**CD-Handbuch print typesetting (Kapitel 4)** — A4 Broschüre body: Frutiger Light, **VH 8,5 pt / ZAB 12 pt**, 100 % Schwarz. Überschrift Light VH 22 pt / ZAB 26,4 pt. Titel Light VH 24 pt / ZAB 26 pt, weiß auf Bild. Bildbeschreibung Light VH 7 pt / ZAB 8,4 pt. Linksbündiger Flattersatz, einzeilig, keine Einrückung.

**CD-Handbuch wording rules (Kapitel 10)** — Schreibweise des Datums: `5.10.2026` (deutsch), `5 October 2026` (englisch). DLR in Web-Adressen in Versalien, ohne `www.` (e.g. `DLR.de/zlp`). Externe URLs mit `www.` Anrede gestaffelt von „Sehr geehrte Damen und Herren" bis „Liebe/Lieber"; Schlussformel „Mit freundlichen Grüßen" / „Freundliche Grüße aus Köln". Englische Übersetzungen in **britischem Englisch**, einzige Ausnahme „German Aerospace Center" (US). Keine Abkürzungen im Fließtext. Länderkürzel ISO 3166 ALPHA 2.

**CD-Handbuch impressum (Kapitel 10.3)** — Herausgeber ist immer das DLR, nie eine Einzelperson. Pflichtfelder: Herausgeber, Organisationseinheit, Anschrift, Telefon, E-Mail, DLR.de-URL, Bilder-Credit „DLR (CC BY-NC-ND 3.0), soweit nicht anders angegeben.", Titelbild-Quelle. Zweisprachig DE | EN nebeneinander.

**Color** — Three chapter variants (A blue / B green / C yellow); lock within a chapter, never mix in one section. Each has a 5-step tint scale. Neutrals `#666 → #ebebeb`. Body text `#000`. Link `#00b0f0`. Teal `#0094a8` and sky `#5f98cb` as data-viz accents.

**Backgrounds & imagery** — Mostly white. Optional `#ebebeb` callout blocks. Imagery is photographic (cool cast, neutral grading, no filters). Section dividers use full-bleed photography with a dark bottom band for the title. No gradients in chrome, no textures, no patterns.

**Layout** — Generous whitespace; strict left edge. Slide frame 33.87 × 19.05 cm (16:9). Logo top-right on slides; thin grey footer with topic/date/page bottom.

**Borders, radii, shadows** — Corner radii 0–2px. No shadow on print/slide. Web hover allows `0 2px 8px rgba(0,0,0,.08)`. Hairline borders `1px solid #cfcfcf` for tables, dividers, cards.

**Animation** — Rare, functional only. 200–300ms ease-out fades. No bounces, no scroll-jacking.

**Press state** — `translateY(1px)` on buttons. No scale changes.

**Transparency & blur** — Only on cover slides for legibility (30–50% bottom gradient). No frosted glass in product UI.

**Cards** — White, hairline border, ≤2px radius, no rest shadow, optional hover shadow. Title in `#666`, body in black, optional accent rule.

### Iconography

Brand is **photography-led, not icon-led**. Icons appear sparingly and functionally.

- Website chrome icons: monoline SVG, 1.5px stroke, `currentColor`, square ends.
- No emoji, no illustration, no isometric tech art.
- No proprietary icon font shipped publicly. Closest CDN substitute: **[Lucide](https://lucide.dev)** — MIT-licensed, neutral monoline.
  - ⚠ *Lucide substitutes for the official DLR set, which is not publicly available. Replace when supplied.*
- Charts use the DLR palette + Arial labels, not iconography.

### Caveats / known gaps

- **Frutiger licensing**: The four Frutiger TTFs (Light / Roman / Regular / Bold) are shipped under `fonts/` for use within this project. Confirm embedding rights for any external distribution channel; fall back to Arial (already in the stack) where Frutiger cannot be redistributed. Per CD-Handbuch §10.1 Arial is in fact the **mandated** face for E-Mail, Web and PowerPoint — Frutiger is for Drucksachen.
- **CD-Handbuch is intranet-only**: The chapter HTMLs in `uploads/` are exports from the DLR intranet (`portal.DLR.de/CD-Handbuch`) and may not be redistributed. They are referenced here as the authoritative source for spec values; treat as internal.
- **Iconography**: Lucide is a stand-in.
- **Photography**: System ships no DLR photography (rights-managed). Use placeholder blocks; supply real images with attribution.
- **Logo dark-mode**: Inverted SVG generated locally; replace with official white variant when DLR supplies one.
