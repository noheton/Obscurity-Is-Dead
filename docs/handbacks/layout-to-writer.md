# Layout → Writer Hand-back

> Stage 4 (Layout Scrutinizer) — round 3, 2026-05-03 (Claude Opus 4.7).
> Branch: `claude/review-open-issues-PfNx9`. Commit under inspection:
> `37ded1f`. PDF: 54 pages, SHA-256
> `4a85be8dd1b56221aa94920da184f9014babb6b45be8dd6098c47677d745de15`.
> 33 overfulls (was 34); zero H-severity entries open.

## Closed this round

### LAY-26 — RESOLVED. Confirmed at `paper/main.tex:2582–2585`. The `\seqsplit{...}` wrap at the `(copy\&paste,~web)/` boundary, plus the refactor of the longer sibling into "the paper-meta-process transcript ... under <path>", eliminated the 168.71pt overflow. No overfull anchored on lines 2570–2620. The pattern matches the §10 enumeration `\seqsplit{}` precedent at `:2834`. Excellent fix.

## Open M-severity entries (writer-owned)

### LAY-29 — §10 ninth-practice / closing-paragraph path-bullet cluster (NEW, top residual)
- Page: ~50–52 (within §10 + §10.AI-disclosure tail)
- Source: `main.tex:2841–2849` (**70.91pt**); `:2854–2859` (32.31pt); `:2877–2882` (16.08pt). Mirrored at `main.md:~733–760` (line range to confirm during edit).
- Observed: the `\fp{experiments/paper-meta-process/raw_conversations (copy&paste, web)/}` literal at `:2849` is the exact same unbreakable shape as the closed LAY-26 monster; siblings carry the same wrap pressure.
- Required action: apply the LAY-26 fix pattern — wrap each long `\fp{...}` or `\texttt{...}` path in `\seqsplit{}` segments split at `(copy\&paste,~web)/` boundaries, or rewrite the parenthetical out of the path. The `\fp{}` macro can be retargeted to expand to `\seqsplit{\texttt{...}}` if a global change is preferred over per-site edits.
- Severity: M

### LAY-09 / LAY-25 — §5.2 + §6.6/§6.7 path-bullet cluster (line-shifted)
- Page: mid-doc (§6 region)
- Source: 7 overfulls in `main.tex:1077–1162` (range 5.21–70.84pt). Largest at `:1077–1087` (70.84pt) and `:1092–1095` (69.91pt).
- Observed: paths such as `\fp{experiments/paper-meta-process/raw_conversations (copy&paste, web)/}`, `\fp{ACTION_W_CFG_BACKUP_REVERSE_SOC}`, and HA-entity `\fp{}` lists (button/number entities) drive the bullets past the right margin.
- Required action: same `\seqsplit{}` / `\path{}` sweep. Consider redefining `\fp{}` to wrap its argument in `\seqsplit{\texttt{...}}` for a one-line global fix; this would close LAY-09, LAY-25, LAY-29, and parts of LAY-22 in a single edit.
- Severity: M

### LAY-22 — trailing-matter / appendix path-list residuals
- Source: `main.tex:2677–2681` (37.70pt); `:2854–2859` (32.31pt — also tagged under LAY-29); `:2223–2232` (25.74pt, trust-laundering bullet with `[REDACTED:repo-path:BALBOA-UPSTREAM-{1,2}]`).
- Observed: the redaction-tag bullet is wrapped in `\texttt{}` but **not** in `\seqsplit{}`.
- Required action: wrap the two `[REDACTED:repo-path:BALBOA-UPSTREAM-{1,2}]` `\texttt{}` calls at `:2228–2229` in `\seqsplit{}`, matching the precedent set for the credential redaction tags at `main.tex:777–778`.
- Severity: M

### LAY-02 / LAY-24 — §1.6 contributions enumerate
- Source: `main.tex:479–488` (32.16pt + 11.72pt).
- Required action: rebreak the two `\texttt{docs/methodology.md}` and `\texttt{experiments/spider-farmer/}` paths with `\seqsplit{}` or wording.
- Severity: M

### LAY-08 — §4.4 writeable-entity comma-list
- Source: `main.tex:625–627` (12.07pt) + `:657–660` (66.39pt).
- Required action: break the writeable-entity comma list across two paragraphs or convert to a bullet list with `\seqsplit{}` on each entity name.
- Severity: M

### LAY-10 — §10 path-bullet cluster (improved, not closed)
- Source: `main.tex:2557–2614` (50.18pt + 3.58pt + 35.69pt).
- Required action: same `\seqsplit{}` sweep applies; some entries are already in the LAY-26 patched paragraph but downstream items at `:2557–2566` and `:2592–2614` still need attention.
- Severity: M

### LAY-20 / LAY-21 — §6.4 wrap pressure
- Source: `main.tex:1464–1480` cluster (30.26pt + 52.64pt + 23.06pt).
- Severity: M

## Open L-severity entries (deferrable)

- **LAY-04** — 0.18pt at `:1432–1447`. Effectively closable; defer.
- **LAY-23** — preamble OT1/cmtt → OT1/lmtt cosmetic; pre-existing.
- **LAY-27** — Spider Farmer tabularx intra-cell at `:753` (11.03/9.38/15.04pt). Cosmetic.
- **LAY-28** — §6.4 underfull cluster. Cosmetic rivers.
- **LAY-30 (new)** — bibliography underfull cluster gained 6 entries from the new `noheton2026powerocean*` `@misc` records. Auto-generated. Optional `\urlstyle{tt}` / truncation.

## Recommended bundling

A single writer pass that redefines `\fp{}` from `\texttt{#1}` to
`\seqsplit{\texttt{#1}}` (or applies `\seqsplit{}` at every long-path
site) would close LAY-09, LAY-22, LAY-25, LAY-29, and parts of LAY-10 in
one edit — five M-severity entries with one global change. The fix is
the same family that closed LAY-26 and is precedent-supported by the
existing redaction-tag `\seqsplit{}` use at `main.tex:777–778`.

## Out of scope for the writer

LAY-12 (Gemini deliverable), FIG-04, FIG-09, FIG-10, FIG-11 are
illustrator-owned; see `layout-to-illustrator.md`.

## Verdict

No H-severity items remain. The pipeline is non-blocked on layout. The
M-severity path-bullet cluster is the dominant residual and is highly
amenable to a single bundled writer pass.
