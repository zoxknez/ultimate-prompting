## 20. Faza O - Testiranje I Quality Engineering

### 20.1 Test Strategija I Determinizam

1. Mapiraj unit, integration, component, UI, screenshot, instrumented, end-to-end, migration, benchmark, fuzz, security i device testove.
2. Vezi testove za rizike i kriticne tokove, a ne samo code coverage.
3. Proveri deterministicko vreme, dispatcher-e, randomness, network, database, locale, time zone i device state.
4. Ukloni flaky sleep i nekontrolisane eksterne dependency-je.
5. Proveri da fake implementacije cuvaju semantiku koju test zahteva i ne skrivaju concurrency ili persistence bug.
6. Razdvoji hermetic testove od environment-dependent testova.
7. Retry belezi kao dokaz flakiness-a, a ne kao dokaz stabilnosti.
8. Svaka P0-P2 popravka treba da dobije regression test gde je tehnicki izvodljivo.

### 20.2 Unit, Coroutine, Flow I Data Testovi

1. Testiraj reducer-e, state holder-e, ViewModel-e, use case-ove, repository-je, parser-e, validator-e, serializer-e, auth, retry i conflict logiku.
2. Testiraj success, empty, boundary, invalid, timeout, cancellation, duplicate, out-of-order, partial i recovery scenario.
3. Ispravno koristi coroutine test API-je i virtual time.
4. Proveri hot i cold Flow ponasanje, replay, sharing, cancellation, completion i error.
5. Testiraj Room query, constraint, transaction, migration i concurrency.
6. Testiraj network error mapping, schema drift, malformed payload i idempotency.
7. Gde je prakticno proveri da test pada za originalni defekt pre popravke.

### 20.3 Compose UI, View I Instrumented Testovi

1. Testiraj semantics i user-visible ponasanje, a ne samo implementation detail-e.
2. Kontrolisi clock, idling, animation, background rad, network, permission i test data.
3. Testiraj navigation, back, restoration, deep link, process recreation, rotation, locale, font scale i window size.
4. Testiraj View i Compose interoperabilnost i lifecycle boundary-je.
5. Proveri da screenshot testovi imaju stabilne rendering uslove i pregledane baseline slike.
6. Pokreni release-like ili minified instrumented smoke testove gde postoji kritican reflection ili R8 behavior.
7. Testiraj na fizickim uredjajima kada su hardware, codec, DRM, Bluetooth, camera, TV remote, OEM ponasanje ili thermal state bitni.

### 20.4 Macrobenchmark, Baseline Profiles I Device Matrica

1. Napravi Macrobenchmark za startup, scroll, navigation, playback i druge kriticne tokove.
2. Generisi app-specific Baseline Profiles i proveri da su merge-ovani i isporuceni.
3. Benchmark-uj release ili benchmark varijante sa reprezentativnim podacima.
4. Definisi device matricu kroz minimum SDK, target behavior, aktuelni stable Android, reprezentativne OEM-ove, low RAM, tablet, foldable, TV, 16 KB i relevantne ABI-je.
5. Ukljuci offline, slow network, low storage, battery saver, dark theme, locale, font scale i permission state.
6. Zabelezi device-lab konfiguraciju i ne proseci tako da sakrijes ozbiljan device-specific kvar.

