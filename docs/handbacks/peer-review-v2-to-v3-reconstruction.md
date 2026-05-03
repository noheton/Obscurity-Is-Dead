# Hand-back: Peer-review reconstruction of Spider Farmer `VERSION 2 → 3` migration

- **Stage:** out-of-band peer-review response (routes to scientific writer, stage 2)
- **Date:** 2026-05-03
- **Author:** AI agent (Claude, opus-4-7), invoked by the orchestrator on behalf of the human author. **All prose, code interpretation, and recommended edits below are AI-generated and require human review before integration into `paper/main.md` / `paper/main.tex`.** Human contribution at this stage is limited to (a) authoring the embedded `original/` snapshot referenced as evidence and (b) reviewing/approving the recommended edit.
- **Scope:** addresses one peer-review concern; does not modify the paper.

---

## (a) Original peer-review concern (verbatim)

> The HA integration migrated from VERSION 1→2 (documented in transcript T4), but the 2→3 migration step has no preserved transcript. Recommendation: Either reconstruct the 2→3 migration from commit history or explicitly note this as a provenance gap in §3.4.

This is also recorded as the standing open issue in `experiments/spider-farmer/provenance.md` §"Open follow-ups" item 5 and in `docs/logbook.md` (entries 2026-05-01 and 2026-05-02 referencing the undocumented `VERSION 2 → 3` step) and is forward-referenced in `paper/main.md` §3.4 line 169 and §10 (line 626).

## (b) Reconstruction methodology

The task brief instructed cloning `https://github.com/noheton/spider_farmer.git`. The following retrieval channels were attempted and **all failed in the current sandbox**:

1. `git clone https://github.com/noheton/spider_farmer.git /tmp/spider_farmer` — failed with `fatal: could not read Username for 'https://github.com'` (no network credential and no anonymous-clone fall-through).
2. GitHub MCP tools (`mcp__github__list_commits`, `mcp__github__list_tags`, `mcp__github__get_file_contents`) — denied: "repository `noheton/spider_farmer` is not configured for this session. Allowed repositories: `noheton/obscurity-is-dead`."
3. `curl https://api.github.com/repos/noheton/spider_farmer/commits` — returned `API rate limit exceeded` (unauthenticated).
4. `curl https://codeload.github.com/noheton/spider_farmer/tar.gz/refs/heads/{main,master}` — both returned `Not Found`. A direct `HEAD https://github.com/noheton/spider_farmer` returned `HTTP/2 404`, indicating the repository is either private, renamed, or otherwise unreachable from this sandbox without credentials.

**Consequence:** the task's primary path — reading commit messages, tags, and CHANGELOG diffs — is unavailable. The fallback path — task step 3, "If clone fails … record the failure and produce a *provenance-gap note* instead of a reconstruction" — is the operative one.

However, a **secondary evidence channel exists locally** and is sufficient to reconstruct the *technical* shape of the v2→v3 migration (though not the dated commit-by-commit narrative):

- The integration source is vendored at `experiments/spider-farmer/original/` (per repo commit `ffdf60c`, "feat(experiments): embed vendor repos as plain files for agent access").
- The migration code itself is preserved in `original/__init__.py` lines 95–135, including a self-documenting docstring naming both transitions.
- Manifest version (`original/manifest.json` line 4: `"version": "3.0.0"`) and config-flow VERSION constant (`original/config_flow.py` line 87: `VERSION = 3`) corroborate the end-state.

The reconstruction below is therefore **derived from the embedded source snapshot, not from upstream git history**. It can answer "*what changed*" and "*why, technically*" with high confidence; it cannot answer "*when*", "*in which commit(s)*", or "*was there a transcript at all*" — those remain provenance gaps.

## (c) Reconstructed narrative

### What the v2→v3 migration does (high confidence — read directly from code)

The single load-bearing artifact is `experiments/spider-farmer/original/__init__.py` lines 95–135. Verbatim docstring (lines 96–100):

```
"""Migrate config entries to the current VERSION.

Version 3: BLE-only.  Drop MQTT fields (pid, uid, mqtt_topic) and derive
pid from the BLE address.  Also carry forward the v1→v2 CB key fix.
"""
```

