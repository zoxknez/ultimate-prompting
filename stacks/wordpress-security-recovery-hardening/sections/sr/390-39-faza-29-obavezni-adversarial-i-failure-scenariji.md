## 39. Faza 29 - Obavezni Adversarial I Failure Scenariji

Izvrši ili eksplicitno označi kao neizvodljivo uz razlog, preostali rizik i kompenzujući dokaz.

1. zatraži poznatu zlonamernu putanju kroz CDN i direktan origin
2. pristupi sajtu kao search crawler, mobile, logged-in i logged-out profil radi detekcije cloaking-a
3. pokušaj direktno PHP izvršavanje u uploads, cache, language i backup direktorijumima
4. kreiraj bezbedan sintetički file-change događaj i potvrdi dostavu alert-a
5. kreiraj i opozovi testni application password i potvrdi audit vidljivost
6. potvrdi da uklonjeni administrator ne može da se autentikuje preko cookie-ja, password reset-a, REST-a, XML-RPC-a ili application password-a
7. potvrdi da se zlonamerni ili nepoznati cron/action ne pojavljuje ponovo posle čišćenja
8. restartuj tačan PHP runtime i potvrdi da nema zastarelog OPcache/preload koda
9. testiraj origin bypass kada se očekuje CDN/WAF zaštita
10. potvrdi da susedni sajt ili deljeni hosting korisnik ne može ponovo da upiše oporavljeni sajt
11. restore-uj izabrani backup u izolaciji i proveri kod, podatke i kredencijale
12. testiraj kompatibilnost stare/nove aplikacije i database-a tokom kontrolisanog rollout-a
13. prekini update ili deployment i potvrdi atomic recovery ili rollback
14. testiraj pun disk, read-only fajl sistem i neuspešnu database konekciju
15. potvrdi da checkout učitava samo odobrene skripte i endpoint-e
16. proveri Search Console/Bing vlasništvo i stanje sitemap-a
17. simuliraj duplu isporuku background job-a i potvrdi idempotentno poslovno ponašanje
18. potvrdi invalidaciju session-a posle rotacije salts i kredencijala
19. testiraj malformed archive/media upload bez izvršavanja parser output-a u produkciji
20. potvrdi oporavak od opozvanog vendor, deployment ili signing kredencijala

