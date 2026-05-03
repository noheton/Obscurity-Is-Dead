# Illustrator (Stage 3) — Figure-overhaul pass 2026-05-03

- **Agent:** Claude Opus 4.7
- **Branch:** `claude/review-open-issues-PfNx9`
- **Trigger:** Author acknowledged that "only fig 1 is acceptable" in the
  current PDF; orchestrator dispatched a comprehensive figure-overhaul
  pass against the 7-dimension critique in
  `docs/prompts/layout-scrutinizer-prompt.md` § "FIGURE & IMAGE
  CRITIQUE".
- **Method note:** Pixel-level inspection unavailable (PDF viewer MCP
  disconnected). Critique therefore performed at source level: read of
  every `*.py` script, every `*.svg` head, palette codes against the
  Wong / Tol CB-safe palettes, font sizes against the ~9 pt
  print-legibility threshold.

---

## A. Inventory + critique (7-dimension table)

Status legend: `KEEP` (no change), `REWORK` (redone this pass),
`DEFER` (deferred to next pass), `EXEMPT` (rule-14 exemption noted).

| Fig | Cites | Legibility | Caption-figure consistency | Density | Colour accessibility | Alt-text in `.tex` | Data-to-ink | Rule-14 source | Status |
|----|-------|------------|----------------------------|---------|----------------------|--------------------|-------------|----------------|--------|
| 1 effort-gap | 1 | OK (annotations small but readable) | OK | OK | OK | **missing** (FIG-01 joint) | OK | compliant (data + script) | **KEEP** (author-accepted) |
| 2 boredom-barrier | 2 | small text | OK | OK | monochrome (CB-safe trivially) | missing | OK | EXEMPT (manual SVG) | **DEFER** (low-leverage; 2 cites) |
| 3 spider-farmer | 2 | small text | OK | OK | monochrome | missing | OK | EXEMPT (manual SVG) | **DEFER** |
| 4 ecoflow | 2 | small text | OK | OK | monochrome | missing | OK | EXEMPT (manual SVG) | **DEFER** |
| 5 methodology | 2 | small text | OK | OK | monochrome | missing | OK | EXEMPT (manual SVG) | **DEFER** |
| **6 dual-use** | **4** | small text in prior SVG | quadrants partly inferred from caption | OK | monochrome only | missing | OK | **was EXEMPT (manual SVG)** | **REWORK** — promoted to script (`fig6-dual-use.py`); CB-safe blue+orange; explicit quadrant labels |
| **7 threat-models** | **4** | small text in prior SVG | OK | OK | monochrome only | missing | OK | **was EXEMPT (manual SVG)** | **REWORK** — promoted to script (`fig7-threat-models.py`); per-hop auth-ring labels added |
| 8 ecoflow-surfaces | 1 | OK (9.5 pt labels) | OK | OK | uses red `#ffe6e6`/`#c0392b` for "legacy" surface — borderline CB | missing | OK | structural (no data file) | **DEFER** — keep red semantic for "legacy / undocumented", file FIG-02-residual; reworking would require renegotiating semantic colour story |
| **9 verification-pipeline** | 1 | small (8.5 pt body) | now needs 4-stage update | OK | red+green+yellow ramp **fails deuteranopia** | missing | OK | structural | **REWORK** — sequential blue ramp; added `[ai-confirmed]` 4th literature stage per CLAUDE.md ladder extension; raised body to 9.0–9.5 pt |
| **10 stage-effort** | 1 | OK | OK | OK | case-by-alpha (collapses in greyscale); red rule-1 annotation | missing | OK | compliant (data + script) | **REWORK** — case-by-colour (DLR_BLUE vs DLR_GREEN); recoloured rule-1 annotation to slate-grey; raised tick fonts to 9 pt |
| **11 eight-practices (HERO)** | 3 | row labels at 8.6 pt borderline | OK; ninth-practice deliberately not added | dense but readable | red `#c0392b` for fab-citations axis fails CVD | missing | OK | structural | **REWORK** — Tol-bright CB-safe header palette; raised row labels to 10.5 pt; zebra-row backgrounds; explicit P/S legend; numbered badges; widened figure |
| 12 difficulty-taxonomy | 1 | OK (10 pt cells; 12 pt title) | OK (post 2026-05-03 morning fix; Composite column dropped) | OK | sequential blue ramp — CB-safe | missing | OK | compliant (data + script) | **KEEP** (already redone this morning) |
| 13 pipeline-vulnerabilities | 1 | OK (9.2 pt) | OK | OK (6 nodes around central hub — fits) | mostly DLR neutrals + blue — CB-safe | missing | OK | structural | **KEEP** |
| **14 malicious-integrator** | 1 | 9.4 pt borderline | OK | OK | uses pure red `#c0392b` for adversarial branch — fails deuteranopia | missing | OK | structural | **REWORK** — Tol-bright orange `#ee6677` + hatched fill on every adversarial node so branch identity survives greyscale; raised labels to 10/9 pt; widened figure |
| 15 apk-mass-probing | 1 | 9.4 pt | OK | OK | green `#cad55c` + blue mix — borderline but distinguishable under deuteranopia (different hues) | missing | OK | structural | **DEFER** (not failing; lower-leverage) |
| 16 scope-limitations | 1 | 7.8 pt — under threshold | OK | OK (5 entries × 2 rings) | red `#fadbd8` for exclusion fails CVD | missing | OK | structural | **DEFER** — borderline; recommend rework next pass to (i) raise font and (ii) recolour exclusion ring |
| logo-pandora-jar-intact | 1 | placeholder typographic | n/a (placeholder) | n/a | n/a | missing | n/a | rule-14 OK (script committed) | **DEFER** (gated on Gemini deliverable; human-author decision) |

