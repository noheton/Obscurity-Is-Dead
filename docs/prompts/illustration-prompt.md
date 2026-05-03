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
- **DLR Design System spec** at `paper/figures/dlr-design-system/`,
  curated 2026-05-03 from an upstream Claude Design handoff bundle. The
  authoritative house rules live in
  `paper/figures/dlr-design-system/project/SKILL.md`; the CSS-token
  surface in `project/colors_and_type.css`; the upstream `dlr_style.py`
  in `project/ui_kits/python_plots/` (the actually-imported adapted
  copy is at `paper/figures/dlr_style.py`); the marp corporate-design
  rule sheet at `project/ui_kits/marp/framework/rules/corporate-design.md`.
  See `paper/figures/dlr-design-system/BUNDLE-SOURCE.md` for what was
  excluded (Frutiger fonts, large brand PDFs/PPTX, background JPGs)
  and why.
- Repository rules in `CLAUDE.md` (rules 1, 2, 3, 11, 12, 13, 14).

## Authoritative house rules (DLR design system, 2026-05-03)

Before generating *any* figure, read
`paper/figures/dlr-design-system/project/SKILL.md` in full. The headline
constraints, summarised here for orientation, are mandatory and will be
enforced by the next layout-scrutinizer pass:

1. **One chapter, one accent.** Three brand variants — A=blue
   (`#00658b`, default), B=green (`#82a043`), C=yellow (`#d2ae3d`).
   Switch with `data-variant`. **Never mix two accents in one section
   or chapter.**
2. **Typography.** Frutiger 45 Light is the Hausschrift for print; *Arial
   is the mandated face for E-Mail / Web / PowerPoint and for screen-
   presented PDFs* per CD-Handbuch §10.1. The paper's `dlr_style.py`
   uses Frutiger → Arial → DejaVu Sans graceful fallback. Bold is reserved
   for headlines and Wortmarken; body weight is regular.
3. **Slide H1 in `#666` mid-grey**, not black. Body in black.
4. **Square corners.** 0–2 px max — the brand reads orthogonal and
   report-like. No pill buttons, no rounded chart bars beyond a 2 px
   radius.
5. **Photography, not illustration.** No emoji, no isometric tech art,
   no gradient backgrounds. If a figure needs a visual anchor and no
   licensed photo is available, use a typographic block with the brand
   palette rather than a clip-art-style illustration.
6. **German number format** in German-language text: `16,8 %` (note the
   space before `%`), `638.000`. English-language text follows British
   conventions: `5 October 2011`. *Exception:* "German Aerospace Center"
   is the one US-spelling allowance.
7. **Voice is institutional, not personal.** No "you" / "Du", no
   marketing verbs, no exclamation marks in captions or labels.
8. **Logo discipline.** Logo top-right on every slide; slide footer is
   thin grey, contains topic / date / page; SVG marks under
   `paper/figures/dlr-design-system/project/assets/`. *Do not use the
   marks in figures unrelated to DLR-affiliated work without re-confirming
   the licence terms* (see `BUNDLE-SOURCE.md` pre-publication note).
9. **Photo credit boilerplate** (when using DLR imagery):
   *"DLR (CC BY-NC-ND 3.0) sofern nicht anders angegeben."*
10. **Caveat — substituted icons.** The bundle's preview pages use Lucide
    as a stand-in for DLR's in-house icon set; *flag any icon
    substitution explicitly in the figure caption* (rule 1 honesty).

The brand-colour palette exported from `dlr_style.py` is the canonical
matplotlib surface for charts: prefer `DLR_BLUE` / `DLR_GREEN` /
`DLR_YELLOW` / `DLR_GRAY` named constants over raw hex codes so a
future palette revision propagates without per-figure edits.

## Protocol

For each `ILL-xx` entry, the agent performs the following steps in order.
A run that completes all five entries produces a single commit on the
designated feature branch.

### 1. Classify the entry

| Annotation type | Realisation | Files produced |
|-----------------|-------------|----------------|
| `comparison-table` | Native Markdown / LaTeX table inlined in the paper | (no figure files) |
| `bar-chart` / data-derived chart | Python script + CSV → SVG + PDF | `figs/data/<name>.csv`, `fig<N>-<name>.py`, `.svg`, `.pdf` |
| `architecture-diagram` / `workflow-diagram` / `conceptual-diagram` | Python script (matplotlib) → SVG + PDF, **or** Mermaid (`.mmd` → `.svg`/`.pdf`), **or** TikZ (`.tex` fragment compiled inline by `paper/main.tex`) | `fig<N>-<name>.{py,mmd,tex}` + `.svg`/`.pdf` as applicable |

Diagrams without numeric data are still produced from a reproducible
source (Python, Mermaid, or TikZ) so they survive Rule 14 spirit, even
though the data they encode is structural rather than empirical.

**Toolchain choice (added 2026-05-03, claude/check-illustration-pipeline).**
The following rendering paths are sanctioned; pick the one that fits the figure:

