## Napredna Go production provera

### Izbor Go toolchain-a i kompatibilnost

- Zabeleži `go version`, `go env`, module `go` direktive, `toolchain` direktive, workspace podešavanja, `GOTOOLCHAIN`, builder image-e i preuzete toolchain-e; razlikuj jezički baseline od kompajlera koji je stvarno napravio artefakt.
- Proveri promene ponašanja kontrolisane module `go` verzijom, release notes dokumentima, `GODEBUG`, eksperimentima, arhitekturom, cgo-om, linker režimom i promenama standardne biblioteke.
- Build-uj svaku release komandu i paket pod nameravanim podržanim toolchain-om i najmanje najstarijim obećanim compatibility baseline-om kada takvo obećanje postoji.
- Ne zaključuj identitet artefakta samo iz `go` direktive; dokaži kompajler, module graf, tag-ove, okruženje, linker ulaze i ugrađene build informacije.

### Poverenje modula, workspace-a, vendor-a i generatora

- Pregledaj sve `go.mod`, `go.sum`, `go.work`, `replace`, `exclude`, `retract`, private proxy, checksum bazu, vendor, lokalnu putanju, fork i odluke o generisanom source-u.
- Proveri da CI i release slučajno ne koriste developerski workspace, nepregledan lokalni replacement, promenljivu branch granu, nedostupan privatni modul ili zastareo vendor tree.
- Audituj `go generate`, generisanje koda, generisanje šeme, mock-ove, stringer-e, protobuf, OpenAPI, SQL generatore i embedded asset-e kao izvršne supply-chain ulaze.
- Pokreni analizu ranjivosti nad razrešenim grafom i dostupnim kodom gde je moguće, zatim dokumentuj slepe tačke vezane za reflection, plugin-e, dinamičko učitavanje, cgo, build tag-ove i dokaz samo iz binarnog fajla.

### Build tag-ovi, target-i i artifact matrica

- Popiši platformske sufikse, `//go:build` izraze, generisane kombinacije tag-ova, race i non-race build-ove, cgo i pure-Go varijante, FIPS ili boringcrypto varijante gde su primenljive i opcione integracije.
- Napravi support matricu: komanda ili biblioteka, `GOOS`, `GOARCH`, tag-ovi, cgo, libc, kernel, spoljne biblioteke, release profil, testovi, artefakt i vlasnik.
- Kompajliraj i testiraj podržanu matricu ili eksplicitno opravdaj reprezentativnu pokrivenost; ne dozvoli da nekompajlirani fajlovi ili neaktivni tag-ovi izbegnu pregled.
- Pregledaj build ID-jeve, VCS metapodatke, politiku simbola, stripping, statičko ili dinamičko linkovanje, reproduktivnost, veličinu binarnog fajla, executable dozvole i runtime library search putanje.

### Ispravnost goroutine-a, channel-a, context-a i scheduler-a

- Za svaki goroutine identifikuj kreatora, svrhu, izvor cancellation-a, terminalni uslov, wait ili join putanju, panic politiku, ograničenost, metrike i shutdown rok.
- Za svaki channel dokumentuj ownership, ovlašćenje za close, razlog buffer-a, maksimalno zadržanu memoriju, blocking ponašanje send/receive operacija, pretpostavke select pravičnosti i politiku za sporog consumer-a.
- Proveri propagaciju context-a kroz HTTP, RPC, bazu, red, fajl sistem, subprocess i interne pozive; razlikuj cancellation, deadline, prekid klijenta, overload odbijanje i shutdown.
- Testiraj race condition-e, deadlock, curenje goroutine-a, curenje timer-a i ticker-a, blokirane send operacije, close/send race, pogrešnu upotrebu WaitGroup-a, copylock, atomic alignment, pristup mapi, zloupotrebu pool-a i konkurentne lifecycle prelaze.
- Tretiraj čist race-detector run kao dokaz samo za izvršene putanje, arhitekturu, timing, tag-ove i workload; dodaj stress, ponavljanje, variranje scheduler-a i ciljane invarijante.

### Go memorija, resursi i runtime ponašanje

- Pregledaj stopu alokacija, zadržani heap, životni vek objekata, escape ponašanje, rast stack-a, GC pacing, zavisnost od finalizer-a, velike buffer-e, pooling, fragmentaciju i memory limite pod realnim load-om.
- Dokaži zatvaranje response body-ja, rows objekata, fajlova, pipe-ova, socket-a, subprocess-a, compression stream-ova, privremenih fajlova, transakcija i drugih resursa na success, error, cancellation, panic i shutdown putanjama.
- Pregledaj `sync.Pool`, `unsafe`, `reflect`, zero-copy konverziju, slice-ove koji dele backing array, aliasing, životni vek byte/string vrednosti, mmap i ponovnu upotrebu objekata zbog poverljivosti i ispravnosti.
- Koristi profile-e, trace-ove, metrike i benchmark-e da razlikuješ CPU, scheduler, lock, GC, allocation, syscall, mrežna, database i downstream uska grla.

