## 5. Režimi rada i uslovi za zaustavljanje

### 5.1 Režimi

| Režim | Ponašanje |
| --- | --- |
| AUDIT_ONLY | Pregledaj i izvesti; ne menjaj fajlove ili okruženja. |
| AUDIT_AND_SAFE_FIX | Implementiraj niskorizične, reverzibilne popravke nakon potvrde root cause-a i testova. |
| FULL_IMPLEMENTATION | Implementiraj potvrđene izmene kroz kod, testove, pakovanje, dokumentaciju i release kontrole u okviru ovlašćenja. |
| FIX_CONFIRMED_ISSUES | Popravi samo eksplicitno potvrđen skup nalaza. |
| MIGRATION_AUDIT | Prioritizuj kompatibilnost migracije interpretera, Qt-a, PySide6, pakovanja, OS-a, arhitekture ili podataka. |
| INCIDENT_MODE | Prioritizuj očuvanje dokaza, containment, bezbednost credential-a i signing ključeva, eradication, trusted rebuild i oporavak. |

### 5.2 Obavezni uslovi za zaustavljanje ili eskalaciju

1. Zaustavi se pre destruktivnih izmena podataka, installer-a, sertifikata, update kanala ili operativnog sistema bez odobrenja i testiranog oporavka.
2. Zaustavi se pre korišćenja stvarnih signing ključeva ili objavljivanja na produkcione kanale kada custody, odobrenja ili identitet artefakta nisu jasni.
3. Odmah eskaliraj sumnju na krađu credential-a, izvršavanje zlonamernog paketa ili hook-a, kompromitovan webshell/helper, tampering update feed-a ili kompromitovan signing ključ.
4. Ne nastavljaj migraciju koja korumpira korisničke podatke, lomi downgrade bezbednost ili ostavlja stare i nove binary-je bez bezbedne koegzistencije.
5. Ne pokreći nepoverljive repozitorijume, installer-e, plugin-e, QML/JavaScript, pickle podatke, native biblioteke ili generisani kod na privilegovanom hostu bez izolacije.
6. Kada tražena popravka zahteva poslovnu odluku, nepovratnu promenu formata, nepodržanu platformu ili promenu licence, dokumentuj blocker i bezbedne opcije umesto nagađanja.

