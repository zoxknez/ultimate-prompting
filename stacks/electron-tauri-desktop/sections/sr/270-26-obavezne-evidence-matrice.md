## 26. Obavezne evidence matrice

### 26.1 Source-to-runtime matrica

| source commit | razreseni graf | builder | paket | potpis | distribution objekat | instalirani binary | runtime proces | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` |

### 26.2 Matrica privilegija prozora i webview-a

| prozor/webview | origin | session/partition | preload/capability | dozvole | podaci/nalog | navigacija | vlasnik | testovi | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` |

### 26.3 IPC i command matrica

| kanal/komanda | caller | sema | autentikacija | autorizacija | scope | side effect | idempotency | limiti | test | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` |

### 26.4 Filesystem i external-open matrica

| operacija | izvor | kanonikalizacija | dozvoljeni scope | symlink/race odbrana | dozvole | audit | test | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` |

### 26.5 Matrica lokalnih podataka i migracija

| skladiste/putanja | vlasnik | osetljivost | sema/verzija | migracija | backup | restore | izolacija naloga | brisanje | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` |

### 26.6 Network i local-service matrica

| klijent/listener | endpoint | trust | auth | TLS/peer provera | timeout | retry/backpressure | podaci | test | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` |

### 26.7 Dependency i native-code matrica

| komponenta | razresena verzija | izvor | isporucena | privilegija | native/build kod | advisory | kompatibilnost | vlasnik | akcija |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` |

### 26.8 Matrica artefakta, signing-a i prodavnice

| platforma/kanal | artefakt | hash | sadrzaj paketa | signing identitet | timestamp/notary | prodavnica/repository | verifikacija | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` |

### 26.9 Update i rollback matrica

| izvorna verzija | target | platforma/kanal | metadata | potpis | migracija podataka | failure point | rollback/recovery | test | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` |

### 26.10 Platform i installer matrica

| OS/verzija | arhitektura | format | cista instalacija | upgrade | repair | rollback | uninstall | OS integracija | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` |

### 26.11 Performance i resource matrica

| tok | uredjaj/profil | budzet | izmereno | usko grlo | popravka | regression test | preostali rizik | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` |

### 26.12 Operational readiness matrica

| kontrola | vlasnik | dokaz | alert | runbook | abort prag | rollback | poslednja vezba | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` |

