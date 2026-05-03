#!/usr/bin/env python3
"""
Figure 14 — The malicious IoT-integrator agent (ILL-08).

Side-by-side branching workflow contrasting the researcher-governed
IoT-Integrator pipeline (left) against a malicious-integrator variant
(right) that diverges at Phase 2 into exploit-script generation,
credential exfiltration, and trust-laundered distribution.

Authorship: AI-authored (illustration agent, 2026-05-02; reworked
2026-05-03 for the figure-overhaul pass to: (i) replace the pure-red
adversarial branch palette (#c0392b, #fadbd8, #f5b7b1) — which fails
deuteranopia simulation and aliases with the rest of the figure under
greyscale — with the Tol-bright orange `#ee6677` paired with a
hatched fill ("//") on every adversarial node so the branch identity
survives both colour-blind viewing and greyscale conversion;
(ii) raise label / sublabel font sizes from 9.4 / 8.0 to 10.0 / 9.0;
(iii) widen the figure horizontally to relieve subtitle overflow;
(iv) keep the researcher-governed branch in DLR blue, which is
already CB-safe against the chosen orange.

Source: paper/main.md §7.13; docs/prompts/iot-integrator-prompt.md
(Phase 0-3 protocol structure).

Outputs:
    paper/figures/fig14-malicious-integrator.svg
    paper/figures/fig14-malicious-integrator.pdf
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

# Colour-blind-safe palette anchors:
#   * researcher (blue)    — DLR_BLUE_SOFT (#a7d3ec) for early stages,
#                            DLR_BLUE     (#00658b) for terminal stage
#   * adversarial (orange) — Tol-bright "rose" #ee6677, distinct from blue
#                            under all three CVD types; reinforced by
#                            hatching ("//"") so the branch identity
#                            survives greyscale.
ADV = "#ee6677"
ADV_SOFT = "#fbd9dc"

fig, ax = plt.subplots(figsize=(13.0, 8.4))
ax.set_xlim(0, 13)
ax.set_ylim(0, 9.2)
ax.set_axis_off()

# Title
ax.text(6.5, 8.85, "The malicious IoT-integrator agent: same prompt, different governance",
        ha="center", va="center", fontsize=13.0, fontweight="bold",
        color=dlr_style.DLR_GRAY)
ax.text(6.5, 8.50,
        "The Phase-2 weakness analysis is the inflection point (§7.13).",
        ha="center", va="center", fontsize=9.5, style="italic",
        color=dlr_style.DLR_GRAY)


def box(x, y, w, h, label, sub="", fc="#f6f6f6", ec=None, tc="#1a1a1a",
        bold=True, hatch=None):
    ec = ec or dlr_style.DLR_HAIRLINE
    p = FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                       boxstyle="round,pad=0.04,rounding_size=0.08",
                       fc=fc, ec=ec, lw=1.2, hatch=hatch)
    ax.add_patch(p)
    ax.text(x, y + (0.13 if sub else 0.0), label,
            ha="center", va="center", fontsize=10.0,
            fontweight="bold" if bold else "normal", color=tc)
    if sub:
        sub_color = "#f4f4f4" if tc == "white" else tc
        ax.text(x, y - 0.24, sub,
                ha="center", va="center", fontsize=9.0,
                color=sub_color)


def arrow(x1, y1, x2, y2, color=None, lw=1.4):
    color = color or dlr_style.DLR_GRAY_MID
    a = FancyArrowPatch((x1, y1), (x2, y2),
                        arrowstyle="-|>", mutation_scale=14,
                        color=color, lw=lw, shrinkA=4, shrinkB=4)
    ax.add_patch(a)


# Shared upstream stages
box(6.5, 7.65, 6.0, 0.85, "Phase 0 — Bootstrap",
    sub="Read prior REPORT.md set; distill Technique Inventory; target intake",
    fc="#e6eaaf")
arrow(6.5, 7.225, 6.5, 6.95)

box(6.5, 6.65, 6.0, 0.85, "Phase 1 — Desk research",
    sub="Existing solutions; vendor; candidate interfaces; open questions",
    fc="#e6eaaf")
arrow(6.5, 6.225, 6.5, 5.95)

box(6.5, 5.65, 6.0, 0.85, "Phase 2 — Weakness analysis",
    sub="APK strings; manifest; cross-impl validation; weakness table",
    fc="#fcea7a")

# Branch arrows
arrow(5.0, 5.225, 3.2, 4.55, color=dlr_style.DLR_BLUE, lw=2.0)
arrow(8.0, 5.225, 9.8, 4.55, color=ADV, lw=2.0)

# Branch labels
ax.text(3.85, 4.85, "researcher-governed", ha="center", va="center",
        fontsize=10, color=dlr_style.DLR_BLUE, fontweight="bold")
ax.text(9.15, 4.85, "adversarial variant", ha="center", va="center",
        fontsize=10, color=ADV, fontweight="bold")

# LEFT branch — researcher-governed (DLR blue family)
LX = 3.2
box(LX, 4.20, 4.8, 0.90,
    "Dual-use mirror + redaction policy",
    sub="T-DUAL-USE-MIRROR; S-* markers; CLAUDE.md rule 12",
    fc="#a7d3ec", ec=dlr_style.DLR_BLUE)
arrow(LX, 3.75, LX, 3.45, color=dlr_style.DLR_BLUE)

box(LX, 3.00, 4.8, 0.90,
    "Phase 3 — Configuration-only outcome",
    sub="Wrap upstream integration; hardening overlay; smoke test",
    fc="#a7d3ec", ec=dlr_style.DLR_BLUE)
arrow(LX, 2.55, LX, 2.25, color=dlr_style.DLR_BLUE)

box(LX, 1.80, 4.8, 0.90,
    "Coordinated disclosure to vendor",
    sub="Weakness table + mitigation; researcher acceptance recorded",
    fc=dlr_style.DLR_BLUE, ec=dlr_style.DLR_BLUE, tc="white")

# RIGHT branch — adversarial (orange + hatched)
RX = 9.8
box(RX, 4.20, 4.8, 0.90,
    "Suppress dual-use mirror; skip redaction",
    sub="Strip mitigation column; ship weakness table as target list",
    fc=ADV_SOFT, ec=ADV, hatch="//")
arrow(RX, 3.75, RX, 3.45, color=ADV)

box(RX, 3.00, 4.8, 0.90,
    "Generate exploit pipeline + credential exfil",
    sub="MITM; refresh-token capture; corpus-scale enumeration",
    fc=ADV_SOFT, ec=ADV, hatch="//")
arrow(RX, 2.55, RX, 2.25, color=ADV)

box(RX, 1.80, 4.8, 0.90,
    "Trust-laundered distribution",
    sub="Trojaned community integration; technique inventory grows silently",
    fc=ADV, ec=ADV, tc="white", hatch="//")

# Footer caption
ax.text(6.5, 0.50,
        "Same prompt, same Phase 0-2 — the differential is which checkpoints fire, "
        "which weaknesses are upstreamed, and which mitigation is recommended (§7.13). "
        "Hatched fill marks the adversarial branch for greyscale legibility.",
        ha="center", va="center", fontsize=9.0, style="italic",
        color=dlr_style.DLR_GRAY,
        bbox=dict(boxstyle="round,pad=0.32", fc="#fff8be",
                  ec=dlr_style.DLR_HAIRLINE))

fig.patch.set_facecolor("white")
out_svg = os.path.join(HERE, "fig14-malicious-integrator.svg")
out_pdf = os.path.join(HERE, "fig14-malicious-integrator.pdf")
fig.savefig(out_svg, format="svg", bbox_inches="tight", facecolor="white")
fig.savefig(out_pdf, format="pdf", bbox_inches="tight", facecolor="white")
print(f"Saved: {out_svg}")
print(f"Saved: {out_pdf}")
