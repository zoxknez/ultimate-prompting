## 33. Faza 23 - Konzistentnost Cache-a, CDN-a, OPcache-a I Zastarelog Koda

Oporavak mora da obuhvati svaki sloj koji može nastaviti da servira ili izvršava sadržaj pre remediation-a.

### Cache i izvršni slojevi

Popiši:

- WordPress object cache i object-cache drop-in
- page-cache plugin i advanced-cache drop-in
- Redis ili Memcached namespace, autentikaciju i model deljenja
- reverse-proxy cache
- CDN cache, worker-e, transformacije, redirect-e i edge HTML injection
- cache i optimization slojeve hosting provajdera
- PHP OPcache, preload i životni vek PHP-FPM procesa
- browser cache i service worker-e
- propagaciju DNS resolver-a i certificate-a

### Evidence-safe redosled invalidacije

- pre purge-a sačuvaj relevantnu cache konfiguraciju, ključeve/metadata i sumnjive keširane objekte kada su korisni
- prvo deploy-uj pouzdan kod i konfiguraciju
- invalidiraj OPcache ili restartuj tačan PHP proces tek posle čuvanja dokaza i sa odobrenim impact planom
- očisti object/page/reverse-proxy/CDN cache dokumentovanim redosledom
- proveri direktan origin i svaku javnu edge putanju
- proveri autentikovane i neautentikovane varijante
- potvrdi da zastareli worker-i, container-i ili PHP child procesi više ne serviraju stari kod
- zabeleži purge ID-jeve, deployment revizije i vremena verifikacije

Cache purge pre deploy-a pouzdanog koda može ponovo napuniti cache zlonamernim sadržajem. Uspešan origin test ne dokazuje da je svaki edge čist.

