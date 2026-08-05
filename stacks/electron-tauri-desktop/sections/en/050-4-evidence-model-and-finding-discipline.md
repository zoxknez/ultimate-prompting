## 4. Evidence Model And Finding Discipline

### 4.1 Evidence Levels

| Level | Meaning | Examples | Allowed conclusion |
| --- | --- | --- | --- |
| E0 | Claim or documentation only | README, issue, diagram, roadmap, user statement | Context only; never sufficient for a production verdict. |
| E1 | Static source evidence | Code, configuration, manifests, capability files, entitlements | Shows intent and potential behavior, not resolved or installed behavior. |
| E2 | Resolved build evidence | Lock files, dependency graph, compiler output, generated configuration | Shows what was resolved and built in a specific environment. |
| E3 | Packaged artifact evidence | Archive contents, binary metadata, fuses, permissions, signatures, SBOM | Shows the actual release candidate before installation. |
| E4 | Installed/runtime evidence | Installed files, process tree, runtime logs, IPC behavior, OS integration, performance | Shows behavior on a specific platform, architecture, profile, and version path. |
| E5 | Operational/recovery evidence | Real update rollout, rollback, restore, key rotation, telemetry, incident drill | Required for strong claims about operations, recovery, and production readiness. |

### 4.2 Mandatory Finding Register

```text
ID:
Title:
Severity: P0 / P1 / P2 / P3
Evidence status: CONFIRMED / PARTIALLY_CONFIRMED / UNVERIFIED
Framework: ELECTRON / TAURI / SHARED / OTHER
Area:
Affected platform and architecture:
Affected version and release channel:
Affected files and symbols:
Affected window, webview, process, command, IPC channel, capability, plugin, installer, or update path:
Environment:
Evidence level: E0 / E1 / E2 / E3 / E4 / E5
Evidence:
Command, test, package inspection, or runtime capture:
Reproduction:
Root cause:
Exploit or failure preconditions:
User and business impact:
Security, privacy, data, and operational impact:
Likelihood:
Proposed fix:
Implemented fix:
Regression test:
Release and migration impact:
Rollback or recovery:
Residual risk:
Owner:
Status:
```

### 4.3 Severity Guidance

1. `P0`: active compromise, arbitrary local code execution through untrusted content, compromised signing/update path, destructive cross-user data loss, credential exfiltration, or an unrecoverable production release condition.
2. `P1`: reachable privilege escalation, authorization bypass, unsafe updater or installer behavior, severe data corruption, widespread crash/startup failure, unsupported security-critical runtime, or no viable rollback for a critical release.
3. `P2`: meaningful reliability, privacy, performance, accessibility, maintainability, or defense-in-depth weakness with bounded impact or additional preconditions.
4. `P3`: low-risk hardening, developer-experience improvement, documentation gap, cleanup, or optional modernization.
5. Severity is based on demonstrated impact, reachability, likelihood, blast radius, detectability, and recovery difficulty. Do not inflate severity from keywords alone.

