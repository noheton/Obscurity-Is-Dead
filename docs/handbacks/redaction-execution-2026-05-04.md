# Hand-back: redaction-execution pass — 2026-05-04

**Agent:** Claude Opus 4.7 (redaction-execution sub-agent).
**Branch:** `claude/check-illustration-pipeline-Jqst3`.
**Authoritative spec:** the orchestrator dispatch dated 2026-05-04
authorising actions 1–8 on top of `docs/redaction-audit-2026-05-03.md`.
**Authority boundary:** working-tree edits only; no history rewrite was
executed (per CLAUDE.md rule 13). The history-rewrite *plan* is
committed at `docs/git-history-rewrite-plan.md`.

---

## What was done

### 1. Paper text leaks (R-AUDIT-05) — already executed pre-pass
Action 1 was already committed before this pass started, in commit
`8c2fec4` ("redact: paper-text leaks of SF-IMPL-2/3 repo names").
Verified: no remaining `[REDACTED:repo-path:SF-IMPL-2]` / `[REDACTED:repo-path:SF-IMPL-3]`
display strings in `paper/main.{md,tex}` outside bib citekeys.

### 2. Handback leak (R-AUDIT-06) — committed
`docs/handbacks/readability-to-writer.md:200`: `[REDACTED:repo-path:BALBOA-UPSTREAM-2]` →
`[REDACTED:repo-path:BALBOA-UPSTREAM-2]`. Commit `3aca873`.

### 3. Third-party PII (R-AUDIT-08a) — committed
`paper/figures/dlr-design-system/project/ui_kits/python_plots/UPSTREAM_README.md:38`:
` | ` line stripped; replaced with a
one-line HTML-comment note pointing to `docs/redaction-policy.md`
(R-AUDIT-08a). Commit `23a0f1d`.

### 4. EcoFlow PowerOcean serials + owner-name clarification (R-AUDIT-01a) — committed
The four serials in `experiments/ecoflow-powerocean/original/doc/equipment.md`,
`…/doc/implementation.md`, and `…/custom_components/powerocean_dev/switch.py`
are replaced with `[REDACTED:serial:R-EF-1..R-EF-4]` (consistent
mapping). Householder name `Florian Krebs` retained with parenthetical
clarification `(paper author / device owner-of-record)`. Commit
`4697f1c`. Register entries `R-EF-1..R-EF-4` added to
`docs/redaction-policy.md` in commit `ac20649`.

### 5. Logbook handles (R-AUDIT-07) — committed
Every occurrence of the six community-implementer handles and
repo-paths in `docs/logbook.md` replaced with the policy markers. Bib
citekey forms (`smurfy_esphome_sf`, `p0rigth_spiderblebridge`,
`pythonspidercontroller`, `niltrip_powerocean`) preserved as
policy-permitted internal identifiers. Commit `82741be`. Logbook
handling decision documented in policy in commit `ac20649`.

Per-handle replacement counts (script output):
- `[REDACTED:maintainer-handle:SF-IMPL-1]`: 1
- `[REDACTED:maintainer-handle:SF-IMPL-2]`: 1
- `[REDACTED:maintainer-handle:EF-IMPL-1]`: 1
- `[REDACTED:maintainer-handle:BALBOA-UPSTREAM-1]`: 2
- `[REDACTED:maintainer-handle:BALBOA-UPSTREAM-2]`: 2
(plus all `owner/repo` and CamelCase forms via literal-string pass)

### 6. Policy-level carve-outs (R-AUDIT-04, -08b, -09, -10, -11, -12) — committed
Documented in `docs/redaction-policy.md` "Policy carve-outs" section
(commit `ac20649`). One paper-text edit:
- `paper/main.md` §9.5 + `paper/main.tex` §9.5: one new sentence
  clarifying that the author's DLR e-mail `florian.krebs@dlr.de` is a
  "contact channel, not institutional endorsement". Commit `56c1f84`,
  rule-11 mirror enforced.

### 7. New marker types — committed
Added `owner`, `contact`, `internal-url`, `hostname` to the marker-type
table in `docs/redaction-policy.md`. Commit `ac20649`.

### 8. History-rewrite plan — committed (NOT EXECUTED)
- Updated the "History rewrite checklist" in
  `docs/redaction-policy.md` to add H-09 (EcoFlow serials) and H-10
  (`` + landline) to the H-01..H-08 already on file.
