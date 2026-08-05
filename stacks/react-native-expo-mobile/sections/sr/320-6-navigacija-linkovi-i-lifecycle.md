## 6. Navigacija, linkovi i lifecycle

### 6.1 Navigacija i restoration
- Popisi Expo Router, React Navigation, native navigaciju, custom routing, modal route, tab, stack, drawer i nested state.
- Validiraj route parametre u runtime-u i nikada ne tretiraj TypeScript route tipove kao validaciju ili autorizaciju.
- Testiraj cold start, warm start, background resume, killed-process restore, otvaranje notification-a, universal link, app link, custom scheme i web URL ulaz.
- Dokazi da protected route ponovo procenjuje session, tenant, resource ownership i feature entitlement posle restore-a i obrade linka.
- Auditiraj duplu navigaciju, stale navigation reference, back ponasanje, modal dismissal, predictive back, persistence stanja i versioned route migracije.
- Testiraj stare linkove sa novim binary-jem i OTA update-om i definisi bezbednu obradu uklonjenih ili preimenovanih ruta.

### 6.2 Lifecycle aplikacije i gasenje procesa
- Modeluj active, inactive, background, suspended, terminated, restored, locked-device, low-memory i interrupted stanje po platformi.
- Ne pretpostavljaj da se cleanup izvrsava pre gasenja procesa, OS eviction-a, crash-a, force-stop-a, gubitka baterije ili reboot-a uredjaja.
- Persistiraj samo minimalno obnovljivo stanje i validiraj svaku restore vrednost prema trenutnom identitetu, schemi, dozvolama i serverskoj istini.
- Testiraj prekinutu autentikaciju, placanje, upload, download, media, migraciju, sync i background operaciju na svakoj durable granici.
- Auditiraj registraciju i uklanjanje listener-a kroz Fast Refresh, navigaciju, foreground tranziciju, OTA reload, native restart i logout.
- Definisi reconciliation posle nejasnog zavrsetka kada klijent ne moze da zna da li je backend commit-ovao operaciju.

