## 28. Faza 18 - Supply-Chain Provenance Pluginova, Tema I Integracija

Svaka izvršiva komponenta mora imati dokumentovano poreklo. Popularnost, update obaveštenje ili poznato ime fajla nisu provenance.

### Obavezni zapis komponente

Za svaki plugin, temu, MU plugin, drop-in, code-snippet paket i bundlovanu biblioteku zabeleži:

- slug i naziv razumljiv čoveku
- instaliranu verziju i putanju fajl sistema
- aktivan, neaktivan, network-active ili orphaned status
- izvor: WordPress.org, vendor portal, Git repozitorijum, interni build ili nepoznato
- URL paketa ili repository commit/tag
- vreme preuzimanja i operatera
- očekivani hash, potpis ili vendor checksum kada postoji
- licencu i vlasnika održavanja
- poslednji update i poslednju poznatu upotrebu
- podržani WordPress/PHP opseg
- poznatu ranjivost i status napuštenosti
- da li komponenta može menjati fajlove, korisnike, uloge, cron, redirect-e, checkout, SMTP, DNS/CDN ili spoljne skripte

### Obavezna verifikacija

- proveri WordPress.org checksum-e kada postoje, ali pakete koji nisu dostupni ili proverljivi evidentiraj odvojeno
- za premium/custom kod uporedi sa paketom dobijenim od pouzdanog vendora ili interno reprodukovanim build-om
- pregledaj sadržaj paketa pre instalacije, uključujući installer skripte, bundlovane binarne fajlove, obfusciran kod i neočekivane domene
- uporedi repository source, izgrađenu distribuciju i instalirane fajlove
- pregledaj Composer/npm dependency lockfile-ove unutar pluginova/tema kada postoje
- proveri update izvor, URL update servera, certificate validation i signing ponašanje
- identifikuj pluginove uklonjene iz direktorijuma, projekte sa promenjenim vlasništvom, napuštene pakete i nulled/piratske distribucije
- automatic update status tretiraj kao konfiguraciju, a ne dokaz da je update uspeo ili bio pravovremen
- pregledaj filtere, konstante i politike provajdera koji isključuju ili odlažu forced security update

### Inventar third-party skripti i connector-a

Uključi:

- tag manager-e, analytics, chat, oglase, consent alate i optimization skripte
- payment gateway SDK-ove i checkout JavaScript učitan sa udaljene lokacije
- SMTP, CRM, backup, storage, AI/provider connector i webhook kredencijale
- OAuth aplikacije, API ključeve i application password-e
- CDN worker-e, edge include i funkcije prepisivanja skripti
- browser ekstenzije ili workstation deployment alate koje koriste administratori

Komponenta može biti čista na disku dok su njen update kanal, remote skripta, vendor nalog ili CI release proces kompromitovani. Obuhvati trust chain, a ne samo ZIP fajl.

