## Research Baseline - 5 August 2026

This baseline is a starting point. Re-check reactnative.dev, docs.expo.dev, EAS docs and real lock/native configuration before recommendations.

| Component | Confirmed status on 5 August 2026 | Mandatory audit check |
| --- | --- | --- |
| Expo SDK | **57** (stable since 30 June 2026; e.g. 57.0.x). | `expo` package, `npx expo-doctor`, `npx expo install --check`. |
| React Native | **0.86** (Expo 57 matrix; RN 0.86 ~June 2026). | bare vs Expo, peer deps, upgrade helper. |
| React | **19.2.x** (e.g. **19.2.3** in SDK 57). | alignment with Expo matrix. |
| Hermes | Default JS engine; bytecode/format changes with RN — tie to **runtimeVersion**. | engine, source maps, reanimated memory note (0.85+). |
| New Architecture | From RN **0.82+** the only architecture (no opt-out); 0.86 fully New Arch. | Fabric/TurboModules/Codegen actually in the build. |
| Node | Expo 57 min Node ~**22.13+**. | `.nvmrc`, EAS image, CI. |
| OTA | EAS Update: **runtimeVersion** protects native/JS compatibility; signature/channel/rollout. | No OTA for native breaking changes; no unsigned updates. |
| Android 16 KB | Play 64-bit native libs; RN/plugins. | AAB, NDK/AGP, plugin `.so`. |

Note: Metro/Expo Go != production binary. A downloaded OTA != native compatibility. Do not assume managed workflow merely because native folders look untouched.

