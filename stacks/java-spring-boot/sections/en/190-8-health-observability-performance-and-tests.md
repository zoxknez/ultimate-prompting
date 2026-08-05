## 8. Health, Observability, Performance, And Tests

Separate liveness, readiness, and degraded-dependency state. Do not put shared external dependencies in liveness probes, because restart loops can cause cascading failure. Decide deliberately whether an external dependency belongs in readiness. For Kubernetes, inspect Actuator probe groups and ensure probes exercise an appropriate main-server path when a separate management port could mask an application failure.

Require structured logs, correlation/trace IDs, route template, user/tenant IDs without unnecessary PII, status, latency, dependency latency, retries, job ID, deployment version, metrics, traces, error rate, latency percentiles, JVM heap/GC, thread-pool/executor saturation, blocked threads, connection-pool/cache/queue metrics, and dependency telemetry. Instrument with Micrometer/OpenTelemetry where appropriate. Alerts need owner, threshold, duration, severity, runbook, dashboard, and user/business impact.

Measure blocking calls, thread starvation, executor sizing/queueing, CPU-heavy work, large JSON/regex/compression/crypto/files, reactive scheduler misuse, memory/GC, connection-pool saturation, database latency, cache behavior, and load behavior. Isolate genuine CPU-bound work into bounded workers or services rather than starving request threads or event loops.

Run/add unit tests for pure logic; integration tests for controllers, filters, database and Spring context; contract tests for HTTP/gRPC; concurrency tests for invariants; security tests for authentication/authorization, SSRF, CORS/CSRF, Actuator exposure, upload and webhook replay; end-to-end tests for critical flows; and load tests for costly endpoints. Each discovered regression needs a focused test that would have failed before its repair.

