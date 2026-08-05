## Napredni Produkcioni Audit Ugovor 2.0

Ova sekcija unapređuje prethodnu kontrolnu listu u source-to-runtime produkcioni audit ugovor. Kada postoji konflikt u formulaciji, primenjuje se stroži zahtev za dokaz, bezbednost, kompatibilnost i oporavak iz ove sekcije.

### Nivoi Dokaza

| Nivo | Minimalno prihvatljivo značenje |
| --- | --- |
| E0 | Samo tvrdnja, roadmap, ticket, dokumentacija ili pretpostavka. |
| E1 | Statički source, build, konfiguracioni, schema ili dependency dokaz. |
| E2 | Razrešeni graph, generisani source, bytecode, artefakt, manifest, digest, potpis ili SBOM dokaz. |
| E3 | Izvršeni test, lokalni runtime, container, migration rehearsal ili integration dokaz. |
| E4 | Staging ili production-like load, rollout, telemetrija, failure ili rollback dokaz. |
| E5 | Produkcijsko posmatranje, izolovani restore, incident drill ili nezavisno reprodukovan dokaz. |

Svaki materijalni zaključak mora navesti nivo dokaza. Bezuslovna production-ready odluka zahteva dokaz proporcionalan riziku, a ne samo veliki broj statičkih nalaza.

### Granica Dokaza

- Nastavi bezbedno istraživanje kada informacije nedostaju, ali svaki nerazrešeni materijalni zaključak označi kao `UNVERIFIED`.
- Navedi tačan repozitorijum, artefakt, okruženje, kredencijal, fixture, workload, odobrenje, telemetriju ili operator pristup potreban za viši nivo dokaza.
- Ne zaključuj produkciono ponašanje iz lokalnog IDE startup-a, unit testa, zelenog pipeline-a, mutable image taga ili zdrave liveness probe.
- Ne tretiraj advisory kao exploitable bez reachable putanje niti odsustvo scanner nalaza kao odsustvo rizika.

### Source-To-Runtime Lanac Identiteta

Zabeleži i poveži:

1. repozitorijum, commit, dirty state, submodule, generisani source i build ulaze;
2. JDK vendor, tačnu verziju i patch, arhitekturu, licencu/podršku, trust store, locale, vremensku zonu i JVM flagove;
3. Maven ili Gradle wrapper distribuciju, checksum, build JVM, toolchain-e, profile, properties, repozitorijume, mirror-e, plugin-e, ekstenzije i init skripte;
4. razrešene zavisnosti, BOM-ove, lock ili verification metadata, annotation procesore, generatore, shaded klase, native biblioteke i agente;
5. bytecode target, JAR/WAR/native image digest, manifest, build info, SBOM, potpis ili provenance, container layer-e i release identifikator;
6. deployment reviziju, configuration verziju, schema verziju, runtime process identitet i telemetry release atribute.

Dokaži da pokrenuti proces koristi nameravani artefakt i konfiguraciju. Source commit i image tag bez digest-a i runtime korelacije predstavljaju nepotpun dokaz.

### Obavezni Dnevnik Komandi

Za svaku izvršenu komandu zabeleži:

- tačnu komandu i working directory;
- lokalno, container, CI, staging ili production-like okruženje;
- JDK, Maven/Gradle, profil, target i relevantne environment vrednosti;
- početak/kraj ili trajanje, exit code, rezime rezultata i materijalne warning-e;
- redakciju tajni i ličnih podataka;
- da li je komanda promenila source, generisani izlaz, zavisnosti, stanje baze, cache, queue, fajlove ili infrastrukturu.

Za svaku neizvršenu proveru napiši: `UNVERIFIED - command not run because [konkretan razlog]`.

