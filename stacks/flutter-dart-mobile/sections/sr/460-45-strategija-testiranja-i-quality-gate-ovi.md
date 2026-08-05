## 45. Strategija testiranja i quality gate-ovi

Koristi slojevite testove vezane za rizike, ugovore, platforme i release artefakte.

- Unit-testiraj domenske invarijante, parsiranje, serializaciju, error mapping, state tranzicije, conflict politiku, retry politiku, authorization odluke i migracije.
- Widget-testiraj semantics, layout constraints, forme, validaciju, loading/error/empty stanja, fokus, tastaturu, text scale, RTL, restoration i interaction race-ove.
- Golden-testiraj stabilne vizuelne ugovore sa kontrolisanim fontovima, locale-ima, veličinama uređaja, pixel ratio-ima, temama i opravdanim tolerancijama; ne skrivaj stvarne regresije širokim pragovima.
- Integration-testiraj kritične tokove na stvarnim ili production-equivalent platformskim ciljevima sa realnim backend, lifecycle, permission, network, storage i update uslovima.
- Contract-testiraj backend API-je, platform channel-e, Pigeon API-je, plugin-e, generisane klijente, šeme baza, deep link-ove, notifikacije i preklapanje stare/nove verzije.
- Property/fuzz-testiraj parser-e, serializer-e, URL/path handling, formate fajlova, obradu arhiva, native granice, state machine-e i rešavanje konflikata gde je vredno.
- Performance-testiraj startup, frame pacing, memoriju, CPU, bateriju, mrežu, disk, veličinu, background rad, realtime, velike podatke, burst i soak scenarije.
- Security-testiraj auth, BOLA/IDOR, tenant izolaciju, storage leakage, WebView bridge-eve, deep link-ove, notifikacije, file parsing, mrežne greške, integritet update-a i kontinuitet potpisivanja.
- Artifact-testiraj finalne release pakete: identitet, verziju, potpise, dozvole, entitlement-e, native biblioteke, asset-e, simbole, source map-e, install, launch, update i uninstall.
- Karantiniraj samo dokazane flaky testove sa vlasnikom, razlogom, istekom, telemetrijom i planom zamene; nikada ne normalizuj tihe retry-je ili trajno preskočene platformske testove.