1. **Python + matplotlib** (default, used by fig1 and fig6–fig16). Best
   for charts, scatter plots, and any figure driven by tabular data.
   Source: `fig<N>-<slug>.py`. Must emit both `.svg` and `.pdf` next to
   itself; `paper/Makefile` regenerates these via the
   `$(SCRIPTED_FIG_PDFS)` rule whenever the `.py` (or `dlr_style.py`)
   changes.
2. **Mermaid** for flowcharts, sequence diagrams, and state machines
   that read more clearly as Mermaid than as matplotlib boxes-and-arrows.
   Source: `fig<N>-<slug>.mmd`. Render to SVG+PDF via `mmdc` (Mermaid
   CLI) — add a Makefile rule mirroring the matplotlib one so edits
   propagate. Stick to the Tol-bright / DLR palette in the theme block.
3. **TikZ** (incl. `pgfplots`, `circuitikz`, `bytefield`) when the figure
   benefits from being typeset alongside the paper (matched fonts, math
   mode, `\ref`-able nodes). Source: a `fig<N>-<slug>.tex` fragment
   included from `paper/main.tex` via
   `\input{figures/fig<N>-<slug>.tex}` inside a `figure` environment;
   no separate `.pdf` artefact — `latexmk` rebuilds it as part of
   `make pdf`. Keep TikZ libraries declared in `paper/main.tex`
   preamble, not inside the fragment. Use `circuitikz` for hardware
   schematics (PowerOcean / EcoFlow internals) and `bytefield` for
   protocol-frame diagrams in reverse-engineering sections — both are
   reproducible and Rule-14-clean.
4. **Graphviz / D2** when the diagram is topology-driven (trust graphs,
   threat graphs, dependency / call graphs) and the layout should
   follow the structure rather than be hand-placed. Source:
   `fig<N>-<slug>.dot` (Graphviz) or `fig<N>-<slug>.d2` (D2). Render to
   `.svg` + `.pdf` via `dot -Tpdf` / `d2 fmt`; add a Makefile rule
   mirroring the matplotlib one. Prefer D2 for new diagrams (better
   defaults), Graphviz where reviewers expect it.
5. **Altair / Vega-Lite** for declarative statistical charts where the
   spec-plus-data style is a stronger Rule-14 fit than imperative
   matplotlib. Source: `fig<N>-<slug>.py` emitting Vega-Lite JSON, or a
   committed `fig<N>-<slug>.vl.json` rendered via `vl-convert`. Output
   `.svg` + `.pdf`.
6. **Inkscape `--export-latex`** when a complex vector composition
   needs LaTeX-typeset labels (best math / font fidelity). Source:
   committed `fig<N>-<slug>.svg`; build emits `.pdf` + `.pdf_tex`
   sidecar that `paper/main.tex` `\input`s. Use sparingly — manual
   composition costs reproducibility.
7. **drawio / diagrams.net** as an *exception* path for hand-composed
   architecture diagrams when none of the above fit. Source: committed
   `fig<N>-<slug>.drawio` XML rendered via the drawio CLI. Mark such
   figures with an "AI-authored, manually composed" note in the
   caption — they are Rule-14-degraded and should be migrated to a
   reproducible path when the structure stabilises.

Whichever path is chosen, Rule 14 still applies: the source file
(`.py` / `.mmd` / `.tex` / `.dot` / `.d2` / `.vl.json` / `.svg` /
`.drawio`) and any input data must be committed and referenced from
the figure caption / `paper/figures/README.md`. Whenever a new path
is exercised for the first time, add the corresponding build rule to
`paper/Makefile` so the figure regenerates on source edits — same
spirit as the `$(SCRIPTED_FIG_PDFS)` rule for matplotlib.

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
- For figures: place the source and any data file under `paper/figures/`
  following the naming pattern `fig<N>-<short-slug>.{py,mmd,tex}` plus
  `.svg`/`.pdf` artefacts where applicable. Python scripts must be
  runnable as `python paper/figures/fig<N>-<slug>.py` and emit both
  `.svg` and `.pdf` next to themselves. Mermaid sources (`.mmd`) render
  via `mmdc` to `.svg`+`.pdf`. TikZ fragments (`.tex`) are included
  directly from `paper/main.tex` and require no separate artefact. Use
  `dlr_style.py` (Python) or the equivalent Tol-bright / DLR palette
  values (Mermaid theme block, TikZ `\definecolor`) for consistent
  styling across all three paths.
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

- For Python sources: run `make -C paper figures` and confirm `.svg` +
  `.pdf` are regenerated for every changed `.py`. The Makefile's
  `$(SCRIPTED_FIG_PDFS)` rule (added 2026-05-03) is the canonical entry
  point — direct invocation of individual `.py` files is acceptable as
  a sanity check but `make figures` must also succeed.
- For Mermaid sources: run the corresponding `mmdc` rule and verify
  `.svg` + `.pdf` are produced.
- For TikZ fragments: run `make -C paper pdf` and confirm the figure
  renders inline without missing-package or undefined-reference errors.
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
