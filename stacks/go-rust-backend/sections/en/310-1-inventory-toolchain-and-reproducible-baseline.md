## 1. Inventory, Toolchain, And Reproducible Baseline

Map path (GO/RUST/MIXED), modules/workspaces/crates, toolchain pins, lock files, feature/build-tag matrices, executables, and deployment units.

Table: `Component | Project version | Resolved | Current stable | Support/EOL | Compatibility | Action`.

For Go: `go`/`toolchain` directive, actual `go version`, stdlib, GOTOOLCHAIN, modules, framework, driver, build tools, base image.

For Rust: rustc, Cargo, channel, rust-toolchain, rust-version, edition, resolver, lockfile, async runtime, framework, DB/TLS/serde crates, test/build tools, base image.

Run deterministic build/test/lint/race/audit baseline and record the first failure.

