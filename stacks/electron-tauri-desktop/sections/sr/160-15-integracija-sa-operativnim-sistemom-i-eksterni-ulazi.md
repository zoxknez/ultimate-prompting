## 15. Integracija sa operativnim sistemom i eksterni ulazi

### 15.1 Deep link-ovi, protocol handler-i, file association-i i CLI

1. Popisi custom URI scheme, app link-ove, universal link-ove, file association-e, open-with handler-e, shell verb-ove, context-menu entry-je, command-line switch-eve, startup argumente i store activation payload-e.
2. Tretiraj svaki payload kao nepoverljiv. Parsiraj strukturno, ograniči velicinu/broj, kanonikalizuj putanje/URL-ove, zahtevaj ocekivane tipove radnji i odbij nepoznata polja i scheme.
3. Zastiti authentication callback-e pomocu state-a, nonce-a, PKCE-a, ocekivanog issuer-a, account binding-a, jednokratne upotrebe i expiry-ja.
4. Spreci argument, shell, URL, path i template injection pri prosledjivanju payload-a postojecoj instanci ili helper-u.
5. Definisi ponasanje pre nego sto je aplikacija spremna, tokom update-a, sa vise instanci, bez prijavljenog naloga i posle promene naloga.
6. Ne izvrsavaj niti automatski otvaraj sadrzaj samo zato sto ga je OS povezao sa aplikacijom.
7. Registruj i uklanjaj integracije konzistentno kroz cistu instalaciju, per-user/per-machine install, upgrade, repair, portable mode, store install, koegzistenciju kanala i uninstall.
8. Testiraj malformed encoding, ogroman payload, duplu aktivaciju, nested URL, local-file URL, alternativnu scheme, stale nalog i istovremene aktivacije.

### 15.2 Tray, meniji, shortcut-i, clipboard, notification-i i autostart

1. Mapiraj svaku tray/menu/global-shortcut/notification radnju na autorizovanu komandu i trenutno account/window stanje.
2. Ne veruj menu ID-ju, notification payload-u ili global shortcut event-u kao dokazu korisnickog identiteta ili namere.
3. Spreci duple registracije i stale handler-e kroz reload, update, promenu naloga, promenu ekrana, sleep/wake i vise instanci.
4. Minimizuj izlaganje osetljivih podataka u clipboard-u; cisti ga samo uz pazljivu ownership logiku i nikada ne unistavaj nepovezan korisnicki clipboard sadrzaj.
5. Sanitizuj notification sadrzaj i radnje. Izbegavaj prikaz tajni na lock screen-u i validiraj activation payload-e.
6. Opravdaj autostart, background mode, login-item helper-e, scheduled task-ove, servise i startup registry/plist entry-je. Obezbedi vidljivu korisnicku kontrolu i uklanjanje.
7. Verifikuj pristupacnost i keyboard navigaciju native menija, tray tokova, dialog-a i shortcut-a, ukljucujuci konflikte i lokalizovane label-e.
8. Testiraj odbijenu OS dozvolu, opozvanu dozvolu, promenjenu default aplikaciju, stale notification, shortcut konflikt, vise monitora, zakljucanu session-u i OS restart.

### 15.3 Uredjaji, media, screen capture, stampa i hardver

1. Popisi koriscenje kamere, mikrofona, display capture-a, audio output-a, USB-a, serial-a, HID-a, Bluetooth-a, smart card-a, stampaca, skenera, GPU-a, codec-a i custom driver-a.
2. Trazi minimalnu OS i web dozvolu u trenutku potrebe, objasni svrhu, obradi odbijanje i podrzi opoziv.
3. Autorizuj izbor uredjaja i operacije prema trenutnom korisniku/nalogu i poslovnoj politici; prisustvo uredjaja nije autorizacija.
4. Validiraj device descriptor-e i duzine podataka. Ogranici stream-ove, frame velicine, sample rate-ove, buffer-e, trajanje snimanja i storage.
5. Spreci nenamerno background snimanje posle zatvaranja prozora, logout-a, sleep-a, lock-a, promene naloga ili opoziva dozvole.
6. Audituj izbor screen-capture izvora i spreci tiho snimanje osetljivih prozora gde politika to zahteva.
7. Tretiraj nazive stampaca, putanje, page settings, media fajlove, codec-e i odgovore firmware-a uredjaja kao nepoverljive ulaze.
8. Testiraj uklanjanje uredjaja, odbijanje dozvole, partial frame-ove, malformed podatke, driver crash, hotplug storm, sleep/wake, vise uredjaja i update tokom aktivne upotrebe.

