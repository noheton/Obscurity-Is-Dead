# `paper/spinoff/` — F(AI)²R methodology / position paper

This directory holds an **initial-generation** spinoff paper extracted
from the parent *Obscurity Is Dead* project. The spinoff focuses
narrowly on the **F(AI)²R** proposal (a candidate FAIR extension for
AI-assisted research processes) and on the **ten-stage agent
pipeline** that operationalises the proposal in the parent
repository. The IoT reverse-engineering case studies that anchor the
parent's empirical contribution are *not* re-derived here; they are
referenced as the worked example.

## Files

| File | Purpose |
|------|---------|
| `main.md` | The spinoff paper (Markdown, single file, ≤10 pages). Initial generation drawn from `docs/fair.md` §F(AI)²R, `docs/human-ai-collaboration-process.md`, `paper/main.{md,tex}` §10, and `paper/main-condensed.{md,tex}` §4. |
| `README.md` | This file. |

## Status (rule 14 / `CLAUDE.md`)

This is a **draft, local artifact**. Distribution to a venue, an
arXiv preprint, a Zenodo deposit, or any public surface beyond the
existing GitHub repository requires explicit written consent from
the human author (Florian Krebs), recorded in
`docs/publication-consent.md` of the parent. The 2026-05-05
publication-consent record covers `docs/site/` only and does not
extend to this spinoff.

## Discipline (inherited from the parent)

The spinoff is governed by the same `CLAUDE.md` rules as the parent.
In particular:

- **Rule 1 (honesty):** every claim, mapping, and source pointer in
  `main.md` is traceable to a parent artifact (`docs/fair.md`,
  `docs/sources.md`, `paper/main.{md,tex}`, `docs/prompts/*`,
  `experiments/*/provenance.md`). The spinoff *omits*, it does not
  *add*. Where the spinoff names a number (e.g. *146 source-register
  entries*, *22 hours cumulative AI-assisted effort*), the number
  is the same as the parent's at the spinoff cut-off (2026-05-05).
- **Rule 11 (logbook chronology):** any non-trivial edit to this
  spinoff appends a logbook entry in the parent's `docs/logbook.md`
  in chronological order at end-of-file.
- **Rule 12 (mirror discipline):** there is no LaTeX mirror yet for
  this spinoff. If a venue submission is later authorised, a
  `main.tex` companion will be added and the pair will be enforced
  per the same discipline as the parent's long-form and condensed
  pairs.
- **Rule 13 (redaction):** the spinoff inherits the parent's
  redaction policy verbatim. No raw values, ever.
- **Rule 17 (condensed self-containment):** the spinoff's *Read
  the parent / extended evidentiary record* section points at
  `paper/main.md` (long-form) and `paper/main-condensed.md` (core
  submission of the parent), but the spinoff itself is
  self-contained for its own claim — F(AI)²R as a candidate and
  the ten-stage pipeline as its operationalisation.
- **Rule 18 (traceability):** the worked example in §6 of `main.md`
  cites the parent's PROV-O graph (`docs/provenance.ttl`) as the
  machine-readable rendering of the same spine the spinoff
  describes in prose.
- **Rule 19 (public-site parity):** if the spinoff is later
  surfaced on the public-facing GitHub Pages site at `docs/site/`,
  the Site Agent (stage 8) takes ownership and the rule-19
  source-pointer discipline applies (every claim has a one-step
  pointer back to its canonical source).

## How to read this

Start with `main.md`. The Abstract and §1 establish the gap that
F(AI)²R proposes to fill. §3 lists the per-axis cells. §4 documents
the verification-status ladder ↔ PRISMA 2020 / GRADE crosswalk that
resolves the I-AI-2 vocabulary-alignment open issue raised in
`docs/fair.md`. §5 lists the ten-stage pipeline. §6 reports the
worked example (the parent project itself). §7 lists the
limitations. §8 closes with the call to action.

## Future work (not blocking the initial generation)

- LaTeX mirror (`main.tex`) once a venue submission is authorised.
- Source Analyzer pass to upgrade L-FAIR-4 (PRISMA 2020) and
  L-FAIR-5 (GRADE) from `[needs-research]` to `[ai-confirmed]` so
  the spinoff can cite them as `[ai-confirmed]` rather than as
  bib stubs.
- Aligner round audit of the spinoff's claims against the parent
  (a per-claim `source-pointer` audit, analogous to the rule-19
  audit applied to `docs/site/`).
- A short illustration-opportunities registry for the spinoff: the
  parent's `fig11-eight-practices.svg` and `fig5-methodology.svg`
  are candidate inclusions; the spinoff currently omits all
  figures to stay within the 10-page ceiling on a first cut.
