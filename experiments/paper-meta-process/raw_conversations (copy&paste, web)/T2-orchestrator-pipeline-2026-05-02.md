---
status: "[reconstructed-from-logbook]"
date: 2026-05-02
model: "Claude Opus 4.7 (anthropic2026claude in paper/references.bib)"
interface: "Claude Code CLI (web-hosted session, harness commit f342d1c → 6ce1a99)"
session-branch: "claude/start-orchestrator-36qQV"
session-purpose: >
  Orchestrator-coordinated pipeline run: Source-Analyzer slices 1+2+3,
  hardware-side effort-gap research and writing (cluster A.2),
  Executive Summary insertion, and Stages 4+5 re-scrutiny. Twelve commits
  (316f58e..6ce1a99) produced via approximately fifteen sub-agent
  dispatches across Stages 0, 1, 1.5, 2, 4, and 5.
canonical-source: "docs/logbook.md, 2026-05-02 entries from line 1463 (Stage 0 first run) through line 1691 (Stage 4 re-run after cluster A.2 + §6.8). Commit messages 316f58e..6ce1a99 carry parallel narrative."
note: >
  This file is a RECONSTRUCTION from the project logbook plus the
  associated commit history, NOT a verbatim export of the live chat
  transport. The Claude Code CLI web harness in use during this session
  did not expose a transcript-export endpoint, so the live conversation
  text cannot be retrieved post-hoc. Per CLAUDE.md rule 4, AI conversation
  transcripts are first-class research artifacts; in the absence of a
  verbatim export, the next-best artifact is this reconstruction, which
  defers to docs/logbook.md as the canonical record. Should a verbatim
  export be recovered later, it should be added as a [verbatim-export]
  companion file and any divergences recorded in
  experiments/paper-meta-process/provenance.md.
redactions: >
  None applied within this transcript. The reconstruction does not
  introduce any community-implementer GitHub handle or repository path
  that the parallel anonymization sweep is removing from the paper
  (CLAUDE.md rule 12). Where the underlying logbook entries reference
  redacted markers (e.g. `[REDACTED:username:S-SF-5-username]`,
  `[REDACTED:credential:S-SF-5-password]` in §3.6 of the paper), this
  file preserves the marker form verbatim and does NOT expand it.
---

# T2 — Orchestrator-coordinated pipeline run, 2026-05-02

## Frontmatter context

The session opened against branch `claude/start-orchestrator-36qQV` with the
working tree clean at predecessor commit `f342d1c` (merge of PR #20, the
layout-scrutinizer agent prompt). The researcher (Florian Krebs) issued the
human directive *"start the orchestrator"* with no specific stage named.
Twelve commits later, the branch carried (a) two new in-paper sections
(§1.4 hardware-side effort-gap paragraph and §6.8 evidence-asymmetry
subsection), (b) a 2-page Executive Summary inserted between the abstract
and §1, (c) fourteen entries upgraded to `[ai-confirmed]` across three
Source-Analyzer slices, (d) six new bib keys for cluster A.2 plus
`papp2015embedded`, and (e) refreshed Stage 4 + Stage 5 defect registries
(`LAY-19..LAY-22`, `RDB-22..RDB-26`).

## Commit timeline

### 1. `316f58e` — Orchestrator first dispatch (Stage 0)

The orchestrator inspected `docs/handbacks/{layout,readability}-defect-registry.md`,
the last ten logbook entries, and the source-ladder counts in
`docs/sources.md` (129 `[lit-retrieved]`, 2 `[ai-confirmed]`, 4 `[lit-read]`,
4 `[needs-research]`, 10 `[unverified-external]`). Decision rule #3 fired:
the `[lit-retrieved]` backlog (≥ 10) plus the H-severity readability defect
RDB-02 (unsupported-novelty framing of "the novelty is the integration"),
which was independently blocked on comparator citations against L-SLOP-7 /
L-SLOP-10 / L-SLOP-12, made the next dispatch unambiguous. Per the
orchestrator-prompt conflict-resolution rule, the Source Analyzer ran first
so any newly `[ai-confirmed]` entries would be available to the writer.
Files written: `docs/handbacks/orchestrator-dispatch.md` (new, append-only)
and a logbook session entry. No edits to `paper/main.{md,tex}`,
`docs/sources.md`, or any scrutinizer registry (orchestrator scope
discipline).

