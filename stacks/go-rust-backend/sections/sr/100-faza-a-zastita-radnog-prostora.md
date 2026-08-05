## Faza A - Zastita Radnog Prostora

Pre izmene:

- repo root, branch, status, necommitovane izmene, commit SHA, submodule-e;
- Go module/workspace fajlove (`go.mod`, `go.sum`, `go.work`);
- Rust workspace/crate fajlove (`Cargo.toml`, `Cargo.lock`, `rust-toolchain.toml`);
- generated code, native biblioteke, vendored source;
- tajne samo po putanji i tipu (bez sadrzaja);
- test konfiguraciju; spreci povezivanje sa production sistemima;
- target OS i architecture.

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

