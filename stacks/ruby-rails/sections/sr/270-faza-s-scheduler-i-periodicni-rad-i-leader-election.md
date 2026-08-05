## Faza S - Scheduler-i, Periodicni Rad I Leader Election

- Popisi Solid Queue recurring taskove, Sidekiq cron, Whenever, system cron, Kubernetes CronJob, cloud scheduler i custom loop-ove.
- Testiraj overlap, dupli trigger, propusteni trigger, clock skew, DST, dugo izvrsavanje, restart i manuelni replay.
- Koristi database ili distribuirano vlasnistvo sa fencing-om gde je dozvoljen samo jedan aktivni scheduler ili task.
- Ucini periodicni rad restartabilnim, posmatranim i bezbednim kada izvrsavanje pocne pre deployment-a a zavrsi se posle njega.