- Created the new file `docs/git-history-rewrite-plan.md` containing:
  - the exact `git-filter-repo --replace-text replacements.txt`
    command,
  - a templated `replacements.txt` body with H-01..H-10 patterns,
  - substring-collision warnings for bib citekeys (regex with
    word-boundary lookarounds for `[REDACTED:maintainer-handle:SF-IMPL-1]`, `[REDACTED:maintainer-handle:EF-IMPL-1]`, `[REDACTED:maintainer-handle:BALBOA-UPSTREAM-1]`,
    `[REDACTED:maintainer-handle:BALBOA-UPSTREAM-2]`),
  - the explicit carve-out for the bare lowercase `pythonspidercontroller`
    citekey (only the CamelCase form is rewritten),
  - a pre-flight checklist (clone-mirror, dry-run, verify markers,
    force-push to fresh public repo not the existing one, shred local
    `replacements.txt`),
  - a prominent "DO NOT EXECUTE" notice deferring to CLAUDE.md rule 13.
- Commit `1b02ccb`.

---

## Verification (rule-11 + redaction-marker discipline)

- `make -C paper pdf` → exit 0; output `paper/main.pdf` 57 pages,
  1,250,221 bytes. Only routine `Underfull \hbox` warnings inside the
  bib `note` fields and one `\paragraph` in the new content (consistent
  with prior REDACTED-marker hyphenation behaviour). No `Overfull
  \hbox`, no undefined references, no missing citations.
