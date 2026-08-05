# Revizija 07 - Go / Rust backend i systems production audit prompt

## Sažetak

Postojeći EN/SR par bio je kvalitetan i strukturno usklađen, ali je i dalje predstavljao naprednu kontrolnu listu više nego kompletan, dokaziv production audit ugovor. Imao je 628 linija i 58 naslova po jeziku. Posebno su nedostajali formalni nivoi dokaza, source-to-runtime identitet, potpune build tag i Cargo feature matrice, dublji ABI/soundness ugovor, rigorozan overload i partial-failure model, obavezne evidence matrice i standardizovani recovery scenariji.

Nova verzija 2.0.0 ima 910 linija i 97 naslova po jeziku. Engleska i srpska verzija imaju identičan strukturni oblik svih linija i izrađene su kao jedan sinhronizovan dvojezični ugovor.

## Stanje pre unapređenja

Dobre strane prethodne verzije:

- korektno razdvajanje Go, Rust i mešovite tehnološke staze;
- dobar osnovni operativni ugovor i P0-P3 registar nalaza;
- korisne Go sekcije za goroutine, channel, context, `database/sql`, cgo i race detector;
- korisne Rust sekcije za Cargo, MSRV, unsafe, FFI, Miri, sanitizer-e i async runtime;
- osnovna pokrivenost transakcija, messaging-a, security-ja, performance-a, observability-ja, CI/CD-a i rollback-a;
- strukturni EN/SR paritet je već prolazio.

Glavni nedostaci:

1. Nije postojao formalni E0-E5 model koji sprečava preuveličavanje statičkog ili delimičnog dokaza.
2. Nije se dokazivao ceo identitet od commit-a i toolchain-a do binarnog fajla, deployment revizije, procesa, telemetrije i recovery-ja.
3. Go `go` i `toolchain` direktive, `GOTOOLCHAIN`, automatsko preuzimanje toolchain-a i stvarni compiler identitet nisu bili dovoljno strogo razdvojeni.
4. Build tag, GOOS, GOARCH, cgo, libc, FIPS/TLS i opcione integracije nisu imale obaveznu support matricu.
5. Race detector je pomenut, ali nije dovoljno jasno ograničeno šta čist run zaista dokazuje.
6. Nisu dovoljno razrađeni goroutine ownership, close autoritet, channel retained memory, scheduler i shutdown deadline.
7. Rust `cargo check` ograničenje nije bilo ugrađeno kao centralno pravilo artifact verifikacije.
8. Cargo feature kombinacije, target-specifične zavisnosti, profile-i, build script-e i proc macro-i nisu imali dovoljno strogu supply-chain i compatibility proveru.
9. Unsafe analiza nije zahtevala pun ugovor za provenance, aliasing, initialization, deallocation, unwind i safe API soundness.
10. Async cancellation safety, lock preko await-a, detached task failure i slow-consumer amplification nisu bili dovoljno sistematizovani.
11. HTTP, gRPC, TCP, UDP, QUIC i custom protokoli nisu imali jedinstvenu obaveznu contract matricu.
12. Transakcije, outbox/inbox, schema evolution, old/new binary koegzistencija, fencing i distributed lock nisu bili dovoljno duboko povezani.
13. Overload, retry multiplication, cancellation storm i recovery nisu imali obavezne merljive scenarije.
14. Nisu postojale standardne evidence matrice za toolchain, artifacts, concurrency, FFI, API, data, migrations, supply chain, SLO i recovery.
15. Production odluka nije bila dovoljno strogo vezana za zatvorene P0/P1 nalaze, immutable artifact, rollback i restore dokaze.

## Ključna unapređenja

### Formalni dokazni model

Dodati su nivoi:

- `E0` - tvrdnja bez proverljivog dokaza;
- `E1` - statički repository ili configuration dokaz;
- `E2` - resolved build, dependency ili generated-output dokaz;
- `E3` - izvršen test, analyzer, benchmark ili kontrolisana reprodukcija;
- `E4` - release-like artifact i target-environment dokaz;
- `E5` - production ponašanje ili dokazan recovery.

