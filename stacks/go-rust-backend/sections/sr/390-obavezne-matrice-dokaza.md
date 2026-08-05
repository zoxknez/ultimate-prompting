## Obavezne matrice dokaza

Napravi svaku primenljivu matricu. Koristi `NOT_APPLICABLE` samo uz razlog i `UNVERIFIED` kada dokaz nije dostupan.

| ID | Matrica | Minimalne kolone |
| --- | --- | --- |
| M1 | Identitet source-a, toolchain-a i artefakta | komponenta | commit | toolchain | graf/lock | tag-ovi/feature-i | target/profile | artifact digest | runtime dokaz | status |
| M2 | Inventar executable-a, modula, crate-a i deployment-a | jedinica | jezik | entrypoint | vlasnik | podaci | mreža | privilegije | deployment | kritičnost | testovi |
| M3 | Go target i build-tag podrška | komanda/paket | GOOS | GOARCH | tag-ovi | cgo | libc | toolchain | build | test | artefakt | vlasnik |
| M4 | Rust target, feature, MSRV i profile podrška | crate/bin | target | feature-i | profile | MSRV | stable | native zavisnosti | build | test | artefakt | vlasnik |
| M5 | Ownership konkurentnosti i lifecycle-a | goroutine/task | kreator | resurs | limit | cancellation | join/supervision | panic | metrika | shutdown | test |
| M6 | Unsafe, cgo, FFI, native i ABI granica | granica | caller | callee | safety ugovor | ownership | ABI/layout | unwind | threading | validacija | tool dokaz | vlasnik |
| M7 | API, RPC, stream i protokolski ugovor | metoda/servis | authn | authz/vlasnik | validacija | limiti | deadline | idempotency | transakcija | kompatibilnost | negativni test |
| M8 | Poslovni tok promene stanja | tok | invarijanta | čitanja | lock-ovi | upisi | side effect-i | commit | retry | reconciliation | rollback | testovi |
| M9 | Kompatibilnost šeme podataka i migracije | promena | stari reader | stari writer | novi reader | novi writer | backfill | lock rizik | rollback | forward repair | restore test |
| M10 | Dependency i supply-chain poverenje | zavisnost/alat | izvor | pin/lock | licenca | advisory | build izvršavanje | native/unsafe | vlasnik | update | opoziv |
| M11 | SLO, kapacitet, overload i observability | tok | SLI | cilj | load model | usko grlo | admission limit | alert | dashboard | runbook | dokaz |
| M12 | Rollout, rollback, restore i incident spremnost | rizik | rollout gate | canary | abort signal | rollback akcija | data kompatibilnost | restore korak | RPO/RTO | vlasnik | dokaz probe |

