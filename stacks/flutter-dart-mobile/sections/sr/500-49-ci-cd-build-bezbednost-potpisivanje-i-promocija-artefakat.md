## 49. CI/CD, build bezbednost, potpisivanje i promocija artefakata

Release pipeline je deo bezbednosne granice aplikacije.

- Mapiraj dozvole repozitorijuma, branch protection, code review, CI trigger-e, fork ponašanje, environment-e, odobrenja, runner trust, cache, artefakte, tajne i deployment identitete.
- Pin-uj action-e, image-e, SDK arhive, package index-e, native zavisnosti i alate po immutable verziji ili digest-u gde je moguće; proveri provenance.
- Spreči nepoverljive pull request-ove, build skripte, testove, generatore, dependency hook-ove ili artifact upload-e da pristupe signing ključevima, store kredencijalima, production tokenima ili privilegovanim runner-ima.
- Preferiraj kratkotrajni workload identity i zaštićene signing servise; definiši čuvanje, pristup, quorum, audit, backup, rotaciju, istek, opoziv i disaster recovery ključeva.
- Build-uj jednom iz identifikovanog commit-a, zadrži immutable artefakte, skeniraj i potpiši tačne bajtove, promoviši isti artefakt i spreči environment-specific rebuild-ove.
- Generiši checksum-e, SBOM, provenance, dependency inventar, simbole, source map-e, release note, efektivnu konfiguraciju, test dokaze i zapis odobrenja po artefaktu.
- Proveri finalne potpise, entitlement-e, dozvole, manifest-e, identitete, verzije, native biblioteke, asset-e, simbole i store/install metapodatke nakon svih transformacija.
- Zaštiti retention artefakata i rollback kandidate od brisanja ili mutacije dok release i incident politika ne dozvole cleanup.
- Testiraj istek ključa, opozvan kredencijal, nedostupan store, neuspešno potpisivanje, parcijalni upload, pogrešan artefakt, duplu verziju, otkazan release i emergency release putanju.

