## 10. Faza 0 - Ovlašćenje, Trijaža I Stabilizacija

1. Potvrdi ovlašćenje vlasnika i tačne asset-e u scope-u.
2. Zabeleži trenutno vreme u lokalnoj vremenskoj zoni i UTC-u.
3. Utvrdi da li je incident još aktivan.
4. Identifikuj neposredne rizike:
   - presretanje payment podataka
   - krađa kredencijala
   - exfiltration podataka
   - javna distribucija malware-a
   - aktivan pristup napadača
   - DNS ili CDN takeover
   - destruktivna aktivnost ili ransomware
5. Odluči da li treba:
   - očuvati servis uz blokiranje zlonamernih putanja
   - postaviti origin iza autentifikovanog maintenance odgovora
   - ograničiti pristup po IP/VPN pravilima
   - selektivno isključiti checkout, login, registration ili uploads
   - kontaktirati hosting/CDN/payment provajdera
6. Dokumentuj poslovni uticaj, ograničenje downtime-a i vlasnika rollback odluke.

### Uslovi za trenutno zaustavljanje i eskalaciju

Zaustavi rutinski rad i eskaliraj kada:

- postoji aktivni payment skimming ili verovatna izloženost podataka platnih kartica
- potvrđena je exfiltration ličnih podataka
- napadač i dalje kontroliše registrar, DNS, CDN, hosting panel ili root nalog
- dokazi ukazuju na kompromitaciju više korisničkih naloga na shared hostingu
- destruktivne akcije su aktivne
- primenjuju se legal hold, osiguranje, policija ili regulatorni zahtevi
- okruženje nije obuhvaćeno ovlašćenjem responder-a

