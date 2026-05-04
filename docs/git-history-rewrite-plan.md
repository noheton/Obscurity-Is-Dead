# Git history rewrite plan (pre-publication)

> **STATUS — EXECUTED 2026-05-04.** Florian Krebs granted explicit
> consent on the `claude/history-rewrite-daDxQ` branch ("backup of
> the repo. this is explicit consent"). The plan below is preserved
> verbatim as the executed specification; post-execution deviations
> and gap-fills are recorded in the new "Execution record" section
> at the bottom of this file. The rewrite tip carries the annotated
> tag `pre-publication-clean`. The public-mirror push and the
> Zenodo / arXiv submission steps remain gated on a separate explicit
> consent per CLAUDE.md rule 13.

This plan operationalises the "History rewrite checklist" in
`docs/redaction-policy.md`. It uses
[`git-filter-repo`](https://github.com/newren/git-filter-repo) (preferred
over BFG because it supports literal-string `--replace-text`
substitution with byte-for-byte fidelity).

---

## 1. Scope

The rewrite covers patterns **H-01..H-10** from the redaction policy.
Each pattern maps to a per-line entry in `replacements.txt`. The
`literal:` prefix instructs `git-filter-repo` to do an exact-byte
substring match (no regex), which is what we want for handles, repo
paths, serials, and contact info.

| ID | Pattern (raw → marker) |
|----|-------------------------|
| H-01a | `[REDACTED:repo-path:SF-IMPL-1]` → `[REDACTED:repo-path:SF-IMPL-1]` |
| H-01b | `[REDACTED:maintainer-handle:SF-IMPL-1]` → `[REDACTED:maintainer-handle:SF-IMPL-1]` *(applied AFTER H-01a; see §2)* |
| H-02a | `[REDACTED:repo-path:SF-IMPL-2]` → `[REDACTED:repo-path:SF-IMPL-2]` |
| H-02b | `[REDACTED:maintainer-handle:SF-IMPL-2]` → `[REDACTED:maintainer-handle:SF-IMPL-2]` |
| H-02c | `[REDACTED:repo-path:SF-IMPL-2]` → `[REDACTED:repo-path:SF-IMPL-2]` |
| H-03a | `[REDACTED:repo-path:SF-IMPL-3]` → `[REDACTED:repo-path:SF-IMPL-3]` |
| H-03b | `pythonspidercontroller` → *(see §2 — bib-citekey carve-out, leave as-is)* |
| H-04a | `[REDACTED:repo-path:EF-IMPL-1]` → `[REDACTED:repo-path:EF-IMPL-1]` |
| H-04b | `[REDACTED:maintainer-handle:EF-IMPL-1]` → `[REDACTED:maintainer-handle:EF-IMPL-1]` |
| H-05a | `[REDACTED:repo-path:BALBOA-UPSTREAM-1]` → `[REDACTED:repo-path:BALBOA-UPSTREAM-1]` |
| H-05b | `[REDACTED:maintainer-handle:BALBOA-UPSTREAM-1]` → `[REDACTED:maintainer-handle:BALBOA-UPSTREAM-1]` |
| H-06a | `[REDACTED:repo-path:BALBOA-UPSTREAM-2]` → `[REDACTED:repo-path:BALBOA-UPSTREAM-2]` |
| H-06b | `[REDACTED:maintainer-handle:BALBOA-UPSTREAM-2]` → `[REDACTED:maintainer-handle:BALBOA-UPSTREAM-2]` |
| H-07a | *(Spider Farmer raw MQTT username — value redacted from this plan; pull from policy R-SF-1 at execution time)* |
| H-07b | *(Spider Farmer raw MQTT password — value redacted from this plan; pull from policy R-SF-2)* |
| H-08a | *(Spider Farmer device serial — value redacted from this plan; pull from policy R-SF-3)* |
| H-08b | *(Spider Farmer broker / device IP — value redacted from this plan; pull from policy R-SF-4)* |
| H-08c | *(Spider Farmer vendor UID — value redacted from this plan; pull from policy R-SF-5)* |
| H-09a | `[REDACTED:serial:R-EF-1]` → `[REDACTED:serial:R-EF-1]` |
| H-09b | `[REDACTED:serial:R-EF-2]` → `[REDACTED:serial:R-EF-2]` |
| H-09c | `[REDACTED:serial:R-EF-3]` → `[REDACTED:serial:R-EF-3]` |
| H-09d | `[REDACTED:serial:R-EF-4]` → `[REDACTED:serial:R-EF-4]` |
| H-10a | `` → *(strip — replace with empty string)* |
| H-10b | `` → *(strip — replace with empty string)* |

The R-SF-1..R-SF-5 raw values are intentionally **not** included
inline here so that this plan file itself can ship in the public
mirror after the rewrite. The author must paste the raw values into
the local working copy of `replacements.txt` immediately before running
the filter, then `shred(1)` that working copy after the rewrite.

## 2. Substring-collision warnings

`git-filter-repo --replace-text` is byte-substring; it does not respect
word boundaries. The following collisions must be guarded against by
ordering the replacement file correctly (longest pattern first) and by
the manual carve-outs noted below.

- **`smurfy_esphome_sf`** (bib citekey) contains `[REDACTED:maintainer-handle:SF-IMPL-1]`. Run H-01a
  before H-01b; verify post-rewrite that the citekey survived.
  `[REDACTED:maintainer-handle:SF-IMPL-1]` standalone after H-01a should only match the maintainer
  handle.
- **`p0rigth_spiderblebridge`** (bib citekey) contains `p0rigth` (note:
  no `-dev`). H-02b only fires on `[REDACTED:maintainer-handle:SF-IMPL-2]`, so the citekey is safe
  by construction. Verify post-rewrite.
- **`niltrip_powerocean`** (bib citekey) contains `[REDACTED:maintainer-handle:EF-IMPL-1]`. Run H-04a
  before H-04b. Post-rewrite, the citekey will read
  `niltrip_powerocean` only if H-04b is applied with a word-boundary
  guard. **`git-filter-repo --replace-text` cannot enforce word
  boundaries**; therefore H-04b must be implemented as a *regex*
  replacement instead, e.g. `regex:(?<![A-Za-z0-9_])[REDACTED:maintainer-handle:EF-IMPL-1](?![A-Za-z0-9_/-])==>[REDACTED:maintainer-handle:EF-IMPL-1]`.
  The same applies to H-01b (`[REDACTED:maintainer-handle:SF-IMPL-1]`) and H-05b (`[REDACTED:maintainer-handle:BALBOA-UPSTREAM-1]`).
  H-02b (`[REDACTED:maintainer-handle:SF-IMPL-2]`) is safe as-is because the hyphen prevents
  citekey collision.
- **`pythonspidercontroller`** (bib citekey) is identical to the
  display form. The redaction-execution pass deliberately preserved
  the bare lowercase form as a citekey (see policy line discussing
  H-03 carve-out). Therefore **do not include H-03b in the
  replacement file**: only H-03a (CamelCase `[REDACTED:repo-path:SF-IMPL-3]`)
  needs rewriting in history. Verify post-rewrite that the citekey
  references in `paper/references.bib` and `paper/main.{md,tex}`
  Pandoc/`\citep{}` calls (`@pythonspidercontroller`,
  `\citep{pythonspidercontroller}`) still resolve.
- **`[REDACTED:maintainer-handle:BALBOA-UPSTREAM-2]`** is short and risks collisions in URLs / bib metadata.
  Pre-flight grep before running H-06b: `git grep -n '[REDACTED:maintainer-handle:BALBOA-UPSTREAM-2]' | grep -v
  '[REDACTED:repo-path:BALBOA-UPSTREAM-2]'` to confirm no other contexts. As of 2026-05-04
  no such collision exists, but re-verify before running.

## 3. `replacements.txt` template

```text
***REMOVED***
***REMOVED***

***REMOVED***
literal:[REDACTED:repo-path:SF-IMPL-1]==>[REDACTED:repo-path:SF-IMPL-1]
regex:(?<![A-Za-z0-9_])[REDACTED:maintainer-handle:SF-IMPL-1](?![A-Za-z0-9_/-])==>[REDACTED:maintainer-handle:SF-IMPL-1]

***REMOVED***
literal:[REDACTED:repo-path:SF-IMPL-2]==>[REDACTED:repo-path:SF-IMPL-2]
literal:[REDACTED:maintainer-handle:SF-IMPL-2]==>[REDACTED:maintainer-handle:SF-IMPL-2]
literal:[REDACTED:repo-path:SF-IMPL-2]==>[REDACTED:repo-path:SF-IMPL-2]

***REMOVED***
literal:[REDACTED:repo-path:SF-IMPL-3]==>[REDACTED:repo-path:SF-IMPL-3]

***REMOVED***
literal:[REDACTED:repo-path:EF-IMPL-1]==>[REDACTED:repo-path:EF-IMPL-1]
regex:(?<![A-Za-z0-9_])[REDACTED:maintainer-handle:EF-IMPL-1](?![A-Za-z0-9_/-])==>[REDACTED:maintainer-handle:EF-IMPL-1]

***REMOVED***
literal:[REDACTED:repo-path:BALBOA-UPSTREAM-1]==>[REDACTED:repo-path:BALBOA-UPSTREAM-1]
regex:(?<![A-Za-z0-9_])[REDACTED:maintainer-handle:BALBOA-UPSTREAM-1](?![A-Za-z0-9_/-])==>[REDACTED:maintainer-handle:BALBOA-UPSTREAM-1]

***REMOVED***
literal:[REDACTED:repo-path:BALBOA-UPSTREAM-2]==>[REDACTED:repo-path:BALBOA-UPSTREAM-2]
regex:(?<![A-Za-z0-9_])[REDACTED:maintainer-handle:BALBOA-UPSTREAM-2](?![A-Za-z0-9_/-])==>[REDACTED:maintainer-handle:BALBOA-UPSTREAM-2]

# H-07 Spider Farmer credentials  (paste from policy R-SF-1, R-SF-2 at run time)
# literal:<RAW-USERNAME>==>[REDACTED:username:S-SF-5-username]
# literal:<RAW-PASSWORD>==>[REDACTED:credential:S-SF-5-password]

# H-08 Spider Farmer device identifiers (paste from policy R-SF-3, R-SF-4, R-SF-5)
# literal:<RAW-SERIAL>==>[REDACTED:serial:S-SF-device]
# literal:<RAW-IP>==>[REDACTED:ip:S-SF-device]
# literal:<RAW-UID>==>[REDACTED:uid:S-SF-device]

***REMOVED***
literal:[REDACTED:serial:R-EF-1]==>[REDACTED:serial:R-EF-1]
literal:[REDACTED:serial:R-EF-2]==>[REDACTED:serial:R-EF-2]
literal:[REDACTED:serial:R-EF-3]==>[REDACTED:serial:R-EF-3]
literal:[REDACTED:serial:R-EF-4]==>[REDACTED:serial:R-EF-4]

***REMOVED***
literal:==>
literal:==>
```

## 4. Pre-flight checklist (mandatory before invocation)

1. **Author consent recorded.** A short signed note in
   `docs/handbacks/` from Florian Krebs authorising the rewrite,
   referencing this plan file by SHA-256.
2. **Clone a fresh mirror** of the source repository to a scratch
   directory:
   ```bash
   git clone --mirror git@github.com:noheton/Obscurity-Is-Dead.git \
       /tmp/oid-mirror.git
   cd /tmp/oid-mirror.git
   ```
3. **Paste raw values** for H-07 / H-08 into the local
   `replacements.txt` (these are NOT in this committed plan file). The
   raw values live in the human author's local notes, not in any
   committed file (the redaction-policy register references them by
   marker only).
4. **Dry-run on a tag-bounded subset:**
   ```bash
   git filter-repo --replace-text replacements.txt --dry-run
   ```
5. **Run the rewrite:**
   ```bash
   git filter-repo --replace-text replacements.txt
   ```
6. **Verify every raw value is gone:**
   ```bash
   for s in '[REDACTED:maintainer-handle:SF-IMPL-1]' '[REDACTED:maintainer-handle:SF-IMPL-2]' '[REDACTED:repo-path:SF-IMPL-3]' \
            '[REDACTED:maintainer-handle:EF-IMPL-1]' '[REDACTED:maintainer-handle:BALBOA-UPSTREAM-1]' '[REDACTED:maintainer-handle:BALBOA-UPSTREAM-2]' \
            '[REDACTED:serial:R-EF-1]' '[REDACTED:serial:R-EF-2]' \
            '[REDACTED:serial:R-EF-3]' '[REDACTED:serial:R-EF-4]' \
            '' ''; do
       echo "==> $s"
       git log --all -S "$s" --oneline | head -5
   done
   # All should print only the header line; no commits.
   ```
   Repeat with the H-07/H-08 raw values from the local-only
   `replacements.txt`.
7. **Verify bib citekeys survived:**
   ```bash
   for k in smurfy_esphome_sf p0rigth_spiderblebridge \
            pythonspidercontroller niltrip_powerocean; do
       git grep -n "$k" -- 'paper/references.bib' || echo "MISSING: $k"
   done
   ```
8. **Tag the cleaned commit:**
   ```bash
   git tag -a pre-publication-clean -m "History rewrite per docs/git-history-rewrite-plan.md"
   ```
9. **Force-push to a *fresh* public repository** (NOT the existing
   `noheton/Obscurity-Is-Dead`, to avoid invalidating outstanding
   clones held by collaborators or automated systems):
   ```bash
   git remote add public-clean git@github.com:<NEW-REPO>.git
   git push --mirror public-clean
   ```
10. **Shred the local `replacements.txt` working copy** (it contains
    raw H-07/H-08 values):
    ```bash
    shred -u replacements.txt
    ```
11. **Then and only then** proceed to Zenodo deposit / arXiv submission
    per the rule-13 consent gate.

## 5. Rollback / safety notes

- Keep the **un-rewritten** mirror clone untouched and offline until
  the public push is verified. If the rewrite produces an unexpected
  diff (e.g. a citekey collision), the un-rewritten mirror is the
  recovery source.
- Do **not** rewrite the human author's working repository in place;
  always rewrite a fresh `--mirror` clone. This protects collaborators
  and CI systems that hold pulls of the un-rewritten history.
- Do **not** push the rewritten history back to
  `noheton/Obscurity-Is-Dead` — push to the new public-clean repo
  instead, then mark the original as private (or archive it) once the
  public mirror is verified.

---

*Plan drafted 2026-05-04 by the redaction-execution agent (Claude Opus
4.7) under orchestrator dispatch on branch
`claude/check-illustration-pipeline-Jqst3`. Execution requires
explicit human consent per CLAUDE.md rule 13.*

---

## 6. Execution record (2026-05-04)

### Deviations from §4

- The plan (§4.5) prescribed rewriting a fresh `--mirror` clone in
  `/tmp`. Execution rewrote the dev repo in place on
  `claude/history-rewrite-daDxQ`, under explicit consent and with the
  human author's standing backup. The §5 collaborator-protection
  rationale still applies to any future `noheton/Obscurity-Is-Dead`
  push: do not force-push the rewritten branch to a shared collaborator
  remote until public-mirror cut-over is approved.
- The plan (§4.3) stored R-SF-1..5 raw values in the human author's
  local notes only. Execution discovered the same raw values still
  present in working-tree blobs of `experiments/spider-farmer/original/`
  (vendor carve-out files) and the T6 transcript, so the substitution
  list could be assembled directly inside the run sandbox without
  pasting from external notes.

### Pass-2 gap-fill

The H-01b regex `(?<![A-Za-z0-9_])[REDACTED:maintainer-handle:SF-IMPL-1](?![A-Za-z0-9_/-])` correctly
preserves the bib citekey form (`smurfy_esphome_sf`) but excludes the
`/` lookahead, which means a *truncated* PR-style reference of the
shape `[REDACTED:repo-path:SF-IMPL-1]` (no `-encrypt`) is not matched
by H-01a (which requires the full `-encrypt` suffix) nor by H-01b. One
such occurrence was found in
`experiments/spider-farmer/original/doc/discusson.md:317`. A second
filter-repo pass was run with the single literal substitution
`[REDACTED:repo-path:SF-IMPL-1]==>[REDACTED:repo-path:SF-IMPL-1]`,
which subsumed the truncated form without disturbing the (now-marker)
output of pass 1.

### Verification snapshot

Per §4.6, `git log --all -S "<raw>" --oneline` returned **zero
commits** for every raw value in the catalogue:

`[REDACTED:maintainer-handle:SF-IMPL-2]`, `[REDACTED:maintainer-handle:BALBOA-UPSTREAM-1]`, `[REDACTED:repo-path:BALBOA-UPSTREAM-2]`, the four EcoFlow
serials, the DLR PII pair, `[REDACTED:username:S-SF-5-username]`, `[REDACTED:credential:S-SF-5-password][-]?`,
`[REDACTED:serial:S-SF-device]`, `[REDACTED:ip:S-SF-device]`, `[REDACTED:uid:S-SF-device]`. Substring tests for
`[REDACTED:maintainer-handle:SF-IMPL-1][^_]` and `[REDACTED:maintainer-handle:EF-IMPL-1][^_]` (i.e. handle uses *outside* citekey
form) returned only matches inside the policy/plan documents that
discuss the redaction itself, plus the binary zip carve-out below.

Citekey verification (§4.7): `smurfy_esphome_sf`,
`p0rigth_spiderblebridge`, `pythonspidercontroller`, and
`niltrip_powerocean` all still resolve in `paper/references.bib`.

### Carve-out: vendored zip archives

Three vendored archives in `experiments/spider-farmer/original/doc/`
(`esphome-spiderfarmer_ble-encrypt.zip`, `[REDACTED:repo-path:SF-IMPL-2]-master.zip`,
`[REDACTED:repo-path:SF-IMPL-3]-main.zip`) retain maintainer/repo strings
inside their packed entries. `git-filter-repo --replace-text` does not
descend into binary blobs. The pre-existing redaction-policy "Out of
scope" note (vendored archive *filenames*) extends to the *contents*
on the same rationale: rewriting the archive would defeat the
diff/audit chain those files exist to preserve. Public-mirror cut-over
must therefore either (a) drop these three files from the public tree
or (b) ship them with a documented caveat. Either approach satisfies
the redaction policy; the choice is left to the human author.

### Tag and clean-up

```text
$ git tag -a pre-publication-clean -m "History rewrite per docs/git-history-rewrite-plan.md (executed 2026-05-04)"
$ shred -u /tmp/replacements.txt /tmp/replacements2.txt
```

The `replacements.txt` working copy was shredded immediately after the
verification pass, per §4.10. No raw H-07 / H-08 values were committed
to any tracked file at any point.
