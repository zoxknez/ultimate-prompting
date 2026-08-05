## 24. CI/CD, provenance, rollout i oporavak

### 24.1 CI/CD trust boundary
- Mapiraj dozvole repozitorijuma, branch protection, pull-request trust, fork ponasanje, workflow dozvole, runner-e, cache, artefakte, OIDC, tajne i deployment odobrenja.
- Spreci da nepoverljivi pull-request kod pristupi signing kredencijalima, update kljucevima, production tokenima, store API-jima, privatnim paketima ili zasticenom cache-u.
- Pinuj ili verifikuj action-e, build image, package manager, toolchain, preuzete binarne fajlove, native zavisnosti i udaljene skripte.
- Zahtevaj cist checkout, immutable zavisnosti, testove, release build, pregled artefakta, SBOM, provenance, potpise i approval gate.
- Razdvoji dozvole za build, signing, submission, OTA objavu, mapiranje kanala i production rollout.
- Sacuvaj immutable dokaz koji povezuje actor-a, workflow, source, okruzenje, artefakt, potpis, store submission, update objavu i rollout odluku.

### 24.2 Rollout, abort, rollback i forward fix
- Definisi rollout kohortu, platformu, uredjaj, OS, verziju aplikacije, native runtime, update kanal, tenant, geografiju, feature flag i monitoring prozor.
- Postavi kvantitativne guardrail-e za crash, ANR, startup, update uspeh, kriticni tok, auth, sync, bateriju, backend gresku i obim podrske.
- Dodeli ovlascenje za pause, abort, OTA rollback, zaustavljanje store rollout-a, iskljucenje funkcije, zaustavljanje background rada, opoziv kredencijala i pokretanje incident rezima.
- Odvoji JavaScript rollback, native binary rollback, configuration rollback, backend rollback, data rollback, reconciliation i forward repair.
- Dokazi da stari i novi binary, stari i novi update, stari i novi backend ugovor i stara i nova lokalna schema mogu koegzistirati potreban period.
- Nikada ne oznaci rollback spremnim dok nije izvrsen sa reprezentativnim podacima, instaliranim verzijama, kanalima i failure stanjima.

### 24.3 Backup, restore i incident recovery
- Popisi obnovljive serverske podatke, klijentske podatke, update metadata, simbole, source map, signing zapis, store zapis, konfiguraciju i audit dokaz.
- Definisi RPO i RTO po kriticnom toku i proveri ih izolovanom restore i reconciliation vezbom.
- Testiraj oporavak od korumpiranih lokalnih podataka, loseg OTA update-a, loseg native izdanja, izgubljenog signing kredencijala, opozvanog sertifikata, backend restore-a i nekompatibilne scheme.
- Sacuvaj forenzicki dokaz pre brisanja cache-a, uninstall-a, republish-a, rotacije kljuceva, rebuild-a ili restore-a.
- Kod supply-chain kompromitacije uradi rebuild iz trusted source-a, cistih runner-a, verifikovanih zavisnosti, novoizdatih kredencijala i pregledanih artefakata.
- Dokumentuj containment, eradication, recovery, uticaj na korisnika, obavezu obavestavanja, preostali rizik i sprecavanje ponavljanja.

