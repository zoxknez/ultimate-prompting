## Definition Of Done

Rad je zavrsen samo kada su primenljivi uslovi obelezeni dokazom ili `NIJE_PRIMENJIVO` uz obrazlozenje:

1. Repo snapshot i status tudjih izmena su zabelezeni.
2. Solution i svi relevantni projekti su inventarisani; dependency graf mapiran.
3. SDK, runtime, C#, ASP.NET Core, EF Core i NuGet verzije proverene; lifecycle/EOL iz aktuelnih zvanicnih izvora.
4. Restore, Debug/Release build, test i publish status zabelezeni stvarnim komandama.
5. Kriticni poslovni tokovi mapirani.
6. Svi P0/P1 imaju dokaz, uzrok, uticaj; popravljeni ili imaju containment i recovery.
7. Potencijalni rizici odvojeni od potvrdjenih nalaza.
8. AuthN/AuthZ/ownership/tenant provereni pozitivnim i negativnim testovima.
9. Data Protection strategija proverena.
10. Kriticni write tokovi imaju constraints, concurrency i idempotency dokaz.
11. EF migracije pregledane; transaction granice dokumentovane.
12. Async propagira cancellation gde treba; timeout/retry definisani.
13. Message/job ack, dedup i shutdown provereni ili oznaceni NEPROVERENO.
14. Secrets, konfiguracija i supply chain auditirani; tajne nisu prikazane.
15. Health/observability omogucavaju dijagnostiku; alert/runbook gde postoje.
16. Performanse nisu proglasene bez merenja.
17. Graceful shutdown testiran ili jasno NEPROVERENO.
18. Rollout i rollback dokumentovani.
19. Implementirane izmene minimalne, povezane sa nalazima; P0-P2 imaju regresione testove.
20. Relevantni test/build/publish opseg izvrsen posle izmena.
21. Komandni dnevnik potpun (komanda, dir, SDK, config, exit, sazetak).
22. Finalni diff bez nepovezanih izmena.
23. Zavrsna presuda, blokatori, preostali rizik, recovery i sledeci vlasnici jasni.

Ako neki uslov nije ispunjen: **Projekat jos nije potpuno production-ready.** Precizno navedi blokirajuce uslove.

