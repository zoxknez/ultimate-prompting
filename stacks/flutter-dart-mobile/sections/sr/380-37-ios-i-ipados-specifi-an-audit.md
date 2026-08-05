## 37. iOS i iPadOS-specifičan audit

Proveri Flutter, Runner/native host-ove, extension-e, entitlement-e, potpisivanje i App Store ponašanje zajedno.

- Audituj Xcode project/workspace, build settings, konfiguracije, scheme-ove, deployment target-e, Swift/Objective-C kod, pod/package zavisnosti, skripte, arhitekture i generisana podešavanja.
- Pregledaj AppDelegate, SceneDelegate/UIScene konfiguraciju, FlutterEngine integraciju, više scene/prozora, restoration, deep link-ove, universal link-ove i add-to-app lifecycle.
- Proveri Info.plist purpose stringove, entitlement-e, capability-je, privacy manifest-e, required-reason API-je, ATS, associated domain-e, keychain group-e, app group-e i extension-e.
- Audituj background mode-ove, BGTaskScheduler, silent push, notification extension-e, audio/location/Bluetooth ponašanje, suspenziju procesa, terminaciju i user force-quit semantiku.
- Proveri data protection class, keychain accessibility, backup/restore, iCloud ponašanje, fajlove, pasteboard, screenshot-e, screen recording i dostupnost protected podataka.
- Pregledaj signing sertifikate, provisioning profile-e, team/bundle ID-jeve, App Store Connect uloge, TestFlight grupe, export opcije, archive, dSYM, upload simbola i istek sertifikata.
- Testiraj iPhone i iPad klase uređaja, orijentacije, multitasking, eksternu tastaturu, pointer, Stage Manager, memory pressure, accessibility, upgrade, restore i stare/nove OS verzije.
- Pregledaj App Store privacy, tracking, subscription/payment, brisanje naloga, review, export compliance, encryption deklaracije i phased release zahteve.