The function body executes the following steps when `entry.version < 3`:

1. **Carry-forward of the v1→v2 CB-key fix** (lines 101, 107–114). The old stale CB key `J4G0M9dX1f1v3fXr` (the candidate that T1 proposed and T4 disproved) is replaced with the corrected pair `BLE_DEVICE_TYPES["cb"]` (key/IV from `const.py` lines 45–47: `iVi6D24KxbrvXUuO` / `RnWokNEvKW6LcWJg`). Idempotent: pre-existing v2 entries already past this fix are left unchanged.
2. **Drop legacy MQTT-only config-entry fields** (lines 117–118): `uid` and `mqtt_topic` are removed from `entry.data`.
3. **Derive `pid` from the BLE address** (lines 121–123): `pid = ble_addr.replace(":", "").upper()`. Where the legacy entry has no `CONF_BLE_ADDRESS`, the migration **fails closed** (returns `False`, lines 126–130) — i.e. v1/v2 entries that were ever MQTT-only and never bound to a BLE address cannot migrate and the entry is not silently mutated.
4. **Update the entry version** (line 132): `async_update_entry(entry, data=new_data, version=3)`.
5. **Log the migration** (line 133): `"Migrated Spider Farmer entry %s to version 3 (BLE-only)"`.

### Why (interpretive — medium confidence)

The architectural shift from v2 to v3 is a **transport simplification, not a protocol change**. v2 retained MQTT-related entry fields (`uid`, `mqtt_topic`) alongside the BLE configuration; v3 is **BLE-only**. This is consistent with:

- The vendor MQTT broker's known security posture (self-signed certs, recovered credentials documented in `original/doc/log.md`, surfaced in `paper/main.md` §3.6) — a defensible reason to drop MQTT from the user-facing config flow.
- The manifest (`original/manifest.json`) declaring `"iot_class": "local_push"` and only Bluetooth match rules — no MQTT discovery surface remains.
- Transcript T6 (the MQTT probe trace) being a *research dataset*, not an integration code path — i.e. MQTT was investigated for security analysis but never elevated to a production transport in v3.

### What cannot be reconstructed (low confidence / explicit gaps)