### Summary of dispositions

- **KEEP:** fig1, fig12, fig13 (3 figures)
- **REWORK (this pass):** fig6, fig7, fig9, fig10, fig11, fig14 (6 figures)
- **DEFER (next pass / human gate):** fig2, fig3, fig4, fig5, fig8, fig15, fig16, logo-pandora-jar-intact (8 figures)
- **EXEMPT note:** fig2–fig5 remain manually drawn, exempt under
  rule-14 exemption clause; documented in `paper/figures/README.md`.

---

## B. What was redone in this pass

### fig6-dual-use (NEW SCRIPT — promotion to scripted-source)

- **Was:** manually drawn monochrome SVG (rule-14-exempt).
- **Now:** `fig6-dual-use.py` matplotlib generator. CB-safe blue
  (researcher-governed) + Tol-bright orange `#ee6677` (adversarial)
  scatter on a 4-quadrant background (defensive disclosure /
  offensive automation / background information / productive
  interoperability). Six labelled points: 4 device cases + meta-process
  + adversarial-integrator. Author-assigned ordinal positions
  documented inline in the script docstring as the data source.
- **Rule-14 status:** generation script committed; no external CSV
  (positions are ordinal author rankings, not measurements — same
  pattern as fig7, fig8, fig9, fig11, fig13–fig16).

### fig7-threat-models (NEW SCRIPT — promotion to scripted-source)

- **Was:** manually drawn monochrome SVG.
- **Now:** `fig7-threat-models.py`. Side-by-side: left panel = single
  orange perimeter with 5 trusted internal nodes, no auth between
  them, "obscurity" in CB-safe orange; right panel = 5 nodes each
  ringed by its own DLR-blue auth boundary, 5 hop arrows labelled
  with the per-hop primitive (mTLS / HMAC / scoped token / signed
  event / row-level ACL).
- **Rule-14 status:** generation script committed; structural — no
  external data.

### fig9-verification-pipeline (REWORK)

- **Palette:** red `#fdecea` / yellow `#fff8be` / green `#e6eaaf` —
  fails deuteranopia + tritanopia — replaced by sequential blue ramp
  from `dlr_style` (light → mid → dark) that monotonically encodes
  verification depth and survives greyscale.
