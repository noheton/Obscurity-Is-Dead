# Stage 5 — Readability & Novelty re-scrutiny (round 2, 2026-05-03)

- **Agent.** Claude Opus 4.7 (Stage 5).
- **Branch.** `claude/review-open-issues-PfNx9`.
- **Trigger.** Orchestrator dispatch after writer commit `370e792`
  ("paper: Mythos hook + guardrails-as-band-aid + plagiarism 9th
  practice") and illustrator commit `d2858ac` (figure overhaul).
  This run does NOT inspect a freshly-built PDF; it is a re-scrutiny
  of `paper/main.md` (Stage 5 scope).
- **Carry-over from round 1.** Round-1 verdict was
  `RE-SCRUTINY REQUIRED: yes` for the two new **L** entries
  RDB-27 (Author's Note paragraph density) and RDB-28 (§3.4 v2→v3
  reconstruction sentence length); RDB-22 / RDB-23 / RDB-25
  RESOLVED-confirmed; RDB-01 H→M. Writer loop-2 commit `4987d9d`
  is recorded in the logbook as the loop intended to close
  RDB-27 / RDB-28.

## Per-RDB status, this round

| ID | Round-1 status | This round | Span (md) | Notes |
|----|----------------|-----------|-----------|-------|
| RDB-01 | RESOLVED-but-residual (H→M) | **PRESERVED** | §7.6 `main.md:512` | Back-reference to §5.6 still in place; named-author triplet at §7.6 unchanged. Optional final tightening still routed to writer; not blocking. |
| RDB-02 | RESOLVED | **PRESERVED** | §10 `main.md:721` | Three-layer comparator triplet (L-SLOP-7 / L-SLOP-10 / L-SLOP-12) still named; "we do not claim to subsume" hedging intact. |
| RDB-03 | DEFERRED | **DEFERRED-unchanged** | abstract / §1.4 / §10 | Triple-restatement pattern preserved by writer round; no progression rule applied. |
| RDB-04 | DEFERRED | **DEFERRED-unchanged + COMPLICATED** | §10 `main.md:704–717` | Eight-item enumeration retained; ninth practice added as item 9 in the same enumeration but explicitly excluded from Figure 11. Stage 5 still endorses option (b) (drop the §10 prose enumeration; lean on Figure 11 + a one-sentence recap), with the ninth practice surviving as a numbered prose addendum so the figure ↔ text count mismatch (8 rows vs 9 prose items) is *intentional and on-record*. The "logged for the next iteration of the framework rather than added to Figure 11" framing at `main.md:715` is the right hedge; option (b) remains preferred. |
| RDB-05 / RDB-06 / RDB-07 / RDB-08 / RDB-09 | DEFERRED | **DEFERRED-unchanged** | per registry | Writer round did not touch these spans. |
| RDB-10 | DEFERRED | **DEFERRED-unchanged** | §1.3 | unchanged |
| RDB-11 | DEFERRED | **DEFERRED-unchanged** | §6.4 | unchanged |
| RDB-12 | RESOLVED | **PRESERVED** | §1.4 | comparator half-clauses intact |
| RDB-13 | DEFERRED | **DEFERRED-unchanged** | §3.4 | unchanged |
| RDB-14 | DEFERRED | **DEFERRED-unchanged** | §5 | unchanged |
| RDB-15 | RESOLVED | **PRESERVED** | §7.13 | unchanged |
| RDB-16 | RESOLVED | **PRESERVED** | abstract | unchanged |
| RDB-17 | DEFERRED | **DEFERRED-unchanged** | §9.1 footnote | unchanged |
| RDB-18 | RESOLVED | **PRESERVED** | §10 caption | unchanged |
| RDB-19 | DEFERRED | **DEFERRED-unchanged** | §6.5 acronyms | unchanged |
| RDB-20 | PARTIAL | **PARTIAL-unchanged** | references.bib | bib has grown again (Mythos / Glasswing / Opus 4.7 entries) without an in-paper note about the dual-channel scheme. |
| RDB-21 | CONFIRMED | **CONFIRMED-preserved** | mirror | spot-check at §7.3 / §7.4 / §10 ninth-practice block confirms parity (`paper/main.tex:1683`, `:1775`, `:2822`, `:2837`). |
| RDB-22 | RESOLVED-confirmed | **PRESERVED** | §1.4 | sub-paragraph structure intact |
| RDB-23 | RESOLVED-confirmed | **PRESERVED** | §6.8 | four short sentences intact |
| RDB-24 | NOVEL (positive trace) | **PRESERVED** | §6.8 | unchanged |
| RDB-25 | STRENGTHENED | **PRESERVED** | year-consistency | grep "2021/2022" still 0 matches |
| RDB-26 | DEFERRED | **DEFERRED-unchanged** | §1.4 contribution 5 | parallelism break persists |
| RDB-27 | NEW round-1 | **RESOLVED-confirmed (writer loop-2 `4987d9d`)** | Author's Note `main.md:31`, `:33` | The two ~70-word sentences flagged in round 1 were split. Confirmation: longest sentence in `main.md:31` (paper-mill paragraph) now ~55 words; `main.md:33` was renumbered — the *invitation* paragraph is now at `main.md:39`, where the GitHub-issue-labels sentence runs ~80 words ("An `idea` triggers a research-protocol pass; a `critique` routes to the relevant scrutinizer hand-back; a `provenance-gap` routes to the meta-process case study (§5)."), but the structure is now three short clauses joined by semicolons rather than a single nested-parenthetical run-on. Within rubric for an L-severity entry; not regressed. |
| RDB-28 | NEW round-1 | **RESOLVED-confirmed (writer loop-2 `4987d9d`)** | §3.4 reconstruction `main.md:177–207` | The single ~254-word run-on is gone; replaced by a short lead clause + 4-step nested ordered sub-list + provenance-gap coda paragraph (per the round-1 suggested fix option a). |
| RDB-29 | NOVELTY/HONESTY: ON-POLICY | **PRESERVED + EXTENDED** | Author's Note | extended to cover the new "What surprised me about the assistant" paragraph (RDB-32, below). |

## New defects this round

| ID | Section | Defect class | Severity | Owner | Span (md) | Evidence | Suggested fix |
|----|---------|--------------|----------|-------|-----------|----------|---------------|
| RDB-30 | §7.3 *Asymmetry of collapse* | sentence-length / paragraph-density | **M** | writer | `main.md:491`; `main.tex:1684–1722` | The new Mythos / Glasswing counter-data-point lands as a single ~257-word paragraph of 6 sentences. Two of those sentences cross the 40-word rubric: (a) the "frontier model" capability catalogue runs ~78 words with four em-dashed clauses, and (b) the "Mythos is not yet broadly deployed adversarial capability" sentence runs ~57 words with another em-dashed list of partner organisations. The paragraph is comprehensible but heavy; sentence cadence is "long-medium-long-short", which makes the two long sentences load-bearing for the whole paragraph. | Split (a) at "every major web browser" so the four red-team capability findings become a second sentence keyed on "Specifically:". Split (b) at "Project Glasswing" so the partner-list and the safeguarded-sibling claim become two short sentences. Net effect: 6 → 8 short-medium sentences, paragraph word count unchanged. |
| RDB-31 | §7.4 *Guardrails as band-aid* | hedging-tightness / overclaim risk | **M** | writer | `main.md:504`; `main.tex:1775–1797` | The load-bearing sentence "every guardrail is a classifier, every classifier has a false-negative rate, and any false-negative rate combined with autonomous offensive capability and global proliferation collapses to attacker-side capability over a short enough horizon" carries a soft hedge ("over a short enough horizon") but the chain of three asserted premises plus the conditional collapse reads as a near-deductive claim. Stage 5 cannot find a `[lit-read]` or `[lit-retrieved]` source in `docs/sources.md` that establishes the *quantitative* "false-negative rate × proliferation → attacker-side capability" reduction; the closest comparators are L-VD-1 / L-VD-2 (uplift literature) and L-MYTHOS-1 / -2 (counter-data-point), neither of which states the band-aid argument as a deductive identity. The argument is plausible and the hedge is real, but the rhetorical register ("collapses to") risks being read as proof rather than as engineering intuition. | Tighten the hedge by reframing as engineering intuition rather than deduction: "any non-zero false-negative rate, combined with autonomous offensive capability and global proliferation, *plausibly* converges to attacker-side capability over a short enough horizon — a claim we present as engineering intuition rather than proof, and one the L-MYTHOS evidence base does not yet quantify." Alternatively, route the same hedge into a footnote keyed off "short enough horizon" so the body sentence reads cleanly and the caveat is auditable. |
| RDB-32 | Author's Note *What surprised me about the assistant* | paragraph-density / sentence-length | **L** | writer | `main.md:33`; `main.tex:178–203` | The new sixth Author's-Note paragraph lands at 213 words and 8 sentences. Three sentences cross 40 words: (a) the "expected — and braced for" opening (~50w); (b) the "durable answer is *security by design at the artifact level*" sentence (~46w); (c) the closing "magnitude and frequency of attempts" sentence (~52w). None is comprehension-blocking and the paragraph is the longest in the Author's Note (next is `main.md:23` at 197w / 7 sentences). The new paragraph also adds the *security-by-design* framing twice in the same Author's Note (here and at `main.md:33` end-of-paragraph), which the §7.4 prose then triples; this is rhetorically deliberate (Author's-Note-as-trailer) but Stage 5 flags it for awareness. | Optional, not blocking: split sentence (a) at "or where the session would be flagged or terminated"; split sentence (c) at "in 2026 than it was in 2024". The triple statement of security-by-design across Author's Note / §7.4 / Author's Note closing is on-policy under the Author's-Note-as-trailer convention; Stage 5 endorses retaining it. |
| RDB-33 | §10 ninth practice | novelty-inflation risk | **L** | writer | `main.md:715–717`; `main.tex:2822–2862` | The ninth practice ("Verbatim-string scanning against the assistant's likely training corpus") closes with the line "practice 9 will need to evolve with detection tooling as that tooling matures". This forward-looking promise is uncited; `docs/sources.md` cluster I (L-SLOP-1..12) covers AI-detector / paraphrase-detection literature but the specific *evolution* claim is presented as a free-floating promise rather than a literature-anchored direction. The framing is honest ("a *first cut*", "the plagiarism-safeguard problem in the AI-assisted-writing era is not yet solved") and the "logged for the next iteration of the framework rather than added to Figure 11" hedge at `main.md:715` is the right move. The practice is therefore *not* novelty-inflated — but the closing promise should either be deleted, or anchored to L-SLOP-12 (Pellegrina & Helmy, "AI detectors and AI-assisted error / citation / image-verification tooling are not yet sufficiently accurate or reliable for use in academic assessment"), which is the closest comparator already cited at `main.md:721`. | Replace "evolve with detection tooling as that tooling matures" with "evolve with detection tooling as that tooling matures (cf. L-SLOP-12 on the current accuracy ceiling)" — or delete the closing half-sentence and let the *first-cut* framing carry the load alone. |
| RDB-34 | §10 ninth practice + Figure 11 | structural inconsistency (count mismatch) | **L** | writer | `main.md:704–719`; Figure 11 caption / asset | Eight-row Figure 11 vs nine numbered practices in §10 prose. The mismatch is *deliberately on record* at `main.md:715` ("logged here for the next iteration of the framework rather than added to Figure 11"), which makes the hedge correct under rule 1. But the §10 paragraph at `main.md:704` opens with "Eight integrated practices distinguish this paper" *before* the ninth practice is introduced, so a cold reader hits the Figure 11 callout, counts eight rows, then encounters a ninth. The framing handles this only at `main.md:715`, three paragraphs in. | Add a half-clause to `main.md:704` such as "Eight integrated practices — with a ninth in development, see below — distinguish this paper". This preserves Figure 11's eight-row scope while priming the reader that the prose count exceeds the figure count. Alternatively, move the ninth-practice block to a clearly-set-off "*Looking ahead: a candidate ninth practice*" sub-heading (visually + structurally separated from the eight-row enumeration). |

## Novelty audit — extended for round 2

The new content extends two existing audits and opens one fresh comparator
question:

1. **§7.3 Mythos counter-data-point.** Verdict: **HONEST-COUNTERPOINT**, on-policy.
   The §1.4 software-side asymmetry argument was calibrated against the
   L-VD-1 / L-VD-2 evidence era; §7.3 explicitly names that calibration
   ("the L-VD-1 / L-VD-2 era of evidence … which the §1.4 framing was
   calibrated against") and concedes that the new evidence base
   (L-MYTHOS-1, L-MYTHOS-2, anthropic2026opus47) makes the gap "narrower"
   and the time horizon "shorter". This is the honest move under rule 1
   and it does *not* falsify the asymmetry argument — it tightens its
   scope. Original asymmetry novelty is therefore **sharpened, not
   weakened**: the contribution is now framed as an explicit,
   time-bounded argument rather than as a static claim, and the §7.4
   band-aid framing is the new contribution that the time-bounded scope
   makes available.

2. **§7.4 band-aid framing.** Verdict: **NEW CONTRIBUTION (incremental
   beyond literature).** No `[lit-read]` or `[lit-retrieved]` source in
   `docs/sources.md` clusters A, A.2, B, C frames guardrails-as-band-aid
   in the security-by-design register the §7.4 paragraph adopts. The
   closest comparators are the L-MYTHOS-1 / L-MYTHOS-2 grey-literature
   trace (Anthropic's own framing of safeguards) and the L-VD-1 refused-
   labs evidence base. The §7.4 differential — that guardrails are
   *necessary but structurally insufficient*, and that the durable
   answer is artifact-level security-by-design — is a framing
   contribution, not an empirical one, and is honest about its
   register (engineering intuition; cf. RDB-31 hedge).

3. **§10 ninth practice (verbatim-string scanning).** Verdict:
   **NOT NOVELTY-INFLATED**, on-policy modulo RDB-33. The "first cut"
   framing and the "logged for the next iteration" hedge correctly
   bound the claim. The closing forward-looking promise is the only
   novelty-inflation risk; RDB-33 routes a fix.

## Most consequential defect — round 2

**RDB-31 — the §7.4 band-aid sentence's hedging tightness.** The §7.4
paragraph is the round-2 contribution that most extends the paper's
argument; its load-bearing sentence is the one a critical reader will
test against the literature. The current hedge is real but understated;
the suggested tightening (engineering intuition vs deduction; or
footnote-the-caveat) closes the gap without weakening the contribution.

## Counts by severity (active actionable, post-round-2)

- **H = 0.**
- **M = 13** (RDB-01 [residual], RDB-03, RDB-04, RDB-05, RDB-06, RDB-07,
  RDB-08, RDB-09, RDB-10, RDB-11, RDB-26 [parallelism], RDB-30 NEW,
  RDB-31 NEW).
- **L = 13** (RDB-13, RDB-14, RDB-17, RDB-19, RDB-20, RDB-26 [if mild],
  RDB-32 NEW, RDB-33 NEW, RDB-34 NEW; plus the carry-over L entries
  preserved from round 1).
- **Resolved this round.** 2 (RDB-27, RDB-28 — writer loop-2 `4987d9d`).
- **New this round.** 5 (RDB-30, RDB-31, RDB-32, RDB-33, RDB-34) — 2 M
  and 3 L.

## Caption-fidelity confirmation (writer-flagged from illustrator pass)

Stage 5 confirms the two illustrator-flagged caption tweaks are
**should-do**, not optional:

- **Fig 9 caption** (`paper/main.tex` near `\includegraphics{fig9-...}`)
  should mention 4 literature-track stages now that the
  `[ai-confirmed]` stage was added per the CLAUDE.md ladder
  extension. The current 3-stage caption is a rule-11 honesty
  defect against the now-4-stage figure. Routed to writer as part
  of the next loop.
- **Fig 11 caption** now risks duplicating the redrawn in-figure
  legend ("P (filled disc) = principal mitigation; S (ring) =
  secondary mitigation"). If the caption text duplicates the
  legend, tighten the caption to a one-sentence pointer ("Eight
  integrated practices × three failure-mode axes; see in-figure
  legend.") and let the asset carry the rest. Routed to writer.

Both items are filed as RDB-35 (fig9 caption) and RDB-36 (fig11
caption) in the registry below.

## Re-scrutiny verdict

`RE-SCRUTINY REQUIRED: yes` — five new entries (RDB-30..RDB-34) are
filed against the new §7.3 / §7.4 / §10-ninth-practice prose plus two
caption-tweak items (RDB-35, RDB-36) at L severity. No new H entries.
Two M entries (RDB-30 sentence-length in §7.3, RDB-31 hedge tightness
in §7.4) are non-blocking but should be addressed in the next writer
loop. RDB-04 (§10 list-of-eight vs Figure 11 collapse) remains
deferred and is now *complicated* by the ninth-practice prose
addendum — Stage 5 still endorses option (b) with an explicit
"eight + 1 forward-looking" framing. Re-scrutiny should follow the
next writer pass.
