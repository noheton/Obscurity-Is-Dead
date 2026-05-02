"""
Optional smoke-test for the Ondilo ICO Spa V2 → Home Assistant integration.

This script is *not* required by the configuration-only Phase 3 artifact;
it is provided so the researcher can independently confirm that:

  1. The Ondilo Customer API at interop.ondilo.com is reachable from the
     researcher's egress IP.
  2. The `ondilo` PyPI library used by the HA core integration imports
     and presents the expected method surface.

The script never reads, writes, or stores a real token. The TOKEN_DICT
below is a placeholder; the researcher fills it in only if they want to
run the live read step, and removes it after the run.

Compatible with:
  - ondilo == 0.5.0  (HA core ondilo_ico requirement, Phase 1 §1.1 ES-1)

Usage:
  python3 smoke-test.py            # offline checks only
  python3 smoke-test.py --live     # also try get_pools() (requires token)
"""

from __future__ import annotations

import argparse
import sys


REQUIRED_API_METHODS = (
    "get_pools",
    "get_ICO_details",
    "get_last_pool_measures",
    "get_pool_recommendations",
    "validate_pool_recommendation",
    "get_user_units",
    "get_user_info",
    "get_pool_config",
    "get_pool_shares",
    "get_pool_histo",
)

# Placeholder. Do not paste a real token. If the researcher wants to run
# --live, they should construct TOKEN_DICT from their own HA
# .storage/application_credentials, run the script once, then DELETE the
# value before saving the file.
TOKEN_DICT = {
    "access_token": "[REDACTED:credential:S-OND-3-access]",
    "refresh_token": "[REDACTED:credential:S-OND-2-refresh]",
    "token_type": "Bearer",
    "expires_at": 0,
}


def offline_checks() -> int:
    try:
        import ondilo  # type: ignore[import-not-found]
    except ImportError:
        print("FAIL: 'ondilo' package not installed. `pip install ondilo==0.5.0`")
        return 1

    print(f"OK: ondilo version = {getattr(ondilo, '__version__', 'unknown')}")

    try:
        client_cls = ondilo.Ondilo
    except AttributeError:
        print("FAIL: ondilo.Ondilo class not present")
        return 1

    missing = [m for m in REQUIRED_API_METHODS if not hasattr(client_cls, m)]
    if missing:
        print(f"FAIL: missing methods on ondilo.Ondilo: {missing}")
        return 1

    print(f"OK: all {len(REQUIRED_API_METHODS)} expected methods present on ondilo.Ondilo")
    return 0


def live_check() -> int:
    if TOKEN_DICT["access_token"].startswith("[REDACTED:"):
        print("SKIP: TOKEN_DICT is unfilled placeholder; --live requires real token.")
        return 0

    import ondilo  # type: ignore[import-not-found]

    client = ondilo.Ondilo(
        token=TOKEN_DICT,
        client_id="customer_api",
        client_secret="",
    )
    pools = client.get_pools()
    print(f"OK: get_pools returned {len(pools)} record(s).")
    # Intentionally do not print pool details — they are pii/uid per Phase 2 §2.5.
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live", action="store_true", help="Also try a real GET /pools call.")
    args = parser.parse_args()

    rc = offline_checks()
    if rc != 0:
        return rc
    if args.live:
        rc = live_check()
    return rc


if __name__ == "__main__":
    sys.exit(main())
