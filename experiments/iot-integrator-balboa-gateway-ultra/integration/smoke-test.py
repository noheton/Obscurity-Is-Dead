#!/usr/bin/env python3
"""
Minimal read-only smoke test for the ControlMySpa cloud integration.

Phase 3 deliverable for `experiments/iot-integrator-balboa-gateway-ultra/`.

The script logs in once with credentials supplied via environment
variables, retrieves the spa state, and prints a redacted summary.
It performs no `POST /spa-commands/*` writes. It does not persist
anything to disk.

Researcher prerequisites
------------------------
- `pip install controlmyspa==4.0.0` (PyPI, MIT, `[REDACTED:repo-path:BALBOA-UPSTREAM-2]`).
- `CONTROLMYSPA_USER` and `CONTROLMYSPA_PASS` exported in the
  environment. Do not pass them on the command line (they would
  appear in the shell history). Use a `.env` file with `chmod 0600`
  or your password manager's CLI.
- The host running this script must reach `iot.controlmyspa.com`.
  See `README.md` §2 step 3 for the TLS-chain caveat.

Exit codes
----------
- 0   success (login + state read worked)
- 1   missing environment variable
- 2   import failure (`controlmyspa` not installed)
- 3   login or read failure

Redaction
---------
Per `process/phase-0-bootstrap.md §0.2.3`, the script substitutes
`[REDACTED:<type>:<marker>]` for any value that would otherwise leak
a credential, account email, DSN, UID, or geo string. The redacted
summary is safe to paste into a research transcript.
"""

from __future__ import annotations

import os
import sys


REDACT_USERNAME = "[REDACTED:username:S-BAL-4]"
REDACT_DSN = "[REDACTED:serial:S-BAL-5]"
REDACT_UID = "[REDACTED:uid:S-BAL-7]"


def _require_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        print(f"missing environment variable: {name}", file=sys.stderr)
        sys.exit(1)
    return value


def main() -> int:
    user = _require_env("CONTROLMYSPA_USER")
    password = _require_env("CONTROLMYSPA_PASS")

    try:
        from controlmyspa import ControlMySpa
    except ImportError:
        print(
            "controlmyspa is not installed. Run: pip install controlmyspa==4.0.0",
            file=sys.stderr,
        )
        return 2

    try:
        api = ControlMySpa(user, password)
    except Exception as exc:
        print(f"login or initial fetch failed: {type(exc).__name__}", file=sys.stderr)
        return 3

    info = getattr(api, "_info", None)
    if not info:
        print("logged in but no spa info returned", file=sys.stderr)
        return 3

    print("ControlMySpa smoke test — redacted summary")
    print("------------------------------------------")
    print(f"account              : {REDACT_USERNAME}")
    print(f"spa_id               : {REDACT_UID}")
    print(f"spa_serial           : {REDACT_DSN}")
    print(f"online               : {bool(getattr(api, 'online', None))}")
    print(f"current_temp         : {getattr(api, 'current_temp', None)}")
    print(f"desired_temp         : {getattr(api, 'desired_temp', None)}")
    print(f"temp_range           : {getattr(api, 'temp_range', None)}")
    print(f"heater_mode          : {getattr(api, 'heater_mode', None)}")
    print(f"panel_lock           : {getattr(api, 'panel_lock', None)}")
    print(f"jets (count)         : {len(getattr(api, 'jets', []) or [])}")
    print(f"blowers (count)      : {len(getattr(api, 'blowers', []) or [])}")
    print(f"lights (count)       : {len(getattr(api, 'lights', []) or [])}")
    print(f"circulation_pumps    : {len(getattr(api, 'circulation_pumps', []) or [])}")
    print(f"ozone_generators     : {len(getattr(api, 'ozone_generators', []) or [])}")
    print()
    print("smoke test ok — no writes were issued")
    return 0


if __name__ == "__main__":
    sys.exit(main())
