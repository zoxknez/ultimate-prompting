## Production Readiness checklist

- [ ] Source, PHP, SAPI, ekstenzije, zavisnosti, artifact, deployment, schema i pokrenuti proces su traceable identifikovani.
- [ ] Svaki podržani režim izvršavanja koristi odobren runtime, INI, set ekstenzija, konfiguraciju, lifecycle i test matricu.
- [ ] Composer lockfile, repository-ji, skripte, plugin-i, platform zahtevi, SBOM, potpisi i provenance su provereni.
- [ ] Framework rute, container-i, middleware, policy-ji, firewall-i, queue-ovi, scheduler-i, cache-evi i debug površine su dokazane iz produkcionog artifact-a.
- [ ] Autentikacija, account lifecycle, autorizacija, ownership, tenancy, administracija i break-glass putanje prolaze negativne testove.
- [ ] Kritične data invarijante, transaction granice, idempotency, outbox ili inbox i reconciliation su verifikovani pod konkurentnošću i crash-om.
- [ ] Queue, scheduler, cache, session, lock, storage, search i failure ponašanje spoljnog provider-a je ograničeno i recoverable.
- [ ] Dugovečni procesi resetuju request stanje, ograničavaju konkurentnost, bezbedno se drain-uju i potpuno zamenjuju tokom release-a.
- [ ] Injection, XSS, CSRF, SSRF, deserializacija, file parsing, traversal i resource-abuse kontrole prolaze exploit-oriented testove.
- [ ] Capacity, pool, FPM, OPcache, worker, dependency, timeout, queue i load-shedding limiti su izmereni i monitorisani.
- [ ] Logovi, trace-ovi, metrike, health, alert-i, runbook-ovi i privacy kontrole objašnjavaju kritične kvarove bez izlaganja osetljivih podataka.
- [ ] CI izoluje nepoverljiv kod, koristi scoped kredencijale, build-uje jednom, promoviše jedan immutable digest i podržava opoziv i trusted rebuild.
- [ ] Migracije i backfill-i podržavaju mixed verzije, ograničeno izvršavanje, pause, resume, verifikaciju, forward repair i recovery.
- [ ] Rollout, OPcache tranzicija, worker reload, rollback, forward repair, izolovani restore, RPO i RTO su izvršeni.
- [ ] Nema nerešenog P0, neprihvaćenog P1, isteklog waiver-a, nepoznate kritične putanje, nepodržane komponente ili nepoverljivog produkcionog stanja.

