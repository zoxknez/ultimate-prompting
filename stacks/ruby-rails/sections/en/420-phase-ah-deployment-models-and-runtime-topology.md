## Phase AH - Deployment Models And Runtime Topology

### Kamal And Containers

- Verify roles for web, jobs, scheduler, cable and one-off tasks; do not hide all roles inside one container without lifecycle proof.
- Audit image digest, registry trust, proxy, TLS, health, accessories, secrets, volumes, hooks and rollback behavior.
- Run migrations once, drain traffic, stop workers safely and prove old and new releases can overlap.

### Kubernetes, PaaS, VM And Serverless

- For Kubernetes, verify probes, resources, disruption, termination grace, autoscaling, jobs, secrets and database connection math.
- For PaaS, verify buildpack or image identity, release command, process types, ephemeral filesystem and platform timeout.
- For VMs, verify systemd or process manager, users, filesystem permissions, log rotation, package updates and restart ordering.
- For serverless, verify cold start, request duration, connection reuse, concurrency, background work limitations and deployment version skew.

