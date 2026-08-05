## 31. Phase 21 - WooCommerce, Payments And High-Risk Commerce Flows

When checkout, subscriptions, customer accounts or payment integrations exist, treat the incident as high risk until browser, server and provider evidence excludes skimming or credential theft.

### Immediate commerce triage

- determine whether checkout or account login must be suspended
- preserve affected page HTML, loaded scripts, network requests and browser evidence
- identify payment method architecture: hosted redirect, iframe, tokenized fields, direct API or custom form
- contact the payment provider/acquirer according to the owner's incident process when exposure is credible
- avoid collecting or reproducing full cardholder data in the investigation report
- preserve gateway, webhook, fraud and transaction logs through trusted provider channels

### WooCommerce and extension inventory

Inspect:

- WooCommerce core and all payment, subscription, tax, shipping and checkout extensions
- REST API keys, webhook secrets and legacy integration credentials
- Store API, checkout blocks, account endpoints and custom templates
- order, customer, coupon, product and downloadable-file access controls
- WooCommerce sessions, transients and object-cache behavior
- scheduled actions, failed actions and Action Scheduler tables
- custom order statuses, email templates and admin automation
- third-party JavaScript loaded on product, cart, checkout and account pages
- tag-manager containers and marketing pixels with publishing privileges

### Skimmer detection and verification

- compare checkout DOM and network activity with a known-good build
- inspect database content, widgets, templates and options for injected scripts
- test conditional behavior by user agent, referrer, geography, authentication and payment method
- inspect service workers, browser cache, CDN transforms and edge workers
- confirm that payment-provider public keys, endpoint domains and webhook destinations are expected
- verify no unauthorized order export, customer export or admin API activity occurred
- rotate affected gateway, webhook and API credentials with provider coordination

Do not resume checkout solely because the visible page looks normal.

