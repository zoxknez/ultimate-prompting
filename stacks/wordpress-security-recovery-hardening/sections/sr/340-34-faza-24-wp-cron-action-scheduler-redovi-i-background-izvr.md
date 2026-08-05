## 34. Faza 24 - WP-Cron, Action Scheduler, Redovi I Background Izvršavanje

Background izvršavanje može sačuvati malware, replay-ovati neželjene akcije ili ponovo uvesti izmenjene fajlove posle naizgled uspešnog čišćenja.

### Inventar izvršavanja

- WordPress cron option i sve registrovane hook-ove
- system cron koji poziva `wp-cron.php`, WP-CLI ili custom skripte
- isključen interni WP-Cron i alternate cron konfiguracije
- Action Scheduler pending, in-progress, failed i completed akcije
- plugin-specific queue tabele i async request endpoint-e
- backup, migration, update, cache-warming, email i webhook poslove
- zakazane zadatke hosting panela i one-click maintenance poslove
- eksterne scheduler-e, uptime servise i CI webhook-ove koji pokreću application akcije

### Obavezne provere

- mapiraj svaki hook/action na vlasničku komponentu i callable
- identifikuj nepoznate callback-ove, encoded argumente, sumnjivo ponavljanje i novokreirane događaje
- sačuvaj zlonamerne action zapise pre otkazivanja
- pregledaj failed akcije radi payload-a i stack trace-a
- spreči duplo izvršavanje tokom maintenance-a i restarta worker-a
- proveri idempotency payment, email, order, user i external API poslova
- potvrdi da stari worker-i ili cron runner-i ne mogu izvršiti uklonjeni kod
- testiraj oporavak scheduler-a posle database restore-a, promene timezone-a i daylight-saving tranzicije
- prati ponovo kreirane događaje posle čišćenja kao persistence indikator

