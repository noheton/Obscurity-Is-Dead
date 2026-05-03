#!/usr/bin/env python3
"""
Figure 7 — Two threat models: single-perimeter "obscurity" vs zero-trust.

Side-by-side conceptual diagram contrasting (left) the
security-through-obscurity model — a single hardened perimeter with
trusted internals — against (right) the zero-trust / per-hop
authenticated model with multiple authentication boundaries.

Authorship: AI-authored Python regenerator (illustration overhaul pass,
2026-05-03). Replaces the prior manually drawn `fig7-threat-models.svg`
(monochrome, no `dlr_style` typography) with a reproducible matplotlib
generator that satisfies CLAUDE.md rule 14 (data + script committed)
for what is now a 4×-cited figure (tied with fig:dual-use as the
most-cited paper figure).

Source: paper/main.md §2 (threat-models framing); §6.7
(operational-obscurity anti-pattern); §7.13 (per-hop authentication
as mitigation).

Outputs:
    paper/figures/fig7-threat-models.svg
    paper/figures/fig7-threat-models.pdf
"""

import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dlr_style  # noqa: E402

ADV = "#ee6677"        # CB-safe orange-rose for "obscurity" model accents
ZT  = dlr_style.DLR_BLUE

fig, ax = plt.subplots(figsize=(13.0, 6.5))
ax.set_xlim(0, 13)
ax.set_ylim(0, 7.0)
ax.set_axis_off()

# Top title.
ax.text(6.5, 6.65,
        "Two threat models: security through obscurity vs zero-trust / per-hop auth",
        ha="center", va="center", fontsize=12.5, fontweight="bold",
        color=dlr_style.DLR_GRAY)

# Vertical divider between panels.
ax.plot([6.5, 6.5], [0.4, 6.2], color=dlr_style.DLR_HAIRLINE, lw=1.0)


def auth_boundary(x, y, w, h, color, lw=1.6, hatch=None):
    r = Rectangle((x, y), w, h, fc="none", ec=color, lw=lw,
                  linestyle="-", hatch=hatch, zorder=2)
    ax.add_patch(r)


def node(x, y, label, color="#f4f4f4", ec=None, tc="#1a1a1a"):
    ec = ec or dlr_style.DLR_HAIRLINE
    p = FancyBboxPatch((x - 0.55, y - 0.30), 1.10, 0.60,
                       boxstyle="round,pad=0.03,rounding_size=0.06",
                       fc=color, ec=ec, lw=1.0, zorder=3)
    ax.add_patch(p)
    ax.text(x, y, label, ha="center", va="center",
            fontsize=9.0, color=tc, zorder=4)


def arrow(x1, y1, x2, y2, color=None, lw=1.2):
    color = color or dlr_style.DLR_GRAY_MID
    a = FancyArrowPatch((x1, y1), (x2, y2),
                        arrowstyle="-|>", mutation_scale=12,
                        color=color, lw=lw, shrinkA=2, shrinkB=2)
    ax.add_patch(a)


# ── LEFT panel: Security through obscurity ─────────────────────────────
ax.text(3.25, 6.10, "Security through obscurity",
        ha="center", va="center", fontsize=11.0, fontweight="bold",
        color=ADV)
ax.text(3.25, 5.78,
        "single perimeter, trusted internals — a breach gives full reach",
        ha="center", va="center", fontsize=9.0, style="italic",
        color=dlr_style.DLR_GRAY)

# Single hardened perimeter (orange dashed = obscurity barrier).
auth_boundary(0.50, 1.00, 5.50, 4.20, ADV, lw=2.0, hatch=None)
ax.text(0.62, 4.95, "perimeter", color=ADV, fontsize=8.5, fontweight="bold")

# Internal nodes — no boundaries between them.
node(1.55, 4.10, "Companion\napp", color="#f4f4f4")
node(3.25, 4.10, "Vendor\ncloud", color="#f4f4f4")
node(4.95, 4.10, "Device", color="#f4f4f4")
node(2.40, 2.20, "DB /\ntoken store", color="#f4f4f4")
node(4.10, 2.20, "Telemetry\nbroker", color="#f4f4f4")

# Trust arrows (no auth at internal hops).
for (x1, y1, x2, y2) in [
    (1.55, 3.80, 3.25, 3.80),
    (3.25, 3.80, 4.95, 3.80),
    (3.25, 3.80, 2.40, 2.50),
    (3.25, 3.80, 4.10, 2.50),
    (2.40, 2.50, 4.10, 2.50),
]:
    arrow(x1, y1, x2, y2, color=dlr_style.DLR_GRAY)

ax.text(3.25, 0.65,
        "Failure mode: one credential captured anywhere\n"
        "inside the perimeter unlocks the whole subsystem.",
        ha="center", va="center", fontsize=9.0, style="italic",
        color=ADV)

# ── RIGHT panel: Zero-trust / per-hop auth ─────────────────────────────
ax.text(9.75, 6.10, "Zero-trust / per-hop authentication",
        ha="center", va="center", fontsize=11.0, fontweight="bold",
        color=ZT)
ax.text(9.75, 5.78,
        "every hop reauthenticates — a breach is contained at the next boundary",
        ha="center", va="center", fontsize=9.0, style="italic",
        color=dlr_style.DLR_GRAY)

# Per-hop boundaries (each node has its own auth ring).
node_positions = [
    (8.05, 4.10, "Companion\napp"),
    (9.75, 4.10, "Vendor\ncloud"),
    (11.45, 4.10, "Device"),
    (8.90, 2.20, "DB /\ntoken store"),
    (10.60, 2.20, "Telemetry\nbroker"),
]
for x, y, label in node_positions:
    # blue auth ring around each node
    auth_boundary(x - 0.78, y - 0.50, 1.56, 1.00, ZT, lw=1.6)
    node(x, y, label, color="#e8f4fb", ec=ZT)

# Per-hop arrows, each labelled with auth.
hop_label_size = 7.8
for (x1, y1, x2, y2, label) in [
    (8.05, 3.80, 9.75, 3.80, "mTLS"),
    (9.75, 3.80, 11.45, 3.80, "HMAC"),
    (9.75, 3.80, 8.90, 2.50, "scoped\ntoken"),
    (9.75, 3.80, 10.60, 2.50, "signed\nevent"),
    (8.90, 2.50, 10.60, 2.50, "row-level\nACL"),
]:
    arrow(x1, y1, x2, y2, color=ZT, lw=1.4)
    ax.text((x1 + x2) / 2, (y1 + y2) / 2 + 0.18, label,
            ha="center", va="center", fontsize=hop_label_size,
            color=ZT, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.18", fc="white",
                      ec="none", alpha=0.9))

ax.text(9.75, 0.65,
        "Failure mode is local: a captured credential is bounded by\n"
        "the scope of the next authentication ring.",
        ha="center", va="center", fontsize=9.0, style="italic",
        color=ZT)

fig.patch.set_facecolor("white")
out_svg = os.path.join(HERE, "fig7-threat-models.svg")
out_pdf = os.path.join(HERE, "fig7-threat-models.pdf")
fig.savefig(out_svg, format="svg", bbox_inches="tight", facecolor="white")
fig.savefig(out_pdf, format="pdf", bbox_inches="tight", facecolor="white")
print(f"Saved: {out_svg}")
print(f"Saved: {out_pdf}")
