## 15. Dozvole, uredjaji, mediji i web povrsine

### 15.1 Dozvole i hardware
- Popisi kameru, mikrofon, fotografije, media library, lokaciju, Bluetooth, nearby devices, kontakte, kalendar, notification, motion, health, NFC, USB i lokalnu mrezu.
- Proveri manifest, Info.plist, entitlement-e, privacy string, config plugin-e, runtime prompt, ogranicen pristup, priblizan pristup i obradu odbijanja.
- Trazi dozvolu samo u korisniku razumljivom trenutku i objasni required, optional, degraded i trajno odbijeno ponasanje.
- Ponovo proveri autorizaciju posle izmene settings-a, OS upgrade-a, restore-a, managed-device pravila, app update-a i promene naloga.
- Auditiraj vlasnistvo hardware resursa, istovremenu upotrebu, interruption, promenu route-a, thermal pritisak, disconnect i cleanup.
- Testiraj fizicke uredjaje kroz podrzane OS verzije, proizvodjace, arhitekture, oblike ekrana, periferije i ogranicene uslove.

### 15.2 Mediji i grafika
- Auditiraj audio focus, interruption, route change, Bluetooth, lock-screen kontrole, background playback, recording, camera session i istovremenu media upotrebu.
- Proveri codec, DRM, subtitle, track, streaming, download, cache, resume i offline-license ponasanje gde je primenljivo.
- Ogranici dimenzije slike, decode memoriju, texture memoriju, frame buffer, prefetch, cache i rast transformisanih asset-a.
- Testiraj backgrounding, prekid pozivom, iskljucen uredjaj, route change, gasenje procesa, malo memorije, thermal throttling i propagaciju native greske.
- Proveri dozvole, secure output, screenshot, screen recording, protected content, privatnost metadata i cleanup privremenog fajla.
- Meri release-mode startup, prvi frame, dropped frame, decode vreme, memoriju, bateriju, mrezu i storage trosak.

### 15.3 WebView, browser i lokalni web sadrzaj
- Popisi sve WebView, authentication browser session, in-app browser, lokalni HTML, custom scheme, injected JavaScript i message bridge.
- Definisi trusted origin, navigation allowlist, popup policy, download policy, mixed-content policy, obradu sertifikata, cookie i storage izolaciju.
- Tretiraj svaku bridge poruku kao nepoverljivu i autorizuj origin, frame, session, tenant, komandu, resurs i payload.
- Spreci zloupotrebu proizvoljnog external URL-a, file URL-a, intent URL-a, JavaScript URL-a, universal-link loop-a i custom scheme-a.
- Testiraj stale stranicu posle logout-a, promene naloga, OTA update-a, native update-a, rotacije sertifikata i restore-a offline cache-a.
- Dokazi da privilegovane native funkcije nisu dostupne iz nepoverljivog, navigiranog, kompromitovanog ili nested sadrzaja.

