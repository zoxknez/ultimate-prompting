## Faza AK - Incident Response I Trusted Rebuild

- Aktiviraj incident rezim za curenje credential-a, kompromitaciju session kljuca, proizvoljno izvrsavanje koda, zlonamerni gem, webshell, korupciju podataka, tenant leak ili neoporavljivo queue ponasanje.
- Containment uradi zaustavljanjem rizicnih upisa, pauziranjem workera, iskljucivanjem pogodjenih ruta, izolacijom hostova i opozivom kompromitovanog poverenja.
- Sacuvaj logove, image-e, procese, pakete, lock fajlove, database dokaz i timeline pre cleanup-a.
- Rotiraj kljuceve i credential-e, invalidiraj sesije i signed podatke po potrebi i pregledaj istorijske artefakte i deployment-e.
- Rebuild uradi iz pregledanog source-a, trusted toolchain-a, cistih dependency-ja, poznato dobrog base image-a i novo izdatih credential-a.
- Vrati sistem, uradi reconciliation, validiraj tenant izolaciju i kriticne invarijante, zatim zavrsi post-incident akcije i regresione testove.

