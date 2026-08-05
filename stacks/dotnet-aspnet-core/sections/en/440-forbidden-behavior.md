## Forbidden Behavior

Do not:

- invent command output, files, classes, endpoints, migrations, CVEs, or test results;
- claim tests pass if not executed; hide failing tests; skip tests so the pipeline passes;
- disable analyzers without analysis; add `!` only to silence nullable warnings;
- use `catch (Exception) { }`; use `Task.Run` as a universal async fix; convert sync I/O into fake async;
- use the same DbContext in parallel; register scoped as singleton to silence a DI error;
- disable authorization or antiforgery; use wildcard CORS with credentials; trust every forwarded header;
- log secrets; retry non-idempotent side effects without protection;
- add an in-memory lock as protection across multiple replicas;
- auto-run destructive migrations; use EF InMemory as proof of relational correctness;
- switch all queries to `AsNoTracking`; add Include everywhere to hide lazy-loading issues;
- enable cache without an invalidation strategy; raise pool/thread limits without capacity analysis;
- move to Native AOT/Minimal APIs/MediatR/CQRS/microservices merely for popularity;
- use preview .NET/C# in production without explicit approval;
- delete user uncommitted changes; format the whole solution to hide a relevant diff;
- declare the project “perfect” or production-ready without evidence.

