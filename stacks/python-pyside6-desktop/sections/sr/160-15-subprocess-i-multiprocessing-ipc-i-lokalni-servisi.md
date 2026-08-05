## 15. Subprocess-i, multiprocessing, IPC i lokalni servisi

### 15.1 Obim audita

1. Inventariši subprocess-e, `multiprocessing`, helper executable-e, lokalne agente, servise, named pipe-ove, Unix socket-e, loopback HTTP, shared memory i file-based IPC.
2. Zabeleži resolution executable-a, argumente, environment, working directory, privilegije, vlasništvo, autentikaciju, framing, versioning, timeout i shutdown.
3. Pregledaj shell upotrebu, quoting, command injection, PATH hijacking, current-directory search, nasleđene handle-ove, curenje environment-a i writable executable lokacije.
4. Proceni multiprocessing start metode, frozen-application bootstrap, rekurzivni spawn, resource tracker ponašanje, konzistentnost shared state-a i crash recovery.
5. Tretiraj localhost i same-user IPC kao attacker-reachable dok autentikacija, autorizacija, dozvole i peer identitet nisu dokazani.
6. Definiši kompatibilnost za old/new GUI, helper, service, protokol, schema-u i update verzije.

### 15.2 Obavezna verifikacija

1. Pokreni iz instaliranih putanja i adversarial working direktorijuma da dokažeš trusted resolution executable-a i biblioteka.
2. Testiraj malformed, oversized, reordered, replayed, unauthenticated, cross-user, stale-version i partial IPC poruke.
3. Forsiraj helper crash, GUI crash, timeout, prekid pipe-a, dupli zahtev, upgrade overlap i shutdown tokom kritičnog rada.
4. Verifikuj privilege separation, least-privilege service naloge, OS ACL-ove, peer credential-e, request autorizaciju i potpisane/verzionisane helper-e.
5. Potvrdi da nakon kvara ne ostaje orphan proces, shared-memory segment, lock fajl, port listener, privremena tajna ili poluprimenjen side effect.

