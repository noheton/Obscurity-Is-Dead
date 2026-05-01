#!/usr/bin/env python3
"""
Spider Farmer GGS-CB MQTT method discovery tool.

Connects to the local MQTT broker, subscribes to the device topic,
then probes each undocumented method with candidate payloads and logs
every response so you can map method names to working parameter shapes.

Usage
-----
  pip install paho-mqtt
  python tools/mqtt_discover.py --pid <PID> --uid <UID>

  # Listen-only mode (just capture what the device sends)
  python tools/mqtt_discover.py --pid <PID> --listen

Options
-------
  --broker      MQTT broker host  (default: localhost)
  --port        MQTT broker port  (default: 1883)
  --pid         Device PID, MAC without colons, e.g. 80F1B2B3B648  [required]
  --uid         User ID from Spider Farmer account  (default: 000000)
  --topic       Override topic    (default: SF/GGS/CB/API/UP/<pid>)
  --username    Broker username   (optional)
  --password    Broker password   (optional)
  --listen      Passive listen only, no probes
  --phase2      Run phase-2 targeted probes (setOnOff semantics, level control)
  --phase3      Run phase-3 topic-discovery probes (find real command topic)
  --listen-secs Seconds to listen before probing  (default: 10)
  --timeout     Seconds to wait for a response per probe  (default: 3)
  --tls         Connect with TLS (port auto-switches to 8883)
  --cafile      CA cert for TLS  (default: doc/certs/ca-sf.pem)
"""

import argparse
import asyncio
import json
import ssl
import sys
import time
from datetime import datetime
from pathlib import Path

try:
    import paho.mqtt.client as mqtt
except ImportError:
    print("ERROR: paho-mqtt not installed.  Run: pip install paho-mqtt")
    sys.exit(1)

# ── Noise filter: these stream every few seconds and drown out responses ──────
QUIET_METHODS = {"getDevSta", "getSysSta"}


def ts():
    return datetime.now().strftime("%H:%M:%S.%f")[:-3]


def envelope(method, data, pid, uid):
    return json.dumps({
        "method": method,
        "pid":    pid,
        "uid":    uid,
        "pcode":  1004,
        "UTC":    int(time.time()),
        "data":   data,
    })


# ── Probe definitions ─────────────────────────────────────────────────────────

