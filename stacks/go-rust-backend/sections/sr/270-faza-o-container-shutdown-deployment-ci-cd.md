## Faza O - Container, Shutdown, Deployment, CI/CD

Artefakt: reproducible build, pinovan base image/digest, non-root, minimal OS, CA/certs, timezone, signal handling, no secrets in layers, SBOM, scan.

Graceful shutdown: prestani da primas posao, drain, otkazi taskove/goroutine sa context, flush log/telemetry, zatvori pool/conn, zavrsi u roku platforme. Testiraj tokom dugih requesta, jobova i migracija.

Deployment: immutable artefakt, migration redosled, rolling/canary, abort kriterijum, rollback aplikacije vs baze (eksplicitno), recovery, post-deploy verification.

CI/CD: pinovan toolchain (Go/Rust), matrix (OS/arch/features/MSRV), race/fuzz/audit gde relevantno, locked build, ne `go install @latest` / floating nightly, artifact promotion, secret hygiene.

