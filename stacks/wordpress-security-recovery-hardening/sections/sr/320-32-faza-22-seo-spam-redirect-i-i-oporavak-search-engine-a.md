## 32. Faza 22 - SEO Spam, Redirect-i I Oporavak Search Engine-a

SEO spam često kombinuje database sadržaj, conditional rendering, redirect logiku, cache slojeve i zloupotrebu vlasništva search engine naloga.

### SEO i redirect dokazi

Proveri:

- server i CDN redirect-e
- WordPress canonical, rewrite, template i redirect hook-ove
- `siteurl`, `home`, permalink i rewrite-rule stanje
- postove, revizije, post metadata, options, widgets, menije, patterns i theme podešavanja
- sitemap, robots, feed-ove, structured data i alternate-language linkove
- skrivene stranice, doorway sadržaj i neočekivane taxonomies
- cloaking po user agent-u, referrer-u, cookie-ju, IP-u, geografiji, vremenu ili auth statusu
- zlonamerne JavaScript redirect-e i service worker-e
- Search Console i Bing verifikovane vlasnike, korisnike, sitemap-e i istoriju izmena
- vlasništvo analytics i tag-manager naloga
- keširane stranice na CDN-u, reverse proxy-ju, browser-u i search-engine slojevima

### Redosled oporavka

1. ukloni root cause i persistence
2. obezbedi čist canonical response na origin-u
3. očisti i proveri svaki cache sloj
4. regeneriši sitemap-e i robots sadržaj
5. proveri Search Console/Bing vlasništvo i ukloni neovlašćene principal-e
6. zatraži review ili removal tek kada je čisto stanje stabilno
7. prati indeksirane URL-ove, crawl greške, manual actions i nove spam obrasce

URL removal alati privremeno skrivaju simptome i nisu remediation.

