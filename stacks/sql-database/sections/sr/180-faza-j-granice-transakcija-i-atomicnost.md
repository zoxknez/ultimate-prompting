## Faza J - Granice transakcija i atomicnost

Rekonstruisi svaku kriticnu transakciju od aplikativnog ulaza do trajnog commit-a.

- Navedi read-ove, write-ove, constraint-e, lock-ove, remote pozive, poruke, fajlove, cache i cekanje korisnika unutar svake transakcije.
- Proveri auto-commit, implicit commit, nested transaction i savepoint ponasanje.
- Proveri da ORM unit-of-work granice odgovaraju poslovnoj atomicnosti i stvarnom ownership-u konekcije.
- Ne drzi database lock-ove tokom sporih remote poziva ili ljudske interakcije bez eksplicitnog dizajna.
- Definisi ponasanje kod commit neizvesnosti nakon timeout-a, gubitka mreze ili pada procesa.
- Koristi outbox, inbox, saga ili reconciliation kada atomicnost obuhvata bazu i spoljne sisteme.

