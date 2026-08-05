## Production Checklist

Fill: YES / NO / PARTIAL / UNVERIFIED / NOT_APPLICABLE

1. Supported Go and/or Rust toolchain; no unapproved preview/nightly baseline.
2. Go toolchain/directives aligned; Rust toolchain/MSRV/edition aligned.
3. Reproducible build; lock/checksum; dependency audit; pinned build tools.
4. Production build and target build actually executed.
5. Unit/integration/race/fuzz/Miri-sanitizer/security/migration/recovery where applicable.
6. Goroutine/task lifecycle, cancellation, timeout, bounded concurrency, backpressure.
7. No confirmed critical data races/leaks; shutdown verified.
8. Unsafe/FFI inventory, safety invariants, ABI, Send/Sync, native lifecycle.
9. Validation, HTTP/RPC, authz, tenant, rate limit, idempotency, TLS, secrets, debug endpoints.
10. DB constraints/pool/transactions/locking/migrations/backup/restore.
11. Timeout/retry/jitter; no retry storms; messaging recovery.
12. Performance measured or explicitly bounded.
13. Observability: log/trace/metrics/health/alert/runbook.
14. Immutable artifact, non-root, SBOM where applicable, graceful shutdown.
15. Rollout, abort, rollback, recovery, post-deploy verification.

