## Faza G - RUST STAZA: Toolchain, Cargo I Workspace

### Toolchain

```text
rustc -Vv
cargo -Vv
rustup show
```

Proveri: active toolchain, host triple, targets/components, `rust-toolchain`/`rust-toolchain.toml`, channel, pinovana verzija, profile, nightly datum, RUSTFLAGS, linker, target config.

Stable vs nightly: da li production koristi stable; zasto nightly; koje feature zastavice ga zahtevaju; da li je nightly pinovan na datum; da li CI testira stable. Ne koristi floating nightly za reproduktivan production build.

### Edition i MSRV

Proveri: `edition`, `rust-version`, workspace-level vrednosti, resolver (Edition 2024 -> resolver 3), CI na MSRV-u, dependency-je koji su podigli MSRV, edition migration warninge.

`edition` i `rust-version` nisu ista stvar. Najnovija edition ne mora automatski znaciti najnoviji compiler, ali funkcije i dependency-ji mogu to zahtevati.

### Workspace i lockfile

Mapiraj members, default/excluded, virtual workspace, shared deps, profiles, `[patch]`/`[replace]`, features, bin/lib/proc-macro/build/dev deps.

```text
cargo metadata --format-version 1
cargo tree
cargo tree -d
cargo tree -e features
```

Proveri duple major verzije, duple native biblioteke, feature unification, razlicite TLS backend-e, vise async runtime verzija. Ne uklanjaj duplicate samo zato sto se pojavljuje u tree-u.

Lockfile: da li postoji i da li treba biti commitovan (da za executable/servis); yanked; git dependency; checksum; `--locked`/`--frozen`; offline build.

