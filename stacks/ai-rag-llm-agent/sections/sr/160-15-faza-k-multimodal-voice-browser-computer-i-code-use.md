## 15. Faza K - Multimodal, Voice, Browser, Computer I Code Use

1. Tekst, slike, PDF, audio, video, OCR, metadata, caption-e, DOM, accessibility tree i screenshot-e tretiraj kao untrusted input.
2. Testiraj skrivene i vizuelno ugradjene instrukcije, adversarial overlay, steganografski ili metadata-based sadrzaj gde je relevantno i cross-modal konflikte.
3. Proveri da browser navigation, download, upload, clipboard, login state, cookies, local files i external links prate least privilege.
4. Gde je moguce primeni kontrole tacne destinacije i URL-a za automatsku navigaciju ili retrieval.
5. Izoluj code execution kroz resource, filesystem, process, package, secret i network kontrole.
6. Validiraj generisani kod pre izvrsavanja i nikada ga ne pokreci sa nepotrebnim host ili production privilegijama.
7. Za voice proveri pristanak, recording indikator, transcription retention, speaker ambiguity, interruption, accidental activation i high-impact verbal confirmation.
8. Za computer use zahtevaj vidljivu potvrdu high-impact akcija i testiraj UI ambiguity, layout promene, malicious stranice i stale screenshot-e.
9. Proveri da su downloadovani artefakti skenirani, tipizirani, ograniceni po velicini i bezbedno sacuvani.

