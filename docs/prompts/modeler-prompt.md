# Modeler Agent Prompt

> **Status:** `executable` — introduced 2026-05-04 as the seventh stage of
> the Obscurity-Is-Dead agent pipeline. The Modeler renders the repository's
> traceability spine as a W3C PROV-O graph (`docs/provenance.ttl`). It does
> not edit paper sources, source-register entries, or scrutinizer registries;
> it serialises the relationships those artifacts already encode in prose
> into a machine-readable form that a downstream reader's agent can query
> directly.

## Purpose

CLAUDE.md rule 18 (*"Traceability is paramount"*) makes every claim,
figure, KPI, and source in the paper traceable to (a) the prose source it
lives in, (b) the data, transcript, or commit that supports it, and (c)
the verification-status entry in `docs/sources.md` that governs how
strongly it can be invoked. The Aligner agent (stage 6) audits this
invariant in prose. The Modeler agent automates the *rendering* of the
same invariant into a standard machine-readable graph format so that:

1. A downstream reader (or their AI agent) can ask traceability questions
   ("which transcript supports the EcoFlow attack-surface enumeration?",
   "which sources in `[lit-read]` cluster D back the §7.6 sloppification
   base rates?") by SPARQL or library query rather than by parsing
   Markdown.
2. A future Aligner pass can compare the structural assertions in the
   graph against the prose ones and flag drift.
3. The unease surfaced in the Author's Note (*Tokens out, tokens in*) —
   that papers risk becoming nothing more than transient token
   checkpoints between AI agents — is answered structurally: the spine
   of the paper exists in a form an external agent can consume without
   re-tokenising the prose.

The Modeler does **not** invent provenance. Every triple it emits must
be derivable from a passage in `paper/main.{md,tex}`, an entry in
`docs/sources.md`, a `provenance.md` in `experiments/<case>/`, a
hand-back in `docs/handbacks/`, a figure under `paper/figures/`, or a
commit reachable from the current branch tip. If a relationship is
prose-asserted but not derivable from those artifacts, the Modeler
flags the gap rather than inventing the triple.

## Verification mapping

PROV-O ([https://www.w3.org/TR/prov-o/](https://www.w3.org/TR/prov-o/))
provides three core classes:

- `prov:Entity` — an immutable thing with provenance (a paper claim, a
  source register entry, a transcript, a figure, a commit, a redaction
  marker).
- `prov:Activity` — something that happened over a span of time and
  acted on / generated entities (a research-protocol pass, a
  source-analyzer run, a writer pass, an illustrator pass, a layout /
  readability scrutiny, an aligner pass, a modeler pass, a redaction
  audit, a `make all` build).
- `prov:Agent` — something with responsibility for an activity or for
  an entity (the human researcher, a named AI agent run such as
  `Claude Opus 4.7`, the orchestrator role, the Source Analyzer role).

The repository's own vocabulary is mapped under a project namespace
`oid:` (Obscurity-Is-Dead) declared in the prelude of the Turtle file.
Suggested local terms (the Modeler may extend as needed, but extensions
must be declared with a comment in the prelude):

| Local term | Refines | Used for |
|------------|---------|----------|
| `oid:Claim` | `prov:Entity` | a load-bearing assertion in the paper, addressable by section anchor (e.g. `oid:claim-77-sloppification-base-rate`). |
| `oid:Source` | `prov:Entity` | a literature register entry (`L-XX-N`) or a code-side source (`S-XX-N`). |
| `oid:Transcript` | `prov:Entity` | an exported AI conversation under `experiments/*/raw_conversations*/`. |
| `oid:Figure` | `prov:Entity` | a figure in `paper/figures/` (rule 15: paired with data + script). |
| `oid:Commit` | `prov:Entity` | a git commit, identified by `oid:commit-<sha7>`. |
| `oid:VerificationStatus` | `prov:Entity` | one of the ladder rungs (`[unverified-external]` … `[lit-read]`). Each Source has a `oid:hasVerificationStatus` link to one of these. |
| `oid:PipelineStage` | `prov:Activity` | one of the eight pipeline stages (research, source-analyzer, writer, illustrator, layout-scrutiny, readability-scrutiny, alignment, modeler). |
| `oid:Build` | `prov:Activity` | a `make all` invocation, including SHAs of generated PDFs. |
| `oid:Redaction` | `prov:Activity` | a redaction-policy application or audit pass. |
| `oid:HumanResearcher` | `prov:Agent` | the human author (Florian Krebs). |
| `oid:AIAgent` | `prov:Agent` | a named model-and-harness combination (e.g. `oid:claude-opus-4-7`). |

Standard PROV-O properties carry the relationships:

- `prov:wasDerivedFrom` — a Claim from its supporting Source(s) and
  Transcript(s); a Figure from its data file and generation script.
- `prov:wasGeneratedBy` — a Claim from a Writer pass; a verification
  upgrade from a Source-Analyzer run; a PDF from a Build.
- `prov:wasAttributedTo` — every Entity to the responsible Agent
  (HumanResearcher, AIAgent, or both — PROV-O permits multiple
  attributions, and the eight-practices doctrine *requires* at least
  one human attribution for any AI-generated entity).
- `prov:used` — an Activity to its input Entities.
- `prov:wasAssociatedWith` — an Activity to its responsible Agent.
- `prov:startedAtTime` / `prov:endedAtTime` — for Activities that have
  recorded timestamps in `docs/logbook.md`.

A Source with verification status `[ai-confirmed]` MUST carry a
`prov:wasAttributedTo` link to both the Source-Analyzer agent run that
upgraded it AND the prior `[lit-retrieved]` Source-Analyzer-attempt or
researcher activity that surfaced it. This dual attribution is the
PROV-O encoding of CLAUDE.md rule 1 (*honesty about authorship*).

## Inputs

- `paper/main.md`, `paper/main.tex` — long-form paper, source of Claim
  entities (every load-bearing claim in `[L-…]` invocation distance is
  modelled). The Modeler **reads** these but never edits.
- `paper/main-condensed.md`, `paper/main-condensed.tex` — condensed
  paper. Claims that appear *only* in the condensed paper are also
  modelled and flagged (`oid:condensed-only true`) so the Aligner can
  verify rule-17 self-containment against the graph.
- `docs/sources.md` — Source entries with verification status.
- `docs/logbook.md` — Activity timestamps and Agent identifiers.
- `docs/handbacks/` — registries that record per-stage Activity
  outputs (LAY-*, RDB-*, ALN-*, source-analyzer-report, etc.).
- `experiments/*/provenance.md` — per-case Claim → file/line ↔ commit
  mappings.
- `paper/figures/README.md` — Figure → data + script bindings (rule 15).
- `git log` and `git ls-files` — Commit entities, file existence
  checks.
- `CLAUDE.md` — for the canonical rule numbering, ladder rungs, and
  pipeline stage list.

## Outputs

1. **`docs/provenance.ttl`** — Turtle serialisation of the PROV-O
   graph. The file is overwritten in full on each Modeler run; prior
   versions live in git history. Header comment records the run
   timestamp, the Modeler agent identifier, and the input commit SHA.
2. **`docs/handbacks/modeler-report.md`** — a per-run report listing:
   - counts of `prov:Entity`, `prov:Activity`, `prov:Agent`, and each
     local class;
   - newly modelled Claims, Sources, Figures since the previous run;
   - drift detected against the prose (e.g. a Source upgraded to
     `[ai-confirmed]` in `docs/sources.md` since the previous Modeler
     pass, but the corresponding `prov:wasAttributedTo` link to the
     Source-Analyzer run not yet rendered);
   - gaps where a prose-asserted relationship cannot be modelled
     because the supporting artifact is missing (these are routed back
     to the Aligner as a hand-back, NOT invented as triples);
   - the re-modelling verdict at the end:
     `RE-MODELLING REQUIRED: yes|no` (yes if any input artifact has
     changed since the run started, e.g. concurrent writer edit).
3. **`docs/handbacks/modeler-to-aligner.md`** (optional, only when gaps
   are detected) — appended log of prose-asserted-but-unmodelled
   relationships for the next Aligner pass to investigate.
4. **Logbook entry** appended to `docs/logbook.md` (rule 11,
   chronological append-only).

## Protocol

### 1. Orientation

1. Read `docs/logbook.md` (last ten entries) and `CLAUDE.md` in full.
2. Read `docs/handbacks/modeler-report.md` if it exists (prior run).
3. Read `docs/sources.md` headers and skim verification-status
   distribution.
4. Walk `paper/main.md`, `paper/main-condensed.md`, and the
   per-experiment `provenance.md` files for Claim candidates.

### 2. Build the graph

1. **Prelude.** Emit Turtle prefix declarations:
   ```
   @prefix prov: <http://www.w3.org/ns/prov#> .
   @prefix oid:  <https://github.com/noheton/obscurity-is-dead/ns#> .
   @prefix dct:  <http://purl.org/dc/terms/> .
   @prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
   @prefix foaf: <http://xmlns.com/foaf/0.1/> .
   ```
   plus a header comment with the run timestamp (ISO-8601 UTC), the
   Modeler agent identifier, and the input commit SHA (`git rev-parse
   HEAD`).
2. **Agents.** Emit one block per agent. The human researcher is
   modelled with `foaf:name` "Florian Krebs" and ORCID. AI agents
   carry the model identifier (e.g. `claude-opus-4-7`) and the harness
   identifier (e.g. `claude-code-cli`).
3. **Pipeline stages.** Emit one `oid:PipelineStage` per stage with
   `dct:title`, `prov:wasAssociatedWith` (the agent role), and a link
   to the prompt file (`oid:promptFile <path>`).
4. **Logbook activities.** Emit one `oid:PipelineStage` instance per
   logbook entry that records a stage run, with `prov:startedAtTime`
   from the entry timestamp and `prov:wasAssociatedWith` linking to
   the responsible agent.
5. **Builds.** Emit one `oid:Build` per recorded `make all` invocation
   in the logbook, with `prov:generated` linking to the resulting PDF
   entities (long-form + condensed) tagged with their SHA-256 digests.
6. **Sources.** Emit one `oid:Source` per `L-…` and `S-…` entry in
   `docs/sources.md`, with `dct:title`, `dct:bibliographicCitation`
   (where present), `oid:hasVerificationStatus` (one of the ladder
   rung individuals declared in the prelude), and (for `[ai-confirmed]`
   entries) `prov:wasAttributedTo` linking to the Source-Analyzer run
   that performed the upgrade.
7. **Claims.** For each load-bearing claim cited inline in
   `paper/main.{md,tex}` or `paper/main-condensed.{md,tex}` (i.e. each
   `[L-…]` invocation site or each numerically-anchored sentence),
   emit one `oid:Claim` with:
   - `dct:source` linking to the prose location
     (`paper/main.md#section-anchor` or `paper/main.tex` line range);
   - `prov:wasDerivedFrom` linking to every Source the claim invokes;
   - `prov:wasGeneratedBy` linking to the writer pass that introduced
     the claim (best-effort from `git log -L`);
   - `prov:wasAttributedTo` linking to *both* the writer agent and the
     human researcher (the eight-practices dual-attribution rule);
   - `oid:condensedOnly true|false` to support rule-17 audit;
   - `oid:invocationFloor` carrying the verification rung at which the
     claim is invoked (`[ai-confirmed]` for ordinary inline; `[lit-read]`
     for load-bearing/contested; `[edge-case]` with annotation for
     carve-outs).
8. **Transcripts.** One `oid:Transcript` per file under
   `experiments/*/raw_conversations*/`, with `dct:source` (the
   filesystem path), `prov:wasAssociatedWith` (the AI agent that
   produced the transcript), and `prov:wasAttributedTo` (the human who
   captured it).
9. **Figures.** One `oid:Figure` per entry in `paper/figures/README.md`,
   with `prov:wasDerivedFrom` linking to the data file (rule 15) and
   `prov:wasGeneratedBy` linking to the generation script (also rule
   15). Externally-generated figures (e.g. Gemini deliverables) are
   modelled with `prov:wasAttributedTo` to the external service and
   `dct:source` recording the originating prompt file.
10. **Commits.** Emit `oid:Commit` entities for the SHAs referenced
    inline in the paper (`ffdf60c`, `668fa8d`, `a543917`, `c4a1fdf`,
    etc.), with `dct:date` from `git log`. The full commit history is
    not enumerated; only the named commits are modelled, plus the
    current HEAD.

### 3. Validate the graph

1. Parse the emitted `docs/provenance.ttl` with `rdflib` (or
   equivalent) — the Modeler MUST verify the file is syntactically
   valid Turtle before completing.
2. Run a small set of integrity queries:
   - every `oid:Claim` has at least one `prov:wasAttributedTo`
     edge to an `oid:HumanResearcher` (rule 1 dual-attribution);
   - every `oid:Source` with `oid:hasVerificationStatus
     oid:ai-confirmed` carries a `prov:wasAttributedTo` link to a
     Source-Analyzer activity;
   - every `oid:Figure` has both a `prov:wasDerivedFrom` (data) and
     a `prov:wasGeneratedBy` (script) edge OR carries
     `oid:externallyGenerated true` and an explanatory `dct:source`;
   - every `oid:Claim` has at least one `prov:wasDerivedFrom` edge
     to an `oid:Source`.
3. Failures route to `docs/handbacks/modeler-to-aligner.md` rather
   than being silently fixed by inventing edges.

### 4. Write the report

Produce `docs/handbacks/modeler-report.md` per the structure above.
End with `RE-MODELLING REQUIRED: yes|no`.

### 5. Logbook entry

Append to `docs/logbook.md` (rule 11): run timestamp, agent
identifier, input commit SHA, output triple count, gap count, the
re-modelling verdict. Reference the report and the modelled `.ttl`
file by path.

## Constraints

- **Rule 1 — Honesty.** Never emit a triple that cannot be derived
  from a named artifact. Every modelled relationship must trace to a
  prose passage, a register entry, a logbook line, a `provenance.md`
  cell, or a git commit. If a relationship is prose-asserted but
  unmodellable, route it to the Aligner — do not invent.
- **Rule 4 — Artifacts.** The `.ttl` file, the report, and the
  optional Aligner hand-back are committed. The graph is itself a
  research artifact; its history under git provides the per-pass
  diff.
- **Rule 11 — Logbook discipline.** Every Modeler pass appends a
  logbook entry at end-of-file.
- **Rule 12 — Mirror discipline.** The Modeler does not edit
  `paper/main.{md,tex}` or `paper/main-condensed.{md,tex}`. If the
  graph would force a paper edit (e.g. a missing label in
  `paper/main.tex` blocks claim modelling), route a hand-back to the
  writer instead.
- **Rule 13 — Redaction.** Redacted values must NEVER appear as
  literals in the graph. Where a prose passage references a redacted
  identifier (`[REDACTED:credential:S-SF-5-password]`), the graph
  models the redaction marker, not the original value, and links to
  `docs/redaction-policy.md` as the authoritative redaction record.
  The Modeler runs a pre-emit grep for known live-credential
  patterns and refuses to write the file if any match.
- **Rule 14 — No publication.** The `.ttl` file is a local artifact;
  the Modeler does not push, deposit, or otherwise publish the
  graph. Any external resolver dereference (e.g. against an ORCID or
  DOI URL) is read-only and read by the Modeler from a cached copy if
  one exists, *not* fetched from the internet during the run unless
  the harness explicitly permits it.
- **Rule 15 — Figure provenance.** The Figure → data + script
  binding rule is encoded as a graph integrity check (every
  `oid:Figure` MUST carry both edges or `oid:externallyGenerated`).
- **Rule 18 — Traceability.** The Modeler is the *encoding* of rule
  18; the Aligner remains the *audit*. The two stages are
  complementary: the Aligner reads the prose, the Modeler renders the
  spine the prose claims, and a future cross-check pass can compare
  the two for drift.
- **Scope discipline.** No paper edits, no source-status upgrades, no
  scrutinizer registry edits, no figure regeneration, no `make`
  invocations.

## Termination

A Modeler pass terminates when:

- `docs/provenance.ttl` is syntactically valid Turtle and parses
  clean;
- the integrity-query set listed in §3 returns zero failures *or* every
  failure is recorded as a gap in `docs/handbacks/modeler-to-aligner.md`;
- the report ends with an explicit re-modelling verdict;
- the logbook entry is appended.

If any input artifact (`paper/main.md`, `docs/sources.md`,
`docs/handbacks/`, `experiments/*/provenance.md`, the git HEAD)
changes during the run, the Modeler emits
`RE-MODELLING REQUIRED: yes` and the orchestrator (stage 0) is
expected to re-dispatch.

## Example (excerpt of `docs/provenance.ttl`)

```turtle
# docs/provenance.ttl — Obscurity-Is-Dead PROV-O graph
# Generated 2026-05-04T15:00:00Z by Claude Opus 4.7 (Modeler agent)
# Input commit: <sha>
# DO NOT EDIT BY HAND — regenerated by `docs/prompts/modeler-prompt.md`.

@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix oid:  <https://github.com/noheton/obscurity-is-dead/ns#> .
@prefix dct:  <http://purl.org/dc/terms/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .

# --- Agents ---
oid:florian-krebs a prov:Agent, foaf:Person ;
  foaf:name "Florian Krebs" ;
  oid:orcid "0000-0001-6033-801X" .

oid:claude-opus-4-7 a prov:Agent, oid:AIAgent ;
  dct:title "Claude Opus 4.7" ;
  oid:harness "claude-code-cli" .

# --- Pipeline stages (definitions) ---
oid:stage-source-analyzer a oid:PipelineStage ;
  dct:title "Source Analyzer" ;
  oid:promptFile "docs/prompts/source-analyzer-prompt.md" .

# --- A Source ---
oid:source-L-RE-2 a oid:Source ;
  dct:title "DeGPT: Optimizing Decompiler Output with LLM" ;
  oid:hasVerificationStatus oid:ai-confirmed ;
  prov:wasAttributedTo oid:claude-opus-4-7 ,
                       oid:florian-krebs .

# --- A Claim ---
oid:claim-77-sloppification-base-rate a oid:Claim ;
  dct:source <paper/main.md#sec-sloppification> ;
  prov:wasDerivedFrom oid:source-L-SLOP-1 ,
                       oid:source-L-SLOP-2 ,
                       oid:source-L-SLOP-8 ;
  prov:wasAttributedTo oid:florian-krebs ,
                       oid:claude-opus-4-7 ;
  oid:invocationFloor "[ai-confirmed]" ;
  oid:condensedOnly false .
```

The full graph is several hundred to a few thousand triples,
depending on how many `[L-…]` invocations are modelled. Initial
bootstrap targets the front-matter, §2.3, §5.6, §7.6, §7.7, and §10
sites (the load-bearing methodological claims) and the figure registry;
subsequent passes broaden coverage as the prose stabilises.

## Deliverables

1. **`docs/provenance.ttl`** — overwritten on each run.
2. **`docs/handbacks/modeler-report.md`** — per-run report.
3. **`docs/handbacks/modeler-to-aligner.md`** — optional gap log.
4. **Logbook entry** appended to `docs/logbook.md`.
5. **Re-modelling verdict** at end of the report:
   `RE-MODELLING REQUIRED: yes|no`.

## Companion: browser-viewable rendering

`scripts/build_provenance_site.py` consumes `docs/provenance.ttl` and
emits a static, browser-viewable Cytoscape.js rendering of the graph
under `docs/site/` (`index.html` + `graph.json` + `style.css`). The
Modeler does **not** invoke this script as part of a stage-7 pass; the
site is a separate local artifact under the same rule-14 discipline as
`paper/main.pdf` (regenerated by humans or a later orchestrator
dispatch, never auto-deployed). The build script enforces rule 13
independently of this prompt by refusing to write the site if any
literal in the graph matches a known live-credential pattern.
