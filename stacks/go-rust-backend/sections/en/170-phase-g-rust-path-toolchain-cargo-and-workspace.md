## Phase G - RUST PATH: Toolchain, Cargo, And Workspace

### Toolchain

```text
rustc -Vv
cargo -Vv
rustup show
```

Check: active toolchain, host triple, targets/components, `rust-toolchain`/`rust-toolchain.toml`, channel, pinned version, profile, nightly date, RUSTFLAGS, linker, target config.

Stable vs nightly: whether production uses stable; why nightly exists; which feature flags require it; whether nightly is date-pinned; whether CI tests stable. Do not use floating nightly for a reproducible production build.

### Edition and MSRV

Check: `edition`, `rust-version`, workspace-level values, resolver (Edition 2024 → resolver 3), CI on MSRV, dependencies that raised MSRV, edition migration warnings.

`edition` and `rust-version` are not the same. The newest edition does not automatically mean the newest compiler, but features and dependencies may require it.

### Workspace and lockfile

Map members, default/excluded, virtual workspace, shared deps, profiles, `[patch]`/`[replace]`, features, bin/lib/proc-macro/build/dev deps.

```text
cargo metadata --format-version 1
cargo tree
cargo tree -d
cargo tree -e features
```

Check duplicate major versions, duplicate native libraries, feature unification, different TLS backends, multiple async runtime versions. Do not remove duplicates merely because they appear in the tree.

Lockfile: whether it exists and should be committed (yes for executables/services); yanked; git dependencies; checksums; `--locked`/`--frozen`; offline build.

