## Phase C - Source-To-Runtime Identity

### Required identity chain

```text
repository + commit + dirty state
Ruby engine + exact patch + build flags + platform
RubyGems + Bundler + lockfile digest + platform set
native extensions + system libraries + generated code
Rails/Rack/server/job adapter versions
artifact or image digest + SBOM + provenance
deployment revision + environment/config digest
database schema version + queue schema version
running web/job/scheduler process identity
telemetry release marker + user-visible behavior
```

- Prove that web, job, scheduler, console and one-off tasks run the intended commit and dependency graph.
- Reject mutable tags, copied source directories or successful CI as sufficient production identity.
- Compare image digest, installed gems, compiled native libraries and schema version across every process role.
- Add a non-secret release identifier to health, logs, traces, jobs and administrative diagnostics.

