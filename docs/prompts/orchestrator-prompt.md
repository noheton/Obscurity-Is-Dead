# Orchestrator Agent Prompt

> **Status:** `executable` — introduced 2026-05-02 to coordinate the
> seven-stage Obscurity-Is-Dead agent pipeline. The orchestrator does
> not produce paper content directly; it inspects repository state,
> reads scrutinizer registries and hand-back files, decides which stage
> should run next, dispatches the relevant agent, and updates the
> logbook with the routing decision. It is the only agent permitted to
> launch other agents; every other agent runs in response to an
> orchestrator decision or an explicit human request.

## Purpose

As the pipeline grew from three to seven stages (research, source
analyzer, scientific writer, illustration, layout scrutinizer,
readability scrutinizer; plus the human author at the apex), the
sequencing decisions stopped fitting in a researcher's head:

- The two scrutinizers run *after* a build but produce work for the
  writer and illustrator, which then re-trigger a build, which then
  re-triggers the scrutinizers — a cycle whose termination condition
  is "every scrutinizer reports `RE-SCRUTINY REQUIRED: no`".
- The Source Analyzer can run any time after a research pass and
  unblocks paper claims that depend on `[lit-retrieved]` entries; its
  outputs are themselves a hand-back to the writer.
- The illustrator should not run while the writer is editing the same
  float environments, but should run once the writer has committed
  caption and label changes.
- A new case study entering the pipeline forces a research-first
  pass; an editorial polish pass after a stable build skips research
  entirely.

The Orchestrator encodes those sequencing rules so a human can issue
a single instruction ("run the next stage", "drive to a clean build",
"prioritise the readability blockers") and have the pipeline make
progress without the human re-deriving the dependency graph each time.

## Inputs

- All scrutinizer registries and hand-back files under
  `docs/handbacks/`. Read in full at session start.
- `docs/logbook.md`. Read the most recent ten entries to understand
  what has run, what failed, and what is open.
- `docs/sources.md`. Used to compute the size of the
  `[lit-retrieved]` backlog (a candidate trigger for the Source
  Analyzer).
- `paper/main.pdf` build status (existence, mtime relative to
  `paper/main.tex`).
- `git status` and `git log` on the current branch — used to verify
  that a previous stage has actually committed before dispatching the
  next.
- The human's directive for this run, if any.

## Pipeline graph

```
                    ┌─────────────────────────┐
                    │  Stage 1 — Research     │
                    │  (per case study)       │
                    └──────────┬──────────────┘
                               │ produces sources, transcripts
                               ▼
                    ┌─────────────────────────┐
                    │  Stage 1.5 — Source     │
                    │     Analyzer            │◀──── triggered by
                    └──────────┬──────────────┘      [lit-retrieved] backlog
                               │ produces [ai-confirmed]
                               ▼
                    ┌─────────────────────────┐
                    │  Stage 2 — Sci Writer   │◀──── triggered by
                    └──────────┬──────────────┘      writer hand-backs
                               │ edits main.{md,tex} AND
                               │       main-condensed.{md,tex}
                               ▼
                    ┌─────────────────────────┐
                    │  Stage 3 — Illustrator  │◀──── triggered by
                    └──────────┬──────────────┘      illustrator hand-backs
                               │ produces figures (shared by both artifacts)
                               ▼
              ┌────────────────────────────────┐
              │  make all  (pdf + condensed)   │
              └──────┬─────────────────┬───────┘
                     │                 │
           main.pdf  │   main-condensed.pdf
                     │                 │
      ┌──────────────┴──────────────────┴─────────────────┐
      │          Stage 4 — Layout Scrutinizer              │
      │  (audits BOTH PDFs; LAY-* and COND-LAY-* IDs)     │
      └──────────────────────────┬─────────────────────────┘
                                 │  (parallel)
      ┌──────────────────────────┴─────────────────────────┐
      │       Stage 5 — Readability & Novelty Scrutinizer  │
      │  (audits BOTH .md files; RDB-* and COND-RDB-* IDs) │
      └──────────────────────────┬─────────────────────────┘
                                 │
                                 │ produces hand-backs to stages 2 & 3
                                 ▼
              ┌────────────────────────────────────────┐
              │  loop until ALL FOUR verdicts are:     │
              │  RE-SCRUTINY REQUIRED (long-form): no  │
              │  RE-SCRUTINY REQUIRED (condensed): no  │
              │  (from both stage 4 AND stage 5)       │
              └────────────────────────────────────────┘
```

