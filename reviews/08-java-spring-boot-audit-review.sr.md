# Revizija 08 - Java / Spring Boot / JVM Production Audit Prompt

Datum revizije: 5. avgust 2026.

## Rezime

Postojeci Java/Spring Boot par bio je kvalitetan i znatno detaljniji od pocetnih kratkih promptova, ali nije predstavljao potpuno uskladjen dvojezicni production audit ugovor.

Glavni problemi:

- EN i SR verzije nisu imale isti broj i dubinu naslova.
- Engleska verzija je faze D-X grupisala pod jednim zajednickim naslovom, dok ih je srpska verzija vodila kao zasebne sekcije.
- Nije postojao formalni E0-E5 model nivoa dokaza.
- Nije postojao kompletan source-to-runtime lanac identiteta.
- Build audit nije dovoljno tretirao Maven/Gradle plugin-e, generator-e, remote cache i executable supply-chain ulaze.
- Nisu bile dovoljno eksplicitne efektivne Spring bean, proxy, advice i filter-chain provere.
- Virtual threads, Reactor, context propagation i scheduler semantika nisu imali obaveznu ownership i saturation matricu.
- Transaction audit nije dovoljno precizno dokazivao proxy putanju, crash tacke, side effect-e van transakcije i ambiguous outcome recovery.
- Boot 4, Framework 7, Jakarta EE 11, Servlet 6.1, Jackson 3 i modularizovani starter-i nisu imali zaseban migration overlay.
- Nedostajale su standardizovane evidence matrice, obavezni failure scenariji i strogo pravilo produkcione odluke.

## Stanje Pre Revizije

| Metrika | EN | SR |
| --- | ---: | ---: |
| Linije | 395 | 399 |
| Markdown naslovi | 46 | 45 |
| Verzija | bez 2.0 frontmatter ugovora | bez 2.0 frontmatter ugovora |
| Strukturni paritet | neuspesan | neuspesan |

Konkretan uzrok paritet greske:

- EN je koristio `## Phases D-X - Required Deep Audit Procedure` i podnaslove nivoa `###`.
- SR je iste faze vodio kao vise zasebnih `##` naslova.
- Pojedine srpske faze imale su vise odvojenih pasusa tamo gde je engleska verzija imala jedan, pa line-shape nije bio isti.

## Stanje Posle Revizije

| Metrika | EN | SR |
| --- | ---: | ---: |
| Linije | 905 | 905 |
| Markdown naslovi | 112 | 112 |
| Verzija | 2.0.0 | 2.0.0 |
| Heading paritet | prosao | prosao |
| Line-shape paritet | 0 odstupanja | 0 odstupanja |

## Uveden Formalni Dokazni Model

Dodati su nivoi:

- E0 - tvrdnja, roadmap, ticket ili pretpostavka.
- E1 - staticki source, build, konfiguracioni, schema ili dependency dokaz.
- E2 - resolved graph, generated source, bytecode, artefakt, manifest, digest, potpis ili SBOM.
- E3 - izvrseni test, lokalni runtime, container, migration rehearsal ili integration dokaz.
- E4 - staging ili production-like load, rollout, failure ili rollback dokaz.
- E5 - produkcijsko posmatranje, izolovani restore, incident drill ili nezavisno reprodukovan dokaz.

Bezuslovni `READY` vise nije dozvoljen samo na osnovu source pregleda, unit testova, zelenog CI-ja ili liveness probe-a.

## Source-To-Runtime Identitet

Novi prompt zahteva korelaciju:

1. repozitorijuma, commit-a i dirty state-a;
2. JDK vendor-a, patch/build-a i arhitekture;
3. Maven/Gradle wrapper-a, build JVM-a, toolchain-a, profila i init konfiguracije;
4. resolved dependency graph-a, generatora, annotation procesora, native biblioteka i agenata;
5. bytecode target-a, JAR/WAR/native image digest-a, manifest-a, SBOM-a i potpisa/provenance-a;
6. deployment revizije, configuration i schema verzije;
7. stvarnog pokrenutog procesa i telemetry release atributa.

Source commit ili mutable image tag bez runtime korelacije vise nisu dovoljan dokaz.

## Build I Supply-Chain Unapredjenja

Dodato je:

- odvojeno dokazivanje JDK-a koji pokrece build, compilation toolchain-a, test JVM-a, native-image toolchain-a i produkcionog runtime-a;
- Maven effective POM, parent/BOM/plugin management, repository i extension audit;
- Gradle init script, composite build, buildSrc, convention plugin, version catalog, dependency verification i cache trust audit;
- provera generatora i izvrsnih build ulaza kao sto su Lombok, MapStruct, Querydsl, jOOQ, OpenAPI, protobuf, Avro, native compiler-i i custom shell komande;
- reproducibility provera iz cistog checkout-a;
- reachability-aware advisory analiza umesto slepog CVE prebrojavanja;
- SBOM i provenance kao pomocni dokaz, ne kao dokaz neeksploatabilnosti.