- **Content:** literature track extended from 3 stages to **4** —
  added the `[ai-confirmed]` stage between `[lit-retrieved]` and
  `[lit-read]` per CLAUDE.md "Verification status ladder (extended
  2026-05-02)". Source Analyzer agent labelled in the promotion
  arrow.
- **Typography:** stage-tag font raised from 10 → 11 pt; body 8.5 → 9.5;
  italic-claim 8.0 → 9.0.
- **Sloppification gate** annotation re-coloured from red to dark blue
  (CB-safe accent + bold).

### fig10-stage-effort (REWORK)

- **Case differentiation:** previously case-by-alpha on the same blue
  hue — alpha-only differentiation collapses to the same grey under
  desaturation. Now Spider-Farmer = DLR_BLUE family, EcoFlow = DLR_GREEN
  family. Within a case, AI = saturated, manual = soft.
- **Rule-1 annotation** ("validation phase omitted for EcoFlow") was in
  red (#c0392b). Recoloured to slate-grey + italic to avoid relying on
  red+green pairings.
- **Typography:** tick / annotation 7.5 → 9.0 pt.

### fig11-eight-practices (REWORK — visual-abstract / hero figure)

- **Palette:** column-header red `#c0392b` ("Fabricated citations")
  fails deuteranopia. Replaced with Tol-bright triple
  (`#4477aa` / `#228833` / `#aa7733`) — all CB-safe and
  greyscale-distinguishable.
- **Marker redundancy:** P (filled disc) vs S (ring with bar) is now
  shape-redundant with colour, so meaning survives greyscale.
- **Typography:** row labels 8.6 → 10.5 pt; header 12.5 → 13.5 pt;
  P/S glyph 9 → 10 pt. Numbered badges as DLR-blue circles for
  visual anchoring.
- **Density:** added zebra-row backgrounds for 8-row scan-readability.
- **Row count:** kept at 8 per the §10 explicit instruction
  ("ninth practice logged for the next iteration of the framework
  rather than added to Figure 11").

### fig14-malicious-integrator (REWORK)

- **Palette:** pure red `#c0392b`, `#fadbd8`, `#f5b7b1` for the
  adversarial branch fails deuteranopia. Replaced by Tol-bright
  rose-orange `#ee6677` paired with hatched (`//`) fill on every
  adversarial node so branch identity survives both CVD and
  greyscale.
- **Typography:** 9.4/8.0 → 10.0/9.0 pt for label/sublabel.
- **Width:** widened figure to 13" for subtitle relief.

---

## C. Items deferred (next pass)

| Fig | Deferred reason | Recommended next-pass action |
|-----|-----------------|------------------------------|
| fig2, fig3, fig4, fig5 | Low cite-count (2 each); manually drawn but rule-14 exempt; budget management | Promote to scripted source if a future pass has spare budget; otherwise leave exempt |
| fig8 | Red `#ffe6e6` `#c0392b` semantically tagged as "legacy / undocumented" surface — recolouring requires renegotiating the semantic story | Replace red with Tol-bright orange + hatched fill per fig14 pattern |
| fig15 | Borderline only; lower leverage | Recolour stage-2/3/4 fills from `#cad55c` (green) to a CB-safe ramp |
| fig16 | Inner cell font 7.8 pt under threshold; red exclusion ring fails CVD | Raise to ≥9 pt; replace red exclusion ring with hatched orange |
| logo-pandora-jar-intact | Gated on second Gemini deliverable from human author | No illustrator action; human-author gate |

## D. Items needing human-author input

1. **Logo deliverable.** Replace
   `paper/figures/logo-pandora-jar-intact.png` with the second
   Gemini-generated PNG. Until then the typographic placeholder remains
   and the §10 honesty disclosure stands (carried over from prior pass).
2. **fig8 palette story.** Confirm whether the red on the legacy-REST
   surface is *semantically* load-bearing (red = "do not use") or
   merely aesthetic. If load-bearing, the next pass should swap to a
   CB-safe red equivalent (`#ee6677`) plus hatched fill so the
   "do-not-use" warning survives greyscale.
3. **fig2–fig5 promotion.** Decide whether to promote the four
   remaining manually drawn figures to scripted-source for full
   rule-14 coverage. They are low-cite-count (2 each) so budget vs
   benefit favours leaving them exempt unless the author wants
   uniform reproducibility across the whole figure stock.
4. **§10 enumeration vs Figure 11 collapse** (carried over from
   readability handback RDB-04). Figure 11 is now visually
   strengthened; the writer can take options (a) / (b) / (c) on the
   §10 prose with confidence the figure carries the load.

## E. Caption-fidelity check (rule 11 spirit)

No `paper/main.{md,tex}` caption rewrites were made this pass. The
six redone figures retain identical LaTeX labels (`fig:dual-use`,
`fig:threat-models`, `fig:verification-pipeline`, `fig:stage-effort`,
`fig:eight-practices`, `fig:malicious-integrator`) so all
`\cref{...}` / `\ref{...}` cross-references continue to resolve.

Two captions to flag for the **writer** as candidate for tightening
(non-blocking, the figures still match):

- **fig9 caption.** Now references 4 literature-track stages (added
  `[ai-confirmed]`); current caption text in `paper/main.tex` may
  still mention only 3 stages. Writer should confirm.
- **fig11 caption.** Header text now says "P (filled disc) =
  principal mitigation; S (ring) = secondary mitigation"; if the
  caption duplicates this legend text, it is now redundant.

## F. Rule-1/11/13/14/15 check

- **Rule 1 (honesty):** every regenerated script's docstring records
  what changed and why. The fig6 + fig7 ordinal positions are
  flagged as author-assigned, not measured. The fig11 P/S mapping
  is flagged as "the agent's reading … auditable against §7.6 /
  §7.8 / §9.4".
- **Rule 11 (mirror discipline):** no `paper/main.{md,tex}` edits
  this pass; mirror is unchanged.
- **Rule 13 (no publication):** no `make pdf`, no `make arxiv`, no
  push.
- **Rule 14 (data + script committed):** fig6 and fig7 promoted from
  exempt to compliant. fig9, fig10, fig11, fig14 already compliant
  (scripts present); reworked content still resolves to script + (for
  fig10) the unchanged CSV.
- **Rule 15 (README mirror):** the visual abstract
  (`fig11-eight-practices.svg`) was reworked; the top-level `README.md`
  hero-image reference is unchanged (same filename, same label) so
  the README remains consistent. No new figure files added (fig6 +
  fig7 SVGs replaced existing files).

## G. RE-ANALYSIS REQUIRED

`RE-SCRUTINY REQUIRED: yes` — Stage 4 must rebuild
`paper/main.pdf` and re-sweep the six reworked figures plus the
eight deferred ones at the new pixel level. Specifically expected
deltas:

1. Six figures now CB-safe (FIG-02 partial-resolution).
2. Hero fig11 row-label legibility raised from 8.6 pt to 10.5 pt
   (FIG-03 closure expected).
3. Caption-fidelity check on fig9 (4-stage track) and fig11 (P/S
   legend text) → routes to writer.
4. FIG-01 (alt-text-missing across all 18 floats) is **unchanged**
   this pass — it requires `\Description{...}` macros in
   `paper/main.tex`, owned by the writer; illustrator can confirm
   text matches asset on the writer's pass.

Files touched this pass:

- `paper/figures/fig6-dual-use.py` (NEW)
- `paper/figures/fig6-dual-use.{svg,pdf}` (regenerated, replaces manual)
- `paper/figures/fig7-threat-models.py` (NEW)
- `paper/figures/fig7-threat-models.{svg,pdf}` (regenerated, replaces manual)
- `paper/figures/fig9-verification-pipeline.{py,svg,pdf}`
- `paper/figures/fig10-stage-effort.{py,svg,pdf}`
- `paper/figures/fig11-eight-practices.{py,svg,pdf}`
- `paper/figures/fig14-malicious-integrator.{py,svg,pdf}`
- `paper/figures/README.md` (inventory + dispositions updated)
- `docs/handbacks/illustrator-pass-2026-05-03-overhaul.md` (this file)
- `docs/logbook.md` (session entry appended)
