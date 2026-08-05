## Ugovor za release, rollback, restore i incident

- Promoviši jedan immutable artefakt kroz okruženja; ne rebuild-uj production tiho iz iste source verzije.
- Definiši pre-deploy gate-ove, canary populaciju, SLI poređenje, uticaj na error budget, abort signale, ljudski ownership, maksimalni observation prozor i automatski naspram ručnog rollback-a.
- Proveri graceful shutdown prema stvarnom orchestration timing-u, connection draining-u, uklanjanju readiness-a, in-flight deadline-ovima, ponašanju queue lease-a, background worker-ima i završnom flush-u telemetrije.
- Dokumentuj rollback ograničenja posle promena šeme, poruke, keša, ključa, formata fajla, side effect-a ili spoljnog ugovora; koristi forward repair kada reversal nije bezbedan.
- Dokaži izolovani restore, kompatibilnost aplikacije, replay migracije, pristup ključu, vraćanje spoljne zavisnosti, reconciliation događaja, RPO, RTO i provere integriteta.
- U incident režimu sačuvaj volatilne i trajne dokaze, zaustavi destruktivni cleanup, ograniči pristup, rotiraj ili opozovi pogođeno poverenje, ograniči blast radius, proizvedi trusted rebuild, proveri eradication i zabeleži recovery odluke.