## Spring Runtime I Proxy Dokazi

Novi prompt zahteva:

- kompletan inventar application context-a i effective bean graph-a;
- `ConditionEvaluationReport` i poreklo svake bitne auto-konfiguracije;
- detekciju duplih transaction manager-a, client-a, scheduler-a, object mapper-a, pool-a i security chain-a;
- dokaz runtime proxy tipa i stvarne invocation putanje;
- test self-invocation, private/final metoda, final klasa, konstruktor/static poziva i non-managed objekata;
- advice ordering za security, validation, transaction, cache, retry, metrics i tracing;
- eksplicitno pravilo da annotation bez dokaza stvarnog prolaska kroz proxy ostaje `UNVERIFIED`.

## Konkurentnost, Virtual Threads I Reactor

Dodato je:

- ownership matrica za svaki executor, scheduler, event loop, queue, semaphore i rate limiter;
- bounded concurrency, rejection, cancellation, context propagation i shutdown ownership;
- virtual-thread pinning, ThreadLocal/MDC/SecurityContext i downstream limit provere;
- zabrana pretpostavke da virtual threads uklanjaju database, HTTP, memory ili rate ogranicenja;
- Reactor hot/cold source, scheduler boundary, backpressure, replay, retry, timeout i cancellation audit;
- provera da blocking/JDBC/filesystem/native rad ne zavrsi na Netty event loop-u;
- poseban audit `@Async`, `@Scheduled`, Quartz i Spring Batch overlap, restartability i duplicate prevention semantike;
- odvojeni fixed-delay, fixed-rate i cron testovi za virtual-thread scheduler-e.

## HTTP, API I Boundary Obrada

Dodati su:

- runtime endpoint inventar za MVC, WebFlux, functional routing, GraphQL, WebSocket, SSE, RSocket, gRPC, Actuator i webhook-e;
- autentikacija, authorization, tenant, timeout, idempotency, transaction i ownership matrica po endpoint-u;
- trusted proxy i forwarded-header dokaz;
- request smuggling, dupli header-i, path normalization i timeout-budget provere;
- Jackson 2/Jackson 3 kao odvojene compatibility povrsine;
- schema evolution old/new producer/consumer scenariji;
- eksplicitni parser, upload, archive, decompression i temporary-storage limiti;
- webhook signature, raw-body, replay, ordering i acknowledgement audit.

## Spring Security I Tenant Izolacija

Dodato je:

- efektivna `SecurityFilterChain` matrica sa matcher-ima, order-om i fallback pravilima;
- provera dispatcher, async, error i forwarded putanja;
- OAuth/OIDC/JWT/session/MFA/passkey i key-rotation scenariji;
- object-level authorization i BOLA/IDOR testovi;
- tenant constraint kroz query, cache, message, file, search, event, async task i admin tok;
- tenant context leakage testovi kroz thread reuse, Reactor, scheduler, retry, dead letter i telemetry;
- admin, support, impersonation i break-glass governance;
- CORS, CSRF, CSP, HSTS, host-header, redirect i clickjacking provere.

## Persistence, Transakcije I Recovery

Dodato je:

- entity identity, equality, ownership, cascade, fetch i serialization audit;
- N+1, Cartesian product, unbounded collection, lazy access i accidental flush provere;
- optimistic/pessimistic locking, write skew, lost update i deadlock testovi;
- stvarni SQL, query plan, cardinality i production-like data-volume dokaz;
- connection-pool capacity prema broju replika, virtual-thread konkurentnosti i database limitima;
- transaction manager, propagation, isolation, timeout, rollback rule i proxy-path matrica;
- crash tacke pre/tokom/posle commit-a;
- outbox/inbox atomarnost, replay, CDC/polling ownership i reconciliation;
- saga state machine, compensation i manuelni recovery;
- expand-and-contract migracije, mixed-version testovi i kontrolisani forward repair;
- izolovani restore i point-in-time recovery sa proverom podataka, schema-e, kljuceva, queue-eva, index-a, RPO i RTO.

## Messaging, Cache I Integracije

Dodato je:

- delivery, ordering, acknowledgement, retry, DLQ, poison message, retention i replay pravilo za svaki broker tok;
- crash-before/after-commit, acknowledgement loss, rebalance i retry-storm scenariji;
- cache key tenant/authorization dimenzije, schema, TTL, invalidacija i outage ponasanje;
- distributed lock i lease fencing zahtevi;
- outbound client connect/request/read/write/total/pool timeout budget;
- nested retry prevention i bounded resilience policy;
- DNS, certificate, credential, redirect, SSRF, malformed response i dependency brownout testovi;
- object storage, email, search i payment idempotency/reconciliation zahtevi.

