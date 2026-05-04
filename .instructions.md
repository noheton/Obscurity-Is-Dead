# Repository AI Instructions — pointer

> **This file is a stub.** The canonical AI policy for this repository
> lives in [`CLAUDE.md`](CLAUDE.md) (rules 1–18, agent pipeline, and
> verification-status ladder). The previous in-line copy of the rules
> drifted out of sync with `CLAUDE.md` and was demoted to this pointer
> by the Aligner agent (`docs/prompts/aligner-prompt.md`, ALN-13,
> 2026-05-04) to eliminate a synchronisation-debt surface.

If your tool reads instructions by filename — `.instructions.md`,
`copilot-instructions.md`, `CLAUDE_CODE_INSTRUCTIONS.md` — it will find
the same pointer here. Open `CLAUDE.md` for the actual policy.

Any change to repository AI policy must be made in `CLAUDE.md`. The
Aligner agent (Stage 6) checks this invariant on every pass.
