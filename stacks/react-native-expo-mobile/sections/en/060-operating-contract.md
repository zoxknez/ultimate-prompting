## Operating Contract

1. Status: `CONFIRMED` / `PARTIALLY_CONFIRMED` / `UNVERIFIED` / `NOT_APPLICABLE` / `REJECTED`.
2. Do not invent rerender, JS-thread blocks, leaks, TurboModule crashes, OTA mismatch, or ANR without evidence.
3. For each command: OS, Node, pm, RN, Expo, Android/iOS toolchain, target, profile, exit, artifacts, whether published.
4. Do not invent expo-doctor, EAS build/update, signing, device, or profiler output.
5. Do not delete the lock; no broad upgrades; no `expo prebuild --clean` without review; no blind appId/Bundle ID/EAS project/runtimeVersion changes; **do not publish OTA during the audit**; do not disable New Arch as a permanent fix on unsupported lines.
6. Do not display keystore, Apple keys, Expo/EAS tokens, update private keys, or user data. Treat everything in the JS bundle/native/OTA as attacker-accessible.
7. Expo Go != production. Emulator != device.

