#!/bin/sh
# lab133.sh : Databases for DevOps, lesson 8: troubleshoot app-to-database connectivity and migration failures. Run with sudo, on any Linux machine with PostgreSQL (server and psql).
#   up | check | down | status
# Needs: sudo apt install -y postgresql postgresql-client     port 5513 free. (The lab runs its own private PostgreSQL cluster in /opt/lab133; it does not touch the system PostgreSQL.)
# Mission: the shop app cannot reach its database, and then a migration fails. Diagnose each error, fix it, and prove it.
D=${LAB133_DIR:-/opt/lab133}
OWNER=${SUDO_USER:-root}
if [ "$OWNER" = root ]; then OWNER=postgres; id postgres >/dev/null 2>&1 || { echo "run with sudo from a normal user account"; exit 1; }; fi
BIN=$(ls -d /usr/lib/postgresql/*/bin 2>/dev/null | sort -V | tail -n 1)
RU="runuser -u $OWNER --"
PORT=5513
down() {
  [ -f $D/data/postmaster.pid ] && $RU $BIN/pg_ctl -D $D/data -m fast stop >/dev/null 2>&1
  sleep 1
  rm -rf "${D:?}"/* "${D:?}"/.[!.]* 2>/dev/null; rmdir "$D" 2>/dev/null; true
}
up() {
  [ -n "$BIN" ] || { echo "PostgreSQL not found: run  sudo apt install -y postgresql postgresql-client"; exit 1; }
  command -v psql >/dev/null 2>&1 || { echo "psql not found: run  sudo apt install -y postgresql-client"; exit 1; }
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  down; mkdir -p $D/app/migrations; chown -R $OWNER $D
  $RU $BIN/initdb -D $D/data --auth-local=trust --auth-host=scram-sha-256 -E UTF8 --locale=C.UTF-8 >/dev/null 2>&1 || { echo "initdb failed"; exit 1; }
  $RU $BIN/pg_ctl -D $D/data -o "-p $PORT -k $D -c listen_addresses=127.0.0.1 -c password_encryption=scram-sha-256" -l $D/server.log -w start >/dev/null 2>&1 || { echo "server did not start (is port $PORT free?)"; exit 1; }
  P="$RU psql -h $D -p $PORT -X -q -v ON_ERROR_STOP=1"
  $P -d postgres -c "CREATE ROLE shopapp LOGIN PASSWORD 'Shop-app-133'" -c "CREATE DATABASE shop OWNER shopapp" >/dev/null
  cat > $D/app/migrations/001_orders.sql <<'EOF_M'
CREATE TABLE orders (id serial PRIMARY KEY, customer_id int NOT NULL, total_cents int NOT NULL);
INSERT INTO orders (customer_id, total_cents) VALUES (1, 2400), (2, 1800), (3, 5200), (1, 900), (2, 4100), (3, 300);
EOF_M
  cat > $D/app/migrations/002_customers.sql <<'EOF_M'
CREATE TABLE customers (id serial PRIMARY KEY, name text NOT NULL);
INSERT INTO customers (name) VALUES ('Ana'), ('Ben'), ('Cy');
EOF_M
  cat > $D/app/migrations/003_order_status.sql <<'EOF_M'
ALTER TABLE orders ADD COLUMN status text NOT NULL DEFAULT 'new';
CREATE INDEX orders_status_idx ON orders (statuss);
EOF_M
  cat > $D/app/migrate.sh <<'EOF_S'
#!/bin/sh
# applies every migration that is not yet in schema_migrations, in order; each one runs in a single transaction
cd "$(dirname "$0")"; . ./app.env
export PGPASSWORD="$DB_PASS" PGOPTIONS="-c client_min_messages=warning"
Q="psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME -X -q -v ON_ERROR_STOP=1"
$Q -c "CREATE TABLE IF NOT EXISTS schema_migrations (version text PRIMARY KEY)" || { echo "migrate: cannot reach the database"; exit 1; }
for f in migrations/*.sql; do
  v=$(basename $f .sql | cut -c1-3)
  [ "$($Q -At -c "SELECT count(*) FROM schema_migrations WHERE version='$v'")" = 0 ] || { echo "skip   $v (already applied)"; continue; }
  if ( cat $f; echo "INSERT INTO schema_migrations VALUES ('$v');" ) | $Q -1; then echo "apply  $v"; else echo "FAILED $v (rolled back, nothing recorded)"; exit 1; fi
done
echo "migrations up to date"
EOF_S
  cat > $D/app/check_app.sh <<'EOF_S'
#!/bin/sh
# what the shop app does at start-up: connect with app.env and count the orders
cd "$(dirname "$0")"; . ./app.env
export PGPASSWORD="$DB_PASS"
out=$(psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME -X -At -c "SELECT count(*) FROM orders" 2>&1) && echo "app OK: $out orders" || { echo "app FAILED:"; echo "$out" | sed 's/^psql: error: //' | tr '\n\t' '  ' | fold -s -w 66 | sed 's/^/  /'; exit 1; }
EOF_S
  cat > $D/app/app.env <<'EOF_E'
# connection settings of the shop app
DB_HOST=db-shop
DB_PORT=5431
DB_NAME=shopp
DB_USER=shopapp
DB_PASS=shop-app-133
EOF_E
  printf '%s\n' 'secret store (do not commit)' 'user      shopapp' 'password  Shop-app-133' 'database  shop' 'server    127.0.0.1 port 5513' > $D/vault.txt
  chmod +x $D/app/migrate.sh $D/app/check_app.sh
  # 001 and 002 were applied earlier; 003 is pending
  $P -d shop -c "CREATE TABLE schema_migrations (version text PRIMARY KEY)" -f $D/app/migrations/001_orders.sql -f $D/app/migrations/002_customers.sql -c "INSERT INTO schema_migrations VALUES ('001'),('002')" -c "ALTER TABLE orders OWNER TO shopapp" -c "ALTER TABLE customers OWNER TO shopapp" -c "ALTER TABLE schema_migrations OWNER TO shopapp" >/dev/null
  cat > $D/TASKS.txt <<'EOF_T'
LAB 133  Troubleshoot app-to-database connectivity and migration failures
Open a terminal in /opt/lab133/app. The shop app cannot start. Run it and read the error:  ./check_app.sh
Fix ONE thing at a time, in app.env (use vim), and run ./check_app.sh again after each fix. Every error points to a different layer:

1  Name:      "could not translate host name"   the host name does not resolve.   getent hosts NAME ;  the real server is 127.0.0.1
2  Port:      "connection refused"              nothing listens on that port.     pg_isready -h HOST -p PORT ;  ss -ltn
3  Password:  "password authentication failed"  wrong password.                   the right one is in /opt/lab133/vault.txt (watch the capital S)
4  Database:  "database ... does not exist"     wrong database name.              psql -h 127.0.0.1 -p 5513 -U shopapp -d postgres -l
5  Migration: ./migrate.sh                       003 fails and is rolled back.     read the error, fix the typo in migrations/003_order_status.sql, run ./migrate.sh again
6  lab check   (judges you: you need all 5 PASS)        7  lab down  (removes it all)
Rule: read the exact error first; change one thing; test again. Never edit an applied migration: fix the pending one.
EOF_T
  chown -R $OWNER $D 2>/dev/null
  echo "lab 133 ready in $D. Read TASKS.txt, then: cd $D/app ; ./check_app.sh"
}
pass=0; total=5
ok() { pass=$((pass+1)); echo "  PASS  $1"; }
no() { echo "  FAIL  $1"; }
check() {
  [ -f $D/data/postmaster.pid ] || { echo "the lab is not running: run  lab up"; exit 1; }
  . $D/app/app.env 2>/dev/null
  if $BIN/pg_isready -q -h "$DB_HOST" -p "$DB_PORT" -t 3 2>/dev/null; then ok "1 DB_HOST and DB_PORT reach the server"; else no "1 DB_HOST and DB_PORT must reach the server (pg_isready -h HOST -p PORT)"; fi
  if PGPASSWORD="$DB_PASS" psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d postgres -X -At -c "SELECT 1" >/dev/null 2>&1; then ok "2 the user and password are accepted"; else no "2 the user and password must be accepted by the server"; fi
  if [ "$($RU psql -h $D -p $PORT -X -At -d postgres -c "SELECT count(*) FROM pg_database WHERE datname='$DB_NAME'" 2>/dev/null)" = 1 ]; then ok "3 DB_NAME is a database that exists"; else no "3 DB_NAME must be a database that exists"; fi
  if $RU sh $D/app/check_app.sh 2>&1 | grep -q "^app OK: 6 orders"; then ok "4 the app starts and reads its 6 orders"; else no "4 ./check_app.sh must print: app OK: 6 orders"; fi
  m=$($RU psql -h $D -p $PORT -X -At -d shop -c "SELECT count(*) FROM schema_migrations WHERE version='003'" 2>/dev/null); c=$($RU psql -h $D -p $PORT -X -At -d shop -c "SELECT count(*) FROM information_schema.columns WHERE table_name='orders' AND column_name='status'" 2>/dev/null)
  if [ "$m" = 1 ] && [ "$c" = 1 ]; then ok "5 migration 003 is applied (status column, recorded)"; else no "5 fix migration 003 and run ./migrate.sh until it is applied"; fi
  echo; echo "$pass / $total passed"; [ $pass -eq $total ]
}
case "$1" in
  up) up ;;
  check) check ;;
  down) down; echo "lab 133 removed." ;;
  status) [ -f $D/data/postmaster.pid ] && echo running || echo "not running" ;;
  *) echo "usage: sudo lab133.sh up|check|down|status" ;;
esac
