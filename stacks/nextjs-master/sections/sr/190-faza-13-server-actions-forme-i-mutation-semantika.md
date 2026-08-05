## Faza 13 - Server Actions, forme i mutation semantika

Tretiraj svaki Server Action i form mutation kao privilegovanu udaljenu komandu sa eksplicitnim identitetom, autorizacijom, validacijom, transakcijom, idempotency-jem i recovery-jem.

### Zahtevi audita

- Inventarisi svaku use server funkciju, export-ovanu akciju, bound akciju, form action, imperativni poziv i indirektnu referencu.
- Autentifikuj i autorizuj unutar akcije koristeci aktuelni server state; ne veruj hidden poljima, bound ID-jevima, client state-u, Proxy-ju ili UI vidljivosti.
- Validiraj strukturu, semantiku, ownership, state transition, velicinu, file content, rate i poslovne invarijante.
- Definisi idempotency key, scope, duplicate response, expiry i ponasanje kroz retry, navigaciju, timeout, disconnect i crash.
- Koristi database constraint-e i transakcije; koordiniraj spoljne efekte outbox-om, reconciliation-om ili compensation-om.
- Pregledaj allowedOrigins, host/origin, body limite, encryption key ponasanje, rotaciju i multi-instance kompatibilnost.

### Obavezni dokazi

- Action matrica sa actor-om, tenant-om, schemom, authz-om, transakcijom, idempotency-jem, rate-om, cache efektom i owner-om.
- Constraint i transaction dokaz za kriticne invarijante.
- Origin, host, body-size, key i multi-instance config dokaz.
- Audit i reconciliation dokaz za spoljne efekte.

### Obavezni failure i acceptance testovi

- Replay-uj istu akciju pre, tokom i posle commit-a, timeout-a, redirect-a i restart-a.
- Promeni hidden ID-jeve, tenant, rolu, cenu, status i ownership polja.
- Posalji konkurentno iz vise tab-ova, uredjaja i actor-a protiv jedne invarijante.
- Rotiraj ili namerno razdvoji action encryption material i proveri kompatibilnost i recovery.

