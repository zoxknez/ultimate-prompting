## 37. Obavezni adversarial i failure scenariji

### 37.1 S1 - Brzo ponovljena UI akcija pokreće dupli ne-idempotent rad.

1. Definiši setup, trigger, očekivanu invarijantu, observable dokaz, cleanup i pass/fail kriterijum.
2. Prvo pokreni u najužem bezbednom izolovanom okruženju, zatim proširi na packaged production-like uslove.
3. Zabeleži da li su prevencija, detekcija, containment, recovery, korisničko uputstvo i telemetrija radili kako je projektovano.

### 37.2 S2 - Prozor, model ili nalog se menja pre povratka odloženog worker rezultata.

1. Definiši setup, trigger, očekivanu invarijantu, observable dokaz, cleanup i pass/fail kriterijum.
2. Prvo pokreni u najužem bezbednom izolovanom okruženju, zatim proširi na packaged production-like uslove.
3. Zabeleži da li su prevencija, detekcija, containment, recovery, korisničko uputstvo i telemetrija radili kako je projektovano.

### 37.3 S3 - QObject receiver se uništava dok signali, timer-i, network reply-i ili callback-ovi ostaju queued.

1. Definiši setup, trigger, očekivanu invarijantu, observable dokaz, cleanup i pass/fail kriterijum.
2. Prvo pokreni u najužem bezbednom izolovanom okruženju, zatim proširi na packaged production-like uslove.
3. Zabeleži da li su prevencija, detekcija, containment, recovery, korisničko uputstvo i telemetrija radili kako je projektovano.

### 37.4 S4 - GUI thread je blokiran, reentered ili direktno ažuriran iz worker-a.

1. Definiši setup, trigger, očekivanu invarijantu, observable dokaz, cleanup i pass/fail kriterijum.
2. Prvo pokreni u najužem bezbednom izolovanom okruženju, zatim proširi na packaged production-like uslove.
3. Zabeleži da li su prevencija, detekcija, containment, recovery, korisničko uputstvo i telemetrija radili kako je projektovano.

### 37.5 S5 - Worker, asyncio task, subprocess ili helper pada tokom kritične operacije.

1. Definiši setup, trigger, očekivanu invarijantu, observable dokaz, cleanup i pass/fail kriterijum.
2. Prvo pokreni u najužem bezbednom izolovanom okruženju, zatim proširi na packaged production-like uslove.
3. Zabeleži da li su prevencija, detekcija, containment, recovery, korisničko uputstvo i telemetrija radili kako je projektovano.

### 37.6 S6 - Aplikacija se zatvara, logout-uje, menja workspace, uspavljuje ili update-uje tokom in-flight rada.

1. Definiši setup, trigger, očekivanu invarijantu, observable dokaz, cleanup i pass/fail kriterijum.
2. Prvo pokreni u najužem bezbednom izolovanom okruženju, zatim proširi na packaged production-like uslove.
3. Zabeleži da li su prevencija, detekcija, containment, recovery, korisničko uputstvo i telemetrija radili kako je projektovano.

### 37.7 S7 - Disk postaje pun, read-only, zaključan, spor ili nedostupan tokom write-a, migracije, download-a ili update-a.

1. Definiši setup, trigger, očekivanu invarijantu, observable dokaz, cleanup i pass/fail kriterijum.
2. Prvo pokreni u najužem bezbednom izolovanom okruženju, zatim proširi na packaged production-like uslove.
3. Zabeleži da li su prevencija, detekcija, containment, recovery, korisničko uputstvo i telemetrija radili kako je projektovano.

### 37.8 S8 - Dve instance aplikacije ili stale lock-ovi menjaju isto lokalno stanje.

1. Definiši setup, trigger, očekivanu invarijantu, observable dokaz, cleanup i pass/fail kriterijum.
2. Prvo pokreni u najužem bezbednom izolovanom okruženju, zatim proširi na packaged production-like uslove.
3. Zabeleži da li su prevencija, detekcija, containment, recovery, korisničko uputstvo i telemetrija radili kako je projektovano.

### 37.9 S9 - Mreža postaje spora, offline, redirected, proxied, sa rotiranim sertifikatom ili partial responsive.

1. Definiši setup, trigger, očekivanu invarijantu, observable dokaz, cleanup i pass/fail kriterijum.
2. Prvo pokreni u najužem bezbednom izolovanom okruženju, zatim proširi na packaged production-like uslove.
3. Zabeleži da li su prevencija, detekcija, containment, recovery, korisničko uputstvo i telemetrija radili kako je projektovano.

### 37.10 S10 - Autentikacija ističe konkurentno i refresh, logout, revocation ili promena naloga ulaze u race.

1. Definiši setup, trigger, očekivanu invarijantu, observable dokaz, cleanup i pass/fail kriterijum.
2. Prvo pokreni u najužem bezbednom izolovanom okruženju, zatim proširi na packaged production-like uslove.
3. Zabeleži da li su prevencija, detekcija, containment, recovery, korisničko uputstvo i telemetrija radili kako je projektovano.

### 37.11 S11 - Neautorizovan deep link, IPC, WebChannel, plugin, lokalni fajl ili izmenjeno lokalno stanje pokušava privilegovanu akciju.

