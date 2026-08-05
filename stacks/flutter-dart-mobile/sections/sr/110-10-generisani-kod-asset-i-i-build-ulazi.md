## 10. Generisani kod, asset-i i build ulazi

Generisani izlaz je deo proizvoda i mora biti reproduktivan i pregledan.

- Popiši `build_runner`, Freezed, JSON serializaciju, Retrofit, GraphQL, protobuf, lokalizaciju, route, DI, asset, icon, splash, Pigeon i custom generatore.
- Proveri verzije generatora, ulaze, opcije, vlasništvo izlaza, ponašanje clean rebuild-a i da li su generisani fajlovi namerno commitovani.
- Regeneriši u izolovanom clean stablu i uporedi izlaz; istraži drift umesto slepog prihvatanja velikih diff-ova.
- Pregledaj generisanu serializaciju, platformske binding-e, rute, registrant-e, dozvole, API klijente i šeme baza radi bezbednosti i kompatibilnosti.
- Audituj deklaracije asset-a, wildcard uključivanje, tajne slučajno upakovane kao asset-i, duplirane medije, licence fontova, pokrivenost locale-a i platformsko pakovanje.
- Pregledaj compile-time konstante i `--dart-define` vrednosti radi environment confusion-a, curenja tajni, pretpostavki o dead code-u i reproduktivnosti.
- Proveri icon, splash, manifest, Info.plist, entitlement, desktop metapodatke, web manifest i service-worker izlaz u finalnim artefaktima.
- Obori CI zbog neobjašnjenog generated drift-a, nedostajućih source ulaza, nereproduktivnog izlaza ili nepregledanih promena privilegija.

