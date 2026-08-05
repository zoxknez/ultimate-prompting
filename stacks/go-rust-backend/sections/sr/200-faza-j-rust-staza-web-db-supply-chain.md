## Faza J - RUST STAZA: Web, DB, Supply Chain

### Web/RPC/serialization

Proveri framework (axum/actix/warp/tonic/...), extractor validaciju, body limite, timeout, auth middleware, CORS, error response bez curenja internih detalja, serde deny unknown gde treba, schema evolution, gRPC message limits.

### Database

Proveri driver/pool (sqlx/diesel/sea-orm/...), compile-time SQL gde se koristi, migracije, transakcije, isolation, connection checkout timeout, cancel, N+1, type mapping (time/money/uuid).

### Cargo supply chain

Proveri: registry izvore, git/path dependency, `[patch]`, yanked, malicious typosquat rizik, feature koji vuce heavy native, `cargo audit`/`cargo deny` gde postoji, SBOM, pinovane tool verzije u CI. Ne koristi `cargo install ...` floating latest u reproduktivnom CI-ju.

