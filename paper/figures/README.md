# Paper Figures

Figures 2–7 are **manually drawn SVG files** (produced in a vector-graphics
editor, not generated from data scripts) and are exempt from the Rule-14
data-source + generation-script requirement per `CLAUDE_CODE_INSTRUCTIONS.md`:

> *"Figures produced by external tools or manually drawn are exempt but must
> be noted as such in a comment in the figure directory."*

**Figures 1 and 10 are data-driven** and are Rule-14 compliant: see
`fig1-effort-gap.py` + `data/effort-gap.csv` and `fig10-stage-effort.py` +
`data/stage-effort.csv` below.

**Figures 8, 9, 11, 13, 14, 15 are AI-authored programmatic diagrams**
(illustration agent, `docs/prompts/illustration-prompt.md`, 2026-05-02):
produced in response to the Illustration Opportunities Registry
(ILL-02, ILL-03, ILL-05, ILL-07, ILL-08, ILL-09). They encode
structural relationships rather than numerical data; their generation
scripts are committed for reproducibility. **Figure 12** is a
data-driven heat-map (Rule-14 compliant; ILL-06).

The Makefile (`paper/Makefile`) converts each SVG/PDF to PDF via `rsvg-convert`
(preferred) or `inkscape` before LaTeX compilation. Run `make figures` to
rebuild the PDFs.  `fig1-effort-gap.pdf` is generated directly by the Python
script and does not require SVG-to-PDF conversion.

## Figure inventory

| File | LaTeX label | Caption summary | Source |
|------|-------------|-----------------|--------|
| `fig1-effort-gap.svg` | `fig:effort-gap` | Cumulative effort vs RE phase; AI flattens the curve | **Generated** — `fig1-effort-gap.py` + `data/effort-gap.csv` |
| `fig2-boredom-barrier.svg` | `fig:boredom-barrier` | Reaction-coordinate view; AI lowers activation energy | Manually drawn |
| `fig3-spider-farmer.svg` | `fig:case-spider-farmer` | Spider Farmer workflow: vendor surface → HA integration | Manually drawn |
| `fig4-ecoflow.svg` | `fig:case-ecoflow` | EcoFlow: cloud-bound default vs AI-assisted local broker | Manually drawn |
| `fig5-methodology.svg` | `fig:methodology` | Four-stage pipeline: Acquire → Analyse → Audit → Validate | Manually drawn |
| `fig6-dual-use.svg` | `fig:dual-use` | Interoperability gain vs security risk scatter | Manually drawn |
| `fig7-threat-models.svg` | `fig:threat-models` | Single-perimeter model vs per-hop authenticated model | Manually drawn |
| `fig8-ecoflow-surfaces.svg` | `fig:ecoflow-surfaces` | Three EcoFlow API surfaces; consumer/docs/integration mapping (ILL-02) | **Generated** — `fig8-ecoflow-surfaces.py` (structural, no data file) |
| `fig9-verification-pipeline.svg` | `fig:verification-pipeline` | Verification-status pipeline; literature + artifact tracks (ILL-03) | **Generated** — `fig9-verification-pipeline.py` (structural, no data file) |
| `fig10-stage-effort.svg` | `fig:stage-effort` | Per-stage AI vs manual effort; compression ratios (ILL-04) | **Generated** — `fig10-stage-effort.py` + `data/stage-effort.csv` |
| `fig11-eight-practices.svg` | `fig:eight-practices` | Eight integrated practices × three failure-mode axes (ILL-05) | **Generated** — `fig11-eight-practices.py` (structural, no data file) |
| `fig12-difficulty-taxonomy.svg` | `fig:difficulty-taxonomy` | Test-case difficulty taxonomy heat-map across four cases (ILL-06) | **Generated** — `fig12-difficulty-taxonomy.py` + `data/difficulty-taxonomy.csv` |
| `fig13-pipeline-vulnerabilities.svg` | `fig:pipeline-vulnerabilities` | Six recurring system-class vulnerabilities of IoT-integrator pipelines (ILL-07) | **Generated** — `fig13-pipeline-vulnerabilities.py` (structural, no data file) |
| `fig14-malicious-integrator.svg` | `fig:malicious-integrator` | Researcher-governed vs malicious-integrator branching workflow (ILL-08) | **Generated** — `fig14-malicious-integrator.py` (structural, no data file) |
| `fig15-apk-mass-probing.svg` | `fig:apk-mass-probing` | Automated mass-probing pipeline for public APK repositories (ILL-09) | **Generated** — `fig15-apk-mass-probing.py` (structural, no data file) |

## Rule-14 compliance

### Figure 1 — compliant (data-driven)

| Artefact | Path | Referenced in |
|----------|------|---------------|
| Data file | `data/effort-gap.csv` | `paper/main.md` §1.1, `paper/main.tex` `\ref{fig:effort-gap}` |
| Generation script | `fig1-effort-gap.py` | same |
| Style module | `dlr_style.py` | imported by `fig1-effort-gap.py` |

Regenerate with: `python paper/figures/fig1-effort-gap.py`

### Figure 10 — compliant (data-driven)

| Artefact | Path | Referenced in |
|----------|------|---------------|
| Data file | `data/stage-effort.csv` | `paper/main.md` §7.3, `paper/main.tex` `\ref{fig:stage-effort}` |
| Generation script | `fig10-stage-effort.py` | same |
| Style module | `dlr_style.py` | imported by `fig10-stage-effort.py` |

Aggregation rule: per-stage hours are summed from the §3.7 / §4.7 KPI
tables (transcript-anchored phase estimates) into the four buckets
Discovery / Build / Debug / Validation. The aggregation is recorded in
the `note` column of `data/stage-effort.csv`. Regenerate with:
`python paper/figures/fig10-stage-effort.py`.

### Figure 12 — compliant (data-driven)

| Artefact | Path | Referenced in |
|----------|------|---------------|
| Data file | `data/difficulty-taxonomy.csv` | `paper/main.md` §6.6, `paper/main.tex` `\cref{fig:difficulty-taxonomy}` |
| Generation script | `fig12-difficulty-taxonomy.py` | same |
| Style module | `dlr_style.py` | imported by `fig12-difficulty-taxonomy.py` |

Aggregation rule: qualitative ratings (Low / Medium / Med-High / High)
mapped to numerics 1 / 2 / 2.5 / 3 in the CSV. Source of each row is
the matching `experiments/<case>/REPORT.md` and `RESEARCH-PROTOCOL.md`
files; the rating is researcher-assigned and recorded in §6.6.

### Figures 8, 9, 11, 13, 14, 15 — AI-authored programmatic diagrams

Generated by Python scripts that encode structural relationships
(diagram nodes, edges, mappings) rather than numerical data. The
scripts are committed for reproducibility and labelled as AI-authored
in their docstrings (CLAUDE.md rule 1). No external data file is
required because the structure is the content. Regenerate any of them
with `python paper/figures/fig<N>-<slug>.py`.

### Figures 2–7 — exempt (manually drawn)

These figures were produced in a vector-graphics editor and contain no
machine-readable data. They are documented here per the Rule-14 exemption
clause. If any of them are replaced by a data-driven version in a future
session, the Rule-14 table above must be updated accordingly.

### Template for future data-driven figures

1. Add raw data file (`CSV` / `JSON` / etc.) to `data/`.
2. Add a generation script (`fig<N>-<name>.py`) that reads the data and
   produces the SVG and PDF outputs.
3. Add references to both files in `paper/main.md` and `paper/main.tex` at
   the point where the figure is cited.
4. Update this README with a new row in the Rule-14 compliance table.
