# Obscurity Is Dead

### AI-Assisted Hacking: Key to Interoperability or Security Nightmare?

**Author:** Florian Krebs &nbsp;·&nbsp; [ORCID 0000-0001-6033-801X](https://orcid.org/0000-0001-6033-801X) &nbsp;·&nbsp; *Independent researcher (personal capacity)*

[![License: CC-BY-4.0](https://img.shields.io/badge/License-CC--BY--4.0-lightgrey.svg)](LICENSE)
[![FAIR compliant](https://img.shields.io/badge/FAIR-compliant-blue)](docs/fair.md)
[![arXiv-ready LaTeX](https://img.shields.io/badge/paper-arXiv--ready-red)](paper/main.tex)

> **Statement of independence.** This is a hobbyist research project carried out by the author in a personal capacity. It is **not** part of, endorsed by, funded by, or representative of the views of any employer, including the German Aerospace Center (DLR). See `paper/main.md` §9.5 for the full disclaimer.

---

## What is this?

This repository is a research paper and its full supporting evidence — case studies, AI conversation transcripts, provenance maps, and methodology — published as a single, auditable, git-tracked artifact.

**Central thesis.** The dominant security posture for consumer IoT is economic, not cryptographic: proprietary protocols and obfuscated APKs raise the *effort gap* high enough that a casual researcher gives up. Large language models collapse that gap. This paper documents *how far* it has collapsed, *how asymmetrically* (faster for interoperability than for exploitation), and *what to do about it*.

---

## Key findings at a glance

| | Spider Farmer | EcoFlow PowerOcean |
|---|---|---|
| **Defence model** | AES-128-CBC keys/IVs hardcoded in APK | 3 undocumented API surfaces; vendor docs cover only one |
| **AI-assisted effort** | ~10.5 h across 7 transcripts | ~8 h across 3 transcripts |
| **Estimated manual effort** | 60–120 h | 80–160 h |
| **Effort-gap compression** | ~12% of manual | ~7% of manual |
| **Live credentials exposed** | Yes (MQTT broker) — redacted | No (token-bearer model) |
| **Dual-use blast radius** | Per-device horticulture control | Grid-in / battery-reserve / EV-charger writes |

---

## Paper figures

| | |
|---|---|
| ![Effort gap](paper/figures/fig1-effort-gap.svg) | ![Boredom barrier](paper/figures/fig2-boredom-barrier.svg) |
| *Fig 1 — The effort gap collapses with AI assistance* | *Fig 2 — AI lowers the activation energy E_a* |
| ![Spider Farmer workflow](paper/figures/fig3-spider-farmer.svg) | ![EcoFlow architecture](paper/figures/fig4-ecoflow.svg) |
| *Fig 3 — Spider Farmer: vendor APK → HA integration* | *Fig 4 — EcoFlow: cloud-bound vs local-broker* |
| ![Methodology](paper/figures/fig5-methodology.svg) | ![Dual-use map](paper/figures/fig6-dual-use.svg) |
| *Fig 5 — Four-stage methodology pipeline* | *Fig 6 — Dual-use outcome map* |
| ![Threat models](paper/figures/fig7-threat-models.svg) | |
| *Fig 7 — Perimeter model vs. per-hop authenticated model* | |

---

## Repository structure

```
Obscurity-Is-Dead/
├── paper/
│   ├── main.md              # Canonical paper source (Markdown)
│   ├── main.tex             # arXiv-ready LaTeX mirror (rule 11: must stay in sync)
│   ├── references.bib       # BibTeX bibliography
│   ├── Makefile             # Build pipeline: make pdf | make figures | make arxiv
│   └── figures/             # SVG figures (fig1–fig7) + README
├── experiments/
│   ├── spider-farmer/       # Case study 1: artifacts, transcripts, provenance
│   ├── ecoflow-powerocean/  # Case study 2: artifacts, transcripts, provenance
│   └── paper-meta-process/  # Case study 3 (recursive): paper-generation pipeline
├── docs/
│   ├── methodology.md       # Research workflow and KPI framework
│   ├── sources.md           # Literature register with verification-status legend
│   ├── logbook.md           # Session-by-session development changelog
│   ├── fair.md              # FAIR principles compliance mapping
│   ├── redaction-policy.md  # Sensitive-item register and pre-publication checklist
│   └── ethics.md            # Ethical considerations and dual-use framing
├── CITATION.cff             # Citation File Format 1.2.0
├── .zenodo.json             # Zenodo metadata (for DOI minting)
├── codemeta.json            # CodeMeta 3.0 / schema.org JSON-LD
├── LICENSE                  # CC-BY-4.0 (human-authored portions only)
└── CLAUDE_CODE_INSTRUCTIONS.md  # Canonical AI policy (14 rules)
```

---

## Reading the paper

- **Markdown source**: [`paper/main.md`](paper/main.md) — readable in any Markdown renderer.
- **arXiv-ready PDF**: build locally with `make -C paper pdf` (requires TeX Live + `rsvg-convert` or `inkscape`).
- **Section guide**:
  - §1 Introduction and Motivation — the effort-gap concept and research question
  - §2 Methodology — auditable AI-assisted RE workflow
  - §3–4 Case studies — Spider Farmer and EcoFlow PowerOcean
  - §5 Meta-process — the paper itself as a third case study
  - §6 Synthesis — cross-case comparison and limits
  - §7 Discussion — interoperability, asymmetry, proliferation risk, prompt-injection countermeasure
  - §9 AI usage disclosure — model acknowledgement, legal framing, independence
  - §10 The Pandora moment — artifact-level disclosure as a research methodology

---

## Reproducibility

Every technical claim is:
1. **Traceable** — mapped to a specific file and line number in `experiments/*/original/` at commit `ffdf60c`.
2. **Transcript-anchored** — the AI conversation that proposed it is preserved in `experiments/*/raw_conversations (copy&paste, web)/`.
3. **Verification-status labelled** — `[repo-vendored]` / `[lit-read]` / `[lit-retrieved]` / `[unverified-external]` as appropriate (see `docs/sources.md` legend).

AI outputs are **never used as authority** — only as claims to be checked against vendor code.

---

## Build the paper

```bash
# Prerequisites: TeX Live, latexmk, rsvg-convert (or inkscape)
make -C paper check        # verify toolchain
make -C paper figures      # SVG → PDF (required before first pdf build)
make -C paper pdf          # build main.pdf
```

> **Publication warning (rule 13):** `make arxiv` packages a submission tarball for *local review only*. Never upload or submit without explicit written consent from the author. See `paper/Makefile` for the full pre-publication checklist.

---

## Citation

```bibtex
@misc{krebs2026obscurity,
  author       = {Krebs, Florian},
  title        = {AI-Assisted Hacking: Key to Interoperability or Security Nightmare?},
  year         = {2026},
  howpublished = {\url{https://github.com/noheton/Obscurity-Is-Dead}},
  note         = {ORCID: 0000-0001-6033-801X. Independent researcher (personal capacity).
                  Preprint. Zenodo DOI pending first release.}
}
```

Citation metadata is also available in machine-readable formats: [`CITATION.cff`](CITATION.cff), [`.zenodo.json`](.zenodo.json), [`codemeta.json`](codemeta.json).

---

## License

The human-authored and human-curated portions of this repository are licensed under [CC-BY-4.0](LICENSE).

**Exclusions** (not covered by the CC-BY-4.0 grant):
- Vendor binaries and documentation under `experiments/*/original/doc/` — each carries its own copyright and redistribution caveats (see `docs/sources.md`).
- Items flagged for redaction in `docs/redaction-policy.md` (live credentials in prior git history — git history rewrite required before any public archive).

AI-generated text is acknowledged but is not a copyrightable contribution under § 2 UrhG (*persönliche geistige Schöpfung*). See §9.1 of the paper for the full discussion.

---

## FAIR compliance

[![F — Findable](https://img.shields.io/badge/F-Findable-green)](docs/fair.md)
[![A — Accessible](https://img.shields.io/badge/A-Accessible-green)](docs/fair.md)
[![I — Interoperable](https://img.shields.io/badge/I-Interoperable-green)](docs/fair.md)
[![R — Reusable](https://img.shields.io/badge/R-Reusable-yellow)](docs/fair.md)

See [`docs/fair.md`](docs/fair.md) for the full F1–R1.3 compliance mapping and the open issues blocking full compliance (notably: Zenodo DOI, git history rewrite, vendor redistribution).

---

*Obscurity is dead. What replaces it has to be designed, not assumed.*
