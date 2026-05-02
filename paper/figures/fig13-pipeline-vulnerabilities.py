#!/usr/bin/env python3
"""
Figure 13 — Vulnerabilities of IoT-integrator pipelines (ILL-07).

Conceptual diagram: six recurring system-class vulnerabilities (vendor
cloud SPoF; long-lived refresh tokens; cross-vendor flows; operational
obscurity; companion-app permission creep; static-only weakness
coverage) feeding into a central residual-risk node.

Authorship: AI-authored (illustration agent, 2026-05-02).

Source: paper/main.md §6.7 — six bullet items synthesised from the four
device case studies' Weakness Tables (W-rows) and the per-case
RESEARCH-PROTOCOL.md gap sections.
"""

import os
import sys
import math

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dlr_style  # noqa: E402

# Six recurring vulnerabilities (short labels; full text in §6.7)
nodes = [
    ("Vendor-cloud\nsingle point of failure", "3 of 4 cases cloud-bound"),
    ("Long-lived\nrefresh tokens", "Ondilo non-expiring;\nBalboa 30 d"),
    ("Cross-vendor\ndata-flow opacity", "BWG ↔ WaterGuru\n(W-5)"),
    ("Operational-obscurity\nanti-pattern", "Sound auth +\nweak ops layer"),
    ("Companion-app\npermission creep", "FCM, Play Install\nReferrer, AD_ID"),
    ("Static-only\nweakness coverage", "Reachability gap;\nlower-bound only"),
]

fig, ax = plt.subplots(figsize=(11, 7))
ax.set_xlim(0, 12)
ax.set_ylim(0, 7.5)
ax.set_axis_off()

# Title
ax.text(6, 7.05, "Vulnerabilities of IoT-integrator pipelines as a system class",
        ha="center", va="center", fontsize=12.5, fontweight="bold",
        color=dlr_style.DLR_GRAY)
ax.text(6, 6.70,
        "Six recurring patterns visible across the four device case studies (§6.7).",
        ha="center", va="center", fontsize=9, style="italic",
        color=dlr_style.DLR_GRAY)

# Central residual-risk node
cx, cy = 6.0, 3.5
central = FancyBboxPatch((cx - 1.55, cy - 0.7), 3.1, 1.4,
                         boxstyle="round,pad=0.06,rounding_size=0.18",
                         fc=dlr_style.DLR_BLUE, ec="white", lw=1.4)
ax.add_patch(central)
ax.text(cx, cy + 0.20, "System-class",
        ha="center", va="center", fontsize=11, fontweight="bold", color="white")
ax.text(cx, cy - 0.12, "residual risk",
        ha="center", va="center", fontsize=11, fontweight="bold", color="white")
ax.text(cx, cy - 0.48,
        "(integrator-side, not\nintegration-code-side)",
        ha="center", va="center", fontsize=8, style="italic", color="#e8f3fa")

# Six surrounding nodes arranged in a circle
n = len(nodes)
radius = 3.6
positions = []
for i, (label, sub) in enumerate(nodes):
    # angle: start at top-left, go clockwise
    angle = math.pi / 2 + math.pi * 2 * i / n
    nx = cx + radius * math.cos(angle) * 1.35  # widen horizontally
    ny = cy + radius * math.sin(angle) * 0.70  # squash vertically
    positions.append((nx, ny))

for (label, sub), (nx, ny) in zip(nodes, positions):
    box = FancyBboxPatch((nx - 1.35, ny - 0.55), 2.7, 1.10,
                         boxstyle="round,pad=0.04,rounding_size=0.10",
                         fc="#f6f6f6", ec=dlr_style.DLR_HAIRLINE, lw=1.0)
    ax.add_patch(box)
    ax.text(nx, ny + 0.18, label,
            ha="center", va="center", fontsize=9.2, fontweight="bold",
            color=dlr_style.DLR_BLUE)
    ax.text(nx, ny - 0.30, sub,
            ha="center", va="center", fontsize=8.2, color="#333")

    # Arrow from node toward central residual-risk node
    arrow = FancyArrowPatch(
        (nx, ny), (cx, cy),
        arrowstyle="-|>", mutation_scale=12,
        color=dlr_style.DLR_GRAY_MID, lw=1.2, alpha=0.85,
        shrinkA=22, shrinkB=42, zorder=1,
    )
    ax.add_patch(arrow)

# Footer
ax.text(6, 0.30,
        "Mitigation set is structural (governance, redaction, "
        "checkpoints) not technical — see §7.13.",
        ha="center", va="center", fontsize=8.6, style="italic",
        color=dlr_style.DLR_GRAY,
        bbox=dict(boxstyle="round,pad=0.3", fc="#fff8be",
                  ec=dlr_style.DLR_HAIRLINE))

out_svg = os.path.join(HERE, "fig13-pipeline-vulnerabilities.svg")
out_pdf = os.path.join(HERE, "fig13-pipeline-vulnerabilities.pdf")
fig.savefig(out_svg, format="svg", bbox_inches="tight")
fig.savefig(out_pdf, format="pdf", bbox_inches="tight")
print(f"Saved: {out_svg}")
print(f"Saved: {out_pdf}")
