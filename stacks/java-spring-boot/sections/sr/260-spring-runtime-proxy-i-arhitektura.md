## Spring Runtime, Proxy I Arhitektura

### Efektivni Runtime Graph

- Napravi inventar application context-a, parent/child context-a, auto-konfiguracija, korisničkih konfiguracija, bean definicija, scope-ova, qualifier-a, condition-a, profila, property-ja i startup runner-a.
- Sačuvaj `ConditionEvaluationReport`, efektivne bean tipove, poreklo, alias-e, proxy klase, order, primary kandidate i sve replacement ili exclusion odluke koje utiču na produkciono ponašanje.
- Uporedi nameru source-a sa efektivnim runtime graph-om u svakom podržanom profilu; bean vidljiv u source-u koji nije instanciran nije runtime dokaz.
- Detektuj slučajno duplirane klijente, transaction manager-e, scheduler-e, object mapper-e, security chain-ove, connection pool-ove, meter registry-je i cache manager-e.
- Zabeleži svaki framework-managed objekat koji poseduje thread-ove, socket-e, fajlove, pool-ove, timer-e, native handle-ove, privremene direktorijume ili shutdown obaveze.

### Proxy, Interception I Annotation Semantika

- Za svaki materijalni `@Transactional`, `@Async`, `@Cacheable`, `@Retryable`, `@PreAuthorize`, scheduling, validation ili custom advice annotation identifikuj proxy tip, invocation putanju, order i uslov aktivacije.
- Testiraj self-invocation, private/final metode, final klase, konstruktore, static metode, default interface metode, package granice, programsku invokaciju i pozive iz objekata kojima framework ne upravlja.
- Proveri advice redosled kada security, validation, transaction, cache, retry, metrics, tracing i custom interceptor-i obavijaju istu operaciju.
- Razdvoji interface-based i class-based proxy-je, AspectJ weaving, bytecode instrumentaciju, native-image ograničenja i ponašanje pod test slice-ovima ili mock-ovima.
- Source annotation bez dokaza da nameravani runtime poziv prolazi kroz nameravani proxy označi kao `UNVERIFIED`.

### Konfiguracija, Profili, Flagovi I Tajne

- Popiši configuration source-ove i precedence: zapakovane fajlove, profile fajlove, import-e, config tree-jeve, environment promenljive, system property-je, command-line argumente, remote config, secret store-ove i platformsku injekciju.
- Uporedi efektivne vrednosti kroz local, test, staging, canary, production, disaster-recovery i migration režime uz redakciju tajni.
- Validiraj typed konfiguraciju, obavezne vrednosti, opsege, jedinice, URL-ove, trajanja, veličine, liste, mape i međusobno isključive opcije pri startup-u ili pre prve upotrebe.
- Audituj refresh i feature-flag ponašanje za atomarnost, vidljivost, stale cache, parcijalnu primenu, rollback, expiry, ownership i audit log.
- Dokaži da tajne nisu commit-ovane, ugrađene u image, izložene kroz Actuator, logove, heap dump, exception poruke, pregled environment-a ili support bundle.

### Domenske Granice I Poslovne Invarijante

- Mapiraj module, package-e, aggregate-e, servis-e, repository-je, adapter-e, event-e, spoljne ugovore i ownership; označi cikluse i cross-boundary pristup koji zaobilazi invarijante.
- Izrazi svaku kritičnu invarijantu, state tranziciju, authorization pravilo, monetarno pravilo, kvotu, uniqueness pravilo i uslov side effect-a u izvršivom ili testabilnom obliku.
- Isprati komande od boundary validacije kroz authorization, domensku mutaciju, persistence, objavu event-a, cache invalidaciju i generisanje odgovora.
- Testiraj stale read, duple komande, paralelne aktere, retry, parcijalne failure-e, promene sata i event-e van redosleda protiv iste invarijante.
- Ne prihvataj samo controller validaciju ili database constraint kada invarijanta obuhvata više zapisa, servisa, tenant-a, vreme ili spoljne sisteme.

### Startup, Readiness I Shutdown

- Identifikuj svaku startup fazu, initializer, migraciju, cache warmup, registraciju, discovery, preuzimanje tajni, native load, uspostavljanje konekcija i background task.
- Razdvoji process alive, framework started, dependencies reachable, schema compatible, data ready, traffic ready i business operation ready stanje.
- Dokaži da readiness ne postaje zdrav pre obavezne inicijalizacije i da postaje nezdrav pre nego što shutdown prestane da prihvata novi rad.
- Testiraj vremenski ograničen graceful shutdown za HTTP, messaging, scheduling, transakcije, upload, streaming, lock-ove, lease-ove i in-flight side effect-e.
- Definiši oporavak posle prekinutog startup-a i shutdown-a, uključujući dupli rad, napuštene lock-ove, parcijalne migracije, privremene fajlove i nepotvrđene poruke.


