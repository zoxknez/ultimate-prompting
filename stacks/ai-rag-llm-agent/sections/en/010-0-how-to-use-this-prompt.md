## 0. How To Use This Prompt

### 0.1 Required Inputs

Collect or infer, and explicitly record:

| Field | Value |
| --- | --- |
| System or repository | `[NAME / PATH / URL]` |
| Business purpose | `[PURPOSE]` |
| Users | `[INTERNAL / PUBLIC / ENTERPRISE / REGULATED]` |
| Deployment environments | `[LOCAL / DEV / STAGING / PROD]` |
| AI providers and models | `[LIST OR UNKNOWN]` |
| Runtime and orchestration | `[DIRECT API / SDK / CUSTOM LOOP / WORKFLOW ENGINE]` |
| Knowledge sources | `[FILES / DB / WEB / DRIVE / GIT / OTHER]` |
| Vector, search, and memory stores | `[LIST OR UNKNOWN]` |
| Tools, plugins, MCP servers, subagents | `[LIST OR UNKNOWN]` |
| High-impact actions | `[EMAIL / PAYMENT / DEPLOY / DELETE / SHELL / ACCOUNT / OTHER]` |
| Sensitive data | `[PII / FINANCIAL / HEALTH / LEGAL / BUSINESS / SECRETS / NONE]` |
| Tenancy model | `[SINGLE-TENANT / MULTI-TENANT / UNKNOWN]` |
| Compliance scope | `[EU AI ACT / GDPR / HIPAA / PCI / SOC 2 / ISO / OTHER / NONE / UNKNOWN]` |
| Work mode | `[AUDIT_ONLY / AUDIT_AND_SAFE_FIX / FULL_IMPLEMENTATION / FIX_CONFIRMED_ISSUES / SECURITY_AND_EVAL_AUDIT]` |

### 0.2 Missing Information Policy

Do not block the whole audit because some inputs are missing.

1. Infer only from repository, configuration, runtime evidence, and authoritative documentation.
2. Mark every unresolved assumption as `UNVERIFIED`.
3. Continue with safe read-only checks where possible.
4. Ask only for access that materially blocks confirmation, repair, or verification.
5. Never convert missing evidence into a positive conclusion.

### 0.3 Work Modes

| Mode | Allowed behavior |
| --- | --- |
| `AUDIT_ONLY` | Inspect, model, test safely, and report. Do not mutate source, lockfiles, data, schemas, infrastructure, prompts, or provider configuration. |
| `AUDIT_AND_SAFE_FIX` | Apply confirmed, low-risk, reversible fixes with focused regression tests. Plan larger or risky changes. |
| `FULL_IMPLEMENTATION` | Implement justified changes incrementally. Back up before destructive work. Verify rollback and recovery. |
| `FIX_CONFIRMED_ISSUES` | Change only findings already registered and confirmed. Do not widen scope silently. |
| `SECURITY_AND_EVAL_AUDIT` | Prioritize trust boundaries, adversarial testing, eval quality, permissions, and incident readiness. |

If unspecified, use `AUDIT_AND_SAFE_FIX`.

