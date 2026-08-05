## Phase N - Resilience, Performance, Observability

Timeout/retry/jitter/cancellation consistent across inbound, DB, HTTP, and jobs. Do not retry non-idempotent writes. Bound concurrency to dependency capacity.

Performance: measurement (p95/p99, CPU, memory, alloc, GC for Go, scheduler, lock contention, I/O, queries). Benchmark and profiler evidence. Do not optimize without a profiler. A microbenchmark is not end-to-end proof.

Observability: structured logs, correlation/trace ID, metrics cardinality, tracing, separated health/readiness/liveness, dashboard, alert, runbook. Do not log secrets/PII.

