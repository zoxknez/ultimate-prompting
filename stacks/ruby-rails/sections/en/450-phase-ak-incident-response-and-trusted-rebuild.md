## Phase AK - Incident Response And Trusted Rebuild

- Trigger incident mode for credential leakage, session-key compromise, arbitrary code execution, malicious gem, webshell, data corruption, tenant leak or unrecoverable queue behavior.
- Contain by stopping risky writes, pausing workers, disabling affected routes, isolating hosts and revoking compromised trust.
- Preserve logs, images, processes, packages, lockfiles, database evidence and timeline before cleanup.
- Rotate keys and credentials, invalidate sessions and signed data as required, and review historical artifacts and deployments.
- Rebuild from reviewed source, trusted toolchain, clean dependencies, known-good base image and newly issued credentials.
- Restore, reconcile, validate tenant isolation and critical invariants, then complete post-incident actions and regression tests.

