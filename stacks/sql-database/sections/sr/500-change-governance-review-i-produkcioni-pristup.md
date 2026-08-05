## Change governance, review i produkcioni pristup

Database promene zahtevaju jace kontrole jer efekti mogu biti trajni, globalni i tesko reverzibilni.

- Zahtevaj peer review za DDL, destruktivni DML, promene rola, backup politiku, failover automatizaciju i retention promene.
- Koristi immutable pregledane skripte ili migration artefakte sa checksum-ima i environment guard-ovima.
- Razdvoji request, approval, execution i audit identitete za visokorizicne akcije.
- Koristi just-in-time privilegovani pristup, session recording i automatski expiry gde je podrzano.
- Zabrani deljene administrativne naloge i nedokumentovane produkcione console promene.
- Pregledaj emergency promene nakon incidenta i pretvori ih u managed source-controlled stanje.

