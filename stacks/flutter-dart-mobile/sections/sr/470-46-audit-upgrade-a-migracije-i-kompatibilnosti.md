## 46. Audit upgrade-a, migracije i kompatibilnosti

Tretiraj SDK, package, platform, architecture, data i distribution upgrade kao migracije ponašanja.

- Popiši trenutne i ciljne Flutter/Dart, package major verzije, native toolchain-e, platform SDK-ove, minimalne OS/browser verzije, renderer-e, storage šeme i distributivne formate.
- Pročitaj zvanične breaking change-ove, migration guide-ove, release note-ove, deprecation-e, store rokove, plugin kompatibilnost i platformske lifecycle promene.
- Napravi compatibility matricu za stare podatke, stari cache, stari server, novi server, stari klijent, novi klijent, background job-ove, deep link-ove, notifikacije i nezavisno deploy-ovane komponente.
- Nadograđuj u ograničenim fazama sa clean build-om, pregledom generated diff-a, contract testovima, platformskim build-ovima, pregledom artefakta, device/browser testovima, poređenjem performansi i rollback-om posle svake faze.
- Koristi expand-and-contract za storage i API promene šeme; izbegni jednosmernu destruktivnu migraciju pre dokazivanja old/new koegzistencije i oporavka.
- Proveri signing identitet, bundle/package ID, keychain/secure-storage dostupnost, putanje fajlova, lokaciju baze, store listing, update eligibility i kontinuitet korisničkih podataka.
- Testiraj prekinut upgrade, malo diska, opozvanu dozvolu, offline launch, vraćen stari backup, downgrade pokušaj, rollback i support handoff.
- Ne uklanjaj compatibility putanje, legacy podatke, staru API podršku, simbole ili rollback artefakte dok telemetrija i politika ne dokažu završetak deprecation prozora.

