# Phase 3 — Implementation (Balboa Gateway Ultra Wi-Fi module)

> Author attribution: drafted by AI agent (Claude Opus 4.7) under
> `docs/prompts/iot-integrator-prompt.md`. Researcher review pending
> at the close-out checkpoint.
>
> Phase 3 outcome category selected at the Phase 2→3 user checkpoint:
> **`T-CONFIG-ONLY-OUTCOME`** (researcher answer 2026-05-02:
> "2, cloud confirmed, drop at publication"). Cloud-touching
> authorisation **explicitly granted, scoped to the household's own
> account**.

## 3.1 Design

The integration shape is a **configuration-only adoption** of an
existing open-source bridge plus a hardening overlay plus a smoke
test, mirroring the Ondilo §5.5 pattern (`experiments/iot-integrator-ondilo-ico-spa-v2/process/phase-3-implementation.md`).
No parallel `custom_components/<slug>/` is shipped.

**Backing library.** `controlmyspa` 4.0.0 (PyPI, MIT,
`[REDACTED:repo-path:BALBOA-UPSTREAM-2]`). Used directly by the smoke test and
implicitly by the recommended bridge.

**Recommended runtime.** `[REDACTED:repo-path:BALBOA-UPSTREAM-1]`
(GPL-3.0, MQTT bridge with autodiscovery). The integration value
this folder *adds* is the hardening overlay and operational
discipline; the runtime itself is upstream.

**Data model.** One `climate` entity (target/current temperature,
heater mode, temp range, temp scale, panel lock); per-component
`switch` / `number` / `light` for jets, blowers, lights, chromozone
zones (state / colour / intensity / power / speed), c8zone, filter
cycles; read-only `binary_sensor.online` and
`sensor.last_command_status`. Endpoint inventory verbatim in
`phase-2-weakness.md §2.1.2`.

**Credential storage.** HA `secrets.yaml` with file-mode `0600`,
encrypted backups (control C-6). Two secrets: `controlmyspa_user`,
`controlmyspa_pass`. Smoke test reads them from
`CONTROLMYSPA_USER` / `CONTROLMYSPA_PASS` environment variables.

**Failure modes** (handled in `integration/operational-notes.md`):

| Failure | Detection | Response |
|---|---|---|
| `iot.controlmyspa.com` TLS-chain regression (W-3 + Phase 1 §1.2.3) | bridge log `SSLError: certificate verify failed` | upgrade `certifi`; do **not** disable TLS verification |
| Cognito refresh-token expiry after 30 d dormant | bridge log `401 Unauthorized` after long downtime | re-login (smoke test); password rotation if suspected leak |
| ES-6 has no rate-limit handling | bridge log `429`/`5xx` clusters | poll cadence ≥ 60 s |
| Cross-vendor data flow to WaterGuru (W-5) | DNS query log shows `api.waterguru-prod.com` | C-2 sinkhole; SAR follow-up |
| Google Mobile Ads SDK fan-out (W-6) | DNS query log shows `pagead2.googlesyndication.com` | C-2 sinkhole |
| Vendor firmware update breaks endpoints | smoke test passes but specific writes 400 / 404 | re-run §A on new APK; diff against `phase-2-weakness.md §2.1.2`; addendum-not-rewrite |

**Scope-creep rejection.** This implementation does **not**:

- ship a parallel HA `custom_component` (the upstream MQTT bridge
  already covers the surface);
- implement certificate pinning at the integration layer (vendor
  TLS posture is too unstable to pin against — would convert a
  silent vendor failure into a noisy household failure with no net
  security gain);
- pursue the §B LAN probe or §A DEX deep-dive (the researcher
  declared LAN-scan "possible later" at Phase 0→1 and has not
  re-opened it);
- implement the §C live cloud capture (out of scope for the
  configuration-only outcome; remains researcher-runnable);
- ingest the §D GDPR SAR responses (researcher-runnable artifact,
  not integrator-deliverable);
- write any setpoint > 40°C / 104°F automation (validation-checklist
  step 5 enforces this at integrator-side because the firmware
  cap is vendor-side, not API-side).

## 3.2 Build

Files written under `experiments/iot-integrator-balboa-gateway-ultra/integration/`:

| File | Role |
|---|---|
| `README.md` | design, install, hardening overlay (six controls C-1..C-6), uninstall |
| `smoke-test.py` | minimal read-only validation against ES-6 |
| `operational-notes.md` | rotation, monitoring, vendor-update response, ToS-change response, backup hygiene, incident-response, decommissioning |
| `validation-checklist.md` | eight researcher-runnable steps + cloud-authorisation block |
| `dual-use.md` | dual-use reflection per CLAUDE.md rule 5 / `T-DUAL-USE-MIRROR` |

No HA YAML is shipped. Householders' HA topologies vary; the
integration value is the **operational discipline**, not the YAML.
A reader can install the upstream bridge and copy in the six C-1..C-6
controls without changing their HA topology.

## 3.3 Validation

The agent runs in a sandbox with no LAN or cloud access; the
end-to-end test is researcher-side. The validation log will be
captured by the researcher in
`captures/phase-3-validation.log.redacted`, following
`integration/validation-checklist.md`.

