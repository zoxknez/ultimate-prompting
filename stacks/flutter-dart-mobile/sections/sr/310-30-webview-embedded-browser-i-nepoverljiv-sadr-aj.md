## 30. WebView, embedded browser i nepoverljiv sadržaj

WebView kombinuje remote sadržaj sa privilegijama aplikacije i zahteva strogu izolaciju.

- Popiši svaki WebView/browser view, origin, izvor navigacije, JavaScript podešavanje, bridge, cookie jar, storage, pristup fajlovima, media dozvolu, download putanju i popup ponašanje.
- Allowlist-uj scheme, host, path, redirect i external-open destinacije; odbij lookalike host-ove, mixed content, nebezbedne scheme, userinfo, malformirane URL-ove i open redirect-e.
- Izloži najmanji mogući message bridge sa validacijom šeme, origin/frame validacijom, autorizacijom, rate limit-ima, korelacijom, timeout-om i lifecycle vezivanjem.
- Ne izlaži tokene, sirov filesystem, shell, proizvoljno pokretanje URL-a, clipboard, kontakte, kameru, bazu ili device API-je nepoverljivom sadržaju.
- Proveri cookie flag-ove, SameSite ponašanje, SSO logout, čišćenje cache-a, promenu naloga, particionisanje storage-a, certificate greške, safe browsing i validaciju download-a.
- Testiraj XSS u remote sadržaju, zlonamerne redirect-e, nested frame-ove, bridge spoofing, replay, navigaciju tokom privilegovanog zahteva, ponovno kreiranje procesa i offline keširane stranice.
- Drži browser i platformske WebView verzije u compatibility matrici i definiši ponašanje nepodržane verzije.
- Zahtevaj security review za svaki novi origin, bridge metod, file dozvolu, download tip ili authentication tok.

