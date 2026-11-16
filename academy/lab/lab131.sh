#!/bin/sh
# lab131.sh : Databases for DevOps, lesson 6: tour a real database web UI (Adminer). Run with sudo, on any Linux machine.
#   up | check | down | status
# Needs: sudo apt install -y postgresql postgresql-client php-cli php-pgsql curl     ports 5511 (database) and 8085 (web page) free.
# The lab runs its own private PostgreSQL in /opt/lab131 and serves Adminer, one PHP file, on http://localhost:8085 . It touches nothing else.
D=${LAB131_DIR:-/opt/lab131}
OWNER=${SUDO_USER:-root}
if [ "$OWNER" = root ]; then OWNER=postgres; id postgres >/dev/null 2>&1 || { echo "run with sudo from a normal user account"; exit 1; }; fi
BIN=$(ls -d /usr/lib/postgresql/*/bin 2>/dev/null | sort -V | tail -n 1)
RU="runuser -u $OWNER --"
PORT=5511; WEB=8085; DBPASS='Shop-UI-131'
ADM_URL=https://github.com/vrana/adminer/releases/download/v5.4.1/adminer-5.4.1-en.php
down() {
  [ -f $D/web.pid ] && kill "$(cat $D/web.pid)" 2>/dev/null
  [ -f $D/data/postmaster.pid ] && $RU $BIN/pg_ctl -D $D/data -m fast stop >/dev/null 2>&1
  sleep 1
  rm -rf "${D:?}"/* "${D:?}"/.[!.]* 2>/dev/null; rmdir "$D" 2>/dev/null; true
}
up() {
  [ -n "$BIN" ] || { echo "PostgreSQL not found: run  sudo apt install -y postgresql postgresql-client"; exit 1; }
  command -v php >/dev/null 2>&1 || { echo "php not found: run  sudo apt install -y php-cli php-pgsql"; exit 1; }
  php -m 2>/dev/null | grep -qi pgsql || { echo "php pgsql driver missing: run  sudo apt install -y php-pgsql"; exit 1; }
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  down; mkdir -p $D/web; chown $OWNER $D $D/web
  if [ -n "$ADMINER_PHP" ] && [ -f "$ADMINER_PHP" ]; then cp "$ADMINER_PHP" $D/web/index.php
  else curl -fsSL -m 90 -o $D/web/index.php "$ADM_URL" || { echo "could not download Adminer from $ADM_URL"; exit 1; }; fi
  chown $OWNER $D/web/index.php
  # the local socket (this machine, the owner) is trusted for setup; the web page logs in with a password over TCP
  $RU $BIN/initdb -D $D/data --auth-local=trust --auth-host=scram-sha-256 -E UTF8 --locale=C.UTF-8 >/dev/null 2>&1 || { echo "initdb failed"; exit 1; }
  $RU $BIN/pg_ctl -D $D/data -o "-p $PORT -k $D -c listen_addresses=127.0.0.1" -l $D/server.log -w start >/dev/null 2>&1 || { echo "PostgreSQL did not start: see $D/server.log"; exit 1; }
  P="$RU psql -h $D -p $PORT -X -q -v ON_ERROR_STOP=1"
  $P -d postgres >/dev/null <<EOF_SQL
CREATE ROLE shopadmin LOGIN PASSWORD '$DBPASS';
CREATE DATABASE shop OWNER shopadmin;
EOF_SQL
  $P -U shopadmin -d shop >/dev/null <<'EOF_SQL'
CREATE TABLE customers (id serial PRIMARY KEY, name text NOT NULL, email text UNIQUE, city text);
CREATE TABLE products (id serial PRIMARY KEY, name text NOT NULL, price_cents int NOT NULL);
CREATE TABLE orders (id serial PRIMARY KEY, customer_id int NOT NULL REFERENCES customers(id), product_id int NOT NULL REFERENCES products(id), qty int NOT NULL DEFAULT 1, ordered_on date NOT NULL);
INSERT INTO customers (name, email, city) VALUES ('Ana','ana@example.com','Lagos'),('Ben','ben@example.com','Accra'),('Cy','cy@example.com','Nairobi'),('Dara','dara@example.com','Lagos');
INSERT INTO products (name, price_cents) VALUES ('Keyboard',4500),('Mouse',1900),('Monitor',18900),('Webcam',6400),('Headset',7200);
INSERT INTO orders (customer_id, product_id, qty, ordered_on) VALUES (1,1,1,'2026-10-01'),(1,2,2,'2026-10-03'),(2,3,1,'2026-10-04'),(3,4,1,'2026-10-06'),(2,5,1,'2026-10-09'),(4,1,2,'2026-10-10'),(3,2,1,'2026-10-12'),(1,3,1,'2026-10-15'),(4,5,1,'2026-10-18'),(2,2,3,'2026-10-20'),(3,1,1,'2026-10-22'),(4,4,2,'2026-10-25');
CREATE VIEW order_totals AS SELECT o.id AS order_id, c.name AS customer, p.name AS product, o.qty * p.price_cents AS total_cents FROM orders o JOIN customers c ON c.id = o.customer_id JOIN products p ON p.id = o.product_id;
EOF_SQL
  $P -U shopadmin -d shop -c "ANALYZE customers, products, orders"
  $RU sh -c "cd $D/web && nohup php -S 127.0.0.1:$WEB -t $D/web >$D/web.log 2>&1 & echo \$! > $D/web.pid"
  sleep 2
  cat > $D/TASKS.txt <<EOF_T
LAB 131  A tour of a database web page (Adminer on real PostgreSQL)
Open  http://localhost:$WEB  in a browser. Log in:  System PostgreSQL | Server 127.0.0.1:$PORT | Username shopadmin | Password $DBPASS | Database shop
Write your findings in  $D/answers.txt  (use any editor), one per line:

1  Select (data) on the table orders: how many rows?                         line 1
2  SQL command:  SELECT sum(total_cents) FROM order_totals;   the number      line 2
3  Edit the row of customer Cy: change the city to Paris (Edit link, Save)
4  New item in customers: name Eli, email eli@example.com, city Cairo   (Save)
5  Alter orders, Indexes: create a plain index on customer_id named orders_customer_idx
5b Structure of orders: how many columns?                                   line 3
6  lab check   (judges you: all 5 must PASS)        7  lab down  (removes it all)
Rule: look first, change second, and always know which database and table you are in.
EOF_T
  chown -R $OWNER $D 2>/dev/null
  echo "lab 131 ready: http://localhost:$WEB  tasks: $D/TASKS.txt"
}
pass=0; total=5
ok() { pass=$((pass+1)); echo "  PASS  $1"; }
no() { echo "  FAIL  $1"; }
check() {
  [ -f $D/data/postmaster.pid ] || { echo "the lab is not running: run  lab up"; exit 1; }
  PS="$RU psql -h $D -p $PORT -X -q -At"
  a=$(sed -n 1p $D/answers.txt 2>/dev/null | tr -d ' \r'); b=$(sed -n 2p $D/answers.txt 2>/dev/null | tr -d ' \r')
  EXP=$($PS -d shop -c "SELECT sum(total_cents) FROM order_totals" 2>/dev/null)
  if [ "$a" = 12 ] && [ "$b" = "$EXP" ] && [ -n "$EXP" ]; then ok "1 answers.txt: 12 orders and the right total"; else no "1 answers.txt: line 1 = rows in orders, line 2 = the sum"; fi
  c=$($PS -d shop -c "SELECT city FROM customers WHERE name='Cy'" 2>/dev/null)
  if [ "$c" = Paris ]; then ok "2 Cy now lives in Paris"; else no "2 customer Cy has city '$c': use Edit, then Save"; fi
  e=$($PS -d shop -c "SELECT count(*) FROM customers WHERE name='Eli' AND email='eli@example.com' AND city='Cairo'" 2>/dev/null)
  if [ "$e" = 1 ]; then ok "3 customer Eli exists"; else no "3 customer Eli (eli@example.com, Cairo) not found"; fi
  i=$($PS -d shop -c "SELECT indexdef FROM pg_indexes WHERE indexname='orders_customer_idx'" 2>/dev/null)
  case "$i" in *"ON public.orders"*"(customer_id)"*) ok "4 index orders_customer_idx on customer_id";; *) no "4 no index orders_customer_idx on orders(customer_id)";; esac
  o=$($PS -d shop -c "SELECT count(*) FROM orders" 2>/dev/null); t=$($PS -d shop -c "SELECT count(*) FROM information_schema.tables WHERE table_schema='public'" 2>/dev/null)
  d=$(sed -n 3p $D/answers.txt 2>/dev/null | tr -d ' \r')
  if [ "$d" = 5 ] && [ "$o" = 12 ] && [ "$t" = 4 ]; then ok "5 orders has 5 columns, and nothing was damaged"; else no "5 line 3 = columns of orders (5); orders must keep 12 rows, 4 tables"; fi
  echo; echo "$pass / $total passed"; [ $pass -eq $total ]
}
case "$1" in
  up) up ;;
  check) check ;;
  down) down; echo "lab 131 removed." ;;
  status) [ -f $D/data/postmaster.pid ] && echo running || echo "not running" ;;
  *) echo "usage: sudo lab131.sh up|check|down|status" ;;
esac
