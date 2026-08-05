## 5. Jobovi, Messaging, Integracije, Fajlovi I SSRF

Za `@Async`, executore, scheduled taskove, Spring Batch, queue-ove, Kafka/JMS/Rabbit consumere i retry mehanizme proceni bounded poolove/queue-ove, context propagaciju, cancellation, startup/shutdown, acknowledgement, visibility/lease timeout, retry/backoff/jitter, dead-letter/poison obradu, deduplikaciju, idempotentnost, konkurentnost, ordering, timeout, deployment overlap i observabilnost. At-least-once delivery zahteva idempotentne consumere; ne potvrduj pre trajnog side effecta.

Za svaku spoljnu zavisnost proceni deadline, connect/read/overall timeout, bounded retry sa jitterom, rate limit, circuit breaker kada je opravdan, kredencijale, webhook potpis/replay zastitu, schema/version promene, fallback, sandbox/production razdvajanje i telemetriju. Ne retry-uj slepo validation, authorization, cancellation ili non-idempotent write. Ponovo koristi managed HTTP klijente i poolove; ne kreiraj klijente po zahtevu.

Za upload/download proveri count/size limite, MIME plus magic bytes, imena, traversal, privremeno skladiste, kvote, streaming, scanning politiku, privatno skladiste, signed URL expiry, tenant izolaciju, retention/cleanup i autorizaciju za svaki download. Ne ucitavaj velike fajlove u memoriju niti veruj client MIME-u/imenu.

Ako servis preuzima URL koji je poslao korisnik, validiraj semu, hostname, razresene IPv4/IPv6 adrese, loopback/private/link-local/cloud-metadata opsege, portove, DNS rebinding, redirecte, embedded kredencijale, velicinu/content type odgovora, timeout i decompression. String-only URL validacija nije dovoljna.

