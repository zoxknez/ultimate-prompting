## Phase S - Test Strategy And Regression Proof

Inventory: unit, integration (real provider where possible — do not treat EF InMemory as proof of relational correctness), contract, security (authz, SSRF, CORS/antiforgery, upload, webhook replay), concurrency, migration, E2E, publish smoke, load where relevant, AOT/trimming if used.

Every implemented P0–P2 fix requires a test that demonstrates the old incorrect and new correct behavior. Do not mark tests skipped so the pipeline passes. Do not disable analyzers without analysis.

