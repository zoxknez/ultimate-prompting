## Phase J - RUST PATH: Web, DB, Supply Chain

### Web/RPC/serialization

Check framework (axum/actix/warp/tonic/...), extractor validation, body limits, timeout, auth middleware, CORS, error responses without leaking internals, serde deny-unknown where needed, schema evolution, gRPC message limits.

### Database

Check driver/pool (sqlx/diesel/sea-orm/...), compile-time SQL where used, migrations, transactions, isolation, connection checkout timeout, cancel, N+1, type mapping (time/money/uuid).

### Cargo supply chain

Check: registry sources, git/path dependencies, `[patch]`, yanked crates, typosquat risk, features that pull heavy native code, `cargo audit`/`cargo deny` where present, SBOM, pinned tool versions in CI. Do not use floating `cargo install ...` latest in reproducible CI.

