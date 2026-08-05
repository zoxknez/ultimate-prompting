## 22. Plugin-i, scripting, dinamički import, serializacija i extension point-i

### 22.1 Obim audita

1. Inventariši Python plugin sisteme, entry point-e, dinamičke import-e, korisničke skripte, makroe, template-e, QML module, native plugin-e, codec-e i third-party ekstenzije.
2. Dokumentuj discovery putanje, trust izvor, verifikaciju potpisa ili hash-a, compatibility ugovor, dozvole, API površinu, process izolaciju, update, disable i uklanjanje.
3. Pregledaj `pickle`, `marshal`, `shelve`, unsafe YAML, object hook-ove, dinamičko učitavanje klasa, `eval`, `exec`, izvršavanje template-a i expression engine-e.
4. Proceni pristup plugin-a fajl sistemu, mreži, credential-ima, UI-ju, clipboard-u, uređajima, bazi, updater-u i privilegovanim helper-ima.
5. Otkrij import shadowing, writable plugin putanje, namespace kolizije, dependency konflikte, ABI mismatch, propagation crash-a i startup denial of service.
6. Definiši ponašanje za nekompatibilne, korumpirane, zlonamerne, revoked, spore, crashujuće ili napuštene plugin-e.

### 22.2 Obavezna verifikacija

1. Pokušaj učitavanje plugin-a sa user-writable lokacija, trenutnog direktorijuma, removable medija, network share-a i tampered package lokacija.
2. Prosledi nepoverljive serializovane objekte, template-e, izraze, skripte i konfiguraciju; potvrdi stroge formate i bezbedan kvar.
3. Testiraj plugin timeout, crash, infinite loop, prekomernu memoriju, dependency konflikt, API mismatch, update, revocation i disable/recovery.
4. Koristi process izolaciju ili namerno ograničen capability model za nepoverljiv extension kod; dokumentuj residual risk kada pravi sandbox nije dostupan.
5. Odbaci arbitrary-code extension funkcije predstavljene kao bezbedne bez eksplicitnih trust, distribution, permission i incident kontrola.

