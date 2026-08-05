## 31. Faza 21 - WooCommerce, Plaćanja I Visokorizični Commerce Tokovi

Kada postoje checkout, subscriptions, korisnički nalozi ili payment integracije, incident tretiraj kao visokorizičan dok browser, server i provider dokazi ne isključe skimming ili krađu kredencijala.

### Neposredna commerce trijaža

- utvrdi da li checkout ili account login moraju biti obustavljeni
- sačuvaj HTML pogođene stranice, učitane skripte, mrežne zahteve i browser dokaze
- identifikuj arhitekturu payment metode: hosted redirect, iframe, tokenizovana polja, direktni API ili custom forma
- kada je izloženost verovatna, kontaktiraj payment provajdera/acquirer-a prema incident procesu vlasnika
- izbegni prikupljanje ili reprodukovanje punih podataka platne kartice u izveštaju istrage
- sačuvaj gateway, webhook, fraud i transaction logove kroz pouzdane kanale provajdera

### WooCommerce i extension inventar

Pregledaj:

- WooCommerce core i sve payment, subscription, tax, shipping i checkout ekstenzije
- REST API ključeve, webhook tajne i legacy integration kredencijale
- Store API, checkout blocks, account endpoint-e i custom template-e
- kontrolu pristupa order, customer, coupon, product i downloadable-file podacima
- WooCommerce session-e, transients i object-cache ponašanje
- zakazane akcije, neuspele akcije i Action Scheduler tabele
- custom order status-e, email template-e i admin automatizaciju
- third-party JavaScript učitan na product, cart, checkout i account stranicama
- tag-manager container-e i marketing pixel-e sa publishing privilegijama

### Detekcija i verifikacija skimmer-a

- uporedi checkout DOM i mrežnu aktivnost sa poznato dobrim build-om
- pregledaj database sadržaj, widgets, template-e i options radi injektovanih skripti
- testiraj uslovno ponašanje po user agent-u, referrer-u, geografiji, autentikaciji i payment metodi
- pregledaj service worker-e, browser cache, CDN transformacije i edge worker-e
- potvrdi da su payment-provider public ključevi, endpoint domeni i webhook destinacije očekivani
- proveri da nije bilo neovlašćenog export-a order-a, customer-a ili admin API aktivnosti
- rotiraj pogođene gateway, webhook i API kredencijale u koordinaciji sa provajderom

Ne nastavljaj checkout samo zato što vidljiva stranica izgleda normalno.

