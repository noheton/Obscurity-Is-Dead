# Infrastructure

All values extracted from `libapp.so` string literals.

---

## Cloud Endpoints

| Purpose | URL |
|---------|-----|
| REST API base | `https://api.spider-farmer.com/` |
| File / static assets | `https://file.spider-farmer.com/` |
| Privacy policy | `https://file.spider-farmer.com/protocol/privacy.html` |
| User agreement | `https://file.spider-farmer.com/protocol/agreement.html` |
| Firebase project | `spider-farmer.appspot.com` |

---

## MQTT Broker

| Parameter | Value |
|-----------|-------|
| Hostname | `sf.mqtt.spider-farmer.com` |
| Port | **8333** (MQTTS — TLS) |
| Username | `[REDACTED:username:S-SF-5-username]` |
| Password | `[REDACTED:credential:S-SF-5-password]` |
| Protocol | MQTT 3.1.1 over TLS |

The controller uses certificate-based TLS. The client certificates are bundled inside the
APK under `assets/files/`:

| File | Description |
|------|-------------|
| `ca-sf.pem` | Root CA certificate (self-signed, CN=MZ, C=CN) |
| `emqx-sf.pem` | Server / broker certificate |
| `emqx-sf.key` | Private key for the broker certificate |
| `ca-temp-sf.pem` | Alternate root CA (likely staging) |
| `emqx-temp-sf.pem` | Alternate broker certificate |
| `emqx-temp-sf.key` | Alternate broker private key |

The CA cert was issued 2025-01-09 and expires 2123-12-17.

### Local intercept setup

DNS-rewrite `sf.mqtt.spider-farmer.com` → your broker IP.  
Configure Mosquitto/EMQX with the extracted CA + server cert on port 8333.

---

## Firebase

The app integrates Firebase for push notifications, crash reporting (Crashlytics),
and Google authentication. The Firebase project is `spider-farmer` (appspot.com).
These services are cloud-only and not relevant to local control.

---

## Device type codes (MQTT topic path component)

These strings appear verbatim in the MQTT topic template
`SF/<TYPE>/API/UP/<PID>`:

| Code | Description |
|------|-------------|
| `GGS/CB` | Main grow controller (SF-GGS-CB) — **primary target** |
| `GGS/ICB` | Industrial controller board |
| `GGS/LC` | Light controller |
| `GGS/PS1` | Single-outlet smart plug |
| `GGS/PS5` | 5-outlet power strip |
| `GGS/PS10` | 10-outlet power strip |

Full topic examples:

```
SF/GGS/CB/API/UP/<PID>          # device publishes state here
SF/Offline/<PID>                 # broker publishes when device disconnects (LWT)
```
