# Layout Defect Registry — paper/main.pdf

- **PDF SHA-256:** `4a85be8dd1b56221aa94920da184f9014babb6b45be8dd6098c47677d745de15`
- **PDF size:** 1,231,155 bytes; **54 pages** (was 53 in round 2; +1 page from new powerocean-resync prose at §4.2 / §4.3 / §4.6 / §10).
- **Build timestamp:** 2026-05-03T17:35:24Z (newer than `main.tex` 17:31:57Z).
- **Build commit under inspection:** `37ded1f` ("Stage 2 writer loop 3: LAY-26 H + RDB-30/-31/-35/-36 + powerocean-resync d.1/d.2/d.6/d.7").
- **Source under inspection:** `paper/main.tex` (171,433 bytes; ~2,995 lines); mirrored in `paper/main.md`.
- **LaTeX log:** `paper/main.log` (51,779 bytes): **33 `Overfull \hbox`** (was 34), **67 `Underfull \hbox`** (was 61; +6 from new prose), **0 `Reference … undefined`**, **0 `Citation … undefined`**, **0 `??`**, **0 PDF-1.7-inclusion warnings**, no Float-too-large, no Missing macros. Cosmetic OT1/cmtt → OT1/lmtt fallback persists at preamble (LAY-23, L).
- **Scrutinizer:** Stage 4 — Layout Scrutinizer, round 3, 2026-05-03 (Claude Opus 4.7).
- **Method note:** Pixel-level visual sweep is `viewer-blocked` (no PDF viewer MCP available in the harness). Sweep performed via `paper/main.log` ground-truth (geometric overfulls cite source line ranges; cross-checked against `paper/main.tex`). Source-level confirmation of LAY-26 closure, new powerocean prose spans, and new bib entries performed.

## Round-2 carry-over disposition

