## Phase J - Input Validation, Serialization And Data Representation

- Validate path, query, header, cookie, form, JSON, XML, GraphQL, CSV and multipart input at the trust boundary.
- Audit strong parameters and reject `permit!`, broad nested attributes and privilege-bearing field assignment without explicit policy.
- Verify serializers do not expose internal IDs, tenant keys, tokens, private fields or authorization-dependent data.
- Test Unicode normalization, locale, time zone, DST, currency, decimal precision, rounding, enum evolution and date parsing.
- Treat Marshal, YAML, ERB, templates and custom deserializers as code-execution or object-construction boundaries.

