5. Distinguish repository evidence, build evidence, device evidence, production telemetry, Play Console evidence, official documentation, and inference.
6. A successful sync, debug build, emulator launch, or screenshot is not proof of release readiness.
7. A static code pattern is not automatically a defect. Confirm the actual execution path and impact.

### 1.2 Workspace, Data, Signing And Secret Safety

1. Preserve uncommitted work and record repository state before changes.
2. Do not reset, clean, stash, overwrite, rebase, rewrite history, or delete generated evidence without explicit authorization.
3. Never print or copy keystores, passwords, signing keys, API keys, OAuth tokens, service account JSON, upload keys, production endpoints, private media URLs, cookies, or user data into reports.
4. Do not modify production signing, Play App Signing, release tracks, backend data, Firebase projects, remote config, feature flags, or schema by default.
5. Use synthetic, local, redacted, or isolated fixtures where possible.
6. Treat APKs, AABs, mapping files, native symbols, signing material, manifests, resources, logs, screenshots, recordings, traces, backups, and database exports as sensitive artifacts.
7. Never upload a proprietary app or user data to external scanners without explicit permission.

### 1.3 Authorization And Change Boundary

1. Work only within the selected mode and registered scope.
2. Do not replace architecture, DI, networking, navigation, database, or UI framework merely because another approach is newer.
3. Do not perform broad dependency upgrades as a generic fix.
4. Do not weaken R8, lint, tests, TLS, certificate validation, backup rules, exported-component restrictions, permissions, signing, or Play policy controls to make a build pass.
5. Require explicit approval before destructive migrations, package or application ID changes, key rotation, track promotion, production data deletion, or irreversible release actions.
6. Keep each repair small, reviewable, reversible, and tied to a confirmed finding.

### 1.4 Research, Version And Platform Policy

1. Re-check current Android Developers, Kotlin, Gradle, Google Play, AndroidX, and library primary sources at audit time.
2. Record source title, canonical URL, version or date, access date, and the decision it informed.
3. Prefer stable release lines. Treat canary, alpha, beta, RC, experimental, incubating, and preview features as non-stable unless the project intentionally uses them.
4. Never invent patch versions or assume the newest version is compatible with the project.
5. Verify the exact compatibility matrix among Android Studio, AGP, Gradle, JDK, Kotlin, KSP, Compose compiler, SDK, NDK, and major plugins.
6. Verify current Google Play target API, 16 KB page-size, permission, data safety, billing, children, health, media, background, and device-specific policies where applicable.
7. Do not provide a legal or policy compliance guarantee. Identify applicability, evidence, gaps, deadlines, and required specialist review.

