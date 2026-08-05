## 23. Faza S - Bezbedna Popravka I Verifikacija

1. Popravljaj root cause, a ne samo wording prompta ili vidljiv simptom.
2. Napravi najmanju odbranjivu izmenu koja zatvara potvrdjeni rizik.
3. Dodaj fokusirani regression test pre ili zajedno sa svakom materijalnom popravkom.
4. Ne radi masovni model, provider, framework ili dependency upgrade kao genericko resenje.
5. Ne brisi lockfile-ove, eval istoriju, traces, dataset-e ili index-e da bi sakrio failure.
6. Ponovo pokreni relevantne unit, integration, adversarial, retrieval, trajectory i end-to-end testove.
7. Proveri negativne slucajeve i failure putanje, a ne samo happy path.
8. Zabelezi promenjene fajlove, konfiguraciju, migracije, provider podesavanja, komande, rezultate i rollback.
9. Ponovo pokreni originalnu reprodukciju i dokazi da je problem popravljen ili contained.
10. Azuriraj dokumentaciju, runbook-e, prompt verzije i eval baseline-e.

