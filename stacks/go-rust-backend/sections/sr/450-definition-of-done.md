## Definition Of Done

Rad je zavrsen samo kada su primenljivi uslovi obelezeni dokazom ili `NIJE_PRIMENJIVO`:

1. Tehnoloska staza potvrdjena; svi relevantni module/workspace/crate inventarisani.
2. Toolchain, lifecycle i support status provereni iz aktuelnih izvora.
3. Dependency graf mapiran; supply chain pregledan.
4. Pocetni build/test baseline i production artefakt stvarno buildani.
5. Target/feature/tag kompatibilnost proverena ili oznacena NEPROVERENO.
6. Kriticni tokovi mapirani.
7. Svaki prijavljeni problem ima dokaz; uzrok razdvojen od simptoma.
8. P0/P1 popravljeni ili imaju containment i recovery; popravke imaju regresione testove.
9. Go concurrency proveren race detectorom gde je moguce.
10. Rust unsafe ima dokumentovane safety invarijante; Miri/sanitizer ogranicenja jasna.
11. Goroutine/task lifecycle i shutdown provereni; cancellation/timeout propagirani.
12. Concurrency ogranicen prema kapacitetu dependency-ja.
13. Transakcije i idempotency proverene; migracije imaju rollout/recovery plan.
14. Security trust granice testirane; tajne nisu prikazane niti ubacene u artefakt.
15. Performanse nisu proglasene bez merenja.
16. Observability omogucava dijagnostiku; debug/profiler endpointi nisu nebezbedno izlozeni.
17. Graceful shutdown odgovara deployment platformi.
18. Rollout, abort i rollback dokumentovani.
19. Finalni diff bez slucajnih izmena; komandni dnevnik potpun.
20. Neproverene oblasti eksplicitne; nema tvrdnje o production spremnosti bez dokaza.

Ako neki uslov nije ispunjen: **Projekat jos nije potpuno production-ready.** Precizno navedi blokirajuce uslove.

