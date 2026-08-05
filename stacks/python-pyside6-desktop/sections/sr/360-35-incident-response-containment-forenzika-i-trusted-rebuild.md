## 35. Incident response, containment, forenzika i trusted rebuild

### 35.1 Obim audita

1. Definiši klase incidenta za zlonamerni paket ili plugin, dependency kompromitovanje, krađu credential-a, kompromitovanje signing ključa, tampering update feed-a, kompromitovan helper/servis, data corruption i privacy breach.
2. Mapiraj izvore dokaza: repozitorijum, CI, package index-e, build logove, provenance, potpise, update metadata, instalirane fajlove, liste procesa/modula, logove, dump-ove, baze i mrežnu telemetriju.
3. Definiši containment kontrole: isključi feed, opozovi ključ ili token, blokiraj paket/verziju, pauziraj rollout, isključi plugin ili feature, izoluj host, zaustavi write i sačuvaj dokaze.
4. Razlikuj cleanup od trusted rebuild-a; kompromitovanom interpreteru, paketu, helper-u, updater-u, signing sistemu ili hostu ne može se verovati samo zato što su sumnjivi fajlovi obrisani.
5. Dokumentuj rotaciju credential-a, opoziv sertifikata, obaveštavanje korisnika, legal/privacy eskalaciju, clean-room rebuild, validaciju restore-ovanih podataka i re-enrollment.
6. Definiši exit kriterijume, pojačan monitoring, retrospective akcije, vlasnika i verifikaciju da su originalni root cause i persistence mehanizmi uklonjeni.

### 35.2 Obavezna verifikacija

1. Pokreni tabletop ili tehničku vežbu za najmanje najuticajniju primenljivu klasu incidenta.
2. Verifikuj brzu identifikaciju pogođenih commit-a, zavisnosti, artefakata, potpisa, kanala, instaliranih verzija, korisnika, podataka i credential-a.
3. Dokaži revocation, isključenje update-a, kill switch, safe-mode startup, quarantine plugin-a, write freeze i trusted replacement mehanizme.
4. Ponovo izgradi iz known-good source-a i trusted toolchain-a na čistoj infrastrukturi; uporedi hash-eve, provenance, SBOM, potpise i ponašanje.
5. Testiraj recovery komunikaciju i operator runbook-e bez izlaganja osetljivih forenzičkih ili ličnih podataka.

