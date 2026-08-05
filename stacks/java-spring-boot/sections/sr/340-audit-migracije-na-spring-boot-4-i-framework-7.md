## Audit Migracije Na Spring Boot 4 I Framework 7

### Migration Baseline I Kompatibilnost

- Utvrdi tačnu matricu trenutnih Spring Boot, Spring Framework, Spring Security, Spring Data, Spring Cloud, Hibernate, Jackson, Jakarta, JDK, build-plugin i third-party starter verzija.
- Pre major migracije ažuriraj na poslednji podržani patch trenutne major linije i ukloni deprecation-e uz testove umesto prenošenja nepoznatog ponašanja.
- Proveri svaki starter, BOM, plugin, agent, test biblioteku, annotation procesor, servlet container, native biblioteku i platform service protiv ciljne linije.
- Razdvoji compile kompatibilnost, test kompatibilnost, runtime kompatibilnost, operativnu kompatibilnost, schema kompatibilnost, client kompatibilnost i rollback kompatibilnost.
- Održavaj migration finding register sa owner-om, blocker-om, workaround-om, trajnom popravkom, testom, rollout fazom i preostalim rizikom.

### Boot 4 Specifične Breaking Površine

- Audituj Jakarta EE 11 i Servlet 6.1 promene, uklonjene deprecated API-je, package i signature promene, podršku servlet container-a, filter-e, listener-e, multipart, async i error dispatch.
- Pregledaj modularizaciju starter-a i preimenovane ili podeljene zavisnosti; dokaži da resolved classpath sadrži nameravane capability-je i isključuje slučajne legacy module.
- Tretiraj usvajanje Jackson 3 kao contract migraciju koja obuhvata package-e, module, default-e, customization, testove, sačuvane payload-e, event-e, cache-eve i spoljne klijente.
- Proveri promene embedded server-a, uključujući uklanjanje ili zamenu nepodržanih servera, connector ponašanje, access logove, compression, TLS, HTTP/2 ili HTTP/3 i graceful shutdown.
- Pregledaj preimenovane/uklonjene property-je, Actuator promene, observability promene, test podršku, AOT/native ponašanje i registraciju custom auto-konfiguracije.

### Izvršenje Migracije I Rollback

- Izgradi dual-line test matricu za trenutnu i ciljnu verziju koristeći production-like konfiguraciju, podatke, zavisnosti, klijente, broker-e, baze i deployment topologiju.
- Pokreni contract, migration, security, concurrency, performance, startup, shutdown, memory, failover i rollback testove pre širokog rollout-a.
- Koristi staged promene koje razdvajaju framework upgrade, JDK upgrade, schema promenu, zamenu zavisnosti, serialization promenu i infrastructure promenu gde je praktično.
- Dokaži da stare i nove verzije mogu koegzistirati tokom potrebnog perioda ili eksplicitno projektuj prekid saobraćaja i data cutover sa recovery checkpoint-ima.
- Ukloni privremene compatibility flagove, dual write, adapter-e, suppression-e i stare zavisnosti uz owner-e i rokove posle potvrđene stabilizacije.


