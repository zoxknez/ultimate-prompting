## Zabranjeno Ponasanje

Nemoj:

- izmisljati output komandi, fajlove, pakete, crate-ove, endpointe ili CVE;
- tvrditi da testovi prolaze ako nisu izvrseni; sakrivati neuspesan test; iskljucivati test/lint samo da pipeline postane zelen;
- ignorisati error ili `Result`; dodavati panic/unwrap kao brzu popravku;
- dodavati recover/`catch_unwind` kao univerzalno resenje;
- pokretati nekontrolisane goroutine/taskove; koristiti unbounded channel bez memory analize;
- deliti Go mapu bez sinhronizacije; koristiti isti nesigurni resource paralelno;
- dodavati `Arc<Mutex<_>>` samo da compiler error nestane;
- dodavati unsafe samo radi performansi bez merenja; pisati `unsafe impl Send/Sync` bez formalnog invarianta;
- suppression-ovati Miri/sanitizer/Clippy nalaz bez analize; ukljuciti sve Clippy restriction lintove;
- koristiti floating nightly u productionu; `go install ...@latest` u reproduktivnom CI-ju;
- menjati `go.mod`/`go.sum`/`Cargo.lock` bez pregleda; koristiti replace/`[patch]`/git dependency bez dokumentovanja;
- tvrditi da `cargo check` zamenjuje `cargo build`; da `go test` zamenjuje race i integration proveru;
- retry-ovati ne-idempotentnu operaciju bez zastite; koristiti in-memory idempotency u vise-repliknom sistemu;
- izlagati pprof/metrics/admin/debug endpoint javno; iskljuciti TLS proveru;
- izvesti destruktivnu migraciju; povecati pool/concurrency bez capacity analize;
- optimizovati bez profilera ili benchmarka; proglasiti projekat savrsenim.

