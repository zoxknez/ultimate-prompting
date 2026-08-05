## JVM Performanse, AOT, Observability I Capacity

### JVM, GC, Memorija I Native Resursi

- Sačuvaj JVM vendor/build, način heap sizing-a, container awareness, GC, pause target-e, region podešavanja, direct memory, metaspace, code cache, thread stack-ove, native biblioteke i relevantne flagove.
- Meri allocation rate, live set, promotion, distribuciju pauza, ponašanje concurrent ciklusa, safepoint-e, class loading, code cache, direct buffer-e, file descriptor-e, socket-e i native memory.
- Istraži leak kroz heap histogram, dump, JFR, native memory tracking, allocation profile, reference chain, classloader retention, ThreadLocal retention i cache ownership.
- Testiraj memory limite, OOM varijante, heap-dump ponašanje, disk capacity, restart petlje, graceful degradation i da li se osetljivi podaci pojavljuju u dump-u ili dijagnostici.
- Ne podešavaj flagove pre utvrđenog workload-a, baseline-a, bottleneck-a, hipoteze, kontrolisanog eksperimenta i rollback kriterijuma.

### Latency, Throughput I Capacity

- Definiši workload modele po endpoint-u, poruci, job-u, tenant-u, payload-u, dataset-u, konkurentnosti, arrival pattern-u, ponašanju zavisnosti i cache stanju.
- Meri p50, p95, p99 i maksimalnu latency, throughput, greške, saturation, queue wait, pool wait, CPU, memoriju, GC, mrežu, disk i downstream pritisak.
- Pokreni cold-start, warm, burst, sustained, soak, failover, recovery, retry-storm, noisy-neighbor, large-payload i degraded-dependency testove.
- Odvoji server processing od queueing-a, mreže, proxy-ja, serializacije, baze, broker-a, cache-a i client vremena koristeći trace-ove i koordinisana merenja.
- Utvrdi bezbedan capacity, headroom, autoscaling signale, scale-up kašnjenje, scale-down bezbednost, admission pragove, load-shedding policy i operator akcije.

### AOT I Native Image

- Tretiraj JVM, CDS, layered JAR, executable JAR, WAR i GraalVM native image kao različite runtime proizvode sa odvojenim compatibility i performance dokazima.
- Proveri AOT processing, reachability metadata, reflection, resource-e, proxy-je, serializaciju, JNI, dynamic class loading, agente, locale-e, charset-e, TLS i service loading.
- Testiraj svaki podržani profil i optional integraciju u native režimu; uspešan minimalni native build ne dokazuje production feature pokrivenost.
- Uporedi startup, RSS, throughput, tail latency, build vreme, binary size, observability, debugging, patching i failure ponašanje sa JVM artefaktom.
- Sačuvaj testiranu rollback putanju između native i JVM artefakata kada operativna politika dozvoljava oba.

### Observability I Health Model

- Definiši release, environment, service, instance, tenant-safe, request, job, message, schema i dependency atribute dosledno kroz logove, metrike i trace-ove.
- Instrumentuj kritične poslovne tranzicije, queueing, retry, timeout, pool wait, transaction ishode, outbox lag, consumer lag, cache ponašanje i recovery akcije.
- Kontroliši metric cardinality, trace sampling, baggage, capture payload-a, stack trace i log volume; rediguj tajne i lične podatke pre export-a.
- Razdvoji liveness, readiness, startup, dependency, degradation, data freshness, backlog i business health; nijedan zeleni endpoint sam ne dokazuje ispravnost servisa.
- Poveži svaki actionable alert sa owner-om, severity-jem, SLO-om ili invarijantom, dashboard-om, evidence query-jem, runbook-om, eskalacijom i proverenom recovery akcijom.


