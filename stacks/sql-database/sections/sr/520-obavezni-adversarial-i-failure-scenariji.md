## Obavezni adversarial i failure scenariji

1. Dva paralelna request-a pokusavaju da kreiraju isti logicki unique resurs.
2. Dve transakcije menjaju isti balans, zalihu ili state transition.
3. Klijent dobija timeout neposredno pre ili posle commit-a i ponavlja zahtev.
4. Proces pada nakon database commit-a, ali pre poruke, fajla, cache-a ili HTTP acknowledgement-a.
5. Deadlock ili serialization failure nastaje pod reprezentativnom konkurentnoscu.
6. Duga transakcija blokira vacuum, purge, DDL ili retention rad.
7. Connection pool je iscrpljen dok je baza spora, ali jos prihvata konekcije.
8. Proxy, DNS target ili primary se menja dok su request-i aktivni.
9. Migracija se izvrsava dok stare i nove verzije aplikacije rade paralelno.
10. Backfill je prekinut, restartovan i slucajno pokrenut dva puta.
11. Disk, WAL, binlog, undo, temporary ili backup storage se priblizava iscrpljenju.
12. Replika je promovisana sa lag-om, a stari primary se kasnije vraca.
13. Stale replika opsluzuje authorization-sensitive ili read-after-write zahtev.
14. Backup restore nailazi na nedostajuci ili korumpiran log segment.
15. PITR target se tumaci u pogresnoj timezone ili prelazi daylight-saving promenu.
16. Kredencijal, sertifikat ili encryption key se rotira dok su pool-ovi i replike aktivni.
17. Tenant identifikator je izostavljen iz cache-a, job-a, export-a ili administrativnog upita.
18. Malformed JSON, text encoding, collation ili numeric input stize do kriticnog upita.
19. SQLite otvaraju dve instance aplikacije ili je postavljen na nepouzdan shared storage.
20. Izolovani restore mora da postane novi produkcioni source dok queue-ovi i spoljni sistemi sadrze kasnije efekte.