## JVM, AOT, Performance I Observability

Dodato je:

- JVM vendor/build, heap, GC, metaspace, direct memory, code cache, stack i native resource inventar;
- allocation, live set, safepoint, classloader, native memory i leak analiza;
- OOM i heap-dump security/recovery testovi;
- p50/p95/p99, queue wait, pool wait, GC, disk, network i downstream pressure merenje;
- cold, burst, sustained, soak, failover, noisy-neighbor i degraded-dependency testovi;
- JVM, CDS, layered JAR, WAR i native image kao odvojeni runtime proizvodi;
- AOT reachability, reflection, resource, proxy, JNI i dynamic loading testovi;
- liveness, readiness, startup, dependency, data freshness, backlog i business health kao odvojeni modeli;
- alert-owner-runbook-recovery veza.

## CI/CD, Release I Incident Response

Dodato je:

- immutable artifact promotion bez rebuild-a izmedju okruzenja;
- repository/runner/fork/OIDC/cache/plugin/deployment trust granice;
- pinovanje action-a, image-a, plugin-a i alata;
- odvajanje untrusted PR izvravanja od release i production tajni;
- canary, guardrail, abort i rollback autoritet;
- old/new application, schema, event, cache, token i session compatibility;
- razdvajanje application rollback-a, configuration rollback-a, traffic shift-a, schema forward repair-a i data reconciliation-a;
- incident kill switch, credential/key revocation, consumer/job pause, write freeze i trusted rebuild;
- post-recovery verifikacija poslovnih invarijanti i tenant izolacije.

## Spring Boot 4 Migration Overlay

Posebno su dodati:

- obaveza da stari projekat prvo dodje do poslednjeg podrzanog Boot 3.5.x patch-a;
- Jakarta EE 11 i Servlet 6.1 compatibility;
- uklonjeni deprecated API-ji;
- modularizovani i promenjeni starter-i;
- Jackson 3 contract migracija;
- embedded server i container promena;
- property, Actuator, observability, test, AOT i custom auto-configuration provera;
- dual-line test matrica i staged upgrade koji razdvaja framework, JDK, schema, serialization i infrastructure promene.

## Obavezne Matrice I Scenariji

Dodato je 12 evidence matrica i 18 obaveznih adversarial/failure scenarija.

Scenariji obuhvataju:

- paralelne promene iste invarijante;
- replay komande oko commit-a i failover-a;
- client disconnect uz nastavak side effect-a;
- iscrpljenje thread, connection, database, heap, disk i file-descriptor kapaciteta;
- dependency brownout i outage;
- nested retry amplifikaciju;
- crash u vise transaction/broker/shutdown tacaka;
- old/new version overlap;
- stale lease holder;
- broker replay i event-e van redosleda;
- BOLA/IDOR i cross-tenant pokusaje;
- rotaciju kljuceva, sertifikata i tajni;
- parcijalni config refresh;
- parcijalnu migraciju i forward repair;
- stale ili nekompatibilan cache;
- izolovani restore;
- supply-chain revocation i trusted rebuild;
- rollback posle parcijalnog rollout-a i nepovratnih efekata.

## Aktuelni Baseline

Baseline je azuriran primarnim izvorima:

- JDK 26 GA i Java 25 LTS status;
- Spring Boot 4.1.0 system requirements;
- Spring Boot 4 migration guide;
- Spring support policy;
- Spring task execution/scheduling i virtual-thread smernice;
- Apache Maven 3.9.16 stable i preview status Maven 3.10/4;
- Gradle 9.6.1 i Java compatibility matrica;
- aktuelna Spring Security projektna linija.

Manifest: `baselines/sources.json`.

## Validacija

- EN linije: 905
- SR linije: 905
- EN naslovi: 112
- SR naslovi: 112
- heading paritet: prosao
- line-shape paritet: 0 odstupanja
- YAML frontmatter: validan
- JSON baseline manifest: validan
- Markdown code fence blokovi: balansirani
- baseline hardcode scan: prosao
- en dash, em dash i non-breaking hyphen u SR promptu: 0
- repository parity checker sada prijavljuje samo jos neobradjeni Python/PySide6 par

## Zakljucak

Java/Spring Boot prompt je sada samostalan, dvojezicno uskladjen i dokazno orijentisan production audit ugovor. Ne zavrsava se na compile/test nivou, vec zahteva dokaz stvarnog runtime identiteta, proxy i authorization putanja, transakcione i konkurentne ispravnosti, rollout kompatibilnosti, rollback-a, restore-a i incident oporavka.
