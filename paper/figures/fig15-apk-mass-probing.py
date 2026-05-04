#!/usr/bin/env python3
"""
Figure 15 — Automated mass probing of public APK repositories (ILL-09).

Pipeline diagram from public APK repository through
fetch -> unpack -> strings/manifest -> DEX-grep -> per-vendor weakness
output, annotated with the per-stage cost (seconds vs. years) so the
asymmetric-collapse claim of §7.3 is visible at corpus scale.

Authorship: AI-authored (illustration agent, 2026-05-02; CB-palette
recolour 2026-05-03 — pipeline-fix pass).

Source: paper/main.md §7.14; literature base rates from L-BLE-4
(Sivakumaran et al. 2023) and L-PRIV-5 (Nan et al. 2023) cited in §7.14.

2026-05-03 recolour: replaced the three green `#cad55c` middle-stage
fills with a sequential blue ramp from `dlr_style` so the pipeline
reads as a CB-safe progression (input → process → output) under
deuteranopia and in greyscale. The yellow `#fff8be` empirical-rates
panel is replaced with a neutral DLR_GRAY_SOFT background so the
single accent (DLR blue) remains the only saturated colour.

2026-05-03 design-consistency materialisation pass: raised every
sub-floor font size to clear the 9 pt body floor that fig11 (hero /
design anchor) establishes for the figure set: stage sub-label 8.2 →
9.0 pt; cost-tier brackets 8 / 8.6 → 9.0 pt; empirical-rates panel
body 8.4 → 9.0 pt; panel italic 8.4 → 9.0 pt; footer 8.6 → 9.0 pt.
Stage label kept at 9.4 (already above floor). Palette unchanged.
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

fig, ax = plt.subplots(figsize=(12, 6.5))
ax.set_xlim(0, 13)
ax.set_ylim(0, 7.5)
ax.set_axis_off()

# Title
ax.text(6.5, 7.05,
        "Automated mass probing of public APK repositories",
        ha="center", va="center", fontsize=12.5, fontweight="bold",
        color=dlr_style.DLR_GRAY)
ax.text(6.5, 6.70,
        "Per-APK cost compresses from team-years (human-led) to seconds (AI-assisted) — §7.14.",
        ha="center", va="center", fontsize=9, style="italic",
        color=dlr_style.DLR_GRAY)


_DARK_FILLS = {"#3b98cb", "#00658b", dlr_style.DLR_BLUE}


def stage(x, y, w, h, label, sub, fc):
    p = FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                       boxstyle="round,pad=0.04,rounding_size=0.10",
                       fc=fc, ec=dlr_style.DLR_HAIRLINE, lw=1.0)
    ax.add_patch(p)
    on_dark = fc in _DARK_FILLS
    label_col = "white" if on_dark else "#222"
    sub_col   = "#f4f4f4" if on_dark else "#333"
    # Header font 9.0 pt (was 9.4 pt prior to 2026-05-04 LAY-32 hand-back).
    # The 0.4 pt drop closes the dark-fill stage-box header/body collision
    # without breaking the 9 pt body floor that fig11 (hero) establishes
    # for the figure set. Two-line header for the DEX-grep stage now fits
    # entirely within the box width.
    ax.text(x, y + 0.18, label,
            ha="center", va="center", fontsize=9.0, fontweight="bold",
            color=label_col)
    ax.text(x, y - 0.22, sub,
            ha="center", va="center", fontsize=9.0, color=sub_col)


def arrow(x1, y, x2):
    a = FancyArrowPatch((x1, y), (x2, y),
                        arrowstyle="-|>", mutation_scale=12,
                        color=dlr_style.DLR_GRAY_MID, lw=1.4)
    ax.add_patch(a)


# Pipeline row (y = 4.5)
y_pipe = 4.5
stages = [
    # CB-safe sequential blue ramp: light → mid → dark, replacing the
    # earlier green `#cad55c` middle stages so colour now monotonically
    # encodes pipeline depth (also survives greyscale).
    (1.4, "Public APK\nrepository", "APKPure / APKMirror\nMillions of APKs", "#d1e8fa"),
    (4.0, "Fetch + unpack", "unzip; manifest;\nDEX extraction", "#a7d3ec"),
    (6.6, "Static probe", "strings + grep;\npermission audit", "#6cb9dc"),
    # Header collapsed from 3 lines → 2 lines to clear the LAY-32
    # collision (2026-05-04): the previous "DEX-grep +\nidentity-provider
    # \ndiscovery" header descender overlapped the 2-line body label
    # "T-REST-WRITE-PROBE;\ntoken-endpoint enum" inside the dark-fill box.
    # Two-line header now matches the line count of every other stage;
    # the line break is placed inside "identity-provider" so neither
    # line exceeds the 2.2-unit box width at 9 pt.
    (9.2, "DEX-grep + identity-\nprovider discovery", "T-REST-WRITE-PROBE;\ntoken-endpoint enum", "#3b98cb"),
    (11.8, "Per-vendor weakness\ninventory + flow graph", "Identity providers;\ncross-vendor edges", dlr_style.DLR_BLUE),
]
for x, label, sub, fc in stages:
    stage(x, y_pipe, 2.2, 1.3, label, sub, fc)
for i in range(len(stages) - 1):
    x1 = stages[i][0] + 1.1
    x2 = stages[i + 1][0] - 1.1
    arrow(x1, y_pipe, x2)

# Per-stage cost annotations
ax.text(1.4, 3.55, "input tier",
        ha="center", va="center", fontsize=9.0, style="italic",
        color=dlr_style.DLR_GRAY)
ax.text(4.0, 3.55, "~1 s / APK",
        ha="center", va="center", fontsize=9.0, fontweight="bold",
        color=dlr_style.DLR_BLUE)
ax.text(6.6, 3.55, "~10 s / APK",
        ha="center", va="center", fontsize=9.0, fontweight="bold",
        color=dlr_style.DLR_BLUE)
ax.text(9.2, 3.55, "~1 min / APK\n(LLM inference)",
        ha="center", va="center", fontsize=9.0, fontweight="bold",
        color=dlr_style.DLR_BLUE)
ax.text(11.8, 3.55, "corpus output",
        ha="center", va="center", fontsize=9.0, style="italic",
        color=dlr_style.DLR_GRAY)

# Cost-comparison panel — human vs AI
panel_y = 1.85
ax.add_patch(FancyBboxPatch((0.6, panel_y - 0.95), 12.0, 1.55,
                            boxstyle="round,pad=0.04,rounding_size=0.10",
                            fc=dlr_style.DLR_GRAY_SOFT,
                            ec=dlr_style.DLR_HAIRLINE, lw=1.0))
ax.text(6.5, panel_y + 0.40,
        "Empirical base rates from human-led corpus studies",
        ha="center", va="center", fontsize=9.5, fontweight="bold",
        color=dlr_style.DLR_GRAY)
ax.text(3.4, panel_y - 0.10,
        ">70% of 17,243 BLE Android APKs vulnerable\n[L-BLE-4, Sivakumaran et al. 2023]",
        ha="center", va="center", fontsize=9.0, color="#222")
ax.text(9.6, panel_y - 0.10,
        "1,973 / 6,208 IoT companion apps leak user data\n(1,559 distinct vendors) [L-PRIV-5, Nan et al. 2023]",
        ha="center", va="center", fontsize=9.0, color="#222")
ax.text(6.5, panel_y - 0.65,
        "Both studies were team-years of human-led static analysis. "
        "AI-assisted compression turns the same coverage into days.",
        ha="center", va="center", fontsize=9.0, style="italic",
        color=dlr_style.DLR_GRAY)

# Footer
ax.text(6.5, 0.30,
        "Mitigation leverage points: repository-side abuse-detection; "
        "vendor-side identity-provider hardening; coordinated-disclosure norm at corpus scale (§7.14).",
        ha="center", va="center", fontsize=9.0, style="italic",
        color=dlr_style.DLR_GRAY)

out_svg = os.path.join(HERE, "fig15-apk-mass-probing.svg")
out_pdf = os.path.join(HERE, "fig15-apk-mass-probing.pdf")
fig.savefig(out_svg, format="svg", bbox_inches="tight")
fig.savefig(out_pdf, format="pdf", bbox_inches="tight")
print(f"Saved: {out_svg}")
print(f"Saved: {out_pdf}")