def build_probes():
    """
    Returns list of (method, description, data) tuples.

    Goal: for each undocumented method, try the most plausible parameter
    shapes so we can see which one the device accepts (and what it replies).
    """
    now = int(time.time())
    return [
        # ── Read-only getters — safe, no side effects ─────────────────────
        ("getConfigFile", "empty data (getter)",   {}),
        ("getConfigFile", "null data",              None),

        # ── setOnOff — device power on / off ─────────────────────────────
        # Shape A: {devType: <string>, on: <0|1>}
        ("setOnOff", "light on  — devType string",   {"devType": "light",  "on": 1}),
        ("setOnOff", "blower on — devType string",   {"devType": "blower", "on": 1}),
        ("setOnOff", "fan on    — devType string",   {"devType": "fan",    "on": 1}),
        ("setOnOff", "heater on — devType string",   {"devType": "heater", "on": 1}),

        # Shape B: {devType: <int>, on: <0|1>}  (devType codes from oplogLast)
        # devType 16 = seen in alarmLast, 21 = seen in oplogLast for blower
        ("setOnOff", "devType 16 on",  {"devType": 16, "on": 1}),
        ("setOnOff", "devType 21 on",  {"devType": 21, "on": 1}),

        # Shape C: nested  {<key>: {on: 1}}
        ("setOnOff", "light on  — nested",  {"light":  {"on": 1}}),
        ("setOnOff", "blower on — nested",  {"blower": {"on": 1}}),

        # Shape D: flat  {device: <str>, on: <0|1>}
        ("setOnOff", "light on  — 'device' key", {"device": "light",  "on": 1}),

        # ── setMode — mode change (alternative to knob press) ────────────
        # Shape A: {devType: <string>, modeType: <int>}
        ("setMode", "blower manual — devType string", {"devType": "blower", "modeType": 0}),
        ("setMode", "blower auto   — devType string", {"devType": "blower", "modeType": 2}),
        ("setMode", "heater manual — devType string", {"devType": "heater", "modeType": 0}),
        ("setMode", "heater temp   — devType string", {"devType": "heater", "modeType": 3}),

        # Shape B: {devType: <int>, modeType: <int>}
        ("setMode", "devType 21 modeType 0",  {"devType": 21, "modeType": 0}),

        # Shape C: nested  {<key>: {modeType: <int>}}
        ("setMode", "blower manual — nested",  {"blower": {"modeType": 0}}),
        ("setMode", "heater temp   — nested",  {"heater": {"modeType": 3}}),

        # ── setDevTimezone — time sync ───────────────────────────────────
        # Described as "JSON ARRAY" but exact shape unknown
        ("setDevTimezone", "array [tz, offset, utc]", ["Europe/Berlin", 3600, now]),
        ("setDevTimezone", "array [tz, offset]",       ["Europe/Berlin", 3600]),
        ("setDevTimezone", "dict {timezone, tzoff}",   {"timezone": "Europe/Berlin", "tzoff": 3600}),
        ("setDevTimezone", "dict {timezone, offset}",  {"timezone": "Europe/Berlin", "offset": 3600}),

        # ── setDevSta debug — isolate why current commands are rejected ───
        # The integration uses setDevSta; let's test minimal variants
        ("setDevSta", "light on  — minimal (no level)", {"light": {"on": 1}}),
        ("setDevSta", "light off — minimal",             {"light": {"on": 0}}),
        ("setDevSta", "light on  — with level 30",       {"light": {"on": 1, "level": 30}}),
        ("setDevSta", "blower manual level 30",
            {"blower": {"modeType": 0, "on": 1, "level": 30}}),

        # ── setConfigFile — unknown; try empty to provoke an error reply ──
        ("setConfigFile", "empty data — see error shape", {}),
    ]


def build_probes_phase2():
    """
    Targeted probes based on phase-1 findings:

    Finding 1: 'setOnOff devType:blower on:1' caused the blower (which was
    already ON at lvl:30) to go OFF. Need to determine if setOnOff is a
    toggle command or whether on:1 = off semantics (inverted).

    Finding 2: All setDevSta commands were silently ignored (light stayed
    on=1 lvl=35 throughout). setDevSta may only work for level, not on/off,
    or may require manual mode to be set first.

    Finding 3: We need to know how to set the blower level — is it setDevSta
    with level, or does level go inside setOnOff?
    """
    return [
        # ── Q1: setOnOff semantics — set or toggle? ───────────────────────
        # Blower is currently OFF (from phase 1). If on:1 means "turn on",
        # this should bring it back. If it's a toggle, it will stay off.
        ("setOnOff", "blower ON (currently off) — expect ON if on:1=set",
            {"devType": "blower", "on": 1}),

        # Now blower should be on. Send on:0 — expect OFF if on:0=set.
        ("setOnOff", "blower OFF (currently on) — expect OFF if on:0=set",
            {"devType": "blower", "on": 0}),

        # Light is ON. Send on:0 — if semantics are correct, light goes off.
        ("setOnOff", "light OFF (currently on) — confirm on:0=off",
            {"devType": "light", "on": 0}),

        # Restore light on
        ("setOnOff", "light ON — restore",
            {"devType": "light", "on": 1}),

        # ── Q2: Does setOnOff accept a level? ────────────────────────────
        # Try sending level alongside on — may be how you set level too
        ("setOnOff", "blower on + level 50 — devType string",
            {"devType": "blower", "on": 1, "level": 50}),
        ("setOnOff", "blower level 75 — devType string (no on field)",
            {"devType": "blower", "level": 75}),
        ("setOnOff", "light level 50 — devType string",
            {"devType": "light", "on": 1, "level": 50}),

        # ── Q3: Does setDevSta work for level when mode is manual? ────────
        # First force blower to manual mode
        ("setMode", "blower → manual (modeType 0)",
            {"devType": "blower", "modeType": 0}),
        # Then try setDevSta level only (no on field)
        ("setDevSta", "blower level 40 — no on field (manual mode set)",
            {"blower": {"level": 40}}),
        # Then try with on field
        ("setDevSta", "blower on + level 40 (manual mode set)",
            {"blower": {"on": 1, "level": 40}}),
        # Full payload
        ("setDevSta", "blower full payload modeType+on+level",
            {"blower": {"modeType": 0, "on": 1, "level": 40}}),

        # ── Q4: Is there a dedicated setLevel method? ─────────────────────
        ("setLevel", "blower level 50",
            {"devType": "blower", "level": 50}),
        ("setLevel", "light level 50",
            {"devType": "light", "level": 50}),
        ("setLevel", "blower nested",
            {"blower": {"level": 50}}),

        # ── Q5: Restore blower to auto mode ──────────────────────────────
        ("setMode", "blower → auto (modeType 2) — restore",
            {"devType": "blower", "modeType": 2}),
    ]


