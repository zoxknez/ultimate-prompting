## Model dokaza i disciplina odluke

### Nivoi dokaza E0-E5

| Nivo | Znacenje | Primeri |
| --- | --- | --- |
| E0 | Tvrdnja, ticket, roadmap ili pretpostavka | README tvrdnja ili nedokumentovan dijagram |
| E1 | Staticki source, config, schema ili deklaracija | package.json, next.config, route source |
| E2 | Resolved ili generisani dokaz i artifact metadata | lock graph, route manifest, digest, SBOM |
| E3 | Izvrseni lokalni ili integration dokaz | production build/start, browser ili migration test |
| E4 | Staging ili production-like load, failure, rollout ili rollback dokaz | canary, load, cache-isolation, rollback drill |
| E5 | Produkcijsko posmatranje, izolovani restore ili incident drill | release telemetry, stvarna restore validacija |

### Status nalaza

- CONFIRMED zahteva dovoljan dokaz da reprodukuje ili direktno demonstrira tvrdnju.
- PARTIALLY_CONFIRMED znaci da je deo uzrocnog lanca dokazan, ali runtime, browser, platform ili recovery korak nedostaje.
- UNVERIFIED znaci da je obavezni dokaz nedostupan, nebezbedan, blokiran ili nije izvrsen.
- NOT_APPLICABLE zahteva konkretan scope razlog.
- REJECTED znaci da je testirana hipoteza opovrgnuta i da je dokaz opovrgavanja sacuvan.

### Obavezni zapis nalaza

```text
ID / Severity P0-P3 / Status / Nivo dokaza
Oblast / Ruta / Fajl / Runtime / Actor ili tenant
Invarijanta / Dokaz / Komanda / Exit code / Reprodukcija
Root cause / Failure ili exploit putanja / Impact / Blast radius
Najmanja popravka / Odbacene alternative / Regresioni test
Rollout / Rollback / Monitoring / Residual risk / Vlasnik
```

