## Istrazivacki Baseline - 5. avgust 2026.

Ovo je pocetna tacka vezana za datum. Pre svake lifecycle, migration, security ili compatibility odluke ponovo proveri zvanicne izvore, lockfile, instalirane pakete, build image, arhitekturu, libc, native ABI i pokrenuti proces.

| Komponenta | Baseline | Obavezna provera tokom audita |
| --- | --- | --- |
| Node.js | 26 Current; 24 Krypton LTS; 22 Jod LTS. Ponovo proveri tacne patch verzije i datume podrske. | Stvarni binary, release linija, arhitektura, libc, OpenSSL, ICU, V8, native ABI, image i EOL. |
| Release model | Planirana je jedna major verzija godisnje pocevsi od Node.js 27. | Ulazak u LTS, ritam upgrade-a, pretpostavke podrske i usvajanje hosting platforme. |
| Express | Express 5 je najnoviji stabilni major; Express 4 ostaje legacy odrzavana linija. | Tacni patch, Node zahtev, advisory-ji, path sintaksa, middleware ponasanje i stanje migracije. |
| Fastify | Fastify 5.11.x je najnovija dokumentovana LTS linija na datum baseline-a. | Tacni patch, plugin podrska, encapsulation, schema compiler, serializer i Node matrica. |
| TypeScript | TypeScript 7 je stabilan; TypeScript 6 ostaje migration i compatibility linija. | Compiler koji koriste editor, CI, build, generatori, testovi i production source map-e. |
| API security | OWASP API Security Top 10 2023 je aktuelno zvanicno API risk izdanje na datum baseline-a. | Mapiraj primenljive rizike na konkretne rute, identitete, resurse, tokove podataka i testove. |
| Observability | OpenTelemetry JavaScript podrzava Node instrumentaciju i OTLP exporter-e; stabilnost paketa se razlikuje. | SDK i instrumentation verzije, redosled inicijalizacije, propagation, sampling, redaction i overhead. |

### Politika Primarnih Izvora

- Koristi zvanicnu Node.js, Express, Fastify, TypeScript, package-manager, database, hosting-platform, OpenTelemetry i standards dokumentaciju.
- Zabelezi naslov izvora, URL, datum pristupa, tacnu tvrdnju, izabranu verziju i repository ili runtime dokaz koji je potvrdjuje ili osporava.
- Ne zamenjuj lifecycle, security, migration ili protocol smernice snippet-ima, popularnoscu, sazecima ili AI generisanim tvrdnjama.
- Kada se zvanicni izvori i runtime dokaz ne slazu, prikazi konflikt i zadrzi odluku uslovnom dok se ne potvrde tacni artefakt i proces.

