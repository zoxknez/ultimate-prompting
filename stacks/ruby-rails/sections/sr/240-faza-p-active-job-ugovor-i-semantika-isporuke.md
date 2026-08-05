## Faza P - Active Job Ugovor I Semantika Isporuke

- Identifikuj stvarni adapter u svakom okruzenju i procesu; development `:async` ponasanje nije dokaz production trajnosti.
- Pretpostavi at-least-once isporuku osim ako jaca semantika nije dokazana end-to-end.
- Audituj serializaciju, GlobalID lookup, nedostajuce zapise, schema evoluciju, stari kod koji trosi nove argumente i novi kod koji trosi stare jobove.
- Definisi retry klase, backoff, jitter, maksimalan broj pokusaja, discard pravila, poison handling i operator workflow.
- Ucini efekte joba idempotentnim na database ili external-system granici, a ne samo proverom flag-a u memoriji.
- Meri queue age, vreme izvrsavanja, retry-je, failure-e, saturation i downstream pritisak po redu i job klasi.

