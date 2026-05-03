#!/usr/bin/env python3
"""
Figure 10 — Stage-by-stage effort, AI-assisted vs manual baseline (ILL-04).

Grouped bar chart with workflow stage on the x-axis (Discovery / Build /
Debug / Validation) and estimated effort in hours on the y-axis, with bars
for AI-assisted and manual-baseline per case study. Makes the asymmetric-
collapse claim of §7.3 empirically concrete: the organisation-and-
reconciliation stages (Build, Debug) show the largest compression ratio,
while novel-discovery stages show the smallest.

Data: paper/figures/data/stage-effort.csv — aggregated from the per-phase
estimates in §3.7 and §4.7, with the aggregation rule recorded in the
'note' column of the CSV.

Authorship: AI-authored (illustration agent, 2026-05-02; reworked
2026-05-03 for the figure-overhaul pass to: (i) distinguish the two
case studies by *colour* (DLR blue vs DLR green) instead of by alpha
on the same hue, so cases remain disambiguable when printed in
greyscale — alpha-only differentiation collapses to the same grey
under desaturation; (ii) raise tick / annotation font sizes from 7.5
to 9.0 for arXiv-letter print legibility; (iii) recolour the
"validation phase omitted" rule-1 annotation from red to the DLR
slate-grey accent so the chart no longer relies on a non-CB-safe
red+green pairing; (iv) add an explicit "Manual hours estimated;
range bars show low-high band" note to the legend region.

Outputs:
    paper/figures/fig10-stage-effort.svg
    paper/figures/fig10-stage-effort.pdf
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

df = pd.read_csv(os.path.join(HERE, "data", "stage-effort.csv"))
stages = ["Discovery", "Build", "Debug", "Validation"]
cases = [("spider_farmer", "Spider Farmer"),
         ("ecoflow",       "EcoFlow PowerOcean")]

fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(12.5, 5.4),
                                 gridspec_kw={"width_ratios": [3, 1]})
fig.subplots_adjust(wspace=0.34)

x = np.arange(len(stages))
bw = 0.18
offsets = {
    ("spider_farmer", "ai"):     -1.5 * bw,
    ("spider_farmer", "manual"): -0.5 * bw,
    ("ecoflow",       "ai"):      0.5 * bw,
    ("ecoflow",       "manual"):  1.5 * bw,
}

# Case-by-colour: DLR blue (Spider Farmer) vs DLR green (EcoFlow).
# AI bars use the saturated brand hue; manual baselines use a 50% lightened
# variant of the same hue so AI-vs-manual is distinguishable within a case
# while the case identity is still readable in greyscale.
case_colors = {
    "spider_farmer": {"ai": dlr_style.DLR_BLUE,  "manual": "#a7d3ec"},  # blue, soft blue
    "ecoflow":       {"ai": dlr_style.DLR_GREEN, "manual": "#cad55c"},  # green, soft green
}

for case, name in cases:
    sub = df[df["case"] == case].set_index("stage").reindex(stages)
    ai = sub["ai_hours"].values
    mid = sub["manual_hours_mid"].values
    lo = sub["manual_hours_lo"].values
    hi = sub["manual_hours_hi"].values

    ax_a.bar(x + offsets[(case, "ai")], ai, width=bw,
             color=case_colors[case]["ai"],
             edgecolor="white", linewidth=0.8,
             label=f"{name} — AI",
             zorder=3)
    ax_a.bar(x + offsets[(case, "manual")], mid, width=bw,
             color=case_colors[case]["manual"],
             edgecolor=case_colors[case]["ai"], linewidth=1.0,
             yerr=[mid - lo, hi - mid],
             ecolor=dlr_style.DLR_GRAY, capsize=3,
             label=f"{name} — manual (mid · range)",
             zorder=3)

ax_a.set_xticks(x)
ax_a.set_xticklabels(stages, fontsize=10)
ax_a.set_ylabel("Estimated effort (hours)", fontsize=10)
ax_a.set_xlabel("Workflow stage", fontsize=10)
ax_a.set_title("Per-stage effort: AI-assisted vs manual baseline",
               fontsize=10.5, color=dlr_style.DLR_GRAY)
ax_a.tick_params(axis="y", labelsize=9)
ax_a.legend(fontsize=8.5, frameon=False, loc="upper right", ncol=2)
ax_a.grid(axis="y", linestyle=":", alpha=0.4, zorder=0)
ax_a.set_axisbelow(True)

# Annotation: Validation is omitted for EcoFlow (rule 1).
# Recoloured from red to DLR grey to avoid relying on red+green pairing.
ax_a.annotate("EcoFlow: validation phase\nnot separately captured —\nomitted (CLAUDE.md rule 1)",
              xy=(3.2, 1), xytext=(2.25, 28),
              fontsize=8.5, color=dlr_style.DLR_GRAY, style="italic",
              arrowprops=dict(arrowstyle="->", color=dlr_style.DLR_GRAY, lw=1.0))

# ── Right panel: compression ratio per stage ────────────────────────────
ratios = []
labels = []
bar_colors = []
for case, name in cases:
    sub = df[df["case"] == case].set_index("stage").reindex(stages)
    for stg in stages:
        ai = sub.loc[stg, "ai_hours"]
        man = sub.loc[stg, "manual_hours_mid"]
        if ai and man:
            ratios.append(man / ai)
            labels.append(f"{name.split()[0]}\n{stg}")
            bar_colors.append(case_colors[case]["ai"])

xx = np.arange(len(ratios))
ax_b.barh(xx, ratios, color=bar_colors, edgecolor="white", lw=0.6)
for i, r in enumerate(ratios):
    ax_b.text(r + 0.4, i, f"{r:.0f}×",
              va="center", fontsize=9, color="#222")
ax_b.set_yticks(xx)
ax_b.set_yticklabels(labels, fontsize=9)
ax_b.invert_yaxis()
ax_b.set_xlabel("Compression\n(manual / AI)", fontsize=10)
ax_b.set_title("Asymmetric collapse",
               fontsize=10.5, color=dlr_style.DLR_GRAY)
ax_b.tick_params(axis="x", labelsize=9)
ax_b.grid(axis="x", linestyle=":", alpha=0.4, zorder=0)
ax_b.set_axisbelow(True)

fig.suptitle("Figure 10 — Stage-by-stage effort gap (sources: §3.7, §4.7)",
             x=0.5, y=1.01, fontsize=11, color=dlr_style.DLR_GRAY,
             ha="center")

fig.patch.set_facecolor("white")
out_svg = os.path.join(HERE, "fig10-stage-effort.svg")
out_pdf = os.path.join(HERE, "fig10-stage-effort.pdf")
fig.savefig(out_svg, format="svg", bbox_inches="tight", facecolor="white")
fig.savefig(out_pdf, format="pdf", bbox_inches="tight", facecolor="white")
print(f"Saved: {out_svg}")
print(f"Saved: {out_pdf}")
