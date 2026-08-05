## Faza C - Source-To-Runtime Identitet

### Obavezni lanac identiteta

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

- Dokazi da web, job, scheduler, konzola i one-off taskovi koriste nameravani commit i dependency graph.
- Odbaci mutable tagove, kopirane source direktorijume ili uspesan CI kao dovoljan production identitet.
- Uporedi image digest, instalirane gemove, kompajlirane native biblioteke i schema verziju kroz svaku ulogu procesa.
- Dodaj release identifikator bez tajni u health, logove, trace-ove, jobove i administrativnu dijagnostiku.

