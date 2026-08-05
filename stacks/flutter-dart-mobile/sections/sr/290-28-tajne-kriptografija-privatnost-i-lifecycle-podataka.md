## 28. Tajne, kriptografija, privatnost i lifecycle podataka

Smanji podatke i tajne pre izbora storage-a ili enkripcije.

- Popiši API ključeve, client secret-e, sertifikate, privatne ključeve, tokene, ključeve baza, analytics identifikatore, device ID-jeve, lične podatke i regulisane podatke.
- Pretpostavi da se vrednosti isporučene u Dart kodu, asset-ima, JavaScript-u, native resursima, manifest-ima, Info.plist-u, desktop resursima ili `--dart-define` mogu izvući.
- Koristi backend-held tajne i scoped kratkotrajne kredencijale za privilegovane servise; ograniči javne client ključeve po origin-u, application ID-ju, sertifikatu, kvoti i backend autorizaciji gde je podržano.
- Proveri kriptografski algoritam, režim, jedinstvenost nonce/IV, slučajnost, key derivation, authentication tag, čuvanje ključa, rotaciju, opoziv, backup, restore i verzionisanje.
- Ne izmišljaj custom kriptografiju i ne tretiraj obfuscation, podeljene stringove, base64, privatni storage aplikacije ili certificate pinning kao enkripciju.
- Mapiraj prikupljanje, svrhu, pristanak, pravni osnov, minimizaciju, retention, brisanje, export, ispravku, backup, support pristup i third-party transfer.
- Audituj screenshot-e, clipboard, notifikacije, logove, crash izveštaje, analitiku, snimke, fajlove, cache, browser storage, backup-e i recent-app preview radi curenja.
- Proveri da se brisanje i zatvaranje naloga propagiraju na lokalne podatke, queued rad, fajlove, notifikacije, analytics identifikatore, backend sisteme, export-e i backup-e prema politici.

