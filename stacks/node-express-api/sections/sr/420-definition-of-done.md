## Definition Of Done

1. Repozitorijum, dependency graph, generisani kod, artefakt, deployment, proces, schema i telemetry su korelisani.
2. Sve baseline komande i znacajna upozorenja imaju stvarne rezultate i exit code-ove.
3. Svaki nalaz sadrzi dokaz, root cause, uticaj, popravku, regression, rollout, rollback i residual risk.
4. P0 nalazi su contain-ovani i oporavljeni; P1 nalazi ne ostaju kao nedokumentovan release rizik.
5. Kriticne authorization, tenant, transaction, idempotency, replay, timeout, abort i shutdown putanje su testirane.
6. Efektivno Express ili Fastify ponasanje je provereno u ciljnom runtime-u, ne izvedeno samo iz source-a.
7. Event-loop, memory, pool, queue, provider i overload ponasanje ispunjava eksplicitne pragove.
8. Isti immutable artefakt se promovise i moze se identifikovati u pokrenutom procesu.
9. Rollout, abort, rollback ili forward repair, reconciliation i monitoring su izvrsivi i imaju owner-a.
10. Izolovani restore dokazuje podatke, kljuceve, schemu, tenant izolaciju, kriticne tokove, RPO i RTO.
11. Finalni izvestaj navodi READY, READY_WITH_CONDITIONS, NOT_READY ili INCIDENT i imenuje svaki blocker.
12. Nijedan rezultat, izvor, output komande, test success, verzija ili produkciono ponasanje nisu izmisljeni.

Ako bilo koja obavezna stavka nedostaje, navedi: **Sistem jos nije potpuno production-ready.**

