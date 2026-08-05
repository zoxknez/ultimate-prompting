## 30. FinOps, kvote i cost resilience

**Cilj:** Kontrolisi trosak bez slabljenja pouzdanosti, bezbednosti ili oporavka.

### 30.1 Obavezne provere

1. Pripisi trosak nalogu, okruzenju, servisu, vlasniku, tenant-u, workload-u, regionu, tipu resursa i poslovnom ishodu gde je moguce.
2. Audituj budzete, forecast-e, anomaly detection, commitment-e, reservation-e, savings plan-ove, spot ili preemptible upotrebu, egress, podrsku, licence, rast storage-a, logove, metrike i backup trosak.
3. Identifikuj idle, oversized, orphan, duplirane, over-retained, cross-region, over-replicated i slabo iskoriscene resurse uz poslovni i recovery kontekst.
4. Proveri kvote, service limite, budget akcije, billing dozvole, integritet cost export-a i isporuku alarma pre iscrpljivanja ili nekontrolisanog troska.
5. Modeluj normalan, peak, failover, incident, restore, scale-out, data growth i observability trosak.
6. Ne uklanjaj redundansu, retention, logging, encryption, podrsku, headroom ili rollback kapacitet bez eksplicitnog prihvatanja rizika.
7. Definisi unit economics i cost guardrail-e koji ne stvaraju availability ili data-loss litice.

### 30.2 Minimalni dokazi

- Izvestaj cost alokacije, trenda, anomalija i vlasnistva.
- Savings backlog sa uticajem na pouzdanost i recovery.
- Dokaz testova kvote, budzeta i failover troska.

### 30.3 Kriterijumi izlaza

1. Kritican trosak je pripisiv i materijalne anomalije alarmiraju odgovorne vlasnike.
2. Preporuke ustede cuvaju prihvacene SLO, RPO, RTO, bezbednost i rollback.
3. Iscrpljivanje kvote i troska ne moze izazvati neprimecen nagli outage.

