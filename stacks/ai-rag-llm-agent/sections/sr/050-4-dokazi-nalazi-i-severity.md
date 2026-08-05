## 4. Dokazi, Nalazi I Severity

### 4.1 Sema Nalaza

Za svaki nalaz zabelezi:

```text
ID
severity: P0 | P1 | P2 | P3
status: OPEN | FIXED | CONTAINED | ACCEPTED | REJECTED | UNVERIFIED
komponenta
okruzenje
akter i tenant
untrusted input ili trigger
preduslovi
reprodukcija ili eval slucaj
evidence status
lokacija dokaza
root cause
security, privacy, quality, reliability, cost ili legal uticaj
blast radius
preporucena popravka
implementirana izmena, ako postoji
verifikacija i regression test
rollback ili containment
residual risk
vlasnik i rok, ako su poznati
```

### 4.2 AI-Specific Severity Model

Koristi zajednicki severity model, uz najmanje sledeca tumacenja:

- `P0`: potvrdjena cross-tenant ili privileged eksfiltracija podataka; neautentifikovana high-impact akcija; tool ili sandbox escape sa host uticajem; otkrivanje produkcione tajne; destruktivna produkciona akcija bez validnog odobrenja; materijalna kompromitacija safety-critical namene.
- `P1`: praktican prompt-injection put sa privilegovanom posledicom; retrieval ACL bypass; confused-deputy koriscenje alata; nedostajuca action-level autorizacija; neogranicena agent potrosnja ili loop; nebezbedno autonomno placanje, deployment, account, delete, shell ili communication dejstvo; materijalno krsenje provider retention ili privacy pravila.
- `P2`: merljiv nedostatak kvaliteta, retrieval-a, evaluacije, dostupnosti, latencije, troska, observability-ja, governance-a ili oporavka bez neposrednog kriticnog uticaja.
- `P3`: maintainability, dokumentacija, imenovanje, low-impact UX ili neblokirajuca konzistentnost.

Severity se odredjuje prema uticaju i iskoristivosti, a ne prema broju propustenih best practice pravila.

### 4.3 Log Komandi I Evaluacija

Za svaku izvrsenu komandu ili evaluaciju zabelezi:

```text
command ili eval ID
cwd ili servis
runtime i toolchain
verzije modela, providera, prompta, index-a, dataset-a i konfiguracije
input dataset ili fixture ID
seed, temperature, sampling i broj ponavljanja gde je primenjivo
vreme pocetka i zavrsetka
exit status
summary metrike
upozorenja i greske
lokacija artefakta ili trace-a
execution environment: local | container | CI | staging | production-read-only
```

Ne prijavljuj agregirane metrike bez cuvanja osnovne run konfiguracije i skupa uzoraka.

