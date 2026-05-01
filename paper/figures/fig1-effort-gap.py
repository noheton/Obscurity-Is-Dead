#!/usr/bin/env python3
"""
Generate Figure 1: The effort gap.

Cumulative human effort to reach a working local integration across phases of
a reverse-engineering project.  AI-assisted analysis flattens the curve,
leaving a wide effort gap between the two trajectories.

Data source : paper/figures/data/effort-gap.csv
Outputs     : paper/figures/fig1-effort-gap.svg  (referenced by paper/main.md §1.1)
              paper/figures/fig1-effort-gap.pdf  (referenced by paper/main.tex \\ref{fig:effort-gap})

Rule 14 compliance: this script and data/effort-gap.csv are the generation
script and data file for Figure 1.  Both are committed to the repository and
referenced in paper/main.md and paper/main.tex per CLAUDE_CODE_INSTRUCTIONS.md.
"""

import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.ticker import MultipleLocator
import numpy as np
import pandas as pd
import seaborn as sns

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dlr_style  # noqa: E402 — applies DLR rcParams and palette on import

# ── Load data ──────────────────────────────────────────────────────────────────
df = pd.read_csv(os.path.join(HERE, "data", "effort-gap.csv"))

# ── Named colours ──────────────────────────────────────────────────────────────
AI_COLOR   = dlr_style.DLR_BLUE       # #00658b — AI-assisted line
MAN_COLOR  = dlr_style.DLR_GRAY_MID   # #b1b1b1 — manual baseline line
GAP_FILL   = dlr_style.DLR_BLUE_SOFT  # #a7d3ec — effort-gap shading
BAR_COLORS = [dlr_style.DLR_BLUE, dlr_style.DLR_GREEN, dlr_style.DLR_YELLOW]

# ── Figure layout ─────────────────────────────────────────────────────────────
fig, (ax_main, ax_bar) = plt.subplots(
    1, 2,
    figsize=(12, 5),
    gridspec_kw={"width_ratios": [2.2, 1]},
)
fig.subplots_adjust(wspace=0.38)

# ════════════════════════════════════════════════════════════════════════════
# Panel A — Spider Farmer cumulative effort (most phases, most illustrative)
# ════════════════════════════════════════════════════════════════════════════
sf = df[df["case"] == "spider_farmer"].reset_index(drop=True)
x  = sf["phase_num"].values

# Uncertainty band on manual baseline
ax_main.fill_between(x, sf["manual_lo_cumul"], sf["manual_hi_cumul"],
                     color=MAN_COLOR, alpha=0.15, label="_nolegend_")
# Effort-gap shading
ax_main.fill_between(x, sf["ai_hours_cumul"], sf["manual_mid_cumul"],
                     color=GAP_FILL, alpha=0.55, label="Effort gap")
# Manual baseline
ax_main.plot(x, sf["manual_mid_cumul"], color=MAN_COLOR, linewidth=2.2,
             marker="o", markersize=5, zorder=3, label="Manual baseline (est.)")
# AI-assisted
ax_main.plot(x, sf["ai_hours_cumul"], color=AI_COLOR, linewidth=2.4,
             marker="o", markersize=5, zorder=4, label="AI-assisted (actual)")

# Phase labels above AI line
for _, row in sf.iterrows():
    if row["phase_num"] == 0:
        continue
    ax_main.annotate(
        row["phase_label"],
        xy=(row["phase_num"], row["ai_hours_cumul"]),
        xytext=(0, 9), textcoords="offset points",
        fontsize=7.5, ha="center", color="#444444", rotation=25,
    )

# Double-headed arrow marking the gap at the final phase
final_x = float(sf["phase_num"].iloc[-1])
ai_end  = float(sf["ai_hours_cumul"].iloc[-1])
man_end = float(sf["manual_mid_cumul"].iloc[-1])
ax_main.annotate(
    "", xy=(final_x + 0.08, man_end), xytext=(final_x + 0.08, ai_end),
    arrowprops=dict(arrowstyle="<->", color="#444444", lw=1.3),
)
ax_main.text(
    final_x + 0.22, (ai_end + man_end) / 2,
    f"{man_end / ai_end:.0f}×\nreduction",
    fontsize=8, color="#444444", va="center",
)

ax_main.set_xlabel("Workflow phase")
ax_main.set_ylabel("Cumulative effort (h)")
ax_main.set_title(
    "Case A · Spider Farmer — cumulative effort trajectory",
    fontsize=9, color=dlr_style.DLR_GRAY, pad=8,
)
ax_main.set_xlim(-0.4, len(sf) - 0.5)
ax_main.set_xticks(sf["phase_num"])
ax_main.yaxis.set_minor_locator(MultipleLocator(5))
ax_main.legend(fontsize=8.5, frameon=False, loc="upper left")

# ════════════════════════════════════════════════════════════════════════════
# Panel B — Effort-gap summary across all three cases
# ════════════════════════════════════════════════════════════════════════════
labels   = ["Spider\nFarmer", "EcoFlow\nPowerOcean", "Meta-\nprocess"]
ai_pct   = [12, 7, 5]
ai_h     = [10.5, 8.0, 15.5]
man_mid  = [90, 120, 300]

xpos = np.arange(len(labels))
bars = ax_bar.bar(xpos, ai_pct, width=0.55, color=BAR_COLORS, alpha=0.88,
                  zorder=3)

for bar, pct, ai_h_, man_ in zip(bars, ai_pct, ai_h, man_mid):
    ax_bar.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.3,
        f"{pct} %\n({ai_h_} h / ~{man_} h)",
        ha="center", va="bottom", fontsize=7.5, color="#444444",
    )

ax_bar.set_xticks(xpos)
ax_bar.set_xticklabels(labels, fontsize=8.5)
ax_bar.set_ylabel("Effort-gap metric [AI h / manual h, %]")
ax_bar.set_title(
    "Effort-gap metric — all cases",
    fontsize=9, color=dlr_style.DLR_GRAY, pad=8,
)
ax_bar.set_ylim(0, 20)
ax_bar.yaxis.set_minor_locator(MultipleLocator(1))

# ── Finish ────────────────────────────────────────────────────────────────────
sns.despine(ax=ax_main, offset=5, trim=False)
sns.despine(ax=ax_bar,  offset=5, trim=False)

fig.suptitle(
    "Figure 1 — The effort gap",
    x=0.5, y=1.01, fontsize=10, color=dlr_style.DLR_GRAY, ha="center",
)

# ── Save ──────────────────────────────────────────────────────────────────────
out_svg = os.path.join(HERE, "fig1-effort-gap.svg")
out_pdf = os.path.join(HERE, "fig1-effort-gap.pdf")

fig.savefig(out_svg, format="svg", bbox_inches="tight", dpi=150)
fig.savefig(out_pdf, format="pdf", bbox_inches="tight")
print(f"Saved: {out_svg}")
print(f"Saved: {out_pdf}")
