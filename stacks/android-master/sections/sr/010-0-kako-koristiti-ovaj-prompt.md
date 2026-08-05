## 0. Kako Koristiti Ovaj Prompt

### 0.1 Obavezni Ulazi

Prikupi ili izvedi i eksplicitno zabelezi:

| Polje | Vrednost |
| --- | --- |
| Aplikacija i repozitorijum | `[NAME / PATH / URL]` |
| Poslovna namena i kriticni user journey-i | `[PURPOSE / FLOWS]` |
| Distribucija | `[GOOGLE_PLAY / ENTERPRISE / SIDELOAD / OEM / MULTIPLE]` |
| Tip aplikacije | `[PHONE / TABLET / FOLDABLE / TV / WEAR / AUTO / MULTI-DEVICE]` |
| UI toolkit | `[COMPOSE / VIEWS / MIXED]` |
| Jezik | `[KOTLIN / JAVA / MIXED]` |
| Moduli | `[LIST OR UNKNOWN]` |
| minSdk / targetSdk / compileSdk | `[VALUES OR UNKNOWN]` |
| Android Studio / AGP / Gradle / JDK / Kotlin | `[VERSIONS OR UNKNOWN]` |
| Build varijante i product flavor-i | `[LIST OR UNKNOWN]` |
| Dependency injection | `[HILT / DAGGER / KOIN / MANUAL / OTHER]` |
| Perzistencija | `[ROOM / DATASTORE / FILES / SQLCIPHER / OTHER]` |
| Mreza | `[OKHTTP / RETROFIT / KTOR / WEBSOCKET / OTHER]` |
| Background rad | `[WORKMANAGER / FGS / ALARMS / FCM / NONE]` |
| Media i device API-ji | `[MEDIA3 / CAMERA / LOCATION / BLUETOOTH / NFC / USB / OTHER]` |
| Native kod i upakovani SDK-ovi | `[NDK / JNI / RUST / C++ / .SO / NONE / UNKNOWN]` |
| Autentikacija i osetljivi podaci | `[DESCRIPTION]` |
| Analytics, crash i performance alati | `[LIST OR UNKNOWN]` |
| CI/CD i signing | `[DESCRIPTION OR UNKNOWN]` |
| Compliance i policy opseg | `[GDPR / CHILDREN / HEALTH / FINANCE / ENTERPRISE / OTHER / NONE / UNKNOWN]` |
| Rezim rada | `[AUDIT_ONLY / AUDIT_AND_SAFE_FIX / FULL_IMPLEMENTATION / FIX_CONFIRMED_ISSUES / RELEASE_READINESS_AUDIT]` |

### 0.2 Pravilo Za Nedostajuce Informacije

Ne blokiraj ceo audit zato sto neki ulazi nedostaju.

1. Zakljucke izvodi samo iz repozitorijuma, Gradle-a, manifesta, generisanih artefakata, CI konfiguracije, device dokaza i autoritativne dokumentacije.
2. Neresene pretpostavke oznaci kao `UNVERIFIED`.
3. Nastavi sa bezbednim read-only proverama gde je moguce.
4. Trazi samo pristup ili kredencijale koji sustinski blokiraju potvrdu, popravku ili verifikaciju.
5. Nedostatak dokaza nikada ne pretvaraj u pozitivan zakljucak.
6. Ne pretpostavljaj da README, roadmap, screenshot-ovi, issue tracker ili komentari tacno opisuju trenutnu implementaciju.

### 0.3 Rezimi Rada

| Rezim | Dozvoljeno ponasanje |
| --- | --- |
| `AUDIT_ONLY` | Pregledaj, bezbedno build-uj, testiraj, profilisi i izvesti. Ne menjaj source, lockfile-ove, seme, signing, Play konfiguraciju ili produkcione podatke. |
| `AUDIT_AND_SAFE_FIX` | Primeni potvrdjene, low-risk i reverzibilne popravke sa fokusiranim regression testovima. Vece ili rizicne izmene samo planiraj. |
| `FULL_IMPLEMENTATION` | Implementiraj opravdane izmene postepeno, uz backup, bezbedne migracije, verifikaciju i rollback. |
| `FIX_CONFIRMED_ISSUES` | Menjaj samo nalaze koji su vec registrovani i potvrdjeni. Ne siri opseg precutno. |
| `RELEASE_READINESS_AUDIT` | Prioritet daj release varijantama, signing-u, R8, native kompatibilnosti, policy zahtevima, kriticnim tokovima, observability-ju i rollback-u. |

Ako rezim nije naveden, koristi `AUDIT_AND_SAFE_FIX`.

