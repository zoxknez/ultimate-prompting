## 23. Phase R - Legacy, Migration And Interoperability Review

1. Identify deprecated Android APIs, support libraries, Kotlin synthetics, AsyncTask, Loader, legacy storage, legacy permissions, old billing, old media, and obsolete Gradle APIs.
2. Classify each legacy item as safe, supported, risky, blocking, or migration candidate.
3. Do not migrate only for fashion. Tie migration to support, security, correctness, performance, policy, or maintainability.
4. Plan framework and toolchain upgrades in compatibility-bounded steps.
5. Preserve behavior with characterization tests before large refactors.
6. Test database, storage, auth, navigation, notification, background, media, and signing continuity during migration.
7. Verify Java and Kotlin nullability, SAM, exceptions, generics, annotations, and threading interoperability.
8. Verify KMP or shared modules do not hide platform lifecycle, security, or storage requirements.
9. Remove obsolete compatibility code only after confirming the supported device and version policy.
10. Document temporary bridges and deadlines so they do not become permanent hidden architecture.

