## Project Context

| Field | Value |
| --- | --- |
| Service | `[NAME]` |
| Purpose | `[DESCRIPTION]` |
| Clients | `[WEB / MOBILE / CLI / PARTNERS / INTERNAL / PUBLIC]` |
| Architecture | `[MONOLITH / MODULAR MONOLITH / MICROSERVICE / WORKER / SYSTEMS / OTHER]` |
| Technology | `[GO / RUST / MIXED_GO_RUST]` |
| Go module/workspace | `[GO_MODULE]` |
| Rust workspace/crate | `[RUST_WORKSPACE]` |
| Target platforms | `[LINUX / WINDOWS / MACOS / EMBEDDED / WASM / OTHER]` |
| Deployment | `[DOCKER / KUBERNETES / VM / BARE METAL / SERVERLESS / OTHER]` |
| Data | `[POSTGRESQL / MYSQL / SQLITE / REDIS / OTHER]` |
| Messaging/cache | `[MESSAGING / CACHE]` |
| Protocols | `[HTTP / gRPC / QUIC / TCP / UDP / OTHER]` |
| FFI/native | `[FFI / CGO / BINDGEN / NONE]` |
| Workload | `[WORKLOAD]` |
| CI/CD | `[CI_CD]` |
| Baseline/compatibility | `[REQUIRED_BASELINE / COMPATIBILITY]` |
| Work mode | `[AUDIT_ONLY / AUDIT_AND_SAFE_FIX / FULL_IMPLEMENTATION / FIX_CONFIRMED_ISSUES / SECURITY_AND_CONCURRENCY_AUDIT / PERFORMANCE_AUDIT]` |
| Regulatory and extra constraints | `[REGULATORY / CONSTRAINTS]` |
| Repo / expected / known problems | `[REPOSITORY / EXPECTED_BEHAVIOR / KNOWN_PROBLEMS]` |

Code, lock files, toolchain files, executed commands, deployed artifact behavior, and database constraints are evidence. Documentation is context only.

When an input is absent, try to establish it from the project; otherwise mark `UNVERIFIED`. Do not assume a web service merely because `main` exists, a microservice merely because Go is used, a systems component merely because Rust is used, Tokio merely because async Rust exists, or PostgreSQL merely because a particular ORM is present.

