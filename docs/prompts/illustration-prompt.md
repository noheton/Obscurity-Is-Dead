# Illustration Agent Prompt

> **Status:** `executable` — promoted from stub on 2026-05-02 after the
> scientific writer pass produced the Illustration Opportunities Registry
> (ILL-01 .. ILL-05) in `paper/main.md` and `paper/main.tex`.

## Purpose

The illustration agent takes the **Illustration Opportunities Registry** —
the set of `[ILLUSTRATION OPPORTUNITY] ILL-xx` annotations placed in the
paper by the scientific writer (see `docs/prompts/scientific-writer-prompt.md`,
Step 4) — and produces production-ready figures for each entry, replacing
the placeholder annotations with real figure (or table) references in both
`paper/main.md` and `paper/main.tex`.

## Inputs

- The five `ILL-xx` registry entries currently in the paper:
  | ID | Type | Anchor section | Source data |
  |----|------|---------------|-------------|
  | ILL-01 | comparison-table | §3.3 (Spider Farmer reconciliation) | `experiments/spider-farmer/original/doc/apk_analysis/implementations.md` and `experiments/spider-farmer/original/const.py` |
  | ILL-02 | architecture-diagram | §4.3 (EcoFlow three surfaces) | `experiments/ecoflow-powerocean/original/doc/apk.md` (referenced from prose) |
  | ILL-03 | workflow-diagram | §5/§7.6 (verification-status pipeline) | `docs/sources.md` legend; `docs/methodology.md` |
  | ILL-04 | bar-chart | §7.3 (asymmetric collapse) | `paper/figures/data/effort-gap.csv` aggregated to four stages |
  | ILL-05 | conceptual-diagram | §10 (eight integrated practices) | §10 list of practices; §7.6 / §7.7 failure-mode taxonomy |
- Existing figure infrastructure: `paper/figures/dlr_style.py`,
  `paper/figures/Makefile` toolchain via `paper/Makefile`, the Rule-14
  template documented in `paper/figures/README.md`.
- Repository rules in `CLAUDE.md` (rules 1, 2, 3, 11, 12, 13, 14).

## Protocol

For each `ILL-xx` entry, the agent performs the following steps in order.
A run that completes all five entries produces a single commit on the
designated feature branch.

### 1. Classify the entry

| Annotation type | Realisation | Files produced |
|-----------------|-------------|----------------|
| `comparison-table` | Native Markdown / LaTeX table inlined in the paper | (no figure files) |
| `bar-chart` / data-derived chart | Python script + CSV → SVG + PDF | `figs/data/<name>.csv`, `fig<N>-<name>.py`, `.svg`, `.pdf` |
| `architecture-diagram` / `workflow-diagram` / `conceptual-diagram` | Python script (matplotlib) → SVG + PDF | `fig<N>-<name>.py`, `.svg`, `.pdf` |

Diagrams without numeric data are still produced from a Python script so
they remain reproducible (Rule 14 spirit), even though the data they encode
is structural rather than empirical.

### 2. Source the underlying data

- Quote or aggregate from artifacts already committed to the repository.
  Do **not** invent numbers; if data is missing, surface the gap in the
  logbook and skip the entry rather than fabricate (CLAUDE.md rule 1).
- For derived numbers (e.g., aggregated stage effort), record the
  aggregation rule in a comment in the generation script and the data
  CSV.
- *Verified-source data preference (2026-05-02 update).* When a
  data-driven figure can plausibly use numbers from a `docs/sources.md`
  entry, prefer entries marked `[ai-confirmed]` or `[lit-read]` over
  entries marked `[lit-retrieved]`. Quote the value verbatim from the
  Source Analyzer's recorded passage (or the human reader's note) and
  cite the entry ID in the figure caption. If only `[lit-retrieved]`
  evidence is available for a number you would otherwise plot, halt
  the figure and file a hand-back to the Source Analyzer requesting
  upgrade to `[ai-confirmed]` before the figure ships.

### 3. Generate the artifact

- For tables: write the rendered table directly into `paper/main.md`
  (Markdown table) and `paper/main.tex` (`tabular` / `tabularx` env with
  matching `\caption` and `\label`).