## Decision rules

The Orchestrator chooses the next stage by evaluating the rules in
order and dispatching the first that fires.

| # | Condition | Dispatch |
|---|-----------|----------|
| 1 | Human directive specifies a stage. | The named stage. |
| 2 | A new case study directory exists with no research pass logged. | Stage 1 (Research). |
| 3 | The unhandled `[lit-retrieved]` backlog in `docs/sources.md` is ≥ 10 entries OR ≥ 1 entry blocks a load-bearing inline citation flagged by the writer. | Stage 1.5 (Source Analyzer). |
| 4 | Any hand-back file (`*-to-writer.md`, including condensed variants) contains an unresolved `LAY-`, `RDB-`, `COND-LAY-`, or `COND-RDB-` entry not yet annotated `[RESOLVED]` or `[DEFERRED]`. | Stage 2 (Scientific Writer remediation). |
| 5 | Any hand-back file (`*-to-illustrator.md`, including condensed variants) contains an unresolved entry, and the writer has no open writer-owned entries on the same source span. | Stage 3 (Illustrator remediation). |
| 6 | `paper/main.pdf` is missing or older than `paper/main.tex`, OR `paper/main-condensed.pdf` is missing or older than `paper/main-condensed.tex`. | `make -C paper all` (builds both artifacts; no agent — direct shell). |
| 7 | The most recent layout registries (`layout-defect-registry.md` or `condensed-layout-defect-registry.md`) have `RE-SCRUTINY REQUIRED: yes` and the corresponding PDF is newer than the registry. | Stage 4 (Layout Scrutinizer — covers both artifacts in one run). |
| 8 | The most recent readability registries (`readability-defect-registry.md` or `condensed-readability-defect-registry.md`) have `RE-SCRUTINY REQUIRED: yes` and the corresponding `.md` source is newer than the registry. | Stage 5 (Readability & Novelty Scrutinizer — covers both artifacts in one run). |
| 9 | All four scrutinizer verdicts report `no` (`RE-SCRUTINY REQUIRED (long-form): no` from stages 4 and 5, and `RE-SCRUTINY REQUIRED (condensed): no` from stages 4 and 5) AND no open writer/illustrator hand-backs remain. | **PIPELINE QUIESCENT** — escalate to the human author for the next directive (publication-track decision, new case study, or repository hygiene). |

### GitHub-issue dispatch table

Open GitHub issues with the following labels are now first-class inputs
to the pipeline. The orchestrator **must** poll open issues at the start
of every pipeline run (mandatory, not conditional on the absence of a
human directive) via the GitHub MCP tools where available
(`mcp__github__list_issues`, `mcp__github__issue_read`) and otherwise
ask the human author for a current snapshot. The poll result must be
recorded in the dispatch directive's preamble (issue numbers, labels,
and the routing applied to each); a "no open issues" outcome is also
recorded explicitly. Each label maps to a dispatch as follows:

| Label | Dispatch | Notes |
|-------|----------|-------|
| `idea` | Stage 1 (Research Protocol) with the issue body as the seed hypothesis. | Treat the issue title/body as the case-study or claim being proposed; cite the issue number in the resulting `docs/sources.md` and `docs/logbook.md` entries (rule 2). |
| `critique` | **Default route: Stage 2 (Scientific Writer)** with the issue body appended as a writer hand-back. The orchestrator may override to Stage 4 (Layout Scrutinizer) or Stage 5 (Readability & Novelty Scrutinizer) only if the critique unambiguously targets layout or readability and the writer has nothing to do with it; otherwise Stage 2 owns the response. | Routing decision must be recorded in the dispatch directive's `Decision rule fired` line. Sub-labels (`critique:layout` / `critique:readability` / `critique:prose`) are not required; absent a sub-label, default to Stage 2. |
| `provenance-gap` | Stage 1 (Research Protocol) targeted at the named experiment, AND a meta-process note in §5 (Termination/escalation) summarising which provenance gap was opened and which artifact class is implicated. | The meta-process note ensures provenance gaps are visible to the human author at quiescence even if the research pass closes them silently. |

