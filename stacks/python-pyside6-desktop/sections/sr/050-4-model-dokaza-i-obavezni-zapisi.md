## 4. Model dokaza i obavezni zapisi

### 4.1 Nivoi dokaza

| Nivo | Značenje | Dozvoljeni zaključak |
| --- | --- | --- |
| E0 | Samo tvrdnja ili pretpostavka | Ne koristiti za readiness odluke. |
| E1 | Statički source ili konfiguracioni dokaz | Koristan za otkrivanje; runtime ponašanje ostaje neprovereno. |
| E2 | Razrešeno okruženje, dependency, generated-code ili build dokaz | Potvrđuje testiranu build putanju, ne instalirano ponašanje. |
| E3 | Dokaz zapakovanog artefakta, potpisa i instalacije na čistoj mašini | Potvrđuje isporučene bajtove i obim instalacije. |
| E4 | Instrumentovan runtime i user-journey dokaz | Potvrđuje ponašanje za testiranu platformu, konfiguraciju, podatke i opterećenje. |
| E5 | Production-like failure, upgrade, rollback, restore ili incident vežba | Obavezno za snažne tvrdnje o otpornosti i oporavku. |

### 4.2 Zapis nalaza

1. Dodeli stabilan ID nalaza, P0-P3 severity, confidence, evidence nivo, pogođenu platformu/verziju, fajl/simbol i vlasnika.
2. Zabeleži simptom, reprodukciju, root cause, trust granicu, poslovni i tehnički uticaj, uslove exploita ili kvara i blast radius.
3. Razlikuj source defekt, build defekt, packaging defekt, installation defekt, runtime defekt, operativni gap i dokumentacioni gap.
4. Definiši najmanju kompletnu popravku, odbačene alternative, compatibility uticaj, potrebu za migracijom, rollback i residual risk.
5. Priloži tačne komande, exit kodove, relevantne delove izlaza, hash-eve artefakata, screenshot-ove ili trace-ove, test podatke i timestamp-e.
6. Zatvori nalaz samo nakon fokusirane regresije i najšire primenljive packaged/runtime verifikacije.

