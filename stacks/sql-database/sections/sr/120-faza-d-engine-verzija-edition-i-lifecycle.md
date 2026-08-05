## Faza D - Engine, verzija, edition i lifecycle

Utvrdi tacan support status i upgrade ogranicenja bez mesanja kompatibilnih proizvoda.

- Zabelezi server verziju, patch, edition, distribuciju, arhitekturu, libc, OpenSSL i operativni sistem.
- Razdvoji protocol kompatibilnost, SQL kompatibilnost, storage-engine kompatibilnost i managed-service kompatibilnost.
- Pregledaj release notes, security advisory-je, deprecation-e, uklonjeno ponasanje i podrzanu upgrade putanju.
- Proveri kompatibilnost ekstenzija i plugin-a pre engine nadogradnje.
- Dokazi downgrade ogranicenja i da li rollback zahteva restore podataka ili forward repair.
- Tretiraj MySQL i MariaDB, PostgreSQL i kompatibilne fork-ove, kao i SQLite binding-e kao posebne proizvode dok se ne dokaze suprotno.

