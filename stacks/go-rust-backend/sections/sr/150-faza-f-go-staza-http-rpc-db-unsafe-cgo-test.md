## Faza F - GO STAZA: HTTP/RPC, DB, Unsafe/CGO, Test

### Networking

Proveri: server timeouts (Read/Write/Idle/Header), body limite, context cancel na disconnect, middleware redosled, TLS, HTTP/2, gRPC interceptors/deadlines/message size, client timeout i connection pool, redirect policy, SSRF na user-supplied URL.

### database/sql i persistence

Proveri: driver, pool (`SetMaxOpenConns`/`MaxIdleConns`/`ConnMaxLifetime`), context na query, prepared statements, transakcije (begin/commit/rollback/defer), isolation, locking, N+1, pagination, migracije, null handling, money/time tipove. Ne tretiraj InMemory/sqlite-in-memory kao dokaz production relational ispravnosti ako se u produkciji koristi drugi engine.

### unsafe i cgo

Inventarisi `unsafe`, cgo, pointer casting, Go pointer u C, finalizer, memory ownership preko FFI. Dokumentuj invarijante. CGO menja deploy (glibc/musl, cross-compile, image).

### Testiranje

```text
go test ./...
go test -race ./...
go test -fuzz=Fuzz -fuzztime=30s ./...
govulncheck ./...
```

Proveri table-driven testove, integration sa stvarnim dependency-jem gde je moguce, fuzz targete, benchmarke sa realnim podacima, build tagove za integration. Fuzz i race su deo production toolchain-a, ne opcionalni luksuz kada postoji konkurentni ili parser kod.

