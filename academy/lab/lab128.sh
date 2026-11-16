#!/bin/sh
# lab128.sh : Databases for DevOps, lesson 3: configuration and persistent storage. Run with sudo, on any Linux machine with PostgreSQL (server and psql).
#   up | check | down | status
# Needs: sudo apt install -y postgresql postgresql-client     port 5481 free. (The lab runs its own private PostgreSQL cluster in /opt/lab128; it does not touch the system PostgreSQL.)
# Mission: configure the server with a drop-in file, restart it, and prove the data survives on the persistent data directory.
D=${LAB128_DIR:-/opt/lab128}
OWNER=${SUDO_USER:-root}
if [ "$OWNER" = root ]; then OWNER=postgres; id postgres >/dev/null 2>&1 || { echo "run with sudo from a normal user account"; exit 1; }; fi
BIN=$(ls -d /usr/lib/postgresql/*/bin 2>/dev/null | sort -V | tail -n 1)
RU="runuser -u $OWNER --"
PORT=5481
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
  mkdir -p $D/data/conf.d; chown $OWNER $D/data/conf.d
  echo "include_dir = 'conf.d'" >> $D/data/postgresql.conf
  $RU $BIN/pg_ctl -D $D/data -o "-p $PORT -k $D -c listen_addresses=" -l $D/server.log -w start >/dev/null 2>&1 || { echo "PostgreSQL did not start: see $D/server.log"; exit 1; }
  P="$RU psql -h $D -p $PORT -X -q -v ON_ERROR_STOP=1"
  $P -d postgres -c "CREATE DATABASE shop" >/dev/null
  $P -d shop >/dev/null <<'EOF_SQL'
CREATE TABLE notes (id serial PRIMARY KEY, body text NOT NULL, saved_at timestamptz NOT NULL DEFAULT now());
INSERT INTO notes (body) VALUES ('first note');
EOF_SQL
  cat > $D/TASKS.txt <<'EOF_T'
LAB 128  Configuration and persistent storage
Open a terminal in /opt/lab128. The short name  pg  opens psql on the shop database.  Load it with: source shortcuts128.sh
This PostgreSQL keeps ALL its data in /opt/lab128/data (the persistent data directory). Its own settings are small defaults. You will configure it with a drop-in file and prove the data survives a restart.

1  Look:       pg   then   SHOW data_directory;   SHOW max_connections;   SHOW shared_buffers;   SHOW log_min_duration_statement;
2  Answer:     write the default max_connections you saw into answers.txt (one line).
3  Drop-in:    create data/conf.d/app.conf (the server already includes that folder) with exactly these three lines:
                 max_connections = 50
                 shared_buffers = 64MB
                 log_min_duration_statement = 250
4  Reload:     SELECT pg_reload_conf();   then SHOW log_min_duration_statement;  (only that one applies now: the others need a restart. See: SELECT name, pending_restart FROM pg_settings WHERE pending_restart;)
5  Restart:    pg_ctl -D data -l server.log -w restart     (run as yourself, in /opt/lab128; after: source shortcuts128.sh gives you pg_ctl)
6  Persist:    before the restart, INSERT INTO notes (body) VALUES ('survives'); After the restart: SELECT * FROM notes; both rows are still there. SELECT pg_postmaster_start_time(); shows the new start.
7  lab check   (judges you: you need all 5 PASS)
8  lab down    (stops PostgreSQL and removes it all)
If a step fails, read the message: PostgreSQL says what it did not like.
EOF_T
  chown -R $OWNER $D 2>/dev/null
  echo "lab 128 ready in $D. Read TASKS.txt, then run: pg"
}
pass=0; total=5
ok() { pass=$((pass+1)); echo "  PASS  $1"; }
no() { echo "  FAIL  $1"; }
check() {
  [ -f $D/data/postmaster.pid ] || { echo "the lab is not running: run  lab up"; exit 1; }
  PS="$RU psql -h $D -p $PORT -X -q -At -d shop"
  a=$(sed -n 1p $D/answers.txt 2>/dev/null | tr -d ' \r')
  if [ "$a" = 100 ]; then ok "1 answers.txt has the default max_connections"; else no "1 answers.txt line 1 must be the default max_connections you saw with SHOW max_connections before changing anything"; fi
  mc=$($PS -c "SHOW max_connections" 2>/dev/null); sb=$($PS -c "SHOW shared_buffers" 2>/dev/null)
  if [ "$mc" = 50 ] && [ "$sb" = 64MB ]; then ok "2 max_connections 50 and shared_buffers 64MB applied"; else no "2 max_connections=$mc shared_buffers=$sb : they need to be 50 and 64MB, and need a restart to apply"; fi
  ms=$($PS -c "SHOW log_min_duration_statement" 2>/dev/null)
  if [ "$ms" = 250ms ]; then ok "3 slow-query log threshold is 250ms"; else no "3 log_min_duration_statement is $ms : put log_min_duration_statement = 250 in data/conf.d/app.conf and reload"; fi
  if [ -f $D/data/conf.d/app.conf ] && grep -q "max_connections" $D/data/conf.d/app.conf && grep -q "^max_connections = 100" $D/data/postgresql.conf && grep -q "^shared_buffers = 128MB" $D/data/postgresql.conf; then ok "4 settings are in the drop-in conf.d/app.conf"; else no "4 the settings must be in data/conf.d/app.conf and postgresql.conf must stay untouched"; fi
  n=$($PS -c "SELECT count(*) FROM notes WHERE body='survives' AND saved_at < pg_postmaster_start_time()" 2>/dev/null); k=$($PS -c "SELECT count(*) FROM notes" 2>/dev/null)
  if [ "$n" = 1 ] && [ "$k" = 2 ]; then ok "5 the note saved before the restart survived"; else no "5 insert the note 'survives' BEFORE the restart, then restart: both notes must still be there (count now: $k)"; fi
  echo; echo "$pass / $total passed"; [ $pass -eq $total ]
}
case "$1" in
  up) up ;;
  check) check ;;
  down) down; echo "lab 128 removed." ;;
  status) [ -f $D/data/postmaster.pid ] && echo running || echo "not running" ;;
  *) echo "usage: sudo lab128.sh up|check|down|status" ;;
esac
