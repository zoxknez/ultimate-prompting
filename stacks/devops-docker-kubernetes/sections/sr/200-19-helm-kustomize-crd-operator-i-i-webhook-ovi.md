## 19. Helm, Kustomize, CRD, Operator-i i webhook-ovi

**Cilj:** Ucini generisanu konfiguraciju deterministickom, preglednom, bezbednom za upgrade i svesnom otkaza.

### 19.1 Obavezne provere

1. Renderuj svako okruzenje iz cistog checkout-a sa pinovanim zavisnostima i uporedi izlaz, values, patch-eve, default vrednosti, capability-je, hook-ove i generisana imena.
2. Audituj provenance chart-a, subchart-a, plugin-a, remote base-a, OCI artefakta i template funkcije, version constraint-e, checksum-e i update policy.
3. Detektuj nebezbedne default vrednosti, skrivene mutabilne values, curenje okruzenja, renderovanje tajni, duple resurse, pretpostavke redosleda i ne-idempotentne hook-ove.
4. Audituj CRD seme, pruning, default vrednosti, status, subresource-e, conversion webhook-ove, stored version-e, migraciju, vlasnistvo, finalizer-e i efekte brisanja.
5. Audituj operator-e i admission webhook-ove za RBAC, image provenance, leader election, idempotentnost reconciliation-a, retry, backoff, finalizer-e, redosled upgrade-a, dostupnost, TLS, timeout i failurePolicy.
6. Testiraj instalaciju, upgrade sa podrzanih prethodnih verzija, rollback ogranicenja, uninstall, cuvanje CRD-a, webhook outage i delimican reconciliation.
7. Ne tvrdi da Helm rollback vraca spoljno stanje, migracije podataka, CRD semu ili cloud resurse osim ako je to eksplicitno potvrđeno.

### 19.2 Minimalni dokazi

- Deterministicki render diff za sva okruzenja.
- Matrica kompatibilnosti CRD-a, operator-a, webhook-a i plugin-a.
- Dokaz testova instalacije, upgrade-a, outage-a, rollback-a i uninstall-a.

### 19.3 Kriterijumi izlaza

1. Generisani resursi su deterministicki, pregledni i bez secret materijala.
2. Redosled upgrade-a CRD-a i webhook-a ne moze blokirati kontrolnu putanju ili tiho ostetiti objekte.
3. Rollback ogranicenja i spoljni side effect-i su eksplicitni.

