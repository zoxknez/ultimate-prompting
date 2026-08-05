## 10. Container runtime i host hardening

**Cilj:** Smanji runtime privilegije i blast radius izlaska na host.

### 10.1 Obavezne provere

1. Proveri engine, containerd, runc, kernel, cgroups, storage driver, seccomp, AppArmor ili SELinux, user namespace, rootless mode i status podrske.
2. Odbaci privileged mode, host PID, host IPC, host network, mount Docker socket-a, sirok device pristup i proizvoljan hostPath osim ako je posebno opravdano i izolovano.
3. Ukloni sve capability-je i dodaj samo dokazane potrebe. Nametni no-new-privileges, read-only root filesystem, ogranicene writable volume-e i kontrolisan proc i sys pristup.
4. Postavi CPU, memory, PID, file-descriptor, ephemeral-storage, log i process limite na osnovu izmerenog ponasanja i semantike otkaza.
5. Proveri izlozenost daemon API-ja, authorization plugin-e, vlasnistvo socket-a, TLS, remote pristup, auditabilnost i odvajanje od nepouzdanih korisnika.
6. Testiraj graceful stop, prinudni termination, restart policy, log rotation, disk pressure, OOM i ponasanje pri ostecenom writable stanju.

### 10.2 Minimalni dokazi

- Runtime security konfiguracija i efektivne privilegije procesa.
- Inventar host izlozenosti i mount-ova sa opravdanjem.
- Rezultati kontrolisanih testova termination-a, pressure-a i restart-a.

### 10.3 Kriterijumi izlaza

1. Nijedna neopravdana privileged putanja ili host-control socket nije dostupan.
2. Limiti i restart ponasanje bezbedno otkazuju pod izmerenim pritiskom.
3. Runtime i host komponente su podrzane, patch-uju se definisanim procesom i observabilne su.

