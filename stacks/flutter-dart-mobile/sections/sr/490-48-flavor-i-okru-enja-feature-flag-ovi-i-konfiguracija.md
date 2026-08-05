## 48. Flavor-i, okruženja, feature flag-ovi i konfiguracija

Izolacija okruženja mora biti sprovedena kroz kod, artefakte, servise, potpisivanje, store-ove i podatke.

- Popiši Dart entrypoint-e, flavor/scheme/configuration, application ID-jeve, bundle ID-jeve, web origin-e, desktop identitete, signing, ikone, nazive, backend-e, analitiku, push, plaćanja i store-ove.
- Proveri da nijedan production artefakt ne može slučajno targetirati staging identitet, bazu, analitiku, push, payment, storage, feature flag ili update kanal i obrnuto.
- Tretiraj `--dart-define`, environment fajlove, remote config, build podešavanja, manifest-e, plist vrednosti, web konfiguraciju i desktop resurse kao jednu efektivnu konfiguraciju.
- Otkrij nedostajuću, dupliranu, zastarelu, konfliktnu, insecure-default konfiguraciju i tihi fallback.
- Feature flag mora definisati vlasnika, svrhu, targeting, preduslov, default, offline ponašanje, telemetriju, istek, cleanup, security granicu i emergency ponašanje.
- Ne koristi client flag-ove za davanje serverske autorizacije ili zaštitu tajni; validiraj rizične kombinacije flag-ova i ponašanje starog klijenta.
- Testiraj fresh install, upgrade, vraćen backup, offline startup, nedostajući remote config, zastareo cache, pogrešan sat, opozvan flag i rollout/rollback.
- Uključi snapshot efektivne konfiguracije u release dokaze bez izlaganja tajni.