- For figures: place the script and any data file under `paper/figures/`
  following the naming pattern `fig<N>-<short-slug>.{py,svg,pdf}`. The
  script must be runnable as `python paper/figures/fig<N>-<slug>.py` and
  emit both `.svg` and `.pdf` next to itself. Use `dlr_style.py` for
  consistent styling.
- Honesty (CLAUDE.md rule 1): the script docstring must label the figure
  as **AI-authored** and identify the prompt that generated it.

### 4. Replace the registry annotation

In **both** `paper/main.md` and `paper/main.tex` (CLAUDE.md rule 11):

- Remove the `> **[ILLUSTRATION OPPORTUNITY]** ILL-xx ...` block (md) and
  the matching `% [ILLUSTRATION OPPORTUNITY] ILL-xx ...` comment (tex).
- For tables: insert the table at the same anchor with a caption that
  references the prose claim it supports.
- For figures: insert
  - in markdown: `![Figure N — caption](figures/fig<N>-<slug>.svg)`
  - in LaTeX: a `figure` environment with `\includegraphics`, `\caption`,
    and `\label` matching the markdown caption.

### 5. Register the artifact

- Append a row to the inventory table in `paper/figures/README.md`.
- For data-driven figures, also fill in the Rule-14 compliance subsection
  with paths to the data file, generation script, and the prose locations
  that cite the figure.
- Append a logbook entry to `docs/logbook.md` describing which `ILL-xx`
  entries were materialised, with paths to the generated artifacts.

### 6. Build and validate

- Run each generation script and confirm `.svg` + `.pdf` are produced.
- Run `python -c "import paper.main"` is **not** applicable; instead
  verify that `paper/main.md` and `paper/main.tex` are consistent
  (CLAUDE.md rule 11): same caption text, same number of figure
  references, no orphaned `ILL-xx` annotation in either file.
- Do **not** run `make arxiv` (CLAUDE.md rule 13). Local `make pdf` is
  permitted but not required for this stage.

## Constraints (carried forward from repository rules)

- **Rule 1 — Honesty.** Every figure script is labelled as AI-authored in
  its docstring. Numbers shown in figures must be sourced from committed
  artifacts; aggregations must document the rule.
- **Rule 2 — Origin of findings.** Each figure caption ends with a
  parenthetical pointing to the source artifact (CSV path, transcript ID,
  or section anchor).
- **Rule 11 — Mirror discipline.** `paper/main.md` and `paper/main.tex`
  must contain the same set of figure references after the run.
- **Rule 12 — Redaction.** No live credentials, device serial numbers,
  or private UIDs in figure data files or labels.
- **Rule 13 — No publication.** Figures are local build artifacts only.
- **Rule 14 — Data + script committed.** Data-driven figures require
  both a data file and a generation script to be committed and
  registered in `paper/figures/README.md`.
- **Rule 15 — README mirror.** When a figure is added, replaced, or
  retired, the top-level `README.md` gallery must be updated in the
  same commit so the flashy front door stays consistent with the
  paper. The visual abstract (currently `fig11-eight-practices.svg`)
  is the README's hero image; other figures slot into the case-study,
  methodology, or synthesis groups by section anchor.

## Output

A single feature-branch commit containing:

1. New / replaced figure scripts and assets under `paper/figures/`.
2. Updated `paper/main.md` and `paper/main.tex` with the five `ILL-xx`
   placeholders replaced by real table or figure references.
3. Updated `paper/figures/README.md` inventory.
4. Updated `docs/logbook.md` with a session entry summarising what was
   produced.

## Stub-promotion record

This file was promoted from `stub` to `executable` on **2026-05-02** by
the illustration agent run requested in session
`claude/run-illustration-agent-IRJKO`. The promotion satisfied the
checklist that previously appeared at the bottom of this file:

- [x] Scientific writing pass completed; Illustration Opportunities
  Registry present as ILL-01 .. ILL-05 in `paper/main.{md,tex}`.
- [x] Each entry reviewed against repository sources for data
  availability before script generation.
- [x] Priority H (visual abstract): ILL-05.
- [x] Stub replaced with the Protocol section above.
