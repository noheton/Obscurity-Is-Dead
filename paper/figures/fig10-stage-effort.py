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

Authorship: AI-authored (illustration agent, 2026-05-02).

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
cases  = [("spider_farmer", "Spider Farmer"),
          ("ecoflow",       "EcoFlow PowerOcean")]

fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(12, 5),
                                 gridspec_kw={"width_ratios": [3, 1]})
fig.subplots_adjust(wspace=0.32)

x = np.arange(len(stages))
bw = 0.18
offsets = {
    ("spider_farmer", "ai"):     -1.5 * bw,
    ("spider_farmer", "manual"): -0.5 * bw,
    ("ecoflow",       "ai"):      0.5 * bw,
    ("ecoflow",       "manual"):  1.5 * bw,
}
ai_color  = dlr_style.DLR_BLUE
man_color = dlr_style.DLR_GRAY_MID
case_alpha = {"spider_farmer": 1.0, "ecoflow": 0.55}

for case, _ in cases:
    sub = df[df["case"] == case].set_index("stage").reindex(stages)
    ai = sub["ai_hours"].values
    mid = sub["manual_hours_mid"].values
    lo  = sub["manual_hours_lo"].values
    hi  = sub["manual_hours_hi"].values

    ax_a.bar(x + offsets[(case, "ai")], ai, width=bw,
             color=ai_color, alpha=case_alpha[case],
             edgecolor="white", linewidth=0.8,
             label=f"{dict(cases)[case]} — AI",
             zorder=3)
    ax_a.bar(x + offsets[(case, "manual")], mid, width=bw,
             color=man_color, alpha=case_alpha[case],
             edgecolor="white", linewidth=0.8,
             yerr=[mid - lo, hi - mid],
             ecolor="#666", capsize=3,
             label=f"{dict(cases)[case]} — manual (mid · range)",
             zorder=3)

ax_a.set_xticks(x)
ax_a.set_xticklabels(stages)
ax_a.set_ylabel("Estimated effort (h)")
ax_a.set_title("Per-stage effort: AI-assisted vs manual baseline",
               fontsize=10, color=dlr_style.DLR_GRAY)
ax_a.legend(fontsize=8, frameon=False, loc="upper right", ncol=2)
ax_a.grid(axis="y", linestyle=":", alpha=0.4, zorder=0)
ax_a.set_axisbelow(True)

# Annotation: Validation is omitted for EcoFlow (rule 1)
ax_a.annotate("EcoFlow: validation phase\nnot separately captured —\nomitted (CLAUDE.md rule 1)",
              xy=(3.2, 1), xytext=(2.3, 25),
              fontsize=7.5, color="#c0392b",
              arrowprops=dict(arrowstyle="->", color="#c0392b", lw=1.0))

# ── Right panel: compression ratio per stage ────────────────────────────
ratios = []
labels = []
for case, name in cases:
    sub = df[df["case"] == case].set_index("stage").reindex(stages)
    for stg in stages:
        ai = sub.loc[stg, "ai_hours"]
        man = sub.loc[stg, "manual_hours_mid"]
        if ai and man:
            ratios.append(man / ai)
            labels.append(f"{name.split()[0]}\n{stg}")

xx = np.arange(len(ratios))
colors = [ai_color if "Spider" in lab else "#82a043" for lab in labels]
ax_b.barh(xx, ratios, color=colors, alpha=0.85, edgecolor="white", lw=0.6)
for i, r in enumerate(ratios):
    ax_b.text(r + 0.4, i, f"{r:.0f}×",
              va="center", fontsize=8, color="#333")
ax_b.set_yticks(xx)
ax_b.set_yticklabels(labels, fontsize=7.5)
ax_b.invert_yaxis()
ax_b.set_xlabel("Compression\n(manual / AI)")
ax_b.set_title("Asymmetric collapse",
               fontsize=10, color=dlr_style.DLR_GRAY)
ax_b.grid(axis="x", linestyle=":", alpha=0.4, zorder=0)
ax_b.set_axisbelow(True)

fig.suptitle("Figure 10 — Stage-by-stage effort gap (sources: §3.7, §4.7)",
             x=0.5, y=1.02, fontsize=11, color=dlr_style.DLR_GRAY,
             ha="center")

out_svg = os.path.join(HERE, "fig10-stage-effort.svg")
out_pdf = os.path.join(HERE, "fig10-stage-effort.pdf")
fig.savefig(out_svg, format="svg", bbox_inches="tight")
fig.savefig(out_pdf, format="pdf", bbox_inches="tight")
print(f"Saved: {out_svg}")
print(f"Saved: {out_pdf}")
