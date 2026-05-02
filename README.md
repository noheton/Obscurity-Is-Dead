# Obscurity Is Dead

### Proprietary by Design. Open by AI.

> *AI-assisted reverse engineering as a means to interoperability — and the security nightmare that comes with it.*

**TL;DR.** Consumer-IoT security has long rested on an *effort gap*: the cost of decompiling APKs and reconciling undocumented protocols was high enough to deter casual researchers. Large language models compress that gap by an order of magnitude — asymmetrically faster for interoperability than for exploitation. This repository is the paper *and* every artifact behind it: case studies, AI transcripts, provenance maps, build pipeline.

[![License: CC-BY-4.0](https://img.shields.io/badge/License-CC--BY--4.0-lightgrey.svg)](LICENSE)
[![FAIR compliant](https://img.shields.io/badge/FAIR-compliant-blue)](docs/fair.md)
[![arXiv-ready LaTeX](https://img.shields.io/badge/paper-arXiv--ready-red)](paper/main.tex)
[![Draft PDF](https://img.shields.io/badge/draft-PDF-orange)](https://github.com/noheton/Obscurity-Is-Dead/actions/workflows/build-paper.yml)
[![Figures: 16](https://img.shields.io/badge/figures-16-purple)](paper/figures/)
[![Case studies: 3](https://img.shields.io/badge/case%20studies-3-teal)](experiments/)

**Author:** Florian Krebs · [ORCID 0000-0001-6033-801X](https://orcid.org/0000-0001-6033-801X) · *Independent researcher (personal capacity).*
This is a hobbyist project. It is **not** part of, endorsed by, funded by, or representative of any employer, including the German Aerospace Center (DLR). See `paper/main.md` §9.5.

---

## Visual abstract

![Visual abstract — Eight integrated practices for AI-assisted reverse-engineering research, mapped against three failure-mode axes (sloppification, model collapse, dual-use). Source: paper §10, ILL-05.](paper/figures/fig11-eight-practices.svg)

> *Eight practices · three failure modes · one auditable workflow. Full registry: `paper/main.md` §10.*

---

## Headline numbers

| | Spider Farmer | EcoFlow PowerOcean | Meta-process (this paper) |
|---|---|---|---|
| **Defence model** | AES-128-CBC keys/IVs hardcoded in APK | 3 undocumented API surfaces; vendor docs cover only 1 | None — open by construction |
| **AI-assisted effort** | ~10.5 h across 7 transcripts | ~8 h across 3 transcripts | ~17.5 h (running) |
| **Estimated manual baseline** | 60–120 h | 80–160 h | ~300 h |
| **Effort-gap compression** | **~12 %** of manual | **~7 %** of manual | **~6 %** of manual |
| **Live credentials exposed** | Yes (MQTT) — redacted | No (token-bearer) | N/A |
| **Dual-use blast radius** | Per-device horticulture control | Grid-in / battery-reserve / EV-charger writes | Fabricated citations, unsourced legal opinions, redaction failures |

Source: `paper/main.md` §3.7, §4.7, §5.7, §6.1.

| | |
|---|---|
| ![The effort gap collapses with AI assistance.](paper/figures/fig1-effort-gap.svg) | ![Reaction-coordinate view: AI lowers the activation energy E_a.](paper/figures/fig2-boredom-barrier.svg) |
| **Fig 1** — The effort gap (data: `figures/data/effort-gap.csv`). | **Fig 2** — The boredom barrier: AI lowers *Eₐ*. |

---

## What is this?

A research paper **and** its full evidence trail — case studies, AI conversation transcripts, provenance maps, figure-generation scripts — published as a single, auditable, git-tracked artifact.

**Central thesis.** The dominant security posture for consumer IoT is economic, not cryptographic. Proprietary protocols and obfuscated APKs raise the *effort gap* high enough that a casual researcher gives up. LLMs collapse that gap. We document *how far* it has collapsed, *how asymmetrically*, and *what to do about it*.

**Read the paper:** [`paper/main.md`](paper/main.md) (Markdown source) · [`paper/main.tex`](paper/main.tex) (arXiv-ready LaTeX) · CI-built draft PDF as the `paper-pdf` artifact of the [Build paper workflow](https://github.com/noheton/Obscurity-Is-Dead/actions/workflows/build-paper.yml). Labelled *draft* until the author authorises submission (rule 13).

---

## More figures

<details>
<summary><b>Case studies, methodology, synthesis</b> — click to expand</summary>

| | |
|---|---|
| ![Spider Farmer: vendor APK → local Home Assistant integration.](paper/figures/fig3-spider-farmer.svg) | ![EcoFlow PowerOcean: cloud-bound default vs. AI-assisted local broker.](paper/figures/fig4-ecoflow.svg) |
| **Fig 3** — Spider Farmer pipeline. | **Fig 4** — EcoFlow architectures. |
| ![Four-stage methodology pipeline.](paper/figures/fig5-methodology.svg) | ![Verification-status pipeline.](paper/figures/fig9-verification-pipeline.svg) |
| **Fig 5** — Acquire → Analyse → Audit → Validate. | **Fig 9** — Two-track verification. |
| ![Dual-use outcome map.](paper/figures/fig6-dual-use.svg) | ![Per-stage AI vs. manual effort.](paper/figures/fig10-stage-effort.svg) |
| **Fig 6** — Dual-use outcome map. | **Fig 10** — Where the gap actually compresses. |

The full inventory (Figs 7, 8, 12–16, plus the Pandora bookend) lives in [`paper/figures/README.md`](paper/figures/README.md).

</details>

---

## Repository layout

```
paper/         # main.md, main.tex (rule-11 mirror), references.bib, Makefile, figures/
experiments/   # spider-farmer/, ecoflow-powerocean/, paper-meta-process/
docs/          # methodology, sources, logbook, fair, redaction-policy, ethics, prompts/
CITATION.cff · .zenodo.json · codemeta.json · LICENSE · CLAUDE.md
```

---

## Reproducibility & build

Every technical claim is **traceable** to a file/line in `experiments/*/original/` at commit `ffdf60c`, **transcript-anchored** in `experiments/*/raw_conversations (copy&paste, web)/`, and **verification-status labelled** (`[repo-vendored]` / `[lit-read]` / `[lit-retrieved]` / `[unverified-external]`). AI outputs are never used as authority — only as claims to be checked against vendor code.

```bash
make -C paper check     # verify toolchain (TeX Live, latexmk, rsvg-convert)
make -C paper figures   # SVG → PDF
make -C paper pdf       # build main.pdf
```

> **Publication warning (rule 13).** `make arxiv` packages a submission tarball *for local review only*. Never upload, push to a public mirror, or submit without explicit written consent from the author.

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

Machine-readable: [`CITATION.cff`](CITATION.cff) · [`.zenodo.json`](.zenodo.json) · [`codemeta.json`](codemeta.json).

---

## License & FAIR

Human-authored portions: [CC-BY-4.0](LICENSE). Excluded: vendor binaries/docs under `experiments/*/original/doc/` (own copyrights — see `docs/sources.md`) and items in `docs/redaction-policy.md` (git-history rewrite required before any public archive). AI-generated text is acknowledged but not a copyrightable contribution under § 2 UrhG; see paper §9.1.

[![F](https://img.shields.io/badge/F-Findable-green)](docs/fair.md)
[![A](https://img.shields.io/badge/A-Accessible-green)](docs/fair.md)
[![I](https://img.shields.io/badge/I-Interoperable-green)](docs/fair.md)
[![R](https://img.shields.io/badge/R-Reusable-yellow)](docs/fair.md)

Full F1–R1.3 mapping and open compliance issues in [`docs/fair.md`](docs/fair.md).

---

## How this README stays honest

This is the flashy front door of [`paper/main.md`](paper/main.md). Per **rule 15** of [`CLAUDE.md`](CLAUDE.md), title, thesis, headline KPIs, and figure inventory must be updated in the same commit that the paper changes any of them. If this page contradicts the paper, the paper wins — please open an issue.

*Obscurity is dead. What replaces it has to be designed, not assumed.*