Materijalna tvrdnja ne sme dobiti viši status od stvarno dobijenog nivoa dokaza.

### Source-to-runtime identitet

Prompt sada zahteva usklađivanje:

`repository -> commit -> toolchain -> resolved graph -> generated code -> tags/features -> native/linker inputs -> artifact digest -> registry/package -> deployment revision -> process -> telemetry -> schema -> recovery`

Time se sprečavaju pogrešni zaključci zasnovani samo na `go.mod`, `Cargo.toml`, zelenom CI-ju ili image tag-u.

### Go audit

Dodate su detaljne provere za:

- `go version`, `go env`, `go`, `toolchain`, `GOTOOLCHAIN`, workspace i builder toolchain;
- module graph, `replace`, `exclude`, `retract`, private proxy, checksum bazu, vendor i lokalne fork-ove;
- `go generate`, protobuf, OpenAPI, SQL generatore, mock-ove i embedded asset-e;
- build tag, platform suffix, GOOS, GOARCH, cgo, libc, FIPS i TLS varijante;
- artifact metadata, VCS informacije, linkovanje, simbole, stripping i reproducibility;
- goroutine creator, cancellation, join, terminal condition, panic policy i shutdown deadline;
- channel ownership, close autoritet, buffer razlog, retained memory i slow-consumer ponašanje;
- race, deadlock, goroutine/timer leak, blocked send, map, atomic, WaitGroup i pool greške;
- heap, allocation rate, GC pacing, escape behavior, stack growth, finalizer zavisnost i resurs lifecycle;
- pprof, trace i benchmark dokaz za CPU, scheduler, lock, GC, syscall, mrežna i database uska grla.

### Rust audit

Dodate su detaljne provere za:

- `rustc -Vv`, Cargo, channel, target komponente, `rust-toolchain.toml`, `rust-version`, edition i resolver;
- odvojenu proveru MSRV-a i aktuelnog stable toolchain-a;
- release/test/bench/dev/custom profile-e, LTO, panic strategy, overflow, stripping i reproducibility;
- workspace članove, target-specifične zavisnosti, registry/git/path izvore, `[patch]`, vendor i yanked verzije;
- additive, mutually exclusive, no-default, target, backend, TLS, database, allocator, SIMD i FIPS feature-e;
- opravdanu kombinatornu feature matricu umesto slepog `--all-features` pristupa;
- `build.rs`, proc macro-e, bindgen, native build, linker directive i environment supply-chain površinu;
- ownership, `Arc`, `Weak`, interior mutability, lock order, Drop, partial initialization i foreign resource lifecycle;
- svaki `unsafe` blok, unsafe trait/impl, raw pointer, union, transmute, inline assembly, allocator, SIMD i FFI boundary;
- validity, alignment, provenance, initialization, aliasing, lifetime, thread-safety, unwind, ownership transfer i deallocation safety ugovor;
- ABI, calling convention, integer width, layout, padding, string, buffer, allocator pairing i cross-language unwind;
- Miri, sanitizer, fuzzing, property test, Loom/model checking i njihove granice;
- async runtime ownership, task supervision, cancellation safety, blocking na worker-u, unbounded spawn, lock preko await-a i shutdown.

### Zajednička distribuirana ispravnost

Dodate su posebne sekcije za:

- HTTP, gRPC, protobuf, TCP, UDP, QUIC i custom protocol contract;
- request smuggling, forwarded header, TLS termination, frame length, decompression i parser limite;
- state-changing flow od validacije do commit-a, side effect-a, retry-ja i reconciliation-a;
- database constraint-e, isolation, lock order, optimistic token, deadlock i serialization failure;
- trajni idempotency, request fingerprint, replay rezultat i multi-replica konkurentnost;
- outbox, inbox, CDC, saga, compensation, DLQ i database/broker partial failure;
- expand-and-contract migracije, backfill, cutover, rollback limit i forward repair;
- cache namespace, tenant scope, stampede, stale policy, distributed lock i fencing;
- queue delivery, ack, visibility timeout, rebalance, ordering, retry budget i poison message;
- admission control, load shedding, bulkhead, bounded queue, fan-out, retry multiplication i deadline propagation.