# Candidate downlink topics — published to in phase-3
CANDIDATE_TOPICS = [
    "SF/GGS/CB/API/DOWN/{pid}",
    "SF/GGS/CB/API/DN/{pid}",
    "SF/GGS/CB/API/SET/{pid}",
    "SF/GGS/CB/{pid}",
    "SF/GGS/CB/API/UP/{pid}/cmd",
    "SF/GGS/CB/API/UP/{pid}/down",
]

# Simple command sent on each candidate topic to provoke a state change
_PHASE3_CMD = {"method": "setOnOff", "pcode": 1004,
               "data": {"devType": "light", "on": 0}}


# ── MQTT client wrapper ───────────────────────────────────────────────────────

class Probe:
    def __init__(self, broker, port, pid, uid, topic,
                 username=None, password=None, tls=False, cafile=None):
        self.broker   = broker
        self.port     = port
        self.pid      = pid
        self.uid      = uid
        self.topic    = topic
        self.responses = []
        self._current = None   # (method, description) of in-flight probe

        self._client = mqtt.Client(
            client_id=f"sf_discover_{int(time.time())}",
            protocol=mqtt.MQTTv311,
        )
        if username:
            self._client.username_pw_set(username, password)
        if tls:
            ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH,
                                             cafile=cafile)
            ctx.check_hostname = False
            self._client.tls_set_context(ctx)

        self._client.on_connect = self._on_connect
        self._client.on_message = self._on_message
        self._client.on_disconnect = self._on_disconnect

    def subscribe_wildcard(self):
        self._client.subscribe("#", qos=0)
        print(f"[{ts()}] Also subscribed → # (all topics)")

    def _on_connect(self, client, userdata, flags, rc):
        codes = {0: "OK", 1: "wrong protocol", 2: "bad client ID",
                 3: "server unavailable", 4: "bad credentials", 5: "not authorised"}
        if rc == 0:
            print(f"[{ts()}] Connected to {self.broker}:{self.port}")
            client.subscribe(self.topic, qos=0)
            print(f"[{ts()}] Subscribed → {self.topic}\n")
        else:
            print(f"[{ts()}] Connect FAILED: rc={rc} ({codes.get(rc, '?')})")

    def _on_disconnect(self, client, userdata, rc):
        if rc != 0:
            print(f"[{ts()}] Unexpected disconnect rc={rc}")

    def _on_message(self, client, userdata, msg):
        raw = msg.payload.decode(errors="replace")
        try:
            data   = json.loads(raw)
            method = data.get("method", "?")
            pretty = json.dumps(data, indent=2)
        except json.JSONDecodeError:
            method = "RAW"
            pretty = raw

        self.responses.append({
            "ts":     ts(),
            "topic":  msg.topic,
            "method": method,
            "data":   pretty,
            "probe":  self._current,
        })

        if method in QUIET_METHODS and msg.topic == self.topic:
            # Print a single-line summary so we know the device is alive
            dev = json.loads(raw).get("data", {})
            parts = []
            for k in ("light", "blower", "fan", "heater"):
                if k in dev:
                    d = dev[k]
                    parts.append(f"{k}(on={d.get('on','?')} lvl={d.get('level','?')})")
            print(f"  [{ts()}] {method}: {', '.join(parts) or '(no devices)'}", end="\r")
            return

        probe_tag = f"{self._current[0]}/{self._current[1]}" if self._current else "passive"
        topic_tag = f" topic={msg.topic!r}" if msg.topic != self.topic else ""
        print(f"\n[{ts()}] ←{topic_tag} [{probe_tag}]  method={method!r}")
        print(pretty)

    def start(self):
        self._client.connect(self.broker, self.port, keepalive=60)
        self._client.loop_start()

    def stop(self):
        self._client.loop_stop()
        self._client.disconnect()

    def publish(self, method, data, desc):
        self._current = (method, desc)
        payload = envelope(method, data, self.pid, self.uid)
        print(f"\n[{ts()}] → {method!r}  ({desc})")
        print(f"         payload: {payload}")

    def publish_to(self, topic, method, data, desc):
        """Publish to an explicit topic (used in phase-3 topic discovery)."""
        self._current = (method, desc)
        payload = envelope(method, data, self.pid, self.uid)
        print(f"\n[{ts()}] → topic={topic!r}  {method!r}  ({desc})")
        self._client.publish(topic, payload, qos=0)
        self._client.publish(self.topic, payload, qos=0)


