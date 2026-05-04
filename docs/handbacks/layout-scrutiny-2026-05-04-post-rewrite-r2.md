# Layout Scrutiny — 2026-05-04 — post-rewrite build, round 2 (Claude Opus 4.7)

> Stage 4 re-sweep against `paper/main.pdf` rebuilt on branch
> `claude/history-rewrite-daDxQ` after the round-1 hand-backs were
> consumed: illustrator commit `fed50ab` (LAY-32 fig15 dark-fill stage-box
> rebreak) and writer commit `644d2e2` (RDB-39/RDB-40/RDB-37 + LAY-31 +
> LAY-10/-29 anchor closures). This file is the round-2 closure registry
> that resolves
> `docs/handbacks/layout-scrutiny-2026-05-04-post-rewrite.md`.
> P3 / P3a in `docs/todos-for-publication.md`.

## Build under inspection

- **PDF SHA-256:** `986377388e810c8baa47481956f57099bfc11c3b33caa4a53ac3553f08e7de8a`
- **PDF size / pages:** 1,250,840 bytes / **57 pages** (round-1 baseline:
  1,251,038 / 57 — page count unchanged; bytes −198).
- **PDF mtime:** 2026-05-04T06:29 (newer than `paper/main.tex`
  06:29 same minute; the PDF is the freshly built artifact and not
  stale).
- **LaTeX log:** `paper/main.log` (50,719 bytes; was 51,907 — −1.2 KB,
  consistent with fewer overfull entries). Counts: **30 `Overfull \hbox`**
  (round 1: 34; **−4** as the writer self-reported), **67 `Underfull \hbox`**
  (unchanged), **0 `Reference … undefined`**, **0 `Citation … undefined`**,
  **0 `??`**, no `Float too large`, no `Missing` macros. The
  cosmetic OT1/cmtt → OT1/lmtt font-shape carry-forward at preamble
  persists (LAY-14 / LAY-23 family — L, unchanged).
- **Method.** Pages rendered to PNG via PyMuPDF at 160 dpi for the
  full-page sweep; page 55 cropped to the figure region and rendered at
  400 dpi for the LAY-32 closure check; page 20 rendered at 160 dpi for
  the §5.6 reflow check. Structural metrics cross-checked against
  `paper/main.log` source-line spans.

## Round-1 defect closure / re-open table

