## Faza P - Observability, Performance I CLR

Razdvoji liveness, readiness i degraded dependency. Liveness = da li proces zahteva restart; prolazni ispad zavisnosti obicno pripada readiness/degraded. Health ne sme otkrivati tajne ili internu topologiju; Host header restriction nije security granica.

Zahtevaj: structured logove, correlation/trace ID, route template, user/tenant bez nepotrebnog PII, status, latency, dependency latency, retries, job ID, deployment version, metrics, traces, error rate, latency percentiles, allocation/GC, thread-pool starvation, connection pool/cache/queue metrike. Instrumentisi OpenTelemetry gde je kompatibilno. Alerti: vlasnik, prag, trajanje, severity, runbook, dashboard, poslovni uticaj.

Performanse zasnuj na merenju. Izmeri blocking, sync-over-async, thread-pool starvation, CPU-heavy rad, veliki JSON/regex/compression/crypto/fajlove, streaming backpressure, LOH/GC, DB latency, connection pool. Izdvoji pravi CPU-bound rad u bounded worker. Microbenchmark nije dokaz end-to-end poboljsanja. Ne proglasavaj performance problem ili poboljsanje bez merenja.

