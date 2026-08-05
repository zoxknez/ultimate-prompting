## 26. Windows produkcioni audit

### 26.1 Obim audita

1. Pregledaj podržane Windows verzije, x64/ARM64, MSVC runtime, Universal CRT, WebView/grafičke zavisnosti, DPI awareness i pretpostavke code page-a.
2. Pregledaj PE import-e, manifest-e, Authenticode, timestamp, catalog/signature chain, redosled DLL pretrage, side-by-side assembly-je i zapakovane Qt platform plugin-e.
3. Proceni MSI/MSIX/EXE/portable installer ponašanje, per-user naspram per-machine scope-a, UAC, registry, servise, scheduled task-ove, firewall, file association-e i repair.
4. Pregledaj DPAPI, Credential Manager, ACL-ove, junction-e, reparse point-e, named pipe-ove, AppData/ProgramData/Program Files lokacije i multi-user izolaciju.
5. Testiraj high DPI, više monitora, Remote Desktop, session lock, fast user switching, sleep/resume, dark mode, input metode i accessibility alate.
6. Definiši SmartScreen reputation, obnovu sertifikata, enterprise deployment, antivirus/EDR interakciju, update, rollback i uninstall podršku.

### 26.2 Obavezna verifikacija

1. Verifikuj finalni instalirani executable i svaki isporučeni DLL/plugin trusted inspekcionim alatima i validacijom signature chain-a.
2. Pokreni iz adversarial working direktorijuma i sa izmenjenim PATH-om radi otkrivanja DLL ili executable hijacking-a.
3. Testiraj standard-user install/use/update/uninstall, elevation granice, drugog OS korisnika, roaming/non-roaming profile-e i zaključane fajlove.
4. Vežbaj kombinacije skaliranja ekrana, uklanjanje monitora, RDP reconnect, graphics fallback, accessibility, locale i IME scenarije.
5. Validiraj update i rollback kroz obnovu sertifikata, fajlove koji zahtevaju reboot, aktivne helper procese i enterprise security softver.

