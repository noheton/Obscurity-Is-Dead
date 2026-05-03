# Research Protocol — PowerOcean Upstream Resync 2026-05-03

- **Agent:** Claude Opus 4.7 (Stage 1, research-protocol targeted resync)
- **Branch:** `claude/review-open-issues-PfNx9`
- **Trigger:** Human-author directive — `noheton/powerocean-dev` upstream has made "significant progress" since the in-repo snapshot (last research pass logged 2026-04 / 2026-05-01; delta sweep `docs/handbacks/research-protocol-delta-2026-05-03.md` flagged trigger-d carry-overs but did not pull upstream).
- **Scope:** Detect upstream changes, cross-check against `paper/main.md` §4, produce paper-edit recommendations. No edits to `paper/main.{md,tex}` (rule 11, rule 13). No data smuggled out: rule 12 redaction enforced (no credentials, SNs, UIDs, IPs reproduced verbatim from upstream).

---

## (a) Probe results

| Channel | Outcome | Notes |
|---|---|---|
| `git clone https://github.com/noheton/powerocean-dev.git` | not attempted | sandbox lacks creds; previous spider_farmer pass showed the same path returned 404. |
| `curl -sI https://github.com/noheton/powerocean-dev` | **HTTP/2 200** | repo public; default branch resolvable. |
| `curl -sI https://api.github.com/repos/noheton/powerocean-dev/commits` | **HTTP/2 403** | unauthenticated; `x-ratelimit-remaining: 0` (hard rate-limit). |
| `curl -sIL https://codeload.github.com/.../tar.gz/refs/heads/main` | **HTTP/2 200** | tarball reachable; `master` returns 404 → default branch is `main`. |
| `curl -sI https://raw.githubusercontent.com/.../main/.../manifest.json` | **HTTP/2 200** | raw path also reachable; same etag as `master` URL → both refs point to identical content. |
| `curl -s https://github.com/noheton/powerocean-dev/commits/main.atom` | **HTTP/2 200** | atom feed delivers ≥30 recent commit SHAs + titles + timestamps. |
| GitHub MCP (`mcp__github__*`) | not attempted | session-config restricted to `noheton/obscurity-is-dead` per prior pass. |
| Exa MCP | not attempted | tarball + atom feed sufficient; no need to spend Exa quota. |

**Tarball downloaded:** `/tmp/powerocean-dev.tar.gz` (867,975 bytes), extracted to `/tmp/po-upstream/powerocean-dev-main/`. **Atom-feed top SHA (latest commit on `main` at probe time):** `56d4f55c34faf89efd7c6599019e70d5d4070106` (`Merge pull request #14 from noheton/claude/review-opcc-status-eNh9N`, 2026-05-03T17:17:24Z).

---

## (b) Repo metadata as observed

- **Default branch:** `main`. (No `master`.)
- **Manifest version:** `2026.05.01` — **identical to in-repo snapshot.** No version bump despite substantive code changes; the upstream maintainer has been pushing post-tag fixes onto the same `2026.05.01` semver string.
- **Codeowner:** `@niltrip` (unchanged). `documentation` and `issue_tracker` still point at `niltrip/powerocean` (unchanged).
- **New top-level files:** `DISCLAIMER.md` (added; legal-method statement — see §c.1).
- **`doc/` directory:** **drastically reduced.** `doc/README.md` (new, 80 lines) replaces `apk.md`, `apk-logs.md`, `equipment.md`, `implementation.md`, `geninfo.pdf`, `powerocean.pdf`, `ecoflow-open-demo.zip`, `EcoFlow_6.13.8.2_APKPure/` (4 APKs + manifest), and `logs/` (six raw extraction logs). All of these are still present in the in-repo snapshot under `experiments/ecoflow-powerocean/original/doc/`. Upstream's `doc/README.md` explicitly explains the removal as a UrhG / GDPR concern and notes that `git rm` does **not** purge prior commits from history (filter-repo would be required for a true purge).
- **README.md:** completely rewritten. Adds OCPP services section, OCPP-options config-flow step, "important caveat" about runtime-handover gap (`vendorInfoSet`), and a new device table with model codes 83 / 85 / 86 / 87.
- **Recent commit cadence (atom feed):** dense activity 2026-05-01 → 2026-05-03 (≥20 commits in ~48 h). Notable titles:
  - `e620adb1cc` 2026-05-01 *Fix chargingStatus crash, add setter pre-fill, complete legal cleanup*
  - `1d1527c565` 2026-05-02 *docs: add niltrip/powerocean as primary inspiration source*
  - `b3e2fd6f00` 2026-05-03 *docs: document OCPP 1.6 support on PowerPulse and prep config-flow*
  - `1aa96507ef` 2026-05-03 *Capture OCPP 1.6 schema from APK decompile (raw_ocpp.txt)*
  - `557e82ecc1` 2026-05-03 *Point OCPP options at lbbrhzn/ocpp HACS host*
  - `b67cc42a59` 2026-05-03 *Add OCPP backend options + EV charging status translations*
  - `5c8b815cf9` 2026-05-03 *Add OCPP catalog services; redact decompile/PII from `doc/`*
  - `3bd89aa585` 2026-05-03 *ocpp: require secure_url and default platformType=2 from probing*
  - `4662cc12d2` 2026-05-03 *sensor: translate raw battery state enums (NORMAL_STATE, PB_*_STATE)*
  - `2d9cf96ca8` 2026-05-03 *ocpp: add async_get_property + ocpp_probe_runtime diagnostic service*
  - `56d4f55c34` 2026-05-03 *Merge pull request #14 from noheton/claude/review-opcc-status-eNh9N* ← HEAD at probe time

