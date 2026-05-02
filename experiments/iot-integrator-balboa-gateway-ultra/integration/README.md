# Integration — Balboa Gateway Ultra (ControlMySpa cloud, configuration-only)

> Author attribution: drafted by AI agent (Claude Opus 4.7) under
> `docs/prompts/iot-integrator-prompt.md`. Researcher review pending.
>
> Phase 3 outcome category: **`T-CONFIG-ONLY-OUTCOME`**
> (the Phase 0→1 declared control surface is already covered by an
> existing open-source library; this folder ships a documented
> integration pattern + hardening overlay + smoke test, **not** a
> parallel `custom_components/` module).
>
> Cloud-touching authorisation: **explicitly granted by the
> researcher at the Phase 2→3 checkpoint** ("2, cloud confirmed,
> drop at publication", 2026-05-02). All endpoints listed below
> contact the BWG cloud (`iot.controlmyspa.com`) and AWS Cognito
> (`cognito-idp.us-west-2.amazonaws.com`). There is no LAN-only
> alternative — see `process/phase-2-weakness.md §2.4.1`.

## 1. Design

| Field | Value |
|---|---|
| Integration shape | configuration-only adoption of an existing open-source bridge + a hardening overlay + a smoke test. |
| Backing library | `controlmyspa` 4.0.0 (PyPI, MIT, `[REDACTED:repo-path:BALBOA-UPSTREAM-2]`). Used directly by the smoke test; recommended underneath any researcher-supplied HA glue. |
| Recommended HA runtime | `[REDACTED:repo-path:BALBOA-UPSTREAM-1]` (GPL-3.0, MQTT bridge). It already publishes climate + sensors + switches via MQTT auto-discovery. The hardening overlay in `operational-notes.md` is what this folder adds. |
| Data model | one `climate` entity (setpoint, current temp, heater mode, temp range, temp scale, panel lock); per-component `switch`/`number`/`light` entities for jets, blowers, lights, chromozone (state / colour / intensity / power / speed), c8zone, filter cycles; read-only `binary_sensor.online`, `sensor.last_command_status`. Endpoint inventory: `process/phase-2-weakness.md §2.1.2`. |
| Credential storage | HA `secrets.yaml`, file-mode `0600`, encrypted backups. Two secrets: `controlmyspa_user` (email) and `controlmyspa_pass` (password). **Do not** check secrets into git. The smoke test reads them from environment variables `CONTROLMYSPA_USER` / `CONTROLMYSPA_PASS`. |
| Failure modes | (a) TLS chain breakage at `iot.controlmyspa.com` — see §2; (b) Cognito refresh-token expiry after 30 d of inactivity — see `operational-notes.md`; (c) Google-ad-host calls (W-6) — sinkhole at network edge; (d) WaterGuru cross-vendor flow (W-5) — sinkhole at network edge or file SAR; (e) ES-6 has no rate-limit handling — poll cadence ≥ 60 s recommended. |

The researcher's declared privacy boundary ("as local as possible /
only escalate to cloud if necessary", Phase 0→1 / Phase 1→2 intake)
is **partially honoured** here: the spa-control surface itself is
unavoidably cloud-bound (W-2), but everything *outside* the
spa-control path (Google Ads, WaterGuru cross-vendor, FCM push
beyond what HA needs) is explicitly disabled or sinkholed by the
hardening overlay below.

## 2. Install (smallest path, summarised)

A reproducible install for a household HA instance:

1. **Install the MQTT bridge** as a docker container or as a HA add-on (instructions in the upstream repo). License: GPL-3.0.
2. **Pin and re-verify** the upstream image's tag against its
   git commit before pulling; the project does not publish tagged
   releases at the time this case was authored
   (`process/phase-2-weakness.md §1.1.2 ES-7`).
3. **Patch the TLS chain**. The bridge's underlying client may fail
   to validate `iot.controlmyspa.com`'s leaf certificate because the
   host has not served a complete intermediate chain since June 2023.
   Two acceptable fixes, in order of preference:
   - upgrade to a `certifi` build that bundles the missing DigiCert
     intermediate (researcher to verify the bridge's
     pinned `certifi` version);
   - **as a last resort**, append the documented intermediate to
     `certifi/cacert.pem` per the ES-6 README — but only after
     manually fetching it from `cacerts.digicert.com` over a
     verified channel and confirming its SHA-256. **Do not** disable
     TLS verification (do not pass `verify=False` anywhere); this
     converts the existing W-3 from "imported but possibly
     unreached" to "definitely reachable".
4. **Configure secrets** in HA `secrets.yaml`:
   ```yaml
   controlmyspa_user: !env_var CONTROLMYSPA_USER
   controlmyspa_pass: !env_var CONTROLMYSPA_PASS
   ```
   Set `CONTROLMYSPA_USER` and `CONTROLMYSPA_PASS` in the bridge's
   docker-compose `env_file` with file-mode `0600`.
5. **Apply the hardening overlay** in `operational-notes.md`
   (network-edge sinkhole, secondary-onboarding device, rotation
   schedule, monitoring).
6. **Run the smoke test** (`smoke-test.py`) — see §4. It must pass
   before any HA automation is allowed to trigger writes.

## 3. Hardening overlay (this is the value this folder adds)

Six controls, all installable independently. Each control has a
weakness ID it answers (from `process/phase-2-weakness.md §2.3`).

| Control | Mitigates | Recipe (one line) |
|---|---|---|
| C-1 Secondary onboarding device | manifest exposure (W-8) | First-time pair the spa from a throwaway Android profile that has no household Google account, then uninstall the app on that profile. |
| C-2 Network-edge sinkhole | W-5 (WaterGuru) + W-6 (Google ads) | Add `api.waterguru-prod.com`, `pagead2.googlesyndication.com`, and `googleadservices.com` to your Pi-hole / AdGuard Home block list. The bridge does not need any of these to operate. |
| C-3 Spa nickname alias | telemetry-as-occupancy proxy | Set the spa nickname in the vendor app to a non-identifying string (e.g. `spa-1`) **before** wiring HA. ControlMySpa's audit log will retain the nickname; the alias keeps the household name out of it. |
| C-4 Dedicated email alias | ControlMySpa account exposure | Use a `+spa@` plus-tag or a Fastmail/Anonaddy alias as `controlmyspa_user`, not the household primary email. |
| C-5 Cognito password rotation schedule | W-1 (refresh-token persistence) | Rotate the password every 90 d. Document the rotation date in `captures/rotation-log.md` (researcher-side; not committed). |
| C-6 HA backup encryption | secrets in backup | HA backups are not encrypted by default; enable HA Cloud or Borg encryption on the backup destination. The cleartext `controlmyspa_pass` is otherwise inside every snapshot. |

Five **explicitly not done** controls (recorded so a future
re-evaluation can revisit):

- **No certificate pinning** at the integration layer. The vendor's
  TLS posture is too fragile to pin against. The W-3 dual-use
  exposure stays open until BWG fixes the chain.
- **No HA automation that writes setpoint > 40°C / 104°F** —
  documented in `validation-checklist.md` step 5; safety-side, not
  privacy-side.
- **No outbound rule that *blocks* `iot.controlmyspa.com`** — the
  device is non-functional without it; a partial block creates
  silent staleness.
- **No DEX-decompile / smali patching of the official APK.** The
  researcher may run `§A` from `phase-2-weakness.md` for evidence,
  but redistributing a patched APK is outside this folder's scope.
- **No exfiltration of DSN, push tokens, or audit-log entries** to
  `provenance.md`; redaction discipline keeps these out per
  `phase-0-bootstrap.md §0.2.3`.

## 4. Smoke test

`smoke-test.py` — minimal validation that the credentials work and
the spa is reachable, **read-only**, no writes. Run with
`CONTROLMYSPA_USER` / `CONTROLMYSPA_PASS` in the environment:

```
$ CONTROLMYSPA_USER='[REDACTED:username:S-BAL-4]' \
  CONTROLMYSPA_PASS='[REDACTED:credential:S-BAL-1]' \
  python3 smoke-test.py
```

The script prints a redacted state summary on success. It does not
write to disk; it does not issue any `POST /spa-commands/*`
endpoint. Researchers wanting to test the write surface should
extend the script in a separate file and document the activation in
`captures/`.

See `validation-checklist.md` for the full 8-step researcher
checklist that wraps this smoke test.

## 5. Uninstall

1. `docker compose down` the MQTT bridge and remove its data volume.
2. Remove the MQTT entities from HA (Settings → Devices & Services).
3. Rotate the ControlMySpa password (so the long-lived refresh
   token a stale install may still hold becomes invalid on its
   30-day clock — and on a force-signout from BWG support if you
   want it to be invalid sooner).
4. Optional: open a SAR with BWG (and WaterGuru, W-5) to recover
   any data they hold from the integration's lifetime.
5. **Do not** delete the audit-log entries in
   `experiments/iot-integrator-balboa-gateway-ultra/`; they are
   research artifacts.

## 6. References

- `process/phase-0-bootstrap.md` — Technique Inventory + Target Intake.
- `process/phase-1-research.md` — Vendor / ecosystem / candidate-interface map.
- `process/phase-2-weakness.md` — Weakness Table W-1..W-8 + Privacy & Security Review + researcher-runnable §A..§D protocols.
- `process/phase-3-implementation.md` — design, validation log, operational notes, dual-use reflection.
- ES-6 source: `https://github.com/[REDACTED:repo-path:BALBOA-UPSTREAM-2]`, PyPI `controlmyspa==4.0.0`, MIT.
- ES-7 source: `https://github.com/[REDACTED:repo-path:BALBOA-UPSTREAM-1]`, GPL-3.0.

## 7. Rule-12 retention decision (researcher decision, recorded for audit)

The researcher confirmed at the Phase 2→3 checkpoint that the
vendor-copyrighted XAPK
(`original/ControlMySpa_4.1.9_APKPure.xapk`,
SHA-256 `c851b25…`) **stays in git for the working branch** and
**will be `git rm`'d before any Zenodo / arXiv publication step**.
The SHA-256 anchors in `process/phase-2-weakness.md §2.0` are the
permanent evidence anchor. This matches CLAUDE.md rule 12
(`legal-grey`) and rule 13 (no public push without explicit
consent).
