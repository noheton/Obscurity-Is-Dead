# Layout Scrutiny — 2026-05-04 — post-rewrite build (Claude Opus 4.7)

> Stage 4 sweep against `paper/main.pdf` rebuilt on branch
> `claude/history-rewrite-daDxQ` after writer commit `ce265e0`
> ("paper(writer): consolidate post-rewrite redaction narrative;
> anchor at §5.6"). Triggered by the integration brief
> `docs/handbacks/integration-pass-2026-05-04-post-rewrite.md`.
> P3 in `docs/todos-for-publication.md`.

## Build under inspection

- **PDF SHA-256:** `bd01b411de160a65cfd95a08ec9de62c062737790a409ec59567ce7c209dbb31`
- **PDF size / pages:** 1,251,038 bytes / **57 pages** (round-4 baseline: 1,236,060 / 54). The +3-page delta is materialised primarily in §7 / §8: the dual-use plane (Fig 11), the two threat-model panels (Fig 13), Fig 14 (APK mass probing), and Fig 15 (scope) each now occupy a dedicated full page (pp 53, 54, 55, 56) with substantial bottom whitespace. Body text otherwise reflows cleanly around the writer's §5.6 trailing-clause edit (commit `ce265e0`).
- **PDF mtime:** 2026-05-04T06:11 (newer than `paper/main.tex` 06:09).
- **LaTeX log:** `paper/main.log` (51,907 bytes). Counts: **34 `Overfull \hbox`** (round-4: 33; +1 from the §5.6 trailing-clause edit), **67 `Underfull \hbox`** (unchanged), **0 `Reference … undefined`**, **0 `Citation … undefined`**, **0 `??`**, no `Float too large`, no `Missing` macros. Cosmetic font-shape `OT1/cmtt → OT1/lmtt` carry-forward at preamble persists (LAY-14/-23 family).
- **Method.** Pages rendered to PNG via PyMuPDF at 150 dpi (full sweep, all 57 pages) and at 220 dpi for primary anchors (pp 12, 19, 20, 55). Visual sweep performed at PNG resolution; structural metrics cross-checked against `paper/main.log` source-line spans.

## Round-4 carry-over disposition (delta vs `layout-defect-registry.md` round 3 + `layout-scrutiny-2026-05-03-round4.md`)

| ID | Round-3 / r4 status | This round | Note |
|----|---------------------|------------|------|
| LAY-01 | RESOLVED | RESOLVED | Zero undefined refs / cites in log. |
| LAY-02 / LAY-24 | PARTIAL (M) | PARTIAL (M) | §1.6 contributions enumerate still produces overfulls at `:504–508` (32.16pt) and `:508–513` (11.72pt). Lines unchanged from round 3 modulo +25 from §5.6 edit. Path-bullet family. |
| LAY-03 / LAY-25 | PARTIAL (L/M) | PARTIAL | §5.2 / §6.x path-bullet cluster at `:976–980` (66.67pt) + `:983–989` (12.76pt) + `:1102–1112` (70.84pt) + `:1117–1120` (69.91pt) + sibling sub-pt-spread items. Same root cause: long `\fp{...}` / `\texttt{...}` literals not yet wrapped in `\seqsplit{}`. **Net unchanged.** |
| LAY-04 | PARTIAL (L) | PARTIAL | 0.18pt residual at `:1471–1486`. Effectively closable. |
| LAY-05 | RESOLVED | RESOLVED | Figure 7 float clean. |
| LAY-06 | PARTIAL (M) | PARTIAL | Difficulty-taxonomy table residual at `:1503–1504` (30.26pt) + `:1505–1506` (52.64pt) + `:1554–1555` (8.80pt) + `:1552–1578` (2.53pt). Same lines as round 3. |
| LAY-08 | PARTIAL (M) | PARTIAL | §4.4 region produces `:650–652` (12.07pt) + `:682–685` (66.39pt) + `:701–710` (1.13pt). Writeable-entity comma-list pressure. **Unchanged.** |
| LAY-09 / LAY-22 | PARTIAL (M) | PARTIAL | §6.6 / §6.7 / §10 path-bullet cluster at `:1124–1129` (28.89 + 56.22pt), `:1146–1151` (43.53pt), `:1161–1164` (5.21pt), `:1182–1187` (61.91pt). Same root cause. **Unchanged.** |
| LAY-10 / LAY-29 | PARTIAL (M) | PARTIAL | Trailing-matter / §10 region overfulls at `:2738–2741` (50.18pt), `:2741–2747` (3.58pt), `:2773–2795` (35.69pt), `:2858–2862` (37.70pt), `:3027–3035` (**70.91pt**, largest in document), `:3040–3045` (32.31pt), `:3063–3068` (16.08pt). Same `\seqsplit{}` opportunity that closed LAY-26 in round 3. |
| LAY-12 | PARTIAL (L) | PARTIAL | Intact-jar Gemini deliverable still a placeholder on p44. Honestly disclosed in caption. |
| LAY-14 / LAY-23 | L (carry) | L (carry) | OT1/cmtt → OT1/lmtt cosmetic. |
| LAY-16 | PARTIAL (L) | PARTIAL | Bibliography underfulls persist (auto-generated, long URLs). |
| LAY-18 | PARTIAL (L) | PARTIAL | §6.x underfull cluster persists. |
| LAY-20 / LAY-21 | PARTIAL (M) | PARTIAL | §6.4 underfull region cosmetic. **Unchanged.** |
| LAY-26 | RESOLVED (was H) | RESOLVED | `\seqsplit{}` refactor at the prior `:2582–2585` line band still anchors clean. |
| LAY-27 / LAY-28 | L (carry) | L (carry) | Spider Farmer tabularx intra-cell residuals. |
| LAY-30 | L (advisory) | L (advisory) | New powerocean bib entries' underfulls. Cosmetic. |
| FIG-01 | RESOLVED | RESOLVED | All `\Description{}` macros present. |
| FIG-04 / FIG-08 / FIG-11 | M (round 3) | M (FIG-04 / FIG-08 only); FIG-11 RESOLVED | Round-4 closure of FIG-11 holds: fig8 / fig15 / fig16 CB-safe palette + 9 pt body floor materialised in the rendered PDF. |
| FIG-12 | L (round 4) | L (carry) | fig16 inner-ring label encroachment still cosmetic; same advisory disposition. |

## New defects this round

| ID | Page | Region | Defect class | Severity | Owner | Source span | Suggested fix |
|----|------|--------|--------------|----------|-------|-------------|---------------|
| **LAY-31** | 20 | §5.6 *Live-credential leakage* bullet | overfull-prose-path-trailing-clause | M | writer | `paper/main.tex:1253–1273`, mirrored at `paper/main.md:365`-region | The post-rewrite trailing clause introduced one new overfull at `:2262–2271` (25.75pt). Root cause: the unbreakable literals `\texttt{noheton/spider\_farmer}` and `\texttt{noheton/powerocean-dev}` plus the `experiments/*/original/` path token in close succession. Fix: wrap each upstream repo path in `\seqsplit{...}` (mirror the LAY-26 pattern), or — preferred per Stage-5 RDB-39 — split the trailing clause into a separate sentence that drops the path-density. Rule-11 mirror needs both `paper/main.tex` and `paper/main.md` updated. |
| **LAY-32** | 55 | Figure 14 dark-fill stage-box | label-collision (figure-internal) | **H** | illustrator | `paper/figures/fig15-apk-mass-probing.py` (header label "DEX-grep + identity-provider discovery" + body label "T-REST-WRITE-PROBE; token-endpoint enum") | The fourth (dark teal) stage box renders the header label and the inner body label overlapping each other — the header descender lands on top of the body-label baseline, producing a legibility failure. Visible at the 150-dpi PNG render of page 55 and confirmed at 220 dpi. The other four stage boxes do not collide, so the regression is local to the dark-fill (or to the longer header text). Fix: either reduce header font size by 0.5–1 pt for the dark-fill box only, raise the box height by ~10 %, or split the header onto two lines ("DEX-grep" / "+ identity-provider discovery"). Owner: illustrator. The figure asset is otherwise round-4-RESOLVED on palette and 9 pt floor. |
| **LAY-33** | 53–56 | Pages 53 / 54 / 55 / 56 — full-page floats | float-leading-whitespace | L | writer (advisory) | `paper/main.tex` figure float specifiers around `\label{fig:dual-use-map}` (Fig 11), `\label{fig:malicious-integrator}` (Fig 13), `\label{fig:apk-mass-probing}` (Fig 14), `\label{fig:scope-limitations}` (Fig 15) | Each of pages 53–56 is now a near-full-page float with substantial vertical whitespace (top half of page 53; bottom 35–40 % of pages 54 / 55 / 56). The PDF has grown 54 → 57 pages with no body-text growth proportionate to the page count. This is normal LaTeX float behaviour (`[!htbp]` cascading to `[t]` and stranding floats on dedicated pages once two consecutive figures land near a section break) but it inflates page count and widens the gap between the figure and its first textual reference. Fix: consider promoting the four floats to `[!t]` only (pin to top-of-page) and add a `\FloatBarrier` after §7.13 / §7.14 / §7.15 to prevent the cascade, or accept the 3-page inflation and close as L. Rule-15 spirit (visual rhythm) is at stake but no claim is hidden. |

No new H-severity defects in the prose; **one** new H in figure-internal layout (LAY-32 fig14 label collision), one new M in the §5.6 region (LAY-31 trailing-clause path overflow), one new L (LAY-33 float pagination). The §5.6 reflow event predicted by the integration brief materialised exactly as described — the trailing clause grew the bullet by ~3 lines and added one anchored overfull (25.75pt) on top of the existing carry-over family.

## §5.6 reflow audit (integration-brief explicit anchor)

The integration brief said: *"The §5.6 bullet just grew by ~3 lines; expect minor reflow on the page that previously hosted it."* Verification:

- Pre-rewrite host page for the live-credential bullet: page 19 (round-3 baseline). Post-rewrite host: **page 20**, with the bullet now spanning 11 lines (up from 8) including the trailing-clause about upstream `noheton/spider_farmer` / `noheton/powerocean-dev` redaction pre-condition.
- The KPI summary table that previously immediately followed §5.6 on the same page now lands lower on page 20 with healthy bottom margin; the page break between §5.6 and §5.7 is clean (no widow / orphan).
- The §5.6 bullet's third grammatical sentence — flagged by Stage 5 as RDB-39 (three thoughts: rewrite-execution + carve-out + upstream-pre-condition) — is structurally responsible for the new 25.75pt overfull (LAY-31). Splitting the sentence per RDB-39 will likely close LAY-31 as a side-effect; the writer pass that picks up RDB-39 should bookkeep LAY-31 as joint-resolved.
- No widow / orphan introduced anywhere on pages 19–21 by the reflow.

## Other figure / float spot-checks

- **Figure 6 (Spider Farmer case study), p11:** clean, no regression from round 4.
- **Figure 8 (EcoFlow API surfaces), p15:** clean, CB-safe palette + hatch encoding holds.
- **Figure 9 (verification pipeline), p19:** clean, 9 pt body floor holds, no collisions.
- **Figure 10 (effort-gap stage chart), p21:** clean, two-panel layout holds.
- **Figure 11 (dual-use plane), p53:** float landed on dedicated page; figure-internal layout clean; whitespace concern noted as LAY-33.
- **Figure 12 (difficulty taxonomy), p25:** clean.
- **Figure 13 (two threat models), p54:** clean, two-panel comparison holds; whitespace concern noted as LAY-33.
- **Figure 14 (APK mass probing), p55:** **LAY-32 H** — dark-fill stage-box label collision.
- **Figure 15 (scope and limitations), p56:** carry-forward FIG-12 (L) inner-ring label encroachment unchanged from round 4; otherwise clean.

## Severity rollup (current open state, post-this-pass)

- **H:** **1** (new: LAY-32 fig14 label collision; fig-internal, illustrator-owned). Round-3 H count was 0; the fig14 collision is a regression introduced after the round-4 illustrator pass.
- **M:** 9 distinct items: LAY-02/-24, LAY-06, LAY-08, LAY-09/-25, LAY-10/-29, LAY-22, **LAY-31 (new)**, FIG-04, FIG-08.
- **L:** 15: LAY-03 (downgraded), LAY-04, LAY-12, LAY-14/-23, LAY-16, LAY-18, LAY-27, LAY-28, LAY-30, **LAY-33 (new)**, FIG-05, FIG-06, FIG-09, FIG-10, FIG-12.

## Severity by class

- **Layout (LAY-*):** H=0, M=8, L=10 (was H=0, M=7, L=9 in round 3).
- **Figure (FIG-*):** **H=1 (new)**, M=2, L=4. The H is illustrator-owned and routes via `docs/handbacks/layout-to-illustrator.md`.

## Owner rollup

- **Writer:** LAY-02/-24, LAY-06, LAY-08, LAY-09/-25, LAY-10/-29, LAY-22, **LAY-31 (new)**, LAY-03, LAY-04, LAY-16 (advisory), LAY-18, LAY-27, LAY-28, LAY-30, **LAY-33 (advisory, new)**, LAY-14/-23 (cosmetic).
- **Illustrator:** **LAY-32 (new, H)**, FIG-04 (Gemini-gated), FIG-05/-06 bookkeeping, FIG-09 audit-incomplete, FIG-10 fidelity audit, FIG-12 (L, fig16 inner-ring residual).
- **Joint:** none.

## Mirror, redaction, distribution

- **Rule 11 (mirror discipline).** Writer commit `ce265e0` declared mirror parity at `paper/main.md` ↔ `paper/main.tex` for the §5.6 trailing-clause edit and the §9.4 disclaimer cross-reference. Layout sweep does not edit either file. Cross-references resolve (zero `??`).
- **Rule 12 (redaction).** No new credentials / serials / UIDs / IPs in the post-rewrite text. The `[REDACTED:repo-path:BALBOA-UPSTREAM-{1,2}]` markers persist at `main.tex:2267–2268` (line-shifted from round 3 `:2228–2229` by the §5.6 edit). The new `\texttt{noheton/spider\_farmer}` and `\texttt{noheton/powerocean-dev}` literals in §5.6 are upstream-repo paths (public on GitHub by author decision per `docs/redaction-policy.md`); they are not redaction targets.
- **Rule 13 (no publication).** Local PDF only. `make arxiv` not invoked.

## Hand-back routing

- `docs/handbacks/layout-to-writer.md` — append LAY-31 (M, §5.6 trailing-clause overfull; preferred fix is the Stage-5 RDB-39 sentence split which would joint-close both) and LAY-33 (L advisory, full-page float pagination).
- `docs/handbacks/layout-to-illustrator.md` — append **LAY-32 (H)**, fig14 dark-fill stage-box header / body-label collision. Fix in `paper/figures/fig15-apk-mass-probing.py`. Suggested options: header font −0.5/−1 pt for dark-fill boxes only; or two-line header break; or +10 % box height for dark-fill boxes.
- `docs/handbacks/layout-defect-registry.md` — full registry update deferred to the next non-narrow Stage-4 pass; this round records its changes here and in the round-4 file.

## Verdict

**RE-SCRUTINY REQUIRED: yes**

Rationale: one new H-severity defect (LAY-32, fig14 dark-fill stage-box label collision) is illustrator-owned and must be fixed before any submission artefact is built; one new M (LAY-31) inherits the §5.6 trailing-clause overflow that the writer pass introduced. The path-bullet M-cluster (LAY-02 / -09 / -10 / -22 / -29) carries forward unchanged and can be cleared in the same writer sweep that addresses LAY-31 plus Stage-5 RDB-39 / RDB-40. After (a) the illustrator regenerates `fig15-apk-mass-probing.pdf` with the LAY-32 fix, (b) the writer addresses LAY-31 (likely jointly with RDB-39), and (c) `make pdf` rebuilds, Stage 4 should re-sweep — primarily to verify LAY-32 closure and confirm LAY-33 (full-page float whitespace) is acceptable or escalated.
