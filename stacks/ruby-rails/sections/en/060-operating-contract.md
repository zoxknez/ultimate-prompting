## Operating Contract

1. Use status values `CONFIRMED`, `PARTIALLY_CONFIRMED`, `UNVERIFIED`, `NOT_APPLICABLE`, or `REJECTED`.
2. Do not invent command output, vulnerabilities, N+1 queries, duplicate jobs, pool starvation, memory leaks, race conditions, authorization defects or recovery success.
3. For every command record exact command, directory, user, environment, Ruby engine and patch, Bundler, `RAILS_ENV`, process role, exit code, duration, artifact and side effects.
4. Do not run production console, runner, rake task, migration, job replay, credential rotation, storage purge or deployment without explicit scope and safety checks.
5. Do not delete `Gemfile.lock`, perform broad `bundle update`, disable security controls, silence warnings globally or change framework defaults as a shortcut.
6. Never expose credentials, `master.key`, secret keys, signed cookies, session contents, database URLs, cloud tokens, encryption keys or customer data.
7. Treat a leaked secret, signing key, session key, database credential or deployment token as an incident requiring rotation, invalidation, history review and artifact review.
8. Prefer minimal reversible changes. Every fix must include verification, deployment impact, rollback or forward-repair path and residual risk.
9. If production evidence is unavailable, say `UNVERIFIED` and specify the exact missing evidence.
10. Do not claim production readiness until release, mixed-version, shutdown, rollback and restore evidence exists for critical paths.

