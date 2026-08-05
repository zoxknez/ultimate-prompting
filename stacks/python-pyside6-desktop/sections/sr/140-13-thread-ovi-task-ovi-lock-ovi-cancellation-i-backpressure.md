## 13. Thread-ovi, task-ovi, lock-ovi, cancellation i backpressure

### 13.1 Obim audita

1. Inventariši `QThread`, worker-object obrasce, `QThreadPool`, `QRunnable`, Python thread-ove, executor-e, timer-e, queue-eve, lock-ove, semaphore, condition-e i background servise.
2. Zabeleži vlasnika, start uslov, limit konkurentnosti, input queue, cancellation ugovor, deadline, isporuku rezultata, exception putanju, join/drain ponašanje i shutdown vlasnika.
3. Identifikuj pogrešnu subclassed-QThread upotrebu, rad koji se izvršava na pogrešnom thread-u, QObject move nakon parentovanja, direktan cross-thread UI pristup i blocking queued deadlock-e.
4. Pregledaj redosled lock-ova, scope lock-a, callback-ove pod lock-om, emitovanje signala pod lock-om, database konekcije po thread-u i thread safety native biblioteka.
5. Proveri unbounded task submission, rast queue-a, velike zadržane payload-e, priority inversion, starvation, retry storm i user-triggered pojačanje konkurentnosti.
6. Razlikuj cancellation zahtev od završenog otkazivanja i definiši ponašanje za native, file, database, device i network rad koji se ne može otkazati.

### 13.2 Obavezna verifikacija

1. Pokreni burst, sustained, cancellation, timeout, shutdown, worker-crash, queue-full i dependency-slowdown scenarije uz instrumentaciju thread-ova i queue-eva.
2. Koristi determinističke synchronization testove, faulthandler dump-ove, platformsko hvatanje stack-a i stress ponavljanje za istragu race-a i deadlock-a.
3. Verifikuj bounded queue-eve, admission control, coalescing progress-a, load shedding, retry budget-e i user-visible degraded stanja.
4. Dokaži da je svaki background exception opažen, klasifikovan, prijavljen i ili oporavljen ili izaziva kontrolisanu tranziciju stanja.
5. Potvrdi da nijedan worker, thread, timer, lock, device handle ili database konekcija ne preživi logout, promenu workspace-a, update restart ili shutdown nenamerno.

