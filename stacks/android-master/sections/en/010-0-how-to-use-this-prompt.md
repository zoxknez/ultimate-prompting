## 0. How To Use This Prompt

### 0.1 Required Inputs

Collect or infer, and explicitly record:

| Field | Value |
| --- | --- |
| Application and repository | `[NAME / PATH / URL]` |
| Business purpose and critical user journeys | `[PURPOSE / FLOWS]` |
| Distribution | `[GOOGLE_PLAY / ENTERPRISE / SIDELOAD / OEM / MULTIPLE]` |
| Application type | `[PHONE / TABLET / FOLDABLE / TV / WEAR / AUTO / MULTI-DEVICE]` |
| UI toolkit | `[COMPOSE / VIEWS / MIXED]` |
| Language | `[KOTLIN / JAVA / MIXED]` |
| Modules | `[LIST OR UNKNOWN]` |
| minSdk / targetSdk / compileSdk | `[VALUES OR UNKNOWN]` |
| Android Studio / AGP / Gradle / JDK / Kotlin | `[VERSIONS OR UNKNOWN]` |
| Build variants and product flavors | `[LIST OR UNKNOWN]` |
| Dependency injection | `[HILT / DAGGER / KOIN / MANUAL / OTHER]` |
| Persistence | `[ROOM / DATASTORE / FILES / SQLCIPHER / OTHER]` |
| Networking | `[OKHTTP / RETROFIT / KTOR / WEBSOCKET / OTHER]` |
| Background work | `[WORKMANAGER / FGS / ALARMS / FCM / NONE]` |
| Media and device APIs | `[MEDIA3 / CAMERA / LOCATION / BLUETOOTH / NFC / USB / OTHER]` |
| Native code and packaged SDKs | `[NDK / JNI / RUST / C++ / .SO / NONE / UNKNOWN]` |
| Authentication and sensitive data | `[DESCRIPTION]` |
| Analytics, crash and performance tools | `[LIST OR UNKNOWN]` |
| CI/CD and signing | `[DESCRIPTION OR UNKNOWN]` |
| Compliance and policy scope | `[GDPR / CHILDREN / HEALTH / FINANCE / ENTERPRISE / OTHER / NONE / UNKNOWN]` |
| Work mode | `[AUDIT_ONLY / AUDIT_AND_SAFE_FIX / FULL_IMPLEMENTATION / FIX_CONFIRMED_ISSUES / RELEASE_READINESS_AUDIT]` |

### 0.2 Missing Information Policy

Do not block the whole audit because some inputs are missing.

1. Infer only from repository, Gradle, manifests, generated artifacts, CI configuration, device evidence, and authoritative documentation.
2. Mark unresolved assumptions as `UNVERIFIED`.
3. Continue with safe read-only checks when possible.
4. Ask only for access or credentials that materially block confirmation, repair, or verification.
5. Never convert missing evidence into a positive conclusion.
6. Do not assume the README, roadmap, screenshots, issue tracker, or comments describe the current implementation correctly.

### 0.3 Work Modes

| Mode | Allowed behavior |
| --- | --- |
| `AUDIT_ONLY` | Inspect, build safely, test, profile, and report. Do not mutate source, lockfiles, schemas, signing, Play configuration, or production data. |
| `AUDIT_AND_SAFE_FIX` | Apply confirmed, low-risk, reversible fixes with focused regression tests. Plan larger or risky changes. |
| `FULL_IMPLEMENTATION` | Implement justified changes incrementally with backups, migration safety, verification, and rollback. |
| `FIX_CONFIRMED_ISSUES` | Change only findings already registered and confirmed. Do not widen scope silently. |
| `RELEASE_READINESS_AUDIT` | Prioritize release variants, signing, R8, native compatibility, policy, critical journeys, observability, and rollback. |

If unspecified, use `AUDIT_AND_SAFE_FIX`.

