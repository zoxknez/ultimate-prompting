## 2. Current Research Baseline - Re-Check Before Every Audit

At the baseline date, primary sources indicated:

| Component | Baseline on 2026-08-05 | Mandatory audit action |
| --- | --- | --- |
| Android Studio | Quail 3, `2026.1.3`, stable channel | Verify the installed IDE and CI-supported AGP range. |
| Android Gradle Plugin | `9.3.x` stable; `9.4` preview | Do not recommend preview by default. Verify the exact release notes and plugin compatibility. |
| Gradle / JDK | AGP 9.3 requires Gradle `9.5.0`; JDK `17` | Verify wrapper checksum, daemon JDK, toolchains, CI image, and local parity. |
| Kotlin | `2.4.10` published on 2026-07-14 | Verify Android, KSP, Compose, serialization, and plugin compatibility before upgrades. |
| SDK | AGP 9.3 supports up to API `37`; API 37 requires at least AGP `9.1.1` | Record actual compileSdk and targetSdk. Do not infer Play eligibility from compileSdk. |
| Google Play target API | New apps and updates must target API `36+` from 2026-08-31, subject to current exceptions | Re-check the current Play policy and app category before release. |
| 16 KB pages | Apps targeting API 35+ on 64-bit Google Play devices must support 16 KB pages; release blocking begins 2027-02-01 | Inspect every packaged native library, alignment, SDK provenance, and test evidence. |

This table is a dated starting point, not a permanent truth.

