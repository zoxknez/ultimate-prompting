## Faza 0 - Safety Snapshot I Reproducibilan Baseline

Audituj efektivno ponasanje u source-u, resolved konfiguraciji, izgradjenom artefaktu, ciljnom deployment-u i failure putanjama. Eksplicitno oznaci nedostupan dokaz umesto popunjavanja praznina pretpostavkama.

### Audit Zahtevi

- Zabelezi branch, commit, dirty state, submodule-e, worktree-e, tagove i generisane fajlove pre promena.
- Odredi autoritativni lockfile i package manager; odbij instalacije koje ga neocekivano menjaju.
- Pokreni repository lint, typecheck, unit, integration, build, production start, smoke i audit komande koje stvarno postoje.
- Pokreni build output bez production side effect-a i proveri kriticne health i request putanje.
- Zabelezi prvi kvar, okruzenje, verzije, upozorenja i tacan exit code umesto maskiranja kvarova.
- Utvrdi pocetnu P0/P1 containment odluku pre low-priority cleanup-a.

### Obavezni Dokazi

- Proizvedi i sacuvaj log komandi i manifest okruzenja.
- Proizvedi i sacuvaj clean install, build i startup artefakte.
- Proizvedi i sacuvaj pocetnu mapu servisa i zavisnosti.

### Obavezni Failure I Acceptance Testovi

- Dokazi da dirty checkout sadrzaj nije prepisan.
- Dokazi da frozen instalacija detektuje lock drift.
- Dokazi da baseline moze da se reprodukuje iz clean checkout-a.