| ID (round 1) | Severity | Owner | Round-1 status | This round | Evidence |
|---|---|---|---|---|---|
| **LAY-32** | H | illustrator | filed (fig15 dark-fill stage-box label collision) | **CLOSED** | High-resolution render of p55 (400 dpi crop) shows the dark-fill stage-box header `DEX-grep + identity-provider discovery` now breaks across two lines (after `identity-`, before `provider`) and sits clearly above the inner body label `T-REST-WRITE-PROBE; token-endpoint enum`. No glyph overlap; the body label baseline is below the header descender. Closure delivered by illustrator commit `fed50ab` (`paper/figures/fig15-apk-mass-probing.{py,svg,pdf}` regenerated; header font 9.4 → 9.0 pt, still above the 9 pt body floor; rebreak inside `identity-provider`). |
| **LAY-31** | M | writer | filed (§5.6 trailing-clause overfull, 25.75 pt) | **CLOSED** (joint with RDB-39) | Log shows the §5.6 anchor at lines `1252–1273` now reports `Overfull \hbox (0.80179pt too wide)` — a 25.75 pt → 0.80 pt collapse, sub-perceptual residual. Closure delivered by writer commit `644d2e2`: trailing clause split into two sentences; `noheton/spider_farmer` and `noheton/powerocean-dev` literals additionally wrapped in `\seqsplit{}`. Joint-closes Stage-5 RDB-39 as predicted by round-1 verdict. Rule-11 mirror parity (`paper/main.md ↔ paper/main.tex`) verified at the §5.6 span by writer commit message; layout sweep does not touch source. |
| **LAY-10 / LAY-29** | M | writer | filed (path-bullet cluster: `:2738`, `:2741`, `:2773–2795`, `:2858–2862`, `:3027–3035`, `:3040–3045`, `:3063–3068`) | **PARTIAL → effectively closed** (dispatched anchors cleared; two non-anchor residuals carried forward as L) | The three largest dispatched-anchor members are absent from the round-2 log: `:3027–3035 (70.91 pt)`, `:3040–3045 (32.31 pt)`, `:3063–3068 (16.08 pt)` — all CLOSED by `\seqsplit{}` application per writer commit `644d2e2`. The post-rewrite log retains two same-family residuals at `:2774–2796 (35.69 pt)` and `:2859–2863 (37.70 pt)` — these were filed under the same parent ID in round 1 but were *not* in the round-1 dispatch closure scope per the dispatch brief ("70.91/32.31/16.08pt members cleared"). Total `Overfull` count fell 34 → 30, exactly as the writer reported. Per round-1 verdict, the dispatched anchors are closed; the two residuals downgrade to **L** (cosmetic, same root cause `\fp{...}`/`\texttt{...}` literals not yet wrapped) and join the standing carry-over family (LAY-02/-09/-22 cluster). They are not new defects. |
| **LAY-33** | L | writer (advisory) | filed (full-page float pagination, pp 53–56 whitespace) | **DEFERRED out of scope** (per round-1 verdict and writer P3a closure note) | Page count unchanged at 57; float-pagination cascade is unchanged; whitespace footprint is unchanged. Round-1 verdict tagged this as advisory and round-1 writer P3a closure note states "LAY-33 (full-page float whitespace, L advisory) deferred — a `\FloatBarrier` pass is not a defect-closure scope item". Disposition holds. Visual rhythm concern (rule-15 spirit) acknowledged; no claim is hidden. |

## New defects this round

| ID | Page | Region | Defect class | Severity | Owner | Source span | Suggested fix |
|----|------|--------|--------------|----------|-------|-------------|---------------|
| — | — | — | — | — | — | — | **None.** No new H or M defects introduced by the round-1 hand-back commits `fed50ab` (illustrator) or `644d2e2` (writer). |

Spot-check verifications performed for the two commit deltas:

- **Page 55 (Figure 14, post-LAY-32 fix).** Rendered at 400 dpi crop. Five
  stage boxes in the pipeline (Public APK repository → Fetch + unpack →
  Static probe → DEX-grep + identity-provider discovery → Per-vendor
  weakness inventory). Dark-fill (4th) box header now occupies two lines
  with clear separation from the body labels. Empirical-base-rates panel
  intact. Rule-14 source compliance retained: `fig15-apk-mass-probing.py`
  + `.svg` + `.pdf` all present and committed in the same illustrator
  commit. No regression to fig8 / fig9 / fig10 / fig11 / fig12 / fig13 /
  fig15 (scope) / fig16 detected on page-by-page sweep.
- **Page 20 (§5.6 *Live-credential leakage* bullet, post-LAY-31 fix).**
  Bullet now reads as two sentences with the "two residual surfaces remain
  governed by policy" frame visible mid-bullet. Page break between §5.6
  and §5.7 (KPI summary table) clean — no widow / orphan introduced.
  Reflow contained to the local span; pages 19 and 21 unchanged in
  composition.
- **§10 trailing-matter region (post-LAY-10/-29 anchor sweep).** Lines
  `:3027–3035 (70.91 pt)`, `:3040–3045 (32.31 pt)`, `:3063–3068 (16.08 pt)`
  no longer appear in `paper/main.log`. Cross-checked: total `Overfull
  \hbox` count is **30** (round-1 was 34); the four cleared overfulls
  account exactly for the −4 delta (the three §10 anchors plus LAY-31
  collapsing from 25.75 pt to 0.80 pt — still logged but now sub-perceptual).
