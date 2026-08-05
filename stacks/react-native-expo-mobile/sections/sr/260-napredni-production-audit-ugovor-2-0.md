## Napredni production audit ugovor 2.0
Auditiraj aplikaciju kao distribuirani proizvod ciji JavaScript, native binarni fajlovi, generisani projekti, backend ugovori, store stanje, OTA stanje, stanje uredjaja i lokalni podaci mogu nezavisno da evoluiraju. Zeleni Metro, Expo Go, simulator build ili EAS posao nisu production dokaz.

### Nivoi dokaza
| Nivo | Znacenje | Najvisa dozvoljena tvrdnja |
| --- | --- | --- |
| E0 | Pretpostavka, secanje ili nedokumentovana izjava | Ne predstavljaj kao cinjenicu |
| E1 | Pregled source koda ili konfiguracije | Poznata je deklarisana namera |
| E2 | Razresene zavisnosti, generisani projekat, build graf ili staticki dokaz artefakta | Poznati su efektivni build ulazi |
| E3 | Ciljani automatizovani test ili kontrolisana reprodukcija | Poznato je testirano ponasanje pod navedenim uslovima |
| E4 | Potpisan release artefakt instaliran i proveren na reprezentativnom fizickom uredjaju | Poznato je release ponasanje za tu celiju matrice |
| E5 | Production telemetrija, kontrolisan rollout, rollback, restore ili incident vezba | Dokazani su operativno ponasanje i oporavak |

### Obavezni zapis nalaza
| Polje | Obavezni sadrzaj |
| --- | --- |
| Identifikator | Stabilan ID kao RN-P0-001 |
| Status | CONFIRMED, PARTIALLY_CONFIRMED, UNVERIFIED, NOT_APPLICABLE ili REJECTED |
| Dokaz | Fajl, simbol, komanda, artefakt, uredjaj, log, trace, screenshot ili merenje |
| Osnovni uzrok | Mehanizam, a ne samo simptom |
| Uticaj | Uticaj na korisnika, podatke, bezbednost, dostupnost, store, trosak ili uskladjenost |
| Opseg | Workflow, platforma, arhitektura, build profil, kanal, verzija, tenant i klasa uredjaja |
| Popravka | Najmanja bezbedna reverzibilna promena |
| Verifikacija | Regresioni, negativni, concurrency, migration, release i recovery testovi |
| Rollback | Izvrsiv rollback ili forward-fix put |
| Preostali rizik | Vlasnik, rok, kompenzaciona kontrola i datum sledece provere |

