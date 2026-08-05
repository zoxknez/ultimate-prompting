## 27. Observability, SLO, alarmi i on-call

**Cilj:** Ucini korisnicki uticaj i sistemski otkaz detektabilnim, dijagnostikovanim i akcionim.

### 27.1 Obavezne provere

1. Definisi granice servisa, korisnicke tokove, SLI, SLO, error budget-e, reporting prozore, izuzetke, vlasnike i posledice trosenja budget-a.
2. Proveri da metrike, logovi, trace-ovi, event-i, profili, audit logovi, deployment metadata i poslovni signali dele stabilne service, environment, version, tenant-safe i korelacione atribute.
3. Audituj kardinalnost, sampling, agregaciju, histogram bucket-e, sinhronizaciju sata, buffering, gubitak, backpressure, retention, encryption, pristup, redigovanje i trosak.
4. Spreci tajne, kredencijale, authorization header-e, tokene, licne podatke, korisnicke payload-e i visokorizicne identifikatore u telemetriji.
5. Dizajniraj paging alarme oko korisnickog uticaja, SLO burn-a, integriteta podataka, security event-a i hitnih capacity rizika. Razdvoji page, ticket, dashboard i informativne signale.
6. Za svaki page proveri threshold, trajanje, grouping, deduplikaciju, inhibition, vlasnistvo, runbook, dashboard, silence policy, escalation i dokaz resenja.
7. Testiraj otkaz telemetry pipeline-a, nedostajuce podatke, kasne podatke, isporuku alarma, on-call routing, istek integracije i regionalni gubitak observability-ja.
8. Pregledaj skorasnje incidente i page-ove za vreme detekcije, potvrde, dijagnoze, mitigacije, resenja, false positive-e, toil i nedostajuce signale.

### 27.2 Minimalni dokazi

- SLO i error-budget definicije vezane za korisnicke tokove.
- Procena pokrivenosti, privatnosti, gubitka, retention-a i troska telemetrije.
- Rezultati testa okidanja, isporuke, routing-a, runbook-a i resenja alarma.

### 27.3 Kriterijumi izlaza

1. Kritican korisnicki uticaj i security uslovi proizvode blagovremene akcione signale.
2. Telemetrija je korisna, zasticena, troskovno prihvatljiva i dovoljno otporna za incident response.
3. On-call vlasnistvo, escalation, runbook-ovi i kvalitet alarma su potvrđeni kroz stvarne ili kontrolisane event-e.

