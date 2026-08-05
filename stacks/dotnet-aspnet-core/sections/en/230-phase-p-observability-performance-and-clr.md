## Phase P - Observability, Performance, And CLR

Separate liveness, readiness, and degraded dependency. Liveness = whether the process needs restart; transient dependency outages usually belong in readiness/degraded. Health must not disclose secrets or internal topology; Host-header restriction is not a security boundary.

Require: structured logs, correlation/trace ID, route template, user/tenant without unnecessary PII, status, latency, dependency latency, retries, job ID, deployment version, metrics, traces, error rate, latency percentiles, allocation/GC, thread-pool starvation, connection pool/cache/queue metrics. Instrument with OpenTelemetry where compatible. Alerts: owner, threshold, duration, severity, runbook, dashboard, business impact.

Base performance claims on measurement. Measure blocking, sync-over-async, thread-pool starvation, CPU-heavy work, large JSON/regex/compression/crypto/files, streaming backpressure, LOH/GC, DB latency, connection pool. Isolate true CPU-bound work into bounded workers. A microbenchmark is not proof of end-to-end improvement. Do not declare a performance problem or improvement without measurement.

