## Phase F - GO PATH: HTTP/RPC, DB, Unsafe/CGO, Tests

### Networking

Check: server timeouts (Read/Write/Idle/Header), body limits, context cancel on disconnect, middleware order, TLS, HTTP/2, gRPC interceptors/deadlines/message size, client timeout and connection pool, redirect policy, SSRF on user-supplied URLs.

### database/sql and persistence

Check: driver, pool (`SetMaxOpenConns`/`MaxIdleConns`/`ConnMaxLifetime`), context on queries, prepared statements, transactions (begin/commit/rollback/defer), isolation, locking, N+1, pagination, migrations, null handling, money/time types. Do not treat in-memory/sqlite-in-memory as proof of production relational correctness if production uses another engine.

### unsafe and cgo

Inventory `unsafe`, cgo, pointer casting, Go pointers into C, finalizers, memory ownership across FFI. Document invariants. CGO changes deployment (glibc/musl, cross-compile, image).

### Testing

```text
go test ./...
go test -race ./...
go test -fuzz=Fuzz -fuzztime=30s ./...
govulncheck ./...
```

Check table-driven tests, integration with real dependencies where possible, fuzz targets, benchmarks with realistic data, build tags for integration. Fuzz and race are part of the production toolchain, not optional luxury when concurrent or parser code exists.