What the agent **did** validate at static-analysis time:

| Validation | Method | Result |
|---|---|---|
| ES-6 endpoint surface vs APK 4.1.9 strings | `T-CROSS-IMPL-VALIDATION` | confirmed; APK exposes additional endpoints (chromozone color/power/speed, filter-cycles schedule, time, c8zone, claim/unlink) — see `phase-2-weakness.md §2.1.2` |
| Identity-provider topology | DEX strings + ES-6 login flow shape | AWS Cognito user pool, us-west-2; 1 h access / 30 d refresh defaults assumed |
| Permission set vs declared control surface | manifest.json (25 entries) vs `phase-0-bootstrap.md §0.2.2` | declared surface (read+write) is achievable with the existing permissions; no permission is "missing" for the integration |
| Smoke-test file is syntactically valid Python | offline `py_compile` (researcher-runnable) | n/a (researcher to run) |

What the agent **did not** validate (researcher checklist):

- bridge container actually publishes the entities to MQTT;
- HA discovers the entities and exposes them in the UI;
- a single read returns sensible numbers;
- a single write succeeds with the integration-level setpoint guard
  in place.

These are the steps in `validation-checklist.md`.

## 3.4 Operational notes

Full runbook is in `integration/operational-notes.md`. Key entries:

- §1 daily / weekly steady state.
- §2 credential rotation (90 d cadence; emergency
  `AdminUserGlobalSignOut` via BWG support).
- §3 TLS-chain regression response.
- §4 vendor firmware-update response.
- §5 vendor ToS / privacy-policy change response.
- §6 backup hygiene.
- §7 incident-response one-paragraph runbook.
- §8 decommissioning.

Cross-cutting operational artifacts:

- `docs/redaction-policy.md` row append on first activation of any
  `S-BAL-*` marker (`phase-0-bootstrap.md §0.2.3`).
- `docs/logbook.md` entry on every checklist run, rotation, and
  vendor-update response (`integration/validation-checklist.md` step 8).
- Researcher-side `captures/rotation-log.md.redacted` for §2.

## 3.5 Dual-use reflection

Full text in `integration/dual-use.md`. Summary for citation from
`paper/main.md`:

The Balboa Gateway Ultra case-study sits between Spider Farmer
(no auth; obscurity = security) and Ondilo (clean OAuth2; the issue
is bearer-token longevity). Balboa has **real cryptographic
authentication** (Cognito bearer over TLS) but a **weak operational
layer** (broken intermediate chain since June 2023; `TrustAllStrategy`
on the classpath; no in-app revocation; public mobile client
secret; cross-vendor data flow to a sister brand). The artifacts
that enable interoperability — the APK, the cloud REST inventory,
the public client secret — are the same artifacts that enable
command injection by anyone holding stolen credentials. The
case-study contribution is to put the gap on the academic record
in a form the vendor cannot dismiss as obscure: the integration
discipline (six C-1..C-6 controls) **shrinks the household's
exposure window** but **cannot fix the vendor-side gap**. Closing
that gap requires BWG to (a) repair the TLS chain, (b) remove
`TrustAllStrategy`, (c) treat `/spas/claim` as an authenticated
re-keying operation, (d) ship an in-app revocation UI.

## 3.6 Phase 3 user-facing summary (for the close-out checkpoint)

- **What was built.** A configuration-only integration package
  under `experiments/iot-integrator-balboa-gateway-ultra/integration/`:
  five Markdown files + one Python smoke test + a six-control
  hardening overlay (C-1..C-6) wrapping the upstream MQTT bridge.
- **What was validated.** Static cross-implementation validation of
  the ES-6 endpoint surface against the APK 4.1.9 strings; identity
  provider topology resolved; permission-vs-control-surface
  consistency confirmed.
- **What was not validated.** Live end-to-end (login → state read →
  one bounded write). This is the researcher-side
  `validation-checklist.md` run; the resulting log goes into
  `captures/phase-3-validation.log.redacted`.
- **Residual risks.** W-3 (TrustAllStrategy reachability) until §A
  jadx run; W-5 (WaterGuru cross-vendor flow conditionality) until
  §A; OQ-2 (signed firmware OTA) until §C live capture; OQ-3 (BWG
  vs Perfect Spa GDPR controller) until §D SAR.
- **Recommended follow-ups.** §A DEX deep-dive (researcher-side, ~30
  min on a workstation with `apktool` + `jadx`); §D SAR with both
  BWG and WaterGuru (paper-grade evidence; open-ended timeline).

## 3.7 Deliverable status

- `integration/README.md` ✓
- `integration/smoke-test.py` ✓
- `integration/operational-notes.md` ✓
- `integration/validation-checklist.md` ✓
- `integration/dual-use.md` ✓
- `process/phase-3-implementation.md` (this file) ✓
- Logbook entry: pending (this commit).
- `docs/redaction-policy.md`: no rows added in Phase 3 (researcher
  activates `S-BAL-*` markers on first use during the
  `validation-checklist.md` run).
- User checkpoint (Phase 3 → close-out): pending researcher
  acceptance; close-out follows.
