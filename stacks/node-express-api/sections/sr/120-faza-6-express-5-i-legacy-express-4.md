## Faza 6 - Express 5 I Legacy Express 4

Audituj efektivno ponasanje u source-u, resolved konfiguraciji, izgradjenom artefaktu, ciljnom deployment-u i failure putanjama. Eksplicitno oznaci nedostupan dokaz umesto popunjavanja praznina pretpostavkama.

### Audit Zahtevi

- Identifikuj tacan Express major i patch i uporedi ponasanje sa podrzanim Node-om i zvanicnim migration smernicama.
- Za Express 5 proveri rejected-promise forwarding, async handler-e, error middleware, path sintaksu, body i query semantiku i uklonjene API-je.
- Za Express 4 inventarisi custom async wrapper-e, unhandled rejection putanje, legacy middleware i migration blocker-e.
- Pregledaj app, router, sub-app, mount path, parameter handler i settings inheritance ponasanje.
- Proveri da error middleware ima ispravan potpis, ne moze double-send i bezbedno obradjuje headers-already-sent.
- Audituj trust proxy prema tacnoj proxy-hop topologiji i spreci spoofing IP-a, protokola i host-a.

### Obavezni Dokazi

- Proizvedi i sacuvaj Express version i migration matricu.
- Proizvedi i sacuvaj graf redosleda middleware-a i router-a.
- Proizvedi i sacuvaj trust-proxy i route regression dokaz.

### Obavezni Failure I Acceptance Testovi

- Dokazi da rejected promise stize do nameravanog error handler-a jednom.
- Dokazi da spoofed forwarded header-i ne menjaju trusted identitet.
- Dokazi da headers-already-sent i legacy wildcard putanje se bezbedno zavrsavaju.

