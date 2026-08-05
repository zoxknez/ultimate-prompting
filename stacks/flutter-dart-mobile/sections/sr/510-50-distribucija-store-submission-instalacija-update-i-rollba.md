## 50. Distribucija, store submission, instalacija, update i rollback

Uspešan release znači da korisnici mogu bezbedno dobiti, instalirati, pokrenuti, ažurirati i oporaviti nameravani artefakt.

- Popiši Google Play, App Store/TestFlight, web/CDN, Microsoft Store/MSIX, direktne Windows installer-e, Mac App Store/Developer ID, Linux store/pakete, enterprise i interne kanale.
- Proveri kontinuitet identiteta, monotonost version/build-a, potpisivanje, metapodatke, screenshot-e, privacy disclosure-e, content rating, export compliance, subscription-e, brisanje naloga i review zahteve.
- Testiraj clean install, upgrade iz svake podržane prethodne verzije, skipped-version upgrade, reinstall, restore, promenu kanala, promenu arhitekture, prekinutu instalaciju, malo diska, offline launch i uninstall.
- Proveri da korisnički podaci, secure storage, baza, fajlovi, dozvole, notifikacije, deep link-ovi, background task-ovi, app link-ovi i association-i prežive ili se resetuju prema politici.
- Definiši staged rollout kohorte, telemetry gate-ove, acceptance pragove, abort trigger-e, freeze ovlašćenje, rollback vlasnika, support komunikaciju i store-specific rollback ograničenja.
- Web deployment mora sprečiti mešane verzije asset-a, stale HTML/service worker zamke, nekompatibilne API promene, nedostajuće source map-e i cache-poisoned rollback.
- Mobile store rollback može zahtevati forward-fix build; sačuvaj old/new kompatibilnost, remote disable kontrole, backend mitigacije i recovery komunikaciju.
- Desktop updater/installer mora proveriti potpis, metapodatke, kanal, arhitekturu, atomsku zamenu, aktivan proces, downgrade politiku, rollback i rotaciju ključa.
- Ne nazivaj rollout uspešnim dok operativni dokazi ne pokriju nameravane kohorte, kritične tokove, migracije, crash-eve, performanse, support signale i rollback spremnost.

