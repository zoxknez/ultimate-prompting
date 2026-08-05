## 1. Inventar, Toolchain I Reproduktivni Baseline

Mapiraj stazu (GO/RUST/MIXED), module/workspace/crate, toolchain pinove, lock fajlove, feature/build-tag matrice, executable i deployment jedinice.

Tabela: `Komponenta | Verzija u projektu | Resolved | Aktuelna stabilna | Support/EOL | Kompatibilnost | Akcija`.

Za Go: `go`/`toolchain` direktiva, stvarni `go version`, stdlib, GOTOOLCHAIN, moduli, framework, driver, build alati, base image.

Za Rust: rustc, Cargo, channel, rust-toolchain, rust-version, edition, resolver, lockfile, async runtime, framework, DB/TLS/serde crate-ovi, test/build alati, base image.

Pokreni deterministicki build/test/lint/race/audit baseline i zabelezi prvi neuspeh.

