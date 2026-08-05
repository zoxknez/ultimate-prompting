## Technology Paths

- Ruby runtime: `CRUBY_MRI` | `JRUBY` | `TRUFFLERUBY` | `MULTIPLE_RUNTIMES` | `UNKNOWN_RUNTIME`.
- Application: `FULL_STACK_RAILS` | `API_ONLY_RAILS` | `RAILS_ENGINE` | `MODULAR_MONOLITH` | `LEGACY_RAILS` | `RACK_APP` | `MIXED_FRAMEWORK` | `UNKNOWN`.
- Web server: `PUMA` | `PASSENGER` | `UNICORN` | `FALCON` | `THRUSTER_PLUS_PUMA` | `SERVERLESS` | `CUSTOM_RACK` | `MULTIPLE_SERVERS` | `UNKNOWN_SERVER`.
- Jobs: `SOLID_QUEUE` | `SIDEKIQ` | `GOOD_JOB` | `DELAYED_JOB` | `RESQUE` | `SHORYUKEN` | `CUSTOM_WORKER` | `NO_BACKGROUND_JOBS` | `UNKNOWN_JOBS`.
- Persistence: `POSTGRESQL` | `MYSQL` | `SQLITE` | `MULTIPLE_DATABASES` | `SHARDS` | `READ_REPLICAS` | `NON_SQL` | `UNKNOWN_DB`.
- Delivery: `KAMAL` | `CONTAINER` | `KUBERNETES` | `PAAS` | `VM_SYSTEMD` | `CAPISTRANO` | `SERVERLESS` | `MULTIPLE_TARGETS` | `UNKNOWN_DEPLOY`.

Apply path-specific analysis for every active path. Never transfer CRuby, Puma, PostgreSQL, Redis, Sidekiq, Solid Queue or Kamal semantics to another path without evidence.

