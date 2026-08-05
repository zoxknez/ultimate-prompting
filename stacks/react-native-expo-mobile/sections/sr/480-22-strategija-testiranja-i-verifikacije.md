## 22. Strategija testiranja i verifikacije

### 22.1 Test piramida i pokrivenost ugovora
- Mapiraj domain unit test, state test, hook test, component test, navigation test, integration test, native test, end-to-end test, release test i recovery test.
- Koristi Jest ili projektni runner za deterministicku logiku, React Native Testing Library za korisniku vidljivo ponasanje i native test framework za native kod.
- Koristi Maestro, Detox, Appium, XCUITest, Espresso ili ekvivalent prema stvarnoj podrsci i pouzdanosti; ne tvrdi end-to-end pokrivenost na osnovu mock-a.
- Dodaj contract testove za API schemu, deep link, notification, native modul, Codegen, storage migraciju, update manifest i background payload.
- Testiraj negativnu autorizaciju, malformed input, duplu akciju, promenjen redosled dogadjaja, partial failure, timeout, gasenje procesa, upgrade, rollback i restore.
- Prati skipped, flaky, quarantined, platform-excluded i nereprezentativne testove kao eksplicitan rizik, a ne tihi uspeh.

### 22.2 Obavezna device i release matrica
- Ukljuci minimalnu, trenutnu i najnoviju podrzanu OS verziju gde je dostupna, plus reprezentativnog proizvodjaca, arhitekturu, memoriju, ekran i performance klasu.
- Ukljuci fizicke Android i Apple uredjaje za native lifecycle, notification, biometriju, background rad, medije, performance, signing i update verifikaciju.
- Testiraj debug, development, internal release, store release, embedded bundle, najnoviji OTA, rollback OTA, offline, upgrade i fresh-install put.
- Ukljuci sporu i nestabilnu mrezu, captive portal, malo storage-a, malo memorije, slabu bateriju, thermal pritisak, odbijene dozvole i prekinute operacije.
- Zabelezi tacan model uredjaja, OS build, arhitekturu, verziju aplikacije, runtimeVersion, update ID, kanal, digest artefakta i test podatke.
- Ne generalizuj jednu celiju matrice na sve podrzane uredjaje ili kanale bez dokumentovanog obrazlozenja.

