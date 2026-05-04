# Orchestrator dispatch log

Append-only. The orchestrator (stage 0) records every dispatch decision
here. See `docs/prompts/orchestrator-prompt.md` for the rule table.

---

## ORCHESTRATOR DISPATCH 2026-05-02T19:00:00Z

- Decision rule fired: **#3** — `[lit-retrieved]` backlog in `docs/sources.md` is 129 entries, far above the threshold of 10.
- Dispatched stage: **Stage 1.5 — Source Analyzer**
- Prompt: `docs/prompts/source-analyzer-prompt.md`
- Inputs:
  - `docs/sources.md` (129 `[lit-retrieved]`, 2 `[ai-confirmed]`, 4 `[lit-read]`, 4 `[needs-research]`, 10 `[unverified-external]`, 0 `[edge-case]`)
  - `docs/handbacks/readability-to-writer.md` — RDB-02 (H, unsupported-novelty framing) is DEFERRED pending comparator citations against L-SLOP-7 / L-SLOP-10 / L-SLOP-12; an `[ai-confirmed]` upgrade on those entries directly unblocks the next writer pass.
- Branch: `claude/start-orchestrator-36qQV`
- Predecessor commit: `f342d1c` (merge of PR #20, writer remediation pass on layout + readability hand-backs).
- Repository state at dispatch:
  - Working tree clean.
  - `paper/main.pdf` missing (gitignored; will need a `make -C paper pdf` rebuild before stage 4 can re-scrutinise).
  - Layout registry: `RE-SCRUTINY REQUIRED: yes` (writer pass largely consumed; illustrator hand-back LAY-05/06/12/13 still open).
  - Readability registry: `RE-SCRUTINY REQUIRED: yes` (RDB-01/02 DEFERRED to next writer pass).
- Why rule 3 ahead of rules 4–8:
  - Rule 4 condition does not hold: every writer-owned entry in both hand-backs carries `[RESOLVED]`, `[PARTIAL]`, or `[DEFERRED]` annotations.
  - Rule 5 (illustrator hand-backs) is queued but per the orchestrator-prompt conflict-resolution rule "if the writer has a queued remediation but the Source Analyzer has newly confirmed sources that change the writer's worklist, run the Source Analyzer first so the writer's pass is informed". RDB-02 is precisely that case.
  - Rules 6–8 require a fresh build; deferred until illustrator + writer passes complete.
- Expected next stage on success: **Stage 5 (Readability) re-evaluation** if RDB-02-relevant entries are upgraded to `[ai-confirmed]`, then **Stage 2 (Writer)** to consume the new RDB-02 / RDB-12 comparator framings, then **Stage 3 (Illustrator)** for the still-open illustrator hand-backs (LAY-05, LAY-06, LAY-12, LAY-13, RDB-04, RDB-05+08, RDB-07), then `make -C paper pdf`, then **Stages 4 + 5 in parallel** for re-scrutiny.
- Expected next stage on failure / partial: re-dispatch Stage 1.5 with the residual `[lit-retrieved]` worklist; surface `[edge-case]` flags to the human author.

---

## ORCHESTRATOR DISPATCH 2026-05-03T08:00:00Z (Stage 4 — Layout Scrutinizer)

- Trigger: brief from human operator citing the 2026-05-03 07:56 UTC `paper/main.pdf` rebuild (46 pp, 1,151,391 bytes) plus accompanying `paper/main.log`.
- Decision rule fired: **#6** — fresh PDF available; rule 11 mirror discipline intact; layout-side defect classes named in the brief require triage.
- Dispatched stage: **Stage 4 — Layout Scrutinizer**
- Prompt: `docs/prompts/layout-scrutinizer-prompt.md`
- Inputs: `paper/main.pdf`, `paper/main.log`, `paper/main.blg`, `paper/main.tex`, `paper/references.bib`.
- Deliverable: `docs/handbacks/layout-scrutiny-2026-05-03-build.md`.
- Findings (counts):
  - Class A (undefined `\ref`/`\cref`): **0** in current build (brief named ~30+; spot-checked 10 highest-impact labels — all defined). Reported as resolved upstream of this scrutiny per rule 1.
  - Class B (undefined citations): **0** `Citation … undefined`; **4** soft `Warning--empty year` (BIB-01..04, M severity).
  - Class C (overfull/underfull hboxes): **97** raw events (33 Overfull + 64 Underfull), collapsed into **6** action groups (OVF-01..05, UNF-01); 2 H-severity (OVF-01, OVF-03).
- Verdict: `RE-SCRUTINY REQUIRED: yes`. Two H-severity geometric overflows survive (table at l. 986–1005, path-bullet cluster at l. 2231–2242).
- Expected next stage: **Stage 2 — Scientific writer** to consume BIB-01..04 + OVF-01..05; then `make -C paper pdf`; then **Stage 4** re-scrutiny.

---

## ORCHESTRATOR DISPATCH 2026-05-04T??:??:??Z (artifact-pipeline rework + final-pass dispatch)

- Trigger: human-author directive — "rework the pipeline to actually build the artifacts (no publication yet); after rebuilding, send agent pipeline to a final pass for publication; close addressed issues with comment; extend `fair.md` with FAIR4AI; sort logbook chronologically; consider an Aligner agent; the condensed paper should be a complete paper by itself."
- Decision rules fired (in order):
  - **Pre-rules (rule changes).** Rule 17 (condensed paper as core submission) and rule 18 (traceability is paramount) added to `CLAUDE.md`. Rule numbering normalised (the duplicate "6" pre-rule-7 collapsed). Rule 11 augmented with chronological-order discipline for `docs/logbook.md`; rule 12 augmented to apply to the condensed pair as well.
  - **New stage.** Stage 6 (Aligner) added to the agent table; prompt at `docs/prompts/aligner-prompt.md`. Rule 18 made the Aligner authoritative for end-to-end traceability across paper sources, sources.md, registries, README, logbook, and redaction.
  - **Rule #6** — `paper/main.pdf` and `paper/main-condensed.pdf` rebuilt from clean state (`make -C paper distclean && make -C paper all`). matplotlib + pandas + seaborn installed in the build environment to satisfy the scripted-figure pipeline. Long-form: 57 pp, 1,250,832 bytes; condensed: 8 pp, 563,136 bytes (under the 10-page ceiling). Zero `??`, zero undefined refs / cites.
  - **Rule #4 / #5 implicit** — writer-side changes consumed: condensed paper made self-contained per rule 17 (eight practices enumerated inline; `Figure 2 → Table 1` + `Figure 3 → Figure 2` + `Figure 4 → Figure 3` renumber to match the rendered order; "DRAFT — derivative" red-box demoted to "Core submission" black-frame; *"Pointers"* section reframed as *"Companion / extended evidentiary record"*). Long-form FAIR4AI paragraph augmented with a back-reference to `docs/fair.md` §FAIR4AI and `docs/human-ai-collaboration-process.md`.
- GitHub-issue poll:
  - Open issues: #25 (peer review, accept with major revisions); #24 (Gödelian framing proposal).
  - **#25 — Status comment posted.** 5 of 10 review items confirmed resolved (LAY-17/-19 KPI overflows; history rewrite; Spider Farmer v2→v3 reconstruction; Stage-4 re-scrutiny post-Executive-Summary; figure PDF-version compatibility). 4 still open (Ondilo / Balboa device validation; EcoFlow coordinated disclosure; §69e UrhG legal sourcing; Zenodo DOI pending first release). Issue left **open** because the headline "Accept with Major Revisions" recommendation has unresolved blockers.
  - **#24 — Triage comment posted.** Disposition: research-direction note; not adopted at the framing level. Issue left open for human-author decision.
- Logbook (rule 11): re-sorted chronologically (oldest first) via `scripts/sort-logbook.py`. Sorted 51 entries; new sessions append at the bottom.
- Files written / modified by this dispatch:
  - `CLAUDE.md` (rules 11, 12, 17, 18; agent table extended to stage 6).
  - `paper/main-condensed.md` and `paper/main-condensed.tex` (rule-17 reframing; figure renumber; eight-practice enumeration).
  - `paper/main.md` and `paper/main.tex` (FAIR4AI cross-reference to `docs/fair.md` and `docs/human-ai-collaboration-process.md`).
  - `docs/fair.md` (FAIR4AI section + open issues + references).
  - `docs/human-ai-collaboration-process.md` (new — process spec).
  - `docs/prompts/aligner-prompt.md` (new — stage 6 prompt).
  - `docs/logbook.md` (chronological re-sort + usage-note update).
  - `scripts/sort-logbook.py` (new — re-sort tool).
  - `docs/handbacks/orchestrator-dispatch.md` (this entry).
- Expected next stage: **Stage 6 (Aligner)** sweep over the post-rebuild state — verify rule-17 self-containment of the condensed paper, mirror parity for both pairs, FAIR4AI cross-references, README KPI parity, logbook chronological order. Then **Stages 4 + 5** in parallel against the rebuilt PDFs / Markdown sources to confirm `RE-SCRUTINY REQUIRED: no` survives the rule-17 reframe of the condensed paper.
- Expected next stage on failure / partial: re-dispatch the writer (stage 2) for any rule-17 / rule-18 violations the Aligner files.
- Rule 14 (no publication): local artifacts only. No `make arxiv`. No public push beyond the working branch.