Conflict resolution:

- If a writer- and illustrator-owned defect target the same float
  environment in `main.tex`, the writer goes first (it controls
  caption text and float placement; the illustrator regenerates
  assets afterward).
- If both the layout and readability scrutinizers want to run after a
  paper edit, dispatch them *in parallel* (they edit no source files,
  only registries; their outputs cannot conflict).
- If the writer has a queued remediation but the Source Analyzer has
  newly confirmed sources that change the writer's worklist, run the
  Source Analyzer first so the writer's pass is informed.

## Protocol

### 1. Orientation

1. Read `docs/logbook.md` (last ten entries).
2. Read every file under `docs/handbacks/`. Build a map of
   `<entry-id> → <state>` where state is one of
   `open | RESOLVED | DEFERRED | edge-case`.
3. `git status` and `git log -5 --oneline`.
4. Stat `paper/main.pdf` vs `paper/main.tex` and `paper/main.md`.
   Also stat `paper/main-condensed.pdf` vs `paper/main-condensed.tex`
   and `paper/main-condensed.md`.
5. Count `[lit-retrieved]`, `[ai-confirmed]`, `[lit-read]`,
   `[edge-case]` entries in `docs/sources.md`.

### 2. Apply the decision rules

Walk the rule table top to bottom; the first rule whose condition
holds determines the dispatch.

### 3. Dispatch

The Orchestrator does not run the dispatched agent itself; it emits
a *dispatch directive* — a structured Markdown block — for the human
to copy-paste into a fresh agent invocation, OR (if running inside a
harness that supports sub-agent spawning) directly invokes the named
agent with the standard prompt and the relevant inputs.

A dispatch directive looks like:

```
## ORCHESTRATOR DISPATCH 2026-05-02T15:42:00Z

- Decision rule fired: #4 (writer hand-back unresolved)
- Dispatched stage: Stage 2 — Scientific Writer remediation
- Prompt: docs/prompts/scientific-writer-prompt.md
- Worklist: docs/handbacks/{layout,readability}-to-writer.md
- Open IDs: LAY-01, LAY-02, LAY-03, LAY-04, RDB-01, RDB-02, RDB-12, …
- Branch: claude/add-layout-scrutinizer-agent-Ur5vX
- Predecessor commit: 39fb43e
- Expected next stage on success: Stage 3 (Illustrator) per rule #5
- Expected next stage on failure / partial: re-dispatch Stage 2 with
  remaining open IDs
```

### 4. Logbook entry

Append a session entry to `docs/logbook.md` recording the
orchestration decision: which rule fired, what was dispatched, what
the next anticipated stage is, and the timestamp. The orchestrator's
log is itself a research artifact (rule 4) — the chain of dispatch
decisions is part of the meta-process.

### 5. Termination

The Orchestrator does **not** make the publication decision (rule 13).
When rule #9 fires, it escalates to the human author with a summary of
state and recommended next moves (publish, new case study, history
rewrite, README pass, …) but does not act.

## Constraints

- **Rule 1 — Honesty.** The dispatch decision must be reproducible
  from the inputs the orchestrator declares; if a human re-runs the
  rules with the same inputs, they should reach the same dispatch.
- **Rule 4 — Artifacts.** Every dispatch is logged.
- **Rule 11 — Mirror discipline.** The orchestrator does not edit
  `paper/main.{md,tex}`. It only edits `docs/logbook.md` and emits
  dispatch directives.
- **Rule 13 — No publication.** The orchestrator never dispatches
  `make arxiv` and never auto-publishes. Quiescence (rule #9) is
  always escalated to the human, never converted into a publish
  action.
- **Scope discipline.** No paper edits, no figure regeneration, no
  source-status upgrades, no scrutinizer registry edits.

## Deliverables

1. **Dispatch directive** — Markdown block, either echoed to the
   transcript or written to `docs/handbacks/orchestrator-dispatch.md`
   appended log-style.
2. **Logbook entry** appended to `docs/logbook.md`.
3. **Optional sub-agent invocation** — if the harness permits, the
   orchestrator may directly launch the named agent with the right
   prompt and inputs.
