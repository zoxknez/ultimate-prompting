## 33. Bezbedna popravka, rollout i verifikacija

**Cilj:** Pretvori potvrđene nalaze u kontrolisane, reverzibilne izmene potkrepljene dokazima.

### 33.1 Obavezne provere

1. Registruj nalaz, invarijantu, vlasnika, preduslove, ocekivani efekat, blast radius, granicu odobrenja, verifikaciju, rollout, stop uslove, rollback i rezidualni rizik pre editovanja.
2. Napravi najmanju koherentnu izmenu. Ne mesaj nepovezane upgrade-e, formatiranje, refactor-e, policy izmene i operativne izmene.
3. Potvrdi sintaksu, semu, render, lint, unit testove, policy, security, plan, diff i izolovano runtime ponasanje pre sireg rollout-a.
4. Backup-uj ili snapshot-uj pogođeno stanje gde je prikladno i proveri da je backup upotrebljiv pre destruktivne ili stateful izmene.
5. Rollout-uj kroz najbezbednije reprezentativno okruzenje, zatim canary ili ogranicen opseg, sa imenovanim posmatracima i definisanim periodom posmatranja.
6. Izmeri korisnicki uticaj, SLO, greske, saturaciju, security signale, ispravnost podataka, trosak i control-plane health tokom rollout-a.
7. Odmah zaustavi ili rollback-uj kada se dostigne stop uslov. Zabelezi stvarni rezultat rollback-a umesto pretpostavke uspeha.
8. Ponovi fokusirane regresione, failure, security i recovery testove nakon izmene i azuriraj dokumentaciju, vlasnistvo i runbook-ove.

### 33.2 Minimalni dokazi

- Trag nalaz-izmena sa review-om i odobrenjem.
- Dokazi pre, tokom, posle i pri rollback-u.
- Fokusirani regresioni dokaz i zapis rezidualnog rizika.

### 33.3 Kriterijumi izlaza

1. Svaka primenjena izmena je pripisiva, review-ovana, reverzibilna, posmatrana i potvrđena.
2. Nije doslo do neplaniranog sirokog upgrade-a, destruktivnog side effect-a ili skrivenog prihvatanja rizika.
3. Rezidualni rizik ima eksplicitnog vlasnika i odluku.

