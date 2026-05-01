# Paper Figures

Figures 2–7 are **manually drawn SVG files** (produced in a vector-graphics
editor, not generated from data scripts) and are exempt from the Rule-14
data-source + generation-script requirement per `CLAUDE_CODE_INSTRUCTIONS.md`:

> *"Figures produced by external tools or manually drawn are exempt but must
> be noted as such in a comment in the figure directory."*

**Figure 1 is data-driven** and is Rule-14 compliant: see `fig1-effort-gap.py`
and `data/effort-gap.csv` below.

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

## Rule-14 compliance

### Figure 1 — compliant (data-driven)

| Artefact | Path | Referenced in |
|----------|------|---------------|
| Data file | `data/effort-gap.csv` | `paper/main.md` §1.1, `paper/main.tex` `\ref{fig:effort-gap}` |
| Generation script | `fig1-effort-gap.py` | same |
| Style module | `dlr_style.py` | imported by `fig1-effort-gap.py` |

Regenerate with: `python paper/figures/fig1-effort-gap.py`

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