---

## (c) Per-section delta vs in-repo snapshot

### c.1 New top-level `DISCLAIMER.md` (load-bearing for paper §4 + §10)

Upstream verbatim (key claims):
- "developed by observing network traffic between the official EcoFlow mobile application and the EcoFlow cloud API using standard HTTP inspection tools"
- "**No EcoFlow application binary was decompiled, disassembled, or reverse-engineered to produce this software. No proprietary source code, trade secrets, signing keys, or cryptographic material belonging to EcoFlow was copied or derived from.**"
- "All field names, endpoint paths, and protocol structures documented here were observed in plaintext HTTP/JSON traffic"
- Cites § 69e UrhG and Art. 6 Software Directive 2009/24/EC for interoperability scope
- Trademark notice (EcoFlow / PowerOcean / PowerPulse, no affiliation)

**Tension with paper claims:** §4.3 step 1 in `paper/main.md:261` (and §3.7 row in `:288`, "Discovery T1 (apk) — APK extraction, three-surface enumeration, field-name convention identified ~3 h") describe the analysis workflow as **APK string and action-field extraction**. The in-repo snapshot's `provenance.md` matches this (T1 transcript, `apk.md` analysis, four committed APKs, `raw_*.txt` logs). The upstream `DISCLAIMER.md` now positions the integration's method as **HTTP-traffic observation, not decompilation**.

These are not strictly contradictory — the *paper case study* documents AI-assisted research that included an APK-decompile arm; the *upstream integration's legal disclaimer* describes the method by which its committed code is licensed and defended. But a reader landing on `DISCLAIMER.md` and then on `paper/main.md` §4 will see a discrepancy unless the paper acknowledges the two-track methodology (researcher-side decompile to *understand*; upstream-side traffic-observation to *defend redistribution*).

There is also a sourcing fact in commit `1aa96507ef` ("Capture OCPP 1.6 schema from APK decompile (raw_ocpp.txt)") that **does** cite an APK decompile, which adds nuance: the upstream maintainer drew protocol structure from APK material during development but the redistributable artifact ships only HTTP-traffic-derived strings. This reconciles the surface tension and is itself a paper-relevant finding.

### c.2 New `doc/README.md` — redaction + git-history caveat (rule-12 / rule-13 directly relevant)

Upstream prose (paraphrased): the previous `doc/` contents — APK, derivative markdown documents, raw log extracts, vendor PDFs, vendor sample-code archive, `equipment.md` (real personal name + device serial numbers — **GDPR personal data**), `implementation.md` (referencing same personal data) — have been removed from the working tree. Upstream **explicitly notes**: *"`git rm` does not purge history: anyone with clone access can still retrieve the deleted blobs from prior commits. If full removal is required, use `git filter-repo` (or `git filter-branch`) on a fresh clone and force-push."*

**Direct paper relevance:** rules 12 + 13 of `CLAUDE.md` already require pre-publication history rewrite. The upstream maintainer has performed exactly this operation on a parallel repository, with the same caveat the paper's methodology section already implies. This is now a **citable real-world precedent** for the rule-12 history-rewrite requirement, and a candidate addition for §6 (synthesis) or §10 (Pandora moment).

### c.3 OCPP scope — substantial new code surface

