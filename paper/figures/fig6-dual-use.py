#!/usr/bin/env python3
"""
Figure 6 — Dual-use scatter: interoperability gain vs security risk.

Conceptual scatter that places the four device case studies (and the
meta-process recursion) on the (interoperability-gain, security-risk)
plane and labels the four quadrants.

Authorship: AI-authored Python regenerator (illustration overhaul pass,
2026-05-03). Replaces the prior manually drawn `fig6-dual-use.svg`
(black-and-white, no `dlr_style` typography, no DLR palette,
rule-14-exempt only) with a reproducible matplotlib generator that
satisfies CLAUDE.md rule 14 (data + script committed) for what is now
a 4×-cited paper figure (the most-cited figure after fig:dual-use's
companion fig:threat-models). The encoded positions are *qualitative*
and recorded inline in the script as the data source — there is no
external CSV because the positions are an author-assigned ranking
along two ordinal axes (gain rank, risk rank), not a measurement.

The four quadrants formalise the dual-use rationale of the paper:
- "Productive interoperability" (high gain, low risk) is the goal.
- "Defensive disclosure" (low gain, high risk) is the redaction-policy
  zone (CLAUDE.md rule 12).
- "Offensive automation" (high gain, high risk) is the adversarial
  zone of §7.13/§7.14 — same artifacts, different governance.
- "Background information" (low gain, low risk) — public-domain
  facts.

Source: paper/main.md §2 (dual-use framing); §7.13, §7.14
(adversarial variants).

Outputs:
    paper/figures/fig6-dual-use.svg
    paper/figures/fig6-dual-use.pdf
"""

import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dlr_style  # noqa: E402

# Qualitative scatter data: (case label, gain_rank 0-10, risk_rank 0-10).
# Positions encode the §2 / §7.13 framing — author-assigned, ordinal.
points = [
    ("Spider Farmer\n(local BLE control)", 7.5, 2.5),
    ("EcoFlow PowerOcean\n(local energy data)", 8.2, 4.0),
    ("Ondilo ICO\n(spa telemetry)", 5.5, 3.2),
    ("Balboa GL\n(spa control)", 6.0, 5.5),
    ("Meta-process\n(this paper)", 4.0, 6.5),
    ("Adversarial\nintegrator (§7.13)", 9.0, 9.0),
]

# Quadrant labels (positions in axes coordinates 0-10 × 0-10).
quadrants = [
    (2.5, 7.5, "Defensive\ndisclosure",       "#e8f4fb"),
    (7.5, 7.5, "Offensive\nautomation",       "#fbd9dc"),
    (2.5, 2.5, "Background\ninformation",     "#f4f4f4"),
    (7.5, 2.5, "Productive\ninteroperability", "#e6eaaf"),
]

fig, ax = plt.subplots(figsize=(9.5, 7.0))

# Quadrant backgrounds.
for x, y, label, color in quadrants:
    ax.add_patch(FancyBboxPatch((x - 2.45, y - 2.45), 4.90, 4.90,
                                boxstyle="square,pad=0",
                                fc=color, ec=dlr_style.DLR_HAIRLINE,
                                lw=0.6, zorder=0))
    ax.text(x, y + 1.9, label, ha="center", va="center",
            fontsize=10.5, fontweight="bold",
            color=dlr_style.DLR_GRAY, zorder=1)

# Cross-hairs at (5,5).
ax.axvline(5, color=dlr_style.DLR_GRAY, lw=1.0, zorder=1)
ax.axhline(5, color=dlr_style.DLR_GRAY, lw=1.0, zorder=1)

# Plot points: blue for researcher-governed, orange for adversarial.
ADV = "#ee6677"
for label, gx, gy in points:
    is_adv = "Adversarial" in label
    color = ADV if is_adv else dlr_style.DLR_BLUE
    ax.scatter(gx, gy, s=140, color=color, edgecolor="white",
               lw=1.4, zorder=4)
    # Label offset per-point to avoid quadrant background label overlap.
    if "Spider" in label:
        ox, oy, ha = 0.25, 0.25, "left"
    elif "EcoFlow" in label:
        ox, oy, ha = 0.25, -0.45, "left"
    elif "Ondilo" in label:
        ox, oy, ha = -0.25, 0.30, "right"
    elif "Balboa" in label:
        ox, oy, ha = 0.25, -0.40, "left"
    elif "Meta" in label:
        ox, oy, ha = -0.25, 0.30, "right"
    else:  # adversarial
        ox, oy, ha = -0.25, -0.45, "right"
    ax.text(gx + ox, gy + oy, label, ha=ha, va="center",
            fontsize=9.5,
            color=color if is_adv else "#1a1a1a",
            fontweight="bold" if is_adv else "normal",
            zorder=5)

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect("equal")
ax.set_xticks([0, 2.5, 5, 7.5, 10])
ax.set_xticklabels(["", "low", "", "high", ""], fontsize=10)
ax.set_yticks([0, 2.5, 5, 7.5, 10])
ax.set_yticklabels(["", "low", "", "high", ""], fontsize=10)
ax.set_xlabel("Interoperability gain  →", fontsize=10.5)
ax.set_ylabel("Security risk  →", fontsize=10.5)
ax.set_title("Dual-use plane: interoperability gain × security risk",
             fontsize=12, color=dlr_style.DLR_GRAY, pad=12, fontweight="bold")
for spine in ("top", "right"):
    ax.spines[spine].set_visible(False)
ax.tick_params(length=0)
ax.grid(False)

# Legend.
ax.scatter([], [], s=140, color=dlr_style.DLR_BLUE, label="researcher-governed")
ax.scatter([], [], s=140, color=ADV, label="adversarial variant")
ax.legend(loc="lower left", fontsize=9.5, frameon=False,
          bbox_to_anchor=(0.0, -0.18), ncol=2)

fig.patch.set_facecolor("white")
plt.tight_layout()
out_svg = os.path.join(HERE, "fig6-dual-use.svg")
out_pdf = os.path.join(HERE, "fig6-dual-use.pdf")
fig.savefig(out_svg, format="svg", bbox_inches="tight", facecolor="white")
fig.savefig(out_pdf, format="pdf", bbox_inches="tight", facecolor="white")
print(f"Saved: {out_svg}")
print(f"Saved: {out_pdf}")
