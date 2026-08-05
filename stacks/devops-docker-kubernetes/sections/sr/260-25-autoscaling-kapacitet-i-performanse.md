## 25. Autoscaling, kapacitet i performanse

**Cilj:** Ispuni potraznju bez nestabilnog skaliranja, skrivene saturacije ili nekontrolisanog troska.

### 25.1 Obavezne provere

1. Uspostavi workload model, kriticne putanje, concurrency, throughput, latencijske percentile, dubinu reda, burst, sezonalnost, rast i limite zavisnosti.
2. Izmeri CPU, memory, GC, file descriptor-e, konekcije, thread-ove, pool-ove, IOPS, throughput, disk, mrezu, DNS, API rate limite, startup i scheduling latenciju.
3. Audituj HPA, VPA, KEDA ili custom metrike za kvalitet signala, target semantiku, stabilizaciju, scale-up i scale-down policy, nedostajuce metrike, zero state i cooldown.
4. Audituj cluster autoscaler ili provider autoscaling za node grupe, zone, taint-ove, arhitekture, kvote, daemon overhead, PDB, local storage, scale-from-zero, konsolidaciju i interruption.
5. Proveri da request-i podrzavaju scheduling i capacity planning, dok limiti ne stvaraju throttling, OOM petlje, noisy-neighbor ponasanje ili laznu efikasnost.
6. Pokreni baseline, ocekivani peak, burst, soak, degradation, failover, cold-start i recovery testove u reprezentativnom okruzenju.
7. Koreliraj aplikacione metrike, infrastrukturnu saturaciju, korisnicku latenciju, greske, retry, starost reda i trosak tokom testova.
8. Definisi capacity headroom, quota alarme, lead time nabavke ili kvote i degradation ponasanje pre iscrpljivanja.

### 25.2 Minimalni dokazi

- Workload model i pretpostavke kapaciteta.
- Rezultati load, scaling, saturation, recovery i cost testova.
- Preporuka resursa i autoscaling-a sa izmerenim kompromisima.

### 25.3 Kriterijumi izlaza

1. Kriticni tokovi ispunjavaju definisane SLO-e pri ocekivanom peak-u sa prihvacenim headroom-om.
2. Autoscaling konvergira bez oscilacije, nekontrolisanog reda, nedostupnog kapaciteta ili prevelikog troska.
3. Rizici iscrpljivanja i kvota imaju akciona rana upozorenja i degradation planove.

