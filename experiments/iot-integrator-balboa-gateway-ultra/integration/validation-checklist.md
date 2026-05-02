# Validation Checklist

Eight researcher-runnable steps that wrap `smoke-test.py`. Each step
states a precondition, a command, the expected result, and what to
do on failure. Run them in order; do not skip.

| # | Step | Precondition | Command | Expected | On failure |
|---|---|---|---|---|---|
| 1 | confirm credential storage | `secrets.yaml` exists, mode `0600` | `stat -c '%a %n' secrets.yaml` | `600 secrets.yaml` | `chmod 0600 secrets.yaml` and re-run |
| 2 | confirm Pi-hole / AdGuard sinkhole entries (C-2) | filter list active | DNS-resolve each host from the bridge container: `getent hosts api.waterguru-prod.com pagead2.googlesyndication.com googleadservices.com` | each resolves to `0.0.0.0` or your sinkhole IP | re-add the three hosts to your filter list and refresh |
| 3 | confirm `controlmyspa` package version | python on the bridge host | `python3 -c "import controlmyspa, sys; sys.stdout.write(controlmyspa.__version__ if hasattr(controlmyspa, '__version__') else 'no version attr')"` | `4.0.0` (or higher within the 4.x line) | `pip install -U controlmyspa==4.0.0` |
| 4 | run the smoke test | env vars set | `CONTROLMYSPA_USER=… CONTROLMYSPA_PASS=… python3 smoke-test.py` | exit 0; redacted summary printed; `online: True` | inspect `stderr` for `SSLError` (apply §3 of `operational-notes.md`), `401` (re-check credentials), `ImportError` (run step 3) |
| 5 | confirm setpoint range guard | HA YAML / bridge config | grep the bridge config for any automation that writes `temperature/value` > 40°C / 104°F | none | remove the offending automation; the safety guard is integrator-side, not vendor-side |
| 6 | confirm no plaintext credential in git | `git grep` | `git grep -n -E '(@[a-z0-9.-]+\.(com\|net\|io)\|password.*=)' experiments/iot-integrator-balboa-gateway-ultra/` | only the redacted forms `[REDACTED:credential:S-BAL-1]`, `[REDACTED:username:S-BAL-4]`, `…/spa@`, ES-6 example placeholders | `git reset` the offending file, redact, re-stage |
| 7 | confirm rule-12 markers logged | `docs/redaction-policy.md` | `grep -c 'S-BAL-' docs/redaction-policy.md` | one row per *activated* marker (zero rows is correct if the agent's static analysis is the only run so far; the row count grows when the researcher activates §C / live capture) | append the missing rows |
| 8 | record the validation in the logbook | `docs/logbook.md` open | append a one-paragraph entry naming this checklist run, the date, and the result | logbook ends with an entry whose timestamp is today | add the entry; do not commit a "ran the checklist" claim without one |

## Cloud-touching authorisation block (recorded for audit)

The Phase 2→3 user checkpoint produced explicit cloud authorisation
("2, cloud confirmed, drop at publication", 2026-05-02). All steps
above that contact `iot.controlmyspa.com` or
`cognito-idp.us-west-2.amazonaws.com` operate under that
authorisation. The authorisation is **scoped to this integration**
and **does not** extend to:

- enumerating accounts that are not the researcher's own;
- triggering mass-write fan-out across the spa command surface for
  load-test purposes;
- any of the §A / §B / §C / §D follow-ups in `process/phase-2-weakness.md`
  (each requires its own per-run authorisation).

If the integration is reset (factory reset of the spa, account
re-creation, change of household member as account owner), the
authorisation must be re-confirmed before re-running this
checklist.
