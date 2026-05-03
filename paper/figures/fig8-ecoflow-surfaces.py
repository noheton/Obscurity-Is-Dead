#!/usr/bin/env python3
"""
Figure 8 — EcoFlow PowerOcean three-API-surface architecture (ILL-02).

Diagram of the three EcoFlow API surfaces — legacy `setDeviceProperty` REST,
published Open API (HMAC-SHA256), and MQTT — labelled with which surface the
consumer app uses, which surface the Open API documentation covers, and which
surface the integration `powerocean_dev` selects. Makes the three-surface
reconciliation finding in §4.3 self-contained.

Authorship: AI-authored (illustration agent, prompt
`docs/prompts/illustration-prompt.md`, session
claude/run-illustration-agent-IRJKO, 2026-05-02; reworked 2026-05-03 in
the design-consistency materialisation pass to: (i) replace the pure-red
"legacy / undocumented" semantic palette (#ffe6e6 / #c0392b) — which
fails deuteranopia simulation and aliases with the rest of the figure
under greyscale — with the Tol-bright rose `#ee6677` paired with a
hatched fill ("//"") on the legacy node so the warning identity
survives both colour-blind viewing and greyscale conversion (matches
the pattern adopted in fig14); (ii) raise body / sub-label font sizes
from 9.5 / 8.0 to 10.0 / 9.0 pt to clear the print-legibility floor;
(iii) raise sub-caption from 8.5 to 9.0 pt; (iv) keep the documented
Open-API surface in DLR blue and the MQTT surface in DLR neutral grey,
both of which are CB-safe against the chosen rose.

Outputs:
    paper/figures/fig8-ecoflow-surfaces.svg
    paper/figures/fig8-ecoflow-surfaces.pdf

Source: `experiments/ecoflow-powerocean/original/doc/apk.md` (esp. line 52),
`apk-logs.md`, `implementation.md`. Structural diagram only — no numerical
data.
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

# Colour-blind-safe semantic anchors (matches fig11 / fig14):
#   * legacy / "do-not-use"  — Tol-bright rose `#ee6677`, hatched ("//") fill
#   * documented / governed  — DLR_BLUE family (CB-safe against rose)
#   * neutral / cloud        — DLR_GRAY family
WARN      = "#ee6677"
WARN_SOFT = "#fbd9dc"

fig, ax = plt.subplots(figsize=(11, 6.4))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6.6)
ax.set_axis_off()

# ── Actors (left + right columns) ─────────────────────────────────────────
def box(x, y, w, h, label, sub=None, fc="#ffffff", ec=dlr_style.DLR_GRAY,
        lw=1.4, fontsize=10.0, weight="normal", hatch=None):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.04,rounding_size=0.12",
                       fc=fc, ec=ec, lw=lw, hatch=hatch)
    ax.add_patch(p)
    ax.text(x + w / 2, y + h / 2 + (0.20 if sub else 0),
            label, ha="center", va="center",
            fontsize=fontsize, fontweight=weight, color="#1a1a1a")
    if sub:
        ax.text(x + w / 2, y + h / 2 - 0.26, sub, ha="center", va="center",
                fontsize=9.0, color=dlr_style.DLR_GRAY)
    return (x + w / 2, y + h / 2)

# Consumers (left)
app_c    = box(0.3, 5.0, 2.2, 1.0, "Vendor Android app",
               sub="(EcoFlow consumer)",
               fc=dlr_style.DLR_BLUE_SOFT, weight="bold")
opendoc_c= box(0.3, 3.05, 2.2, 1.0, "Open API docs",
               sub="(developer.ecoflow.com)",
               fc=dlr_style.DLR_GRAY_SOFT)
ha_c     = box(0.3, 1.1, 2.2, 1.0, "powerocean_dev\n(HA integration)",
               sub="this paper, §4",
               fc="#fff8be", weight="bold")

# Three API surfaces (middle column)
s_legacy = box(4.0, 4.7, 3.0, 1.3,
               "Legacy REST: setDeviceProperty",
               sub="POST /iot-devices/device/setDeviceProperty\n"
                   "session-token auth · camelCase params",
               fc=WARN_SOFT, ec=WARN, lw=1.6, hatch="//")
s_open   = box(4.0, 2.7, 3.0, 1.3,
               "Open API (published)",
               sub="HMAC-SHA256 signed · documented\nrate-limited",
               fc="#e8f4fb", ec=dlr_style.DLR_BLUE, lw=1.6)
s_mqtt   = box(4.0, 0.7, 3.0, 1.3,
               "MQTT broker",
               sub="vendor cloud · TLS\ntelemetry + commands",
               fc=dlr_style.DLR_GRAY_SOFT, ec=dlr_style.DLR_GRAY, lw=1.6)

# Device (right)
dev = box(8.4, 2.7, 1.4, 1.3, "PowerOcean\ndevice",
          sub="(home gateway)",
          fc=dlr_style.DLR_BLUE_SOFT, weight="bold")

def arrow(p1, p2, label=None, color="#444", style="-|>", lw=1.5,
          rad=0.0, label_offset=(0, 0.18), label_color="#1a1a1a",
          label_size=9.0):
    a = FancyArrowPatch(p1, p2, arrowstyle=style, mutation_scale=14,
                        lw=lw, color=color,
                        connectionstyle=f"arc3,rad={rad}")
    ax.add_patch(a)
    if label:
        mx = (p1[0] + p2[0]) / 2 + label_offset[0]
        my = (p1[1] + p2[1]) / 2 + label_offset[1]
        ax.text(mx, my, label, ha="center", va="center",
                fontsize=label_size, color=label_color, fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.20", fc="white",
                          ec="none", alpha=0.9))

# Consumer → surface arrows (which surface each consumer uses)
arrow(app_c,    s_legacy[0:2], label="USES (undocumented)",
      color=WARN, lw=2.0, label_color=WARN)
arrow(opendoc_c, s_open[0:2],  label="DOCUMENTS",
      color=dlr_style.DLR_BLUE, lw=2.0, label_color=dlr_style.DLR_BLUE)
arrow(ha_c,      s_legacy[0:2], label="SELECTS\n(apk.md line 52)",
      color=dlr_style.DLR_YELLOW, lw=2.0, rad=-0.25,
      label_color="#7a5b08",
      label_offset=(0, -0.05))

# Surface → device
for s in (s_legacy, s_open, s_mqtt):
    arrow(s[0:2], dev[0:2], color=dlr_style.DLR_GRAY, lw=1.1,
          style="-|>")

# Title and legend caption
ax.text(5.0, 6.30, "EcoFlow PowerOcean — three API surfaces and how they are reached",
        ha="center", va="center", fontsize=12.0,
        fontweight="bold", color=dlr_style.DLR_GRAY)
ax.text(5.0, 0.20,
        "Reconciliation finding (§4.3): the consumer app and the integration "
        "both target the legacy endpoint;\nthe Open API documents a different "
        "surface; MQTT is the cloud-bound telemetry surface. "
        "Hatched rose = legacy / undocumented (CB-safe).",
        ha="center", va="center", fontsize=9.0, color=dlr_style.DLR_GRAY,
        style="italic")

out_svg = os.path.join(HERE, "fig8-ecoflow-surfaces.svg")
out_pdf = os.path.join(HERE, "fig8-ecoflow-surfaces.pdf")
fig.savefig(out_svg, format="svg", bbox_inches="tight", facecolor="white")
fig.savefig(out_pdf, format="pdf", bbox_inches="tight", facecolor="white")
print(f"Saved: {out_svg}")
print(f"Saved: {out_pdf}")
