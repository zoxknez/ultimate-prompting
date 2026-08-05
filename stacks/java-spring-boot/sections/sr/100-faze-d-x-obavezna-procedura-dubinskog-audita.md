## Faze D-X - Obavezna Procedura Dubinskog Audita

### D. Java, JVM I Jezicka Ispravnost

Pregledaj Java `release`/bytecode target, Lombok/annotation processor, module path/classpath, reflection/proxy/generisani kod, serialization, classloader i JDK-internal API upotrebu. Proveri `null` ugovore, `Optional` granice, equals/hashCode/comparator ugovore, mutabilnost kolekcija, defensive copy, exception granice, resource zatvaranje, `try-with-resources`, prekide i cancellation. Proveri `BigDecimal` konstrukciju/scale/rounding, overflow, UUID/ID generisanje, kriptografsku slucajnost i bezbedne kolekcijske granice. Pregledaj vreme, zone, locale i formatiranje: `Instant` kao trajni trenutak gde je prikladno, jasne zone za poslovni datum/vreme, DST prelaze, clock injection, deterministicke testove i nedvosmislene API formate. Ne mesaj server lokalnu zonu sa korisnickom ili poslovnom zonom. Za records, sealed klase, pattern matching, text blockove, virtual threads, structured concurrency, foreign-function/memory API-je i preview feature-e proveri ciljnu JDK podrsku, library/agent kompatibilnost, deployment runtime i operativni rizik. Preview API nije production default bez eksplicitne odluke, podrzanog lifecycle-a i rollbacka.

### E. Konkurentnost, Virtual Threads I Reaktivni Tokovi

Za `Executor`, `CompletableFuture`, `@Async`, scheduler i virtual thread upotrebu proveri vlasnistvo executora, bounded concurrency, redove, rejection politiku, context/MDC/SecurityContext/trace propagaciju, cancellation, interrupt, exception posmatranje, lifecycle i metrike. Virtual threads ne uklanjaju ogranicenja baze, HTTP poola, rate limita, memorije ni spoljne zavisnosti; proveri pinning i bounded pristup scarce resursima. Za Reactor/WebFlux proveri da nema `block()`, `subscribe()` side-effecta ili JDBC/JPA rada na event loopu; proveri scheduler granice, backpressure, cancellation, `Context` propagaciju, timeout/retry redosled, buffer limite, hot/cold publisher semantiku i cleanup. Ne kombinuj imperativnu `@Transactional` JPA granicu sa reaktivnim tokom kao da dele istu transakciju.

### F. Poslovni Tokovi I Drzavni Model

Za svaki kritican tok nacrtaj stanje pre/uslov, komandu, autentikaciju/authorization/ownership/tenant proveru, validaciju, transakcioni zapis, spoljni side effect, dogadjaj, observabilnost, failure/compensation, retry/idempotency i stanje posle. Proveri nedozvoljene state transition-e, race scenarije, pravila za novac/inventar/licence, audit trail i admin override. Domain pravila ne smeju postojati samo u controlleru, klijentu ili UI-ju.

### G. HTTP, API I Granice Potrosaca

Auditiraj endpoint registraciju, path/method konflikt, content negotiation, deserialization, `@ControllerAdvice`, pagination/filter/sort allow liste, ETag/cache-control, download/upload i OpenAPI stvarno-vs-dokumentovano ponasanje. Odvoji javni, partner, internal i management API; uvedi kompatibilan version/deprecation plan kada je javni ugovor promenjen. Za gRPC proveri interceptor, deadline, metadata auth, message limits, reflection exposure i status mapping.

### H. Persistencija, SQL I Integritet Podataka

Uz JPA/Hibernate proveri JDBC template/raw SQL, R2DBC, driver, pool, prepared parametre, pagination, query plan, indekse, lockove, batch, cursor/stream zatvaranje i charset/collation. Dokazi query-plan i data-volume pretpostavke za skupe upite. Svaka data-migracija mora biti ponovljiva, merljiva, segmentirana i bezbedna za restart; razdvoji schema expand, backfill, application switch i contract korake.

### I. Transakcije, Outbox I Konzistentnost

