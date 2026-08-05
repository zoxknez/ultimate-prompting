## 24. Faza S - Bezbedna Popravka I Verifikacija

1. Popravi root cause, a ne samo vidljivi simptom.
2. Napravi najmanju odbranjivu izmenu koja zatvara potvrdjeni rizik.
3. Dodaj ili unapredi fokusirani regression test pre ili zajedno sa svakom materijalnom popravkom.
4. Izbegavaj nepovezano formatiranje, mass rename, dependency churn i architecture rewrite.
5. Sacuvaj public API, seme, application ID, signing, korisnicke podatke i ponasanje osim ako odobrena popravka zahteva izmenu.
6. Za migracije napravi backup reprezentativnih podataka i testiraj svaki podrzani upgrade put.
7. Prvo ponovo pokreni originalnu reprodukciju i najuze pogodjene testove.
8. Zatim pokreni relevantne module, variant, lint, unit, instrumented, release, R8, native i device provere.
9. Proveri negative i failure putanje, a ne samo happy path.
10. Zabelezi izmenjene fajlove, rationale, komande, rezultate, artefakte, rollback i preostali rizik.
11. Ponovo proveri release ponasanje i production-equivalent konfiguraciju.
12. Unapredi dokumentaciju, runbook, baseline, test matricu i release checklist.

