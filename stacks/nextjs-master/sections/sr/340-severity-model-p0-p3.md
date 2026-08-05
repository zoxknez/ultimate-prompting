## Severity model P0-P3

| Severity | Definicija | Odgovor |
| --- | --- | --- |
| P0 | Aktivna kompromitacija, auth bypass, cross-tenant disclosure, secret exposure, RCE, destruktivan gubitak podataka, korumpiran release ili nekontrolisan kritican outage | Odmah containment, cuvanje dokaza, revocation/isolation i incident command |
| P1 | Eksploatabilan BOLA, private cache leak, pokvaren mutation authz, ozbiljan race/idempotency, nebezbedna migracija ili release blocker | Popravi ili contain pre release-a sa regresijom, guardrail-om i recovery-jem |
| P2 | Materijalan performance, a11y, SEO, observability, resilience, cost, maintainability ili compatibility rizik | Zakazi sa owner-om, acceptance-om, evidence planom i rokom |
| P3 | Manji cleanup, consistency, dokumentacija, developer experience ili low-impact optimizacija | Backlog sa jasnom vrednoscu, owner-om i non-regression scope-om |

