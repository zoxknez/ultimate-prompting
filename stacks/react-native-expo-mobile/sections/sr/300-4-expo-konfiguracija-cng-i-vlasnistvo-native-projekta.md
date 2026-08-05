## 4. Expo konfiguracija, CNG i vlasnistvo native projekta

### 4.1 Efektivna Expo konfiguracija
- Razresi dinamicku app konfiguraciju sa tacnim okruzenjem koje koriste lokalni, CI, EAS, preview, production i store build.
- Pregledaj granice javne i privatne konfiguracije i dokazi da nijedna tajna nije ugradjena u JavaScript bundle, manifest, resurse, native stringove ili OTA metadata.
- Uporedi introspected config, generisani Android manifest, Gradle properties, Info.plist, entitlement-e, Podfile properties, URL scheme i associated domain.
- Auditiraj redosled config plugin-a, idempotentnost, resavanje konflikta, dangerous mod-ove, vlasnistvo fajla, uslovne grane i platformsko ponasanje.
- Dokazi da ponovljeni prebuild ne uklanja tiho rucne native izmene, ne duplira unose, ne menja redosled kriticne konfiguracije i ne menja identifikatore.
- Dokumentuj autoritativno mesto za svaku native konfiguracionu vrednost i proceduru regeneracije.

### 4.2 Development build i Expo Go
- Popisi svaku native mogucnost koja nije dostupna ili se drugacije ponasa u Expo Go.
- Koristi development build za custom native kod, config plugin-e, push kredencijale, background mode, universal link, app link i production-like dozvole.
- Odvoji development client meni, debugger, dev server, network security i bundle loading ponasanje od release ponasanja.
- Proveri offline pokretanje i embedded bundle ponasanje bez Metro servera ili dostupnog development racunara.
- Ne zatvaraj native, update, signing, performance, memory ili lifecycle nalaz samo na osnovu Expo Go dokaza.
- Sacuvaj tacan development-build profil i native fingerprint koriscen za svaku reprodukciju.

