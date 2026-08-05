## 34. Obavezna test matrica

Pokreni samo testove koji su autorizovani i bezbedni za cilj. Za svaki red zabelezi `PASS`, `FAIL`, `BLOCKED` ili `NOT_APPLICABLE` sa dokazom.

| Domen | Minimalni testovi |
| --- | --- |
| Repozitorijum i konfiguracija | Cist render, sintaksa, sema, lint, secret scan, dependency lock, deterministicko generisanje, diff. |
| Container build | Multi-stage, non-root, layer-i bez tajni, reproduktivnost, potrebne arhitekture, SBOM, provenance, potpis, runtime smoke. |
| Pipeline | Trusted i untrusted putanje, fork, OIDC, dozvole, pinning, izolacija runner-a, injection, zamena artefakta, cancellation, retry. |
| Supply chain | SBOM pokrivenost, provenance verifikacija, identitet potpisa, admission odbijanje, vulnerability trijaza, opoziv i rebuild. |
| Kubernetes temelj | Version skew, uklonjeni API-ji, control-plane pristup, zamena noda, drain, pretpostavka zone, recovery dodataka. |
| Workload-i | Startup, readiness, liveness, shutdown, rollout, rollback, OOM, disk pressure, job retry, dupla isporuka, propusteni schedule. |
| Bezbednost i identitet | PSS ili ekvivalent, admission bypass, efektivni RBAC, workload identity, odbijen pristup, break-glass, opoziv, rotacija tajne. |
| Mreza i TLS | Default deny, potrebni tokovi, DNS otkaz, obnova i istek sertifikata, konflikt ruta, timeout, retry amplifikacija, egress. |
| Stanje i podaci | Migracija, konzistentnost, idempotency, pun disk, attachment otkaz, replica lag, korupcija, failover, zastita od brisanja. |
| Performanse i kapacitet | Baseline, peak, burst, soak, cold start, scaling, saturacija, failover, recovery, kvota i trosak. |
| Observability i incident | Gubitak telemetrije, okidanje i isporuka alarma, routing, runbook, kompromitovan artefakt, opoziv kredencijala, cuvanje dokaza. |
| Backup i DR | Izolovani restore, integritet, point in time, nedostajuci kljuc, ostecen backup, gubitak regiona, failover, failback, izmeren RPO i RTO. |

### 34.1 Pravila pokrivenosti

1. Testiraj stvarni produkcioni artefakt ili artefakt dokazano identican po digest-u, konfiguraciji i deployment ulazima.
2. Koristi release-like optimization, security, identity, network, storage i policy podesavanja.
3. Pokrij najmanje jedan kritican sinhroni tok, jednu asinhronu ili scheduled putanju, jednu administrativnu putanju i jednu recovery putanju gde je primenljivo.
4. Ukljuci negativne i failure slucajeve. Samo happy-path testovi nisu dovoljni.
5. Ne pokreci destruktivne produkcione eksperimente bez eksplicitne autorizacije, aktuelnih backup-a, ogranicenog blast radius-a i rollback-a.
6. Ponovi neuspesne ili korigovane testove i sacuvaj before-and-after dokaze.

