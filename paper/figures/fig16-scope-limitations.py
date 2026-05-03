#!/usr/bin/env python3
"""
Figure 16 — Scope and limitations of the study (ILL-10).

Concentric perimeter diagram: an inner ring labels the five
in-scope dimensions of the study; the outside lists the corresponding
named exclusions. Visualises §7.15 (Scope and limitations of the
study) so a reader can read the perimeter of the work at a glance.

Authorship: AI-authored (illustration agent, 2026-05-02; CB-palette
+ legibility recolour 2026-05-03 — pipeline-fix pass).

Source: paper/main.md §7.15 (five numbered dimensions plus two further
constraints).

2026-05-03 changes:
  - Inner cell font raised from 7.8 pt to 9.5 pt to clear the print-
    legibility threshold (FIG-11 carry-forward).
  - Exclusion ring fill replaced from pink/red `#fadbd8` (fails
    deuteranopia) to Tol-bright orange `#ee6677` plus a hatched
    `////` pattern so "named exclusion" survives both CVD and
    greyscale; in-scope ring kept at DLR `#a7d3ec` (CB-safe blue).
  - Figure widened from 11"×9" to 12"×9.5" so the larger labels do
    not overlap.

2026-05-03 design-consistency materialisation pass: footer caption
8.6 → 9.0 pt to match the 9 pt body floor that fig11 (hero / design
anchor) sets across the figure set. No palette change.
"""

import os
import sys
import math

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Wedge

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dlr_style  # noqa: E402

# Five in-scope dimensions and their corresponding exclusions
ENTRIES = [
    ("Case base &\nsegment",
     "4 consumer-IoT cases\n+ 1 meta-process",
     "Industrial / OT / ICS /\nsafety-critical excluded"),
    ("Unit of\nanalysis",
     "AI-assisted workflow\n(artifacts + governance)",
     "Absolute LLM capability\nnot measured"),
    ("Validation\ncompleteness",
     "Spider Farmer + EcoFlow\nvalidated at ffdf60c",
     "Ondilo + Balboa\nresearcher-side pending"),
    ("Literature\nread-state",
     "Clusters A–O registered\nas [lit-retrieved]",
     "[lit-read] upgrades and\n§ 69e UrhG legal sources\nstill open"),
    ("Outputs are\ndual-use",
     "Pinned hashes; weakness\ntables; runnable smoke tests",
     "Same artifacts feed\nadversarial integrators\n(§7.13, §7.14)"),
]

fig, ax = plt.subplots(figsize=(12, 9.5))
ax.set_xlim(-7, 7)
ax.set_ylim(-7, 7)
ax.set_aspect("equal")
ax.set_axis_off()

# Title
ax.text(0, 6.5,
        "Scope and limitations of the study",
        ha="center", va="center", fontsize=13, fontweight="bold",
        color=dlr_style.DLR_GRAY)
ax.text(0, 6.05,
        "Inner ring = in-scope dimensions; outer labels = named exclusions (§7.15).",
        ha="center", va="center", fontsize=9, style="italic",
        color=dlr_style.DLR_GRAY)

# Inner perimeter ring
inner_r = 2.0
ring = Wedge((0, 0), inner_r + 0.45, 0, 360, width=0.45,
             facecolor=dlr_style.DLR_BLUE, edgecolor="white", lw=1.2,
             alpha=0.85)
ax.add_patch(ring)
ax.text(0, 0, "Study\nperimeter",
        ha="center", va="center", fontsize=11.5, fontweight="bold",
        color=dlr_style.DLR_BLUE)

n = len(ENTRIES)
inner_label_r = 3.0     # in-scope description
outer_label_r = 5.4     # exclusion description
ring_label_r  = 2.25    # short dimension name on the ring itself

for i, (short, in_scope, exclusion) in enumerate(ENTRIES):
    angle = math.pi / 2 - 2 * math.pi * i / n  # start at top, clockwise
    cx, cy = math.cos(angle), math.sin(angle)

    # Short label on the ring
    ax.text(cx * ring_label_r, cy * ring_label_r,
            short, ha="center", va="center",
            fontsize=9.2, fontweight="bold", color="white", zorder=5)

    # In-scope description (just outside ring)
    box_in = FancyBboxPatch(
        (cx * inner_label_r - 1.2, cy * inner_label_r - 0.45),
        2.4, 0.9,
        boxstyle="round,pad=0.04,rounding_size=0.10",
        fc="#a7d3ec", ec=dlr_style.DLR_HAIRLINE, lw=0.9,
    )
    ax.add_patch(box_in)
    ax.text(cx * inner_label_r, cy * inner_label_r,
            in_scope, ha="center", va="center",
            fontsize=9.5, color="#222")

    # Exclusion description (further out)
    # Tol-bright orange `#ee6677` (CB-safe) + hatched fill so the
    # "named exclusion" semantic survives deuteranopia and greyscale.
    box_ex = FancyBboxPatch(
        (cx * outer_label_r - 1.4, cy * outer_label_r - 0.55),
        2.8, 1.1,
        boxstyle="round,pad=0.04,rounding_size=0.10",
        fc="#fbe0e2", ec="#ee6677", lw=1.1,
        hatch="////",
    )
    ax.add_patch(box_ex)
    ax.text(cx * outer_label_r, cy * outer_label_r,
            exclusion, ha="center", va="center",
            fontsize=9.5, color="#222")

# Footer
ax.text(0, -6.2,
        "Two further interpretive bounds (§7.15): the recursive meta-process case is "
        "evidence for the methodology, not\nindependent confirmation; the §6.6 "
        "difficulty taxonomy is a qualitative spread, not an absolute scale.",
        ha="center", va="center", fontsize=9.0, style="italic",
        color=dlr_style.DLR_GRAY,
        bbox=dict(boxstyle="round,pad=0.3", fc="#fff8be",
                  ec=dlr_style.DLR_HAIRLINE))

# Legend
ax.add_patch(FancyBboxPatch((-6.8, -7.3), 1.6, 0.45,
                            boxstyle="round,pad=0.02,rounding_size=0.06",
                            fc="#a7d3ec", ec=dlr_style.DLR_HAIRLINE, lw=0.8))
ax.text(-5.0, -7.07, "in scope", ha="left", va="center",
        fontsize=9, color="#222")
ax.add_patch(FancyBboxPatch((-2.6, -7.3), 1.6, 0.45,
                            boxstyle="round,pad=0.02,rounding_size=0.06",
                            fc="#fbe0e2", ec="#ee6677", lw=1.0,
                            hatch="////"))
ax.text(-0.8, -7.07, "named exclusion", ha="left", va="center",
        fontsize=9, color="#222")

out_svg = os.path.join(HERE, "fig16-scope-limitations.svg")
out_pdf = os.path.join(HERE, "fig16-scope-limitations.pdf")
fig.savefig(out_svg, format="svg", bbox_inches="tight")
fig.savefig(out_pdf, format="pdf", bbox_inches="tight")
print(f"Saved: {out_svg}")
print(f"Saved: {out_pdf}")
