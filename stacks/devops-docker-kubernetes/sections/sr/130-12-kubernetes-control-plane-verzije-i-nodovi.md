## 12. Kubernetes control plane, verzije i nodovi

**Cilj:** Potvrdi podrzane temelje klastera, bezbednost upgrade-a i failure domain-e.

### 12.1 Obavezne provere

1. Popisi distribuciju, provider-a, region, control-plane verziju, node verzije, dodatke, CRI, CNI, CSI, kube-proxy mode, DNS, ingress, admission, autoscaler i lifecycle podrske.
2. Proveri podrzan version skew između control plane-a, kubelet-a, kube-proxy-ja, kubectl-a, dodataka, operator-a, API-ja i ogranicenja managed provider-a.
3. Skeniraj manifeste i live resurse za deprecated ili uklonjene API-je, conversion zavisnosti, nekompatibilne CRD-ove i webhook upgrade blokere.
4. Proveri izlozenost control-plane endpoint-a, privatni pristup, audit logging, encryption konfiguraciju, maintenance policy, backup-e i granice odgovornosti provider-a.
5. Pregledaj node pool-ove, operativne sisteme, image-e, patch cadence, taint-ove, label-e, arhitekturu, zone, kapacitet, bootstrap, metadata pristup i instance identitet.
6. Testiraj zamenu noda, drain, disruption, upgrade surge, otkaz noda, pretpostavke gubitka zone i oporavak kriticnih dodataka.
7. Za self-managed control plane audituj etcd topologiju, peer i client TLS, encryption, backup, compaction, defragmentation, quorum, restore i pristup.

### 12.2 Minimalni dokazi

- Inventar cluster komponenti i lifecycle-a podrske.
- Izvestaj version skew-a i deprecated API-ja sa upgrade blokerima.
- Dokaz node ili zone disruption-a i control-plane recovery dokaz gde je primenljivo.

### 12.3 Kriterijumi izlaza

1. Verzije klastera i dodataka su podrzane ili imaju odobrenu vremenski ogranicenu remedijaciju.
2. Upgrade blokeri, uklonjeni API-ji i webhook zavisnosti su poznati pre izmene.
3. Pretpostavke otkaza noda i control plane-a su potvrđene, a ne samo dokumentovane.

