## Phase A - Protect The Workspace

Before changes:

- repo root, branch, status, uncommitted changes, commit SHA, submodules;
- Go module/workspace files (`go.mod`, `go.sum`, `go.work`);
- Rust workspace/crate files (`Cargo.toml`, `Cargo.lock`, `rust-toolchain.toml`);
- generated code, native libraries, vendored source;
- secrets only by path and type (no contents);
- test configuration; prevent connections to production systems;
- target OS and architecture.

```text
git status --short --branch
git rev-parse --show-toplevel
git rev-parse HEAD
git submodule status
go version
go env
rustc -Vv
cargo -Vv
rustup show
rustup show active-toolchain
```

