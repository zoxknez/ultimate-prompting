## 19. EAS Update i OTA kompatibilnost

### 19.1 Ugovor runtime kompatibilnosti
- Tretiraj native binary i JavaScript update kao nezavisno deploy-ovane artefakte spojene samo eksplicitnim ugovorom runtime kompatibilnosti.
- Popisi runtimeVersion policy, native fingerprint ulaze, update URL, request header-e, kanal, branch, platformu, arhitekturu, okruzenje i embedded update.
- Promeni runtime kompatibilnost kad god to zahteva native kod, native konfiguracija, Hermes kompatibilnost, Codegen schema, native zavisnost, lokalna schema ili privilegovana mogucnost.
- Testiraj novi update na svakom kompatibilnom native binary-ju koji je jos na terenu i dokazi da nekompatibilan binary ne moze da ga primi.
- Testiraj stari embedded update, najnoviji update, rollback update, offline launch, neuspesan download, korumpiran asset, malo prostora i recovery posle ponovljenog crash-a.
- Ne koristi OTA update za native breaking promenu, signing promenu, entitlement promenu, deklaraciju dozvole, store-policy promenu ili ireverzibilnu migraciju podataka.

### 19.2 OTA poverenje, rollout i oporavak
- Proveri autenticnost update manifesta i asset-a, code-signing certificate konfiguraciju, cuvanje privatnog kljuca, key ID, rotaciju, opoziv i offline verifikaciju.
- Eksplicitno mapiraj kanale na branch i okruzenje; spreci da preview, staging, test, tenant ili white-label update stigne do production binary-ja.
- Koristi staged rollout sa velicinom kohorte, guardrail-om, crash pragom, launch pragom, poslovnim metrikama, pause, abort i rollback ovlascenjem.
- Sacuvaj update ID, grupu, kanal, branch, runtimeVersion, commit, poruku, signer-a, manifest, asset-e, source map, actor-a objave i rollout istoriju.
- Definisi automatski oporavak iz crash loop-a i dokazi da fallback ne moze da otvori format podataka koji je neuspesan update nekompatibilno promenio.
- Izvrsi rollback, republish, channel remap, iskljucivanje update-a, hitno native izdanje i forward-fix procedure.

