## Faza 25 - CI/CD, repository trust, kredencijali, provenance i promocija

### Cilj

Audituj delivery sistem kao privilegovani production control plane sa eksplicitnim trust-om, izolacijom i dokazima.

### Zahtevi audita

- Mapiraj repository, branch protection, review, CODEOWNERS, tag, release, runner, action, plugin, cache, artifact store, registry, deployer i environment trust granice.
- Odvoji izvršavanje nepoverljivih pull request-ova i fork-ova od tajni, signing ključeva, package publikovanja, produkcionih mreža i deployment kredencijala.
- Pinuj third-party action-e i image-e immutable, proveri download-e, zaključaj zavisnosti, zaštiti cache-eve i ograniči Composer skripte i plugin-e.
- Preferiraj short-lived scoped identity kao OIDC; audituj odobrenje, separation of duties, break-glass, rotaciju, opoziv i audit trail-ove.
- Build-uj jednom, proveri jednom, potpiši jednom i promoviši isti artifact digest kroz okruženja uz policy provere i eksplicitna odobrenja.
- Proveri SBOM, provenance, potpis, vulnerability policy, ownership waiver-a, expiry, revocation i trusted rebuild procedure.

### Obavezni dokazi

- CI/CD trust-boundary i credential matrica.
- Run-to-artifact-to-deployment provenance za reprezentativni release.
- Dokaz untrusted-change, cache-poisoning, credential-revocation, artifact-substitution i trusted-rebuild testova.

### Kriterijumi prihvatanja

- Nepoverljivi kod ne može da dobije produkciono ovlašćenje, signing materijal ili trusted artifact status.
- Svaka deploy-ovana revision je odobren, proveren, immutable artifact sa poznatim rollback target-om.

