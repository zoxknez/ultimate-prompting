## 37. Production Readiness Definition of Done

1. Opseg, autorizacija, vlasnici, kriticnost, okruzenja, identiteti, data flow-ovi, zavisnosti, SLO, RPO i RTO su eksplicitni.
2. Kriticni produkcioni artefakti su ispraceni do review-ovanog izvora, zasticenih build-ova, immutable digest-a, potvrđenog provenance-a, potpisa, policy-ja i promocije.
3. Desired state, GitOps stanje, live cluster stanje, cloud stanje i korisnicki uoceno ponasanje su usklađeni ili dokumentovani kao prihvacen drift.
4. Container, runtime, host, cluster, workload, identity, network, secret, storage, CI/CD i supply-chain kontrole su potvrđene prema realnim abuse i failure putanjama.
5. Kriticni workload-i ispunjavaju izmerene zahteve performansi, kapaciteta, scaling-a, dostupnosti, ispravnosti podataka i graceful degradation-a.
6. SLO, telemetrija, alarmi, on-call routing, runbook-ovi, incident uloge i escalation su testirani i akcioni.
7. Backup-i su zasticeni i reprezentativni kriticni restore, failover i failback ispunjavaju prihvacene ciljeve sa dokazom integriteta.
8. Nijedan nerazresen P0 ili neprihvatljiv P1 nalaz nije ostao. Svaki prihvacen rizik ima odgovornog vlasnika, obrazlozenje, rok ili datum pregleda i compensating kontrole.
9. Svaka implementirana izmena ima fokusirane testove, odobrenje, rollout dokaz, posmatranje, rollback dokaz, dokumentaciju i vlasnistvo.
10. Rizici verzija, podrske, deprecation-a, upgrade-a, ranjivosti, troska, kvote i zavisnosti imaju vremenski ogranicene planove.
11. Zavrsni verdict je podrzan nivoom dokaza i ne preuvelicava nedostupno produkciono ponasanje.

