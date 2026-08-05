## Faza AI - Release, Mixed-Version Rollout I Rollback

- Definisi canary cohort, trajanje, guardrail-e, error-budget uticaj, abort pragove i vlasnika odluke.
- Testiraj stari web sa novom schema-om, novi web sa old-compatible schema-om, stare jobove sa novim argumentima, nove jobove sa starim queued payload-ima i stare asset-e sa novim serverom.
- Odvoji application, configuration, traffic, job, cache, data i schema rollback procedure.
- Koristi forward repair kada destruktivne data ili schema izmene cine binary rollback nebezbednim.
- Proveri queue pause, write freeze, feature kill switch, cache invalidaciju i session-key ponasanje tokom rollback-a.
- Zabelezi tacne release i rollback komande i izvrsi kontrolisanu probu pre kriticnog launch-a.

