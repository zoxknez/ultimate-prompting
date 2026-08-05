## 14. Asyncio, QtAsyncio, qasync i više event loop-ova

### 14.1 Obim audita

1. Identifikuj asyncio upotrebu, QtAsyncio ili qasync integraciju, loop policy, task group-e, executor-e, async generator-e, network klijente i loop-ove u vlasništvu biblioteka.
2. Dokumentuj koji loop poseduje svaku coroutine-u, kako se Qt i asyncio callback-ovi prepliću i gde se dešava thread ili process handoff.
3. Pregledaj kreiranje task-a, structured concurrency, propagation cancellation-a, kompoziciju timeout-a, shielded task-ove, exception group-e i zadržavanje task-a.
4. Otkrij nested `asyncio.run`, kreiranje loop-a u worker thread-u, blocking kod na loop-u, neopažene task-ove, cross-loop future-e i shutdown upozorenja.
5. Proceni kompatibilnost biblioteka koje pretpostavljaju main thread, određenu event-loop implementaciju ili Unix-only signal ponašanje.
6. Definiši offline, reconnect, retry, backpressure, application-close, logout i update-restart ponašanje asinhronog rada.

### 14.2 Obavezna verifikacija

1. Instrumentuj kreiranje task-a, završetak, cancellation, izuzetke, dubinu queue-a, loop lag i shutdown kroz reprezentativne tokove.
2. Testiraj odložene i reordered odgovore, disconnect tokom await-a, cancellation tokom write-a, destrukciju prozora, promenu naloga i izlazak aplikacije.
3. Obezbedi da cancellation stigne do socket-a, stream-a, fajlova, database operacija, child procesa i poslovnih workflow-a ili da bude eksplicitno kompenzovan.
4. Verifikuj jednu jasnu integration strategiju umesto slučajne koegzistencije nezavisnih GUI i asyncio loop-ova.
5. Zaustavi readiness kada kritični background task-ovi mogu postati orphan, tiho pasti, ažurirati stale UI ili sprečiti čist shutdown.

