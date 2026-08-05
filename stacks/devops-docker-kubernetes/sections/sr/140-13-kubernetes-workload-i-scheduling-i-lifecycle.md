## 13. Kubernetes workload-i, scheduling i lifecycle

**Cilj:** Obezbedi da workload-i predvidivo startuju, staju, skaliraju se, update-uju i otkazuju.

### 13.1 Obavezne provere

1. Audituj Deployment-e, StatefulSet-ove, DaemonSet-ove, Job-ove, CronJob-ove, custom workload-e, revizije, selektore, vlasnistvo, update strategije i history limite.
2. Razdvoji startup, readiness, liveness i gRPC probe semantiku. Proveri failure threshold-e, timeout-e, ponasanje zavisnosti i cenu probe-a.
3. Postavi izmerene request-e i opravdane limite za CPU, memory, ephemeral storage, huge page, GPU i extended resource-e.
4. Proveri terminationGracePeriodSeconds, preStop, obradu signala, connection draining, finalizer-e, prekid job-a i redosled gasenja.
5. Zajedno audituj affinity, anti-affinity, topology spread, taint-ove, toleration-e, prioritete, preemption, PDB i pretpostavke kapaciteta.
6. Testiraj rolling update, rollback, nedostupnu zavisnost, spor startup, OOM, disk pressure, node drain, duplu isporuku, retry job-a i propusteni schedule.
7. Obezbedi da init container-i, sidecar-i, ephemeral container-i i service-mesh injection ne skrivaju lifecycle, security ili resource otkaze.

### 13.2 Minimalni dokazi

- Renderovana i live workload konfiguracija sa efektivnim default vrednostima.
- Izmereni rezultati resursa, startup-a, shutdown-a, update-a i disruption-a.
- Matrica otkaza workload-a ukljucujuci Job-ove i stateful workload-e.

### 13.3 Kriterijumi izlaza

1. Kriticni workload-i imaju ispravne probe, resurse, shutdown, scheduling i disruption ponasanje.
2. Rollout i rollback se zavrsavaju unutar definisanih granica bezbednosti i dostupnosti.
3. Retry i scheduling ponasanje ne stvaraju nekontrolisano dupliranje, gubitak ili iscrpljivanje resursa.

