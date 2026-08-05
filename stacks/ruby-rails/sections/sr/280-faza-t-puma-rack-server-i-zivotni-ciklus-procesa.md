## Faza T - Puma, Rack Server I Zivotni Ciklus Procesa

- Proveri server verziju, Rack kompatibilnost, bind adrese, TLS terminaciju, proxy protocol, request parser i reverse-proxy pretpostavke.
- Izracunaj worker i thread topologiju po hostu, podu ili dyno-u i uporedi je sa CPU, memorijom, database, cache i external connection limitima.
- Proveri `preload_app!`, copy-on-write, worker boot hook-ove, fork safety, ponovno uspostavljanje konekcija i handling background thread-ova.
- Testiraj phased restart, rolling restart, graceful shutdown, drain, keep-alive, streaming, websocket i long-request ponasanje.
- Potvrdi da health probe razlikuje process alive, ready for traffic i dependencies degraded bez izazivanja outage kaskade.
- Primeni ekvivalentnu lifecycle analizu na Passenger, Unicorn, Falcon, serverless adapter-e ili custom Rack server-e.

