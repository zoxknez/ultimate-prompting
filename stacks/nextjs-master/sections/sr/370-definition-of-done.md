## Definition of Done

1. Repozitorijum, graph, generisani izlaz, artefakt, deployment, runtime, schema, cache, browser i recovery putanja su auditirani.
2. Lifecycle i security baseline-i su ponovo provereni iz primarnih izvora i izabrane verzije su opravdane.
3. Komande, okruzenja, exit code-ovi, upozorenja, blokirane provere i nivoi dokaza su zabelezeni.
4. Svaki nalaz ima dokaz, uzrok, impact, popravku, regresiju, rollout, recovery i residual risk.
5. Nijedan privatni podatak, tajna, tenant context ili privilegovana operacija ne prelazi neproverenu granicu.
6. Kriticne invarijante su autoritativne i testirane pod concurrency-jem, duplim delivery-jem, timeout-om, crash-om i retry-jem.
7. Kriticni tokovi prolaze artifact, browser, accessibility, performance, security i failure testove.
8. Migration, compatibility, canary, abort, rollback, repair, restore, RPO i RTO su demonstrirani.
9. Observability identifikuje release, rutu, runtime, actor klasu, tenant-safe context, ishod i recovery bez leakage-a.
10. P0 ne postoji ili je pod incident command-om; P1 je popravljen ili blokira release uz eksplicitno odobrenje.
11. Dokumentacija, runbook-ovi, owner mape, matrice i finalni izvestaj odgovaraju implementiranoj i deploy-ovanoj stvarnosti.
12. Odluka je READY, READY_WITH_CONDITIONS, NOT_READY ili INCIDENT sa eksplicitnim obrazlozenjem.

