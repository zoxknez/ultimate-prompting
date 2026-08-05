## Zabranjene Precice

- Ne izmisljaj verzije, advisory-je, output komandi, prolazne testove, performance brojeve ili produkciona posmatranja.
- Ne proglasavaj bezbednost zato sto TypeScript kompajlira, Express ili Fastify se pokrece ili je health zelen.
- Ne koristi trust proxy true slepo, wildcard credentialed CORS, client-supplied tenant identitet ili UI visibility kao autorizaciju.
- Ne gutaj rejected promise-e, emitter greske, stream greske, fatal process greske ili background task kvarove.
- Ne retry-uj non-idempotent write operacije slepo i ne cuvaj durable idempotency i lock-ove samo u process memoriji.
- Ne kompajliraj user-provided Fastify scheme i ne obavljaj skup eksterni rad unutar pocetne validacije.
- Ne blokiraj event loop neogranicenim sinhronim CPU, parser, crypto, compression, filesystem ili child-process radom.
- Ne koristi floating alate, mutable artefakte, skrivene rebuild-e, neproveren migration-on-start ili produkcione podatke u nebezbednim testovima.
- Ne pretpostavljaj da deployment rollback vraca data, queue, email, payment, file, cache ili provider side effect-e.
- Ne proglasavaj READY bez monitoringa, abort-a, rollback-a ili forward repair-a, izolovanog restore-a i ownership-a residual risk-a.

