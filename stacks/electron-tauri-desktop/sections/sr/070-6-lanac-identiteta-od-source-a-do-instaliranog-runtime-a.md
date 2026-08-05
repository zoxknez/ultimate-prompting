## 6. Lanac identiteta od source-a do instaliranog runtime-a

Ne pretpostavljaj da su repozitorijum, CI artefakt, upload-ovan paket, preuzet installer, instalirana aplikacija, pokrenut proces i update payload ista stvar. Dokazi lanac ili eksplicitno identifikuj prekid.

| Faza | Obavezni dokaz | Pitanje |
| --- | --- | --- |
| Source identitet | Commit, tag, dirty stanje, submodule-i, generisani source, lock fajlovi, build ulazi | Moze li drugi inzenjer tacno da reprodukuje koji source je koriscen? |
| Razreseni graf | npm/pnpm/yarn/Bun lock, Cargo.lock, native dependencies, plugin-i, verzije alata | Da li razreseni graf odgovara politici i deklarisanom izdanju? |
| Build identitet | Builder image/host, okruzenje, flag-ovi, feature set-ovi, target triple, generisani fajlovi | Da li je build dovoljno deterministican da objasni razlike artefakata? |
| Package identitet | App ID/bundle ID, naziv proizvoda, verzija, build broj, kanal, tip paketa, arhitektura | Moze li paket da se veze za source i namenjeni kanal? |
| Integritet identitet | Hash-evi, ASAR integrity, ugradjeni resursi, SBOM, provenance, potpis, timestamp, notarizacija | Moze li izmena ili zamena da se otkrije? |
| Distribucioni identitet | Release zapis, store listing, CDN objekat, update manifest, feed odgovor | Da li korisnik dobija pregledani artefakt? |
| Instalirani identitet | Install putanja, package manager/store registracija, binary potpis, resursi, dozvole | Da li instalirano stanje odgovara pregledanom artefaktu? |
| Runtime identitet | Putanja executable-a, process tree, ucitani moduli/biblioteke, WebView/runtime verzije, kanal, profil | Da li je pokrenuti proces ocekivano instalirano izdanje? |

### 6.1 Obavezne provere identiteta

1. Uporedi source deklaracije verzije sa generisanim package metadata, executable metadata, installer metadata, store metadata i update feed metadata.
2. Verifikuj kontinuitet application ID-a, bundle identifier-a, imena executable-a, publisher identiteta, protocol scheme-a, file association-a, data direktorijuma, keychain/credential namespace-a i update kanala.
3. Verifikuj da CI promovise nepromenljiv artefakt umesto nezavisnog rebuild-a za test, signing, staging i release.
4. Verifikuj da simboli, source map-e, dSYM/PDB/debug fajlovi, SBOM, provenance i release notes odgovaraju tacno isporucenom artefaktu.
5. Pregledaj instaliranu aplikaciju, ne samo raspakovani staging direktorijum.
6. Verifikuj runtime-ucitane native biblioteke, sidecar-e i sistemske WebView/runtime komponente kada uticu na ponasanje.
7. Dokumentuj svaku nedokazanu identity vezu kao release blocker ili eksplicitan preostali rizik.

