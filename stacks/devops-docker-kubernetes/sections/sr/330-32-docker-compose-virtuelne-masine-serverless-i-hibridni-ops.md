## 32. Docker Compose, virtuelne masine, serverless i hibridni opseg

**Cilj:** Primeni ekvivalentnu produkcionu strogost van Kubernetes-a.

### 32.1 Obavezne provere

1. Za Compose proveri interpolaciju, profile, dependency semantiku, health, restart, resource limite, mreze, volume-e, tajne, konfiguraciju, logging, update proces i host pretpostavke.
2. Za virtuelne masine audituj image provenance, bootstrap, patching, configuration management, metadata pristup, host firewall, SSH ili remote administraciju, endpoint zastitu, disk encryption, backup, replacement i drift.
3. Za serverless audituj provenance paketa i layer-a, identitet, event source-ove, concurrency, cold start, retry, dead-letter ponasanje, idempotency, timeout-e, VPC pristup, tajne, logove, deployment verzije i rollback.
4. Za edge sisteme proveri ogranicenu konektivnost, sat, sertifikate, lokalno stanje, potpisivanje remote update-a, staged rollout, fizicki pristup, offline rad i recovery.
5. Za hibridne ili multi-cloud sisteme audituj identity federation, routing, DNS, transfer podataka, egress trosak, konzistentnost, observability, granice podrske, failover i korelisane zavisnosti.
6. Ne kopiraj Kubernetes kontrole mehanicki. Sacuvaj invarijantu uz prilagođavanje implementacije stvarnom runtime-u.
7. Testiraj startup, shutdown, replacement, update, rollback, gubitak host-a ili regiona, rotaciju tajni, backup, restore i incident izolaciju za svaki tip runtime-a.

### 32.2 Minimalni dokazi

- Runtime-specific inventar arhitekture, poverenja, vlasnistva i lifecycle-a.
- Mapiranje ekvivalentnih kontrola van Kubernetes-a.
- Dokaz update-a, otkaza, rollback-a i recovery-ja za svaki primenljiv runtime.

### 32.3 Kriterijumi izlaza

1. Ne-Kubernetes produkcione putanje ispunjavaju iste poslovne invarijante za identitet, integritet artefakta, izolaciju, observability i recovery.
2. Runtime-specific ogranicenja i deljeni failure domain-i su eksplicitni.
3. Update-i i recovery su testirani za svaki kritican tip runtime-a.

