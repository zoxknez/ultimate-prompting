## 12. Faza 2 - Containment

Ograniči pretnju bez nepotrebnog uništavanja dokaza.

Proceni i dokumentuj:

- ograničenje pristupa origin-u
- CDN/WAF challenge ili deny pravila
- privremeni autentifikovani maintenance odgovor
- selektivno isključivanje checkout-a, formi, XML-RPC-a, REST ruta, uploads-a ili registracije
- isključivanje WordPress file editor-a
- privremeno ograničenje write dozvola
- uklanjanje prava izvršavanja iz uploads direktorijuma
- ukidanje sumnjivih sesija i API/application password-a
- suspenziju nepoznatih administratora
- izolaciju kompromitovanih pluginova/tema
- blokiranje poznatih zlonamernih IP adresa samo kada ima smisla i bez predstavljanja toga kao potpune remediation akcije

Containment nije eradication. Sama maintenance stranica nije dovoljna ako su origin, API, uploads, cron, admin-ajax, XML-RPC ili direktne PHP putanje i dalje dostupne.

