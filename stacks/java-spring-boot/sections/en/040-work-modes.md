## Work Modes

Use `AUDIT_AND_SAFE_FIX` unless a mode is explicitly supplied.

| Mode | Allowed work |
| --- | --- |
| `AUDIT_ONLY` | Analyze and test without changing source, configuration, dependencies, or infrastructure; provide concrete changes and a roadmap. |
| `AUDIT_AND_SAFE_FIX` | Implement only confirmed local, safe, low-risk repairs. Plan destructive migrations, major architecture changes, and public-contract changes. |
| `FULL_IMPLEMENTATION` | Implement confirmed repairs and justified improvements, but never perform destructive work without a backup/rollback strategy; split large changes into verifiable steps. |
| `FIX_CONFIRMED_ISSUES` | Do not widen scope; repair only previously confirmed issues, add tests, and run the relevant regression scope. |

