## 10. Hermes, Metro, bundle i source map

### 10.1 Hermes runtime
- Potvrdi Hermes verziju bundlovanu sa stvarnim React Native izdanjem i artefaktom; ne upravljaj njome kao nepovezanom verzijom na osnovu pretpostavke.
- Uporedi debug, development, profile i release ponasanje po bytecode-u, optimizaciji, debugger-u, obradi exception-a, startup-u, memoriji i native integraciji.
- Pregledaj sinhrone native pozive, velike object grafove, serializaciju, ponovljeno globalno zadrzavanje i duge JS taskove.
- Proveri symbolication crash-a i greske sa odgovarajucim JavaScript bundle-om, Hermes source map-om, native simbolima, update ID-jem i identitetom izdanja.
- Testiraj cold launch, warm launch, reload, OTA launch, offline launch, low-memory stanje i ponovljenu navigaciju u release rezimu.
- Tretiraj migraciju engine-a ili promenu koja utice na bytecode kao dogadjaj native runtime kompatibilnosti.

### 10.2 Metro i granice bundle-a
- Auditiraj resolver konfiguraciju, monorepo watch folder, symlink obradu, platform extension, package exports, alias, transformer i serializer hook.
- Otkrij duple React, React Native, native-module wrapper, state biblioteku ili singleton kopije nastale zbog workspace-a ili resolver drift-a.
- Pregledaj bundle sadrzaj radi tajni, privatnih endpoint-a, internih feature flag-ova, debug koda, source putanja, test fixture-a, kredencijala i nepotrebnih asset-a.
- Izmeri bundle velicinu, broj modula, lazy loading, route splitting gde je podrzan, startup import-e i dupliranje asset-a.
- Dokazi minification, dead-code elimination, zamenu environment vrednosti, cuvanje source map-a i release-only code putanje.
- Sacuvaj manifest koji mapira release i update identitet na tacan bundle, source map, asset i native binarni fajl.

