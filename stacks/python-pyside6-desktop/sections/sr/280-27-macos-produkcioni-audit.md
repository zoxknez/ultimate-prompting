## 27. macOS produkcioni audit

### 27.1 Obim audita

1. Pregledaj podržane macOS verzije, Intel/Apple Silicon, universal binary-je, deployment target, SDK/Xcode, hardened runtime, sandbox i Rosetta pretpostavke.
2. Pregledaj strukturu app bundle-a, Mach-O arhitekture, load command-e, rpath-ove, framework-e, dylib-ove, Qt plugin-e, resurse, Info.plist, entitlement-e i helper aplikacije.
3. Proceni Developer ID ili App Store signing, redosled potpisivanja nested koda, secure timestamp, notarizaciju, stapling, Gatekeeper, quarantine i designated requirement-e.
4. Pregledaj Keychain access group-e, application group-e, bookmark-e, file access, privacy usage description-e, TCC dozvole, launch agent-e i privilegovane helper-e.
5. Testiraj Retina/high DPI, više ekrana, spaces, full screen, sleep/wake, screen lock, locale/input metode, accessibility i system appearance.
6. Definiši DMG/PKG/store instalaciju, app translocation, update framework, obnovu ključa/sertifikata, rollback i uninstall/data-retention ponašanje.

### 27.2 Obavezna verifikacija

1. Verifikuj svaki nested binary i resource seal nakon finalnog pakovanja i potvrdi notarization acceptance i stapled ticket gde je primenljivo.
2. Testiraj clean download sa quarantine-om, first launch, translocation-sensitive putanje, standard-user rad, permission denial/revocation i drugog macOS korisnika.
3. Vežbaj Intel, Apple Silicon i universal putanje gde su podržane; otkrij slučajne Rosetta-only helper-e ili architecture-mismatched plugin-e.
4. Testiraj TCC prompt-ove, revoked dozvole, zaključan/nedostupan Keychain, sleep/wake, promene ekrana, VoiceOver, locale i IME.
5. Validiraj update i rollback kada aplikacija radi, helper-i su aktivni, data schema se menja, sertifikati rotiraju ili notarization/update servisi padnu.

