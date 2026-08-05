## Napredna Rust production provera

### Toolchain, edition, MSRV, resolver i profile-i

- Zabeleži `rustc -Vv`, Cargo verziju, kanal, target komponente, `rust-toolchain.toml`, `rust-version`, edition, resolver, profile podešavanja, linker, source standardne biblioteke i CI/container pin-ove.
- Testiraj deklarisani MSRV i aktuelni podržani stable odvojeno; obezbedi da dependency resolution, proc macro-i, build skripte, generisani kod, dokumentacija, primeri i testovi poštuju obećanje.
- Proveri pretpostavke migracije na Edition 2024, ponašanje resolver-a, dependency `rust-version` obradu, promene lint-a, unsafe promene i macro kompatibilnost umesto mehaničke promene edition-a.
- Pregledaj release, test, bench, dev i custom profile-e uključujući optimizaciju, debug informacije, overflow provere, panic strategiju, codegen unit-e, LTO, stripping, incremental stanje i reproduktivnost.
- Ne tretiraj `cargo check` kao release proveru; izvrši autoritativni build i testove za stvarne target-e, feature-e, profile-e i native zavisnosti.

### Cargo graf, feature-i, build skripte i proc macro-i

- Popiši workspace članove, isključene crate-ove, default članove, virtual manifeste, primere, benchmark-e, binarne fajlove, testove, build zavisnosti, dev zavisnosti, target-specifične zavisnosti i neobjavljene interne crate-ove.
- Pregledaj `Cargo.lock`, registry i git izvore, `[patch]`, `[replace]`, lokalne putanje, zamenu source-a, sparse registry, vendoring, yanked verzije, licence, duplirane verzije i dependency ownership.
- Modeluj additive, međusobno isključive, default, opcione, target, backend, TLS, database, allocator, SIMD, FIPS, tracing i test-only feature-e; otkrij kombinacije koje se kompajliraju ali krše invarijante.
- Kompajliraj podržanu feature matricu koristeći opravdanu kombinatornu strategiju; uključi no-default, all-features samo kada ima smisla, reprezentativne pairwise kombinacije i production preset-e.
- Audituj `build.rs`, proc macro-e, generisanje koda, čitanje okruženja, pristup fajl sistemu i mreži, native kompilaciju, bindgen ulaze, linker direktive, rerun uslove, generisane metapodatke i cache ponašanje kao izvršni supply-chain kod.

### Ownership, interior mutability i Drop semantika

- Prati ownership request-a, buffer-a, kredencijala, transakcija, task-ova, konekcija, file descriptor-a, memory mapping-a, lock-ova, callback-ova i stranih resursa kroz success i failure putanje.
- Pregledaj `Arc`, `Rc`, `Weak`, `Mutex`, `RwLock`, atomic operacije, `Cell`, `RefCell`, `OnceLock`, lazy inicijalizaciju, pinning, self-reference, cikluse, životni vek guard-a i redosled lock-ova.
- Proveri `Drop` ponašanje pri normalnom povratku, propagaciji greške, panic-u, abort-u, cancellation-u, završetku procesa, delimičnoj inicijalizaciji i stranim callback-ovima; nikada se ne oslanjaj na destructor za distribuirane efekte koji moraju da se dese.
- Pregledaj clone i copy operacije zbog skrivenog troška, zastarelog stanja, dupliranog ovlašćenja, zadržavanja tajni, ne-idempotentnih handle-ova i razilaženja logičkog i fizičkog ownership-a.

### Unsafe kod, memory model, FFI i soundness

- Popiši svaki `unsafe` blok, unsafe funkciju ili trait, unsafe impl, raw pointer, union, `MaybeUninit`, transmute, unchecked operaciju, inline assembly, allocator, SIMD intrinsic, FFI deklaraciju i unsafe granicu iz zavisnosti.
- Za svaku granicu dokumentuj safety ugovor: validnost, alignment, provenance, inicijalizaciju, aliasing, lifetime, thread-safety, panic ponašanje, unwind ponašanje, prenos ownership-a, dealokaciju i callback ograničenja.
- Dokaži da safe caller-i ne mogu da prekrše ugovor i da javni safe API-ji ostaju sound pod neprijateljskim validnim ulazima, reentrancy-jem, konkurentnošću, panic-om, cancellation-om i redosledom uništavanja.
- Proveri ABI, calling convention, širine integer-a, layout strukture, padding, enum-e, stringove, buffer-e, ownership, uparivanje allocator-a, pregovaranje verzije, vidljivost simbola, exception-e, signal-e i cross-language unwind politiku.
- Koristi Miri, sanitizer-e, fuzzing, property testove, Loom ili model checking, ciljani stress i code review gde su primenljivi; navedi target, zavisnost od nightly-ja, nepodržane operacije, prostor false negative rezultata i šta svaki alat ne može da dokaže.
- Nikada ne zaključuj soundness iz odsustva eksplicitnog unsafe koda u first-party kodu; tranzitivni crate-ovi, platformski API-ji, kernel-i, allocator-i, driver-i i strane biblioteke ostaju deo trusted computing base-a.

### Async runtime, task-ovi, cancellation i backpressure

- Identifikuj runtime ili executor, feature set, worker i blocking pool-ove, izvor tajmera, I/O driver, compatibility slojeve, runtime ownership, rizik nested runtime-a i shutdown semantiku.
- Za svaki spawned task identifikuj kreatora, svrhu, cancellation, join ili supervision putanju, panic obradu, ownership rezultata, ograničenost, tracing context i shutdown rok.
- Audituj cancellation safety `select` operacija, timeout-a, stream-ova, framed protokola, codec-a, database operacija, write operacija, lock-ova, channel-a i delimičnih state machine-a; dokaži šta sme bezbedno da se ponovi.
- Otkrij blocking rad na async worker-ima, neograničen spawn, neograničene redove, lock guard-e držane preko await-a, curenje task-ova, detached failure-e, lost wakeup, starvation, priority inversion, timer storm i pojačavanje sporog consumer-a.
- Testiraj overload admission, limite konkurentnosti, kapacitet reda, deadline-ove, cancellation storm, downstream zastoj, shutdown tokom in-flight rada i koegzistenciju starog i novog deployment-a.

### Rust error, panic i process-failure politika

- Definiši koji failure-i su validation, domain conflict, not found, unauthorized, dependency, timeout, overload, corruption, programmer bug, invariant violation ili neoporavljivo stanje procesa.
- Pregledaj `Result`, konverziju grešaka, context, source chain, stabilne spoljne error ugovore, redaction, retry klasifikaciju, metrike i ownership odluka o oporavku.
- Popiši `unwrap`, `expect`, indeksiranje, pretpostavke arithmetic overflow-a, unreachable putanje, process exit, abort, panic hook-ove, `catch_unwind` i panic preko FFI ili task granica.
- Ne pretvaraj kršenje invarijante u tiho nastavljanje; definiši fail-fast, izolaciju, restart, degradaciju, quarantine ili repair ponašanje koristeći dokaze i blast radius.

