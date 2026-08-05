## 8. Integritet od izvora do produkcije i drift

**Cilj:** Dokazi sta je aktivno, odakle potice i kako je promovisano.

### 8.1 Obavezne provere

1. Isprati reprezentativnu produkcionu reviziju od commit-a i review-a preko build-a, testova, digest-a artefakta, potpisa, provenance-a, registra, deployment revizije i aktivnog procesa.
2. Uporedi source manifeste, generisane manifeste, Helm ili Kustomize izlaz, GitOps desired state, live objekte, cloud resurse i runtime konfiguraciju.
3. Detektuj rucne hotfix-eve, mutabilne tagove, floating zavisnosti, nereview-ovane console izmene, hitne izmene i izuzetke kontrolera.
4. Proveri da promocija kroz okruzenja cuva identitet artefakta umesto ponovnog build-a razlicitih binarnih artefakata po okruzenju, osim ako je to namerno dizajnirano i kontrolisano.
5. Proveri da deployment metadata prikazuje commit, digest, build, vlasnika, change request i rollback cilj bez curenja tajni.
6. Uskladi deklarisano i live stanje bez prepisivanja hitnih dokaza ili legitimnih kontrolisanih izuzetaka.

### 8.2 Minimalni dokazi

- End-to-end trag za najmanje jedan produkcioni i jedan rollback artefakt.
- Izvestaj desired-versus-live drift-a kroz aplikacione i infrastrukturne slojeve.
- Lista mutabilnih, ponovo build-ovanih, rucno menjanih ili neproverljivih artefakata.

### 8.3 Kriterijumi izlaza

1. Aktivni kriticni workload-i mogu se pripisati review-ovanom izvoru i potvrđenim artefaktima.
2. Materijalni drift ima vlasnika, odluku i bezbednu putanju usklađivanja.
3. Promocija i rollback cuvaju identitet i auditabilnost.

