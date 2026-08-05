## 17. Code signing, notarizacija, kljucevi i poverenje artefakta

### 17.1 Signing arhitektura

1. Popisi svaki signing identitet i svrhu: Windows executable/installer, macOS aplikaciju/installer, Apple notarization kredencijale, Linux pakete, Tauri updater, store upload, mobile target-e i interno enterprise potpisivanje.
2. Koristi odvojene kljuceve gde threat model ili tooling zahtevaju separaciju. Dokumentuj koja kompromitacija pogadja koji kanal i kako se poverenje moze obnoviti.
3. Cuvaj privatne kljuceve u hardware-backed ili managed signing sistemima gde je prakticno. Ogranici export, interaktivnu upotrebu, CI pristup, uloge, odobrenja, IP/mrezu, repozitorijum, granu i okruzenje.
4. Koristi timestamping gde platform politika to podrzava da validna izdanja prezive istek sertifikata. Verifikuj timestamp authority i failure ponasanje.
5. Zabelezi certificate subject, issuer, serial/thumbprint, vazenje, key algoritam, timestamp, entitlement-e, hardened-runtime stanje, notarization rezultat i tacan hash artefakta bez izlaganja privatnog materijala.
6. Verifikuj potpise posle svih packaging, fuse, resource, installer i update transformacija. Nikada tiho ne menjaj potpisan artefakt.
7. Definisi overlap obnove sertifikata, opoziv, response na izgubljen kljuc, ponasanje isteklog sertifikata, kontinuitet publisher identiteta i emergency release procedure.
8. Odvoji signing od publishing-a tako da potpisan artefakt i dalje zahteva pregledanu promociju u kanal.
9. Audituj ko moze da posalje proizvoljne bajtove signing servisu. Zasticen kljuc nije dovoljan ako nepoverljivi job-ovi mogu traziti potpise.
10. Verifikuj lokalnu proveru potpisa i store/platform verifikaciju na cistim masinama, ne samo unutar CI-ja.

### 17.2 macOS signing, hardened runtime, entitlement-i i notarizacija

1. Verifikuj bundle identifier, team ID, tip sertifikata, designated requirement, potpise nested koda, framework-e, helper-e, login item-e, XPC/servise, sidecar-e i installer image-e.
2. Koristi minimalne entitlement-e. Opravdaj JIT, unsigned executable memory, iskljucenu library validation, automation, kameru, mikrofon, screen recording, fajlove, mrezu, keychain group-e i sandbox izuzetke.
3. Osiguraj da je svaki nested executable i framework potpisan pravilnim redosledom sa kompatibilnim entitlement-ima pre spoljnog bundle-a.
4. Pokreni strogu signature verifikaciju i proceni Gatekeeper ponasanje na cistom preuzetom artefaktu sa quarantine metadata.
5. Posalji tacan release artefakt na notarizaciju, verifikuj uspeh, staple-uj gde je primenljivo i potvrdi offline/online Gatekeeper ponasanje.
6. Testiraj direct download, DMG/PKG, App Store build gde je primenljivo, update replacement, helper launch, first run, permission prompt-ove i razlike OS verzija.
7. Definisi ponasanje kada notarizacija nije dostupna, kasni, odbijena je ili naknadno invalidirana. Ne izdaji neverifikovanu zamenu.
8. Sacuvaj notarization logove i submission ID-jeve vezane za hash-eve artefakta za incident response.

### 17.3 Windows signing i reputacija

1. Verifikuj Authenticode potpise na executable-ima, DLL-ovima, installer-ima, update paketima, driver/helper fajlovima i catalog fajlovima gde je primenljivo.
2. Koristi nameravani publisher identitet konzistentno kroz izdanja da sacuvas upgrade trust i reputaciju. Dokumentuj obnovu sertifikata i promene organizacije.
3. Timestamp-uj potpise i verifikuj i signature i timestamp chain na cistim podrzanim Windows verzijama.
4. Audituj EV/standard certificate ili managed-signing workflow, HSM/Key Vault pristup, sign-command argumente, digest algoritam, potrebu za dual-signing-om i cross-signing pretpostavke.
5. Verifikuj SmartScreen/Mark-of-the-Web ponasanje za direct download i kako se reputacija prati bez slabljenja korisnicke zastite.
6. Osiguraj da unsigned ili drugacije potpisani child binary fajlovi ne mogu da se ucitaju iz writable direktorijuma ili slucajno spakuju.
7. Testiraj install, repair, update, rollback, uninstall, side-by-side kanale, per-user/per-machine scope, UAC, zakljucane fajlove, antivirus i enterprise policy.
8. Definisi response na kompromitovane publisher kredencijale, opozvan sertifikat, false-positive malware klasifikaciju i suspenziju prodavnice.

### 17.4 Linux package signing i repository poverenje

1. Identifikuj svaki format distribucije i trust model: AppImage, Debian, RPM, Flatpak, Snap, AUR/source paket, tarball ili managed enterprise repository.
2. Verifikuj package/repository potpise, expiry metadata, distribuciju kljuceva, rotaciju, opoziv, poverenje mirror-a i vlasnistvo update-a.
3. Audituj desktop fajlove, MIME handler-e, ikone, AppStream metadata, sandbox dozvole, portal-e, systemd unit-e, polkit pravila, post-install script-e i uninstall script-e.
4. Ne tretiraj potpisan paket kao univerzalno pouzdan kroz distribucije. Testiraj tacan repository, store ili direct-download put.
5. Verifikuj library dependency-je i minimalne verzije distribucije na cistim podrzanim okruzenjima, ukljucujuci WebKitGTK i sistemske runtime zahteve za Tauri.
6. Testiraj install, upgrade, downgrade, rollback, package-manager conflict, read-only filesystem, sandbox portal-e, nedostajuce dependency-je i offline enterprise mirror-e.
7. Definisi kako direct-download korisnici dobijaju security update-e kada ne postoji ugradjeni updater ili kada distribution politika upravlja update-ima.
8. Dokumentuj response na kompromitaciju kljuca i preuzimanje repository-ja.

