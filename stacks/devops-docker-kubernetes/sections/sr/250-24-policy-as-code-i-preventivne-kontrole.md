## 24. Policy as code i preventivne kontrole

**Cilj:** Pretvori kriticne invarijante u testirane, observabilne i upravljive kontrole.

### 24.1 Obavezne provere

1. Definisi kriticne invarijante za identitet, privilegije, mrezu, artefakte, resurse, encryption, javnu izlozenost, lokaciju podataka, label-e, vlasnistvo, verzije i backup.
2. Mapiraj svaku invarijantu na preventivne, detektivne, responsive ili accepted-risk kontrole kroz source, CI, registry, admission, cloud, runtime i monitoring slojeve.
3. Audituj policy source, review, testove, bundle-ove, distribuciju, versioning, vlasnistvo, proces izuzetka, istek, telemetriju i rollback.
4. Koristi reprezentativne pozitivne, negativne, granicne, legacy, emergency i malicious fixture-e. Potvrdi policy rezultate pre enforce-a.
5. Rollout-uj u audit ili warn modu gde je prikladno, izmeri false positive-e i bypass-e, pa nametni uz eksplicitan plan izmene.
6. Proveri dostupnost policy engine-a, timeout, cache, zastareli bundle, fail-open ili fail-closed ponasanje, break-glass i control-plane zavisnosti.
7. Ne dupliraj kontrole slepo. Identifikuj autoritativni sloj i ocekivano ponasanje kada se slojevi ne slazu.

### 24.2 Minimalni dokazi

- Matrica invarijanta-kontrola sa vlasnicima i enforcement tackama.
- Policy test korpus, pokrivenost, izuzeci, false-positive i bypass dokazi.
- Rezultati testa otkaza policy engine-a i rollback-a.

### 24.3 Kriterijumi izlaza

1. P0 i P1 invarijante imaju efektivne preventivne ili brzo detektivne kontrole.
2. Izuzeci su uski, pripisivi, vremenski ograniceni, vidljivi i testirani.
3. Ponasanje pri otkazu policy sloja je razumljivo i ne moze stvoriti neprimecen sirok bypass.

