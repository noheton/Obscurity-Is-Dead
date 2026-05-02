# Operational notes — Ondilo ICO Spa V2 in Home Assistant

These notes are the operational side of the configuration-only artifact
described in `README.md`. They condense the relevant subsections of
`../process/phase-3-implementation.md` §3.4 into a one-screen runbook the
researcher can refer back to without re-reading the full phase report.

## §3.4.1 Pre-onboarding — pool-nickname alias

Rename the pool to a non-identifying alias (e.g. `Spa`) in the Ondilo
account **before** authorising HA's OAuth flow. The alias propagates into
HA's device registry, recorder DB, and backups, so the time to do this is
*before* HA ever reads it.

## §3.4.2 Refresh-token rotation

Refresh tokens are documented as non-expiring (Phase 2 W-2). Rotate by
deleting the HA config entry and re-adding the integration:

- **Routine:** every 6–12 months.
- **Incident:** immediately after any HA backup leaves the household
  (third-party cloud upload, support attachment, copy to a different
  machine).
- **Belt-and-braces:** after rotation, change the Ondilo account password
  to invalidate any outstanding refresh tokens.

## §3.4.3 Monitor for silent staleness

The HA coordinator does not handle 429 / token-refresh failure (Phase 2
W-3); the failure mode is "no updates" rather than a loud error. Two
cheap watchdogs:

- HA automation: trigger when
  `now() - states.sensor.<pool>_temperature.last_updated > timedelta(hours=4)`.
- Periodic check of `home-assistant.log` for `OndiloError` and `UpdateFailed`
  emitted by `homeassistant.components.ondilo_ico`.

## §3.4.4 Avoid quota collisions

Vendor quota: 5 req/s, 30 req/h **per user**. HA's own polling is well
under the limit, but a parallel high-frequency client on the same Ondilo
account (Node-RED flow, second HA, mobile app left actively browsing) can
starve HA. Avoid running two authenticated clients during the day.

## §3.4.5 Backup hygiene

- Encrypt HA backups at rest with a passphrase HA does not also store.
- Treat any backup leaving the household as a credential-leak event and
  rotate per §3.4.2.
- Never paste an HA `.tar` snapshot or the `.storage/application_credentials`
  file into a public chat, issue tracker, or AI assistant.

## §3.4.6 Vendor change response

If the integration breaks after a vendor firmware or API change:

1. Read `OndiloError` and `UpdateFailed` lines from `home-assistant.log`.
2. Do **not** patch the `ondilo` library or HA component locally; flag
   upstream (HA core issue tracker).
3. If the change touches OAuth or rate-limit contracts, re-open Phase 2
   §2.1.2 with new constants — the relevant Technique Inventory entries
   are `T-CROSS-IMPL-VALIDATION`, `T-OBSCURITY-VS-AUTH`, `T-BEARER-LIFETIME`.

## Uninstall

`Settings → Devices & Services → Ondilo ICO → ⋮ → Delete`. This removes the
config entry, the cached refresh token in HA, and the device registry
entry. The vendor account itself is unaffected and must be deleted via the
Ondilo app if that is also desired.
