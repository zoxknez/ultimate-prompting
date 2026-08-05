## Production readiness checklist

1. [ ] Podrzane i patch-ovane Next.js, React, TypeScript, Node.js, package manager, ORM, auth i platform linije su proverene.
2. [ ] Frozen instalacija i autoritativni production build/start uspevaju iz cistog checkout-a.
3. [ ] Source-to-runtime identitet i immutable artifact promocija su dokazani.
4. [ ] Rute, runtime-i, rendering, cache-evi, auth, tenant-i, owner-i i SLO su inventarisani.
5. [ ] Server/client i RSC granice ne izlagu tajne ili privatne podatke.
6. [ ] Hydration, state, effect-i, optimistic update-i i concurrency su deterministicki i testirani.
7. [ ] Svaki cache ima potpune kljuceve, ispravan privacy scope, bounded staleness, invalidaciju i outage ponasanje.
8. [ ] Akcije i API-ji sprovode server authn, authz, validaciju, idempotency, transakciju, limite i audit.
9. [ ] Identity, session, revocation, tenant, admin i impersonation lifecycle-i su dokazani.
10. [ ] Browser, application, file, webhook, SSRF, CSP, CSRF, XSS i abuse zastite su proverene.
11. [ ] Database invarijante, concurrency, migracije, durable side effect-i, reconciliation i restore su dokazani.
12. [ ] Runtime/platform limiti, multi-instance ponasanje, version skew, draining i asset retention su testirani.
13. [ ] Field/lab performanse, kapacitet, headroom, load shedding i cost guardrail-i postoje.
14. [ ] Accessibility, i18n, SEO, error state-ovi, offline, vise tab-ova i service worker ispunjavaju acceptance.
15. [ ] Observability dokazuje user impact, release identitet, uzrocnu putanju, saturaciju i recovery bez leakage-a.
16. [ ] Testovi pokrivaju kriticne tokove, negativni authz, cache privacy, concurrency, migraciju, platformu, rollout, rollback i restore.
17. [ ] CI/CD izoluje untrusted kod i promovise trusted immutable artefakte sa dokazima.
18. [ ] Canary, abort, rollback, repair, kill switch-evi, restore, RPO, RTO i incident runbook-ovi su izvrseni.
19. [ ] Svi P0/P1 su popravljeni ili contained sa owner-om, rokom, monitoring-om i odobrenim residual risk-om.
20. [ ] Svaka READY tvrdnja ima obavezni dokaz i nijedna kriticna matrix celija ne nedostaje precutno.

