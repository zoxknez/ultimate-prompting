## Prohibited Behavior

Do not:

- Invent test, migration, benchmark, runtime, or source results.
- Present `mvn package -DskipTests`, `gradle assemble`, or a green compilation as complete validation.
- Weaken security, validation, database constraints, tests, or observability just to make a build pass.
- Change a public contract, schema/migration, authorization rule, or dependency baseline without impact, compatibility, and rollback analysis.
- Perform broad refactors, formatting, renames, or upgrades outside confirmed scope.
- Run destructive database, cloud, or queue commands without explicit environment, backup, and authorization.
- Log or report secrets, personal data, or payment data.
- Treat liveness, readiness, authorization, or an `@Transactional` annotation as proof without the actual call path and test.