Upstream additions absent from in-repo snapshot:
- `custom_components/powerocean_dev/api.py` (+115 LOC; 317 → 432): three new methods — `async_ocpp_list_backends`, `async_ocpp_post_backend`, `async_get_property` (with `acquireQuotaAll` fallback for diagnostic dump). New endpoints: `GET /provider-service/app/ocppPlatformConfig/list`, `POST /provider-service/app/ocppPlatformConfig`. Diagnostic path: `POST /iot-devices/device/getDeviceProperty` (read companion to `setDeviceProperty`), with fallback to `GET /iot-devices/device/acquireQuotaAll`.
- `custom_components/powerocean_dev/__init__.py` (+152 LOC; 328 → 480): four new services — `ocpp_list_backends`, `ocpp_register_backend`, `ocpp_disable_backend`, `ocpp_probe_runtime`. New helper `_build_ocpp_bind_req`. Voluptuous schema `_ocpp_bind_schema`.
- `custom_components/powerocean_dev/const.py`: four new options keys (`CONF_OCPP_ENABLED`, `CONF_OCPP_URL`, `CONF_OCPP_CP_ID`, `CONF_OCPP_AUTH_KEY`). One source-comment cleanup: the snapshot's `# (APK: /iot-devices/device/setDeviceProperty)` annotation is removed; replaced with neutral `# ── EcoFlow consumer API write endpoint ──` (consistent with the §c.1 `DISCLAIMER.md` rewrite).
- `services.yaml`: +174 LOC documenting the four OCPP services with field selectors.
- README "Important caveat": *"The catalog write alone does not redirect the charger at runtime — that handover requires an additional proto write (`vendorInfoSet`) which is not yet shipped."* Empirical discoveries documented inline: (a) `secureUrl` empty → API returns code 1006 ("安全URL地址不能为空"); (b) `platformType=2` is the empirically-verified value for third-party hosts (vs `platformType=1` "SmartRed built-in"); (c) `lbbrhzn/ocpp` is the supported HACS host.

**Auth model unchanged.** Same EU/US region probe (`api-e.ecoflow.com` / `api-a.ecoflow.com`); same `https://api.ecoflow.com/auth/login` username+password endpoint; same bearer-token model; same `setDeviceProperty` legacy endpoint as primary write path. **No move to HMAC-signed Open API; no MQTT shift.** This is a confirmation, not a change, of the §4.4 paper claim.

**No new credentials, SNs, UIDs, or IPs surfaced.** The OCPP service examples use `ws://homeassistant.local:9000` / `wss://homeassistant.local:9001` (RFC-1918-equivalent loopback hostname; not exfiltratable). Rule-12 redaction not triggered.

### c.4 Sensor / parser fixes (low paper-relevance)

