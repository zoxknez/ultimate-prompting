## 1. Current Research Baseline - Re-Check Before Every Audit

This baseline is a starting point, not a substitute for verification at execution time. Re-check current first-party sources and the actual project before recommending or changing anything.

| Component | Confirmed status on 5 August 2026 | Mandatory audit-time verification |
| --- | --- | --- |
| Go stable | Current stable line is Go 1.26.5 (released 7 July 2026; security/bugfix patch of the 1.26 line). | `go version`, `go` directive, `toolchain` directive, `GOTOOLCHAIN`, production image. |
| Go 1.27 | Not yet released; documentation is draft, expected during August 2026. | Do not treat draft as a production baseline without explicit approval. |
| Go support | No classic LTS. Each major line is supported until two newer majors ship; currently supported are Go 1.26 and Go 1.25 (e.g. 1.25.12 on the same July patch wave). | Actual support status, EOL, and upgrade plan. |
| Go compatibility | Strong compatibility promise, but behavioral changes may ship with the `go` directive and `GODEBUG`. | Toolchain, module `go` version, `GODEBUG` overrides, and release notes. |
| Go production tools | Race detector, built-in fuzzing, and `govulncheck` (vulnerabilities + reachability/call graph; limits: reflect/unsafe can cause false negatives; binary mode is less precise). | `go test -race`, fuzz targets, pinned `govulncheck`, CI matrix. |
| Rust stable | Rust 1.97.1 released 16 July 2026 (1.97.0: 9 July 2026). The point release fixes an LLVM miscompilation; 1.97.0 is not an equivalent production baseline. | `rustc -Vv`, `rust-toolchain.toml`, CI pin, image/digest. |
| Rust support | Six-week release train; only the latest stable is officially supported; previous stable enters EOL when the new one ships. | Explicit MSRV and CI on both MSRV and latest stable. |
| Rust edition | Edition 2024 is the current line; it defaults to Cargo resolver 3, which considers `rust-version` when selecting dependency versions. | `edition`, `rust-version`, resolver, lockfile, dependency MSRV. |
| Rust build | `cargo check` is not full build verification; official Rust policy treats `cargo build` as authoritative for all compilation errors. | Release/workspace build, feature matrix, `--locked`. |
| Rust lint/unsafe | Clippy is standard; do not enable pedantic/nursery/restriction groups blindly. Unsafe requires hand-checked safety invariants; Miri is an extra UB check, not a formal proof of full soundness. | Clippy policy, unsafe inventory, Miri/sanitizer limits. |

Note: at real audit time always use the current release/support record, not a hard-coded version from this baseline.

