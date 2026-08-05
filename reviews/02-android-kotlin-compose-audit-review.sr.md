# Revizija 02 - Android / Kotlin / Jetpack Compose / Android TV Audit Prompt

## Status

- Srpska verzija: zavrsena
- Engleska verzija: zavrsena
- Strukturna EN/SR paritet provera: prosla
- Broj linija pre: 159 po jeziku
- Broj linija posle: 913 po jeziku
- Broj heading-a pre: 20 po jeziku
- Broj heading-a posle: 72 po jeziku
- Line-shape EN/SR paritet: 913/913, bez mismatch-a
- YAML front matter provera: prosla
- Markdown code fence provera: prosla
- En dash, em dash i non-breaking hyphen u srpskoj verziji: 0

## Glavni Problemi Prethodne Verzije

1. Prompt je bio dobra kratka kontrolna lista, ali nije predstavljao kompletan Android production audit ugovor.
2. Baseline je imao zastarelu i nedovoljno preciznu formulaciju Google Play 16 KB roka.
3. Nije razdvajao Android Studio, AGP, Gradle, JDK, Kotlin, KSP, Compose, SDK i NDK kompatibilnost dovoljno detaljno.
4. Build audit nije dovoljno pokrivao source set-ove, flavor-e, variant-e, manifest merge, code generation, convention plugin-e i dynamic feature module.
5. Release audit nije dovoljno pokrivao R8 configuration analysis, mapping, native symbols, update continuity, version code i rollback.
6. Native i 16 KB deo nije zahtevao pregled svake upakovane tranzitivne `.so` biblioteke, ELF alignment i stvarni 16 KB test.
7. Arhitektura je bila pomenuta, ali bez dependency direction, scope, hidden global state i module boundary analize.
8. Coroutines i Flow deo nije dovoljno pokrivao structured concurrency, sharing policy, backpressure, cancellation propagation i deterministicke testove.
9. Process death, SavedStateHandle, one-time events, account switching i state reconstruction nisu bili dovoljno razradjeni.
10. Navigation audit nije pokrivao hostile deep link, app link, predictive back, existing-task i duplicate side effect scenario.
11. Compose audit je bio prekratak za state ownership, side effect key-eve, strong skipping, compiler report-e i release performance.
12. Views i Compose interoperabilnost prakticno nisu bili obradjeni.
13. Adaptive UI nije pokrivao window size, foldable, multi-window, desktop mode, keyboard, mouse i external display.
14. Android TV deo nije bio dovoljno detaljan za focus restoration, lazy list promene, multiview, low-memory TV i remote varijacije.
15. Room audit nije pokrivao kompletan migration graph, historical schema fixture-e, downgrade, WAL i schema export.
16. Offline sync nije pokrivao authoritative source, idempotency, duplicate delivery, conflict i multi-device scenario.
17. Network audit nije dovoljno pokrivao auth refresh race, resumable transfer, parser bounds, IPv6-only, captive i real-time ordering.
18. Security deo nije imao pun IPC, PendingIntent, exported component, OAuth callback, token lifecycle, Keystore i untrusted parser audit.
19. Privacy deo nije povezivao stvarno SDK ponasanje sa consent-om, Data safety deklaracijom, account deletion-om i backup-om.
20. Background audit nije dovoljno pokrivao FGS type, exact alarm policy, WorkManager uniqueness, OEM kill i notification privacy.
21. Media3 deo nije dovoljno pokrivao DRM, MediaSession, audio route, headers, live edge, decoder leak i multiview.
22. Performance deo nije definisao TTID, TTFD, ANR izvore, native memory, file descriptor-e, energy i merljive budget-e.
23. Test deo nije sadrzao pun risk-based device matrix, release-like instrumented testove, Macrobenchmark i Baseline Profile verifikaciju.
24. Observability, staged rollout, kill switch, bad-release runbook, supply chain i CI secret boundary bili su nedovoljni.

## Najvaznija Unapredjenja

