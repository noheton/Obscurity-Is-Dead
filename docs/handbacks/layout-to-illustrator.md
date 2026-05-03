# Layout Scrutinizer — Hand-back to Illustration Agent (2026-05-03)

Source: `docs/handbacks/layout-defect-registry.md` — PDF SHA-256 `04e818e993e2eea84cf05d5a5bc7045d80270d6a856a398cc04106ca7ac5cf99`, 49 pages, build commit `b5162ee`, build timestamp 2026-05-03T12:54:14Z.

The prior LAY-* illustrator items closed during the 2026-05-03 illustrator pass:

- **LAY-05** (Figure 7 textwidth overflow) — RESOLVED.
- **LAY-06** (figure side) — RESOLVED; `fig12-difficulty-taxonomy.{py,svg,pdf}` regenerated with the Composite column dropped. Writer-side caption mirror flagged separately as **FIG-07**.
- **LAY-13** (PDF version 1.7 inclusion warnings) — **RESOLVED in this build**: zero `pdfTeX warning: PDF inclusion … version <1.7>` in `paper/main.log` (Makefile post-process worked).
- **LAY-12** (intact-jar Gemini deliverable) — PARTIAL, gated on human author supplying the second Gemini PNG.
- **LAY-16** (bibliography rivers) — DEFERRED (advisory; out of illustrator scope).

New illustrator-owned items this pass (per the figure-and-image critique extension):

## FIG-01 — Alt-text macros missing on every `\includegraphics` (joint with writer)

- Source: all 18 `\includegraphics` calls (see writer hand-back for the full line list under FIG-01).
- Illustrator's role: once the writer adds `\Description{...}` macros (or equivalent), confirm the description text correctly matches each asset's visual content. For data-driven figures, the description should name the axes, the chart class (line / bar / heat-map), and the headline finding (≤ 1 sentence each). For structural diagrams, name the entities and the relationship (e.g. "branching workflow with two outcomes").
- Severity: **H** (accessibility)

## FIG-02 — Colour-blind palette migration (DLR style)

- Source: `paper/figures/dlr_style.py`; consumed by `fig1-effort-gap.py`, `fig10-stage-effort.py`, `fig12-difficulty-taxonomy.py`, and the structural-diagram scripts that import it.
- Observed: prior passes flagged the DLR palette as failing deuteranopia simulation; no migration this build. `viewer-blocked` for direct visual confirmation in this pass.
- Required action: where categorical/sequential semantics permit, migrate to ColorBrewer or Viridis. Add explicit greyscale fallback (line dashing, marker shapes) so the figures survive monochrome printing. Document the swap in `paper/figures/README.md`.
- Severity: M

## FIG-03 — fig11-eight-practices in-figure font size at print scale

- Source: `paper/figures/fig11-eight-practices.py`.
- Observed: per illustrator hand-back, cell labels are at fontsize ~8.6. At full `\textwidth` print scale on a letter page that is borderline; once the figure is shrunk for arXiv compilation it may drop below the ~7pt-equivalent legibility threshold. `viewer-blocked` for direct measurement.
- Required action: verify the rendered point size of the cell labels in `paper/main.pdf`; raise to 9 pt if they are below ~7 pt at the rendered width, or split the eight practices into a two-row figure to relax horizontal pressure.
- Severity: M

## FIG-04 — `logo-pandora-jar-intact.png` placeholder still in place

- Source: `paper/figures/logo-pandora-jar-intact.png` (950×944 RGBA, ~83 kB, matplotlib typographic placeholder).
- Observed: included at `width=0.55\linewidth` (`main.tex:2589`); occupies a meaningful share of the §10 anchor page. The matplotlib stand-in noticeably degrades the visual rhetoric next to the Gemini-quality shattered-jar hero.
- Required action: **gated on human author supplying the second Gemini PNG.** When the binary lands, swap in place (preserve the filename), do not regenerate `logo-placeholders.py`, and re-run a narrow-scope Stage 4/5 pass on §10. No autonomous Gemini calls.
- Severity: M

## FIG-05 — Manually drawn figures (fig2–fig7) rule-14 exemption confirmed

- Source: `paper/figures/fig{2..7}-*.svg`.
- Observed: explicitly exempt from rule 14 per `paper/figures/README.md`. Filed as L bookkeeping so the registry shows the exemption was checked, not as a defect.
- Required action: none. Reconfirm whenever fig2–fig7 are revised.
- Severity: L

## FIG-06 — Structural-diagram figures (fig8, fig9, fig11, fig13–fig16) rule-14 data-absence

- Source: `paper/figures/fig{8,9,11,13,14,15,16}-*.py`.
- Observed: generation scripts present, no CSV — these encode structural relationships. README documents the exemption.
- Required action: none. L bookkeeping.
- Severity: L

## FIG-09 — Per-figure data-to-ink (Tufte) audit deferred

- Source: every `\includegraphics` in `paper/main.tex`.
- Observed: `viewer-blocked`. The prompt extension calls for flagging chartjunk shortcomings against the Tufte criteria; pixel-level inspection of each rendered float requires a working PDF viewer MCP, which was unavailable this pass.
- Required action: no immediate action. When the viewer MCP is restored, perform a one-shot per-figure audit (gridlines, 3D bevels, drop shadows, oversized legends, redundant titles, tick-label precision; under-inked indistinguishable series). File any finding as a follow-up FIG-* entry.
- Severity: L

---

## Items needing human-author decision (cross-referenced)

1. **LAY-12 / FIG-04** — second Gemini PNG for `logo-pandora-jar-intact.png`.
2. **§10 enumeration vs Figure 11 collapse (writer hand-back option a/b/c)** — FIG-08 caption-defer choice depends on this.
3. **FIG-02 colour migration scope** — full Viridis migration vs targeted palette tweak per figure (illustrator can implement either; the rhetorical choice is authorial).
