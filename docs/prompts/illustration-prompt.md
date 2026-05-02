# Illustration Agent Prompt — STUB

> **Status:** `stub` — This prompt is not yet executable. It is created here as a placeholder to be completed after the scientific writing pass has produced the Illustration Opportunities Registry.

## Purpose

The illustration agent takes the **Illustration Opportunities Registry** produced by the scientific writer (see `docs/prompts/scientific-writer-prompt.md`, Step 4) and produces production-ready figures for each identified opportunity.

For each `ILL-xx` annotation in `paper/main.md` and `paper/main.tex`, the agent will:

1. Determine the appropriate figure type and data requirements.
2. Source or synthesise the underlying data from the repository's verified artifacts.
3. Produce a generation script (Python/matplotlib or equivalent) and commit it to `paper/figures/`.
4. Commit the generated figure in both `.svg` and `.pdf` formats.
5. Replace the `[ILLUSTRATION OPPORTUNITY]` stub annotation with a proper `\includegraphics` / `![...]()` reference in both paper files (rule 11).
6. Register the figure in `paper/figures/README.md` per rule 14.

## Inputs (to be defined when stub is promoted)

- Illustration Opportunities Registry from the scientific writer's output
- `paper/main.md` and `paper/main.tex` with `ILL-xx` annotations
- `docs/sources.md` for verified data sources
- Per-case-study `provenance.md` files for quantitative evidence

## Constraints (carried forward from repository rules)

- Rule 14: every data-derived figure must have its data file and generation script committed alongside it.
- Rule 11: every figure placement must be mirrored between `paper/main.md` and `paper/main.tex`.
- Rule 12: no sensitive data (credentials, device identifiers) in figure data files.
- Rule 13: figures are local build artifacts only until explicit author consent for distribution.

## Stub promotion checklist

Before this file can be used as an executable agent prompt, the following must be completed:

- [ ] Scientific writing pass has been run and has produced the Illustration Opportunities Registry.
- [ ] Each `ILL-xx` entry has been reviewed by the researcher and confirmed as required.
- [ ] Priority H entries are identified as the first implementation targets.
- [ ] Data sources for each entry are confirmed available in the repository.
- [ ] This stub is replaced with a full Protocol section following the structure of `docs/prompts/scientific-writer-prompt.md`.
