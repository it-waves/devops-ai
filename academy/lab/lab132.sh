#!/bin/sh
# lab132.sh : Databases for DevOps, lesson 7: inspect connections, locks, resource pressure and slow queries. Run with sudo, on any Linux machine with PostgreSQL (server, contrib and psql).
#   up | check | down | status
# Needs: sudo apt install -y postgresql postgresql-client     port 5512 free. (The lab runs its own private PostgreSQL cluster in /opt/lab132; it does not touch the system PostgreSQL.)
# Mission: a busy shop database has a stuck session and a slow query. Find them, fix them, and prove it.
D=${LAB132_DIR:-/opt/lab132}
OWNER=${SUDO_USER:-root}
if [ "$OWNER" = root ]; then OWNER=postgres; id postgres >/dev/null 2>&1 || { echo "run with sudo from a normal user account"; exit 1; }; fi
BIN=$(ls -d /usr/lib/postgresql/*/bin 2>/dev/null | sort -V | tail -n 1)
RU="runuser -u $OWNER --"
PORT=5512
down() {
  pkill -f "sleep 86413" 2>/dev/null
  [ -f $D/data/postmaster.pid ] && $RU $BIN/pg_ctl -D $D/data -m fast stop >/dev/null 2>&1
  sleep 1
  rm -rf "${D:?}"/* "${D:?}"/.[!.]* 2>/dev/null; rmdir "$D" 2>/dev/null; true
}
up() {
  [ -n "$BIN" ] || { echo "PostgreSQL not found: run  sudo apt install -y postgresql postgresql-client"; exit 1; }
  command -v psql >/dev/null 2>&1 || { echo "psql not found: run  sudo apt install -y postgresql-client"; exit 1; }
  [ -f "$(dirname $BIN)/lib/pg_stat_statements.so" ] || { echo "pg_stat_statements missing: run  sudo apt install -y postgresql postgresql-contrib"; exit 1; }
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  down; mkdir -p $D; chown $OWNER $D
  $RU $BIN/initdb -D $D/data -A trust -E UTF8 --locale=C.UTF-8 >/dev/null 2>&1 || { echo "initdb failed"; exit 1; }
  $RU $BIN/pg_ctl -D $D/data -o "-p $PORT -k $D -c listen_addresses= -c max_connections=40 -c max_parallel_workers_per_gather=0 -c shared_preload_libraries=pg_stat_statements -c log_lock_waits=on -c deadlock_timeout=1s" -l $D/server.log -w start >/dev/null 2>&1 || { echo "PostgreSQL did not start: see $D/server.log"; exit 1; }
  P="$RU psql -h $D -p $PORT -X -q -v ON_ERROR_STOP=1"
  $P -d postgres -c "CREATE DATABASE shop" >/dev/null
  $P -d shop >/dev/null <<'EOF_SQL'
CREATE EXTENSION pg_stat_statements;
CREATE TABLE accounts (id int PRIMARY KEY, owner text NOT NULL, balance int NOT NULL);
INSERT INTO accounts VALUES (1, 'Ana', 100), (2, 'Ben', 100), (3, 'Cy', 100);
CREATE TABLE orders (id serial PRIMARY KEY, customer_id int NOT NULL, total_cents int NOT NULL, ordered_on date NOT NULL);
INSERT INTO orders (customer_id, total_cents, ordered_on) SELECT (random()*999)::int + 1, (random()*9000)::int + 500, date '2026-01-01' + (random()*300)::int FROM generate_series(1, 300000);
ANALYZE;
EOF_SQL
  i=0; while [ $i -lt 25 ]; do echo "SELECT count(*), sum(total_cents) FROM orders WHERE customer_id = 777;"; i=$((i+1)); done > $D/.work.sql
  $RU env PGAPPNAME=reports psql -h $D -p $PORT -X -q -d shop -f $D/.work.sql >/dev/null 2>&1
  $RU psql -h $D -p $PORT -X -q -d shop -c "SELECT pg_stat_statements_reset()" >/dev/null 2>&1
  $RU env PGAPPNAME=reports psql -h $D -p $PORT -X -q -d shop -f $D/.work.sql >/dev/null 2>&1
  rm -f $D/.work.sql
  n=0; while [ $n -lt 3 ]; do
    $RU sh -c "( echo 'SELECT 1;'; sleep 86413 ) | PGAPPNAME=cart-api nohup psql -h $D -p $PORT -X -q -d shop >/dev/null 2>&1 &"
    n=$((n+1))
  done
  $RU sh -c "( echo 'BEGIN;'; echo 'UPDATE accounts SET balance = balance WHERE id = 1;'; sleep 86413 ) | PGAPPNAME=report-job nohup psql -h $D -p $PORT -X -q -d shop >/dev/null 2>&1 &"
  sleep 2
  $RU sh -c "PGAPPNAME=cart-api nohup psql -h $D -p $PORT -X -q -d shop -c 'UPDATE accounts SET balance = balance + 1 WHERE id = 1' >/dev/null 2>&1 &"
  sleep 2
  cat > $D/TASKS.txt <<'EOF_T'
LAB 132  Inspect connections, locks and slow queries
Open a terminal in /opt/lab132. Load the short names:  source shortcuts132.sh   (lab, pg, and  usedb  which sets PGHOST and PGPORT for this lab)
The shop database is busy: some web app sessions are connected, one session is stuck holding a lock, and a report query is slow.

1  Connections:  pg -c "SELECT application_name, state, count(*) FROM pg_stat_activity WHERE datname='shop' GROUP BY 1,2;"
   How many sessions are named cart-api?   And what is max_connections (SHOW max_connections)?   Write them into answers.txt: line 1 and line 2
2  Locks:        find the blocker:  SELECT pid, application_name, state, pg_blocking_pids(pid) FROM pg_stat_activity WHERE datname='shop';
   Write the PID of the session that is BLOCKING the others on line 3 of answers.txt
3  Fix it:       end that one session with  SELECT pg_terminate_backend(PID);   The waiting update must then finish by itself
4  Slow query:   pg -c "EXPLAIN (ANALYZE) SELECT count(*), sum(total_cents) FROM orders WHERE customer_id = 777;"     it reads every row (Seq Scan)
   Also look at  SELECT calls, round(mean_exec_time::numeric,1) AS ms, query FROM pg_stat_statements ORDER BY total_exec_time DESC LIMIT 3;
5  Speed it up:  CREATE INDEX orders_customer_idx ON orders (customer_id);     then run the EXPLAIN again: it must use the index
6  lab check   (judges you: you need all 5 PASS)        7  lab down  (removes it all)
Rule: look first (pg_stat_activity, pg_locks), end only the one session that blocks, and prefer pg_cancel_backend before pg_terminate_backend.
EOF_T
  chown -R $OWNER $D 2>/dev/null
  $RU psql -h $D -p $PORT -X -q -At -d shop -c "SELECT pid FROM pg_stat_activity WHERE application_name='report-job'" > $D/.blocker
  chown root:root $D/.blocker; chmod 600 $D/.blocker
  echo "lab 132 ready in $D. Read TASKS.txt, then: source shortcuts132.sh ; usedb"
}
pass=0; total=5
ok() { pass=$((pass+1)); echo "  PASS  $1"; }
no() { echo "  FAIL  $1"; }
check() {
  [ -f $D/data/postmaster.pid ] || { echo "the lab is not running: run  lab up"; exit 1; }
  PS="$RU psql -h $D -p $PORT -X -q -At -d shop"
  a=$(sed -n 1p $D/answers.txt 2>/dev/null | tr -d ' \r'); b=$(sed -n 2p $D/answers.txt 2>/dev/null | tr -d ' \r'); c=$(sed -n 3p $D/answers.txt 2>/dev/null | tr -d ' \r')
  if [ "$a" = 4 ] && [ "$b" = 40 ]; then ok "1 answers.txt: 4 cart-api sessions, max_connections 40"; else no "1 answers.txt: line 1 = sessions named cart-api, line 2 = max_connections"; fi
  bp=$(cat $D/.blocker 2>/dev/null)
  if [ -n "$bp" ] && [ "$c" = "$bp" ]; then ok "2 answers.txt line 3 names the blocking session"; else no "2 answers.txt line 3 must be the PID of the session that blocks the others"; fi
  w=$($PS -c "SELECT count(*) FROM pg_stat_activity WHERE application_name='report-job'" 2>/dev/null); bal=$($PS -c "SELECT balance FROM accounts WHERE id=1" 2>/dev/null)
  if [ "$w" = 0 ] && [ "$bal" = 101 ]; then ok "3 the blocker is gone and the waiting update finished"; else no "3 end ONLY the blocking session (pg_terminate_backend); the waiting update then completes"; fi
  ix=$($PS -c "SELECT count(*) FROM pg_indexes WHERE tablename='orders' AND indexdef LIKE '%(customer_id)%'" 2>/dev/null)
  if [ "$ix" -ge 1 ] 2>/dev/null; then ok "4 an index on orders(customer_id) exists"; else no "4 create an index on orders(customer_id)"; fi
  pl=$($PS -c "EXPLAIN SELECT count(*), sum(total_cents) FROM orders WHERE customer_id = 777" 2>/dev/null | grep -c "Index")
  if [ "$pl" -ge 1 ] 2>/dev/null; then ok "5 the slow query now uses the index"; else no "5 EXPLAIN of the report query must show an Index scan"; fi
  echo; echo "$pass / $total passed"; [ $pass -eq $total ]
}
case "$1" in
  up) up ;;
  check) check ;;
  down) down; echo "lab 132 removed." ;;
  status) [ -f $D/data/postmaster.pid ] && echo running || echo "not running" ;;
  *) echo "usage: sudo lab132.sh up|check|down|status" ;;
esac
