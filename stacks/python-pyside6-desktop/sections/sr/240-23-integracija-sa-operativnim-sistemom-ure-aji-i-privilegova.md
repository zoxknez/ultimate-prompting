## 23. Integracija sa operativnim sistemom, uređaji i privilegovani helper-i

### 23.1 Obim audita

1. Inventariši file association-e, URL schema-e, deep link-ove, autostart, tray, notifikacije, global shortcut-e, clipboard, drag/drop, recent fajlove, shell integraciju i single-instance ponašanje.
2. Pregledaj kameru, mikrofon, screen capture, lokaciju, Bluetooth, USB, serial, HID, smart card, štampanje, skenere, media key-eve i druge device dozvole.
3. Mapiraj servise, daemon-e, scheduled task-ove, driver-e, kernel ekstenzije, privilegovane helper-e, elevation prompt-ove i installer custom action-e.
4. Validiraj sve OS-isporučene ulaze: command line, environment, file-open event-e, URL-ove, notification akcije, clipboard, drag/drop, device podatke i registry/plist vrednosti.
5. Proceni same-user process impersonation, symlink/junction napade, TOCTOU, nebezbedne privremene fajlove, nasleđene dozvole i writable service/helper putanje.
6. Definiši disconnect, reconnect, permission denial, uklanjanje uređaja, sleep/resume, fast user switching, remote desktop i OS update ponašanje.

### 23.2 Obavezna verifikacija

1. Fuzz-uj deep link-ove, file association-e, notification akcije, clipboard, drag/drop, command-line argumente i device payload-e malformed i oversized ulazom.
2. Testiraj least-privilege rad kao standardni korisnik i verifikuj eksplicitnu, usku elevaciju samo gde je potrebna.
3. Verifikuj helper identitet, potpis, version handshake, request autorizaciju, ACL-ove, installation putanju, update redosled, rollback i odgovor na kompromitovan helper.
4. Vežbaj permission denied, revoked dozvolu, nedostupan uređaj, zamenu uređaja, sleep/resume, session lock, promenu korisnika i shutdown.
5. Potvrdi da uninstall uklanja ili namerno zadržava servise, task-ove, driver-e, association-e, dozvole i podatke prema dokumentovanoj politici.

