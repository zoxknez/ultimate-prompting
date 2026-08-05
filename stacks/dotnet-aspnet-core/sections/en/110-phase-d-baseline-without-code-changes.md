## Phase D - Baseline Without Code Changes

Establish baseline before changing code:

1. `dotnet restore` (and `--locked-mode` when expected);
2. Debug and Release `dotnet build`;
3. analyzers / `dotnet format` where configured;
4. `dotnet test` (unit, integration, security, contract);
5. `dotnet publish --configuration Release` (and RID/self-contained profile if that is what is deployed);
6. production-like startup with safe local/test configuration;
7. migration status, health/readiness, graceful shutdown where supported.

For every failure keep the first relevant error and find the root cause: SDK mismatch, restore, secret, port, database, test order, or local environment. Startup must not send email, use production queues/payments, or change production data.

