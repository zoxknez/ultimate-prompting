## Faza 21 - PHP-FPM, OPcache, JIT, kapacitet i iscrpljivanje resursa

### Cilj

Izmeri i ograniči procesni, pool, cache, CPU, memory, connection i downstream kapacitet pod realnim i zlonamernim load-om.

### Zahtevi audita

- Inventariši FPM pool-ove, process manager režim, child limite, spare podešavanja, request limite, timeout-e, slow logove, termination ponašanje i status izlaganje.
- Proveri OPcache memory, interned strings, validation, preload, file cache, huge pages, deployment invalidaciju, stale code rizik i emergency reset.
- Tretiraj JIT kao izmeren workload-specific izbor; uporedi correctness, startup, CPU, memory, latency i observability sa i bez njega.
- Izmeri application memory, peak request memory, leak-like rast, fragmentaciju, recycle worker-a, queue memory, veličinu serializacije i ponašanje velikih response-a.
- Modeluj FPM, queue, web server, database, Redis, HTTP klijent i provider pool veličine zajedno radi sprečavanja multiplikativnog overload-a.
- Pokreni cold, burst, sustained, soak, failover, dependency-slowdown, large-payload, expensive-query i malicious-input testove.

### Obavezni dokazi

- Capacity model sa arrival rate-om, konkurentnošću, service time-om, queue depth-om, pool limitima, memorijom i headroom-om.
- Merenja FPM-a, OPcache-a, JIT-a, dugovečnih worker-a i saturation-a zavisnosti.
- Dokaz load, burst, soak, failover, overload i recovery testova.

### Kriterijumi prihvatanja

- Resource limiti, queue-ovi, timeout-i i load shedding otkazuju predvidljivo pre kolapsa hosta ili zavisnosti.
- Deployment i OPcache tranzicije ne mogu da služe neispratljivu mešavinu starog koda, novog koda i stale konfiguracije.