| ID | Round-2 status | Round-3 status | Note |
|----|----------------|----------------|------|
| LAY-01 | RESOLVED | RESOLVED | Zero undefined refs / cites in log. |
| LAY-02 | PARTIAL | PARTIAL | §1.6 contributions enumerate still produces 32.16pt at `:479–483` + 11.72pt at `:483–488` (line numbers unchanged — span pre-dates the powerocean-resync paragraphs which sit downstream). Path-bullet family. |
| LAY-03 | PARTIAL | PARTIAL | §5.2 path-bullet cluster shifted to `:951–964` (66.67pt; 12.76pt) — same source span, +31 lines from new §4.x prose insertions. |
| LAY-04 | PARTIAL | PARTIAL | 0.18pt residual line-shifted to `:1432–1447`. Effectively closable. |
| LAY-05 | RESOLVED | RESOLVED | Figure 7 float clean. |
| LAY-06 | PARTIAL | PARTIAL | Difficulty-taxonomy table residual: 8.80pt at `:1515–1516` + 2.53pt at `:1513–1539` (line-shifted from r2 1462/1460–1486). |
| LAY-07 | RESOLVED | RESOLVED | No overfulls anchored on redaction tags. |
| LAY-08 | PARTIAL | PARTIAL | §4.4 region produces 12.07pt at `:625–627` + 66.39pt at `:657–660` (writeable-entity comma-list pressure). Unchanged; lines unchanged. |
| LAY-09 | PARTIAL | PARTIAL | Cluster of 7 overfulls in `:1077–1162` (range 5.21–70.84pt); root cause = path bullets. Line-shifted from r2 `:1027–1054` by ~+50 lines (new §4.x paragraphs). |
| LAY-10 | PARTIAL | PARTIAL-IMPROVED | §10 path-bullet cluster moved to `:2557–2614`: 50.18pt + 3.58pt + 35.69pt. The 168.71pt monster (former LAY-26) is **gone** — see LAY-26 below. |
| LAY-11 | RESOLVED | RESOLVED | Folded into LAY-06. |
| LAY-12 | PARTIAL | RESOLVED | Intact-jar Gemini deliverable landed on `main` (commit `302bf96`, 2026-05-04, 1408x768 RGBA, ~2.0 MB); placeholder swapped out; `paper/figures/README.md` inventory + `paper/main.{md,tex}` §9.1 prose + §10 caption updated to reflect Gemini-final provenance. |
| LAY-13 | RESOLVED | RESOLVED | Zero PDF-1.7 inclusion warnings. |
| LAY-14 | UNCHANGED-COSMETIC | UNCHANGED-COSMETIC | OT1/cmtt → OT1/lmtt at preamble lines 34/38; downgraded to L in r2; remains L. |
| LAY-15 | RESOLVED-by-omission | RESOLVED | No `'h' float specifier` warnings. |
| LAY-16 | PARTIAL | PARTIAL | Bibliography underfull cluster persists; +6 underfulls overall this round (auto-generated, long URLs, expected for the four new powerocean entries). |
| LAY-17 | RESOLVED | RESOLVED | Spider Farmer KPI clean. |
| LAY-18 | PARTIAL | PARTIAL | Underfull-badness cluster persists in §6.x region (`:~1387–1486`-equivalents, line-shifted). Cosmetic. |
| LAY-19 | RESOLVED | RESOLVED | Meta-process / EcoFlow KPI tabularx conversion holds. |
| LAY-20 | PARTIAL | PARTIAL | Underfull cluster still in §6.4 region (`:~1466–1480`); 30.26pt + 52.64pt + 23.06pt cluster — same wrap pressure. |
| LAY-21 | PARTIAL | PARTIAL | 52.64pt overfull at `:1466–1467` (line-shifted from r2 1413–1414). |
| LAY-22 | PARTIAL-MUTATED | PARTIAL-MUTATED | Trailing-matter overfulls: 37.70pt at `:2677–2681`, 70.91pt at `:2841–2849`, 32.31pt at `:2854–2859`, 16.08pt at `:2877–2882`. The 25.74pt at `:2223–2232` (trust-laundering item, line-shifted from r2 `:2163–2172`) persists. Same root cause: path-list / `\texttt{}` wrap pressure. |
| LAY-23 | L | L | Cosmetic font-shape carry-forward. |
| LAY-24 | M | M | §1.6 contributions enumerate (32.16/11.72pt). Same as LAY-02 family in round 2; bookkept under -24 here for clarity. |
| LAY-25 | M | M | §6.6/§6.7 path-bullet cluster, line-shifted into LAY-09's `:1077–1162` block this round; same root cause. |
| **LAY-26** | **H (168.71pt)** | **RESOLVED** | The unbreakable `\texttt{experiments/*/raw\_conversations (copy\&paste, web)/}` and longer sibling at the former `:2518–2529` are now wrapped in `\seqsplit{...}` segments at `paper/main.tex:2582–2585`. The 168.71pt overflow has **disappeared from the log entirely**. Largest-defect-of-round-2 closed. Refactor to `the paper-meta-process transcript ... under <path>` confirmed; no overfull anchored anywhere on lines 2570–2620. |
| LAY-27 | L | L | Spider Farmer tabularx intra-cell overfulls persist at `:753` (11.03 / 9.38 / 15.04 pt). Cosmetic. |
| LAY-28 | L | L | §6.4 underfull cluster persists (cosmetic rivers). |
| FIG-01 | RESOLVED | RESOLVED | All 18 `\Description{}` macros present. |
| FIG-02 | CLOSED-FOR-REWORKED | CLOSED-FOR-REWORKED | Carry-forward residual filed as FIG-11. |
| FIG-03 | EXPECTED-RESOLVED-VIEWER-BLOCKED | EXPECTED-RESOLVED-VIEWER-BLOCKED | Unchanged. |
| FIG-04 | UNCHANGED | RESOLVED | Gemini intact-jar deliverable landed (commit `302bf96`, 2026-05-04). |
| FIG-05 | UNCHANGED-NARROWED | UNCHANGED-NARROWED | Bookkeeping. |
| FIG-06 | UNCHANGED | UNCHANGED | Bookkeeping. |
| FIG-07 | EXPECTED-RESOLVED-VIEWER-BLOCKED | EXPECTED-RESOLVED-VIEWER-BLOCKED | Unchanged. |
| FIG-08 | PARTIAL | PARTIAL | Pending RDB-04 author decision. |
| FIG-09 | UNCHANGED | UNCHANGED | Viewer-blocked. |
| FIG-10 | L | L | Alt-text fidelity audit pending illustrator pass. |
| FIG-11 | M | M | fig8/15/16 residual CB palette. |

