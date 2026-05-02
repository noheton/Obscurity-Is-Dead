# Validation checklist — researcher-side

Run this once after the OAuth setup in `README.md`. It produces a single
redacted artifact under `../captures/phase-3-validation.log.redacted`.

Apply the redaction markers from `../process/phase-2-weakness.md` §2.5 at
**capture time**, not retroactively, per `CLAUDE.md` rule 12. The marker
catalogue:

| Marker | Replace |
|--------|---------|
| `[REDACTED:username:S-OND-1-account]` | researcher's Ondilo account email |
| `[REDACTED:credential:S-OND-2-refresh]` | refresh token fragments |
| `[REDACTED:credential:S-OND-3-access]` | access token fragments |
| `[REDACTED:uid:S-OND-4-pool]` | pool/spa identifier |
| `[REDACTED:uid:S-OND-5-device]` | device identifier |
| `[REDACTED:pii:S-OND-6-nickname]` | residual nickname leftovers |
| `[REDACTED:geo:S-OND-7-timezone]` | narrow timezone strings |
| `[REDACTED:serial:S-OND-8-uuid]` | device UUID (the BLE-Scanner one) |

## Steps

- [ ] **VC-1.** Wait one full device cycle (~65 minutes) after the
      integration is added in HA. Confirm all seven sensors have a
      non-`unknown` state in `Settings → Devices → Ondilo ICO`:
      temperature, oxydo_reduction_potential, ph, tds, battery, rssi, salt.
- [ ] **VC-2.** From the HA host, capture the relevant log section:

      ```
      grep -E "ondilo_ico|OndiloError|UpdateFailed" /config/home-assistant.log \
        | tail -n 200 > /tmp/ondilo-validation.log
      ```

- [ ] **VC-3.** Open `/tmp/ondilo-validation.log` and apply the markers
      above to **every** sensitive value before saving. In particular:
      anywhere a token is logged at DEBUG, anywhere the pool or device ID
      appears, anywhere the nickname leaks despite the §3.4.1 alias.
- [ ] **VC-4.** Save the redacted result as
      `experiments/iot-integrator-ondilo-ico-spa-v2/captures/phase-3-validation.log.redacted`.
- [ ] **VC-5.** Append a row to `docs/redaction-policy.md` for **each
      marker actually used** (not the unused ones), per
      `CLAUDE.md` rule 12.
- [ ] **VC-6.** Run the pre-commit redaction grep before `git add` /
      `git commit`:

      ```
      git diff --cached | grep -nE 'eyJ|ghp_|xoxb-|Bearer |-----BEGIN' && echo "ABORT" || echo "ok"
      ```

      Abort and re-redact if anything matches.
- [ ] **VC-7.** Commit with message
      `iot-integrator: Ondilo ICO Spa V2 Phase 3 validation log (redacted)`.

## Negative path

If VC-1 fails (sensors stay `unknown` after 65 minutes):

- Confirm the official Ondilo app shows a recent measurement. If the cloud
  has none, HA cannot create one.
- Re-authenticate the integration. This issues a fresh refresh token and
  is the standard recovery for the Phase 2 W-3 silent-failure case.
- If still failing, open an HA core issue against `ondilo_ico` and
  reference the redacted excerpt.
