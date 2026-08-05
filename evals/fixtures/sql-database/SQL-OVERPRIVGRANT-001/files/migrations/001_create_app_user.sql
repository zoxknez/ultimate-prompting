CREATE USER 'app_service'@'%' IDENTIFIED BY 'REPLACED-AT-DEPLOY-TIME';

-- Vulnerable: the application's runtime database user is granted every
-- privilege on every schema, including DROP, ALTER, GRANT OPTION, and
-- access to schemas this service never queries. A SQL injection or a
-- compromised dependency in this one service can now read, modify, or
-- destroy data belonging to every other service sharing this database
-- instance, and can create further privileged accounts via GRANT OPTION.
-- The application only ever needs SELECT/INSERT/UPDATE/DELETE on its own
-- schema.
GRANT ALL PRIVILEGES ON *.* TO 'app_service'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
