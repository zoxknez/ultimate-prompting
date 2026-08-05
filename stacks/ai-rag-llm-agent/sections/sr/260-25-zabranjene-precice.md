## 25. Zabranjene Precice

Ne radi sledece:

1. Ne koristi "model ce paziti" kao mitigaciju.
2. Ne tretiraj system prompt, refusal ili classifier kao autorizaciju.
3. Ne ubacuj untrusted retrieval ili tool output u privilegovan kontekst bez kontrola.
4. Ne radi auto-pay, deploy, delete, publish, message, promenu dozvola, shell execution ili sensitive export bez odobrenog deterministickog policy-ja i odgovarajuce potvrde.
5. Ne tvrdi da security kontrola radi bez testiranja relevantne attack putanje.
6. Ne prijavljuj lazne eval metrike, zelene testove, command output, model ponasanje ili source citate.
7. Ne koristi jedan demo ili jednog LLM judge-a kao production dokaz.
8. Ne hardkoduj univerzalni chunk size, top-k, model, context length ili safety prag.
9. Ne loguj tajne ili osetljive promptove radi pogodnosti.
10. Ne precutkuj provider, parser, retrieval, tool ili policy greske i ne nastavljaj kao da je sve uspelo.
11. Ne koristi fail-open kada authorization, approval, safety policy ili tenant context nisu dostupni.
12. Ne oznacavaj sistem kao ready dok primenjivi P0 nalazi ostaju otvoreni ili su kriticne oblasti neproverene.

