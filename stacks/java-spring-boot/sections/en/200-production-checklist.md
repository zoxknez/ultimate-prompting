## Production Checklist

Before a final verdict, explicitly complete this checklist with evidence rather than assumptions:

1. Supported Java, Spring Boot, Spring Framework, build tool, and production-image baseline.
2. Reproducible wrapper build, locked/verified dependencies, and known dependency source.
3. Safe profile/config startup with no production side effects during tests.
4. Clear separation of public, internal, and management endpoints.
5. Proven authentication, authorization, ownership, and tenant scope for critical operations.
6. DTO, boundary, semantic, and file/message validation for untrusted input.
7. Database constraints, transaction, locking, and concurrency model for each critical invariant.
8. Idempotency and crash/replay recovery for write, webhook, job, and message flows.
9. Safe, rollout-compatible, measured, recoverable migrations.
10. Bounded timeouts, retries, pools, queues, and resource limits for local and external flows.
11. Bounded upload/download/SSRF behavior and verified outbound access.
12. Protected Actuator, secrets, TLS/cookies/CSRF/CORS, and supply-chain controls.
13. Liveness, readiness, degraded dependencies, structured logs, metrics, tracing, alerts, and runbooks.
14. Measured or explicitly limited capacity/performance risk.
15. Container/Kubernetes/native deployment verification where applicable.
16. Proven graceful shutdown, deployment, application rollback, and data recovery.

