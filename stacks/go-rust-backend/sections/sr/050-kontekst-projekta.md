## Kontekst Projekta

| Polje | Vrednost |
| --- | --- |
| Servis | `[NAME]` |
| Namena | `[DESCRIPTION]` |
| Klijenti | `[WEB / MOBILE / CLI / PARTNERS / INTERNAL / PUBLIC]` |
| Arhitektura | `[MONOLITH / MODULAR MONOLITH / MICROSERVICE / WORKER / SYSTEMS / OTHER]` |
| Tehnologija | `[GO / RUST / MIXED_GO_RUST]` |
| Go module/workspace | `[GO_MODULE]` |
| Rust workspace/crate | `[RUST_WORKSPACE]` |
| Target platforme | `[LINUX / WINDOWS / MACOS / EMBEDDED / WASM / OTHER]` |
| Deployment | `[DOCKER / KUBERNETES / VM / BARE METAL / SERVERLESS / OTHER]` |
| Podaci | `[POSTGRESQL / MYSQL / SQLITE / REDIS / OTHER]` |
| Messaging/cache | `[MESSAGING / CACHE]` |
| Protokoli | `[HTTP / gRPC / QUIC / TCP / UDP / OTHER]` |
| FFI/native | `[FFI / CGO / BINDGEN / NONE]` |
| Workload | `[WORKLOAD]` |
| CI/CD | `[CI_CD]` |
| Baseline/kompatibilnost | `[ZAHTEVANI_BASELINE / KOMPATIBILNOST]` |
| Rezim rada | `[AUDIT_ONLY / AUDIT_AND_SAFE_FIX / FULL_IMPLEMENTATION / FIX_CONFIRMED_ISSUES / SECURITY_AND_CONCURRENCY_AUDIT / PERFORMANCE_AUDIT]` |
| Regulatorni i dodatni zahtevi | `[REGULATORNI_ZAHTEVI / OGRANICENJA]` |
| Repo / ocekivano / poznati problemi | `[REPOZITORIJUM / OCEKIVANO_PONASANJE / POZNATI_PROBLEMI]` |

Kod, lock fajlovi, toolchain fajlovi, izvrsene komande, deployovani artefakt i ogranicenja baze su dokazi. Dokumentacija je samo kontekst.

Ako podatak nije prosledjen, pokusaj da ga utvrdis iz projekta; inace oznaci `NEPROVERENO`. Ne pretpostavljaj web servis samo zbog `main`, microservice samo zbog Go, systems komponentu samo zbog Rust, Tokio samo zbog async Rust, niti PostgreSQL samo zbog odredjenog ORM-a.

