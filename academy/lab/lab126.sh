#!/bin/sh
# lab126.sh : Databases for DevOps, lesson 1: meet PostgreSQL, connect with psql, run diagnostic SQL and a transaction. Run with sudo, on any Linux machine with PostgreSQL (server and psql).
#   up | check | down | status
# Needs: sudo apt install -y postgresql postgresql-client     port 5461 free. (The lab runs its own private PostgreSQL cluster in /opt/lab126; it does not touch the system PostgreSQL.)
# Mission: connect to the shop database, answer three questions with SQL, and run one transaction that rolls back and one that commits.
D=${LAB126_DIR:-/opt/lab126}
OWNER=${SUDO_USER:-root}
if [ "$OWNER" = root ]; then OWNER=postgres; id postgres >/dev/null 2>&1 || { echo "run with sudo from a normal user account"; exit 1; }; fi
BIN=$(ls -d /usr/lib/postgresql/*/bin 2>/dev/null | sort -V | tail -n 1)
RU="runuser -u $OWNER --"
PORT=5461
down() {
  [ -f $D/data/postmaster.pid ] && $RU $BIN/pg_ctl -D $D/data -m fast stop >/dev/null 2>&1
  sleep 1
  rm -rf "${D:?}"/* "${D:?}"/.[!.]* 2>/dev/null; rmdir "$D" 2>/dev/null; true
}
up() {
  [ -n "$BIN" ] || { echo "PostgreSQL not found: run  sudo apt install -y postgresql postgresql-client"; exit 1; }
  command -v psql >/dev/null 2>&1 || { echo "psql not found: run  sudo apt install -y postgresql-client"; exit 1; }
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  down; mkdir -p $D; chown $OWNER $D
  $RU $BIN/initdb -D $D/data -A trust -E UTF8 --locale=C.UTF-8 >/dev/null 2>&1 || { echo "initdb failed"; exit 1; }
  $RU $BIN/pg_ctl -D $D/data -o "-p $PORT -k $D -c listen_addresses=''" -l $D/server.log -w start >/dev/null 2>&1 || { echo "PostgreSQL did not start: see $D/server.log"; exit 1; }
  P="$RU psql -h $D -p $PORT -X -q -v ON_ERROR_STOP=1"
  $P -d postgres -c "CREATE DATABASE shop" >/dev/null
  $P -d shop >/dev/null <<'EOF_SQL'
CREATE TABLE schema_migrations (version int PRIMARY KEY, applied_on date NOT NULL DEFAULT current_date);
CREATE TABLE customers (id serial PRIMARY KEY, name text NOT NULL);
CREATE TABLE products (id serial PRIMARY KEY, name text NOT NULL, price_cents int NOT NULL);
CREATE TABLE orders (id serial PRIMARY KEY, customer_id int NOT NULL REFERENCES customers(id), product_id int NOT NULL REFERENCES products(id), qty int NOT NULL);
INSERT INTO schema_migrations (version) VALUES (1);
INSERT INTO customers (name) VALUES ('Ana'), ('Ben'), ('Cy'), ('Dee'), ('Eli');
INSERT INTO products (name, price_cents) VALUES ('Mug', 900), ('Lamp', 2500), ('Desk', 14900);
INSERT INTO orders (customer_id, product_id, qty) SELECT (g % 5) + 1, (g % 3) + 1, (g % 4) + 1 FROM generate_series(1, 12) g;
EOF_SQL
  cat > $D/TASKS.txt <<'EOF_T'
LAB 126  Meet PostgreSQL: connect, look around, run a transaction
Open a terminal in /opt/lab126. The short name  pg  opens psql on the shop database of this lab.  Load it with: source shortcuts126.sh
The shop database has four tables. Do the steps in order.

1  Connect:      pg          (you see the prompt  shop=#  ; type  \q  to leave)
2  Look around:  \dt  lists the tables.    \d customers  describes one.    SELECT version();  shows the server.
3  Write three answers into  answers.txt , one per line, one number each:
     line 1: how many tables are in the shop database (count them with \dt, or:  SELECT count(*) FROM pg_tables WHERE schemaname = 'public';)
     line 2: how many rows are in the orders table:   SELECT count(*) FROM orders;
     line 3: the MAJOR version of the server (the first number of  SHOW server_version;)
4  Roll back a transaction:      BEGIN;   INSERT INTO customers (name) VALUES ('Ghost');   ROLLBACK;
   Look:  SELECT * FROM customers;    Ghost is gone.
5  Commit a transaction:         BEGIN;   INSERT INTO customers (name) VALUES ('Zed');     COMMIT;
   Look again: Zed stays. Notice his id: the rolled-back row still used up a number.
6  lab check   (judges you: you need all 5 PASS)
7  lab down    (stops PostgreSQL and removes it all)
If a step fails, read the message: PostgreSQL says what it did not like, and where.
EOF_T
  chown -R $OWNER $D 2>/dev/null
  echo "lab 126 ready in $D. Read TASKS.txt, then run: pg"
}
pass=0; total=5
ok() { pass=$((pass+1)); echo "  PASS  $1"; }
no() { echo "  FAIL  $1"; }
check() {
  [ -S $D/.s.PGSQL.$PORT ] || { echo "lab is not up: run  lab up"; exit 1; }
  q() { $RU psql -h $D -p $PORT -X -q -At -d shop -c "$1" 2>/dev/null; }
  a1=$(sed -n 1p $D/answers.txt 2>/dev/null | tr -d ' \r'); a2=$(sed -n 2p $D/answers.txt 2>/dev/null | tr -d ' \r'); a3=$(sed -n 3p $D/answers.txt 2>/dev/null | tr -d ' \r')
  maj=$(( $(q 'SHOW server_version_num') / 10000 ))
  if [ "$a1" = 4 ]; then ok "1 you counted the four tables"; else no "1 line 1 of answers.txt is '$a1': count the tables with \\dt"; fi
  if [ "$a2" = 12 ]; then ok "2 you counted the orders"; else no "2 line 2 of answers.txt is '$a2': SELECT count(*) FROM orders;"; fi
  if [ "$a3" = "$maj" ]; then ok "3 you read the server version"; else no "3 line 3 of answers.txt is '$a3': SHOW server_version; gives the major number"; fi
  zid=$(q "SELECT id FROM customers WHERE name = 'Zed'"); g=$(q "SELECT count(*) FROM customers WHERE name = 'Ghost'")
  if [ -n "$zid" ]; then ok "4 the committed transaction kept Zed"; else no "4 Zed is missing: BEGIN; INSERT ... ('Zed'); COMMIT;"; fi
  if [ "$zid" = 7 ] && [ "$g" = 0 ]; then ok "5 the rolled-back Ghost is gone, and it used up an id"; else no "5 Zed has id '$zid' and Ghost count is '$g': first BEGIN, insert Ghost, ROLLBACK; then insert Zed and COMMIT"; fi
  echo; echo "$pass / $total passed"; [ $pass -eq $total ]
}
status() { [ -S $D/.s.PGSQL.$PORT ] && echo "lab 126 is up in $D" || echo "lab 126 is not up"; }
case "$1" in up) up ;; check) check ;; down) down; echo "lab 126 removed" ;; status) status ;; *) echo "usage: lab126.sh up|check|down|status" ;; esac
