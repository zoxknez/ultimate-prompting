## Work Modes

Use `AUDIT_AND_SAFE_FIX` unless a mode is explicitly supplied.

| Mode | Allowed work |
| --- | --- |
| `AUDIT_ONLY` | Analyze and run safe checks without changing source, package versions, schema, or infrastructure; deliver precise changes and a roadmap. |
| `AUDIT_AND_SAFE_FIX` | Implement only confirmed local, low-risk repairs and regression tests; plan large migrations and public breaking changes. |
| `FULL_IMPLEMENTATION` | Implement justified changes in small verifiable steps; for destructive work require backup, rollout, and recovery strategy. |
| `FIX_CONFIRMED_ISSUES` | Do not widen scope; fix only registered, confirmed issues and run the relevant regression scope. |
| `INCIDENT_MODE` | Preserve evidence, contain safely, restore service, identify cause, eradicate it, rotate affected trust material, and document recovery. |
| `MIGRATION_AUDIT` | For .NET Framework → modern .NET, .NET 6–9 → .NET 10+, System.Web/MVC → ASP.NET Core, EF6 → EF Core, Newtonsoft.Json → System.Text.Json, or legacy hosting/auth moves: produce a compatibility matrix, migration waves, strangler/dual-run, rollback, and recovery plan. |

