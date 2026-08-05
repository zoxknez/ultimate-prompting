## Faza AH - Deployment Modeli I Runtime Topologija

### Kamal I Container-i

- Proveri uloge za web, jobove, scheduler, cable i one-off taskove; ne skrivaj sve uloge u jednom container-u bez lifecycle dokaza.
- Audituj image digest, registry trust, proxy, TLS, health, accessories, tajne, volume-e, hook-ove i rollback ponasanje.
- Pokreni migracije jednom, drain-uj saobracaj, bezbedno zaustavi workere i dokazi da se stari i novi release mogu preklapati.

### Kubernetes, PaaS, VM I Serverless

- Za Kubernetes proveri probe-ove, resource-e, disruption, termination grace, autoscaling, jobove, tajne i matematiku database konekcija.
- Za PaaS proveri buildpack ili image identitet, release komandu, process type-ove, ephemeral filesystem i platform timeout.
- Za VM proveri systemd ili process manager, korisnike, filesystem permission-e, log rotation, package update i redosled restarta.
- Za serverless proveri cold start, trajanje zahteva, reuse konekcija, concurrency, ogranicenja background rada i deployment version skew.

