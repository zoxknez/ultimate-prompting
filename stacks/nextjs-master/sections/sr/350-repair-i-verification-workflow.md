## Repair i verification workflow

1. Zamrzni scope i zabelezi baseline, nalaze i safety ogranicenja.
2. Izaberi jednu potvrdjenu ili highest-risk opovrgljivu hipotezu.
3. Reprodukuj sa najmanjim bezbednim okruzenjem i skupom podataka.
4. Identifikuj autoritativnu invarijantu i tacnu failing granicu.
5. Dizajniraj najmanju popravku i dokumentuj odbacene alternative, kompatibilnost, migraciju i rollback.
6. Implementiraj reviewable korak bez nepovezanog refaktorisanja.
7. Dodaj regresioni test koji pada pre i prolazi posle.
8. Pokreni narrow, affected, production build, artifact smoke i primenljive failure testove.
9. Proveri telemetry, rollout guardrail, recovery i residual risk.
10. Azuriraj nalaze, logove, matrice, release notes, runbook-ove i odluku.

