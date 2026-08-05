## Faza 27 - Rollout, reload worker-a, OPcache tranzicija, rollback, forward repair i restore

### Cilj

Dokaži da release-i bezbedno i reverzibilno tranzicioniraju sve tipove procesa, cache-eve, kod, konfiguraciju, traffic i schema-u.

### Zahtevi audita

- Inventariši web, FPM, Octane, RoadRunner, Swoole, Messenger, Horizon, queue, scheduler, cron, CLI, migration, websocket i maintenance procese.
- Definiši release redosled za artifact, konfiguraciju, tajne, cache-eve, OPcache, web traffic, worker-e, scheduler-e, migracije i spoljne ugovore.
- Proveri graceful drain, zamenu worker-a, maksimalni lifetime, queue kompatibilnost, ponašanje in-flight zahteva, session continuity i postupanje sa konekcijama.
- Koristi canary ili staged rollout sa eksplicitnim cohort-om, metrikama, error budget-om, business guardrail-ima, observation window-om, abort kriterijumima i odgovornim owner-om.
- Razdvoji application rollback, configuration rollback, traffic rollback, worker rollback, schema rollback, forward repair i data reconciliation.
- Izvrši izolovani backup restore, point-in-time recovery, recovery zavisnosti, queue replay i restart servisa prema deklarisanim RPO i RTO.

### Obavezni dokazi

- Release state machine i matrica zamene procesa.
- Dokaz canary, mixed-version, drain, OPcache, worker reload, rollback i forward-repair postupka.
- Dokaz izolovanog restore-a sa izmerenim RPO, RTO, integritetom i reconciliation-om.

### Kriterijumi prihvatanja

- Nijedan neispratljiv stari kod, stale OPcache, stari worker, nekompatibilna poruka ili stale konfiguracija ne ostaje posle završetka release-a.
- Rollback i restore su izvršive testirane procedure, ne pretpostavke u dokumentaciji.

