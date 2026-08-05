## Evidence Model I Disciplina Odlucivanja

### Nivoi Dokaza E0-E5

| Nivo | Znacenje | Primeri |
| --- | --- | --- |
| E0 | Tvrdnja, ticket, roadmap ili pretpostavka | README tvrdnja ili nedokumentovana napomena |
| E1 | Staticki source, konfiguracija, schema ili deklaracija | package.json, source rute, ORM schema |
| E2 | Resolved, generisani ili artifact dokaz | lock graph, compiled JS, image digest, SBOM |
| E3 | Izvrseni lokalni ili integration dokaz | production start, integration ili migration test |
| E4 | Staging ili production-like load, failure, rollout ili rollback dokaz | soak, canary, queue replay, rollback drill |
| E5 | Produkcijsko posmatranje, izolovani restore ili incident drill | release telemetry, restore validacija, containment vezba |

### Status Nalaza

- CONFIRMED zahteva dokaz koji reprodukuje ili direktno demonstrira materijalnu tvrdnju.
- PARTIALLY_CONFIRMED znaci da je deo uzrocnog lanca dokazan, ali nedostaje runtime, network, data, load ili recovery korak.
- UNVERIFIED znaci da obavezni dokaz nije dostupan, nije bezbedan, blokiran je ili nije izvrsen.
- NOT_APPLICABLE zahteva konkretan scope razlog.
- REJECTED znaci da je testirana hipoteza opovrgnuta i dokaz opovrgavanja sacuvan.

### Obavezan Zapis Nalaza

```text
ID / Severity P0-P3 / Status / Evidence nivo
Oblast / Servis / Ruta / Job / Fajl / Runtime / Akter / Tenant
Invarijanta / Dokaz / Komanda / Exit code / Reprodukcija
Root cause / Putanja kvara ili exploita / Uticaj / Blast radius
Minimalna popravka / Odbacene alternative / Regression test
Rollout / Rollback / Monitoring / Residual risk / Owner
```

