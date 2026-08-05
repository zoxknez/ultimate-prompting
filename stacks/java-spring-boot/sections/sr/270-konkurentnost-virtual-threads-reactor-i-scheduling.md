## Konkurentnost, Virtual Threads, Reactor I Scheduling

### Matrica Executor I Task Ownership-a

- Inventariši svaki platform thread, virtual thread, executor, fork-join pool, scheduler, Reactor scheduler, timer, queue, semaphore, rate limiter i pool koji framework kreira.
- Za svaki zabeleži kreatora, owner-a, klasu task-a, tip i granicu queue-a, konkurentnost, rejection policy, timeout, cancellation, context propagation, metrike i shutdown owner-a.
- Odbaci unbounded slanje task-ova ili skrivenu upotrebu common pool-a za produkciono kritičan rad bez dokazane capacity i failure semantike.
- Proveri da blocking rad nikada ne radi na event-loop ili scheduler thread-ovima čiji ugovor zabranjuje blokiranje i da CPU rad ne može izgladneti I/O ili control-plane task-ove.
- Testiraj saturation, rejection, interruption, cancellation, timeout, process shutdown, usporenje zavisnosti i memory pressure za svaki kritični executor.

### Audit Virtual Thread-ova

- Proveri gde su virtual thread-ovi uključeni i da li su framework, server, klijent, scheduler, baza, logging, tracing i native biblioteke kompatibilni sa nameravanim modelom.
- Detektuj pinning rizike iz synchronized blokova, native poziva, monitor contention-a, class inicijalizacije, file lock-ova i biblioteka koje zadržavaju carrier thread-ove.
- Ne pretvaraj jeftino kreiranje thread-a u neograničenu downstream konkurentnost; zadrži semaphore, pool limit, rate limit, kvotu i admission control.
- Testiraj ThreadLocal, MDC, SecurityContext, transaction context, locale, tenant context, scoped value, interruption i cancellation ponašanje.
- Uporedi throughput, tail latency, heap, native memory, pritisak na konekcije i failure ponašanje sa platform-thread baseline-om pod realnim blocking workload-om.

### Reactive I WebFlux Ispravnost

- Mapiraj publisher-e, subscriber-e, hot i cold source-ove, scheduler granice, backpressure, buffering, replay, retry, timeout, cancellation i lifetime resursa.
- Detektuj blocking pozive, skriveni JDBC ili filesystem rad, `block()`, sinhroni logging, native pozive i skupo mapiranje na Netty event-loop thread-ovima.
- Dokaži da request cancellation stiže do database/client rada gde je podržano i da ne ostavlja orphan task-ove ili parcijalno commit-ovane side effect-e.
- Proveri context propagation za security, tenant, tracing, locale, transakcije i correlation podatke bez oslanjanja na ThreadLocal semantiku.
- Testiraj spore consumer-e, disconnect, retry petlje, velike stream-ove, prazne publisher-e, višestruke subscription-e, duple side effect-e i mešane imperative/reactive transaction granice.

### Async, Scheduling I Batch Rad

- Inventariši `@Async`, `TaskExecutor`, `@Scheduled`, `TaskScheduler`, Quartz, Spring Batch, integration flow-ove, maintenance job-ove i spoljne scheduler-e.
- Proveri uniqueness, leader election, overlap policy, misfire policy, vremensku zonu, daylight-saving ponašanje, retry, checkpoint, partitioning, restartability i sprečavanje duplikata.
- Za virtual-thread scheduler-e testiraj fixed-delay, fixed-rate i cron semantiku odvojeno; ne pretpostavljaj ekvivalentno thread ponašanje.
- Dokaži job parametre, execution identitet, chunk granice, skip/retry policy, writer idempotency i restart ponašanje posle failure-a između read, process, write i commit koraka.
- Testiraj dve replike koje pokreću isti job, dugotrajne task-ove tokom deployment-a, clock skew, propuštene trigger-e, catch-up storm i parcijalne spoljne side effect-e.

### Context Propagation I Cancellation

- Popiši security, tenant, request, trace, locale, transaction, feature, deadline i idempotency context i definiši njegov autoritativni nosač.
- Proveri propagation kroz servlet async, virtual thread-ove, custom executor-e, Reactor, messaging listener-e, scheduled job-ove, coroutine ili language interop i callback-ove.
- Očisti context po završetku task-a i ponovnoj upotrebi pool-a; testiraj curenje između korisnika, tenant-a, request-ova, job-ova i testova.
- Propagiraj deadline gde je moguće i prevedi cancellation u vremenski ograničen cleanup umesto tihog napuštanja.
- Ne koristi MDC ili tracing context kao authorization izvor; authorization context mora biti eksplicitan, autentifikovan i otporan na izmenu.