### 2. `eb8293c` — Source-Analyzer slice 1 (10 entries; 4 `[ai-confirmed]`)

First parallel-dispatch Source Analyzer run in the project. **Five parallel
sub-agents (Claude Opus 4.7), two entries each, return-only protocol**;
the orchestrator merged centrally to avoid file-write races. Slices:
L-SLOP-7 + L-SLOP-10; L-SLOP-12 + L-VD-5; L-RE-2 + L-VD-1; L-HC-1 + L-HC-6;
L-BLE-4 + L-BLE-5. Outcome: four `[ai-confirmed]` upgrades (L-BLE-4,
L-SLOP-7, L-SLOP-10, L-SLOP-12 — collectively the comparator triplet that
unblocks RDB-02), five edge cases (L-VD-1, L-VD-5, L-HC-1, L-HC-6, L-BLE-5),
one fetch-failure (L-RE-2: NDSS PDF + 3 mirrors HTTP 403). Each upgrade
also surfaced a `references.bib` authorship correction.

### 3. `79d7958` — Writer remediation pass on RDB-02 + RDB-12

The §10 novelty paragraph was rewritten to name the three-layer comparator
triplet (Sabel & Larhammar Stockholm Declaration; Cheng/Calhoun/Reedy
practitioner-level guidance; Pellegrina & Helmy AI-detector / citation /
image-verification review) and recast the integration claim as application
of these named prior strands to the security-research interoperability
context. §1.4 contributions gained comparator half-clauses: (1) ↔ L-RE-2;
(2) ↔ L-BLE-4; (3) ↔ L-SLOP-7/-10/-12. Four BibTeX entries added with
corrected authors and DOIs (`sivakumaran2023bleguuide`, `sabel2025stockholm`,
`cheng2025aiwriting`, `pellegrina2025aiintegrity`). RDB-02 and RDB-12
flipped DEFERRED → RESOLVED. Mirror discipline: md ↔ tex updated together.

### 4. `b39ba0c` — Source-Analyzer slice 2 (10 entries; 8 `[ai-confirmed]`)

Run **in parallel** with the slice-1 writer pass (`79d7958`); no file
conflict (analyzers wrote `docs/sources.md` only; writer wrote
`paper/main.{md,tex}` + `references.bib`). Same five-agent / two-entries
pattern. Eight upgrades: L-RE-1 (LLM4Decompile, >100% re-executability
verbatim), L-RE-3 (REx86 ACSAC 2025, n=43, 31% → 53% with p=0.189
preserved), L-VD-2 (8-34% / 68-72% PoC success), L-VD-3 (71/102 ~70%
CVE reproduction), L-HC-4 (strongest direct-contradiction quote), L-HC-7
(5,135-app three-tool comparison), L-BLE-1, L-BLE-2. Two
`[ai-confirmed-attempt-failed]` (L-HC-2, L-HC-3 — PDFs 403 but cross-
confirmed via search snippets). Cumulative across slices 1+2: 12 net
`[ai-confirmed]` upgrades; project-level count 2 → 14.

### 5. `5fc415b` — Hardware-side effort-gap hypothesis lodged (cluster A.2)

The researcher raised a parallel hypothesis: AI-assisted reverse engineering
compresses the **hardware-access** path (JTAG/UART/SPI test-pad
identification, ChipWhisperer-class glitching, AI-assisted PCB photo
analysis, automated firmware extraction) alongside the software path
already documented in cluster A. Six placeholder entries lodged in
`docs/sources.md` as a new **Claim cluster A.2 — Hardware-side effort-gap
reduction**, all `[needs-research]`. Open question recorded explicitly:
peer-reviewed-vs-grey-literature evidence asymmetry between software and
hardware sides — itself a publishable observation. No edits to `paper/`
per rule 8.

### 6. `e3d6166` — Stage 1 research pass on cluster A.2 (3 parallel research agents)

