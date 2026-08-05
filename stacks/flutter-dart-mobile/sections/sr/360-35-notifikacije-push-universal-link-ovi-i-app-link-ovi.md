## 35. Notifikacije, push, universal link-ovi i app link-ovi

Push isporuka je nepoverljiva, duplirana, odložena i zavisna od platforme.

- Popiši FCM/APNs/web push provajdere, tokene, topic-e, channel/category, background handler-e, notification service extension-e, akcije, badge-eve i lokalne notifikacije.
- Proveri registraciju tokena, rotaciju, brisanje, odvajanje okruženja, account/tenant vezivanje, logout cleanup, zamenu uređaja i serversku autorizaciju.
- Tretiraj payload polja kao nepoverljiva; validiraj tip, veličinu, rutu, identifikator objekta, actor-a, tenant, freshness, potpis gde se koristi i trenutnu autorizaciju.
- Testiraj foreground, background, terminated, force-stopped, offline, dupliranu, odloženu, promenjenog redosleda, revoked-session, wrong-account i app-upgrade isporuku.
- Izbegni osetljiv sadržaj notifikacije na zaključanom ekranu osim ako politika i izbor korisnika to dozvoljavaju; obradi preview podešavanja i platformsku redakciju.
- Proveri app link-ove, universal link-ove, custom scheme, asset association fajlove, vlasništvo domena, fallback stranice, više aplikacija i otpornost na hijack.
- Učini notification akcije idempotentnim i serverski autorizovanim; spreči da ponovljeni tap duplira plaćanje, porudžbinu, poruku ili destruktivnu izmenu.
- Meri delivery, open rate, duplicate rate, invalid token rate, neuspeh akcije, neuspeh deep link-a i notification-to-backend amplification.

