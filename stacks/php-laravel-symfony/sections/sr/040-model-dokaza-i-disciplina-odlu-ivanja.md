## Model dokaza i disciplina odlučivanja

### Nivoi dokaza E0-E5

| Nivo | Značenje | Primeri |
| --- | --- | --- |
| E0 | Tvrdnja, ticket, roadmap ili pretpostavka | README tvrdnja ili nedokumentovana beleška |
| E1 | Statički source, konfiguracija, šema ili deklaracija | composer.json, route source, ORM mapping, php.ini template |
| E2 | Razrešeni, generisani ili artifact dokaz | composer.lock graf, optimizovani autoload, container digest, SBOM |
| E3 | Izvršeni lokalni ili integracioni dokaz | production bootstrap, integration, migration, worker ili security test |
| E4 | Staging ili production-like load, failure, rollout ili rollback dokaz | soak, queue replay, canary, worker drain, rollback drill |
| E5 | Produkcijsko posmatranje, izolovani restore ili incident drill | release telemetrija, restore validacija, containment vežba |

### Status nalaza

- POTVRĐENO zahteva dokaz koji reprodukuje ili direktno pokazuje materijalnu tvrdnju.
- DELIMIČNO_POTVRĐENO znači da je deo uzročnog lanca dokazan, ali nedostaje runtime, network, data, load ili recovery korak.
- NEPROVERENO znači da je potreban dokaz nedostupan, nebezbedan, blokiran ili nije izvršen.
- NIJE_PRIMENJIVO zahteva konkretan razlog iz obima.
- ODBAČENO znači da je testirana hipoteza opovrgnuta i da je dokaz opovrgavanja sačuvan.

### Obavezni zapis nalaza

```text
ID / Težina P0-P3 / Status / Nivo dokaza
Oblast / Framework / Ulazna tačka / Ruta / Posao / Fajl / Runtime / Akter / Tenant
Invarijanta / Dokaz / Komanda / Exit code / Reprodukcija
Uzrok / Putanja kvara ili zloupotrebe / Uticaj / Blast radius
Najmanja popravka / Odbačene alternative / Regresioni test
Rollout / Rollback / Monitoring / Preostali rizik / Vlasnik
```