**Three parallel sub-agents (Claude Opus 4.7), two L-HW-RE-* placeholders
each**, return-only protocol; first parallel-dispatch Stage-1 run.
All six placeholders concretised: L-HW-RE-1 Grand DEF CON 21 2013
(JTAGulator, grey); L-HW-RE-2 O'Flynn & Chen COSADE 2014 (ChipWhisperer,
~100× cost reduction; *the* peer-reviewed quantitative cost anchor);
L-HW-RE-3 Vasile, Oswald & Chothia CARDIS 2018 (>45% UART suffices on 24
IoT devices); L-HW-RE-4 Botero et al. ACM JETC 2021 (AI-assisted PCB-RE
canonical, narrowed claim only); L-HW-RE-5 hardware-hacking handbook
cluster (Grand 2004; Huang 2003+2017; van Woudenberg & O'Flynn 2021/2022;
Smith 2016) plus Papp et al. 2015 IEEE PST taxonomy; L-HW-RE-6 Becker et
al. SOUPS 2020 (14-week skill-floor verbatim). **Headline meta-finding
(rule 4 artefact):** the cluster A.2 hypothesis is supported, but with an
evidence base structurally asymmetric to cluster A — no peer-reviewed
paired "time-to-extract 2010 vs 2024" longitudinal benchmark exists.

### 7. `f3ce051` — Writer pass inserting cluster A.2 into §1.4 + new §6.8

§1.4 gained a new paragraph between the boredom-barrier figure and the
"The paper contributes:" enumeration, naming the hardware-side effort gap
and triangulating it via L-HW-RE-2 (~100× equipment-cost), L-HW-RE-3
(>45% UART-suffices), L-HW-RE-6 (14-week skill-floor), with L-HW-RE-5
bookending the period. A fifth contribution bullet was appended pointing
at the new §6.8. **§6.8 Evidence asymmetry between software-side and
hardware-side effort-gap compression** landed as a synthesis-section meta-
observation, framed as a finding about empirical hardware-security-research
methodology (not as a weakness of cluster A.2). All six entries cited as
**footnoted `[L-HW-RE-X]` markers** under `fn:hwre-cluster`, NOT inline,
since Source Analyzer had not yet upgraded the cluster. Ten new bib keys
lodged for the eventual inline-citation upgrade.

### 8. `a12da72` — Source-Analyzer slice 3 (cluster A.2; 5 `[ai-confirmed]`)

