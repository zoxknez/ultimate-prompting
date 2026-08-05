## Work Modes

Default mode: `AUDIT_AND_SAFE_FIX`.

| Mode | Allowed behavior |
| --- | --- |
| `AUDIT_ONLY` | Read, inspect and test without changing source, lockfiles, data, queues, credentials or infrastructure. |
| `AUDIT_AND_SAFE_FIX` | Apply low-risk confirmed fixes with tests; plan breaking, data, dependency and deployment changes. |
| `FULL_IMPLEMENTATION` | Implement in small verified steps; obtain explicit approval before production migration, deploy, queue replay or secret rotation. |
| `FIX_CONFIRMED_ISSUES` | Change only findings supported by reproducible evidence. |
| `SECURITY_AUDIT` | Prioritize auth, tenancy, sessions, injection, files, serialization, secrets, supply chain and administrative surfaces. |
| `PERFORMANCE_AUDIT` | Measure web, jobs, SQL, GC, memory, pools, queues, cache, realtime and deployment behavior in production-like mode. |
| `MIGRATION_AUDIT` | Audit Ruby, Rails, Rack, Puma, Bundler, database, job backend, frontend defaults and mixed-version compatibility. |
| `INCIDENT_AND_RECOVERY` | Contain first, preserve evidence, revoke trust, restore from known-good state, reconcile and harden. |

