#!/usr/bin/env python3
"""
Figure 12 — Test-case difficulty taxonomy (ILL-06).

Heat-map of the four device-integration case studies along three
difficulty axes (cryptographic barrier, labour to break, blast radius).
Visualises the §6.6 taxonomy spread.

The composite axis previously rendered as a fourth column has been
**dropped** from the figure (illustrator pass 2026-05-03, LAY-06
PARTIAL-fix): the preceding `tab:difficulty-taxonomy` already carries
the Composite ("Easy / Medium / Hard") rating in textual form, and
duplicating it as a heat-map column was the source of the "Med High"
two-line wrap that triggered the LAY-06 row-split warning. Removing
the Composite column also relieves text-width pressure on the figure
include and keeps the heat-map focused on the three independent axes.

Authorship: AI-authored (illustration agent, 2026-05-02; revised
2026-05-03 by illustrator pass to drop the redundant composite column
per LAY-06).

Source data: paper/figures/data/difficulty-taxonomy.csv (qualitative
ratings sourced from per-case REPORT.md evidence; aggregation rule
recorded in CSV header).
"""

import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dlr_style  # noqa: E402

DATA = os.path.join(HERE, "data", "difficulty-taxonomy.csv")
df = pd.read_csv(DATA, comment="#")

cases = df["case"].tolist()
cols = ["crypto_barrier", "labour_to_break", "blast_radius"]
col_labels = ["Crypto\nbarrier", "Labour\nto break", "Blast\nradius"]

M = df[cols].values  # rows = cases, cols = axes

fig, ax = plt.subplots(figsize=(7.2, 4.8))

# Custom colormap from DLR palette: light yellow -> dark blue
from matplotlib.colors import LinearSegmentedColormap
cmap = LinearSegmentedColormap.from_list(
    "dlr_diff",
    ["#fff8be", "#a7d3ec", "#3b98cb", "#00658b"],
)

im = ax.imshow(M, cmap=cmap, vmin=1, vmax=3, aspect="auto")

# Cell annotations
labels_for_value = {1: "Low", 1.5: "Low–Med", 2: "Medium", 2.5: "Med–High", 3: "High"}
for i in range(M.shape[0]):
    for j in range(M.shape[1]):
        v = M[i, j]
        text = labels_for_value.get(v, f"{v:g}")
        color = "white" if v >= 2.2 else "#222"
        ax.text(j, i, text, ha="center", va="center",
                fontsize=10, fontweight="bold", color=color)

ax.set_xticks(range(len(cols)))
ax.set_xticklabels(col_labels, fontsize=10)
ax.set_yticks(range(len(cases)))
ax.set_yticklabels(cases, fontsize=10)
ax.tick_params(top=False, bottom=False, left=False, right=False)

# Title
ax.set_title(
    "Test-case difficulty taxonomy — four device-integration cases",
    fontsize=12, fontweight="bold", color=dlr_style.DLR_GRAY, pad=14,
)

# Colour-bar
cbar = fig.colorbar(im, ax=ax, ticks=[1, 2, 3], shrink=0.7, pad=0.02)
cbar.ax.set_yticklabels(["Low", "Medium", "High"], fontsize=9)
cbar.outline.set_visible(False)

# Footer caption
fig.text(
    0.5, -0.02,
    "Qualitative rating along three independent axes; composite "
    "(Easy / Medium / Hard) is reported separately in the preceding "
    "table (§6.6). Source: paper/figures/data/difficulty-taxonomy.csv",
    ha="center", va="top", fontsize=8.6, style="italic",
    color=dlr_style.DLR_GRAY,
)

plt.tight_layout()
out_svg = os.path.join(HERE, "fig12-difficulty-taxonomy.svg")
out_pdf = os.path.join(HERE, "fig12-difficulty-taxonomy.pdf")
fig.savefig(out_svg, format="svg", bbox_inches="tight")
fig.savefig(out_pdf, format="pdf", bbox_inches="tight")
print(f"Saved: {out_svg}")
print(f"Saved: {out_pdf}")