Run **in parallel** with the cluster A.2 writer pass (`f3ce051`); no file
conflict. **Three parallel sub-agents, two L-HW-RE-* entries each.**
Outcomes: L-HW-RE-1 `[ai-confirmed]` within grey-lit framing (JTAGulator
GitHub README quote, since the DEF CON slides PDF returned 403); L-HW-RE-2
`[ai-confirmed-attempt-failed]` (ChipWhisperer 2014: all paper mirrors
returned 403; the load-bearing ~USD 30,000 vs ~USD 300 quote could not be
retrieved verbatim — principal residual blocker); L-HW-RE-3 `[ai-confirmed]`
("in over 45% of the cases, an exposed UART interface is sufficient to
obtain a firmware dump", verbatim); L-HW-RE-4 `[ai-confirmed]` for the
narrowed claim only; L-HW-RE-5 books `[ai-confirmed-grey]` (bibliographic
existence only) plus Papp 2015 `[ai-confirmed]`; L-HW-RE-6 `[ai-confirmed]`
for the verbatim 14-week training claim, sub-claim "two participants
matched expert solution times" held back. Two writer-relevant corrections
surfaced: van Woudenberg & O'Flynn copyright is 2022, not 2021; ReverSim
first author is Becker, not Wiesen.

### 9. `537fae2` — Writer cluster A.2 inline-citation promotion + bib corrections

L-HW-RE-1/-3/-4/-6 promoted from footnoted `[L-HW-RE-X]` markers to inline
`\citep{}` calls (`grand2013jtagulator`, `vasile2018breakingallthethings`,
`botero2021hwretutorial`, `becker2020hwreexploratory`). Papp et al. 2015
added as `papp2015embedded` and inline-cited in §6.8 as the peer-reviewed
embedded-systems attack-taxonomy complement to the L-HW-RE-5 grey-lit
cluster. L-HW-RE-2 stays footnoted (attempt-failed); L-HW-RE-5 stays
footnoted (grey-lit). Bib corrections: `vanwoudenberg2021hwhandbook` →
`vanwoudenberg2022hwhandbook` with `year = {2022}`; in-prose mentions now
read "2021/2022" consistently. Pre-existing `\fp{RESEARCH-PROTOCOL.md}`
caption-macro fragility fixed (replaced with `\texttt{}`) to unblock
`make pdf`. Build green: 42 pages, SHA-256 `62e68f6a...`.

### 10. `e9ff2f0` — Readability-Scrutinizer re-run

Re-scrutiny of `paper/main.md` against the post-`537fae2` head.
RDB-01..RDB-21 annotated in-place: `[RESOLVED]` ×5 (RDB-02, RDB-12,
RDB-15, RDB-16, RDB-18); `[PARTIAL]` ×1 (RDB-20); `[DEFERRED — unchanged]`
×13; `[CONFIRMED — preserved]` ×1. New entries: **RDB-22** (M, §1.4
cluster A.2 paragraph: 254-word block, three sentences over 40 words,
list-of-citations-as-prose); **RDB-23** (M, §6.8 ~120-word run-on
enumerating five evidence items — longest single sentence in the paper);
**RDB-24** (positive trace; novelty audit — §6.8 evidence-asymmetry
meta-observation **NOVEL**, no comparable peer-reviewed source);
**RDB-25** (positive trace; year-consistency for van Woudenberg & O'Flynn);
**RDB-26** (L, §1.4 fifth contribution breaks artifact-tied parallelism).
Sub-claim discipline: L-HW-RE-6 "two participants matched expert solution
times" CONFIRMED ABSENT from `paper/main.md`. Verdict:
`RE-SCRUTINY REQUIRED: yes`.

### 11. `a104fa3` — Executive Summary writer

Researcher-driven writer pass adding a 2-page Executive Summary between the
abstract and §1 (Introduction) so readers can absorb the paper's claims in
≈ 90 seconds. AI-drafted from existing body content (rule 1); introduces
no new claims; every numerical anchor (24.4% / 31% → 53% / >100% software-
side; >45% UART / 14-week / 125–500× / 8–34% / 68–72%) appears in the body
and is sourced via the same source-register entry the body cites. Hero
figure (`fig11-eight-practices`, ILL-05) and supporting figure
(`fig1-effort-gap`) referenced via `\cref{}` rather than re-embedded —
text-only summary keeps the page count at 2 and avoids duplicating the
visual abstract. Edge-case L-VD-1 / L-VD-5 markers footnoted, not promoted
inline. Total paper page count: 42 → 44.

### 12. `6ce1a99` — Layout-Scrutinizer re-run

Re-scrutiny of the rebuilt PDF (SHA-256 `62e68f6a...`, 42 pages — the
Executive Summary in commit `a104fa3` had not yet been rebuilt; layout
re-sweep will need one more pass). LAY-01..LAY-18 dispositions:
`[RESOLVED]` ×2 (LAY-01 broken cref now resolves; LAY-05 Fig 7 overflow
closed); `[PARTIAL]` ×11; `[UNCHANGED]` ×2; `[DEFERRED-by-design]` ×1
(LAY-12 logo placeholder); `[REGRESSED-INTERPRETATION]` ×1 (LAY-11 folded
into LAY-06); `[REGRESSED]` ×1 (LAY-17 severity L → M); **NEW ×4
(LAY-19..LAY-22)**. H-severity count went from 6 to 1. Most consequential:
**LAY-19** — Meta-process KPI `tabular{llll}` at `main.tex:872` overflows
by 226.22pt; same root cause as LAY-17 family (Spider Farmer + EcoFlow
KPI tables); a single project-wide `tabular{llll}` → `tabularx{l l X r}`
conversion closes all three. Cluster A.2 / §6.8 verification: all five new
`\citep{}` calls resolve; `\cref{sec:synthesis-evidence-asymmetry}` and
`\textsuperscript{\ref{fn:hwre-cluster}}` resolve at all four reuse sites;
L-HW-RE-2 verified as footnote, not inline. Verdict:
`RE-SCRUTINY REQUIRED: yes`.

## Sub-agent inventory

Across the twelve commits, the orchestrator dispatched approximately
**fifteen sub-agents (Claude Opus 4.7)**, all under a return-only protocol
(sub-agents proposed annotations, report-table rows, and writer hand-back
blocks; the orchestrator merged centrally on the canonical files):

| Stage | Pass | Sub-agents | Pattern |
|-------|------|------------|---------|
| 1.5 | Source Analyzer slice 1 | 5 | parallel, 2 entries / agent |
| 2   | Writer (RDB-02 + RDB-12) | 1 | serial |
| 1.5 | Source Analyzer slice 2 | 5 | parallel with slice-1 writer |
| 1   | Research cluster A.2 | 3 | parallel, 2 placeholders / agent |
| 2   | Writer (cluster A.2 §1.4 + §6.8) | 1 | serial |
| 1.5 | Source Analyzer slice 3 | 3 | parallel with cluster-A.2 writer |
| 2   | Writer (cluster A.2 inline-citation promotion) | 1 | serial |
| 5   | Readability-Scrutinizer | 1 | serial |
| 2   | Writer (Executive Summary) | 1 | serial |
| 4   | Layout-Scrutinizer | 1 | serial |

**Rationale for the parallel-dispatch tactic.** The Source Analyzer (and,
adapted from it, the Stage 1 cluster-A.2 research pass) is intrinsically
embarrassingly parallel: each entry is independent, the work is
fetch-bound rather than reasoning-bound, and the per-agent context window
stays small when each agent owns only two entries. Three properties
followed:

1. **Context economy.** Each sub-agent saw only its two entries plus the
   Source-Analyzer prompt; the orchestrator carried the cumulative state.
2. **Failure-mode isolation.** Five parallel sub-agents made fetch-failure
   surface as a *harness-level network signal* (NDSS / arXiv / IEEE Xplore
   / SemanticScholar / ResearchGate concentrating on the same gateway
   block), not as a per-paper signal — visible only because multiple
   independent agents reported the same failure family.
3. **Write-conflict avoidance.** Sub-agents were instructed *not* to edit
   `docs/sources.md` directly; the orchestrator merged centrally,
   eliminating the parallel-write race on a single file.

## Headline outcomes

- **§1.4 cluster A.2 paragraph + new §6.8 evidence-asymmetry subsection.**
  The §1.4 effort-gap thesis now triangulates a hardware-side dimension
  (cost / skill / interface-yield); §6.8 frames the asymmetry between
  software-side and hardware-side evidence bases as a publishable
  meta-observation. RDB-24 verdict: **NOVEL — no comparable peer-reviewed
  source found.**
- **14 entries upgraded to `[ai-confirmed]`** across three SA slices
  (slices 1+2: 12 net; slice 3: 4 cluster-A.2 anchors plus 1 grey-lit-
  framed). Cumulative project-level `[ai-confirmed]` count: 2 → ~22 if the
  `[ai-confirmed-grey]` and `[ai-confirmed-bibliographic]` tiers are
  counted; 14 if only the strict tier is.
- **6 cluster A.2 anchors lodged** — L-HW-RE-1..6, four promoted to inline
  `\citep{}` (`grand2013jtagulator`, `vasile2018breakingallthethings`,
  `botero2021hwretutorial`, `becker2020hwreexploratory`) plus
  `papp2015embedded` in §6.8; L-HW-RE-2 (ChipWhisperer 2014) held footnoted
  pending human `[lit-read]` (load-bearing ~100× cost-floor anchor).
- **Executive Summary** (2 pages) inserted between abstract and §1;
  re-presents claims at the 90-second-skim register without adding new
  claims; total page count 42 → 44.
- **New defect IDs.** Readability registry: **RDB-22..RDB-26**. Layout
  registry: **LAY-19..LAY-22**. RDB-22 + RDB-23 are mechanical
  sentence-length / list-of-citations-as-prose remedies; LAY-19 is the
  H-severity Meta-process KPI tabular overflow that, together with the
  LAY-17 KPI-table family, can be cleared by a single `tabular{llll}` →
  `tabularx{l l X r}` conversion.
- **Two writer-relevant corrections** propagated from the SA slice 3:
  van Woudenberg & O'Flynn 2021 → 2022; ReverSim first author Wiesen →
  Becker.

## Honesty disclosures (CLAUDE.md rule 1)

- This file was **reconstructed** from `docs/logbook.md` (2026-05-02
  entries from line 1463 through line 1691) and the commit messages of
  `316f58e..6ce1a99`, NOT exported from a chat-transport endpoint. The
  Claude Code CLI web harness in use during this session does not provide
  a transcript-export endpoint that the assistant or the human can invoke
  post-hoc; the in-session conversation buffer is not persisted to a file
  the harness can read back. The next-best research artifact (rule 4) is
  the project logbook plus the commit-message corpus, both of which are
  written contemporaneously by the assistant and reviewed/accepted by the
  human via the commit step. This reconstruction is faithful to the
  logbook narrative but is necessarily a *summary* of the agent-loop
  exchanges, not their literal text.
- The canonical source for any claim in this file is `docs/logbook.md`.
  If this transcript and the logbook diverge, the logbook wins.
- Sub-agent prompts and replies are described, not quoted — none of the
  sub-agent text strings are recoverable from the harness. The Source-
  Analyzer report and writer hand-back files
  (`docs/handbacks/source-analyzer-report.md`,
  `docs/handbacks/source-analyzer-to-writer.md`) carry the structured
  artefacts the sub-agents produced and remain the closest available
  proxy for the sub-agent reply text.

## Reproduction notes — the user prompts that drove the session

The session was driven by a small number of human directives, recoverable
from the orchestrator-dispatch log and the per-stage logbook entries:

1. **Initial directive (Stage 0 trigger):** *"start the orchestrator"* —
   no stage named; the orchestrator walked decision rules top-to-bottom
   and fired rule #3 (`[lit-retrieved]` backlog ≥ 10 plus the H-severity
   readability defect RDB-02 blocked on comparator citations).
2. **Researcher-raised hypothesis (cluster A.2 trigger):** the researcher
   raised during the orchestrator session that the effort gap has a
   hardware-access dimension parallel to the software-side compression
   already documented in cluster A — JTAGulator-style automated test-point
   identification, ChipWhisperer-class glitching, AI-assisted PCB photo
   analysis, automated UART/SWD probing, off-the-shelf FFC / pogo-pin
   breakouts. This drove commit `5fc415b` (placeholder lodgement) → `e3d6166`
   (Stage 1 research pass) → `f3ce051` (writer insertion into §1.4 + §6.8).
3. **Researcher-driven Executive Summary directive** (commit `a104fa3`):
   request to add a 2-page front-matter section that re-presents claims
   in a 90-second-skim register without adding new claims.
4. **Stage 4 + Stage 5 re-scrutiny dispatch** after `537fae2` and
   `a104fa3`, run in parallel against the same rebuilt PDF, files-disjoint
   by construction (Stage 4 → `docs/handbacks/layout-*.md`; Stage 5 →
   `docs/handbacks/readability-*.md`).

To reproduce the session against the same predecessor commit `f342d1c`,
an operator would invoke each stage prompt under
`docs/prompts/{orchestrator,source-analyzer,research-protocol,scientific-writer,layout-scrutinizer,readability-novelty}-prompt.md`
in the order recorded in the timeline above, dispatching the Source
Analyzer (slice 1), the cluster-A.2 research pass, and slice 3 in parallel
with their respective writer passes per the per-commit logbook entries.
The build verification step is `make -C paper pdf` after each writer pass;
the rebuilt PDF after `537fae2` had SHA-256
`62e68f6a5208814d47a51a8124bc7c7a836e7c9f3104951bc40a5c8dfda81384` and
42 pages prior to the Executive Summary; 44 pages after `a104fa3`.

## Cross-references

- Canonical session record: `docs/logbook.md`, 2026-05-02 entries.
- Orchestrator dispatch log: `docs/handbacks/orchestrator-dispatch.md`.
- Source-Analyzer reports: `docs/handbacks/source-analyzer-report.md`,
  `docs/handbacks/source-analyzer-to-writer.md`.
- Defect registries (post-pipeline state): `docs/handbacks/layout-defect-registry.md`,
  `docs/handbacks/readability-defect-registry.md`.
- Source register entries lodged in this session: `docs/sources.md` cluster
  A.2 (L-HW-RE-1..6) and the slice-1 / slice-2 / slice-3 status-line
  annotations.
- BibTeX entries lodged in this session: `paper/references.bib` —
  `sivakumaran2023bleguuide`, `sabel2025stockholm`, `cheng2025aiwriting`,
  `pellegrina2025aiintegrity` (slice 1 hand-back); `grand2013jtagulator`,
  `oflynn2014chipwhisperer`, `vasile2018breakingallthethings`,
  `botero2021hwretutorial`, `grand2004hardwarehacking`,
  `huang2003hackingxbox`, `huang2017hardwarehacker`,
  `vanwoudenberg2022hwhandbook`, `smith2016carhackershandbook`,
  `becker2020hwreexploratory`, `papp2015embedded` (cluster A.2).
