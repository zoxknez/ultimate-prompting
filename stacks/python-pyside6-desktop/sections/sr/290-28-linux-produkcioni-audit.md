## 28. Linux produkcioni audit

### 28.1 Obim audita

1. Pregledaj podržane distribucije, glibc/musl baseline, x86_64/ARM64, desktop environment-e, Wayland/X11, grafičke driver-e, portal-e i pretpostavke sistemskih biblioteka.
2. Pregledaj ELF arhitekturu, interpreter, RPATH/RUNPATH, bundled/shared biblioteke, symbol verzije, Qt plugin-e, platform teme, codec-e i licencne obaveze.
3. Proceni AppImage, Flatpak, Snap, deb, rpm, tarball, distribution repository, system package i portable deployment ponašanje.
4. Pregledaj filesystem dozvole, XDG putanje, Secret Service/KWallet, D-Bus, Unix socket-e, udev pravila, systemd unit-e, polkit, sandbox dozvole i multi-user izolaciju.
5. Testiraj Wayland i X11, više desktop environment-a, fractional scaling, remote sesije, screen lock, sleep/resume, accessibility, input metode i headless kvar.
6. Definiši potpisivanje repository-ja, package update-e, delta ponašanje, rollback, uklanjanje zavisnosti, uninstall i zadržane podatke.

### 28.2 Obavezna verifikacija

1. Pokreni dependency i symbol inspekciju finalnog artefakta i launch na minimalnim podržanim čistim distribution image-ovima.
2. Testiraj nedostajuće opcione biblioteke, stare driver-e, Wayland/X11 switching, portal denial, sandbox restrikcije i read-only ili noexec lokacije.
3. Verifikuj package/repository potpise, update metadata, mapiranje arhitekture, downgrade ponašanje i cross-package-manager konflikte.
4. Vežbaj standard-user rad, drugog korisnika, zaključan secret store, system sleep, promene ekrana, screen reader-e, locale i IME.
5. Potvrdi da uninstall uklanja integracije i helper-e bez brisanja korisničkih podataka izvan dokumentovane politike.

