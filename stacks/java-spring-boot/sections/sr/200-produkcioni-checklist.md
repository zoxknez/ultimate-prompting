## Produkcioni Checklist

Pre finalne presude eksplicitno popuni sledeci checklist dokazima, a ne sa pretpostavkama:

1. Podrzani Java, Spring Boot, Spring Framework, build alat i produkcioni image baseline.
2. Reproducibilan wrapper build, zakljucane/proverene zavisnosti i poznat dependency izvor.
3. Bezbedan profile/config startup i odsustvo produkcionih side effecta u testu.
4. Jasno razdvojeni javni, interni i management endpointi.
5. Dokazani authentication, authorization, ownership i tenant scope za kriticne operacije.
6. DTO, granicna, semanticka i file/message validacija za nepoverljive ulaze.
7. Database constraint, transakcija, locking i concurrency model za svaku kriticnu invarijantu.
8. Idempotency i crash/replay oporavak za write, webhook, job i message tokove.
9. Bezbedne, rollout-kompatibilne, merene i recoverable migracije.
10. Bounded timeout, retry, pool, queue i resource limiti za lokalne i spoljne tokove.
11. Ograniceni upload/download/SSRF i provereni outbound access.
12. Zasticeni Actuator, tajne, TLS/cookies/CSRF/CORS i supply-chain kontrole.
13. Liveness, readiness, degraded zavisnosti, structured logovi, metrike, tracing, alerti i runbook.
14. Izmeren ili eksplicitno ogranicen capacity/performance rizik.
15. Container/Kubernetes/native deployment provera gde je primenljivo.
16. Dokazan graceful shutdown, deployment, rollback aplikacije i recovery podataka.

