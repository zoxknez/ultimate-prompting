## 18. Installer, prodavnica, enterprise, upgrade i uninstall ponasanje

### 18.1 Installer semantika

1. Identifikuj installer tehnologiju, verziju, scope, elevation model, install putanju, data putanju, repair ponasanje, upgrade code/product code/bundle identitet, custom action-e, prerequisite-e i rollback podrsku.
2. Verifikuj cistu instalaciju, same-version repair, patch/minor/major upgrade, odbijanje downgrade-a, side-by-side kanale, per-user u per-machine tranziciju, tranziciju arhitekture i uninstall.
3. Ucini custom action-e minimalnim, deterministickim, logovanim, retry-safe i reverzibilnim. Nikada ne skrivaj proizvoljne network download-e ili shell execution unutar installer-a.
4. Validiraj putanje i dozvole koje installer kreira. Spreci normalne korisnike da zamene executable fajlove, DLL-ove, helper-e, update komponente ili privilegovanu konfiguraciju.
5. Namerno sacuvaj korisnicke podatke, eksplicitno ih migriraj i ukloni ih samo prema dokumentovanom izboru korisnika/enterprise-a.
6. Obradi pokrenute instance aplikacije, tray procese, servise, sidecar-e, zakljucane fajlove, antivirus, reboot-required stanje i prekinutu instalaciju.
7. Verifikuj registraciju i ciscenje protokola, file association-a, shortcut-a, startup entry-ja, servisa, scheduled task-ova, firewall pravila, driver-a i store metadata.
8. Testiraj installer logove i error poruke zbog curenja tajni i upotrebljivog recovery-ja.

### 18.2 Prodavnice i enterprise distribucija

1. Mapiraj Microsoft Store, Mac App Store, Snap/Flatpak prodavnice, package repository-je, MDM, software-distribution alate i direct-download kanale odvojeno.
2. Pregledaj sandbox, entitlement, API, payment, update, telemetry, privacy, age-rating i content pravila za svaki kanal.
3. Koristi channel-specific konfiguraciju umesto runtime nagadjanja. Verifikuj bundle identitet i kontinuitet data putanje izmedju store i direct build-a samo kada je migracija podrzana.
4. Spreci kanal nizeg trust nivoa da nenamerno update-uje ili zameni kanal viseg trust nivoa.
5. Verifikuj offline installer-e, proxy podrsku, deployment sertifikata, WebView/runtime prerequisite-e, silent install switch-eve, exit code-ove, logove i detection pravila za enterprise upotrebu.
6. Dokumentuj vlasnistvo store naloga, publisher organizacija, recovery kontakata, MFA-a, API kljuceva, signing profile-a i emergency pristupa.
7. Testiraj fallback posle store review/rejection-a, pauzu phased release-a, povlacenje paketa, mandatory update ogranicenja i korisnike zaglavljene na starim store verzijama.
8. Osiguraj da release notes, privacy deklaracije, dozvole, data safety i screenshot-ovi odgovaraju stvarnom ponasanju.

