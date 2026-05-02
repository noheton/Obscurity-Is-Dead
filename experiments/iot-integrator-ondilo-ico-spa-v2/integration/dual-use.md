# Dual-use mirror (rule 5) — narrow form

Per `CLAUDE.md` rule 5, every interoperability win in this case study is
mirrored to its attacker-side capability. The full reflection is in
`../process/phase-3-implementation.md` §3.5; this file is the one-screen
condensation.

## Win

Read-only ingestion of seven water-chemistry sensors into Home Assistant
without writing or modifying a line of code, by configuring the existing
HA core integration `ondilo_ico` against the documented Ondilo Customer
API.

## Mirror

The attack surface unlocked by this case study is **narrow** because the
vendor cloud is conventionally authenticated (TLS + OAuth2), not
obscurity-protected:

- **W-1 — public OAuth client.** Enables third-party clients (HA, this
  case study) to integrate at all. Mirror: a phisher can render an OAuth
  prompt visually identical to the real Ondilo prompt. Mitigation is
  generic browser hygiene; not improved or worsened by this case study.
- **W-2 — non-expiring refresh token.** Enables HA to keep working without
  user re-authentication. Mirror: a one-time backup leak yields perpetual
  read access until manual revocation. Mitigation: §3.4.2 rotation.
- **W-4 — coarse `api` scope.** The bearer can also call
  `validate_pool_recommendation`. Mirror: token theft has slightly more
  authority than a true read-only credential. Mitigation: §3.4.5 backup
  hygiene.

## Compared to the prior case studies

- **Spider Farmer** (`experiments/spider-farmer/REPORT.md` §7) — local BLE
  with hardcoded keys. Win and mirror are both **large**; obscurity
  dominated. This case is the opposite: small mirror, openness-protected.
- **EcoFlow PowerOcean** (`experiments/ecoflow-powerocean/REPORT.md` §8) —
  bearer with `setDeviceProperty` write authority. Mirror was
  write-anywhere. Ondilo's bearer mirror is one specific write, much
  narrower.

## Researcher-acceptable residual

The remaining residual the researcher accepts under "as private as
reasonable" is **behavioural inference from water-chemistry time-series**
(presence / occupancy proxy, Phase 0 §0.2 heuristic). The pool-nickname
alias mitigates *identification*, not inference. Inference cannot be
removed without removing the integration.
