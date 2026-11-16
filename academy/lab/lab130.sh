#!/bin/sh
# lab130.sh : Databases for DevOps, lesson 5: back up and restore a database, and prove the recovered data. Run with sudo, on any Linux machine with PostgreSQL (server and psql).
#   up | check | down | status
# Needs: sudo apt install -y postgresql postgresql-client     port 5501 free. (The lab runs its own private PostgreSQL cluster in /opt/lab130; it does not touch the system PostgreSQL.)
# Mission: take a backup, survive an accidental DELETE, restore into a new database and validate the recovered data.
D=${LAB130_DIR:-/opt/lab130}
OWNER=${SUDO_USER:-root}
if [ "$OWNER" = root ]; then OWNER=postgres; id postgres >/dev/null 2>&1 || { echo "run with sudo from a normal user account"; exit 1; }; fi
BIN=$(ls -d /usr/lib/postgresql/*/bin 2>/dev/null | sort -V | tail -n 1)
RU="runuser -u $OWNER --"
PORT=5501
down() {
  [ -f $D/data/postmaster.pid ] && $RU $BIN/pg_ctl -D $D/data -m fast stop >/dev/null 2>&1
  sleep 1
  rm -rf "${D:?}"/* "${D:?}"/.[!.]* 2>/dev/null; rmdir "$D" 2>/dev/null; true
}
up() {
  [ -n "$BIN" ] || { echo "PostgreSQL not found: run  sudo apt install -y postgresql postgresql-client"; exit 1; }
  command -v psql >/dev/null 2>&1 || { echo "psql not found: run  sudo apt install -y postgresql-client"; exit 1; }
  command -v pg_dump >/dev/null 2>&1 || { echo "pg_dump not found: run  sudo apt install -y postgresql-client"; exit 1; }
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  down; mkdir -p $D/backups; chown $OWNER $D $D/backups
  $RU $BIN/initdb -D $D/data -A trust -E UTF8 --locale=C.UTF-8 >/dev/null 2>&1 || { echo "initdb failed"; exit 1; }
  $RU $BIN/pg_ctl -D $D/data -o "-p $PORT -k $D -c listen_addresses=" -l $D/server.log -w start >/dev/null 2>&1 || { echo "PostgreSQL did not start: see $D/server.log"; exit 1; }
  P="$RU psql -h $D -p $PORT -X -q -v ON_ERROR_STOP=1"
  $P -d postgres -c "CREATE DATABASE shop" >/dev/null
  $P -d shop >/dev/null <<'EOF_SQL'
CREATE TABLE customers (id serial PRIMARY KEY, name text NOT NULL);
CREATE TABLE orders (id serial PRIMARY KEY, customer_id int NOT NULL REFERENCES customers(id), total_cents int NOT NULL);
INSERT INTO customers (name) VALUES ('Ana'), ('Ben'), ('Cy');
INSERT INTO orders (customer_id, total_cents) VALUES (1, 1800), (2, 2500), (3, 900), (1, 4000), (2, 2500), (3, 2700);
EOF_SQL
  cat > $D/TASKS.txt <<'EOF_T'
LAB 130  Back up and restore a database, and prove it
Open a terminal in /opt/lab130. Load the short names:  source shortcuts130.sh   (lab, pg, and  usedb  which sets PGHOST and PGPORT for this lab)
After  usedb  the tools pg_dump, pg_restore, createdb and psql all find this lab server by themselves.

1  Measure:   pg -c "SELECT count(*), sum(total_cents) FROM orders;"      write the two numbers into answers.txt, one per line
2  Backup:    pg_dump -Fc shop -f backups/shop.dump          (custom format, compressed)      then  ls -lh backups
3  Verify:    pg_restore -l backups/shop.dump | head          (the table of contents proves the file is readable)
4  Disaster:  pg -c "DELETE FROM orders;"      (an UPDATE or DELETE without WHERE)     count again: 0 rows
5  Restore:   createdb shop_restored      pg_restore -d shop_restored backups/shop.dump
6  Validate:  psql -d shop_restored -c "SELECT count(*), sum(total_cents) FROM orders;"      the numbers must match answers.txt
7  lab check   (judges you: you need all 5 PASS)        8  lab down  (removes it all)
Rule: a backup you never restored is only a hope. Restore into a NEW database first, validate, and only then put the data back.
EOF_T
  chown -R $OWNER $D 2>/dev/null
  echo "lab 130 ready in $D. Read TASKS.txt, then: source shortcuts130.sh ; usedb"
}
pass=0; total=5
ok() { pass=$((pass+1)); echo "  PASS  $1"; }
no() { echo "  FAIL  $1"; }
check() {
  [ -f $D/data/postmaster.pid ] || { echo "the lab is not running: run  lab up"; exit 1; }
  PS="$RU psql -h $D -p $PORT -X -q -At"
  a=$(sed -n 1p $D/answers.txt 2>/dev/null | tr -d ' \r'); b=$(sed -n 2p $D/answers.txt 2>/dev/null | tr -d ' \r')
  if [ "$a" = 6 ] && [ "$b" = 14400 ]; then ok "1 you measured 6 orders and 14400 cents first"; else no "1 answers.txt: line 1 = number of orders, line 2 = sum of total_cents, measured BEFORE the disaster"; fi
  f=$D/backups/shop.dump
  if [ -s $f ] && $RU $BIN/pg_restore -l $f >/dev/null 2>&1; then ok "2 backups/shop.dump is a valid backup"; else no "2 backups/shop.dump must exist and be readable by pg_restore -l"; fi
  s=$($PS -d shop -c "SELECT count(*) FROM orders" 2>/dev/null)
  if [ "$s" = 0 ]; then ok "3 the disaster happened: shop has 0 orders"; else no "3 shop.orders has $s rows: run the accidental DELETE FROM orders (after the backup!)"; fi
  r=$($PS -d shop_restored -c "SELECT count(*) FROM orders" 2>/dev/null)
  if [ "$r" = 6 ]; then ok "4 shop_restored has all 6 orders back"; else no "4 database shop_restored must exist with 6 orders (createdb, then pg_restore)"; fi
  t=$($PS -d shop_restored -c "SELECT sum(total_cents) FROM orders" 2>/dev/null)
  if [ "$t" = "$b" ] && [ "$t" = 14400 ]; then ok "5 the restored total matches answers.txt: validated"; else no "5 the restored sum is '$t' but answers.txt says '$b'"; fi
  echo; echo "$pass / $total passed"; [ $pass -eq $total ]
}
case "$1" in
  up) up ;;
  check) check ;;
  down) down; echo "lab 130 removed." ;;
  status) [ -f $D/data/postmaster.pid ] && echo running || echo "not running" ;;
  *) echo "usage: sudo lab130.sh up|check|down|status" ;;
esac
