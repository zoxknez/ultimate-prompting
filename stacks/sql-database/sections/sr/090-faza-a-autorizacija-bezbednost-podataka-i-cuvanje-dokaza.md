## Faza A - Autorizacija, bezbednost podataka i cuvanje dokaza

Pre dodira sa bazom utvrdi ovlascenje, identitet okruzenja, maintenance ogranicenja i opcije oporavka.

- Zabelezi repository SHA, stanje migracija, deployment revision, server time, timezone i aktivni incident ili maintenance window.
- Proveri da test alati podrazumevano ne mogu da resolve-uju ili autentifikuju produkciju.
- Potvrdi storage headroom, prostor transaction log-a, backup retention, zdravlje replike i kapacitet restore destinacije.
- Sacuvaj logove, planove, catalog snapshot-e i hash-eve bez kopiranja nepotrebnih osetljivih podataka.
- Definisi stop uslove za rast lock-ova, replication lag, I/O saturation, error rate, disk usage i recovery neizvesnost.
- Za incident rezim zamrzni nebezbedne write-ove pre ciscenja i sacuvaj originalno stanje.

