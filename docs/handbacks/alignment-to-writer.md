# Alignment hand-back to writer (stage 2)

This file records `ALN-*` defects routed to the scientific writer
agent (stage 2, `docs/prompts/scientific-writer-prompt.md`). Each
round appends a block. The writer is responsible for closing the
defects in a follow-up writer pass against the same branch; the
Aligner records closure on the next round.

---

## Stage 6 — Aligner, round 2, 2026-05-04

**Source registry block:** `docs/handbacks/alignment-defect-registry.md`,
*Stage 6 — Aligner, round 2, 2026-05-04*.

**Defects routed to writer.** Ten entries — one H, seven M, two L —
all of which are pure-text fixes inside the four paper-source files
plus `paper/figures/README.md`. None require new figures, new
research, or new sources. Suggested closure: a single writer pass
on branch `claude/prepare-for-publish-fERq5` covering all ten,
followed by a round-3 Aligner sweep.

### High-severity (H)

- **ALN-18 (H)** — Condensed paper §4 dual-use carve-out import.
  - Files: `paper/main-condensed.md:76`, `paper/main-condensed.tex:357–366`.
  - Fault: invokes `L-VD-1` (status `[lit-retrieved]+[edge-case]`)
    and `L-VD-5` (same) as load-bearing dual-use asymmetry
    evidence without importing the long-form footnote
    disclosure (`paper/main.md:63`, `[^exec-edge]`) that licenses
    the otherwise-blocked invocation. Violates rule 17
    (self-containment) and rule 18 (invocation level below the
    `[ai-confirmed]` ladder floor for inline citation, without
    disclosure).
  - Fix: import `[^exec-edge]` (or an equivalent inline aside) into
    the condensed paper §4 immediately after the `(L-VD-5)`
    parenthetical. Suggested wording (parallel to the long-form
    footnote): *"L-VD-1 and L-VD-5 are recorded at `[edge-case]`
    verification status in `docs/sources.md` of the long-form
    companion (load-bearing, first-of-its-kind, awaiting human
    `[lit-read]`); they are invoked here under the verification
    ladder's edge-case carve-out (CLAUDE.md, 2026-05-02
    extension)."*  Rule 12: apply symmetrically to md and tex.

### Medium-severity (M)

- **ALN-14 (M)** — Long-form §5.7 *Estimated manual baseline*
  70-entry temporal-anchor unflagged.
  - Files: `paper/main.md:388`, `paper/main.tex:1311–1313`.
  - Fix: add a temporal-anchor qualifier (e.g. *"a paper of this
    2026-05-01-era scope"* or *"as of the 2026-05-01 manuscript
    snapshot — see the 2026-05-04 row below"*). Mirror md ↔ tex.

- **ALN-15 (M)** — Long-form §5.5 democratisation 70-entry / 17 h
  inline temporal inconsistency.
  - Files: `paper/main.md:766`, `paper/main.tex:3247–3252`.
  - Fix: rewrite to make the 17 h figure cumulative-meta-process
    (matches §5.7) and the literature register a temporally-spanned
    figure (70 → 144 between 2026-05-01 and 2026-05-04 along the
    verification-status ladder). Suggested wording in the registry
    block.

- **ALN-17 (M)** — Condensed §3 *rule-11 mirror parity check* →
  *rule-12*.
  - Files: `paper/main-condensed.md:60`, `paper/main-condensed.tex:251`.
  - Fix: literal substitution.

- **ALN-19 (M)** — Figures README rule 14 → rule 15 (~10 sites)
  and CCI pointer retarget.
  - File: `paper/figures/README.md:4, 12, 16, 30, 68, 119, 124,
    131, 143, 187` (Rule 14 / Rule-14 / rule 14 → 15) plus line
    5 (`CLAUDE_CODE_INSTRUCTIONS.md` → `CLAUDE.md`).
  - Fix: global rule-14 → rule-15 substitution in the
    figure-data-rule context; pointer retarget on line 5.

- **ALN-20 (M)** — Long-form md ↔ tex rule-14 → rule-15 (four
  sites) plus historical-row "Rule 11 compliance" framing.
  - Files: `paper/main.md:74, 378, 384`, `paper/main.tex:376,
    1297, 1303, 1852`.
  - Fix: rule-14 → rule-15 at the four prose / comment sites; for
    `paper/main.md:378` / `paper/main.tex:1297` historical row,
    keep the label or annotate parenthetically (rule 12 in current
    `CLAUDE.md`).

- **ALN-21 (M)** — Long-form front-matter rule-4 pointer
  `CLAUDE_CODE_INSTRUCTIONS.md` → `CLAUDE.md`.
  - Files: `paper/main.md:37`, `paper/main.tex:233–234`.
  - Fix: pointer retarget. Rule number (4) is correct as-is.

- **ALN-22 (M)** — Long-form §5.2 / §5.3
  `CLAUDE_CODE_INSTRUCTIONS.md` references.
  - Files: `paper/main.md:331, 341`, `paper/main.tex:1118–1120,
    1148`.
  - Fix at §5.2: demote the three stubs in the listing to
    "historical stub pointers `.instructions.md` /
    `copilot-instructions.md` / `CLAUDE_CODE_INSTRUCTIONS.md`"
    so the canonical `CLAUDE.md` is named first and the stubs
    are flagged as such. Fix at §5.3 step 1: replace
    `CLAUDE_CODE_INSTRUCTIONS.md` with `CLAUDE.md` (the agent
    actually reads the canonical file; round-1 made CCI a stub).

### Low-severity (L)

- **ALN-16 (L)** — Condensed §2 *seventy-entry literature
  register* parallel to ALN-15.
  - Files: `paper/main-condensed.md:50`, `paper/main-condensed.tex:218–219`.
  - Fix: parallel to ALN-15 close — *"seventy-entry"* →
    *"144-entry as of 2026-05-04"* or temporally-qualified
    wording. Required under rule 12 (mirror) once ALN-15 is
    closed in the long-form pair.

- **ALN-24 (L)** — Condensed §3 ladder description omits
  `[unverified-external]` rung.
  - Files: `paper/main-condensed.md:62`, `paper/main-condensed.tex:298–303`.
  - Fix: prefix the rung list with `[unverified-external]` →`,
    or annotate as "the four invocation-eligible rungs of the
    ladder defined in `CLAUDE.md`".

### Suggested closure ordering

1. ALN-19 (figures README — single-file global edit).
2. ALN-20 (long-form md ↔ tex rule-14 → rule-15 + historical-row).
3. ALN-21 + ALN-22 (CCI pointer retargets in long-form, ~5 sites).
4. ALN-17 (condensed rule-11 → rule-12, single substitution).
5. ALN-14 + ALN-15 + ALN-16 (temporal-anchor rewrite, three sites
   coordinated under rule 12 mirror).
6. ALN-18 (condensed dual-use carve-out import — most prose
   work; do last after the easier sites are closed).
7. ALN-24 (condensed ladder-rung addition, single-line edit).

After the writer pass, request orchestrator dispatch of round-3
Aligner sweep.
