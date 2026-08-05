## Rezim Rada

Ako nije zadat, koristi `AUDIT_AND_SAFE_FIX`.

| Rezim | Dozvoljeni rad |
| --- | --- |
| `AUDIT_ONLY` | Analiziraj i izvrsi bezbedne provere; ne menjaj source, dependency-je, lock fajlove, bazu ili infrastrukturu; dostavi precizan plan. |
| `AUDIT_AND_SAFE_FIX` | Implementiraj potvrdjene lokalne niskorizicne popravke i regresione testove; planiraj destruktivne, ugovorno nekompatibilne ili arhitektonski velike promene. |
| `FULL_IMPLEMENTATION` | Implementiraj opravdane popravke u malim proverljivim koracima; ne izvrsavaj destruktivne migracije bez backup/rollback strategije. |
| `FIX_CONFIRMED_ISSUES` | Popravi samo prethodno potvrdjene probleme; ne siri scope bez dokaza. |
| `SECURITY_AND_CONCURRENCY_AUDIT` | Fokus: race, deadlock, goroutine/task leak, cancellation, unsafe/FFI, input/network security, dependency rizici, tajne, idempotency, resource exhaustion. |
| `PERFORMANCE_AUDIT` | Fokus: realan workload, CPU, memorija, alokacije, GC, scheduler, contention, I/O, query-ji, latency percentile, benchmark i profiler dokazi. |

