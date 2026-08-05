## 39. Windows-specifičan audit

Proveri Win32 host, paket, signing identitet, instalaciju, protocol handling i update putanju.

- Audituj CMake, Visual Studio workload, MSVC/runtime, Windows SDK, arhitekturu, runner kod, plugin-e, generated registrant, native DLL-ove i build konfiguraciju.
- Proveri identitet aplikacije, package family, publisher-a, AppUserModelID, MSIX ili installer metapodatke, install scope, elevation, per-user/per-machine ponašanje i repair/uninstall.
- Audituj Authenticode sertifikat, timestamp, nested binarne fajlove, DLL search, side-loading, SmartScreen reputaciju, obnovu sertifikata, opoziv i čuvanje ključa.
- Proveri protocol/file association-e, command-line argumente, single-instance ponašanje, više prozora, toast aktivaciju, startup task-ove, drag/drop, clipboard i eksterne procese.
- Testiraj DPI scaling, više monitora, remote desktop, high contrast, screen reader-e, tastaturu, IME, touch, tablet mode, sleep/resume, lock/unlock i fast user switching.
- Audituj lokalne fajlove, registry, credential storage, ACL-ove, privremene putanje, symlink/reparse point-e, roaming podatke, backup i enterprise politiku.
- Pregledaj atomicnost update-a, zamenu aktivnog fajla, potrebu za reboot-om, downgrade, promenu kanala, rollback, čišćenje starih shortcut-a i očuvanje korisničkih podataka.
- Testiraj Windows verzije, arhitekture, clean install, upgrade, repair, uninstall, restricted user-a, offline install, antivirus interakciju i malo diska.

