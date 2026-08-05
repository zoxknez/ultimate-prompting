## 1. Aktuelni istrazivacki baseline - proveriti pre svakog audita

Ovaj baseline je polaziste, ne zamena za proveru pri svakom izvrsavanju. Pre preporuke ili izmene proveri aktuelne primarne izvore i stvarni projekat.

| Komponenta | Potvrdjeno stanje na 5. avgust 2026. | Obavezna provera pri auditu |
| --- | --- | --- |
| Go stabilna | Aktuelna stabilna linija je Go 1.26.5 (objavljen 7. jula 2026.; security/bugfix patch linije 1.26). | `go version`, `go` direktiva, `toolchain` direktiva, `GOTOOLCHAIN`, production image. |
| Go 1.27 | Jos nije objavljen; dokumentacija je draft, ocekivano izdanje tokom avgusta 2026. | Ne tretiraj draft kao production baseline bez eksplicitnog odobrenja. |
| Go podrska | Nema klasican LTS. Svaka major linija podrzana je dok ne budu objavljene dve novije major verzije; trenutno podrzane su Go 1.26 i Go 1.25 (npr. 1.25.12 na istoj julskoj patch talasi). | Stvarni support status, EOL i plan upgrade-a. |
| Go kompatibilnost | Jako obecanje kompatibilnosti, ali behavioral promene mogu ici uz `go` direktivu i `GODEBUG`. | Toolchain, module `go` verziju, `GODEBUG` override-e i release notes. |
| Go production alati | Race detector, ugradjeni fuzzing i `govulncheck` (ranjivosti + reachability/call graph; ogranicenja: reflect/unsafe mogu dati false negative; binary mode je manje precizan). | `go test -race`, fuzz targete, pinovan `govulncheck`, CI matricu. |
| Rust stabilna | Rust 1.97.1 objavljen 16. jula 2026. (1.97.0: 9. jul 2026.). Point release ispravlja LLVM miscompilation; 1.97.0 nije ekvivalentan production baseline. | `rustc -Vv`, `rust-toolchain.toml`, CI pin, image/digest. |
| Rust podrska | Sestonedeljni release train; zvanicno podrzana je samo najnovija stabilna; prethodna ulazi u EOL kada izadje nova. | Eksplicitan MSRV, CI na MSRV i latest stable. |
| Rust edition | Edition 2024 je aktuelna linija; podrazumeva Cargo resolver 3 koji uzima `rust-version` u obzir pri izboru dependency verzija. | `edition`, `rust-version`, resolver, lockfile, dependency MSRV. |
| Rust build | `cargo check` nije potpuna build verifikacija; `cargo build` je merodavna provera svih compilation gresaka. | Release/workspace build, feature matrica, `--locked`. |
| Rust lint/unsafe | Clippy je standard; pedantic/nursery/restriction ne ukljucivati naslepo. Unsafe zahteva rucne safety invarijante; Miri je dodatna UB provera, ne formalni dokaz potpune soundness. | Clippy politika, unsafe inventar, Miri/sanitizer ogranicenja. |

Napomena: pri stvarnom auditu uvek koristi aktuelni release/support zapis, ne hardkodovanu verziju iz ovog baseline-a.

