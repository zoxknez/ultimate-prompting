## 56. Production readiness checklist

- [ ] Scope, vlasnici, ovlašćenje, granica dokaza, kritični tokovi i tvrdnje podrške su dokumentovani.
- [ ] Workspace, korisnički podaci, signing materijal, store-ovi i production sistemi bili su zaštićeni tokom audita.
- [ ] Razrešeni Flutter/Dart/native toolchain-i i zavisnosti su podržani, reproduktivni i bez neobjašnjenog drift-a.
- [ ] Generisani kod i asset-i se reprodukuju čisto, a diff-ovi koji utiču na privilegije su pregledani.
- [ ] Arhitektura čuva domenske invarijante, eksplicitno vlasništvo, platformsku izolaciju, lifecycle i testabilnost.
- [ ] Autentikacija, autorizacija, tenant izolacija, tajne, privatnost i lifecycle podataka zadovoljavaju dokumentovanu politiku.
- [ ] Async operacije, stream-ovi, isolate-i, background job-ovi, channel-i, FFI i plugin-i imaju ograničen lifecycle i failure ponašanje.
- [ ] Mreža, WebView, storage, migracija, offline, fajlovi, dozvole, hardver, notifikacije i deep link-ovi imaju adversarial pokrivenost.
- [ ] Android, iOS/iPadOS, web, Windows, macOS i Linux tvrdnje su pojedinačno dokazane ili eksplicitno isključene.
- [ ] Adaptivni layout, accessibility, lokalizacija, RTL, input režimi i reduced-motion ponašanje prolaze kritične tokove.
- [ ] Release performanse, kapacitet, memorija, baterija, veličina, simboli i dijagnostički budžeti zadovoljavaju odobrene pragove.
- [ ] Slojeviti testovi i quality gate-ovi pokrivaju source, generisani kod, native granice, artefakte, instalaciju, upgrade i recovery.
- [ ] Telemetrija je privacy-safe, artifact-aware, actionable, otporna i povezana sa vlasnicima i runbook-ovima.
- [ ] Izolacija flavor-a i okruženja sprečava cross-targeting, a feature flag-ovi ne mogu dati autorizaciju.
- [ ] CI/CD koristi pregledane trust boundary-je, immutable promociju, zaštićeno potpisivanje, provenance, SBOM i zadržane recovery artefakte.
- [ ] Store/distribution, install, update, staged rollout, abort, rollback/forward-fix i support procedure su testirane.
- [ ] Backup restore, oporavak signing/store pristupa, trusted rebuild, incident containment i izmereni RPO/RTO su demonstrirani.
- [ ] Preostali rizici, prihvaćeni izuzeci, istek, vlasnici, kompenzacione kontrole i sledeći review su zabeleženi.

