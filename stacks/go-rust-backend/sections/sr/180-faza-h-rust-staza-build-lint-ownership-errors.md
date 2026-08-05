## Faza H - RUST STAZA: Build, Lint, Ownership, Errors

### Baseline

```text
cargo fmt --all -- --check
cargo check --workspace --all-targets
cargo build --workspace --all-targets --locked
cargo build --release --workspace --locked
cargo clippy --workspace --all-targets --locked -- -D warnings
cargo doc --workspace --no-deps --locked
cargo test --doc --workspace --locked
cargo test --workspace --locked
```

`cargo check` je brza provera, **nije** zamena za `cargo build`. Ne ukljucuj `--all-features` naslepo ako su feature-i medjusobno iskljucivi; napravi feature matricu. Ne ukljucuj kompletne pedantic/nursery/restriction grupe naslepo.

### Ownership i tipovi

Proveri: nepotrebno clone, preveliki lifetime, cyclic Rc/Arc, Weak, borrow preko async granice, self-referential strukture, Pin.

Send/Sync: da li tip stvarno sme da predje thread granicu; `unsafe impl Send/Sync` bez formalnog invarianta je P0/P1 kandidat.

Interior mutability: `Cell`/`RefCell`/`Mutex`/`RwLock`/`Atomic*`; scope locka; poison; deadlock; async + `std::sync::Mutex` na executor threadu.

### Error handling

Proveri: `Result` vs panic, `unwrap`/`expect` u production putanjama, `?` i error context (`thiserror`/`anyhow` gde postoji), discard `Result`, partial cleanup, `catch_unwind` kao univerzalno resenje. Ne dodavaj panic/unwrap kao brzu popravku.

