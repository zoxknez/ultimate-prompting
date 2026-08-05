## 27. Obavezni adversarial i failure scenariji
1. S1 - Dve brze korisnicke akcije pokrecu istu privilegovanu ili finansijsku mutaciju.
2. S2 - Odgovor se zavrsava posle navigacije, logout-a, promene tenant-a, zamene stavke ili unistenja view-a.
3. S3 - Aplikacija se gasi pre slanja zahteva, tokom transfera, posle server commit-a i pre lokalne potvrde.
4. S4 - Stari binary prima novi JavaScript, novi binary se pokrece sa starim embedded JavaScript-om i rollback sledi posle lokalne migracije.
5. S5 - OTA download je prekinut, korumpiran, bez prostora, sa nevazecim potpisom, pogresnim kanalom ili crash loop-om.
6. S6 - Nalog ili tenant se menja dok cache podaci, offline komande, stream, notification i background rad ostaju aktivni.
7. S7 - Deep link ili notification cilja uklonjen, neautorizovan, stale, cross-tenant ili malformed resurs.
8. S8 - Token refresh, logout, opoziv, key rollover, network retry i vise paralelnih zahteva ulaze u race.
9. S9 - Native callback stize posle React instance reload-a, rekreiranja activity-ja, zamene view controller-a ili Fabric view recycling-a.
10. S10 - JSI ili native kod prima malformed, prevelik, lose poravnat, stale, dupliran ili konkurentno koriscen podatak.
11. S11 - Background task, push akcija, media dogadjaj ili location dogadjaj se izvrsava sa starim kodom, isteklim kredencijalima ili promenjenom schemom.
12. S12 - Mreza je spora, captive, metered, menja se, offline je, TLS je rotiran, delimicno otkazuje ili vraca nekompatibilne podatke.
13. S13 - Migracija lokalne baze je prekinuta, storage je pun, podaci su korumpirani, backup je vracen ili dve verzije aplikacije pristupaju stanju.
14. S14 - Dozvola se menja u settings-u, ogranicena je, trajno odbijena ili opozvana dok je resurs aktivan.
15. S15 - Aplikacija ide u background, suspenduje se, gasi, restore-uje, upgrade-uje ili se uredjaj reboot-uje tokom svake kriticne operacije.
16. S16 - Malo memorije, thermal pritisak, slaba baterija, malo storage-a, spor uredjaj, duga lista, velika slika i ponovljena navigacija nastupaju zajedno.
17. S17 - Obradjuje se zlonameran fajl, arhiva, slika, medij, PDF, URL, WebView stranica, bridge poruka ili native intent.
18. S18 - Kompromitovan je signing kredencijal, update kljuc, CI runner, zavisnost, config plugin, native SDK ili build image.
19. S19 - Store rollout, OTA rollout, backend rollout, lokalna migracija i feature flag se preklapaju nekompatibilnim redosledom.
20. S20 - Production rollback i izolovani restore se izvrsavaju posle stvarnih promena podataka, queue-a, update-a i scheme.

