## 35. Faza 25 - Dubinski Database, Serialized Data I Content Integrity Audit

Koristi otkriveni table prefix i stvarnu schema-u. Nikada ne pretpostavljaj `wp_` ili single-site layout.

### Data domeni visoke vrednosti

Pregledaj, prema primenljivosti:

- korisnike, user metadata, uloge, capabilities, session-e i application password-e
- options, site options, transients, autoloaded vrednosti i cron podatke
- postove, stranice, revizije, template-e, patterns, navigation, attachments i metadata
- komentare i comment metadata
- terms, taxonomies i relationships
- plugin-specific tabele za forme, snippets, redirect-e, SEO, cache, security, backup i commerce
- WooCommerce orders, customers, webhook-ove i zakazane akcije
- multisite globalne i per-site tabele
- database korisnike, grant-ove, routine, trigger-e, events i definer-e

### Pravila za serialized i encoded podatke

- identifikuj PHP serialized vrednosti pre mutacije
- koristi serialization-aware alate za zamene
- sačuvaj tačne dužine bajtova i strukturu objekata
- unserialization nepoverljivih objekata tretiraj kao code-execution rizik
- traži sumnjive URL-ove, domene, script fragmente, iframe-ove, event handler-e, encoded blob-ove i neočekivani PHP bez slepog dekodiranja ili izvršavanja sadržaja
- skupe pattern pretrage izvrši na kopiji ili replici kada je uticaj na produkciju neizvestan
- za svaku mutaciju zabeleži query, broj redova, primary key/object ID i before/after hash
- koristi transakcije ili testirane reverzibilne batch-eve kada su podržani

### Content integrity i reconciliation

- uporedi kritična podešavanja sa poznato dobrom konfiguracijom ili vrednostima koje je vlasnik odobrio
- identifikuj neočekivane administratore, promene uloga i prenose vlasništva
- proveri objavljeni sadržaj, revizije i attachments oko perioda incidenta
- uskladi orders, korisnike, form submissions i druge poslovne zapise sa eksternim sistemima
- identifikuj praznine nastale restore-om starijeg backup-a
- dokumentuj podatke kojima se ne može verovati i poslovnog vlasnika odgovornog za odluku

