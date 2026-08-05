## Istrazivacki Baseline - 5. avgust 2026.

Ovaj baseline je polaziste. Pre preporuke proveri reactnative.dev, docs.expo.dev, EAS docs i stvarne lock/native konfiguracije.

| Komponenta | Potvrdjeno stanje na 5. avgust 2026. | Obavezna provera pri auditu |
| --- | --- | --- |
| Expo SDK | **57** (stable od 30. jun 2026.; npr. 57.0.x). | `expo` package, `npx expo-doctor`, `npx expo install --check`. |
| React Native | **0.86** (Expo 57 matrica; RN 0.86 ~jun 2026.). | bare vs Expo, peer deps, upgrade helper. |
| React | **19.2.x** (npr. **19.2.3** u SDK 57). | uskladjivanje sa Expo matrix. |
| Hermes | Default JS engine; bytecode/format menja se sa RN - vezati za **runtimeVersion**. | engine, source maps, reanimated memory note (0.85+). |
| New Architecture | Od RN **0.82+** jedina arhitektura (nema opt-out); 0.86 fully New Arch. | Fabric/TurboModules/Codegen stvarno u buildu. |
| Node | Expo 57 min Node ~**22.13+**. | `.nvmrc`, EAS image, CI. |
| OTA | EAS Update: **runtimeVersion** stiti native/JS kompatibilnost; potpis/kanal/rollout. | Ne OTA za native breaking; ne unsigned. |
| Android 16 KB | Play 64-bit native libs; Flutter/RN/plugins. | AAB, NDK/AGP, plugin `.so`. |

Napomena: Metro/Expo Go != production binary. OTA preuzimanje != native compatibility. Ne pretpostavljaj managed samo jer nema rucnih native izmena.

