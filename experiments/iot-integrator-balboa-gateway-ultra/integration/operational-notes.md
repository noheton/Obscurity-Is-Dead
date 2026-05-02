# Operational Notes — Balboa Gateway Ultra (ControlMySpa cloud)

> Companion to `README.md`. These notes are **runbook-shaped**: each
> section describes a recurring operation, the expected steady state,
> the symptom of failure, and the remediation step. Designed for the
> household operator (Phase 0 persona).

## 1. Daily / weekly steady state

| Indicator | Expected | Remediation if not |
|---|---|---|
| `binary_sensor.online` | `on` | check Wi-Fi RSSI at the spa, then `iot.controlmyspa.com` reachability from the bridge host |
| `sensor.last_command_status` | `ok` (or last successful command name) | inspect HA logs for `401` (token expired), `5xx` (BWG-side outage), `SSLError` (TLS chain — see §3 below) |
| HA log: TLS errors | none | apply the certifi patch documented in `README.md` §2 step 3; never bypass with `verify=False` |
| HA log: rate-limit / 429 | none | raise the bridge poll interval to ≥ 60 s; ES-6 has no built-in throttle |
| Pi-hole / AdGuard query log | no traffic to `pagead2.googlesyndication.com`, `googleadservices.com`, `api.waterguru-prod.com` | verify the C-2 sinkhole entries are still installed (filter-list updates can revert them) |

## 2. Credential rotation (C-5)

Frequency: every 90 d. Earlier if you suspect compromise (lost
phone, suspicious BWG email, disclosure of a household password
elsewhere).

1. Log in to the ControlMySpa app (vendor) and change the password.
2. Update the bridge's `CONTROLMYSPA_PASS` env var.
3. Restart the bridge container.
4. Run `smoke-test.py` to confirm the new credential works.
5. Append a one-line entry to `captures/rotation-log.md.redacted`:
   `YYYY-MM-DD rotated; smoke-test ok`. **Do not** record the old or
   new password — the timestamp is the audit value.

The 30-day Cognito refresh-token TTL means a stale device that
cached the old refresh token can survive up to 30 days *unless* you
ask BWG support to perform an `AdminUserGlobalSignOut`. For routine
rotations the 30-day clock is acceptable; for incident response it
is not — escalate to support.

## 3. Vendor outages and TLS-chain regressions

The `iot.controlmyspa.com` host has shown a broken intermediate-CA
chain since June 2023 (`process/phase-1-research.md §1.2.3`).
Symptoms in the bridge log:
```
SSLError: certificate verify failed: unable to get local issuer certificate
```

Remediation, in order of preference:

1. Wait — sometimes the chain re-converges after a few hours when
   BWG's load balancer reissues. Many libraries (including ES-6)
   already attempt to repair the chain at load time; check the
   bridge image is on a recent build.
2. Update `certifi` to a version whose CA bundle includes the
   missing intermediate. Do not pin an old `certifi`.
3. Append the documented intermediate to the bridge image's
   `certifi/cacert.pem` per the ES-6 README — but only after
   fetching it from `cacerts.digicert.com` over a verified channel
   and recording its SHA-256 in your operations log.
4. **Never** add `verify=False` or a `TrustAllStrategy` workaround.
   That converts W-3 from "imported but possibly unreachable" to
   "definitely reachable" and changes the household's MITM exposure.

If BWG has rolled a wider outage, the bridge will simply report
`5xx`. HA `binary_sensor.online` flips to `off` and any setpoint
write you queue will fail; restore happens automatically.

## 4. Vendor pushes a firmware update that breaks the integration

Symptoms: the smoke test still passes (login + state read work) but
specific endpoints return `400` / `404`. Most likely causes:

- a `/spa-commands/*` path is renamed (rare; the surface is stable
  across the ES-6 4.0.0 release window);
- a new field appears in the state read that ES-6's parser drops;
- the Cognito user-pool client is rotated and your stored bearer
  token becomes invalid (resolves itself on the next login).

Response:

1. Re-run `smoke-test.py`.
2. Compare the log entries for `Cognito` token issuance and
   `https://iot.controlmyspa.com/...` paths against
   `process/phase-2-weakness.md §2.1.2`.
3. If a new endpoint is suspected, run the §A DEX deep-dive on the
   *new* APK version, diff the endpoint list against the 4.1.9
   inventory in §2.1.2, and append the findings to
   `process/phase-2-weakness.md` as an addendum (do not rewrite
   history).

## 5. Vendor pushes a ToS or privacy-policy change

The ControlMySpa account is bound by the ToS at
`https://iot.controlmyspa.com/portal/terms-of-use.html` and the BWG
privacy policy. Material changes (data-sharing expansion, new
processors, change of controller jurisdiction) are notified by
email to the account address. Recommendation:

1. Forward the change notice to the household research-archive
   mailbox.
2. If the change introduces a new processor (e.g. another Helios
   sister brand beyond WaterGuru), update `process/phase-2-weakness.md
   §2.1.3` with a new row.
3. Re-evaluate whether the configuration-only Phase 3 outcome still
   holds, or whether the integration shape needs to be retired
   (revert to `T-DO-NOT-INTEGRATE`).

## 6. Backup hygiene (C-6)

HA snapshots include `secrets.yaml` in cleartext. Mitigations:

- Enable HA Cloud encryption, or push snapshots to a Borg-encrypted
  remote, or rclone-encrypt-then-push.
- Restrict snapshot access on the destination (S3 IAM, NAS share,
  etc.) to the household admin.
- **Do not** check snapshots into this repository (they would carry
  the cleartext credential into git, which is precisely what rule
  12 protects against).

## 7. Incident response (one-paragraph runbook)

Trigger: any one of (a) BWG-side breach disclosure, (b) lost
household device with cached ControlMySpa credentials, (c)
unexpected setpoint/jet activity in HA logs that nobody in the
household initiated.

Do, in order:

1. Rotate the password (§2 above).
2. Email BWG support requesting `AdminUserGlobalSignOut` on the
   account; otherwise stale refresh tokens survive up to 30 days.
3. Power-cycle the spa gateway (drops the FCM session at the
   device).
4. Review HA's command-history log for the previous 30 days and
   reconcile with household members.
5. File an SAR with BWG and WaterGuru asking for the cloud-side
   audit trail. Append the redacted response to
   `captures/sar-response-bwg.md.redacted` and
   `captures/sar-response-waterguru.md.redacted`.
6. If credentials were also reused elsewhere, rotate those too.
   Treat this as a generic credential-leak exercise; the
   integration is incidental to the incident.

## 8. Decommissioning

Follow `README.md` §5 ("Uninstall"). Then:

- After 30 days, re-attempt login from a fresh client; the cached
  refresh tokens should be expired by then.
- File a SAR/erasure request with BWG (Art. 17 GDPR) for full
  account deletion. Note: erasure under Art. 17 may be refused if
  BWG argues legitimate interest in retaining warranty/support
  history; record the response.
