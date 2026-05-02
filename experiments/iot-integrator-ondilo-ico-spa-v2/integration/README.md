# Ondilo ICO Spa V2 — Home Assistant integration (configuration-only)

This folder is the **runnable artifact** produced by Phase 3 of the
`iot-integrator-ondilo-ico-spa-v2` case study. It does **not** contain a
custom_component. The chosen integration shape is *configuration-only
adoption* of the existing HA core integration `ondilo_ico`, paired with the
operational mitigations recorded in `operational-notes.md`.

The rationale for not shipping new code is in
`../process/phase-3-implementation.md` §3.2: the upstream integration
already satisfies the read-only intake exactly, and producing a parallel
component would violate the prompt's §3.1 scope-creep rule without any
privacy benefit.

## Setup checklist (researcher-side)

> Skim `operational-notes.md` first — at least §3.4.1 (pool-nickname alias)
> needs to be done **before** the OAuth flow.

1. **Pool-nickname alias** (`operational-notes.md` §3.4.1). Rename the pool
   to a non-identifying alias such as `Spa` in the official Ondilo app or
   web account.
2. **Confirm device is reporting to the cloud.** The official Ondilo app
   should show a recent measurement; HA cannot synthesise data the cloud
   has not received.
3. **Enable HA `application_credentials`.** Already enabled in default HA
   core builds.
4. **Add the integration in HA.** `Settings → Devices & services → Add
   integration → Ondilo ICO`. Follow the OAuth prompts in your browser;
   sign in with the Ondilo account that owns the pool.
5. **Wait one device cycle (~65 minutes).** The seven sensor entities
   should populate. If they do not, see §3.3.3 of
   `../process/phase-3-implementation.md`.
6. **Run `validation-checklist.md`** to record a redacted excerpt of
   `home-assistant.log` under `../captures/phase-3-validation.log.redacted`.

## Files

- `README.md` — this file.
- `operational-notes.md` — rotation, monitoring, backup hygiene.
- `validation-checklist.md` — runnable researcher-side checklist with
  redaction reminders.
- `dual-use.md` — rule-5 dual-use mirror, narrow form.
- `smoke-test.py` — optional Python verifier, runs *outside* HA, no token
  is read or written by this script (placeholders only).

## What this artifact intentionally does **not** do

- It does not embed any token, account email, pool ID, device UUID, or
  household-identifying string. All such values stay in HA's credential
  store or in `../captures/` under redaction.
- It does not modify the researcher's HA configuration. The researcher
  performs steps 1–6 above interactively.
- It does not bypass, MITM, or reimplement the vendor cloud. The cloud is
  the only data source for HA in this shape; alternatives are documented
  in `../process/phase-1-research.md` §1.4 and rejected for this Phase 3.
