## Operativni Ugovor

1. Status: `POTVRDJENO` / `DELIMICNO_POTVRDJENO` / `NEPROVERENO` / `NIJE_PRIMENJIVO` / `ODBACENO`.
2. Ne izmisli rerender, JS-thread block, leak, TurboModule crash, OTA mismatch, ANR dok nema dokaza.
3. Za komandu: OS, Node, pm, RN, Expo, Android/iOS toolchain, target, profil, exit, artefakti, da li je objavljeno.
4. Ne izmisli expo-doctor, EAS build/update, signing, device, profiler output.
5. Ne brisi lock; ne sirok upgrade; ne `expo prebuild --clean` bez pregleda; ne menjaj appId/Bundle ID/EAS project/runtimeVersion naslepo; **ne objavljuj OTA tokom audita**; ne iskljucuj New Arch kao trajno resenje na nepodrzanoj liniji.
6. Ne prikazuj keystore, Apple keys, Expo/EAS tokens, update private keys, user data. Sve u JS bundle/native/OTA smatraj napadacu dostupnim.
7. Expo Go != production. Emulator != device.

