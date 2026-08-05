## 23. Observability, crash i operativna spremnost

### 23.1 Telemetrija i symbolication
- Koreliraj logove, trace, metrike, crash report, ANR, hang, native crash, JavaScript gresku, network dogadjaj, background rad i update sa jednim identitetom izdanja.
- Upload-uj i bezbedno sacuvaj odgovarajuci JavaScript source map, Hermes map, Android mapping, native simbole, dSYM i build metadata.
- Rediguj tokene, kredencijale, licne podatke, sadrzaj poruke, putanju fajla, preciznu lokaciju i osetljiv identifikator pre nego sto telemetrija napusti uredjaj.
- Definisi SLI i SLO za crash-free korisnika, crash-free session, ANR ili hang stopu, startup, update uspeh, uspeh kriticnog toka, sync freshness i obradu notification-a.
- Napravi alert sa pragom, prozorom, kohortom, severity-jem, vlasnikom, runbook-om, suppression-om i korelacijom sa release-om ili update-om.
- Proveri da telemetrija radi tokom delimicnog backend outage-a, update greske, authentication greske, offline stanja i crash-loop recovery-ja bez izazivanja dodatne greske.

### 23.2 Runbook i supportability
- Obezbedi runbook za crash spike, ANR spike, update mismatch, signing gresku, store rejection, push gresku, auth outage, sync korupciju i kompromitovanu zavisnost.
- Definisi bezbednu support dijagnostiku sa korisnickim pristankom, redakcijom, ogranicenim retention-om, identitetom verzije i bez izlaganja tajni.
- Dokumentuj kako se utvrdjuje instalirani native build, trenutni update, kanal, okruzenje, account scope, klasa uredjaja, storage schema i pending rad.
- Obezbedi kill switch za rizicne klijentske funkcije, background job, provider-e, native mogucnosti i backend interakcije gde je primenljivo.
- Definisi komunikaciju sa korisnikom, store review ogranicenje, staged mitigaciju, data reconciliation i cuvanje dokaza.
- Izvrsi runbook i zabelezi propuste, vlasnike, rokove i naknadnu verifikaciju.

