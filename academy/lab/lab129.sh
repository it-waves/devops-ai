#!/bin/sh
# lab129.sh : Databases for DevOps, lesson 4: schema migrations in a deployment workflow. Run with sudo, on any Linux machine with PostgreSQL (server and psql).
#   up | check | down | status
# Needs: sudo apt install -y postgresql postgresql-client     port 5491 free. (The lab runs its own private PostgreSQL cluster in /opt/lab129; it does not touch the system PostgreSQL.)
# Mission: run versioned migrations with a tiny runner, survive a failing migration, fix it, add a new one, and prove the runner is repeatable.
D=${LAB129_DIR:-/opt/lab129}
OWNER=${SUDO_USER:-root}
if [ "$OWNER" = root ]; then OWNER=postgres; id postgres >/dev/null 2>&1 || { echo "run with sudo from a normal user account"; exit 1; }; fi
BIN=$(ls -d /usr/lib/postgresql/*/bin 2>/dev/null | sort -V | tail -n 1)
RU="runuser -u $OWNER --"
PORT=5491
down() {
  [ -f $D/data/postmaster.pid ] && $RU $BIN/pg_ctl -D $D/data -m fast stop >/dev/null 2>&1
  sleep 1
  rm -rf "${D:?}"/* "${D:?}"/.[!.]* 2>/dev/null; rmdir "$D" 2>/dev/null; true
}
up() {
  [ -n "$BIN" ] || { echo "PostgreSQL not found: run  sudo apt install -y postgresql postgresql-client"; exit 1; }
  command -v psql >/dev/null 2>&1 || { echo "psql not found: run  sudo apt install -y postgresql-client"; exit 1; }
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  down; mkdir -p $D/migrations; chown $OWNER $D
  $RU $BIN/initdb -D $D/data -A trust -E UTF8 --locale=C.UTF-8 >/dev/null 2>&1 || { echo "initdb failed"; exit 1; }
  $RU $BIN/pg_ctl -D $D/data -o "-p $PORT -k $D -c listen_addresses=" -l $D/server.log -w start >/dev/null 2>&1 || { echo "PostgreSQL did not start: see $D/server.log"; exit 1; }
  $RU psql -h $D -p $PORT -X -q -d postgres -c "CREATE DATABASE shop" >/dev/null
  cat > $D/migrations/001_customers.sql <<'EOF_M'
CREATE TABLE customers (id serial PRIMARY KEY, name text NOT NULL);
INSERT INTO customers (name) VALUES ('Ana'), ('Ben'), ('Cy');
EOF_M
  cat > $D/migrations/002_email.sql <<'EOF_M'
ALTER TABLE customers ADD COLUMN email text;
UPDATE customers SET email = lower(name) || '@example.test';
EOF_M
  cat > $D/migrations/003_orders.sql <<'EOF_M'
CREATE TABLE orders (
  id serial PRIMARY KEY,
  customer_id int NOT NULL REFERENCES customer(id),
  total_cents int NOT NULL
);
INSERT INTO orders (customer_id, total_cents)
  VALUES (1, 1800), (2, 2500);
EOF_M
  cat > $D/migrate.sh <<'EOF_R'
#!/bin/sh
# migrate.sh : a tiny migration runner.   ./migrate.sh status   |   ./migrate.sh up
export PGHOST=/opt/lab129 PGPORT=5491 PGDATABASE=shop PGOPTIONS='--client-min-messages=warning'
cd "$(dirname "$0")/migrations"
P="psql -X -q -At -v ON_ERROR_STOP=1"
$P -c "CREATE TABLE IF NOT EXISTS schema_migrations (version text PRIMARY KEY, applied_at timestamptz NOT NULL DEFAULT now())"
case "$1" in
  status)
    for f in *.sql; do v=$(basename $f .sql)
      if [ "$($P -c "SELECT 1 FROM schema_migrations WHERE version='$v'")" = 1 ]; then echo "applied  $v"; else echo "pending  $v"; fi
    done ;;
  up)
    n=0
    for f in *.sql; do v=$(basename $f .sql)
      [ "$($P -c "SELECT 1 FROM schema_migrations WHERE version='$v'")" = 1 ] && continue
      echo "applying $v"
      if $P --single-transaction -f "$f" -c "INSERT INTO schema_migrations (version) VALUES ('$v')" >/dev/null; then n=$((n+1)); else echo "FAILED  $v (rolled back, nothing applied)"; exit 1; fi
    done
    echo "done: $n applied" ;;
  *) echo "usage: ./migrate.sh status|up" ;;
esac
EOF_R
  chmod +x $D/migrate.sh
  cat > $D/TASKS.txt <<'EOF_T'
LAB 129  Schema migrations
Open a terminal in /opt/lab129. Short names:  pg  (psql on the shop database)  Load with: source shortcuts129.sh
migrations/ holds numbered SQL files. migrate.sh applies the ones not yet recorded in schema_migrations, each in ONE transaction.

1  Look:      cat migrations/*.sql     ./migrate.sh status      (all pending)
2  Run:       ./migrate.sh up          (001 and 002 apply, 003 FAILS and rolls back)
3  Answer:    write into answers.txt (one line) how many migrations are applied now (ask: ./migrate.sh status)
4  Read:      the error says  relation "customer" does not exist.  003 never applied, so you may fix it: the table is  customers .
5  Fix:       vim migrations/003_orders.sql   then   ./migrate.sh up      (003 applies)
6  New:       create migrations/004_status.sql :   ALTER TABLE orders ADD COLUMN status text NOT NULL DEFAULT 'new';   then ./migrate.sh up
7  Repeat:    ./migrate.sh up again: it must say  done: 0 applied
8  lab check  (judges you: you need all 5 PASS)        9  lab down  (removes it all)
Rule: never edit a migration that has already been applied. Add a new one instead.
EOF_T
  chown -R $OWNER $D 2>/dev/null
  echo "lab 129 ready in $D. Read TASKS.txt, then run: ./migrate.sh status"
}
pass=0; total=5
ok() { pass=$((pass+1)); echo "  PASS  $1"; }
no() { echo "  FAIL  $1"; }
check() {
  [ -f $D/data/postmaster.pid ] || { echo "the lab is not running: run  lab up"; exit 1; }
  PS="$RU psql -h $D -p $PORT -X -q -At -d shop"
  a=$(sed -n 1p $D/answers.txt 2>/dev/null | tr -d ' \r')
  if [ "$a" = 2 ]; then ok "1 you counted the 2 migrations that applied first"; else no "1 answers.txt line 1 must be how many migrations were applied after the FIRST ./migrate.sh up (see the status)"; fi
  v=$($PS -c "SELECT string_agg(version, ',' ORDER BY version) FROM schema_migrations" 2>/dev/null)
  o=$($PS -c "SELECT count(*) FROM orders" 2>/dev/null)
  if [ "$o" = 2 ] && echo "$v" | grep -q 003_orders; then ok "2 003 is fixed and applied (2 orders)"; else no "2 fix migrations/003_orders.sql (customer -> customers) and run ./migrate.sh up"; fi
  s=$($PS -c "SELECT count(*) FROM information_schema.columns WHERE table_name='orders' AND column_name='status'" 2>/dev/null)
  if [ "$s" = 1 ] && echo "$v" | grep -q 004; then ok "3 your 004 migration added orders.status"; else no "3 add migrations/004_*.sql that adds the column status to orders, then ./migrate.sh up"; fi
  c=$($PS -c "SELECT count(*) FROM schema_migrations" 2>/dev/null)
  if [ "$c" = 4 ]; then ok "4 schema_migrations lists exactly 4 versions"; else no "4 schema_migrations has $c rows: it must list 4 migrations, each once"; fi
  e=$($PS -c "SELECT count(*) FROM customers WHERE email LIKE '%@example.test'" 2>/dev/null)
  if [ "$e" = 3 ]; then ok "5 the 3 customers kept their data and emails"; else no "5 the customers data must stay intact (3 rows with email)"; fi
  echo; echo "$pass / $total passed"; [ $pass -eq $total ]
}
case "$1" in
  up) up ;;
  check) check ;;
  down) down; echo "lab 129 removed." ;;
  status) [ -f $D/data/postmaster.pid ] && echo running || echo "not running" ;;
  *) echo "usage: sudo lab129.sh up|check|down|status" ;;
esac
