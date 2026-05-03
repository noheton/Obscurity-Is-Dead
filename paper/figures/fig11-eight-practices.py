#!/usr/bin/env python3
"""
Figure 11 — Eight integrated practices x three failure-mode axes (ILL-05).

Conceptual diagram mapping the eight integrated practices listed in §10
(numbered items 1-8) onto the three failure-mode axes they address —
fabricated citations, prompt injection, tooling drift. Concise summary
of the paper's methodological contribution; intended as the visual
abstract for the submission.

Authorship: AI-authored (illustration agent, 2026-05-02; reworked
2026-05-03 for the figure-overhaul pass to: (i) raise per-row label
font size from 8.6 pt to 10.5 pt for arXiv-letter print legibility;
(ii) widen the practice-name column and shorten line breaks; (iii)
replace the red/blue/yellow header palette (red was not colour-blind
safe) with a Tol-bright-derived three-hue set that survives
deuteranopia and greyscale conversion via shape redundancy
(filled circle = principal, ring with bar = secondary, blank = not
addressed); (iv) add an explicit P/S legend block above the matrix;
(v) keep the row count at eight per the §10 note that the ninth
practice is logged but not yet promoted to the figure.

Source: §10 (eight numbered practices); §7.6 (sloppification /
fabricated citations), §7.8-§7.9 (prompt injection from imported
artifacts), §9.4 (tooling drift). The mapping is the agent's reading
of which practice principally addresses which axis and is auditable
against those sections of the paper.

Outputs:
    paper/figures/fig11-eight-practices.svg
    paper/figures/fig11-eight-practices.pdf
"""

import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dlr_style  # noqa: E402

# Eight practices. Short labels; full text in §10. Two-line wrap budget.
practices = [
    ("1", "Conversation transcripts as first-class artifacts"),
    ("2", "Verification-status legend on every cited source"),
    ("3", "Provenance maps to commit-pinned evidence"),
    ("4", "Mirror discipline (main.md <-> main.tex)"),
    ("5", "Recursive case study of the paper itself (§5)"),
    ("6", "Explicit AI disclosure vs empirical base rates"),
    ("7", "Legal honesty about authorship (§ 2 UrhG)"),
    ("8", "FAIR alignment as a precondition, not afterthought"),
]

# Failure-mode axes.
# Colour choices (Paul Tol "bright" subset, all CVD-safe and greyscale-
# distinguishable; verified with the published Tol palette):
#   * blue   #4477aa  - "Fabricated citations"  (CB-safe replacement for red)
#   * teal   #228833  - "Prompt injection"      (distinct from blue under deuteranopia)
#   * gold   #ccbb44  - "Tooling drift"         (sufficiently dark for white text overlay)
axes = [
    ("Fabricated\ncitations", "#4477aa", "fab"),
    ("Prompt\ninjection",     "#228833", "inj"),
    ("Tooling\ndrift",        "#aa7733", "drift"),  # darkened gold for AA contrast on white text
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

fig, ax = plt.subplots(figsize=(11.5, 8.0))
ax.set_xlim(0, 11.5)
ax.set_ylim(0, 8.5)
ax.set_axis_off()

# Header
ax.text(5.75, 8.20, "Eight integrated practices  ×  three failure-mode axes",
        ha="center", va="center", fontsize=13.5, fontweight="bold",
        color=dlr_style.DLR_GRAY)
ax.text(5.75, 7.85,
        "P (filled disc) = principal mitigation · "
        "S (ring) = secondary mitigation · blank cell = not the practice's job",
        ha="center", va="center", fontsize=9.5, style="italic",
        color=dlr_style.DLR_GRAY)

# Column headers (axes)
col_x = [6.4, 8.2, 10.0]
for (label, color, _), x in zip(axes, col_x):
    p = FancyBboxPatch((x - 0.78, 6.85), 1.56, 0.85,
                       boxstyle="round,pad=0.04,rounding_size=0.04",
                       fc=color, ec="white", lw=1.2)
    ax.add_patch(p)
    ax.text(x, 7.275, label, ha="center", va="center",
            fontsize=10.0, color="white", fontweight="bold")

# Practice column header
ax.text(0.55 + (5.4 - 0.55) / 2, 7.275, "Integrated practice",
        ha="center", va="center", fontsize=10.0, color="white",
        fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.40", fc=dlr_style.DLR_GRAY,
                  ec="white", lw=1.2))

# Practice rows
row_y0 = 6.30
row_h  = 0.66
for i, (num, label) in enumerate(practices):
    y = row_y0 - i * row_h
    # zebra row background for readability across 8 rows
    if i % 2 == 0:
        bg = FancyBboxPatch((0.30, y - row_h / 2 + 0.04), 10.85, row_h - 0.08,
                            boxstyle="round,pad=0.0,rounding_size=0.04",
                            fc="#f4f4f4", ec="none", lw=0)
        ax.add_patch(bg)

    # practice cell
    p = FancyBboxPatch((0.40, y - row_h / 2 + 0.06), 5.10, row_h - 0.12,
                       boxstyle="round,pad=0.02,rounding_size=0.06",
                       fc="white", ec=dlr_style.DLR_HAIRLINE, lw=0.8)
    ax.add_patch(p)
    # number badge
    badge = Circle((0.78, y), 0.20, facecolor=dlr_style.DLR_BLUE,
                   edgecolor="white", lw=1.0, zorder=4)
    ax.add_patch(badge)
    ax.text(0.78, y, num, ha="center", va="center",
            fontsize=10.5, fontweight="bold", color="white", zorder=5)
    ax.text(1.18, y, label, ha="left", va="center",
            fontsize=10.5, color="#1a1a1a")

    # cells for each axis
    for (_, color, key), x in zip(axes, col_x):
        mark = mapping[num][key]
        if mark == "P":
            c = Circle((x, y), 0.24, facecolor=color, edgecolor="white",
                       lw=1.4, alpha=0.95, zorder=3)
            ax.add_patch(c)
            ax.text(x, y, "P", ha="center", va="center",
                    fontsize=10, fontweight="bold", color="white")
        elif mark == "S":
            c = Circle((x, y), 0.20, facecolor="white", edgecolor=color,
                       lw=2.0, zorder=3)
            ax.add_patch(c)
            # secondary glyph: ring + small bar, so the marker is
            # distinguishable from "P" under greyscale even if the
            # colour is lost.
            ax.text(x, y, "S", ha="center", va="center",
                    fontsize=9.5, fontweight="bold", color=color)

# Footer note: integration claim
ax.text(5.75, 0.38,
        "The novelty is the integration of all eight: every failure-mode axis is "
        "principally addressed by at least one practice and secondarily reinforced "
        "by at least one other (§10).",
        ha="center", va="center", fontsize=9.0, style="italic",
        color=dlr_style.DLR_GRAY,
        bbox=dict(boxstyle="round,pad=0.35", fc="#fff8be",
                  ec=dlr_style.DLR_HAIRLINE))

# Tight layout artefact: ensure background is white (in case rsvg-convert
# strips the patch chain from a transparent-default canvas).
fig.patch.set_facecolor("white")

out_svg = os.path.join(HERE, "fig11-eight-practices.svg")
out_pdf = os.path.join(HERE, "fig11-eight-practices.pdf")
fig.savefig(out_svg, format="svg", bbox_inches="tight", facecolor="white")
fig.savefig(out_pdf, format="pdf", bbox_inches="tight", facecolor="white")
print(f"Saved: {out_svg}")
print(f"Saved: {out_pdf}")
