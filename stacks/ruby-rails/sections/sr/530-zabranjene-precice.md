## Zabranjene Precice

- Izmisljen output komandi, rezultati testova, CVE-jevi, benchmark, incidenti ili production opservacije.
- Brisanje lock fajla, siroke dependency nadogradnje, floating Git branch-evi ili nepregledane izmene framework default-a.
- Koriscenje model validacije kao jedine uniqueness ili integrity kontrole.
- Koriscenje `permit!`, iskljucivanje CSRF-a, siroki CORS, `html_safe`, raw SQL ili unsafe deserializacije kao popravke.
- Pretpostavka da se jobovi izvrsavaju jednom, da uniqueness plugin daje exactly-once ili da su retry-ji bezopasni.
- Povecanje Puma thread-ova ili job concurrency-ja bez analize database, cache, memory i downstream kapaciteta.
- Ukljucivanje YJIT-a, Fiber-a, Ractor-a ili drugog Ruby runtime-a bez izmerene kompatibilnosti i rollback-a.
- Pokretanje migracija sa svake web replike ili destruktivni DDL bez backup-a i mixed-version dokaza.
- Tretiranje health check-a, zelenog CI-ja ili statickih skenova kao dokaza production ispravnosti.
- Proglasavanje sistema savrsenim ili potpuno spremnim dok dokaz nedostaje.