# ── Main ─────────────────────────────────────────────────────────────────────

async def run(args):
    topic = args.topic or f"SF/GGS/CB/API/UP/{args.pid}"

    if args.tls and args.port == 1883:
        args.port = 8883

    probe = Probe(
        broker   = args.broker,
        port     = args.port,
        pid      = args.pid,
        uid      = args.uid,
        topic    = topic,
        username = args.username,
        password = args.password,
        tls      = args.tls,
        cafile   = args.cafile,
    )
    probe.start()

    print(f"[{ts()}] Passive listen for {args.listen_secs}s …")
    await asyncio.sleep(args.listen_secs)

    if args.listen:
        print(f"\n[{ts()}] Listen-only mode active. Ctrl-C to stop.")
        try:
            while True:
                await asyncio.sleep(1)
        except KeyboardInterrupt:
            print()

    elif args.phase3:
        # ── Phase 3: topic discovery ──────────────────────────────────────
        # Subscribe to all topics so we see anything the device publishes
        # in response, regardless of topic.
        probe.subscribe_wildcard()
        await asyncio.sleep(1)

        candidates = [t.format(pid=args.pid) for t in CANDIDATE_TOPICS]
        cmd = dict(_PHASE3_CMD)
        cmd["pid"] = args.pid
        cmd["uid"] = args.uid

        print(f"\n[{ts()}] Phase-3: probing {len(candidates)} candidate command topics …")
        print(f"         Command: setOnOff light off (easy to spot in getDevSta)")
        print(f"         Watch for light state change in getDevSta stream.\n")

        state_before = None
        for r in reversed(probe.responses):
            if r["method"] == "getDevSta":
                state_before = r["data"]
                break

        for topic in candidates:
            print(f"\n[{ts()}] Trying command topic: {topic}")
            probe.publish_to(topic, "setOnOff",
                             {"devType": "light", "on": 0},
                             f"light off → {topic}")
            await asyncio.sleep(args.timeout)

            # After each attempt, check if light state changed
            for r in reversed(probe.responses):
                if r["method"] == "getDevSta" and r["topic"] == probe.topic:
                    try:
                        d = json.loads(r["data"])
                        light = d.get("data", {}).get("light", {})
                        if light.get("on", 1) == 0 or light.get("level", 1) == 0:
                            print(f"\n*** STATE CHANGED after publishing to {topic!r} ***")
                            print(f"    light is now OFF — this may be the command topic!")
                            # Restore light
                            probe.publish_to(topic, "setOnOff",
                                             {"devType": "light", "on": 1},
                                             "light on — restore")
                            await asyncio.sleep(2)
                    except Exception:
                        pass
                    break

        print(f"\n\n{'='*64}")
        print("PHASE-3 SUMMARY")
        print("If no state changes occurred above, the device either:")
        print("  1. Uses a topic not in the candidate list")
        print("  2. Requires the EMQX admin API to find its subscription")
        print("\nTo query EMQX admin API:")
        print(f"  curl http://{args.broker}:18083/api/v5/clients")
        print(f"  curl http://{args.broker}:18083/api/v5/subscriptions")
        topics_seen = {r["topic"] for r in probe.responses}
        print(f"\nAll topics seen during this session: {sorted(topics_seen)}")

    else:
        probes = build_probes_phase2() if args.phase2 else build_probes()
        phase = "phase-2 (targeted)" if args.phase2 else "phase-1 (discovery)"
        print(f"\n[{ts()}] Starting {len(probes)} {phase} probes (timeout={args.timeout}s each) …")
        for method, desc, data in probes:
            probe.publish(method, data, desc)
            await asyncio.sleep(args.timeout)

        # ── Summary ──────────────────────────────────────────────────────
        print(f"\n\n{'='*64}")
        print("SUMMARY — non-status responses received:")
        relevant = [r for r in probe.responses
                    if r["method"] not in QUIET_METHODS and r["probe"]]
        if relevant:
            seen = {}
            for r in relevant:
                key = r["probe"][0]
                seen.setdefault(key, []).append(
                    f"  desc={r['probe'][1]!r}  response={r['method']!r}"
                )
            for method, lines in seen.items():
                print(f"\n  probe method: {method!r}")
                for l in lines:
                    print(l)
        else:
            print("  (none — device sent no replies to probes)")

        passive = [r for r in probe.responses
                   if r["method"] not in QUIET_METHODS and not r["probe"]]
        if passive:
            print(f"\n  Passive (unprompted) non-status messages: {len(passive)}")
            for r in passive[:5]:
                print(f"    [{r['ts']}] method={r['method']!r}")

    probe.stop()