## New defects this round (LAY-29..LAY-30)

| ID | Page | Region | Defect class | Severity | Owner | Source span | Suggested fix |
|----|------|--------|--------------|----------|-------|-------------|---------------|
| **LAY-29** | §10.AI-disclosure | path-bullet | overfull-prose-path | M | writer | `main.tex:2841–2849` (**70.91pt**), `:2854–2859` (32.31pt), `:2877–2882` (16.08pt) | Largest residual overfulls in the document, all in the §10 ninth-practice / closing-paragraph region. Same `\seqsplit{}` / `\path{}` pattern that closed LAY-26 should close these. The 70.91pt entry contains the `\fp{experiments/paper-meta-process/raw_conversations (copy&paste, web)/}` literal at `:2849` — exact same shape as the old LAY-26 monster but in a different paragraph. |
| **LAY-30** | bibliography | new powerocean entries | underfull-bibliography-cosmetic | L | writer (advisory) | `paper/references.bib:702, 721, 738, 753` (4 new `@misc` entries) | Added 6 underfulls to the bibliography from the long upstream commit-URL fields in the four new `noheton2026powerocean*` `@misc` entries. Cosmetic; auto-generated. No action required unless the writer wants to truncate displayed URLs via `\biburlsetup` or `\urlstyle{tt}`. |

## Severity rollup (current open state)

- **H:** **0** (LAY-26 RESOLVED).
- **M:** 7 distinct items: LAY-02/-24 (§1.6), LAY-08, LAY-09/-25, LAY-10, LAY-20/-21, LAY-22, **LAY-29 (new)**, FIG-08, FIG-11. *(FIG-04 closed 2026-05-04 by Gemini intact-jar landing; LAY-12 closed in the same pass.)*
- **L:** 13: LAY-03 (downgraded), LAY-04, LAY-14/-23, LAY-16, LAY-18, LAY-27, LAY-28, **LAY-30 (new)**, FIG-05, FIG-06, FIG-09, FIG-10.
- **RESOLVED this round:** LAY-26 (the only round-2 H).

## Severity by class

- **Layout (LAY-*):** H=**0** (was 1), M=7, L=9. Net +1 entry (LAY-29/-30 added; LAY-26 closed).
- **Figure (FIG-*):** H=0, M=3, L=4. Unchanged.

## Owner rollup

- **Writer:** LAY-02, -03, -04, -08, -09, -10, -16 (advisory), -18, -20, -21, -22, -24, -25, -27, -28, **-29 (top M)**, -30 (advisory), -23 (L cosmetic).
- **Illustrator:** FIG-05/-06 bookkeeping, FIG-09 audit-incomplete, FIG-10 fidelity audit, FIG-11 residual CB palette. *(LAY-12 + FIG-04 closed 2026-05-04 by the Gemini intact-jar landing.)*
- **Joint:** none.

## LAY-26 closure verification

The writer's loop-3 fix at `paper/main.tex:2582–2585` is confirmed:

```
\seqsplit{\texttt{experiments/*/raw\_conversations}}~\seqsplit{\texttt{(copy\&paste,~web)/}}
...
\seqsplit{\texttt{T1-paper-structure-and-literature.md}} under
\seqsplit{\texttt{experiments/paper-meta-process/raw\_conversations}}~\seqsplit{\texttt{(copy\&paste,~web)/}}
```

