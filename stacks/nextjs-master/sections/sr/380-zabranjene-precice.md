## Zabranjene precice

- Ne proglasavaj readiness iz dev mode-a, zelenog build-a, unit testova, samo Lighthouse-a ili zelenog platform dashboard-a.
- Ne tretiraj Proxy, Middleware, route group-e, layout-e, skriven UI ili TypeScript tipove kao autorizaciju.
- Ne cache-uj private ili tenant podatke dok key, scope, invalidacija, deployment i outage nisu dokazani.
- Ne resavaj concurrency samo disabled dugmetom, debounce-om, in-memory flag-om ili optimistic UI-jem.
- Ne slabi CSP, CSRF, CORS, validaciju, rate limit-e, lint, tipove, testove ili header-e da bi proslo.
- Ne preporucuj latest, canary, preview ili release candidate samo zato sto je noviji.
- Ne rebuild-uj izmedju okruzenja i ne nazivaj izlaze istim release-om.
- Ne pretpostavljaj da traffic rollback vraca data, cache, session, queue, file, email, payment ili worker efekte.
- Ne oznacavaj blokirane testove kao prosle, ne izostavljaj exit code-ove i ne skrivaj UNVERIFIED gap-ove.
- Ne izvrsavaj destruktivne produkcione akcije bez eksplicitnog odobrenja i recovery dokaza.