### Obavezne matrice i scenariji

Dodato je 12 obaveznih evidence matrica:

1. source, toolchain i artifact identitet;
2. executable, module, crate i deployment inventar;
3. Go target i build-tag podrška;
4. Rust target, feature, MSRV i profile podrška;
5. concurrency i lifecycle ownership;
6. unsafe, cgo, FFI, native i ABI granice;
7. API, RPC, stream i protocol contract;
8. poslovni tok promene stanja;
9. schema i migration kompatibilnost;
10. dependency i supply-chain poverenje;
11. SLO, capacity, overload i observability;
12. rollout, rollback, restore i incident spremnost.

Dodato je i 18 obaveznih adversarial/failure scenarija, uključujući paralelne mutacije, replay oko commit-a, client disconnect, zlonamerni peer, resource exhaustion, downstream slowdown, retry storm, shutdown tokom in-flight rada, process crash, old/new koegzistenciju, retku tag/feature putanju, stale lease, broker replay, cross-tenant pokušaj, rotaciju ključeva, izolovani restore, proveru telemetrije tokom degradacije i rollback posle različitih tipova promena.

### Posebni target-i

Dodati su overlay-i za:

- CLI, daemon i system service;
- WebAssembly i plugin sisteme;
- embedded i constrained target-e;
- no-std, watchdog, power failure, flash wear, firmware signing i hardware-in-the-loop proveru.

### Release i recovery

Prompt sada zahteva:

- promociju jednog immutable artefakta;
- canary i rollout gate-ove sa merljivim abort signalima;
- stvarnu proveru graceful shutdown-a prema orchestration timing-u;
- eksplicitne rollback granice posle schema, message, cache, key i file-format promena;
- izolovani restore sa proverom RPO, RTO, ključeva i reconciliation-a;
- incident režim sa čuvanjem dokaza, containment-om, revocation-om, trusted rebuild-om i eradication proverom.

## Aktuelni baseline

Baseline je ažuriran na 5. avgust 2026. i koristi zvanične izvore za:

- Go 1.26.5 i podržanu 1.25.x liniju;
- Go toolchain selection i `GOTOOLCHAIN` ponašanje;
- Go vulnerability management i `govulncheck` ograničenja;
- Rust 1.97.1 i ispravku LLVM miscompilation-a iz 1.97.0;
- Cargo `check`, build, feature i build-script ponašanje;
- Rust unsafe pravila i Miri kao dodatni, ograničeni UB dokaz.

Sve verzije i politike moraju ponovo da se provere tokom stvarnog audita.

## Rezultati validacije

- prethodni EN: 628 linija, 58 naslova;
- prethodni SR: 628 linija, 58 naslova;
- novi EN: 910 linija, 97 naslova;
- novi SR: 910 linija, 97 naslova;
- EN/SR line-shape odstupanja: 0;
- heading-count i heading-depth paritet: prošao;
- YAML frontmatter: validan;
- JSON baseline manifest: validan;
- Markdown fence blokovi: balansirani;
- baseline hardcode scan: prošao;
- en dash u SR promptu: 0;
- em dash u SR promptu: 0;
- non-breaking hyphen u SR promptu: 0.

Repository-level checker i dalje očekivano prijavljuje samo stare Java/Spring i Python/PySide6 parove, koji još nisu obrađeni.

## Ocena

Novi Go/Rust paket je znatno bliži punom production audit ugovoru nego prethodna verzija. Posebno je unapređena dokazivost, toolchain i artifact identitet, concurrency lifecycle, unsafe/FFI soundness, distributed correctness, overload ponašanje, release kontrola i recovery. Prompt i dalje zahteva stručnu primenu i stvarne projektne dokaze; njegova širina ne zamenjuje izvršenje testova, target pristup, produkcionu telemetriju ili restore probu.
