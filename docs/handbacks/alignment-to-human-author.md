# Alignment hand-back to human author

This file records `ALN-*` defects routed to the human author when
the resolution is a policy decision (rule-conflict surfacing, rule
14 distribution-consent gating, rule 13 redaction-scope decisions),
or when the upstream brief contained a factual error worth
flagging without requiring a code / prose change.

Each round appends a block.

---

## Stage 6 — Aligner, round 2, 2026-05-04

**Source registry block:** `docs/handbacks/alignment-defect-registry.md`,
*Stage 6 — Aligner, round 2, 2026-05-04*.

### Notes for the human author (round 2)

1. **Round-1 closure verification — clean baseline.** All thirteen
   round-1 ALN entries (ALN-01..ALN-13) are confirmed closed by the
   round-1 commit `668fa8d` plus subsequent commits. The
   round-1 H-severity defect (ALN-08) and the M-severity rule-number
   sites (ALN-06, ALN-09..ALN-12) are all closed. ALN-13 (CCI
   canonicality) is closed by the policy decision recorded in
   `CLAUDE.md` line 5 — `CLAUDE_CODE_INSTRUCTIONS.md`,
   `.instructions.md`, and `copilot-instructions.md` are now thin
   stub pointers at `CLAUDE.md`.

2. **ALN-23 — README cluster-range non-defect (informational).**
   The Q1 + Q2 commit-message brief and the round-1 logbook entry
   (`docs/logbook.md` line 2590) both stated that "the README says
   clusters A–O at three sites" and asked the Aligner to reconcile
   this against the paper's current `A–Q`. Round-2 audit — full
   `grep` and `git log -S` against `README.md` — finds **zero
   cluster-range references in the README, ever**. The brief
   appears to have inferred the README state from a prior artifact
   rather than from a direct read.

   **No action required**: there is no defect to fix in `README.md`.
   This entry is filed for two reasons: (a) so the next round's
   closure-tracking has a clean record that the audit was performed,
   and (b) so a future writer / orchestrator pass that re-uses the
   "README ↔ paper cluster-range parity" framing knows the brief
   was based on a misobservation. Rule 1 honesty: the registry
   records the fact rather than papering over the upstream error.

3. **No publication-consent surfaces touched.** Rule 14 gating is
   not at issue this round. The condensed paper carries the rule-14
   distribution-consent statement at `paper/main-condensed.md:9` and
   `paper/main-condensed.tex:76` — both round-1-corrected and
   round-2-clean. The ten round-2 defects routed to the writer are
   all pre-publication consistency fixes; none affect the
   distribution gate.

4. **ALN-18 (H) — flag for awareness.** The round-2 H-severity
   defect is a *self-containment / disclosure* fault in the
   condensed paper §4 dual-use citation set: it invokes
   `[edge-case]`-status `L-VD-1` and `L-VD-5` without the long-form
   footnote disclosure that the `[edge-case]` ladder rung licenses.
   The fix is a writer-side carve-out import (see
   `docs/handbacks/alignment-to-writer.md` round 2 ALN-18), not a
   policy decision. Surfacing here only because the dual-use
   asymmetry argument is the most legally- and reputationally-
   sensitive prose in the condensed paper — the human author may
   want to review the writer's carve-out wording before round 3.

### No human-author action required this round.

The round-2 verdict (`RE-ALIGNMENT REQUIRED: yes`) routes back to
the writer (stage 2), not to the human author. Once the writer
closes ALN-14..ALN-22 and ALN-24, the round-3 Aligner sweep is
the next step.
