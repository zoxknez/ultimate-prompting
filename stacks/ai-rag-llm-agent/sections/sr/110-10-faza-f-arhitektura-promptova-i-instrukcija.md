## 10. Faza F - Arhitektura Promptova I Instrukcija

1. Popisi system, developer, user, tool, retrieval, memory i hidden instrukcije.
2. Proveri da je instruction precedence nameran, dokumentovan i testiran.
3. Razdvoji trusted control instrukcije od untrusted podataka kroz strukturne kanale i typed polja, a ne samo natural-language delimitere.
4. Ukloni tajne, authorization policy, skrivene poslovne odluke i osetljive interne podatke iz promptova gde su potrebne deterministicke kontrole.
5. Validiraj prompt promenljive, template escaping, lokalizaciju i truncation ponasanje.
6. Testiraj direct, indirect, multi-turn, encoded, obfuscated, multilingual, multimodal i tool-result prompt injection.
7. Testiraj instruction collision izazvan retrieved dokumentima, email-om, web stranicama, file metadata-om, OCR-om, komentarima, alt text-om, kodom i tool opisima.
8. Proveri da su refusal, escalation i safe-completion pravila sprovedena van modela gde je potrebno.
9. Verzionisi promptove i povezi svaki produkcioni odgovor i eval sa prompt revizijom.
10. Zahtevaj review i regression eval za izmene prompta.

