# DLR Python Plot Style

A drop-in `matplotlib` + `seaborn` theme that ships the official DLR house colours, Frutiger/Arial typography, and the DLR-typical despined-axes look as the global default.

## Files

| File | Role |
|---|---|
| `dlr_style.py` | The theme module — import once, all subsequent plots inherit DLR styling |
| `index.html` | Visual reference — palette, parameter table, example gallery |
| `examples/*.py` | Reproducible scripts for each plot in the gallery |
| `examples/*.png` | Rendered references |
| `UPSTREAM_README.md` | Original repo README (Jan Wagner, DLR AS-EXV) |

## Usage

```python
import dlr_style          # sets the seaborn theme as a side-effect of import
import seaborn as sns
sns.lineplot(data=data)
sns.despine(offset=5, trim=True)
```

For heatmaps and many-class series, build a continuous palette:

```python
palette = dlr_style.get_blend_palette(n_colors=12)   # blue → green → yellow
sns.heatmap(matrix, cmap=palette)
```

## API surface

- `get_dlr_palette(n_colors, offset)` — the 20-colour master palette as a `seaborn.color_palette`. `offset` (0=blue · 1=grey · 2=green · 3=yellow) returns a single colour family.
- `get_subset(offset)` — five hex stops of one colour family.
- `get_blend_palette(offset, n_colors, multiColor=True)` — continuous gradient. `multiColor=True` blends across blue → yellow (heatmap-friendly); `False` blends within one family.

## Defaults the module sets

- Font family `Frutiger` with `Arial` fallback, weight `light`, size 10
- Top + right spines off; ticks black; white background; no grid
- Line width 2, white patch edges (clean bar separation)
- Default colour cycle = the 20-colour DLR palette in the documented order: blue · yellow · green · grey, repeated through the lightness band.

## Maintenance

Upstream repo by **M.Sc. Jan Wagner** — DLR Institut für Aerodynamik und Strömungstechnik, Experimentelle Verfahren (AS-EXV), Göttingen.
