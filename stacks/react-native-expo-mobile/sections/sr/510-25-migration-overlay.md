## 25. Migration overlay

### 25.1 React Native i Expo upgrade
- Upgrade-uj podrzane framework i Expo SDK verzije inkrementalno osim kada dokaz opravdava drugaciji redosled.
- Pre svakog koraka zamrzni baseline ponasanje, testove kriticnih tokova, release artefakte, simbole, source map, store stanje, update stanje i rollback put.
- Uporedi native template, config plugin, generisani projekat, build alat, deklaraciju dozvole, lifecycle, Hermes, Metro, Codegen i third-party podrsku.
- Testiraj release binary i OTA kompatibilnost na svakom koraku; ne oslanjaj se samo na Expo Doctor ili uspesnu kompilaciju.
- Prati deprecated API, uklonjeno ponasanje, support period, store zahtev, promenu minimalnog OS-a i zamenu native biblioteke.
- Rollout-uj svaki korak nezavisno sa telemetrijom, guardrail-om, abort-om, rollback-om i sacuvanim dokazom.

### 25.2 New Architecture i Expo usvajanje
- Popisi nepodrzane biblioteke, custom native module, view manager, JSI kod, brownfield surface, build skriptu i native patch pre migracije.
- Migriraj jednu granicu po koraku sa schema, threading, lifecycle, memory, error i compatibility testovima.
- Pri usvajanju Expo-a ili CNG-a definisi vlasnistvo native projekta, pokrivenost config plugin-a, pravila regeneracije, development-build strategiju, EAS vezu i izlazni put.
- Ne brisi ispravno native ponasanje prebuild cleanup-om dok svaka rucna izmena nema autoritativni config plugin ili dokumentovanu strategiju vlasnistva.
- Validiraj maintainera biblioteke, fork plan, vlasnistvo patch-a, buducu framework podrsku i rollback iz delimicno migriranog stanja.
- Ukloni compatibility kod tek kada production dokaz potvrdi zamenu kroz podrzane platforme i verzije.

