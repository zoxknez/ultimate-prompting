## 14. Pod Security, admission i izolacija

**Cilj:** Nametni merljiv baseline izolacije workload-a sa kontrolisanim izuzecima.

### 14.1 Obavezne provere

1. Klasifikuj namespace-ove i workload-e prema aktuelnim Pod Security Standards profilima i dokumentuj zasto svaki izuzetak postoji.
2. Konfigurisi Pod Security Admission ili ekvivalentni policy sloj sa namernim `enforce`, `audit` i `warn` verzijama i label-ima.
3. Proveri efektivni securityContext na pod i container nivou: UID, GID, supplemental group-e, fsGroup, capability-je, privilege escalation, root filesystem, seccomp, AppArmor ili SELinux.
4. Audituj host namespace-ove, host portove, device plugin-e, hostPath, CSI driver-e, proc mount, sysctl, runtimeClass, sandbox runtime-e i privileged sistemske workload-e.
5. Spreci bypass preko neoznacenih namespace-ova, prava kreiranja namespace-a, exempt korisnika, service account-a, runtime class-a, debug container-a ili webhook failure policy-ja.
6. Testiraj odbijene i prihvacene manifeste, upgrade ponasanje, outage policy kontrolera i istek hitnog izuzetka.

### 14.2 Minimalni dokazi

- Matrica security profila namespace-a i izuzetaka.
- Admission test korpus sa ocekivanim i stvarnim odlukama.
- Inventar efektivnih privilegija kriticnih i sistemskih workload-a.

### 14.3 Kriterijumi izlaza

1. Restricted ili ekvivalentan posture je nametnut gde je moguce, a izuzeci su uski, imaju vlasnika i rok.
2. Nijedan trivijalan namespace, identity, runtime ili webhook bypass nije ostao.
3. Otkaz policy sloja ne propusta precutno nebezbedne workload-e osim ako je to namerno dizajnirano i prihvaceno.

