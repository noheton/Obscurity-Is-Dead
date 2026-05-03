---
status: "[MISSING-TRANSCRIPT]"
case-study: "iot-integrator-balboa-gateway-ultra"
created: 2026-05-03
created-by: "Claude Opus 4.7 (transcript-reconstruction pass)"
canonical-source: "docs/logbook.md, 2026-05-02 entries (lines 1139-1248) for IoT Integrator Phase 0 bootstrap, Phase 0 conflict resolution, Phase 1 desk research, Phase 2 weakness analysis, Phase 3 implementation + close-out, and researcher acceptance."
---

# T-BAL-* — Missing IoT-Integrator transcripts (Balboa Gateway Ultra)

## What should be here

Per CLAUDE.md rule 4, AI conversation transcripts are first-class research
artifacts. The Balboa Gateway Ultra case study
(`experiments/iot-integrator-balboa-gateway-ultra/`) was produced across at
least six agent-loop sessions on 2026-05-02 (logbook entries at lines
1139–1248) and a follow-up research-protocol audit pass:

- **T-BAL-0** Phase 0 bootstrap.
- **T-BAL-0b** Phase 0 conflict resolution (project-name disambiguation).
- **T-BAL-1** Phase 1 desk research.
- **T-BAL-2** Phase 2 weakness analysis.
- **T-BAL-3** Phase 3 implementation + close-out.
- **T-BAL-ACCEPT** Researcher acceptance / close-out turn.
- **T-BAL-AUDIT** Research-protocol audit + scientific-writer + illustration
  pass that touched this case (logbook entry at line 1258).

## Why they are not here

The Claude Code CLI web harness in use during these sessions did not
expose a transcript-export endpoint, and the live session buffers were
not persisted to a file the assistant or the human can read back
post-hoc. **No fabricated transcript content has been written to this
directory.** Per rule 1 (honesty), the absence is recorded explicitly
rather than papered over with a reconstructed narrative.

## Closest available substitute

- `docs/logbook.md` — the per-phase narratives at lines 1139–1248 were
  written contemporaneously and reviewed / accepted by the human at
  commit time.
- `experiments/iot-integrator-balboa-gateway-ultra/REPORT.md`,
  `RESEARCH-PROTOCOL.md`, `provenance.md`, and the `process/`,
  `integration/`, and `original/` subtrees — the structured artefacts each
  session produced.
- The corresponding commit-message corpus on the relevant branch and its
  merge into `main`.

If a verbatim export is recovered later, it should be added here as
`T-BAL-N-<phase>.md` files with `status: [verbatim-export]` and any
divergence from the logbook narrative recorded in
`experiments/paper-meta-process/provenance.md`.
