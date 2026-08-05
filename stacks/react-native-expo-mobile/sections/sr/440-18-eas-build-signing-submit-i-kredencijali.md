## 18. EAS Build, signing, submit i kredencijali

### 18.1 EAS Build reproducibilnost
- Popisi svaki build profil, inheritance lanac, distribution rezim, kanal, okruzenje, image, resource class, cache, izvor kredencijala i tip artefakta.
- Uporedi lokalni, CI i EAS razreseni app config, environment promenljive, tajne, Node, package manager, Android, iOS i native dependency graf.
- Pinuj ili zabelezi build image i toolchain dovoljno za reprodukciju i istragu izdanja; otkrij tihi image drift.
- Auditiraj cache kljuceve i sadrzaj radi cross-branch, cross-environment, cross-tenant, stale-native ili secret leakage-a.
- Build-uj jednom i promovisi isti potpisani artefakt gde distributivni model dozvoljava; ne radi nezavisan rebuild za svako okruzenje bez opravdanja.
- Sacuvaj build URL, identitet posla, commit, razreseni config, native fingerprint, digest artefakta, potpis, simbole, source map i SBOM.

### 18.2 Kredencijali i store submission
- Popisi Android upload key, vlasnistvo app-signing kljuca, backup keystore-a, fingerprint sertifikata, Apple distribution sertifikat, profile, API kljuc i rolu.
- Koristi least privilege, kratkotrajne kredencijale gde je moguce, razdvajanje duznosti, zasticena okruzenja, audit log i hitan opoziv.
- Proveri package name, bundle ID, store aplikaciju, signing lineage, version code, build broj, track, phased release i metadata pre submission-a.
- Ne izlozi kredencijale u logovima, artefaktima, environment dump-u, support bundle-u, pull request-u, shell istoriji ili generisanoj konfiguraciji.
- Testiraj replacement, expiration, revocation, transfer tima, izgubljen kredencijal i proceduru za kompromitovan kredencijal.
- Zahtevaj izricito odobrenje pre submission-a, track promotion-a, promene phased rollout-a, promene store listing-a ili production izdanja.

