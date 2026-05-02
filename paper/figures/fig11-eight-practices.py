#!/usr/bin/env python3
"""
Figure 11 — Eight integrated practices × three failure-mode axes (ILL-05).

Conceptual diagram mapping the eight integrated practices listed in §10
(numbered items 1–8) onto the three failure-mode axes they address —
fabricated citations, prompt injection, tooling drift. Concise summary of
the paper's methodological contribution; intended as the visual abstract
for the submission.

Authorship: AI-authored (illustration agent, 2026-05-02).

Source: §10 (eight numbered practices); §7.6 (sloppification / fabricated
citations), §7.8–§7.9 (prompt injection from imported artifacts), §9.4
(tooling drift). The mapping below is the agent's reading of which
practice principally addresses which axis and is auditable against those
sections of the paper.
"""

import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dlr_style  # noqa: E402

# Eight practices (short labels; full text in §10).
practices = [
    ("1", "Conversation transcripts\nas first-class artifacts"),
    ("2", "Verification-status legend\non every cited source"),
    ("3", "Provenance maps to\ncommit-pinned evidence"),
    ("4", "Mirror discipline\n(main.md ↔ main.tex)"),
    ("5", "Recursive case study\nof the paper itself (§5)"),
    ("6", "Explicit AI disclosure\nvs empirical base rates"),
    ("7", "Legal honesty about\nauthorship (§ 2 UrhG)"),
    ("8", "FAIR alignment as a\nprecondition, not afterthought"),
]

# Failure-mode axes
axes = [
    ("Fabricated\ncitations", "#c0392b", "fab"),
    ("Prompt\ninjection",     dlr_style.DLR_BLUE, "inj"),
    ("Tooling\ndrift",        "#b8860b", "drift"),
]

# Mapping: which axis each practice principally addresses.
# Marks: "P" = principal mitigation, "S" = secondary mitigation.
mapping = {
    "1": {"fab": "S", "inj": "S", "drift": "P"},
    "2": {"fab": "P", "inj": "S", "drift": "S"},
    "3": {"fab": "P", "inj": "P", "drift": "P"},
    "4": {"fab": "S", "inj": "",  "drift": "P"},
    "5": {"fab": "S", "inj": "S", "drift": "S"},
    "6": {"fab": "P", "inj": "S", "drift": "S"},
    "7": {"fab": "S", "inj": "",  "drift": ""},
    "8": {"fab": "S", "inj": "",  "drift": "P"},
}

fig, ax = plt.subplots(figsize=(11, 7.5))
ax.set_xlim(0, 11)
ax.set_ylim(0, 8)
ax.set_axis_off()

# Header
ax.text(5.5, 7.65, "Eight integrated practices  ×  three failure-mode axes",
        ha="center", va="center", fontsize=12.5, fontweight="bold",
        color=dlr_style.DLR_GRAY)
ax.text(5.5, 7.30,
        "P = principal mitigation · S = secondary mitigation · "
        "blank = not the practice's job",
        ha="center", va="center", fontsize=9, style="italic",
        color=dlr_style.DLR_GRAY)

# Column headers (axes)
col_x = [5.7, 7.5, 9.3]
for (label, color, _), x in zip(axes, col_x):
    p = FancyBboxPatch((x - 0.7, 6.15), 1.4, 0.8,
                       boxstyle="round,pad=0.04,rounding_size=0.10",
                       fc=color, ec="white", lw=1.2, alpha=0.85)
    ax.add_patch(p)
    ax.text(x, 6.55, label, ha="center", va="center",
            fontsize=9.5, color="white", fontweight="bold")

# Practice rows
row_y0 = 5.7
row_h  = 0.62
for i, (num, label) in enumerate(practices):
    y = row_y0 - i * row_h
    # practice cell
    p = FancyBboxPatch((0.3, y - row_h / 2 + 0.05), 4.8, row_h - 0.1,
                       boxstyle="round,pad=0.03,rounding_size=0.08",
                       fc="#f6f6f6", ec=dlr_style.DLR_HAIRLINE, lw=0.8)
    ax.add_patch(p)
    ax.text(0.55, y, num, ha="center", va="center",
            fontsize=11, fontweight="bold", color=dlr_style.DLR_BLUE)
    ax.text(0.95, y, label, ha="left", va="center",
            fontsize=8.6, color="#222")

    # cells for each axis
    for (_, color, key), x in zip(axes, col_x):
        mark = mapping[num][key]
        if mark == "P":
            c = Circle((x, y), 0.22, facecolor=color, edgecolor="white",
                       lw=1.2, alpha=0.95, zorder=3)
            ax.add_patch(c)
            ax.text(x, y, "P", ha="center", va="center",
                    fontsize=9, fontweight="bold", color="white")
        elif mark == "S":
            c = Circle((x, y), 0.18, facecolor="white", edgecolor=color,
                       lw=1.6, zorder=3)
            ax.add_patch(c)
            ax.text(x, y, "S", ha="center", va="center",
                    fontsize=8, fontweight="bold", color=color)

# Footer note: integration claim
ax.text(5.5, 0.45,
        "The novelty is not any single row but the integration of all eight: "
        "every failure-mode axis is principally addressed by ≥ 1 practice and "
        "secondarily reinforced by ≥ 1 other (§10).",
        ha="center", va="center", fontsize=8.6, style="italic",
        color=dlr_style.DLR_GRAY,
        bbox=dict(boxstyle="round,pad=0.3", fc="#fff8be",
                  ec=dlr_style.DLR_HAIRLINE))

out_svg = os.path.join(HERE, "fig11-eight-practices.svg")
out_pdf = os.path.join(HERE, "fig11-eight-practices.pdf")
fig.savefig(out_svg, format="svg", bbox_inches="tight")
fig.savefig(out_pdf, format="pdf", bbox_inches="tight")
print(f"Saved: {out_svg}")
print(f"Saved: {out_pdf}")
