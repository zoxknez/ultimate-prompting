## 31. Platform engineering, developer experience i governance

**Cilj:** Smanji kognitivno opterecenje uz cuvanje bezbednog vlasnistva i escape hatch-eva.

### 31.1 Obavezne provere

1. Mapiraj platform proizvode, paved road-ove, template-e, kataloge, portale, API-je, golden path-eve, self-service akcije, dokumentaciju, podrsku i vlasnistvo.
2. Izmeri onboarding, prvi deployment, rollback, pristup tajni, preview okruzenje, debugging, incident handoff, upgrade i decommission workflow-e.
3. Obezbedi da template-i kodiraju bezbedne default vrednosti bez skrivanja kriticnog ponasanja, zakljucavanja timova na zastarele verzije ili davanja nepotrebnih privilegija.
4. Proveri vlasnistvo, support tier-e, deprecation policy, versioning, migration vodiče, telemetriju, feedback loop, usvajanje, zadovoljstvo i product SLO-e.
5. Definisi kontrolisane escape hatch-eve sa odobrenjem, vidljivoscu, rokom, compensating kontrolama i putanjom nazad na paved road.
6. Audituj tenancy, vending namespace-a ili naloga, kvote, mrezu, identitet, tajne, billing i deletion granice u self-service workflow-ima.
7. Ukloni toil automatizacijom tek kada su osnovna invarijanta, failure ponasanje, vlasnistvo i rollback razumljivi.

### 31.2 Minimalni dokazi

- Mapa platform proizvoda i vlasnistva.
- Izmereni rezultati developer toka i failure putanje.
- Procena template-a, self-service-a, izuzetaka i deprecation-a.

### 31.3 Kriterijumi izlaza

1. Kriticni developer workflow-i su bezbedni, razumljivi, dokumentovani, merljivi i podrzani.
2. Self-service ne moze tiho preci tenant, identity, network, cost ili deletion granice.
3. Izuzeci i deprecated putanje su vidljivi i aktivno konvergiraju.

