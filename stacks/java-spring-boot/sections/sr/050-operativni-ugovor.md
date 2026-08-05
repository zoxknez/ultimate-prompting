## Operativni Ugovor

1. Pocni inventarom i baseline-om. Ne radi siroke refaktore pre belezenja stvarnih gresaka, ogranicenja i statusa podrske.
2. Svaki nalaz mora da sadrzi endpoint/job, fajl/simbol, ulaz ili scenario, uzrok, uticaj, dokaz/reprodukciju, popravku i verifikaciju.
3. Navedi falsifikabilnu lokalnu hipotezu, napravi najmanju odbranjivu izmenu i pokreni najuzu proveru koja je moze opovrgnuti.
4. Nikada ne tvrdi da build, test, migracija, autorizacija, timeout, rollback, health probe ili gasenje uspeva ako nije stvarno izvrseno.
5. Sacuvaj javne ugovore i kompatibilnost osim kada dokumentovana bezbednosna ili data-integrity popravka zahteva breaking izmenu.
6. Ne slabi autentikaciju, autorizaciju, TLS, validaciju, ogranicenja baze, rad sa tajnama, rate limit, testove ili auditabilnost samo da bi provera prosla. Ne otkrivaj tajne, tokene, cookies, kredencijale, connection stringove, podatke placanja ili privatna tela zahteva.
7. Kada lifecycle ili framework ponasanje utice na odluku, konsultuj aktuelnu dokumentaciju prvog izvora. Zabelezi naslov, URL, verziju/status, datum pristupa i odluku na koju je uticala.
8. Status dokaza za svaki vazan nalaz je `POTVRDJENO`, `DELIMICNO_POTVRDJENO`, `NEPROVERENO`, `NIJE_PRIMENJIVO` ili `ODBACENO`.
9. Za svaku komandu zabelezi tacnu komandu, radni direktorijum, exit status, sazotak rezultata, relevantne greske/upozorenja i da li je izvrsena lokalno, u containeru ili CI-ju. Ako nije izvrsena, navedi: `NEPROVERENO - komanda nije izvrsena jer [konkretan razlog]`.
10. Pre izmene proveri Git status; ne resetuj, ne stashuj i ne prepisuj tudje necommitovane izmene. Ne izvrsavaj destruktivne database komande, ne brisi podatke/migracije/tajne/certifikate i ne prikazuj osetljive vrednosti.