def main():
    repo_root = Path(__file__).parent.parent
    default_ca = str(repo_root / "doc" / "certs" / "ca-sf.pem")

    p = argparse.ArgumentParser(
        description="Spider Farmer GGS-CB MQTT method prober",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    p.add_argument("--broker",      default="localhost",
                   help="MQTT broker host (default: localhost)")
    p.add_argument("--port",        type=int, default=1883,
                   help="MQTT broker port (default: 1883)")
    p.add_argument("--pid",         required=True,
                   help="Device PID — MAC without colons, e.g. 80F1B2B3B648")
    p.add_argument("--uid",         default="000000",
                   help="User ID from Spider Farmer account (default: 000000)")
    p.add_argument("--topic",       default=None,
                   help="Override topic (default: SF/GGS/CB/API/UP/<pid>)")
    p.add_argument("--username",    default=None, help="Broker username")
    p.add_argument("--password",    default=None, help="Broker password")
    p.add_argument("--listen",      action="store_true",
                   help="Passive listen only — no probes sent")
    p.add_argument("--phase2",      action="store_true",
                   help="Run phase-2 targeted probes (setOnOff semantics, level control)")
    p.add_argument("--phase3",      action="store_true",
                   help="Run phase-3 topic-discovery probes (find real command topic)")
    p.add_argument("--listen-secs", type=int, default=10, dest="listen_secs",
                   help="Seconds to passively listen before probing (default: 10)")
    p.add_argument("--timeout",     type=float, default=3,
                   help="Seconds to wait between probes (default: 3)")
    p.add_argument("--tls",         action="store_true",
                   help="Connect with TLS (auto-switches port to 8883)")
    p.add_argument("--cafile",      default=default_ca,
                   help=f"CA cert for TLS (default: {default_ca})")
    args = p.parse_args()
    asyncio.run(run(args))


if __name__ == "__main__":
    main()
