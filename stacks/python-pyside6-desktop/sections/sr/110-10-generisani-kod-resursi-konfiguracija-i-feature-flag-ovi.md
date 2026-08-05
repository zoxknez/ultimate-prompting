## 10. Generisani kod, resursi, konfiguracija i feature flag-ovi

### 10.1 Obim audita

1. Inventariši `.ui`, `.qrc`, QML cache, translation kataloge, protobuf/OpenAPI klijente, ORM modele, ikone, teme, schema-e, version fajlove i generisane binding-e.
2. Zabeleži generator executable, verziju, ulaze, opcije, okruženje, vlasništvo izlaza, determinizam i komandu regeneracije.
3. Mapiraj precedence konfiguracije kroz default-e, spakovane fajlove, environment, command line, registry/plist, korisnička podešavanja, enterprise policy, remote config i feature flag-ove.
4. Razlikuj javnu konfiguraciju od tajni i identifikuj vrednosti kopirane u pakete, logove, crash izveštaje ili support bundle-ove.
5. Pregledaj vlasništvo feature flag-a, targeting, expiry, offline ponašanje, fail-open/fail-closed ponašanje i rollback zavisnosti.
6. Otkrij stale generisani izlaz, developer-local resurse, nedostajuće prevode, razlike case-sensitive putanja i source/package drift.

### 10.2 Obavezna verifikacija

1. Regeneriši iz čistog checkout-a i zaustavi na neobjašnjenom diff-u ili nedostajućem toolchain-u.
2. Pregledaj paket i instaliranu aplikaciju da potvrdiš da su nameravani resursi, prevodi, sertifikati, schema-e i konfiguracija prisutni jednom i učitani sa trusted lokacija.
3. Testiraj precedence i ponašanje malformed vrednosti bez tihog fallback-a na nebezbedne default-e.
4. Vežbaj enable, disable, stale cache, network loss, targeting change, emergency kill i rollback scenarije feature flag-a.
5. Obezbedi da se osetljive vrednosti ubrizgavaju na ispravnoj runtime granici i da ne postoje u source kontroli, package resursima, logovima i telemetriji.

