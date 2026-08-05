## 2. Aktuelni Istrazivacki Baseline - Ponovo Proveriti Pre Svakog Audita

Na datum baseline-a primarni izvori su navodili:

| Komponenta | Baseline 2026-08-05 | Obavezna audit akcija |
| --- | --- | --- |
| Android Studio | Quail 3, `2026.1.3`, stable channel | Proveri instalirani IDE i AGP opseg koji CI podrzava. |
| Android Gradle Plugin | `9.3.x` stable; `9.4` preview | Ne preporucuj preview po default-u. Proveri tacne release notes i plugin kompatibilnost. |
| Gradle / JDK | AGP 9.3 zahteva Gradle `9.5.0`; JDK `17` | Proveri wrapper checksum, daemon JDK, toolchain-e, CI image i lokalni paritet. |
| Kotlin | `2.4.10` objavljen 2026-07-14 | Pre unapredjenja proveri Android, KSP, Compose, serialization i plugin kompatibilnost. |
| SDK | AGP 9.3 podrzava do API `37`; API 37 zahteva najmanje AGP `9.1.1` | Zabelezi stvarni compileSdk i targetSdk. Ne izvodi Play podobnost iz compileSdk vrednosti. |
| Google Play target API | Nove aplikacije i update-i moraju ciljati API `36+` od 2026-08-31, uz aktuelne izuzetke | Pre release-a ponovo proveri aktuelni Play policy i kategoriju aplikacije. |
| 16 KB pages | Aplikacije koje ciljaju API 35+ na 64-bit Google Play uredjajima moraju podrzavati 16 KB; blokiranje release-a pocinje 2027-02-01 | Pregledaj svaku upakovanu native biblioteku, alignment, poreklo SDK-a i test dokaz. |

Ova tabela je datirana polazna tacka, a ne trajna istina.

