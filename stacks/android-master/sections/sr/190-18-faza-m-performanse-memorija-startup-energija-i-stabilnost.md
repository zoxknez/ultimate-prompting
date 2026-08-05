## 18. Faza M - Performanse, Memorija, Startup, Energija I Stabilnost

1. Uspostavi device, build, thermal, network i data baseline pre merenja.
2. Izmeri cold, warm i hot startup, TTID, TTFD, first useful content i ownership startup inicijalizacije.
3. Pregledaj App Startup initializer-e, content provider-e, kreiranje DI graph-a, SDK inicijalizaciju, disk I/O i synchronous network ili crypto pri startup-u.
4. Koristi StrictMode, Perfetto, CPU, memory, network, energy, layout, Compose i database alate prema potrebi.
5. Detektuj Activity, Fragment, View, Compose, Context, receiver, callback, coroutine, bitmap, cursor, WebView, player, surface i native leak.
6. Izmeri heap growth, GC, allocation churn, bitmap pressure, native memory, file descriptor-e, thread-ove i decoder resurse.
7. Testiraj ponovljenu navigaciju, rotation, playback, download, search, account switching i background cycle.
8. Izmeri frame timing i jank na kriticnim scrolling, animation, transition, keyboard i TV focus tokovima.
9. Proveri image loading dimenzije, cache policy, transformation, prefetch, cancellation i OOM ponasanje.
10. Proveri da database, serialization, parsing, diffing, sorting, filtering i formatting ne blokiraju kriticne thread-ove.
11. Izmeri battery, wakeup, alarm, network, location, Bluetooth, sensor, FGS i media lock uticaj.
12. Proveri ANR izvore ukljucujuci main-thread blocking, lock contention, binder call, broadcast receiver, service i input dispatch.
13. Koristi release-like build-ove i reprezentativne uredjaje. Ne izvodi production performanse iz brzog development racunara.
14. Definisi merljive budget-e i acceptance gate-ove za kriticne tokove.

