## 27. Autorizacija, vlasništvo objekata i tenant izolacija

Klijent može poboljšati UX, ali ne može biti autoritativna bezbednosna granica.

- Mapiraj svaku privilegovanu akciju, lookup objekta, mutaciju, export, share, upload, download, admin tok, support tok i tenant-scoped query.
- Proveri serversku autentikaciju, dozvolu, ulogu, vlasništvo resursa, članstvo u tenant-u, status, kvotu i provere poslovnih invarijanti.
- Tretiraj route guard-e, skrivene dugmiće, lokalne uloge, keširane entitlement-e, feature flag-ove i disabled kontrole samo kao presentation.
- Spreči BOLA/IDOR testiranjem promenjenih identifikatora, zastarelih linkova, drugog korisnika, drugog tenant-a, obrisanog članstva, smanjene uloge i opozvanog share-a.
- Proveri da local cache key-evi, particije baze, putanje fajlova, search index-i, notification payload-i, analitika i background task-ovi uključuju tačan account i tenant identitet.
- Testiraj promenu naloga i tenant-a tokom aktivnih read, write, upload, download, realtime, migration i restoration operacija.
- Audituj impersonation i delegated access sa eksplicitnim actor-om, subject-om, svrhom, trajanjem, scope-om, logovanjem, vidljivošću korisniku i opozivom.
- Zahtevaj negativne authorization testove na API, repository, state, route, storage, notification i UI integration slojevima.

