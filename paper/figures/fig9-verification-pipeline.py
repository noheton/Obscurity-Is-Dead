#!/usr/bin/env python3
"""
Figure 9 — Verification-status pipeline (ILL-03).

Diagram of the verification-status pipeline used in `docs/sources.md`:
    [needs-research] → [lit-retrieved] → [lit-read]
plus the parallel artifact-status track
    [unverified-external] → [repo-referenced] → [repo-vendored]
with an annotation of what claims each status permits. Concretely
illustrates the sloppification mitigation described in §7.6.

Authorship: AI-authored (illustration agent, 2026-05-02).

Source: `docs/sources.md` (verification-status legend),
`docs/methodology.md` (rule statements), §7.6 of the paper.
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

fig, ax = plt.subplots(figsize=(12, 5.5))
ax.set_xlim(0, 12)
ax.set_ylim(0, 5.5)
ax.set_axis_off()

def stage(x, y, w, h, tag, label, allowed, color):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05,rounding_size=0.12",
                       fc=color, ec=dlr_style.DLR_GRAY, lw=1.4)
    ax.add_patch(p)
    ax.text(x + w / 2, y + h - 0.32, tag, ha="center", va="center",
            fontsize=10, fontweight="bold", color="#222",
            family="monospace")
    ax.text(x + w / 2, y + h - 0.7, label, ha="center", va="center",
            fontsize=8.5, color="#333")
    ax.text(x + w / 2, y + 0.32, allowed, ha="center", va="center",
            fontsize=8, color=dlr_style.DLR_GRAY, style="italic", wrap=True)
    return (x + w, y + h / 2), (x, y + h / 2)

def chevron(p1, p2, label):
    a = FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=18,
                        lw=2.0, color=dlr_style.DLR_BLUE)
    ax.add_patch(a)
    ax.text((p1[0] + p2[0]) / 2, p1[1] + 0.22, label, ha="center",
            va="bottom", fontsize=8.5, color=dlr_style.DLR_BLUE,
            fontweight="bold")

# ── Literature track ─────────────────────────────────────────────────────
ax.text(0.2, 5.05, "Literature track  (docs/sources.md, clusters A–K)",
        fontsize=10.5, fontweight="bold", color=dlr_style.DLR_GRAY)
r1, _ = stage(0.4, 3.3, 3.4, 1.5, "[needs-research]",
              "candidate handle exists",
              "no claim may cite this",
              "#fdecea")
_, l2 = stage(4.2, 3.3, 3.4, 1.5, "[lit-retrieved]",
              "metadata + abstract retrieved",
              "may be referenced by handle\nin §1, §7.6 etc., not as evidence",
              "#fff8be")
_, l3 = stage(8.0, 3.3, 3.4, 1.5, "[lit-read]",
              "full text read by researcher",
              "may be cited as evidence\nfor a paper claim",
              "#e6eaaf")
chevron(r1, l2, "abstract retrieved")
chevron((7.6, 4.05), l3, "full text read")

# ── Artifact track ───────────────────────────────────────────────────────
ax.text(0.2, 2.55, "Artifact track  (docs/sources.md, S-XX entries)",
        fontsize=10.5, fontweight="bold", color=dlr_style.DLR_GRAY)
a1, _ = stage(0.4, 0.8, 3.4, 1.5, "[unverified-external]",
              "URL only; not vendored",
              "may inform background;\ncannot ground a finding",
              "#fdecea")
_, b2 = stage(4.2, 0.8, 3.4, 1.5, "[repo-referenced]",
              "checksum / commit pin",
              "claims may cite the pinned\nexternal artifact",
              "#fff8be")
_, b3 = stage(8.0, 0.8, 3.4, 1.5, "[repo-vendored]",
              "copy committed under original/",
              "claims may cite line numbers;\nfully reproducible",
              "#e6eaaf")
chevron(a1, b2, "pin commit/SHA")
chevron((7.6, 1.55), b3, "vendor in original/")

# Sloppification gate
ax.annotate(
    "Sloppification gate (§7.6):\nupgrade requires the researcher\nto have read / vendored.\nNo gate-jumping.",
    xy=(7.85, 4.05), xycoords="data",
    xytext=(11.0, 5.2), textcoords="data",
    fontsize=8.5, color="#c0392b", fontweight="bold",
    ha="center",
    arrowprops=dict(arrowstyle="->", color="#c0392b", lw=1.3),
)

ax.text(6.0, -0.15,
        "Each stage gates the kind of claim the paper may make. "
        "The legend itself is the sloppification mitigation: it makes the "
        "read-state of every cited source explicit (CLAUDE.md rules 1, 8).",
        ha="center", va="center", fontsize=8.5, style="italic",
        color=dlr_style.DLR_GRAY)

out_svg = os.path.join(HERE, "fig9-verification-pipeline.svg")
out_pdf = os.path.join(HERE, "fig9-verification-pipeline.pdf")
fig.savefig(out_svg, format="svg", bbox_inches="tight")
fig.savefig(out_pdf, format="pdf", bbox_inches="tight")
print(f"Saved: {out_svg}")
print(f"Saved: {out_pdf}")
