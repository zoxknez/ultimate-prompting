## 20. GitOps, progresivna isporuka i promocija okruzenja

**Cilj:** Kontrolisi reconciliation, promociju, rollout rizik i hitne izmene.

### 20.1 Obavezne provere

1. Proveri vlasnistvo GitOps repozitorijuma, branch protection, review pravila, potpisivanje, path dozvole, razdvajanje okruzenja, identitet kontrolera i pristup tajnama.
2. Audituj source definicije, generator ponasanje, sync wave-ove, hook-ove, health check-ove, pruning, self-heal, retry, timeout-e, izuzetke, ignore pravila i multi-tenancy granice.
3. Obezbedi da produkciona promocija zahteva review-ovane dokaze i cuva immutable identitet artefakta.
4. Proveri da canary, blue-green, rolling, feature-flag, shadow ili traffic-splitting analiza koristi smislene metrike, minimalni uzorak, guardrail-e, abort uslove i rollback.
5. Testiraj outage kontrolera, outage source-a, zastareli cache, nevalidan desired state, partial sync, neuspesan hook, zaglavljen finalizer i hitnu pauzu.
6. Definisi putanju hitne izmene koja cuva dokaze, odobrenje, pripisivost, reconciliation i vremenski ograniceno ciscenje.
7. Obezbedi da preview okruzenja ne mogu pristupiti produkcionim podacima, kredencijalima, mrezama, billing ovlascenju ili deljenim mutabilnim resursima bez eksplicitnih kontrola.

### 20.2 Minimalni dokazi

- GitOps model poverenja i dozvola.
- Dokaz promocije i progresivne isporuke za reprezentativan release.
- Vezba otkaza kontrolera i usklađivanja hitne izmene.

### 20.3 Kriterijumi izlaza

1. Samo odobreni immutable artefakti mogu stici u produkciju kroz pripisive promotion putanje.
2. Rollout analiza detektuje smislene regresije i bezbedno prekida.
3. Hitne izmene su vidljive, reverzibilne, usklađene i ne mogu postati trajna shadow konfiguracija.