Potvrdi granicu transakcije stvarnim testom, ne samo anotacijom. Pregledaj izolaciju, propagation, timeout, rollback pravila, transakcione eventove, entity lifecycle callback-ove, lazy granice i order poziva. Za database-plus-message/API/email/filesystem kombinacije izaberi dokumentovan obrazac: transactional outbox, inbox/deduplication, saga/kompenzacija ili namerno prihvacen rizik. Dokazi obradu pada pre i posle commit/ack granice.

### J. Migracije, Backup I Oporavak

Proveri redosled, checksum, baseline/repair politiku, transactional DDL pretpostavke, privilegije, lock time, retry i monitoring migracija. Backup nije dovoljan bez obnovljenog restore testa, RPO/RTO cilja, verifikacije integriteta i pristupa kljucevima. Ne edituj izvrsene migracije i ne koristi `clean`, `baseline`, `repair` ili destructive SQL nad podacima bez eksplicitnog odobrenja i dokaza okruzenja.

### K. Messaging I Asinhrona Obrada

Mapiraj producer/consumer, topic/queue, schema ownership, consumer grupu, partitions, retention, retry/DLQ, ordering, poison-message handling, idempotency i reprocessing proceduru. Proveri da li se commit/ack radi tek nakon trajnog obradjenog rezultata. Za scheduled procese proveri distributed lock/leader election, overlap pri deploy-u, clock/timezone i recovery posle propustenog izvrsavanja.

### L. Cache I Distribuirano Stanje

Proveri Caffeine/Redis/Hazelcast i svaki cache adapter: key scope, authorization/tenant segmentation, serialization, TTL, invalidaciju, cache stampede, Redis outage, eviction, memory limit, metrics i rollback. Distribuirani lock mora imati vlasnistvo, lease/renewal, failure semantiku i test split-brain/timeout scenarija; ne koristi ga kao zamenu za database constraint.

### M. Identitet, Sesije I Kriptografija

Pored login/OIDC/JWT provere, pregledaj key rotation, JWKS cache/failure, audience/issuer/algorithm allow listu, clock skew, token disclosure u logovima/URLs, session store, concurrent session pravila, CSRF i cookie domen/path. Kriptografske kljuceve, saltove, nonce-ove i algoritme preuzmi od standardnih biblioteka; ne implementiraj kriptografiju rucno. Verifikuj minimalne privilegije za service account, bazu, broker, cloud i CI identitete.

### N. Application Security I Supply Chain

Uradi targeted threat model po granicama poverenja: browser, partner, webhook, queue, fajl, admin, interni servis i cloud metadata. Proveri dependency/plugin provenance, checksum/signature gde je podrzano, repository allow list, dependency confusion, CVE sa stvarnom reachability procenom, SBOM, SLSA/provenance gde postoji i base-image digest. Ne proglasavaj CVE exploitable bez putanje izvrsavanja; ne ignorisi reachable problem zbog niskog CVSS-a.

### O. Konfiguracija, Tajne I Feature Kontrole

Proveri `application*.yml/properties`, profile, environment override, `SPRING_APPLICATION_JSON`, command-line argumente, config tree, external config i feature flagove. Svaka promena ponasanja mora imati vlasnika, default, audit, rollout i removal plan. Tajne ne smeju biti u source-u, test fixture-u, image layeru, logu, exceptionu, Actuatoru ni CI artefaktu. Proveri rotaciju i ponasanje kada secret nedostaje ili se promeni.

### P. Otpornost I Spoljne Zavisnosti

Napravi dependency matricu sa vlasnikom, SLO/deadline, timeout, retry kriterijumom, idempotency, circuit/bulkhead/rate-limit politikom, fallbackom, degradacijom i alertom. Timeout mora biti dosledan kroz inbound request, database, HTTP/gRPC i async job, sa budzetom manjim od nadredjenog deadline-a. Ne koristi neograniceni retry, globalne fallback odgovore koji skrivaju gubitak podataka ili fail-open za bezbednosne provere bez eksplicitne odluke.

### Q. Performanse I Kapacitet

