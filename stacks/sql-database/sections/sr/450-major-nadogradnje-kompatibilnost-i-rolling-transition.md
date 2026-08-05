## Major nadogradnje, kompatibilnost i rolling transition

Major engine nadogradnja je aplikativna, data, operativna i recovery migracija, a ne samo promena paketa.

- Inventarisi uklonjeno ponasanje, reserved reci, default-e, collation-e, autentikaciju, ekstenzije, replikaciju i backup kompatibilnost.
- Pokreni vendor checker-e, ali nezavisno testiraj aplikativni SQL, migracije, planove i operativnu automatizaciju.
- Uvezbaj logical, physical, in-place, replica-first ili blue-green putanje sa realnim podacima i merenjem downtime-a.
- Uporedi kriticne planove upita, statistiku, collation rezultate i transaction anomalije pre i posle.
- Dokazi kompatibilnost aplikacije, driver-a, pooler-a, proxy-ja, backup-a i monitoringa.
- Definisi cutover, freeze, abort, rollback ogranicenja, forward repair i post-upgrade validaciju.