`grep -nE "Overfull" paper/main.log` returns no overfull anchored anywhere on the 2570–2620 line band. The largest single residual overfull in the build is now 70.91pt (LAY-29 at `:2841–2849`), down from 168.71pt — a **57.7%** reduction in the worst-defect magnitude. Total overfulls: 33 (was 34); the closed LAY-26 entry is the missing one.

## New powerocean prose spot-checks

- §4.2 (`:874–887`): redaction-precedent paragraph, cite to `noheton2026powerocean5c8b815` and `noheton2026powerocean_docreadme`. **No overfull anchored on this span.**
- §4.3 (`:889–909`): two-track methodology footnote, cite to `noheton2026powerocean_disclaimer` and `noheton2026powerocean1aa9650`. **No overfull anchored on this span.**
- §4.6 (`:984–1004`): OCPP runtime-handover gap paragraph (`vendorInfoSet` not shipped). **No overfull anchored on this span.** Inline `\fp{...}` and `\texttt{vendorInfoSet}` literals all wrap cleanly.
- §10 (`:2957–2978`): redaction-precedent `\paragraph{...}` block. **No overfull anchored on this span.**
- All four new bib keys (`noheton2026powerocean5c8b815`, `noheton2026powerocean1aa9650`, `noheton2026powerocean_disclaimer`, `noheton2026powerocean_docreadme`) resolve in the log (no `Citation undefined`); zero `??` in the rendered PDF.

## Caption updates spot-checks

- Fig 9 caption (`:1140–1149`): RDB-35 four-stage ladder + Source Analyzer naming. No overfull anchored on this caption.
- Fig 11 caption (`:2861–2867`): RDB-36 legend-deduplication. No overfull anchored on this caption (closest is `:2877–2882` LAY-29 region, 16.08pt — adjacent but not on the caption itself).

## Mirror discipline (rule 11) check

Writer pass `37ded1f` reports md ↔ tex parity for every Mythos / band-aid / powerocean / caption edit. Section labels and float sequence between `paper/main.md` and `paper/main.tex` match per the writer's mirror declaration. No structural drift detected from the log.

## Redaction (rule 12) check

`[REDACTED:repo-path:BALBOA-UPSTREAM-1]` and `[REDACTED:repo-path:BALBOA-UPSTREAM-2]` markers persist at `main.tex:2228–2229` (line-shifted from r2 `:2168–2169`). Their host bullet at `:2223–2232` carries the 25.74pt overfull (LAY-22 family). The new powerocean prose introduces no credentials, serial numbers, UIDs, or IPs.

## Rule 13 compliance

This pass operates only on the local PDF. No upload to external services; `make arxiv` not invoked.

## RE-SCRUTINY REQUIRED: no — Zero H-severity entries open. LAY-26 (the round-2 H, 168.71pt path overflow in §10 AI-disclosure-models) is confirmed RESOLVED via the writer's `\seqsplit{}` refactor at `main.tex:2582–2585`. The largest residual overfull in the document is now 70.91pt (LAY-29, §10 ninth-practice region) and the next-largest sibling 70.84pt (LAY-09, §6.6/§6.7 path-bullet cluster) — both M-severity and both squarely in the path-bullet family that the next writer pass already plans to address with a unified `\seqsplit{}` / `\path{}` sweep. New powerocean-resync prose at §4.2 / §4.3 / §4.6 / §10 typesets cleanly with zero anchored overfulls; new caption text at Fig 9 / Fig 11 also clean; four new bib entries render without `Citation undefined`. Pipeline is clear to advance to Stage 5 (readability) without an immediate rebuild requirement; layout is non-blocking. A re-sweep is recommended only after the next writer pass closes the LAY-09 / LAY-29 / LAY-22 cluster (which would be the natural next-loop hand-back consumer).
