## Produkcioni Checklist

Popuni: DA / NE / DELIMICNO / NEPROVERENO / NIJE_PRIMENJIVO

1. Podrzan Go i/ili Rust toolchain; nema neodobrenog preview/nightly baseline-a.
2. Go toolchain/direktive uskladjeni; Rust toolchain/MSRV/edition uskladjeni.
3. Reproduktivan build; lock/checksum; dependency audit; pinovani build alati.
4. Production build i target build stvarno izvrseni.
5. Unit/integration/race/fuzz/Miri-sanitizer/security/migration/recovery gde primenljivo.
6. Goroutine/task lifecycle, cancellation, timeout, bounded concurrency, backpressure.
7. Nema potvrdjenih kriticnih data race-ova/leak-ova; shutdown proveren.
8. Unsafe/FFI inventar, safety invariants, ABI, Send/Sync, native lifecycle.
9. Validacija, HTTP/RPC, authz, tenant, rate limit, idempotency, TLS, tajne, debug endpointi.
10. DB constraints/pool/transakcije/locking/migracije/backup/restore.
11. Timeout/retry/jitter; nema retry storma; messaging recovery.
12. Performance merena ili eksplicitno ogranicena.
13. Observability: log/trace/metrics/health/alert/runbook.
14. Immutable artefakt, non-root, SBOM gde primenljivo, graceful shutdown.
15. Rollout, abort, rollback, recovery, post-deploy verification.

