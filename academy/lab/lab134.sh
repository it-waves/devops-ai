#!/bin/sh
# lab134.sh : Databases for DevOps, mastery lesson: ship the CloudCart database, survive an incident, prove it. Run with sudo, on any Linux machine with PostgreSQL (server and psql).
#   up | incident | check | down | status
# Needs: sudo apt install -y postgresql postgresql-client     port 5514 free. (The lab runs its own private PostgreSQL cluster in /opt/lab134; it does not touch the system PostgreSQL.)
D=${LAB134_DIR:-/opt/lab134}
OWNER=${SUDO_USER:-root}
if [ "$OWNER" = root ]; then OWNER=postgres; id postgres >/dev/null 2>&1 || { echo "run with sudo from a normal user account"; exit 1; }; fi
BIN=$(ls -d /usr/lib/postgresql/*/bin 2>/dev/null | sort -V | tail -n 1)
RU="runuser -u $OWNER --"
PORT=5514
down() {
  pkill -f "sleep 86414" 2>/dev/null
  [ -f $D/data/postmaster.pid ] && $RU $BIN/pg_ctl -D $D/data -m fast stop >/dev/null 2>&1
  sleep 1
  rm -rf "${D:?}"/* "${D:?}"/.[!.]* 2>/dev/null; rmdir "$D" 2>/dev/null; true
}
up() {
  [ -n "$BIN" ] || { echo "PostgreSQL not found: run  sudo apt install -y postgresql postgresql-client"; exit 1; }
  command -v psql >/dev/null 2>&1 || { echo "psql not found: run  sudo apt install -y postgresql-client"; exit 1; }
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  down; mkdir -p $D/app/migrations $D/backups; chown -R $OWNER $D
  $RU $BIN/initdb -D $D/data -U postgres --auth-local=trust --auth-host=scram-sha-256 -E UTF8 --locale=C.UTF-8 >/dev/null 2>&1 || { echo "initdb failed"; exit 1; }
  $RU $BIN/pg_ctl -D $D/data -o "-p $PORT -k $D -c listen_addresses=127.0.0.1 -c password_encryption=scram-sha-256" -l $D/server.log -w start >/dev/null 2>&1 || { echo "server did not start (is port $PORT free?)"; exit 1; }
  $RU psql -h $D -p $PORT -U postgres -X -q -d postgres -c "CREATE DATABASE cloudcart" >/dev/null
  cat > $D/app/migrations/001_orders.sql <<'EOF_M'
CREATE TABLE orders (id serial PRIMARY KEY, customer text NOT NULL, total_cents int NOT NULL);
INSERT INTO orders (customer, total_cents) VALUES ('Ana', 2400), ('Ben', 1800), ('Cy', 5200), ('Dee', 900), ('Eli', 4100), ('Fay', 300), ('Gus', 7700), ('Hal', 1500);
EOF_M
  cat > $D/app/migrations/002_products.sql <<'EOF_M'
CREATE TABLE products (id serial PRIMARY KEY, name text NOT NULL, stock int NOT NULL);
INSERT INTO products (name, stock) VALUES ('Mug', 10), ('Lamp', 10), ('Desk', 10);
EOF_M
  cat > $D/app/migrations/003_order_status.sql <<'EOF_M'
ALTER TABLE orders ADD COLUMN status text NOT NULL DEFAULT 'new';
CREATE INDEX orders_status_idx ON orders (statuss);
EOF_M
  cat > $D/app/migrate.sh <<'EOF_S'
#!/bin/sh
# deploy step: apply every migration not yet in schema_migrations, in order, each in one transaction (runs as the database admin)
cd "$(dirname "$0")"
export PGOPTIONS="-c client_min_messages=warning"
Q="psql -h /opt/lab134 -p 5514 -U postgres -d cloudcart -X -q -v ON_ERROR_STOP=1"
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
# what the CloudCart app does at start-up: connect with app.env and count the orders
cd "$(dirname "$0")"; . ./app.env
export PGPASSWORD="$DB_PASS"
out=$(psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME -X -At -c "SELECT count(*) FROM orders" 2>&1) && echo "app OK: $out orders" || { echo "app FAILED:"; echo "$out" | sed 's/^psql: error: //' | tr '\n\t' '  ' | fold -s -w 66 | sed 's/^/  /'; echo; exit 1; }
EOF_S
  cat > $D/app/app.env <<'EOF_E'
# connection settings of the CloudCart app
DB_HOST=127.0.0.1
DB_PORT=5441
DB_NAME=cloudcart
DB_USER=cloudcart_app
DB_PASS=Cart-134-pass
EOF_E
  chmod +x $D/app/migrate.sh $D/app/check_app.sh
  cat > $D/TASKS.txt <<'EOF_T'
LAB 134  Databases mastery: ship the CloudCart database, survive an incident, prove it
Work in /opt/lab134. Load the short names:  source shortcuts134.sh   (lab, pg, usedb: PGHOST, PGPORT and PGUSER=postgres for the admin)
The admin connects over the socket as postgres. The app connects over TCP as cloudcart_app, password Cart-134-pass, using app/app.env.

1  Deploy:      cd app ; ./migrate.sh     003 fails and rolls back. Fix the typo in migrations/003_order_status.sql and run it again.
2  Access:      create the login role cloudcart_app (password Cart-134-pass) with LEAST privilege on database cloudcart:
               CONNECT on the database, SELECT and INSERT and UPDATE on orders, SELECT on products. No superuser, no DELETE, no DROP.
3  App:         ./check_app.sh fails. Read the error, fix ONE setting in app.env, test again, until: app OK: 8 orders
4  Back up:     BEFORE the incident:  pg_dump -Fc cloudcart -f backups/cloudcart.dump     and check it is readable (pg_restore -l)
5  Incident:    lab incident      (someone deletes every order, and a report session is stuck holding a lock that blocks the cart)
6  Recover:     a  find and end ONLY the blocking session (pg_stat_activity, pg_blocking_pids, pg_terminate_backend); the waiting update must finish
               b  createdb cloudcart_restored ; pg_restore into it ; validate: it must have all 8 orders again
7  Report:      write REPORT.txt, one value per line:  1 the number of orders restored   2 the PID of the blocking session
               3 the number of the migration that failed   4 the port the app really needs
8  lab check   (judges you: you need all 6 PASS)        9  lab down  (removes it all)
EOF_T
  chown -R $OWNER $D 2>/dev/null
  echo "lab 134 ready in $D. Read TASKS.txt, then: source shortcuts134.sh ; usedb"
}
incident() {
  [ -f $D/data/postmaster.pid ] || { echo "the lab is not running: run  lab up"; exit 1; }
  P="$RU psql -h $D -p $PORT -U postgres -X -q -d cloudcart"
  $P -c "DELETE FROM orders" >/dev/null 2>&1 || { echo "incident needs the migrations applied first (step 1)"; exit 1; }
  $RU sh -c "( echo 'BEGIN;'; echo 'UPDATE products SET stock = stock WHERE id = 1;'; sleep 86414 ) | PGAPPNAME=report-job nohup psql -h $D -p $PORT -U postgres -X -q -d cloudcart >/dev/null 2>&1 &"
  sleep 2
  $RU sh -c "PGAPPNAME=cart-api nohup psql -h $D -p $PORT -U postgres -X -q -d cloudcart -c 'UPDATE products SET stock = stock - 1 WHERE id = 1' >/dev/null 2>&1 &"
  sleep 1
  $RU psql -h $D -p $PORT -U postgres -X -q -At -d cloudcart -c "SELECT pid FROM pg_stat_activity WHERE application_name='report-job'" > $D/.blocker
  chown root:root $D/.blocker; chmod 600 $D/.blocker
  echo "incident started: orders deleted, a session is blocking the cart"
}
pass=0; total=6
ok() { pass=$((pass+1)); echo "  PASS  $1"; }
no() { echo "  FAIL  $1"; }
check() {
  [ -f $D/data/postmaster.pid ] || { echo "the lab is not running: run  lab up"; exit 1; }
  PS="$RU psql -h $D -p $PORT -U postgres -X -q -At"
  r=$($PS -d postgres -c "SELECT count(*) FROM pg_roles WHERE rolname='cloudcart_app' AND rolcanlogin AND NOT rolsuper AND NOT rolcreatedb AND NOT rolcreaterole" 2>/dev/null)
  g=$($PS -d cloudcart -c "SELECT has_table_privilege('cloudcart_app','orders','SELECT') AND has_table_privilege('cloudcart_app','orders','INSERT') AND has_table_privilege('cloudcart_app','orders','UPDATE') AND NOT has_table_privilege('cloudcart_app','orders','DELETE') AND has_table_privilege('cloudcart_app','products','SELECT') AND NOT has_table_privilege('cloudcart_app','products','UPDATE')" 2>/dev/null)
  if [ "$r" = 1 ] && [ "$g" = t ]; then ok "1 cloudcart_app: least privilege (no DELETE, no superuser)"; else no "1 cloudcart_app: login role, SELECT/INSERT/UPDATE orders, SELECT products only"; fi
  m=$($PS -d cloudcart -c "SELECT count(*) FROM schema_migrations WHERE version IN ('001','002','003')" 2>/dev/null); c=$($PS -d cloudcart -c "SELECT count(*) FROM information_schema.columns WHERE table_name='orders' AND column_name='status'" 2>/dev/null)
  if [ "$m" = 3 ] && [ "$c" = 1 ]; then ok "2 all three migrations are applied"; else no "2 fix migration 003 and run ./migrate.sh until all three are applied"; fi
  . $D/app/app.env 2>/dev/null
  if PGPASSWORD="$DB_PASS" psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d "$DB_NAME" -X -At -c "SELECT count(*) FROM orders" >/dev/null 2>&1; then ok "3 the app connects and reads its data"; else no "3 ./check_app.sh must print: app OK"; fi
  n=$($PS -d cloudcart_restored -c "SELECT count(*) FROM orders" 2>/dev/null)
  if [ -s $D/backups/cloudcart.dump ] && pg_restore -l $D/backups/cloudcart.dump >/dev/null 2>&1 && [ "$n" = 8 ]; then ok "4 a readable backup, restored into cloudcart_restored: 8 orders"; else no "4 back up BEFORE the incident, restore into cloudcart_restored, 8 orders"; fi
  w=$($PS -d cloudcart -c "SELECT count(*) FROM pg_stat_activity WHERE application_name='report-job'" 2>/dev/null); s=$($PS -d cloudcart -c "SELECT stock FROM products WHERE id=1" 2>/dev/null)
  if [ "$w" = 0 ] && [ "$s" = 9 ] && [ -f $D/.blocker ]; then ok "5 the blocker is gone and the waiting update finished"; else no "5 run lab incident, then end ONLY the blocking session"; fi
  bp=$(cat $D/.blocker 2>/dev/null); a=$(sed -n 1p $D/REPORT.txt 2>/dev/null | tr -d ' \r'); b=$(sed -n 2p $D/REPORT.txt 2>/dev/null | tr -d ' \r'); e=$(sed -n 3p $D/REPORT.txt 2>/dev/null | tr -d ' \r'); f=$(sed -n 4p $D/REPORT.txt 2>/dev/null | tr -d ' \r')
  if [ "$a" = 8 ] && [ -n "$bp" ] && [ "$b" = "$bp" ] && [ "$e" = 3 -o "$e" = 003 ] && [ "$f" = 5514 ]; then ok "6 REPORT.txt: 8 restored, the blocker PID, migration 003, port 5514"; else no "6 REPORT.txt, one value per line: orders restored, blocker PID, failed migration, app port"; fi
  echo; echo "$pass / $total passed"; [ $pass -eq $total ]
}
case "$1" in
  up) up ;;
  incident) incident ;;
  check) check ;;
  down) down; echo "lab 134 removed." ;;
  status) [ -f $D/data/postmaster.pid ] && echo running || echo "not running" ;;
  *) echo "usage: sudo lab134.sh up|incident|check|down|status" ;;
esac
