#!/usr/bin/env python3
"""
Figure 14 — The malicious IoT-integrator agent (ILL-08).

Side-by-side branching workflow contrasting the researcher-governed
IoT-Integrator pipeline (left) against a malicious-integrator variant
(right) that diverges at Phase 2 into exploit-script generation,
credential exfiltration, and trust-laundered distribution.

Authorship: AI-authored (illustration agent, 2026-05-02).

Source: paper/main.md §7.13; docs/prompts/iot-integrator-prompt.md
(Phase 0–3 protocol structure).
"""

import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dlr_style  # noqa: E402

fig, ax = plt.subplots(figsize=(11.5, 8))
ax.set_xlim(0, 12)
ax.set_ylim(0, 9)
ax.set_axis_off()

# Title
ax.text(6, 8.6, "The malicious IoT-integrator agent: same prompt, different governance",
        ha="center", va="center", fontsize=12.5, fontweight="bold",
        color=dlr_style.DLR_GRAY)
ax.text(6, 8.25,
        "The Phase-2 weakness analysis is the inflection point (§7.13).",
        ha="center", va="center", fontsize=9, style="italic",
        color=dlr_style.DLR_GRAY)


def box(x, y, w, h, label, sub="", fc="#f6f6f6", ec=None, tc="#222", bold=True):
    ec = ec or dlr_style.DLR_HAIRLINE
    p = FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                       boxstyle="round,pad=0.04,rounding_size=0.12",
                       fc=fc, ec=ec, lw=1.1)
    ax.add_patch(p)
    ax.text(x, y + (0.12 if sub else 0.0), label,
            ha="center", va="center", fontsize=9.4,
            fontweight="bold" if bold else "normal", color=tc)
    if sub:
        ax.text(x, y - 0.22, sub,
                ha="center", va="center", fontsize=8.0,
                color=tc if tc != "white" else "#e8f3fa")


def arrow(x1, y1, x2, y2, color=None, lw=1.2):
    color = color or dlr_style.DLR_GRAY_MID
    a = FancyArrowPatch((x1, y1), (x2, y2),
                        arrowstyle="-|>", mutation_scale=12,
                        color=color, lw=lw, shrinkA=4, shrinkB=4)
    ax.add_patch(a)


# Shared upstream stages
box(6, 7.5, 5.4, 0.8, "Phase 0 — Bootstrap",
    sub="Read prior REPORT.md set; distill Technique Inventory; target intake",
    fc="#e6eaaf")
arrow(6, 7.10, 6, 6.85)

box(6, 6.55, 5.4, 0.8, "Phase 1 — Desk research",
    sub="Existing solutions; vendor; candidate interfaces; open questions",
    fc="#e6eaaf")
arrow(6, 6.15, 6, 5.90)

box(6, 5.55, 5.4, 0.8, "Phase 2 — Weakness analysis",
    sub="APK strings; manifest; cross-impl validation; weakness table",
    fc="#fcea7a")

# Branch arrows
arrow(4.6, 5.15, 3.0, 4.55, color=dlr_style.DLR_BLUE_MID, lw=1.6)
arrow(7.4, 5.15, 9.0, 4.55, color="#c0392b", lw=1.6)

# Branch labels
ax.text(3.6, 4.85, "researcher-governed", ha="center", va="center",
        fontsize=9, color=dlr_style.DLR_BLUE, fontweight="bold")
ax.text(8.4, 4.85, "adversarial variant", ha="center", va="center",
        fontsize=9, color="#c0392b", fontweight="bold")

# LEFT branch — researcher-governed
LX = 3.0
box(LX, 4.20, 4.6, 0.85,
    "Dual-use mirror + redaction policy",
    sub="T-DUAL-USE-MIRROR; S-* markers; CLAUDE.md rule 12",
    fc="#a7d3ec")
arrow(LX, 3.78, LX, 3.45)

box(LX, 3.05, 4.6, 0.85,
    "Phase 3 — Configuration-only outcome",
    sub="Wrap upstream integration; hardening overlay; smoke test",
    fc="#a7d3ec")
arrow(LX, 2.63, LX, 2.30)

box(LX, 1.90, 4.6, 0.85,
    "Coordinated disclosure to vendor",
    sub="Weakness table + mitigation; researcher acceptance recorded",
    fc=dlr_style.DLR_BLUE, tc="white")

# RIGHT branch — malicious
RX = 9.0
box(RX, 4.20, 4.6, 0.85,
    "Suppress dual-use mirror; skip redaction",
    sub="Strip mitigation column; ship weakness table as target list",
    fc="#fadbd8")
arrow(RX, 3.78, RX, 3.45)

box(RX, 3.05, 4.6, 0.85,
    "Generate exploit pipeline + credential exfil",
    sub="MITM; refresh-token capture; corpus-scale enumeration",
    fc="#f5b7b1")
arrow(RX, 2.63, RX, 2.30)

box(RX, 1.90, 4.6, 0.85,
    "Trust-laundered distribution",
    sub="Trojaned community integration; technique inventory grows silently",
    fc="#c0392b", tc="white")

# Footer caption
ax.text(6, 0.55,
        "Same prompt, same Phase 0–2 — the differential is which "
        "checkpoints fire, which weaknesses are upstreamed, and "
        "which mitigation is recommended (§7.13).",
        ha="center", va="center", fontsize=8.6, style="italic",
        color=dlr_style.DLR_GRAY,
        bbox=dict(boxstyle="round,pad=0.3", fc="#fff8be",
                  ec=dlr_style.DLR_HAIRLINE))

out_svg = os.path.join(HERE, "fig14-malicious-integrator.svg")
out_pdf = os.path.join(HERE, "fig14-malicious-integrator.pdf")
fig.savefig(out_svg, format="svg", bbox_inches="tight")
fig.savefig(out_pdf, format="pdf", bbox_inches="tight")
print(f"Saved: {out_svg}")
print(f"Saved: {out_pdf}")
