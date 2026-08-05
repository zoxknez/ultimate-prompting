## Faza 3 - Package Manager, Zavisnosti I Supply Chain

Audituj efektivno ponasanje u source-u, resolved konfiguraciji, izgradjenom artefaktu, ciljnom deployment-u i failure putanjama. Eksplicitno oznaci nedostupan dokaz umesto popunjavanja praznina pretpostavkama.

### Audit Zahtevi

- Koristi jedan autoritativni lockfile po workspace granici i dokumentuj namerne izuzetke.
- Proveri frozen instalaciju, peer resolution, hoisting, override-e, patch-eve, optional dependencies i platform uslove.
- Audituj lifecycle skripte, install-time binary download-e, git i path zavisnosti, privatne registry-je, proxy-je i auth scope.
- Razlikuj prisustvo ranjivosti od reachable i exploitable upotrebe, ali nikada ne ignorisi nepatch-ovane runtime zavisnosti bez dokaza.
- Pregledaj dependency confusion, typosquatting, kompromitovanog maintainer-a, napusten paket, malicious update i tranzitivne native-code rizike.
- Proveri kompletnost SBOM-a, provenance, potpise ili attestations i politiku koja ih koristi.

### Obavezni Dokazi

- Proizvedi i sacuvaj resolved dependency graph i lock digest.
- Proizvedi i sacuvaj mapu poverenja skripti, registry-ja i advisory-ja.
- Proizvedi i sacuvaj SBOM, provenance i enforcement dokaz.

### Obavezni Failure I Acceptance Testovi

- Dokazi da clean instalacija je deterministicka.
- Dokazi da untrusted pull request-i ne mogu da pristupe release kredencijalima.
- Dokazi da opozvani paket ili alat je blokiran i zamenljiv.

