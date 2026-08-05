## Rezim Rada

Default: `AUDIT_AND_SAFE_FIX`.

| Rezim | Dozvoljeno |
| --- | --- |
| `AUDIT_ONLY` | Bez izmene source/lock/signing/EAS kanala/store. |
| `AUDIT_AND_SAFE_FIX` | Niskorizicne popravke + testovi; plan za native/OTA/data. |
| `FULL_IMPLEMENTATION` | Male korake; ne publish build/OTA bez odobrenja. |
| `FIX_CONFIRMED_ISSUES` | Samo potvrdjeni. |
| `SECURITY_AUDIT` | Auth, tokens, deep links, WebView, native/JSI, storage, network, OTA trust, signing. |
| `PERFORMANCE_AUDIT` | Startup, Hermes, JS/UI thread, Fabric, lists, memory, images, JSI, DB, battery; release profile. |
| `NEW_ARCHITECTURE_MIGRATION` | Legacy inventar, Turbo/Fabric/Codegen/JSI, threading, rollback. |
| `EXPO_MIGRATION` | bare/CNG/SDK, Router, EAS, config plugins, dev clients. |
| `RELEASE_AND_OTA_AUDIT` | Native build, runtimeVersion, channels, signing, rollout, local-data, store. |

