# -*- coding: utf-8 -*-
"""
DLR Corporate Design matplotlib/seaborn theme.

Original: DLR Design System, ui_kits/python_plots/dlr_style.py (wagn_ja, DLR, 2022).
Adapted for paper/figures: graceful font fallback; removed intranet references.

Usage: ``import dlr_style`` — palette + rcParams are applied on import.

Font note: Frutiger (DLR Hausschrift) is not bundled here.
           Falls back to Arial → DejaVu Sans → system sans-serif.
           Per CD-Handbuch §10.1 Arial is the mandated face for electronic
           channels (web / screen-presented PDFs).
"""
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# ── DLR Color Palette ─────────────────────────────────────────────────────────
# Source: DLR Corporate Design (colors_and_type.css / CD-Handbuch)
# Layout: 5 rows × 4 columns — [blue, yellow, green, gray] × [base/bright/dark/brighter/darker]
dlr_colors = [
    "#6cb9dc",  "#f8de53",  "#cad55c",  "#b1b1b1",  # base
    "#a7d3ec",  "#fcea7a",  "#d9df78",  "#cfcfcf",  # bright
    "#3b98cb",  "#f2cd51",  "#a6bf51",  "#868585",  # dark
    "#d1e8fa",  "#fff8be",  "#e6eaaf",  "#ebebeb",  # brighter
    "#00658b",  "#d2ae3d",  "#82a043",  "#666666",  # darker (primary brand colours)
]

# Named brand colours for convenience
DLR_BLUE      = "#00658b"   # dlr_colors[16] — primary accent
DLR_BLUE_MID  = "#3b98cb"   # dlr_colors[8]
DLR_BLUE_SOFT = "#a7d3ec"   # dlr_colors[4]
DLR_YELLOW    = "#d2ae3d"   # dlr_colors[17]
DLR_GREEN     = "#82a043"   # dlr_colors[18]
DLR_GRAY      = "#666666"   # dlr_colors[19]  — slide-title grey
DLR_GRAY_MID  = "#b1b1b1"   # dlr_colors[3]
DLR_GRAY_SOFT = "#ebebeb"   # dlr_colors[7]
DLR_HAIRLINE  = "#cfcfcf"   # dlr_colors[7] — border


def get_dlr_palette(n_colors=None, desat=None, as_cmap=False, offset=None):
    """Return DLR color palette as a seaborn color_palette.

    offset: 0=blue, 1=yellow, 2=green, 3=gray  (selects single-hue scale)
    """
    colors = get_subset(offset) if offset is not None else dlr_colors
    return sns.color_palette(colors, n_colors, desat, as_cmap)


def get_subset(offset=0):
    """Return the 5 gradations of one DLR hue (offset 0–3: blue/yellow/green/gray)."""
    if offset < 4:
        return list(np.roll(dlr_colors, offset)[0::4])
    import warnings
    warnings.warn("Only 4 hues available; offset must be < 4.")
    return dlr_colors


def get_blend_palette(offset=0, n_colors=6, as_cmap=False, multi_color=True, reverse=False):
    """Gradient palette: dark-blue → yellow (multi_color=True) or single-hue ramp."""
    color_list = [dlr_colors[16], dlr_colors[1]] if multi_color else get_subset(offset)[-2:]
    if reverse:
        color_list = list(reversed(color_list))
    return sns.blend_palette(color_list, n_colors=n_colors, as_cmap=as_cmap, input="hex")


# ── Font resolution ───────────────────────────────────────────────────────────
def _resolve_font():
    available = {f.name for f in fm.fontManager.ttflist}
    for candidate in ("Frutiger", "Arial", "Helvetica Neue", "Liberation Sans", "DejaVu Sans"):
        if candidate in available:
            return candidate
    return "sans-serif"


_FONT = _resolve_font()

# ── rcParams (DLR corporate style) ────────────────────────────────────────────
dlr_params = {
    "axes.labelcolor":   "0",
    "axes.labelsize":    10,
    "axes.labelweight":  "light",
    "text.color":        "0",
    "xtick.color":       "0",
    "ytick.color":       "0",
    "xtick.bottom":      True,
    "xtick.top":         False,
    "ytick.left":        True,
    "ytick.right":       False,
    "xtick.labelsize":   10,
    "ytick.labelsize":   10,
    "font.family":       ["sans-serif"],
    "font.sans-serif":   [_FONT, "Arial", "DejaVu Sans", "Helvetica", "sans-serif"],
    "font.weight":       "light",
    "font.size":         10,
    "lines.linewidth":   2,
    "patch.edgecolor":   "w",
    "axes.spines.right": False,
    "axes.spines.top":   False,
    "figure.facecolor":  "white",
    "axes.facecolor":    "white",
}

sns.set_theme(
    context="notebook",
    style="white",
    palette=get_dlr_palette(),
    font=_FONT,
    font_scale=1,
    color_codes=True,
    rc=dlr_params,
)
