## Mandatory Evidence Matrices

Produce every matrix below. Mark unknown cells `UNVERIFIED`; do not omit rows because evidence is unavailable.

| ID | Matrix | Minimum required columns |
| --- | --- | --- |
| M1 | Source, runtime, and artifact identity | component; source commit; build PHP; runtime PHP; SAPI; extensions; artifact digest; deployment revision; evidence |
| M2 | Supported execution modes | mode; binary; INI; extensions; config; lifecycle; owner; test; support status |
| M3 | Composer and supply chain | package or tool; source; version; trust; script or plugin; vulnerability; waiver; expiry; evidence |
| M4 | Routes, commands, messages, and authority | surface; input; authentication; authorization; tenant; transaction; idempotency; rate limit; test |
| M5 | Authentication and account lifecycle | flow; credential; expiry; rotation; revocation; MFA; recovery; abuse control; evidence |
| M6 | Data, ORM, schema, and invariants | entity or table; authority; tenant key; invariant; constraint; concurrency; retention; recovery |
| M7 | Transactions and external effects | flow; database boundary; isolation; idempotency; external effect; crash points; reconciliation; owner |
| M8 | Queues, workers, and schedulers | job or message; transport; delivery; retry; DLQ; ordering; deduplication; concurrency; shutdown; recovery |
| M9 | Caches, sessions, locks, files, and search | store; authority; key or namespace; isolation; consistency; expiry; invalidation; restore; test |
| M10 | Dependencies, limits, and degraded modes | dependency; owner; credential; timeout; retry; rate limit; capacity; failure mode; fallback; SLO |
| M11 | Release, migration, rollback, and restore | change; compatibility window; order; canary; abort; rollback; forward repair; RPO; RTO; evidence |
| M12 | Findings, fixes, and residual risk | finding; severity; evidence; root cause; fix; test; rollout; owner; deadline; residual risk; status |

