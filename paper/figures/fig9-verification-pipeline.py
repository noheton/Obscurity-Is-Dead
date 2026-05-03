#!/usr/bin/env python3
"""
Figure 9 — Verification-status pipeline (ILL-03).

Diagram of the verification-status pipeline used in `docs/sources.md`:
    [needs-research] -> [lit-retrieved] -> [ai-confirmed] -> [lit-read]
plus the parallel artifact-status track
    [unverified-external] -> [repo-referenced] -> [repo-vendored]
with an annotation of what claims each status permits. Concretely
illustrates the sloppification mitigation described in §7.6.

Authorship: AI-authored (illustration agent, 2026-05-02; reworked
2026-05-03 in figure-overhaul pass to: (i) replace the red/yellow/
green stage palette — which fails deuteranopia and tritanopia
simulation — with a sequential blue ramp from `dlr_style` (light
blue -> mid blue -> dark blue) that monotonically encodes
verification depth and survives greyscale; (ii) add the
`[ai-confirmed]` stage promoted to the verification ladder
2026-05-02 per `CLAUDE.md` §"Verification status ladder
(extended 2026-05-02)"; (iii) raise stage-cell font sizes from
8.5 / 8.0 to 9.5 / 9.0 and stage-label tag from 10.0 to 11.0 for
print legibility; (iv) replace the red sloppification-gate
annotation colour with the dark-blue accent + bold so the gate
remains semantically marked without relying on red).

Source: `docs/sources.md` (verification-status legend including the
2026-05-02 ladder extension), `docs/methodology.md`, §7.6.

Outputs:
    paper/figures/fig9-verification-pipeline.svg
    paper/figures/fig9-verification-pipeline.pdf
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

fig, ax = plt.subplots(figsize=(13.0, 6.2))
ax.set_xlim(0, 13)
ax.set_ylim(0, 6.2)
ax.set_axis_off()

# Sequential blue ramp (monotone with verification depth).
# Source: dlr_style brighter -> bright -> mid -> darker.
RAMP = ["#d1e8fa", "#a7d3ec", "#6cb9dc", "#3b98cb", "#00658b"]


def stage(x, y, w, h, tag, label, allowed, color, text_light=False):
    p = FancyBboxPatch((x, y), w, h,
                       boxstyle="round,pad=0.05,rounding_size=0.04",
                       fc=color, ec=dlr_style.DLR_GRAY, lw=1.2)
    ax.add_patch(p)
    tag_color = "white" if text_light else "#1a1a1a"
    body_color = "#f4f4f4" if text_light else "#222"
    italic_color = "#e8f3fa" if text_light else dlr_style.DLR_GRAY
    ax.text(x + w / 2, y + h - 0.34, tag, ha="center", va="center",
            fontsize=11.0, fontweight="bold", color=tag_color,
            family="monospace")
    ax.text(x + w / 2, y + h - 0.78, label, ha="center", va="center",
            fontsize=9.5, color=body_color)
    ax.text(x + w / 2, y + 0.36, allowed, ha="center", va="center",
            fontsize=9.0, color=italic_color, style="italic", wrap=True)
    return (x + w, y + h / 2), (x, y + h / 2)


def chevron(p1, p2, label):
    a = FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=20,
                        lw=2.2, color=dlr_style.DLR_BLUE)
    ax.add_patch(a)
    ax.text((p1[0] + p2[0]) / 2, p1[1] + 0.24, label, ha="center",
            va="bottom", fontsize=9.0, color=dlr_style.DLR_BLUE,
            fontweight="bold")


# ── Literature track (4 stages: needs-research → lit-retrieved →
#                     ai-confirmed → lit-read) ──────────────────────────
ax.text(0.20, 5.85, "Literature track  (docs/sources.md, clusters A-O)",
        fontsize=11.0, fontweight="bold", color=dlr_style.DLR_GRAY)

LIT_W = 2.85
LIT_GAP = 0.20
LIT_X0 = 0.30
LIT_Y = 3.65
LIT_H = 1.55

stages_lit = [
    ("[needs-research]",  "candidate handle exists",
     "no claim may cite this", RAMP[0], False),
    ("[lit-retrieved]",   "metadata + abstract retrieved",
     "may be referenced by handle\nin §1, §7.6 etc., not as evidence", RAMP[1], False),
    ("[ai-confirmed]",    "passage extracted + cross-checked",
     "may be cited inline; load-bearing\nclaims still require [lit-read]", RAMP[2], False),
    ("[lit-read]",        "full text read by researcher",
     "may be cited as evidence\nfor any paper claim", RAMP[4], True),
]

centers_lit = []
for i, (tag, lbl, allowed, col, light) in enumerate(stages_lit):
    x = LIT_X0 + i * (LIT_W + LIT_GAP)
    right, left = stage(x, LIT_Y, LIT_W, LIT_H, tag, lbl, allowed, col, light)
    centers_lit.append((right, left))

for i in range(len(stages_lit) - 1):
    chevron(centers_lit[i][0], centers_lit[i + 1][1], "")

# Stage-promotion labels (above arrows)
labels_lit = ["abstract retrieved", "Source Analyzer\nupgrade", "full text read"]
for i, lbl in enumerate(labels_lit):
    x_left = centers_lit[i][0][0]
    x_right = centers_lit[i + 1][1][0]
    ax.text((x_left + x_right) / 2, LIT_Y + LIT_H + 0.18, lbl,
            ha="center", va="bottom", fontsize=8.5,
            color=dlr_style.DLR_BLUE, fontweight="bold")

# ── Artifact track ────────────────────────────────────────────────────────
ax.text(0.20, 2.95, "Artifact track  (docs/sources.md, S-XX entries)",
        fontsize=11.0, fontweight="bold", color=dlr_style.DLR_GRAY)

# Three stages laid out across the same width as the literature track.
ART_W = 3.95
ART_GAP = 0.30
ART_X0 = 0.30
ART_Y = 0.85
ART_H = 1.55

stages_art = [
    ("[unverified-external]", "URL only; not vendored",
     "may inform background;\ncannot ground a finding", RAMP[0], False),
    ("[repo-referenced]",     "checksum / commit pin",
     "claims may cite the pinned\nexternal artifact", RAMP[2], False),
    ("[repo-vendored]",       "copy committed under original/",
     "claims may cite line numbers;\nfully reproducible", RAMP[4], True),
]

centers_art = []
for i, (tag, lbl, allowed, col, light) in enumerate(stages_art):
    x = ART_X0 + i * (ART_W + ART_GAP)
    right, left = stage(x, ART_Y, ART_W, ART_H, tag, lbl, allowed, col, light)
    centers_art.append((right, left))

labels_art = ["pin commit / SHA", "vendor in original/"]
for i, lbl in enumerate(labels_art):
    chevron(centers_art[i][0], centers_art[i + 1][1], "")
    x_left = centers_art[i][0][0]
    x_right = centers_art[i + 1][1][0]
    ax.text((x_left + x_right) / 2, ART_Y + ART_H + 0.18, lbl,
            ha="center", va="bottom", fontsize=8.5,
            color=dlr_style.DLR_BLUE, fontweight="bold")

# Sloppification gate annotation — re-coloured to dark blue (CB-safe).
ax.annotate(
    "Sloppification gate (§7.6):\nupgrade requires evidence,\nnot inference. No gate-jumping.",
    xy=(centers_lit[3][1][0], LIT_Y + LIT_H), xycoords="data",
    xytext=(11.0, 5.95), textcoords="data",
    fontsize=9.0, color=dlr_style.DLR_BLUE, fontweight="bold",
    ha="center",
    arrowprops=dict(arrowstyle="->", color=dlr_style.DLR_BLUE, lw=1.4),
)

ax.text(6.5, 0.18,
        "Each stage gates the kind of claim the paper may make. The legend itself "
        "is the sloppification mitigation: it makes the read-state of every cited "
        "source explicit (CLAUDE.md rules 1, 8).",
        ha="center", va="center", fontsize=9.0, style="italic",
        color=dlr_style.DLR_GRAY)

fig.patch.set_facecolor("white")
out_svg = os.path.join(HERE, "fig9-verification-pipeline.svg")
out_pdf = os.path.join(HERE, "fig9-verification-pipeline.pdf")
fig.savefig(out_svg, format="svg", bbox_inches="tight", facecolor="white")
fig.savefig(out_pdf, format="pdf", bbox_inches="tight", facecolor="white")
print(f"Saved: {out_svg}")
print(f"Saved: {out_pdf}")