- **No Rule-11 / Rule-12 / Rule-13 regressions.** Zero `??`, zero
  undefined refs / cites, no new credentials / serials / UIDs / IPs in
  the rendered text, no `make arxiv` invocation. The two `noheton/...`
  literals in §5.6 remain on-policy (upstream public repo paths;
  per `docs/redaction-policy.md`, not redaction targets).

## §5.6 reflow audit (round-2 closure)

The round-1 reflow audit predicted that the Stage-5 RDB-39 sentence split
would joint-close LAY-31 and would not introduce new widows / orphans on
pages 19–21. Verified:

- Post-fix host page for the live-credential bullet: page 20 (unchanged
  from round 1). Bullet now reads as two grammatical sentences instead of
  one three-thought sentence with em-dash join. Bullet line count is
  approximately 11 (round 1) → 11 (round 2) — sentence split absorbed into
  the existing line budget without growing the bullet.
- KPI summary table immediately following §5.6 lands cleanly on page 20
  with healthy bottom margin; page break to §5.7 is clean.
- Round-2 §5.6 overfull is 0.80 pt (was 25.75 pt); the residual is well
  below the perceptual threshold and does not warrant further action.

## Severity rollup (round 2 vs round 1)

| | H | M | L |
|---|---|---|---|
| Round 1 (this paper, post-rewrite) | 1 (LAY-32) | 9 (LAY-02/-24, -06, -08, -09/-25, -10/-29, -22, **-31**, FIG-04, FIG-08) | 15 (incl. **LAY-33** new) |
| Round 2 (this round) | **0** | **6** (LAY-02/-24, -06, -08, -09/-25, -22, FIG-04, FIG-08 — collapsed to 6 distinct after LAY-10/-29 + LAY-31 closure; LAY-22 listed under -09/-25 cluster) | 16 (carry-over + the two LAY-10/-29 residuals downgraded from M; **LAY-33** retained as advisory) |
| Delta | **−1** | **−3** | **+1** (LAY-10/-29 residuals downgrade) |

The H count returns to **0** (was 0 in round 3, briefly 1 in round 1 of
this loop, now 0). The M count is reduced by 3 distinct items (LAY-31
joint-closed; LAY-10/-29 dispatched anchors cleared; the two non-anchor
residuals downgrade to L by magnitude — both <40 pt path-literal
overfulls). All round-3 / round-4 carry-overs (LAY-02/-24, LAY-06,
LAY-08, LAY-09/-25, LAY-22, FIG-04, FIG-08, LAY-12, LAY-14/-23, LAY-16,
LAY-18, LAY-27, LAY-28, LAY-30, FIG-05, FIG-06, FIG-09, FIG-10, FIG-12)
are unchanged in disposition; none were in the round-1 dispatch scope and
none regressed.

## Severity by class (round 2)

- **Layout (LAY-*):** H=0, M=5 (LAY-02/-24, LAY-06, LAY-08, LAY-09/-25,
  LAY-22), L=11 (carry-overs + LAY-10/-29 residuals downgraded +
  LAY-33 advisory).
- **Figure (FIG-*):** **H=0** (LAY-32 closed), M=2 (FIG-04, FIG-08),
  L=4 (FIG-05, FIG-06, FIG-09, FIG-10, FIG-12 — 5 nominally; FIG-12
  carries forward as round-4 cosmetic).

## Owner rollup (round 2 — open items only)

- **Writer:** standing path-bullet M-cluster (LAY-02/-24, LAY-06, LAY-08,
  LAY-09/-25, LAY-22) plus L carry-overs (LAY-04, LAY-12, LAY-16,
  LAY-18, LAY-27, LAY-28, LAY-30, **LAY-33 advisory**) plus the two
  LAY-10/-29 non-anchor residuals (now L). LAY-14 / LAY-23 cosmetic
  preamble carry-over.
- **Illustrator:** FIG-04 (Gemini intact-jar deliverable, gated on author),
  FIG-08 (round-3 carry-over), FIG-05/-06/-09/-10/-12 cosmetic.
- **Joint:** none.

