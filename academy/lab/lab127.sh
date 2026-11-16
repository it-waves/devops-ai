#!/bin/sh
# lab127.sh : Databases for DevOps, lesson 2: roles, passwords and least privilege. Run with sudo, on any Linux machine with PostgreSQL (server and psql).
#   up | check | down | status
# Needs: sudo apt install -y postgresql postgresql-client     port 5471 free. (The lab runs its own private PostgreSQL cluster in /opt/lab127; it does not touch the system PostgreSQL.)
# Mission: the app role shopapp is a superuser with a weak password and no password check. Make it least-privilege.
D=${LAB127_DIR:-/opt/lab127}
OWNER=${SUDO_USER:-root}
if [ "$OWNER" = root ]; then OWNER=postgres; id postgres >/dev/null 2>&1 || { echo "run with sudo from a normal user account"; exit 1; }; fi
BIN=$(ls -d /usr/lib/postgresql/*/bin 2>/dev/null | sort -V | tail -n 1)
RU="runuser -u $OWNER --"
PORT=5471
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
  $RU $BIN/pg_ctl -D $D/data -o "-p $PORT -k $D -c listen_addresses=127.0.0.1" -l $D/server.log -w start >/dev/null 2>&1 || { echo "PostgreSQL did not start: see $D/server.log"; exit 1; }
  printf '%s\n' 'local all all trust' 'host all all 127.0.0.1/32 trust' > $D/data/pg_hba.conf
  P="$RU psql -h $D -p $PORT -X -q -v ON_ERROR_STOP=1"
  $P -d postgres -c "CREATE DATABASE shop" >/dev/null
  $P -d postgres -c "SELECT pg_reload_conf()" >/dev/null
  $P -d shop >/dev/null <<'EOF_SQL'
CREATE ROLE shopapp LOGIN SUPERUSER PASSWORD 'changeme';
CREATE TABLE customers (id serial PRIMARY KEY, name text NOT NULL);
CREATE TABLE products (id serial PRIMARY KEY, name text NOT NULL, price_cents int NOT NULL);
CREATE TABLE orders (id serial PRIMARY KEY, customer_id int NOT NULL REFERENCES customers(id), product_id int NOT NULL REFERENCES products(id), qty int NOT NULL);
INSERT INTO customers (name) VALUES ('Ana'), ('Ben'), ('Cy');
INSERT INTO products (name, price_cents) VALUES ('Mug', 900), ('Lamp', 2500);
INSERT INTO orders (customer_id, product_id, qty) VALUES (1, 1, 2), (2, 2, 1), (3, 1, 4);
EOF_SQL
  cat > $D/TASKS.txt <<'EOF_T'
LAB 127  Least privilege: roles, passwords and grants
Open a terminal in /opt/lab127. The short name  pg  opens psql on the shop database as the admin of this lab.  Load it with: source shortcuts127.sh
The shop application connects as the role  shopapp  over the network (127.0.0.1, port 5471). Today shopapp is far too powerful.

1  Look:       pg      then   \du      (who is a Superuser?)     Count the superusers BEFORE you change anything.
2  Answer:     write the number of superuser roles you saw into answers.txt (one line).
3  Demote:     ALTER ROLE shopapp NOSUPERUSER NOCREATEDB NOCREATEROLE;
4  Password:   the password is 'changeme'. Choose a long new one (12 or more characters), set it, and keep it for the app:
               ALTER ROLE shopapp PASSWORD 'your-new-password';       and write one line  DB_PASSWORD=your-new-password  into app.env
5  Grants:     shopapp may read customers and products, and read and insert orders. Nothing else.
               GRANT SELECT ON customers, products TO shopapp;
               GRANT SELECT, INSERT ON orders TO shopapp;
               GRANT USAGE ON SEQUENCE orders_id_seq TO shopapp;     (an insert needs the sequence too)
6  Require passwords: pg_hba.conf says  host ... trust  : anyone on this machine can log in as anybody. Edit  data/pg_hba.conf , change trust to scram-sha-256 on the host line, then reload:  SELECT pg_reload_conf();   (keep the local line as it is)
7  Test as the app:  PGPASSWORD=your-new-password psql -h 127.0.0.1 -p 5471 -U shopapp shop      (try a SELECT, an INSERT into orders, and a DELETE: the delete must fail)
8  lab check   (judges you: you need all 5 PASS)
9  lab down    (stops PostgreSQL and removes it all)
If a step fails, read the message: PostgreSQL says what it did not like.
EOF_T
  chown -R $OWNER $D 2>/dev/null
  echo "lab 127 ready in $D. Read TASKS.txt, then run: pg"
}
pass=0; total=5
ok() { pass=$((pass+1)); echo "  PASS  $1"; }
no() { echo "  FAIL  $1"; }
check() {
  [ -S $D/.s.PGSQL.$PORT ] || { echo "lab is not up: run  lab up"; exit 1; }
  q() { $RU psql -h $D -p $PORT -X -q -At -d shop -c "$1" 2>/dev/null; }
  app() { PGPASSWORD="$PW" psql -h 127.0.0.1 -p $PORT -X -q -At -w -U shopapp -d shop -c "$1" 2>&1; }
  PW=$(sed -n 's/^DB_PASSWORD=//p' $D/app.env 2>/dev/null | head -n 1 | tr -d '\r')
  a1=$(sed -n 1p $D/answers.txt 2>/dev/null | tr -d ' \r')
  if [ "$a1" = 2 ]; then ok "1 you counted the superusers before changing anything"; else no "1 answers.txt line 1 is '$a1': count the Superuser roles in \\du before you change anything"; fi
  su=$(q "SELECT rolsuper FROM pg_roles WHERE rolname = 'shopapp'")
  if [ "$su" = f ]; then ok "2 shopapp is no longer a superuser"; else no "2 shopapp rolsuper is '$su': ALTER ROLE shopapp NOSUPERUSER ..."; fi
  if [ -n "$PW" ] && [ "$PW" != changeme ] && [ ${#PW} -ge 12 ] && [ "$(app 'SELECT 1')" = 1 ]; then ok "3 shopapp has a new strong password, and app.env holds it"; else no "3 app.env needs DB_PASSWORD=<12+ characters, not changeme> and it must be the role's real password"; fi
  PGPASSWORD= psql -h 127.0.0.1 -p $PORT -X -q -At -w -U shopapp -d shop -c 'SELECT 1' >/dev/null 2>&1; nopw=$?
  PGPASSWORD=changeme psql -h 127.0.0.1 -p $PORT -X -q -At -w -U shopapp -d shop -c 'SELECT 1' >/dev/null 2>&1; oldpw=$?
  if [ $nopw -ne 0 ] && [ $oldpw -ne 0 ]; then ok "4 the network login now demands the password"; else no "4 a login without a password or with the old one still works: pg_hba.conf host line must say scram-sha-256, then reload"; fi
  r1=$(app 'SELECT count(*) FROM orders'); r2=$(app "BEGIN; INSERT INTO orders (customer_id, product_id, qty) VALUES (1, 1, 1); ROLLBACK;" | grep -c ERROR); r3=$(app 'BEGIN; DELETE FROM orders; ROLLBACK;' | grep -c 'permission denied'); r4=$(app "BEGIN; UPDATE customers SET name = 'x'; ROLLBACK;" | grep -c 'permission denied'); r5=$(app 'BEGIN; CREATE TABLE evil (a int); ROLLBACK;' | grep -c 'denied')
  if [ "$r1" = 3 ] && [ "$r2" = 0 ] && [ "$r3" -ge 1 ] && [ "$r4" -ge 1 ] && [ "$r5" -ge 1 ]; then ok "5 the app can read and insert orders, and nothing more"; else no "5 reads '$r1', insert errors '$r2', delete denied '$r3', update denied '$r4', create denied '$r5': grant only SELECT, INSERT on orders, SELECT on the others, and the sequence"; fi
  echo; echo "$pass / $total passed"; [ $pass -eq $total ]
}
status() { [ -S $D/.s.PGSQL.$PORT ] && echo "lab 127 is up in $D" || echo "lab 127 is not up"; }
case "$1" in up) up ;; check) check ;; down) down; echo "lab 127 removed" ;; status) status ;; *) echo "usage: lab127.sh up|check|down|status" ;; esac