- `git grep -n -E '([REDACTED:maintainer-handle:SF-IMPL-1]|[REDACTED:maintainer-handle:SF-IMPL-2]|pythonspidercontroller|[REDACTED:maintainer-handle:EF-IMPL-1]|[REDACTED:maintainer-handle:BALBOA-UPSTREAM-1]|[REDACTED:maintainer-handle:BALBOA-UPSTREAM-2]|jan\.wagner@dlr\.de|[REDACTED:serial:R-EF-1]|[REDACTED:serial:R-EF-2]|[REDACTED:serial:R-EF-3]|[REDACTED:serial:R-EF-4])'`:
  remaining matches are all in policy-permitted contexts:
  - Bibliography citekeys (`@smurfy_esphome_sf`,
    `\citep{niltrip_powerocean}`, etc.) in `paper/main.{md,tex}` and
    `paper/references.bib`.
  - Policy-register entries in `docs/redaction-policy.md`.
  - Audit report (read-only historical) in
    `docs/redaction-audit-2026-05-03.md`.
  - The new history-rewrite plan in `docs/git-history-rewrite-plan.md`
    (where the raw H-09 / H-10 patterns must appear so the filter run
    can pick them up).
  - **Out-of-scope research artifacts** (see §"What was deliberately
    left for the human" below).
- `git grep -n '\[REDACTED:'` shows all new markers present; spot-check
  confirms they all map to a policy register entry or carve-out:
  - `[REDACTED:serial:R-EF-1..R-EF-4]` → register entries R-EF-1..R-EF-4.
  - `[REDACTED:repo-path:SF-IMPL-1..3]`, `[REDACTED:maintainer-handle:*]`
    → policy "Community-implementer anonymisation" table.
  - The four new policy types (`owner`, `contact`, `internal-url`,
    `hostname`) are all in the marker-type table.
- Rule 11 (`paper/main.md` ↔ `paper/main.tex` consistency): the only
  paper edit in this pass is the one-sentence §9.5 cross-reference;
  mirrored in both surfaces in commit `56c1f84`.

---

## What was deliberately left for the human

These items are **outside the scope** of the current redaction-execution
authorisation and require human consent / further authorisation before
action.

### Items requiring history rewrite (rule 13 gate)
The full git-history rewrite per `docs/git-history-rewrite-plan.md` —
including the H-07 / H-08 raw values for Spider Farmer credentials,
serial, IP, and UID, which are intentionally not in any committed file.
The author must paste those values into a local `replacements.txt`
working copy at run time and `shred(1)` it after the rewrite.

### Items requiring upstream-repo work (R-AUDIT-11)
Per the human decision recorded in the dispatch, the
author-controlled upstreams `noheton/spider_farmer` and
`noheton/powerocean-dev` will be made public alongside the main repo.
This pass had **no local clones of those upstreams** in its working
tree. Each upstream needs its own redaction pass for the same `R-SF-*`
(credentials, serial, IP, UID) and `R-EF-*` (serials) patterns
documented in `docs/redaction-policy.md`. This is left as a TODO for
the upstream-publish step and is recorded in the
"Pre-publication checklist" in the policy.

### Items requiring author knowledge (R-AUDIT-12 follow-up)
The audit flagged that the `iot.controlmyspa.com/idm/tokenEndpoint`
section of the paper cites a vendor cloud endpoint whose response
includes a `mobileClientSecret`. The redaction-execution agent
verified that **no literal `client_secret` value appears in the
working tree** (the only match is an empty placeholder in
`experiments/iot-integrator-ondilo-ico-spa-v2/integration/smoke-test.py:89`)
and that `git log --all -S 'client_secret' --oneline` /
`git log --all -S 'clientSecret' --oneline` return only the audit
commit and unrelated documentation commits. The agent could not
derive the canonical Cognito-client-secret string fragment without
seeing the actual value. The human author should run a final
`git log --all -S '<actual-fragment>'` against the literal value
before the public-mirror gate; the result should be documented in
`docs/redaction-policy.md` under the R-AUDIT-12 carve-out (the
section already references this open task).

### Items left as research-artifact carve-outs
The following raw handles still appear in **research artifacts** that
were explicitly out of scope for this redaction pass:

- `experiments/iot-integrator-balboa-gateway-ultra/**` — REPORTs,
  RESEARCH-PROTOCOL, integration READMEs, phase-1 / phase-2 / phase-3
  notes, smoke-test.py, provenance.md (contain `[REDACTED:repo-path:BALBOA-UPSTREAM-2]`,
  `[REDACTED:repo-path:BALBOA-UPSTREAM-1]`).
- `experiments/ecoflow-powerocean/provenance.md` (`[REDACTED:repo-path:EF-IMPL-1]`).
- `experiments/ecoflow-powerocean/raw_conversations (copy&paste, web)/`
  (research-transcript, rule-4 carve-out).
- `experiments/spider-farmer/raw_conversations (copy&paste, web)/`
  (rule-4 carve-out — never opened by this agent to avoid pulling raw
  credentials into context).
- `docs/handbacks/layout-scrutiny-2026-05-03-build.md`,
  `docs/handbacks/research-protocol-powerocean-resync-2026-05-03.md`,
  `docs/handbacks/writer-pass-2026-05-03-loop3.md` — bib-citekey
  references plus a few raw `[REDACTED:repo-path:EF-IMPL-1]` / `[REDACTED:maintainer-handle:EF-IMPL-1]` mentions
  in the research-protocol resync handback.

The original `paper/redaction-policy.md` "Out of scope" carve-out for
the 2026-05-03 anonymisation pass already lists `experiments/`,
`docs/handbacks/`, and `docs/prompts/` as out of scope. The current
pass did not extend that boundary; the dispatch for action 5
explicitly limited the in-place handle redaction to `docs/logbook.md`.
**If the public-mirror policy decides the experiments and handbacks
should also ship redacted, a follow-up redaction pass is needed.**
The history-rewrite plan in `docs/git-history-rewrite-plan.md`
already covers these strings byte-for-byte across the entire history,
so a public-mirror push *after* the rewrite would scrub them
automatically — at the cost of changing the rendered narrative inside
those files.

### Cosmetic follow-ups
- Layout: the new §9.5 cross-reference produces one extra
  `Underfull \hbox` warning in the rendered PDF (the long
  `\texttt{florian.krebs@dlr.de}` token does not hyphenate). Stage 4
  may want to confirm.
- Logbook readability: in-place redaction in `docs/logbook.md`
  produces several adjacent REDACTED markers in the §2026-05-03 entry
  describing the original anonymisation pass. The marker density is
  high but the narrative remains decodable via
  `docs/redaction-policy.md` "Community-implementer anonymisation"
  table. No fix required; flagged for visibility.

---

## Commit chain produced by this pass

| Commit | Description |
|--------|-------------|
| `8c2fec4` | (pre-existing) Action 1: paper text leaks (R-AUDIT-05). |
| `3aca873` | Action 2: handback `[REDACTED:repo-path:BALBOA-UPSTREAM-2]` (R-AUDIT-06). |
| `23a0f1d` | Action 3: strip third-party DLR contact info (R-AUDIT-08a). |
| `4697f1c` | Action 4: EcoFlow serials + owner-name clarification (R-AUDIT-01a). |
| `82741be` | Action 5: logbook in-place handle redaction (R-AUDIT-07). |
| `56c1f84` | Action 6 paper-edit: §9.5 DLR-email cross-reference (R-AUDIT-08b). |
| `ac20649` | Actions 4-register / 5-policy-decision / 6-carve-outs / 7-new-types / 8-checklist consolidated into `docs/redaction-policy.md`. |
| `1b02ccb` | Action 8: new file `docs/git-history-rewrite-plan.md` (DO NOT EXECUTE). |

Push to `claude/check-illustration-pipeline-Jqst3` is performed at the
end of this hand-back; **no PR is opened** per the dispatch.

---

*Hand-back filed 2026-05-04 by the redaction-execution agent (Claude
Opus 4.7).*
