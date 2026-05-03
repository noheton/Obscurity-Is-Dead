# Layout Scrutiny — 2026-05-03 — round 3 (Claude Opus 4.7)

> Stage 4 against `paper/main.pdf` rebuilt from commit `37ded1f` on
> branch `claude/review-open-issues-PfNx9`.

## Build under inspection

- **PDF SHA-256:** `4a85be8dd1b56221aa94920da184f9014babb6b45be8dd6098c47677d745de15`
- **PDF size / pages:** 1,231,155 bytes / 54 pages (was 53; +1 page from new powerocean-resync prose at §4.2 / §4.3 / §4.6 / §10).
- **PDF mtime:** 2026-05-03T17:35:24Z (newer than `main.tex` 17:31:57Z — fresh build).
- **Commit:** `37ded1f` ("Stage 2 writer loop 3: LAY-26 H + RDB-30/-31/-35/-36 + powerocean-resync d.1/d.2/d.6/d.7").

## Log summary

- **Overfull \hbox:** 33 (was 34; LAY-26 closed). Largest residual: 70.91pt at `:2841–2849` (LAY-29, new).
- **Underfull \hbox:** 67 (was 61; +6 from new bibliography entries — LAY-30, L).
- **Reference … undefined:** 0.
- **Citation … undefined:** 0.
- **`??` in rendered PDF:** 0.
- **PDF-1.7 inclusion warnings:** 0.
- **Float too large:** 0.
- **Other:** preamble OT1/cmtt → OT1/lmtt cosmetic substitution persists (LAY-23, L).

## Executive summary

1. **LAY-26 (the only round-2 H) is RESOLVED.** The writer's
   `\seqsplit{}` refactor at `paper/main.tex:2582–2585` eliminated the
   168.71pt path-overflow in §10 AI-disclosure-models. No overfull is
   now anchored anywhere on the 2570–2620 line band. The
   largest-defect-of-round-2 is closed; the worst-defect magnitude
   dropped from 168.71pt to 70.91pt (a 57.7% reduction).
2. **Zero H-severity entries open.** Eight M-severity entries remain,
   all in the well-known path-bullet family (LAY-02, LAY-08, LAY-09,
   LAY-10, LAY-20/-21, LAY-22, LAY-24, LAY-25, **LAY-29 new**, plus the
   illustrator-owned FIG-04, FIG-08, FIG-11). Thirteen L-severity
   entries (cosmetic / advisory).
3. **New powerocean-resync prose typesets cleanly.** All four new
   paragraphs / footnote (§4.2 `:874–887`; §4.3 `:889–909`; §4.6
   `:984–1004`; §10 `:2957–2978`) produce zero anchored overfulls.
   None contradicts §4-§6 mirror discipline.
4. **Four new `@misc` bib entries render correctly.**
   `noheton2026powerocean5c8b815`, `noheton2026powerocean1aa9650`,
   `noheton2026powerocean_disclaimer`,
   `noheton2026powerocean_docreadme` all resolve (zero `Citation
   undefined`). They contribute the 6 new bibliography underfulls
   (LAY-30, L, cosmetic).
5. **Caption updates at Fig 9 (RDB-35) and Fig 11 (RDB-36)** typeset
   without anchored overfulls.
6. **One new defect filed: LAY-29 (M).** `\fp{experiments/paper-meta-
   process/raw_conversations (copy&paste, web)/}` literal at
   `main.tex:2849` is the exact same unbreakable shape as the closed
   LAY-26 monster, but in a different paragraph — 70.91pt overflow.
   Closeable by the same `\seqsplit{}` pattern.
7. **Recommendation for next writer pass.** Redefining `\fp{}` from
   `\texttt{#1}` to `\seqsplit{\texttt{#1}}` (or applying `\seqsplit{}`
   site-by-site) would close LAY-09, LAY-22, LAY-25, LAY-29, and parts
   of LAY-10 in a single global edit — five M-severity entries with
   one change.

## Hand-back routing

- `docs/handbacks/layout-to-writer.md` — top entry: LAY-29 (70.91pt,
  §10 ninth-practice path-bullet) plus the LAY-09/-22/-25 family.
- `docs/handbacks/layout-to-illustrator.md` — no new entries; FIG-04,
  FIG-09, FIG-10, FIG-11 carry forward unchanged.
- `docs/handbacks/layout-defect-registry.md` — full updated registry.

## Mirror, redaction, distribution

- **Rule 11:** writer reports md ↔ tex parity for every loop-3 edit;
  no structural drift in the log; section labels and float sequence
  intact.
- **Rule 12:** `[REDACTED:repo-path:BALBOA-UPSTREAM-{1,2}]` markers
  persist at `:2228–2229` (line-shifted from r2). No new credentials,
  serial numbers, UIDs, or IPs introduced by the powerocean prose.
- **Rule 13:** local PDF only; `make arxiv` not invoked.

## Verdict

**RE-SCRUTINY REQUIRED: no.**

Zero H-severity defects remain. The path-bullet M cluster is non-
blocking and is the natural target of the next writer pass; another
layout sweep is justified only after that pass lands.
