## 1. Inventar, Lifecycle I Reproduktivni Baseline

Mapiraj solution/project topologiju, TFM, `global.json`, SDK/runtime, CPM/package reference, lock fajlove, NuGet izvore, analyzere, nullable/implicit-using, trimming/AOT, build/publish profile, entry pointove, host tip, DI, middleware redosled, endpointe, EF context-e/migracije, jobove, queue-ove, cache, auth, konfiguraciju, deployment, CI/CD i testove.

Potvrdi da je production runtime podrzan i na aktuelnom patchu. LTS ima tri godine podrske, STS dve; nepodrzan ili nepatchovan runtime je produkcioni rizik. Razdvoji framework-dependent i self-contained; self-contained se mora rebuildovati kada bundled runtime zahteva update.

Napravi mapu: `client -> CDN/load balancer/reverse proxy -> Kestrel/IIS -> middleware -> endpoint -> authentication -> authorization -> validation -> application operation -> database/cache/queue/external dependency -> response`.

Pokreni deterministicki restore, build, analyzere, testove, publish, production-like startup, migration status, health/readiness i graceful-shutdown gde je podrzano. Zabelezi komande, verzije, exit kodove i uzrok prvog neuspeha.