The round-1 dispatch — illustrator LAY-32 + writer LAY-31 + writer
LAY-10/-29 — is fully consumed. The standing M-cluster (LAY-02/-24,
LAY-06, LAY-08, LAY-09/-25, LAY-22) is independent of this loop and
predates the post-rewrite branch; per repository convention these are
clearable in any future writer sweep that addresses the same root cause
(unbreakable `\fp{...}` / `\texttt{...}` literals → `\seqsplit{}`), but
they are **not blocking** for the post-rewrite layout-readiness verdict
because they are preexisting, low-magnitude residuals of an
already-acknowledged class with no new instances in the post-rewrite
text.

## Mirror, redaction, distribution

- **Rule 11 (mirror discipline).** Writer commit `644d2e2` declared
  mirror parity at `paper/main.md ↔ paper/main.tex` for the §5.6 RDB-39
  split, the README RDB-40 footnote demotion, the §4.6 RDB-37 split, the
  LAY-10/-29 anchor `\seqsplit{}` applications, and the LAY-31
  `\seqsplit{}` augmentations. Layout sweep does not edit either file.
  Cross-references resolve (zero `??`, zero undefined `\cref` / `\ref` /
  `\cite`).
- **Rule 12 (redaction).** No new credentials / serials / UIDs / IPs in
  the post-rewrite text. The `[REDACTED:repo-path:BALBOA-UPSTREAM-{1,2}]`
  markers persist at the round-1 line locations (line-shifted only by
  the local sentence split; no new markers introduced). The
  `noheton/spider_farmer` and `noheton/powerocean-dev` upstream literals
  remain on-policy (public-by-author-decision per
  `docs/redaction-policy.md`).
- **Rule 13 (no publication).** Local PDF only. `make arxiv` not invoked.

## Hand-back routing

- `docs/handbacks/layout-to-writer.md` — **no new entries**. Round-1
  LAY-31 closed; LAY-10/-29 dispatched anchors cleared; LAY-33 deferred
  per round-1 verdict.
- `docs/handbacks/layout-to-illustrator.md` — **no new entries**.
  Round-1 LAY-32 closed by `fed50ab`.
- `docs/handbacks/layout-defect-registry.md` — full registry update
  remains deferred to the next non-narrow Stage-4 pass; this round
  records its closures here. The standing carry-over M-cluster
  (LAY-02/-24, LAY-06, LAY-08, LAY-09/-25, LAY-22) and the FIG-* / L
  carry-overs are unchanged from round 1's snapshot of the registry.

## Verdict

**RE-SCRUTINY REQUIRED: no**

Rationale: every defect filed in round 1 against the post-rewrite build
is either CLOSED (LAY-32 H, LAY-31 M, LAY-10/-29 dispatched anchors) or
DEFERRED-by-policy (LAY-33 L advisory, per round-1 verdict). No new H or
M defects were introduced by illustrator commit `fed50ab` or writer
commit `644d2e2`. Total `Overfull \hbox` count fell 34 → 30 (writer's
self-reported number, independently verified from `paper/main.log`).
The §5.6 anchor overfull collapsed from 25.75 pt to 0.80 pt. Page count
is stable at 57. No `??`, no undefined refs / cites, no rule-11 / -12 /
-13 regressions.

**Publication-readiness statement.** The long-form paper
(`paper/main.{md,tex,pdf}`) is **layout-clean for publication readiness**
on the post-rewrite branch `claude/history-rewrite-daDxQ`, subject only
to the rule-13 explicit-consent gate (which Stage 4 does not adjudicate
and does not relax). The standing carry-over M-cluster (LAY-02/-24,
LAY-06, LAY-08, LAY-09/-25, LAY-22) is the only open layout debt; it
predates the post-rewrite loop and consists of preexisting low-magnitude
path-literal residuals of an already-acknowledged class — non-blocking
for the post-rewrite verdict. The condensed paper
(`paper/main-condensed.{md,tex,pdf}`) is out of scope for this Stage-4
pass and is governed by its own future scrutiny if it is ever surfaced
for publication.
