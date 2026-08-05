# Revizija 06 - Flutter / Dart multiplatform production audit prompt

Datum: 2026-08-05

## Sažetak

Postojeći dvojezični prompt bio je strukturno usklađen, ali je sa 227 linija i 35 naslova predstavljao pre svega proširenu checklist-u. Nije dovoljno dokazivao identitet artefakta, native host stanje, ponašanje plugin-a, platformske lifecycle razlike, instalaciju, store/distribution tok, update, rollback, restore i incident recovery.

Novi EN/SR par je rekonstruisan kao samostalan production audit ugovor verzije 2.0.0. Ima po 990 stvarnih Markdown linija i 87 potpuno usklađenih naslova.

## Glavni nedostaci stare verzije

- Nedovoljan source-to-runtime evidence lanac.
- Nedovoljno odvajanje Dart/Flutter koda, generisanog koda, native host projekata, plugin implementacija i finalnog artefakta.
- Prekratka obrada async race condition-a, stream backpressure-a, isolate-a i background rada.
- Nedovoljno precizna pravila za platform channel, Pigeon, FFI i native memory safety.
- Nedovoljno detaljan offline queue, idempotency, conflict-resolution i migration model.
- Nedostatak zasebnih Android, iOS/iPadOS, web, Windows, macOS i Linux audit matrica.
- Nedovoljno detaljna obrada WebView-a, deep link-ova, notification payload-a, file parser-a i lokalnog storage-a.
- Slabo dokazivanje release artefakta, signing identiteta, store/distribution stanja, staged rollout-a i rollback-a.
- Nedostatak obaveznih evidence matrica, incident trusted rebuild-a i merljivog disaster recovery-ja.

## Ključna unapređenja

- Aktuelni Flutter 3.44.8 / Dart 3.12.2 stable baseline uz obaveznu ponovnu proveru.
- Jasno označeno da je Flutter 3.47 beta linija, ne podrazumevani production izbor.
- E0-E5 evidence model i strogi P0-P3 finding register.
- Potpun lanac: commit -> dependency graph -> generated code -> native host -> build -> potpis -> distribucija -> instalacija -> runtime -> telemetrija -> rollback/recovery.
- Toolchain matrice za Android, Apple, web, Windows, macOS i Linux.
- Supply-chain audit za pub, git/path dependency-je, build_runner, native biblioteke, plugin-e i binarne blob-ove.
- Duboka obrada Dart correctness-a, state management-a, routing-a, widget identity-ja, lifecycle-a i process death-a.
- Async cancellation, stale-result suppression, idempotency, stream ordering, backpressure, isolate protokoli i background scheduling.
- Platform channel/Pigeon autorizacija, FFI ownership i federated plugin ugovori.
- Add-to-app, više engine-a i old host/new module kompatibilnost.
- Auth, BOLA/IDOR, tenant izolacija, secure storage, kriptografija, privacy i deletion lifecycle.
- Network, TLS, retry budget, WebView bridge, storage migracije, offline sync, files/media i hardware permissions.
- Posebni production audit slojevi za Android, iOS/iPadOS, web, Windows, macOS i Linux.
- Accessibility, adaptive layout, lokalizacija, RTL, input režimi i assistive-technology testiranje.
- Performance, size, symbols, obfuscation, crash deobfuscation i release dijagnostika.
- CI/CD trust boundary, immutable artifact promotion, signing custody, SBOM i provenance.
- Store/distribution, install, update, staged rollout, forward-fix, rollback, backup/restore i trusted rebuild.
- 12 obaveznih evidence matrica i 18 adversarial/failure scenarija.

## Aktuelni baseline

- Flutter stable: 3.44.8.
- Dart stable u tom izdanju: 3.12.2.
- Datum objave stable artefakta: 2026-07-23.
- Flutter 3.47 je beta linija i zahteva eksplicitno opravdanje i rollback dokaz.
- Platformska podrška mora se proveravati po zvaničnim Flutter deployment matricama i realnim plugin/toolchain ograničenjima.
- Flutter web JavaScript/Wasm režim, renderer, CSP, service worker i COOP/COEP moraju se dokazati u stvarnom deployment-u.
- iOS UIScene lifecycle, Android host/manifest, desktop packaging i signing proveravaju se u finalnim artefaktima, ne samo u source konfiguraciji.

## Rezultati validacije

- EN stvarne linije: 990.
- SR stvarne linije: 990.
- EN naslovi: 87.
- SR naslovi: 87.
- Heading parity: prošao.
- Line-shape parity: prošao.
- YAML frontmatter: validan.
- Markdown code fence blokovi: balansirani.
- JSON baseline manifest: validan.
- Baseline hardcode scan: prošao.
- En dash, em dash i non-breaking hyphen u SR promptu: 0.
- ZIP integritet: proverava se u koraku pakovanja.

## Preostali repository-level problemi

- Java/Spring Boot stari EN/SR par i dalje ima heading mismatch i biće rekonstruisan u svom koraku.
- Python/PySide6 stari EN/SR par i dalje ima različit broj naslova i biće rekonstruisan u svom koraku.
- Semantic parity, markdownlint, link checker i fixture-based eval harness ostaju zajednički repository-level poslovi.
