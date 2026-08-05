## 8. Health, Observabilnost, Performanse I Testovi

Razdvoji liveness, readiness i degraded-dependency stanje. Ne stavljaj zajednicke spoljne zavisnosti u liveness probe, jer restart loop moze izazvati cascading failure. Namerno odluci da li spoljna zavisnost pripada readinessu. Za Kubernetes pregledaj Actuator probe grupe i osiguraj da probe koriste odgovarajucu main-server putanju kada poseban management port moze maskirati kvar aplikacije.

Zahtevaj strukturisane logove, correlation/trace ID-jeve, route template, user/tenant ID-jeve bez nepotrebnog PII, status, latenciju, latenciju zavisnosti, retry-jeve, job ID, deployment verziju, metrike, traceove, error rate, latency percentile, JVM heap/GC, thread-pool/executor zasicenje, blokirane threadove, connection-pool/cache/queue metrike i dependency telemetriju. Instrumentisi Micrometer/OpenTelemetry gde je prikladno. Alerti zahtevaju vlasnika, prag, trajanje, ozbiljnost, runbook, dashboard i uticaj na korisnika/posao.

Izmeri blocking pozive, thread starvation, executor sizing/queueing, CPU-intenzivan rad, veliki JSON/regex/compression/crypto/fajlove, reactive scheduler misuse, memory/GC, connection-pool zasicenje, database latenciju, cache ponasanje i load ponasanje. Izdvoji pravi CPU-bound rad u bounded workere ili servise umesto da gladujes request threadove ili event loopove.

Pokreni/dodaj unit testove za cistu logiku; integration testove za controllere, filtere, bazu i Spring context; contract testove za HTTP/gRPC; concurrency testove za invarijante; security testove za authentication/authorization, SSRF, CORS/CSRF, Actuator exposure, upload i webhook replay; end-to-end testove kriticnih tokova; i load testove skupih endpointa. Svaka pronadjena regresija mora dobiti fokusiran test koji bi pao pre popravke.