- `chargingStatus` crash fix (commit `e620adb1cc`).
- Battery state enum translation (`NORMAL_STATE`, `PB_*_STATE` → human-readable; commit `4662cc12d2`).
- Setter pre-fill from state (already documented in T3 transcript / snapshot's `types.py` regex).

These touch `sensor.py`, `binary_sensor.py`, `parser.py`, `select.py`, `switch.py`, `number.py`, `button.py`, three translation files. None alters a paper claim; documented here for completeness.

### c.5 Sourcing acknowledgement — `1d1527c565`

`docs: add niltrip/powerocean as primary inspiration source` — upstream now formally credits `niltrip/powerocean` as the parent. The in-repo snapshot's `provenance.md` already established this via `const.py:13 ISSUE_URL`. Confirms (does not change) the existing paper sourcing.

---

## (d) Cross-check against paper claims + edit recommendations

For the **scientific writer (Stage 2)** to consider — none of these are blocking; all are recommended.

### d.1 §4.2 Artifact inventory (`paper/main.md:247-253`) — **CONFIRM + ANNOTATE**
Current text: "`original/doc/EcoFlow_6.13.8.2_APKPure/` — four APK split files plus manifest. `original/doc/ecoflow-open-demo.zip` — vendor reference Java implementation. `original/doc/powerocean.pdf`, `geninfo.pdf` — vendor documentation."
Recommendation: keep the in-repo snapshot enumeration (these artifacts genuinely live in the snapshot tree and are part of the paper's research provenance), but **add a note** that the upstream integration repository as of 2026-05-03 has removed these artifacts from its own working tree (commit `5c8b815cf9` *Add OCPP catalog services; redact decompile/PII from `doc/`*). This is a methodology-honesty point (rule 1 + rule 4) and a concrete instance of rule-12 enforcement happening upstream.
Suggested phrasing (writer to refine): *"As of 2026-05-03 the upstream `noheton/powerocean-dev` repository has removed the APK, derivative APK analysis, vendor PDFs, and the `equipment.md` personal-data file from its working tree (commit `5c8b815cf9`), citing UrhG and GDPR concerns; the snapshot preserved here under `experiments/ecoflow-powerocean/original/` predates that redaction and is retained for research provenance only."*

### d.2 §4.3 Workflow step 1 (`paper/main.md:261`) — **HEDGE**
Current: "**APK string and action-field extraction** to enumerate writeable parameters."
Recommendation: keep as the *researcher-side* method, but acknowledge the *upstream-redistributable* method is now framed differently. Footnote candidate: *"The upstream integration's `DISCLAIMER.md` (added 2026-05-03) documents its committed code as derived from observed HTTP traffic rather than decompilation; commit `1aa96507ef` separately captures OCPP-1.6 schema material from an APK decompile, indicating a two-track methodology where decompilation supports protocol *understanding* while the redistributable artifact contains only traffic-observable structures."*

### d.3 §4.4 Findings — write-surface confirmation (`paper/main.md:269`) — **CONFIRM**
Current: "Write surface: `POST /iot-devices/device/setDeviceProperty` with payload `{"sn": ..., "params": {...}}` — confirmed at `api.py` line 306."
Status: **still correct in upstream** (now `api.py` line 421 due to OCPP-method insertions; snapshot reference to line 306 remains valid for the snapshot). No edit required. Optionally update the line cite if the writer prefers an upstream-current pointer.

### d.4 §4.4 Findings — three API surfaces / Figure 8 (`paper/main.md:266`) — **EXTEND**
Figure 8 currently enumerates three surfaces (legacy `setDeviceProperty`, Open API HMAC-signed, MQTT). Upstream now adds a **fourth observable plane** within the legacy surface family: the OCPP catalog endpoints (`/provider-service/app/ocppPlatformConfig{,/list}`) and the read-side diagnostic endpoint (`/iot-devices/device/getDeviceProperty` + `/iot-devices/device/acquireQuotaAll`).
Recommendation: writer-discretionary. Either add a sentence noting that the legacy bearer-token surface has now been mapped to write/read/list-OCPP/diagnostic verbs (without changing Figure 8), or hand to the **illustrator (Stage 3)** for a Figure 8 v2 with the expanded verb set under the legacy plane. Lower priority than §69e UrhG sourcing.

### d.5 §4.7 KPI table T1 row (`paper/main.md:288`) — **OPTIONAL HEDGE**
Current: "Discovery | T1 (apk) | APK extraction, three-surface enumeration, field-name convention identified | ~3 h"
Recommendation: leave as-is (this is the *researcher's* time, not the upstream maintainer's). If d.2's footnote lands, no further KPI edit needed.

### d.6 §4.6 Findings — security implications (`paper/main.md:280`) — **CONFIRM + EXTEND**
Current: "Vendor APK and PDF redistribution status is flagged in `docs/sources.md` (S-EF-2, S-EF-3, S-EF-4) and must be resolved before public release."
Status: confirmed as *still open* in the in-repo snapshot, and now precedented by the upstream redaction event. Recommendation: extend the §4.6 list with the OCPP-runtime caveat as a concrete *interoperability gap*: the integration can now write the EcoFlow-side OCPP catalog but cannot redirect the charger at runtime without the unshipped `vendorInfoSet` proto write. This is a useful empirical data point for §6 (synthesis) on the asymmetry between catalog-level and runtime-level interoperability.

### d.7 §6 / §7 synthesis — **NEW MATERIAL CANDIDATE**
The upstream `doc/README.md` explicitly stating "`git rm` does not purge history" is a clean, citable, recently-dated, real-world enactment of the rule-12 publication discipline that this paper argues for. Recommendation: §6 ("synthesis-evidence-asymmetry") or §10 ("Pandora moment") could cite the upstream redaction commit (`5c8b815cf9`) and the accompanying `doc/README.md` paragraph as a concrete instance of an AI-assisted-integration project applying the same discipline this paper proposes — without requiring this paper to claim attribution.
Sources entry to add: a `[lit-retrieved]` row under EcoFlow case study, pointing to commit `5c8b815cf9` and `doc/README.md` on `noheton/powerocean-dev@main` (probe date 2026-05-03).

### d.8 `provenance.md` open follow-up #5 (OCPP scope decision) — **NOW DECIDABLE**
The 2026-05-03 delta sweep flagged this as open. Upstream has now committed substantial OCPP code with documented runtime-handover gap. Recommendation to the human author / orchestrator: **decide for inclusion as a Future Work item in §11**, citing the documented runtime gap as live evidence of an unresolved interoperability boundary. Not a new case study; a one-paragraph reference suffices.

### d.9 `provenance.md` open follow-up #4 (§69e UrhG sourcing) — **STILL OPEN, NOT CLOSED BY UPSTREAM**
Upstream's `DISCLAIMER.md` cites § 69e UrhG and 2009/24/EC but does **not** itself constitute a sourced legal commentary. The medium-priority research subpass queued by the 2026-05-03 delta sweep remains needed; upstream's disclaimer is **not** a substitute citation for the paper's load-bearing legal-honesty footnote.

### d.10 `provenance.md` open follow-up #6 (APK / PDF licensing audit before public release) — **PRECEDENT AVAILABLE**
Upstream has now made the redistribution decision (remove). This does not bind the paper repo, but provides clean precedent if/when the human author decides to do the same before any rule-13 release event.

---

## (e) Provenance gaps (what was NOT verifiable from this resync)

1. **Authorship attribution of upstream commits.** Branch names `claude/...` (e.g. `claude/review-opcc-status-eNh9N`, `claude/add-ocpp-backend-probing-...`, `claude/ocpp-investigation-findings`, `claude/investigate-opcc-1.6-72Vfn`, `claude/check-powerpulse-implement...`, `claude/ecoflow-set-parameters-...`, `claude/fix-powerpulse-entities-qhHch`) suggest AI-assisted commits, mirroring this project's own commit-naming convention. Not verified — atom feed gives titles + SHAs but not commit-message bodies or `Co-authored-by:` trailers. Verification would require an authenticated GitHub API call (rate-limited at probe time) or `git log` on the cloned tarball, which **does not include `.git/`** and so commit metadata beyond the working tree is unrecoverable from the tarball channel.
2. **PR / issue narrative.** Atom feed gives commit titles but not PR descriptions. PR #6, #7, #8, #9, #10, #11, #12, #13, #14 are referenced in merge-commit titles; their bodies were not fetched.
3. **`raw_ocpp.txt`** referenced in commit `1aa96507ef`'s title is **not present** in the upstream working tree (consistent with the §c.2 redaction of `doc/logs/`). The commit added it, a later commit (`5c8b815cf9`) removed it. The blob is recoverable only via `git cat-file` against an authenticated clone; out of scope here.
4. **No signature verification.** Did not check `gpg`-signed commit status; not blocking.
5. **No CI / release-asset inspection.** `.github/workflows/{validate,lint,release}.yml` were not diffed.
6. **No `[ai-confirmed]` upgrade attempted.** The Source Analyzer (Stage 1.5) is the owner of that step. This document files findings; the analyzer should sweep `docs/sources.md` for new entries on its next pass.

---

## Summary

- **Probe outcome:** upstream reachable via tarball + atom-feed; API rate-limited; MCP not used.
- **Material changes detected:** (1) new `DISCLAIMER.md` reframing the integration's legal method; (2) `doc/` redaction with explicit `git rm`-doesn't-purge-history caveat — a real-world rule-12 / rule-13 precedent; (3) OCPP scope (~+440 LOC across `api.py`, `__init__.py`, `services.yaml`, `const.py`) with documented runtime-handover gap; (4) sensor / parser fixes; (5) sourcing acknowledgement of `niltrip/powerocean`.
- **Auth / endpoint model:** unchanged. §4.4 paper claims hold.
- **Recommended writer actions:** d.1 + d.2 + d.6 + d.7 are the load-bearing edits. d.3, d.5 are no-op confirms. d.4 is illustrator-optional. d.8 unblocks `provenance.md` follow-up #5; d.9 + d.10 are still-open / precedent-only.
- **Provenance gaps filed:** 6 (mainly authorship-attribution + PR-body texts; not blocking).
- **Rule-12 redaction:** none triggered; no credentials / SNs / UIDs / IPs reproduced from upstream.
- **Rule-11 / rule-13:** no edits to `paper/main.{md,tex}`; no push; no `make pdf`; no Zenodo / arXiv dispatch.
