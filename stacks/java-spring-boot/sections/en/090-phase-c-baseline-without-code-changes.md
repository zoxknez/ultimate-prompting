## Phase C - Baseline Without Code Changes

First verify dependency resolution, main/test compilation, unit/integration tests, static analysis, style/format, packaging, startup, health, native/AOT when officially supported, container image, and a smoke test of the deployed artifact. Adapt `./mvnw -B -ntp compile`, `test`, `verify`, and `package` for Maven; use `./gradlew compileJava`, `test`, `check`, and `build` for Gradle. Do not treat `-DskipTests` as proof that the build passes; distinguish skipped execution, compiled tests, disabled tests, and inactive integration profiles.

For each failure preserve the first material error and identify the root cause: JDK/toolchain mismatch, repository/certificate, profile, secret, port, locale/timezone, test order, local database, or Docker runtime. Start the application only with safe local/test configuration that cannot send email, use production queue/payment/service discovery, or alter production data.

