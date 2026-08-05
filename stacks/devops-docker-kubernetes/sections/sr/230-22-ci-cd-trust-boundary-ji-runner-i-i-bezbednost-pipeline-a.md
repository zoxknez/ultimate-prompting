## 22. CI/CD trust boundary-ji, runner-i i bezbednost pipeline-a

**Cilj:** Spreci da nepouzdane izmene dobiju build, secret, artifact, deployment ili cloud ovlascenja.

### 22.1 Obavezne provere

1. Mapiraj event-e, repozitorijume, grane, tagove, pull request-ove, fork-ove, aktere, okruzenja, odobrenja, reusable workflow-e, spoljne trigger-e i deployment ciljeve.
2. Audituj default token dozvole, job-level dozvole, OIDC claim-ove, cloud trust policy-je, zastitu okruzenja, branch pravila, obavezne review-e i razdvajanje build-a od deployment-a.
3. Pinuj third-party action-e, image-e, plugin-e, orb-ove, template-e i include-e na immutable review-ovane reference. Proveri maintainer-a, provenance, dozvole i update proces.
4. Razdvoji trusted i untrusted job-ove. Spreci da fork ili pull-request kod pristupi produkcionim tajnama, cache-u, artefaktima, potpisivanju, registrima, self-hosted mrezama ili deployment kredencijalima.
5. Audituj self-hosted runner-e za tenancy, perzistenciju, ciscenje, patching, mreznu dostupnost, container escape, host kredencijale, reuse workspace-a, autoscaling i reakciju na kompromitovanje.
6. Spreci command, path, expression, matrix, artifact, cache, environment-file, log i shell injection iz nepouzdanih metapodataka.
7. Proveri identitet upload-a i download-a artefakta, checksum, attestation, retention, pristup, overwrite ponasanje i otpornost na zamenu između workflow-a.
8. Testiraj cancellation, retry, dupli trigger, zastarelo odobrenje, partial publish, nedostupan registry, kompromitovanu zavisnost, gubitak runner-a i rollback pipeline.

### 22.2 Minimalni dokazi

- Mapa pipeline trust boundary-ja i dozvola.
- Dokaz testova fork-a, OIDC-a, runner-a, artefakta, cache-a i injection-a.
- Reprezentativan audit trag od build-a do deployment-a sa odobrenjima i immutable referencama.

### 22.3 Kriterijumi izlaza

1. Nepouzdan kod ne moze pristupiti trusted kredencijalima, mrezama, artefaktima, cache-u ili deployment ovlascenju.
2. Produkcioni deployment zahteva pripisive, zasticene, least-privileged identitete i review-ovane dokaze.
3. Kompromitovanje runner-a, zamena artefakta i duplo izvrsavanje imaju testirane putanje ogranicavanja.