1. Uveden YAML front matter sa prompt ID-jem, verzijom, jezikom, statusom, default rezimom i required core fajlovima.
2. Uveden kompletan input contract za aplikaciju, distribuciju, device klase, toolchain, module, persistence, mrezu, background, media, native kod, podatke, CI i policy.
3. Uvedeno pravilo za bezbedan nastavak rada kada informacije nedostaju.
4. Prosiren protect-first ugovor za source, podatke, signing, keystore, mapping, native symbols i build artefakte.
5. Uveden aktuelan datirani baseline za Android Studio, AGP, Gradle, JDK, Kotlin, API 37, Play target API 36 i 16 KB rok.
6. Uvedena Android-specific P0-P3 interpretacija.
7. Uveden kompletan repository, included build, module, source-set, variant, flavor, manifest i native inventar.
8. Uvedena puna toolchain compatibility matrica i AGP 10 migration pregled.
9. Prosiren dependency i SDK governance na resolved graph, BOM drift, permissions, startup initializer, native code i privacy ponasanje.
10. Uveden kompletan debug i release build baseline sa ocuvanjem artefakata.
11. Prosiren R8 audit na keep rules, reflection, JNI, serialization, release-only putanje i configuration analysis.
12. Uvedena puna signing, versioning, update continuity, migration, downgrade i rollback analiza.
13. APK/AAB audit sada obuhvata manifest, permissions, splits, ABI, native provenance, ELF alignment i 16 KB test.
14. Arhitektura sada pokriva dependency direction, module cycle, DI scope, hidden singleton state i data invarijante.
15. Coroutines i Flow deo prosiren je na structured concurrency, exception propagation, sharing, lifecycle collection, cancellation, race i deterministic test scheduler.
16. Uveden detaljan process death, SavedStateHandle, transient event, account i UI state audit.
17. Navigation deo sada pokriva deep link trust boundary, app links, predictive back, duplicate navigation i sensitive route leakage.
18. Compose audit prosiren je na state ownership, side effect API-je, lazy key-eve, stability, strong skipping, compiler report-e i release benchmark.
19. Dodat je pun Views, Fragment i Compose interoperability audit.
20. Uvedene posebne faze za phone, tablet, foldable, desktop-like, Android TV, Wear OS i Automotive.
21. Room i storage audit prosiren je na query plan, transaction, migration graph, historical schema, backup, files, URI grant i cache policy.
22. Uveden kompletan offline-first, sync, conflict, queue, idempotency i multi-device audit.
23. Network audit prosiren je na timeout semantiku, auth refresh, retry, TLS, parser bounds, resume, caching, IPv6 i real-time reconnect.
24. Security audit sada pokriva exported component, intent, PendingIntent, Binder, provider, auth, session, Keystore, cryptography, WebView i parser input.
25. Privacy audit povezuje permissions, SDK ponasanje, consent, Data safety, analytics, backup, deletion i export.
26. Background audit prosiren je na WorkManager, FGS, exact alarm, FCM, notification, Doze, OEM kill i battery impact.
27. Media i device API audit obuhvata Media3, DRM, audio focus, MediaSession, headers, playback recovery, camera, location, Bluetooth, NFC i sensor data.
28. Performance audit sada zahteva startup, TTID, TTFD, jank, memory, native memory, ANR, battery i merljive acceptance gate-ove.
29. Accessibility i localization deo prosiren je na TalkBack, D-pad, keyboard, font scale, RTL, reduced motion, forms i locale correctness.
30. Uvedena potpuna risk-based test strategija sa unit, Flow, Room, Compose, instrumented, migration, Macrobenchmark, Baseline Profile i device matricom.
31. Uveden observability, crash mapping, native symbols, alerts, kill switch, rollout, rollback i incident runbook audit.
32. Uveden CI/CD i supply-chain audit sa untrusted PR granicom, pinned alatima, provenance-om, artifact promotion-om i credential least privilege zahtevima.
33. Uveden legacy i migration review bez modernizacije radi mode.
34. Uvedena obavezna test matrica, forbidden shortcuts, final report format i strogi Production Readiness Definition of Done.

## Primarni Baseline Izvori Dodati U Manifest

- Android Studio stable release notes i compatibility tabela
- Android Gradle Plugin 9.3 release notes i roadmap
- Kotlin release proces i aktuelne verzije
- Google Play target API level policy
- Android 16 KB page-size compatibility guidance
- Android architecture recommendations
- Jetpack Compose performance guidance
- Android security best practices

## Namerno Uklonjene Ili Ispravljene Pretpostavke

- Ispravljena je zastarela formulacija 16 KB roka i zahtev je vezan za stvarni Play policy i aplikaciju.
- Uklonjena je pretpostavka da najnoviji toolchain treba automatski instalirati.
- Uklonjena je pretpostavka da debug build ili emulator dokazuju release spremnost.
- Uklonjena je mogucnost da se siroko R8 keep pravilo koristi kao genericka popravka.
- Uklonjena je ideja da Clean Architecture, Compose rewrite ili veliki dependency upgrade predstavljaju univerzalno poboljsanje.
- Uklonjena je implicitna pretpostavka da client-side auth, root detection ili button disable predstavljaju authorization ili idempotency kontrolu.
- Uklonjena je mogucnost da se 16 KB podrzava samo na osnovu odsustva direktnog NDK koda.

## Sledeci Paket

DevOps / Docker / Kubernetes audit prompt na srpskom i engleskom.
