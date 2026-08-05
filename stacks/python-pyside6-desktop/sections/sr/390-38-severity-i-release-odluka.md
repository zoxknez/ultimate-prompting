## 38. Severity i release odluka

### 38.1 P0-P3 tumačenje

| Severity | Značenje | Podrazumevana akcija |
| --- | --- | --- |
| P0 | Aktivna kompromitacija, arbitrary code execution, kompromitovan signing/update, nepovratan širok gubitak podataka ili neposredan kritičan safety/poslovni uticaj. | Zaustavi release ili rad; containment, očuvanje dokaza i recovery. |
| P1 | Visoko verovatan ozbiljan security, authorization, data-integrity, crash-loop, update, migration ili rollback kvar koji pogađa materijalne korisnike. | Blokiraj release dok se ne popravi i verifikuje ili dok ovlašćeni vlasnici eksplicitno ne prihvate rizik. |
| P2 | Materijalan reliability, performance, accessibility, operability, privacy, maintainability ili compatibility defekt sa ograničenim uticajem. | Popravi pre release-a kada je primenljivo ili zakaži sa vlasnikom, rokom, kontrolama i acceptance kriterijumima. |
| P3 | Niskorizično unapređenje, cleanup, dokumentacija, dubina testova ili opciona modernizacija. | Prioritizuj transparentno; ne predstavljaj kao blocker bez dokaza. |

### 38.2 Zaključci

1. `READY`: svi primenljivi production dokazi i Definition of Done uslovi su ispunjeni bez nerazrešenog blocking rizika.
2. `READY_WITH_CONDITIONS`: nema nerazrešenog P0/P1 blocker-a, ali ostaju eksplicitni ograničeni uslovi, vlasnici, datumi, kontrole i plafoni dokaza.
3. `NOT_READY`: ostaje jedan ili više blocking security, correctness, data, packaging, platform, update, rollback, restore ili operativnih uslova.
4. `INCIDENT`: aktivna ili sumnjiva kompromitacija, nebezbedan release kanal, korumpirano stanje ili untrusted build/runtime zahteva containment i trusted recovery.
5. Nikada ne pretvaraj nedostatak dokaza u pozitivan zaključak; navedi `UNVERIFIED` i tačan dokaz koji nedostaje.

