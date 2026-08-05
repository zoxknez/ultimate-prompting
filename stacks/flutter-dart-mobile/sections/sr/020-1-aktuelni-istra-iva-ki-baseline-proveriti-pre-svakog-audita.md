## 1. Aktuelni istraživački baseline - proveriti pre svakog audita

Ovaj baseline odražava primarne izvore dostupne 5. avgusta 2026. Predstavlja samo početnu tačku. Pre svake preporuke ili izmene ponovo proveri aktuelna stabilna izdanja, politike podrške, platformske zahteve, breaking change-ove, bezbednosna upozorenja, store pravila i toolchain koji projekat stvarno razrešava.

| Oblast | Baseline 5. avgusta 2026. | Obavezna provera tokom audita |
| --- | --- | --- |
| Flutter stable | Flutter 3.44.8 sa Dart 3.12.2, objavljen 23. jula 2026. | Tačan SDK hash i kanal u lokalnom, CI, build i release okruženju; aktuelni stabilni patch i status podrške. |
| Flutter prerelease | Flutter 3.47 je beta linija i nije podrazumevani production baseline. | Da li se koristi beta/dev SDK ili eksperimentalna funkcija, zašto je potrebna i kako je dokazan rollback. |
| Podržane platforme | Flutter objavljuje odvojene matrice deployment podrške za Android, iOS, web, Windows, macOS i Linux. | Projektni minimumi, ciljne OS/browser verzije, matrica arhitektura, plugin podrška, store pravila i pokrivenost stvarnim uređajima. |
| Arhitektura | Aktuelne Flutter smernice favorizuju eksplicitne UI/data slojeve, repozitorijume, immutable modele, jednosmerni tok podataka i testabilne granice zavisnosti kada je prikladno. | Da li izabrana arhitektura stvarno čuva domenske invarijante, vlasništvo, cancellation, testabilnost i platformsku nezavisnost. |
| Web rendering | Flutter web podržava JavaScript i WebAssembly build režime sa ograničenjima renderer-a i browser-a. Threaded Wasm može zahtevati cross-origin isolation header-e. | Stvarni build režim, browser matrica, COOP/COEP, CSP, keširanje, service worker ponašanje, source map-e i fallback putanja. |
| iOS lifecycle | Moderni Flutter iOS projekti koriste UIScene lifecycle ponašanje; migracija i plugin kompatibilnost moraju biti provereni. | Scene konfiguracija, deep link-ovi, state restoration, notifikacije, background režimi, add-to-app host-ovi i plugin callback-ovi. |
| Bezbednost i supply chain | Framework podrazumevana podešavanja ne zamenjuju autorizaciju aplikacije, rukovanje tajnama, pregled zavisnosti, platformski hardening ili proveru potpisanog izdanja. | Razrešeni paketi, upozorenja, native kod, generisani kod, signing identiteti, provenance artefakata i runtime granice dozvola. |

