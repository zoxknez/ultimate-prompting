## Forbidden Shortcuts

- Invented command output, test results, CVEs, benchmarks, incidents or production observations.
- Deleting the lockfile, broad dependency upgrades, floating Git branches or unreviewed framework-default changes.
- Using model validation as the only uniqueness or integrity control.
- Using `permit!`, disabling CSRF, broad CORS, `html_safe`, raw SQL or unsafe deserialization as a fix.
- Assuming jobs run once, uniqueness plugins provide exactly-once, or retries are harmless.
- Increasing Puma threads or job concurrency without database, cache, memory and downstream capacity analysis.
- Enabling YJIT, Fibers, Ractors or a different Ruby runtime without measured compatibility and rollback.
- Running migrations from every web replica or using destructive DDL without backup and mixed-version proof.
- Treating health checks, green CI or static scans as proof of production correctness.
- Declaring a system perfect or fully ready while evidence is missing.