1. Definiši setup, trigger, očekivanu invarijantu, observable dokaz, cleanup i pass/fail kriterijum.
2. Prvo pokreni u najužem bezbednom izolovanom okruženju, zatim proširi na packaged production-like uslove.
3. Zabeleži da li su prevencija, detekcija, containment, recovery, korisničko uputstvo i telemetrija radili kako je projektovano.

### 37.12 S12 - Malformed, oversized, recursive, polyglot ili path-traversing fajl stiže do import ili preview putanje.

1. Definiši setup, trigger, očekivanu invarijantu, observable dokaz, cleanup i pass/fail kriterijum.
2. Prvo pokreni u najužem bezbednom izolovanom okruženju, zatim proširi na packaged production-like uslove.
3. Zabeleži da li su prevencija, detekcija, containment, recovery, korisničko uputstvo i telemetrija radili kako je projektovano.

### 37.13 S13 - Writable trenutni direktorijum, PATH, plugin putanja, temp putanja ili user direktorijum pokušava hijacking modula, DLL-a, helper-a ili resursa.

1. Definiši setup, trigger, očekivanu invarijantu, observable dokaz, cleanup i pass/fail kriterijum.
2. Prvo pokreni u najužem bezbednom izolovanom okruženju, zatim proširi na packaged production-like uslove.
3. Zabeleži da li su prevencija, detekcija, containment, recovery, korisničko uputstvo i telemetrija radili kako je projektovano.

### 37.14 S14 - Queue, thread pool, event loop, memorija, handle-ovi, disk ili GPU postaju saturisani pod burst i soak opterećenjem.

1. Definiši setup, trigger, očekivanu invarijantu, observable dokaz, cleanup i pass/fail kriterijum.
2. Prvo pokreni u najužem bezbednom izolovanom okruženju, zatim proširi na packaged production-like uslove.
3. Zabeleži da li su prevencija, detekcija, containment, recovery, korisničko uputstvo i telemetrija radili kako je projektovano.

### 37.15 S15 - Native ekstenzija, Qt plugin, codec, driver ili grafički backend nedostaje, nekompatibilan je ili pada.

1. Definiši setup, trigger, očekivanu invarijantu, observable dokaz, cleanup i pass/fail kriterijum.
2. Prvo pokreni u najužem bezbednom izolovanom okruženju, zatim proširi na packaged production-like uslove.
3. Zabeleži da li su prevencija, detekcija, containment, recovery, korisničko uputstvo i telemetrija radili kako je projektovano.

### 37.16 S16 - Installer ili updater je prekinut, tampered, bez prostora, blokiran antivirusom ili ne može zameniti aktivne fajlove.

1. Definiši setup, trigger, očekivanu invarijantu, observable dokaz, cleanup i pass/fail kriterijum.
2. Prvo pokreni u najužem bezbednom izolovanom okruženju, zatim proširi na packaged production-like uslove.
3. Zabeleži da li su prevencija, detekcija, containment, recovery, korisničko uputstvo i telemetrija radili kako je projektovano.

### 37.17 S17 - Stari i novi binary-ji, helper-i, plugin-i, schema-e ili serverski API-ji se preklapaju tokom staged rollout-a i rollback-a.

1. Definiši setup, trigger, očekivanu invarijantu, observable dokaz, cleanup i pass/fail kriterijum.
2. Prvo pokreni u najužem bezbednom izolovanom okruženju, zatim proširi na packaged production-like uslove.
3. Zabeleži da li su prevencija, detekcija, containment, recovery, korisničko uputstvo i telemetrija radili kako je projektovano.

### 37.18 S18 - Signing sertifikat ili update ključ ističe, rotira, opoziva se ili se sumnja da je kompromitovan.

1. Definiši setup, trigger, očekivanu invarijantu, observable dokaz, cleanup i pass/fail kriterijum.
2. Prvo pokreni u najužem bezbednom izolovanom okruženju, zatim proširi na packaged production-like uslove.
3. Zabeleži da li su prevencija, detekcija, containment, recovery, korisničko uputstvo i telemetrija radili kako je projektovano.

### 37.19 S19 - Restore backup-a se dešava na čistoj mašini sa nedostajućim keyring-om, promenjenim putanjama, drugim korisnikom ili novijim OS-om.

1. Definiši setup, trigger, očekivanu invarijantu, observable dokaz, cleanup i pass/fail kriterijum.
2. Prvo pokreni u najužem bezbednom izolovanom okruženju, zatim proširi na packaged production-like uslove.
3. Zabeleži da li su prevencija, detekcija, containment, recovery, korisničko uputstvo i telemetrija radili kako je projektovano.

### 37.20 S20 - Zlonamerna zavisnost, plugin, helper, paket ili build runner zahteva containment i trusted rebuild.

1. Definiši setup, trigger, očekivanu invarijantu, observable dokaz, cleanup i pass/fail kriterijum.
2. Prvo pokreni u najužem bezbednom izolovanom okruženju, zatim proširi na packaged production-like uslove.
3. Zabeleži da li su prevencija, detekcija, containment, recovery, korisničko uputstvo i telemetrija radili kako je projektovano.