- **Date of the v2→v3 transition.** No commit timestamps are accessible.
- **Commit SHA(s) bracketing the boundary.** Upstream history is not retrievable from this sandbox.
- **Verbatim commit messages.** Cannot be quoted.
- **Whether a chat transcript ever existed for the v2→v3 work.** The seven preserved transcripts (T1–T7) plausibly do not cover it, but absence of evidence here is not evidence of absence; the work may have been done in an unsaved session, in-IDE, or without LLM assistance.
- **Whether the v2→v3 step was a single commit, a sequence, or a release-branch merge.** The migration function is self-contained, which is *consistent with* a single focused commit but does not prove it.
- **Issue/PR references** (e.g. an upstream PR number analogous to `noheton/spider_farmer` PR #9 cited for T4-era work in the logbook).

## (d) Recommended paper-edit

The writer agent should replace the parenthetical in `paper/main.md` §3.4 line 169 with the block below, and mirror the change in `paper/main.tex`. The edit is conservative: it converts an open admission of a gap into a *bounded* gap (technical content reconstructed; provenance metadata still missing) and surfaces both the reconstruction and its limits, in keeping with rule 1 (honesty about AI vs human contributions) and the `[ai-confirmed]` evidence ladder (the migration code itself is `[lit-read]` — directly inspected — but the upstream git narrative remains `[unverified-external]`).

### Drop-in block for `paper/main.md` §3.4 (replaces the current line 169 parenthetical)

> Migration framework `async_migrate_entry` in `__init__.py` line 95; the integration is now at `VERSION = 3` past the T4-era `1→2` migration. The `2→3` step is **not covered by any preserved chat transcript**, but the migration logic itself — vendored at `experiments/spider-farmer/original/__init__.py` lines 95–135 — is self-documenting and reconstructs to: (i) drop the legacy MQTT-only config-entry fields `uid` and `mqtt_topic`; (ii) derive `pid` deterministically from the stored BLE address (failing closed if no BLE address is present); (iii) idempotently carry forward the `v1→v2` CB-key correction; (iv) bump the entry version and emit `"Migrated Spider Farmer entry %s to version 3 (BLE-only)"`. Architecturally this is a transport simplification (BLE-only; MQTT retained only as a security-research dataset surface, §3.6), not a protocol change. **Provenance gap that remains:** the upstream commit history of `noheton/spider_farmer` was not retrievable from the build environment used for this paper (clone, GitHub API, and codeload tarball all failed; reconstruction worked from the embedded `original/` snapshot at repo commit `ffdf60c` only). Date, commit SHA, and any associated PR or issue thread for the v2→v3 transition are therefore unverified-external.

### Drop-in block for `paper/main.tex` (mirror of the above)

```latex
Migration framework \texttt{async\_migrate\_entry} in \texttt{\_\_init\_\_.py}
line~95; the integration is now at \texttt{VERSION = 3} past the T4-era
\(1\!\to\!2\) migration. The \(2\!\to\!3\) step is \textbf{not covered by any
preserved chat transcript}, but the migration logic itself --- vendored at
\texttt{experiments/spider-farmer/original/\_\_init\_\_.py} lines 95--135 ---
is self-documenting and reconstructs to: (i)~drop the legacy MQTT-only
config-entry fields \texttt{uid} and \texttt{mqtt\_topic}; (ii)~derive
\texttt{pid} deterministically from the stored BLE address (failing closed if
no BLE address is present); (iii)~idempotently carry forward the
\(v1\!\to\!v2\) CB-key correction; (iv)~bump the entry version and emit
\texttt{"Migrated Spider Farmer entry \%s to version 3 (BLE-only)"}.
Architecturally this is a transport simplification (BLE-only; MQTT retained
only as a security-research dataset surface, \S3.6), not a protocol change.
\textbf{Provenance gap that remains:} the upstream commit history of
\texttt{noheton/spider\_farmer} was not retrievable from the build
environment used for this paper (clone, GitHub API, and codeload tarball all
failed); reconstruction worked from the embedded \texttt{original/} snapshot
at repo commit \texttt{ffdf60c} only. Date, commit SHA, and any associated
PR or issue thread for the v2$\to$v3 transition are therefore
unverified-external.
```

The §10 (Future Work / open issues) bullet at line 626 ("Reconstruct the Spider Farmer `VERSION 2 → 3` migration step that no preserved transcript currently documents.") should be amended to reflect partial closure:

> Recover upstream `noheton/spider_farmer` commit-history metadata (date, SHA, PR/issue references) for the `VERSION 2 → 3` migration. The technical content of the migration has been reconstructed from the embedded `original/__init__.py` (see §3.4); only the dated commit-history narrative remains outstanding.

## (e) Explicit provenance-gap statement

Even after this reconstruction, the following items remain **unverified-external** in `docs/sources.md` terms and should not be promoted past `[lit-retrieved]` until the upstream repository is accessible:

1. The commit SHA(s) implementing the v2→v3 boundary.
2. The commit dates and chronological position relative to the T1–T7 transcript window (2026-04-25 – 2026-04-26 per the §3.7 table).
3. Verbatim commit messages, CHANGELOG entries, or release notes for the v3 cut.
4. Issue/PR references and any code-review discussion.
5. Whether the migration was authored with AI assistance and, if so, in which session.

These are the items a reader following the *FAIR / reproducibility* clauses of the methodology (`docs/methodology.md`) would most plausibly want; the recommended paper-edit names them as outstanding rather than papering over them.

---

### Redaction check (rule 12)

This addendum surfaces only material already present and already redacted in the repository: the stale BLE candidate key `J4G0M9dX1f1v3fXr` (publicly recorded in T1 and `provenance.md` line 29 as a *disproved* candidate, not a live credential), the corrected device-type key/IV pairs (already published in `paper/main.md` §3.4 Table 1 lines 179–182), and a reference to the MQTT credentials in §3.6 that are themselves already redacted via `R-SF-1`/`R-SF-2`. No new credential material is introduced.

### Public-distribution check (rule 13)

This file is a hand-back artifact under `docs/handbacks/`. It is not a paper edit, not a release, and not a publication. No push, no Zenodo deposit, no arXiv submission is implied or performed.
