## Verifikacija Build-a, Toolchain-a I Supply Chain-a

### JDK I JVM Identitet

- Proveri `java -version`, `javac -version`, vendor property-je, patch/build, arhitekturu i JVM unutar stvarnog release image-a ili hosta.
- Razdvoji JDK koji pokreće Maven/Gradle, compilation toolchain, test JVM, native-image toolchain i produkcioni runtime.
- Proveri bytecode target i API target odvojeno; `sourceCompatibility`, `targetCompatibility`, `--release` i toolchain deklaracije mogu se razići.
- Pregledaj preview/incubator/interne API-je, vendor-specifične flagove, uklonjene module, illegal access, native access i ponašanje kroz podržane JDK patch-eve.
- Proveri politiku kvartalnih security update-a, emergency patch proces, runtime licencu/podršku, rollback i compatibility test scope.

### Maven Build Poverenje

- Proveri wrapper distribution URL, checksum ili potpis, Maven verziju, `.mvn` konfiguraciju, build JDK, `toolchains.xml`, `settings.xml`, mirror-e, server-e, proxy-je, ekstenzije i aktivne profile.
- Pregledaj effective POM, parent hijerarhiju, importovane BOM-ove, dependency management, plugin management, repozitorijume, plugin repozitorijume, scope-ove, classifier-e, relocation-e i optional zavisnosti.
- Pinuj i pregledaj compiler, Surefire, Failsafe, Enforcer, Shade, Spring Boot, Jib, native, release, deploy, signing i publication plugin-e.
- Proveri dependency convergence, duplicate klase, reproduktivne timestamp-ove, checksum-e, potpise, repository allow liste i plugin validation.
- Tretiraj Maven 3.10 i Maven 4 kao preview baseline dok njihov aktuelni zvanični status i kompatibilnost projekta nisu eksplicitno odobreni.

### Gradle Build Poverenje

- Proveri wrapper distribution URL i SHA-256, Gradle runtime JVM, Java toolchain-e, daemon podešavanja, init skripte, included/composite build-ove, buildSrc, convention plugin-e i version catalog-e.
- Pregledaj repozitorijume, exclusive content, dependency verification, locking, constraint-e, platforme, capabilities, substitution-e, dinamičke verzije, changing module-e i resolution rules.
- Pregledaj custom taskove, `Exec` i `JavaExec`, script plugin-e, generisani source, annotation procesore, publication, signing, test suite-ove, configuration cache i build cache.
- Dokaži da cache key-evi uključuju sve materijalne ulaze i da remote cache ne može ubaciti stale, cross-branch, cross-tenant ili nepoverljiv izlaz.
- Proveri podržane Gradle/JDK i Spring Boot/plugin kombinacije u projektnoj matrici, ne samo na jednoj developerskoj mašini.

### Generator I Build-Execution Površina

- Inventariši Lombok, MapStruct, Querydsl, jOOQ, OpenAPI, protobuf, Avro, annotation procesore, bytecode enhancement, GraalVM reachability metadata i custom generatore.
- Tretiraj build plugin-e, procesore, generatore, shell komande, native compiler-e, preuzete alate i container build korake kao izvršne supply-chain ulaze.
- Zabeleži izvor, verziju, pin, checksum/potpis, network pristup, kredencijale, generisane putanje, determinizam i review ownership.
- Regeneriši iz čistog checkout-a i uporedi izlaz; neobjašnjiv generated drift blokira tvrdnju o reproduktivnosti.

### Analiza Zavisnosti I Advisory-ja

- Razreši stvarni graph po profilu, source set-u, target-u, optional integraciji i artefaktu; lista deklarisanih zavisnosti nije dovoljna.
- Detektuj dependency confusion, typosquatting, mutable snapshot-e, nepoverljive repozitorijume, skrivene plugin zavisnosti, shaded ranjivi kod i duple verzije.
- Poveži advisory-je sa reachable kodom, konfiguracijom, podacima, protokolom, class loading-om, reflection-om, native putevima i deployment izloženošću.
- Zabeleži CVE/advisory, pogođeni opseg, razrešenu verziju, reachability, exploit preduslove, kompenzacione kontrole, popravku, test, rollout i preostali rizik.
- Generiši SBOM i provenance gde su podržani, ali nijedan ne tretiraj kao dokaz ispravnosti ili neeksploatabilnosti.

