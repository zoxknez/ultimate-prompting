## Obavezne Matrice Dokaza I Failure Scenariji

### Obavezne Matrice Dokaza

- M1 - Source, JDK, build alat, dependency graph, generisani kod, artefakt, deployment i runtime identitet.
- M2 - Moduli, application context-i, efektivni bean-ovi, proxy-ji, condition-i, profili, configuration source-ovi i ownership tajni.
- M3 - Endpoint-i, protokoli, authentication, authorization, tenant pravila, validacija, idempotency, limiti i transaction granice.
- M4 - Executor-i, virtual thread-ovi, event loop-ovi, Reactor scheduler-i, queue-evi, context propagation, cancellation i shutdown ownership.
- M5 - Baze, entity-ji, query-ji, pool-ovi, transakcije, migracije, outbox/inbox, backup, restore, RPO i RTO.
- M6 - Broker-i, consumer-i, ordering, retry, dead letter-i, replay, schema kompatibilnost, backpressure i reconciliation.
- M7 - Cache-evi, lock-ovi, lease-ovi, fencing, autoritativni store-ovi, invalidacija, tenant dimenzije i outage ponašanje.
- M8 - Spoljni klijenti, destinacije, kredencijali, TLS, timeout-i, retry, circuit breaker-i, kvote i degraded mode-ovi.
- M9 - Osetljivi podaci, cryptographic materijal, retention, deletion, export, logovi, metrike, trace-ovi, dump-ovi i support pristup.
- M10 - JVM memorija, GC, native resursi, startup, latency, throughput, saturation, load shedding i capacity headroom.
- M11 - CI/CD identiteti, runner-i, plugin-i, cache-evi, artifact trust, SBOM, provenance, potpisi, promotion i revocation.
- M12 - Rollout, compatibility window, migracija, rollback, forward repair, incident kontrole, restore dokaz i owner-i.

### Obavezni Adversarial I Failure Scenariji

- S1 - Dva autorizovana aktera paralelno menjaju isti resurs koji nosi invarijantu.
- S2 - Ista komanda se replay-uje pre commit-a, posle commit-a pre odgovora, posle failover-a i posle deploy-a.
- S3 - Klijent prekida vezu ili cancel-uje dok database, broker, file, payment ili remote rad nastavlja.
- S4 - Thread pool, virtual-thread downstream limit, database pool, queue, heap, disk, file descriptor ili connection capacity se iscrpljuje.
- S5 - Zavisnost postaje spora, parcijalno odgovara, vraća malformed podatke, ima nevalidan sertifikat, stale DNS ili potpuni outage.
- S6 - Nested retry kroz gateway, servis, klijent, broker i consumer stvara amplifikaciju ili duple efekte.
- S7 - Proces pada pre commit-a, posle commit-a, pre acknowledgement-a, tokom publication-a i tokom shutdown-a.
- S8 - Stare i nove application verzije se preklapaju sa promenljivim database, event, cache, token, session i API schema-ma.
- S9 - Stale lock ili lease holder nastavlja rad nakon što je ownership prešao drugome.
- S10 - Broker redelivery, rebalance, dead-letter replay i event-i van redosleda dešavaju se zajedno.
- S11 - Korisnik menja object, parent, tenant, export, batch stavku, file putanju ili indirektni identifikator tuđim vrednostima.
- S12 - Authentication signing key-evi, TLS sertifikati, database kredencijali i application tajne rotiraju tokom saobraćaja.
- S13 - Configuration refresh ili feature-flag promena se primenjuje parcijalno kroz instance ili usred operacije.
- S14 - Migracija zastaje, parcijalno commit-uje, zaključava produkcione podatke, puni disk ili zahteva forward repair.
- S15 - Cache je stale, poisoned, evicted, nedostupan ili sadrži vrednosti iz nekompatibilnog release-a.
- S16 - Restore se izvršava izolovano i aplikacija mora dokazati podatke, schema-u, ključeve, fajlove, queue-eve, index-e i invarijante.
- S17 - Kompromitovana zavisnost, plugin, runner, signing key ili artefakt zahteva revocation i trusted rebuild.
- S18 - Rollback sledi posle parcijalnog rollout-a, nepovratnih side effect-a, promenjene schema-e i queued rada iz novije verzije.


