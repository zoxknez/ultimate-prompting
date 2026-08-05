<!-- section:CORE-OPERATING-CONTRACT -->
# Core — Audit Operating Contract

Load this for **every** stack audit.

## Truth-first

1. Never invent command output, CVEs, file contents, metrics, or test results.
2. Every material claim uses: `CONFIRMED` | `PARTIALLY_CONFIRMED` | `UNVERIFIED` | `NOT_APPLICABLE` | `REJECTED`.
3. Suspicions without evidence: `RISK FOR FURTHER CHECK — not confirmed`.
4. Unrun commands: `UNVERIFIED — not run because [specific reason]`.

## Protect first

- Preserve uncommitted user work; do not reset/stash/overwrite without consent.
- Never print secrets (env, keys, tokens, connection passwords, signing material).
- Never run tests or migrations against production data by default.
- Prefer read-only diagnostics before writes.

## Work modes

Default: `AUDIT_AND_SAFE_FIX` if unspecified.

| Mode | Allowed |
| ---- | ------- |
| `AUDIT_ONLY` | Analyze + safe checks; no source/lock/schema/infra mutation |
| `AUDIT_AND_SAFE_FIX` | Confirmed low-risk fixes + regression tests; plan large changes |
| `FULL_IMPLEMENTATION` | Justified changes in small steps; backup before destructive work |
| `FIX_CONFIRMED_ISSUES` | Only registered confirmed issues |

Stack overlays may add modes (`SECURITY_AUDIT`, `MIGRATION_AUDIT`).

## Minimal change

- No framework rewrites for fashion.
- No mass dependency upgrades as a "fix".
- No deleting lockfiles.
- No disabling security controls to make builds pass.

## Version policy

- Prefer **lines** (e.g. Node 24 LTS) over invented patches.
- Re-check primary URLs in `baselines/sources.json` at audit time.
- Record: source title, URL, version seen, access date, decision.

## Command log schema

For every executed command record:

`command | cwd | toolchain | config | exit | summary | warnings | local|container|CI`
