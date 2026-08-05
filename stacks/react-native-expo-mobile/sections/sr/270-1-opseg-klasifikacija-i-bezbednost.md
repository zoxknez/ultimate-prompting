## 1. Opseg, klasifikacija i bezbednost

### 1.1 Klasifikacija proizvoda i workflow-a
- Posebno klasifikuj bare React Native, Expo managed sa CNG, Expo prebuild, Expo bare, brownfield, biblioteku, Expo Module, monorepo, white-label i varijante sa vise aplikacija.
- Zabelezi svaku podrzanu platformu, arhitekturu, store, enterprise kanal, update kanal, okruzenje, tenant, brend i feature-flag kohortu.
- Odvoji trenutnu production podrsku od aspirativnih, eksperimentalnih, community-maintained ili netestiranih tvrdnji o podrsci.
- Utvrdi da li su android i ios direktorijumi autoritativni source, generisani izlaz, delimicno generisani izlaz ili rucno odrzavano stanje.
- Mapiraj application ID, bundle identifier, EAS project ID, update URL, runtime version, scheme, associated domain, signing identitet i store zapis.
- Ne spajaj nalaze izmedju platformi ili workflow-a osim kada dokaz potvrdi isti mehanizam i uticaj.

### 1.2 Autorizacija i granice promena
- Potvrdi dozvolu pre promene verzija paketa, lock fajlova, native projekata, identifikatora aplikacije, signing konfiguracije, EAS project veze, update kanala ili store stanja.
- Nikada ne objavljuj OTA update, ne salji store build, ne rotiraj signing materijal, ne opozivaj kredencijale i ne migriraj production podatke bez izricite dozvole.
- Sacuvaj forenzicke dokaze pre ciscenja generisanih direktorijuma, cache-a, build izlaza, native zavisnosti, lokalnih baza ili crash logova.
- Koristi redigovane dokaze i komande bezbedne za tajne; nikada ne prikazuj keystore, provisioning profile, privatni update kljuc, access token, refresh token ili korisnicke podatke.
- Definisi stop uslove za destruktivni prebuild, schema migraciju, signing promenu, OTA rollout, upgrade native zavisnosti i incident containment.
- Daj prednost reverzibilnim, preglednim i uskim promenama sa eksplicitnim testom i rollback putem.

