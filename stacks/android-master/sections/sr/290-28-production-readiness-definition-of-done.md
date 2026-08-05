## 28. Production Readiness Definition Of Done

Aplikacija je production-ready samo kada su svi primenjivi elementi dokazani:

1. Necommitovan rad, produkcioni podaci, signing materijal i tajne bili su zasticeni tokom audita.
2. Stvarni moduli, varijante, flavor-i, manifesti, dependency-ji, SDK-ovi, native biblioteke i release putanje su inventarisani.
3. Android Studio, AGP, Gradle, JDK, Kotlin, SDK, NDK, KSP, Compose i plugin verzije su kompatibilne i reproduktivne.
4. Debug i release baseline prolaze za zahtevane varijante sa stvarnim command dokazima.
5. Release koristi namenjeni signing, endpoint-e, flag-ove, R8, resource shrinking, mapping, native symbols i policy deklaracije.
6. Application ID, signing kontinuitet, version code, database migration i update putanje su bezbedni.
7. 16 KB kompatibilnost je proverena za svaku upakovanu native biblioteku ili formalno oznacena kao `NOT_APPLICABLE`.
8. Nijedan primenjivi P0 ne ostaje otvoren.
9. P1 nalazi su popravljeni ili formalno contained sa owner-om, rokom, monitoring-om i recovery-jem.
10. Kriticni happy, negative, offline, retry, cancellation, lifecycle, process-death, account, migration i rollback tokovi prolaze.
11. Identitet, session, autorizacija, deep link, exported komponenta, WebView, fajl, permission i osetljivi podaci su zasticeni.
12. Concurrency, transaction, idempotency, synchronization i conflict ponasanje cuvaju data invarijante.
13. Background rad, notification, media, device API i battery use su ispravni pod platform ogranicenjima.
14. Accessibility, localization, adaptive layout, TV ili drugo target-device ponasanje prolazi definisanu matricu.
15. Startup, jank, memory, ANR, energy i kriticni performance budget-i su izmereni i prihvatljivi.
16. Unit, integration, UI, instrumented, migration, release i benchmark testovi pokrivaju najvece rizike i dovoljno su deterministicki.
17. Crash mapping, native symbols, telemetry, alert, feature flag, kill switch, runbook, staged rollout i rollback su testirani.
18. Aktuelni Google Play i primenjivi pravni ili sektorski zahtevi su pregledani, uz eksplicitno blokiranje neresenih strucnih pitanja gde je potrebno.
19. Preostali rizik je eksplicitan i prihvacen od ovlascenog owner-a.
20. Nijedna materijalna oblast nije proglasena bezbednom samo zato sto nije testirana.

Ako je bilo koji primenjivi blokirajuci element nepotpun, napisi:

> Not fully production-ready.

Zatim navedi tacne blokirajuce uslove.