Izmeri ili jasno oznaci kao neprovereno throughput, p95/p99 latenciju, error rate, alokacije/heap/GC, CPU, thread i connection pool saturation, queue lag, cache hit rate i database load za kriticne tokove. Proveri payload/pagination limite, algorithmic complexity, regex DoS, compression bomb, JSON depth, ORM query count i N+1. Performance optimizacija ne sme promeniti authorization, transakcioni integritet ili API semantiku bez testova.

### R. Observability I Incident Response

Proveri log schema, PII redaction, trace sampling, baggage propagaciju, metric cardinality, exemplare, dashboarde, alert fatigue i runbooke. Svaki alert mora moci da vodi do akcije. Incident tok treba da ukljuci correlation ID, release/commit verziju, konfiguracioni trag, rollout/rollback, on-call vlasnika i post-incident proveru da je data integrity obnovljen.

### S. Kontejner, Native, Kubernetes I Deployment

Pregledaj Dockerfile/buildpacks, base image, non-root user, filesystem permissions, exposed port, signal handling, image tag/digest, build reproducibility, layer cache, OS pakete i vulnerability scan. Za Kubernetes proveri request/limit, HPA, PDB, security context, service account/RBAC, NetworkPolicy, ingress/TLS, config/secret mount, probe timing, topology i rolling-update parametre. Za native/AOT proveri reflection/resources/proxy hints, JNI, agents, test pokrivenost i funkcionalne razlike od JVM artefakta.

### T. CI/CD, Release, Rollback I Recovery

Mapiraj CI trigger, privileged steps, secrets, artifact promotion, test gates, image scan, SBOM, signature/provenance, environment approval, migration owner i deployment strategiju. Release mora imati verzionisan artefakt, kompatibilnu konfiguraciju, canary/blue-green ili dokumentovan rolling postupak, health gate, monitoring prozor, rollback plan i data-recovery odluku. Rollback aplikacije nije automatski rollback baze; to mora biti eksplicitno testirano ili zabranjeno u release proceduri.

### U. Test Strategija I Dokaz Regresije

Inventarisi test piramidu i stvarne granice: unit, slice, Spring context, integration, Testcontainers, contract, security, migration, concurrency, E2E, load i chaos/failure testove. Testcontainers koristi za stvarne database/broker/search integracije kada je dostupno, uz izolovane test podatke i bez produkcionih endpointa. Proveri flaky/disabled/quarantined testove, test order, paralelizam, timezone/locale, random seed i cleanup. Svaka implementirana P0-P2 popravka zahteva test koji demonstrira staro neispravno i novo ispravno ponasanje.

### V. Popravke I Kontrolisana Implementacija

Pre izmene navedi nalaz, hipotezu, minimalnu izmenu, ugovor koji se cuva, rizik, test koji moze opovrgnuti pretpostavku i rollback. Menjaj najmanji skup fajlova; ne radi opportunistic refactor ili dependency upgrade van potrebnog opsega. Nakon svake znacajne izmene pokreni najuzi relevantan test/build korak, zatim agregiraj validaciju tek kada lokalna provera uspe.

### W. Production Readiness Provera

Pre presude proveri: podrzan runtime i dependency baseline; reproducibilan build; izolovane testove; bezbedan startup; auth/authz i tenant ownership; database invarijante i migracije; idempotency i messaging recovery; timeout/retry granice; tajne/Actuator/supply-chain; health/readiness/liveness; observability i alert/runbook; resource/limit/deployment; graceful shutdown; rollback/restore. Svaka stavka mora biti `POTVRDJENO`, `DELIMICNO_POTVRDJENO`, `NEPROVERENO` ili `NIJE_PRIMENJIVO` sa dokazom.

### X. Zavrsna Kontrola Kvaliteta Izvestaja

Pre isporuke proveri da su potvrdjeni nalazi reproduktivni, severity proporcionalan uticaju, predlozi izvedivi, implementirane izmene povezane sa testovima, neizvrsene provere jasno oznacene, komandni dnevnik potpun, tajne redigovane, a preostali rizik i vlasnistvo eksplicitni. Ne pretvaraj listu potencijalnih rizika u lazni dokaz izvrsenog audita.

