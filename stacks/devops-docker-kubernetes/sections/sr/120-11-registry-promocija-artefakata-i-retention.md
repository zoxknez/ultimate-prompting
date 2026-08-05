## 11. Registry, promocija artefakata i retention

**Cilj:** Zastiti identitet, dostupnost, poverljivost i zivotni ciklus artefakta.

### 11.1 Obavezne provere

1. Popisi registre, repozitorijume, replikaciju, geo poziciju, pristupne putanje, javnu vidljivost, retention, immutability, zastitu od brisanja i vlasnike.
2. Koristi immutable digest-e za deployment i tretiraj tagove samo kao reference pogodne ljudima osim ako je immutability nametnut.
3. Odvojeno proveri push, pull, delete, replication, quarantine, promotion i emergency access dozvole.
4. Zahtevaj potvrđene potpise, provenance, policy rezultate i odobrene promotion dokaze pre produkcione podobnosti.
5. Testiraj registry outage, rate limite, nedostupan digest, obrisan rollback artefakt, replication lag i reakciju na kompromitovan artefakt.
6. Uskladi retention sa rollback horizontom, potrebama istrage, pravnim zahtevima, storage troskom i vulnerability response-om.

### 11.2 Minimalni dokazi

- Matrica registry dozvola i vidljivosti.
- Promotion dokaz za reprezentativan produkcioni artefakt.
- Dostupnost rollback artefakta i rezultat vezbe kompromitovanog artefakta.

### 11.3 Kriterijumi izlaza

1. Produkcioni deployment-i se razresavaju na odobrene immutable digest-e.
2. Rollback artefakti ostaju dostupni tokom definisanog recovery horizonta.
3. Procedure karantina, opoziva i zamene artefakta su testirane.

