## 6. Phase A - Protect, Freeze And Inventory

1. Record `git status --short --branch`, current revision, branches, submodules, worktrees, untracked files, and local modifications.
2. Identify the repository root and every included build, composite build, convention plugin, `buildSrc`, version catalog, and custom Gradle plugin.
3. Map application, library, dynamic-feature, benchmark, test-fixture, baseline-profile, Wear, TV, Auto, and KMP modules.
4. Map source sets, variants, flavors, signing configurations, manifest overlays, generated sources, native source sets, assets, resources, and packaging options.
5. Locate CI workflows, release scripts, Fastlane, Play Publisher, Firebase App Distribution, artifact repositories, and environment configuration.
6. Inventory keystore references and secret paths without printing values.
7. Inventory application IDs, namespaces, version code and name logic, deep-link hosts, content authorities, services, receivers, providers, activities, permissions, features, and queries.
8. Inventory native libraries and third-party SDKs from both source configuration and built artifacts.
9. Identify critical user journeys, destructive operations, regulated data, offline requirements, and device-specific behavior.
10. Establish a no-change baseline before repairs.

Minimum safe commands, adapted to the project:

```text
git status --short --branch
git rev-parse HEAD
./gradlew --version
./gradlew projects
./gradlew tasks --all
```

