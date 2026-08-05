## 16. Auto-update, release kanali, rollback i opoziv

### 16.1 Zajednicki update trust model

1. Mapiraj ko moze da build-uje, potpisuje, objavljuje, menja metadata, menja endpoint-e, promovise kanale, pokrene rollout, pauzira rollout, forsira update, dozvoli downgrade i opozove izdanje.
2. Odvoji identitet artefakta, transport security, authenticnost metadata, artifact signature, platform code signature, channel politiku i installer autorizaciju. Svaka kontrola resava drugaciji problem.
3. Koristi nepromenljive versioned artefakte. Nikada ne menjaj bajtove na postojecem version URL-u nakon izdanja.
4. Vezi metadata za tacan proizvod, kanal, platformu, arhitekturu, verziju, minimum/current version pravila, artifact hash ili potpis, velicinu, vreme objave i rollout politiku.
5. Validiraj update metadata kao nepoverljiv mrezni ulaz. Ogranici velicinu i polja, odbij nepoznata platform mapiranja gde su opasna i obradi clock skew.
6. Po default-u spreci downgrade i cross-channel confusion. Ako kontrolisani rollback zahteva downgrade, definisi eksplicitno ovlascenje, compatibility provere, ponasanje migracije korisnickih podataka i ponovni upgrade.
7. Koristi staged rollout sa telemetrijom, minimalnim uzorkom, soak periodom, crash/startup/update/error pragovima, rucnom pauzom, automatskim abort-om i vlasnikom.
8. Definisi ponasanje za offline korisnike, preskocene verzije, veoma stare klijente, nepodrzan OS, nepodrzanu arhitekturu, proxy/captive portal, metered mrezu, malo diska i prekinut download.
9. Verifikuj full i differential update put nezavisno. Delta update ne sme zaobici integrity, signing ili package-content provere.
10. Testiraj update sa svake podrzane izvorne verzije na kandidat, ne samo candidate-to-candidate ili cistu instalaciju.
11. Definisi rollback za application kod, lokalne podatke/semu, sidecar-e/servise, protokole, file association-e, konfiguraciju i cache-irano frontend stanje.
12. Odrzavaj kill switch ili mehanizam iskljucenja kanala koji sam ne stvara neautentifikovanu remote-control putanju.
13. Definisi response na kompromitaciju sertifikata/kljuceva: zamrzni publishing, opozovi ili ukloni poverenje, rotiraj kljuceve gde arhitektura dozvoljava, izdaj pouzdanu zamenu i komuniciraj oporavak.
14. Sacuvaj update logove i artefakte potrebne za incident istragu bez belezenja tajni.

### 16.2 Electron updater audit

1. Identifikuj updater implementaciju: ugradjeni `autoUpdater`, `update-electron-app`, Electron Forge publisher/update servis, Electron Builder updater, custom updater, store updater ili eksterni enterprise alat.
2. Verifikuj podrsku platforme i paketa za tacan updater. Ugradjeno ponasanje se razlikuje izmedju macOS-a, Squirrel.Windows-a, MSIX-a i Linux pakovanja; ne pretpostavljaj da jedan API daje identicnu cross-platform semantiku.
3. Na macOS-u verifikuj code signing, notarizaciju gde je potrebna, application identity, feed format, signature ponasanje i kompatibilnost hardened runtime-a/entitlement-a.
4. Na Windows-u verifikuj Squirrel/MSIX/NSIS/custom installer ponasanje, application user model ID, per-user/per-machine scope, update lock-ove, pokrenute instance i interakciju sa repair/uninstall tokom.
5. Zastiti se od duplih update provera i download-a. Osiguraj da UI radnje, timer-i, startup provere, reconnect i vise prozora ne pokrecu konkurentne update-e.
6. Validiraj feed URL i izbor kanala. Spreci renderer-kontrolisane proizvoljne feed URL-ove ili release kanale osim kada su strogo autorizovani.
7. Verifikuj `checkForUpdates`, download, cancellation, progress, ready stanje, quit-and-install, restart i error tranzicije kao jednu eksplicitnu state machine-u.
8. Ne instaliraj dok su kriticni write-ovi, migracije, export-i, snimanja, device operacije ili nepovratni job-ovi aktivni osim ako operacija moze bezbedno da se nastavi.
9. Verifikuj code-signature provere i package verifikaciju na finalnom distribution putu. Testiraj izmenjene metadata, izmenjen paket, pogresnog publisher-a, pogresan kanal, pogresnu arhitekturu i istekao/opozvan sertifikat.
10. Testiraj cistu instalaciju, normalan update, preskocene verzije, veoma star klijent, update dok aplikacija radi u tray-u, vise instanci, prekinut download, malo diska, zakljucan fajl, antivirus interference i forced shutdown.

### 16.3 Tauri updater audit

1. Razresi tacnu verziju updater plugin-a, Rust i JavaScript API verzije, capabilities, permissions, javni kljuc, endpoint konfiguraciju, install mode i platform podrsku.
2. Verifikuj da su update potpisi obavezni i provereni prema nameravanom pinovanom javnom kljucu. Zastiti privatni signing kljuc odvojeno od platform code-signing kljuceva.
3. Ogranici frontend updater dozvole. Prozor koji sme da proveri dostupnost ne mora automatski da ima download ili install ovlascenje.
4. Validiraj static JSON ili dynamic server metadata, ukljucujuci RFC 3339 datum ako se koristi, semantic verziju, platform key, arhitekturu, sadrzaj potpisa, URL, velicinu i release notes.
5. Verifikuj da runtime endpoint i header override-i ne mogu biti pod uticajem nepoverljivog renderer sadrzaja ili konfiguracije nizeg trust nivoa.
6. Testiraj Windows install mode-ove, elevation prompt-ove, restart ponasanje, pokrenute sidecar-e/servise i per-user/per-machine konzistentnost.
7. Testiraj Linux package-specific ponasanje umesto tretiranja AppImage, Debian, RPM, Flatpak, Snap i distribution repository-ja kao zamenljivih.
8. Testiraj macOS app bundle identitet, signing, notarizaciju, quarantine, update replacement i rollback ponasanje.
9. Ako custom version comparison dozvoljava rollback, zahtevaj autentifikovanu rollback odluku, data compatibility gate, eksplicitnu telemetriju i plan vracanja korisnika na bezbednu forward verziju.
10. Testiraj los potpis, nedostajuci potpis, pogresan kljuc, izmenjen paket, pogresan OS/architecture key, server error, partial download, malo diska, odbijenu dozvolu, prekinutu instalaciju i star klijent.

