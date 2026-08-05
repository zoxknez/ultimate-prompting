## Work Modes

Use `AUDIT_AND_SAFE_FIX` unless a mode is explicitly supplied.

| Mode | Allowed work |
| --- | --- |
| `AUDIT_ONLY` | Analyze and run safe checks; do not change source, dependencies, lock files, database, or infrastructure; deliver a precise plan. |
| `AUDIT_AND_SAFE_FIX` | Implement confirmed local low-risk repairs and regression tests; plan destructive, contract-breaking, or architecturally large changes. |
| `FULL_IMPLEMENTATION` | Implement justified repairs in small verifiable steps; do not run destructive migrations without backup/rollback strategy. |
| `FIX_CONFIRMED_ISSUES` | Fix only previously confirmed issues; do not widen scope without evidence. |
| `SECURITY_AND_CONCURRENCY_AUDIT` | Focus: race, deadlock, goroutine/task leak, cancellation, unsafe/FFI, input/network security, dependency risk, secrets, idempotency, resource exhaustion. |
| `PERFORMANCE_AUDIT` | Focus: real workload, CPU, memory, allocations, GC, scheduler, contention, I/O, queries, latency percentiles, benchmark and profiler evidence. |

