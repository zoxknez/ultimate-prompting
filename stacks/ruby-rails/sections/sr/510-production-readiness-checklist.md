## Production Readiness Checklist

- [ ] Podrzane Ruby i Rails linije sa dokazom tacnog runtime-a.
- [ ] Immutable source-to-runtime identitet za svaku ulogu procesa.
- [ ] Pregledan Bundler graph, native biblioteke i supply-chain dokaz.
- [ ] Production eager-load, boot, asset i release build verifikacija.
- [ ] Default-deny autorizacija i negativni testovi tenant izolacije.
- [ ] Database constraint-i, granice transakcije i concurrency testovi.
- [ ] Idempotentni jobovi, retry, DLQ ili failure workflow i mixed-version kompatibilnost.
- [ ] Web, job, scheduler i Cable kapacitet sa matematikom connection pool-a.
- [ ] Session, CSRF, CORS, rotacija tajni i kontrole administrativnog pristupa.
- [ ] Active Storage i parser izolacija sa testovima zlonamernih fajlova.
- [ ] SLO-jevi, dashboard-i, alert-i, release correlation i testirani runbook-ovi.
- [ ] Build-once promocija artefakta sa SBOM-om i provenance-om.
- [ ] Expand-and-contract migracija i dokaz old/new koegzistencije.
- [ ] Kontrolisani rollout, abort kriterijumi i testiran rollback ili forward repair.
- [ ] Izolovani restore, izmereni RPO/RTO i cross-system reconciliation.
- [ ] Incident containment, opoziv i trusted rebuild procedura.

