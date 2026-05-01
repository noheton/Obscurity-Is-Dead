# Paper Figures

All seven figures in this directory are **manually drawn SVG files** (produced
in a vector-graphics editor, not generated from data scripts). They are exempt
from the Rule-14 data-source + generation-script requirement per
`CLAUDE_CODE_INSTRUCTIONS.md`:

> *"Figures produced by external tools or manually drawn are exempt but must
> be noted as such in a comment in the figure directory."*

The Makefile (`paper/Makefile`) converts each SVG to PDF via `rsvg-convert`
(preferred) or `inkscape` before LaTeX compilation. Run `make figures` to
rebuild the PDFs.

## Figure inventory

| File | LaTeX label | Caption summary |
|------|-------------|-----------------|
| `fig1-effort-gap.svg` | `fig:effort-gap` | Cumulative effort vs RE phase; AI flattens the curve |
| `fig2-boredom-barrier.svg` | `fig:boredom-barrier` | Reaction-coordinate view; AI lowers activation energy |
| `fig3-spider-farmer.svg` | `fig:case-spider-farmer` | Spider Farmer workflow: vendor surface → HA integration |
| `fig4-ecoflow.svg` | `fig:case-ecoflow` | EcoFlow: cloud-bound default vs AI-assisted local broker |
| `fig5-methodology.svg` | `fig:methodology` | Four-stage pipeline: Acquire → Analyse → Audit → Validate |
| `fig6-dual-use.svg` | `fig:dual-use` | Interoperability gain vs security risk scatter |
| `fig7-threat-models.svg` | `fig:threat-models` | Single-perimeter model vs per-hop authenticated model |

## Rule-14 compliance note

If a future figure is derived from a dataset (e.g. a plot of effort-gap KPI
data), the following must be committed alongside it:

1. The raw data file (CSV / JSON / etc.) in this directory or a `data/`
   subdirectory.
2. A generation script (`plot_<figname>.py` or equivalent) that reads the
   data and produces the SVG.
3. References to both files in `paper/main.md` and `paper/main.tex` at the
   point where the figure is cited.
