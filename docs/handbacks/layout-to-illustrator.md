# Layout → Illustrator hand-back (round 2 — 2026-05-03)

> Stage 4 → Stage 3 routing. Build commit `d2858ac` (the figure-overhaul
> commit itself); PDF SHA-256
> `db8774f125898ab4d0fd3d3450c39c4e5b3fc2f425fdc4c9a25af270f4d511d2`;
> 53 pages.

Round-1 figure-side state: FIG-01 (alt-text-missing) **CLOSED** by writer
on `4987d9d`; FIG-02 / FIG-03 closed for the six reworked figures
(fig6/7/9/10/11/14) per `d2858ac`; method note: pixel-level visual
verification is `viewer-blocked` for this scrutiny round (no PDF viewer
MCP), so the items below are filed at L unless source inspection alone
justifies higher.

## FIG-10 — L — Alt-text fidelity audit (post-FIG-01-closure)

- Source: `main.tex:355, 420, 605, 644, 882, 905, 1139, 1500, 1589, 1727, 1762, 1770, 2229, 2352, 2458, 2739, 2860` (every `\includegraphics` followed by `\Description{...}`).
- Observed: writer authored `\Description{}` text from the `\caption{}` and asset filename, not from pixels. Each text is ≤25 words and factual.
- Required action: walk each rendered figure float; confirm the description names what the figure visually shows (panel count, axes, called-out features). If a description is wrong, route a **caption-fidelity** correction back to the writer (FIG-10 has owner = illustrator only for the audit; the fix belongs to the writer because the macro lives in `main.tex`).
- Severity: L (FIG-01 H closed; this is residual confirmation).

## FIG-11 — M — Residual CB-palette work on the deferred figures

Per the illustrator hand-back's "DEFER" set, three figures still carry CB-fail palettes:

- **fig8 (`fig8-ecoflow-surfaces`)** — red `#ffe6e6` / `#c0392b` for the "legacy / undocumented" surface. Gated on **human-author decision** ("is the red semantic 'do-not-use'?"). If yes: swap to Tol-bright `#ee6677` + hatched fill, mirroring the fig14 pattern. If no: drop the red entirely.
- **fig15 (`fig15-apk-mass-probing`)** — green `#cad55c` borderline; lower leverage.
- **fig16 (`fig16-scope-limitations`)** — red `#fadbd8` exclusion ring fails CVD; inner cell font 7.8 pt under 9 pt threshold. Recolour exclusion ring to hatched orange and raise font to ≥9 pt.

- Severity: M (each has at least one CB-failure plus, for fig16, a legibility-threshold violation).

## FIG-04 — M — Intact-jar Gemini deliverable (carry-over)

- Asset: `paper/figures/logo-pandora-jar-intact.png`.
- Status: still the matplotlib typographic placeholder. Gated on the second Gemini PNG from the human author. No illustrator action required until the deliverable lands.
- Severity: M (carry-over from round 1).

## Items closed for the six reworked figures (informational)

- **fig6 (`fig6-dual-use`)** — promoted to script (`fig6-dual-use.py`), rule-14-compliant, CB-safe.
- **fig7 (`fig7-threat-models`)** — promoted to script (`fig7-threat-models.py`), rule-14-compliant.
- **fig9 (`fig9-verification-pipeline`)** — sequential blue ramp; 4-stage track including `[ai-confirmed]`. CB-safe. Caption text at `main.tex:1139` reviewed: it describes "two parallel verification pipelines (literature track and artifact track) with gated stages and arrows showing how each cited source progresses to a final confirmed status" — matches the reworked asset; the 4-stage extension is implicit in "gated stages". Recommend **close** on next visual sweep.
- **fig10 (`fig10-stage-effort`)** — case-by-colour (DLR_BLUE vs DLR_GREEN), slate-grey rule-1 annotation. CB-safe.
- **fig11 (`fig11-eight-practices`, hero)** — Tol-bright header palette, P/S marker shape-redundant, 10.5 pt row labels, zebra rows. CB-safe and greyscale-survives. Caption at `main.tex:2860` carries the P/S legend; the in-figure legend now also embeds it. Defer FIG-08 (caption legend redundancy) per RDB-04 author decision.
- **fig14 (`fig14-malicious-integrator`)** — Tol-bright `#ee6677` + hatched fill on adversarial branch. CB-safe and greyscale-survives.

## Items previously bookkept

- **FIG-05** (rule-14 advisory): fig2 / fig3 / fig4 / fig5 remain manually drawn, exempt under the rule-14 exemption clause; documented in `paper/figures/README.md`. fig6 + fig7 promoted to compliant.
- **FIG-06** (structural-data exemption): seven structural-diagram SVGs encode relationships, not numerical data; documented exemption.
- **FIG-09** (Tufte chartjunk audit): viewer-blocked. Recommend a follow-up pixel-level pass once the PDF viewer MCP is restored.

## Suggested illustrator-loop strategy

Single highest-leverage move: get the human-author decision on fig8's
red semantics, then either (a) swap fig8/fig15/fig16 palettes in one
script-edit pass mirroring the fig14 hatched-orange pattern, or (b)
defer all three to a future loop. Independently of fig8, fig16's font
threshold (7.8 pt → ≥9 pt) is unconditionally a fix worth shipping.

The intact-jar logo remains gated on the human author; no illustrator
action until the Gemini PNG arrives.
