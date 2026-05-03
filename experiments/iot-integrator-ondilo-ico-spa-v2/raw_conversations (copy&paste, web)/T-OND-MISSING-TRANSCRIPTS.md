---
status: "[MISSING-TRANSCRIPT]"
case-study: "iot-integrator-ondilo-ico-spa-v2"
created: 2026-05-03
created-by: "Claude Opus 4.7 (transcript-reconstruction pass)"
canonical-source: "docs/logbook.md, 2026-05-02 entries — Sessions 13/14/15/16 (lines 930-1067) for IoT Integrator Phase 0/1/2/3 + APK addendum, plus the post-pass research-protocol audit recorded in the 2026-05-02 IoT-Integrator-cases entry."
---

# T-OND-* — Missing IoT-Integrator transcripts (Ondilo ICO Spa V2)

## What should be here

Per CLAUDE.md rule 4, AI conversation transcripts are first-class research
artifacts. The Ondilo ICO Spa V2 case study (`experiments/iot-integrator-ondilo-ico-spa-v2/`)
was produced across at least four agent-loop sessions on 2026-05-02
(logbook Sessions 13–16, lines 930–1067) and a follow-up
research-protocol audit pass:

- **T-OND-0** Phase 0 bootstrap (Session 13).
- **T-OND-1** Phase 1 desk research (Session 14).
- **T-OND-2** Phase 2 weakness analysis (Session 15).
- **T-OND-3** Phase 3 implementation + APK addendum + close-out (Session 16).
- **T-OND-AUDIT** Research-protocol audit + scientific-writer + illustration
  pass that touched this case (logbook entry at line 1258).

## Why they are not here

The Claude Code CLI web harness in use during these sessions did not
expose a transcript-export endpoint, and the live session buffers were
not persisted to a file the assistant or the human can read back
post-hoc. **No fabricated transcript content has been written to this
directory.** Per rule 1 (honesty), the absence is recorded explicitly
rather than papered over with a reconstructed narrative.

## Closest available substitute

- `docs/logbook.md` — Sessions 13/14/15/16 carry contemporaneously-written
  per-phase narratives reviewed and accepted by the human at commit time.
- `experiments/iot-integrator-ondilo-ico-spa-v2/REPORT.md`,
  `RESEARCH-PROTOCOL.md`, `provenance.md`, and the `process/` and
  `integration/` subtrees — the structured artefacts each session produced.
- The corresponding commit-message corpus on `claude/iot-pool-spa-integration-tkpaD`
  (and its merge into `main`).

If a verbatim export is recovered later (e.g. from harness storage that
becomes accessible), it should be added here as
`T-OND-N-<phase>.md` files with `status: [verbatim-export]` and any
divergence from the logbook narrative recorded in
`experiments/paper-meta-process/provenance.md`.
