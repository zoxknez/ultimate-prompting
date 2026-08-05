## Zajednički audit protokola, podataka i distribuirane ispravnosti

### Matrica mrežnog protokola i API ugovora

- Popiši listener-e, klijente, transport, metode, rute, RPC servise, streaming režime, autentikaciju, autorizaciju, tenant ownership, limite payload-a, deadline-ove, idempotency, retry, granicu transakcije, kompatibilnost i testove.
- Proveri HTTP parsing, zaštitu od request smuggling-a, proxy trust, forwarded header-e, TLS terminaciju, HTTP/2 i HTTP/3 podešavanja, limite dekompresije, multipart obradu, redirect-e i ponovnu upotrebu konekcija.
- Za gRPC i protobuf proveri evoluciju polja, unknown fields, oneof promene, rast enum-a, deadline-ove, mapiranje statusa, interceptor-e, reflection, health, streaming backpressure i kompatibilnost starih i novih klijenata.
- Za TCP, UDP, QUIC, framed, binarne ili custom protokole proveri framing, validaciju dužine, incremental parsing, timeout-e, peer identitet, replay, amplification, fragmentaciju, state-machine prelaze i fuzz pokrivenost.
- Primeni limite request-a, response-a, header-a, metadata-e, stream-a, fajla, poruke i dekompresovane veličine pre skupe alokacije ili parsiranja.

### Transakcije, idempotency i evolucija šeme

- Mapiraj svaki tok promene stanja od validacije kroz autorizaciju, čitanja, lock-ove, upise, side effect-e, commit, odgovor, retry, objavu događaja i reconciliation.
- Proveri database constraint-e, izolaciju, redosled lock-ova, optimistic token-e, serialization failure-e, deadlock retry, stanje konekcije, ownership transakcije, savepoint-e, cancellation i rollback ponašanje.
- Koristi idempotency ključeve sa trajnim ownership-om, request fingerprinting-om, čuvanjem rezultata, conflict semantikom, expiry-jem, replay odgovorom, kontrolom konkurentnosti i multi-replica ponašanjem.
- Audituj outbox, inbox, CDC, saga, compensation, deduplication, ordering, partition ownership, poison poruke, DLQ replay i delimičan failure između baze i broker-a.
- Proveri expand-and-contract migracije, koegzistenciju starog i novog binarnog fajla, idempotency backfill-a, ponašanje online index-a ili constraint-a, trajanje lock-a, cutover, rollback limite, forward repair i restore kompatibilnost.

### Ispravnost keša, reda i koordinacije

- Dokumentuj namespace cache ključa, tenant scope, authorization osetljivost, verziju serializacije, TTL, invalidaciju, stampede zaštitu, negative caching, stale politiku, eviction i ponašanje pri prekidu.
- Tretiraj distribuirane lock-ove i lease-eve kao nepouzdanu koordinaciju; proveri fencing token-e, pretpostavke o satu, renewal, gubitak ownership-a, split brain, ponašanje zastarelog holder-a i oporavak.
- Za redove i stream-ove proveri delivery semantiku, vreme ack-a, visibility timeout, rebalance, ordering, delimičan failure batch-a, retry budžet, poison obradu, retention, replay i consumer idempotency.
- Testiraj broker prekid, cache prekid, odložene ili duplirane poruke, promenjen redosled događaja, restart consumer-a, pomeranje particije, gubitak lease-a i database/broker recovery skew.

### Kontrola overload-a, retry-ja, deadline-a i delimičnog failure-a

- Izvedi limite konkurentnosti, reda, pool-a i rate-a iz downstream kapaciteta, latency budžeta, memorije, CPU-a, file descriptor-a, database limita i recovery ciljeva.
- Propagiraj deadline od početka do kraja i rezerviši vreme za cleanup, završetak transakcije, response serializaciju, retry i fallback; izbegavaj nezavisno povećavanje timeout-a na svakom hop-u.
- Klasifikuj operacije po idempotency-ju i retry mogućnosti; ograniči pokušaje i ukupno vreme, koristi jitter, poštuj server signale, spreči umnožavanje retry-ja i izloži retry budget metrike.
- Proveri admission control, load shedding, circuit ponašanje, bulkhead-e, ograničene redove, pravično raspoređivanje, tenant izolaciju, hot-key obradu, fan-out limite i režime degradacije.
- Pokreni burst, sustained load, soak, dependency slowdown, dependency outage, connection churn, cancellation storm, retry storm i recovery testove sa eksplicitnim pass/fail pragovima.

