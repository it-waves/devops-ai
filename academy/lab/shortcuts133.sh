# shortcuts133.sh : source this file to get the short names  lab  pg  and  usedb
lab() { sudo /usr/local/sbin/lab133.sh "$@"; }
pg() { PGPASSWORD='Shop-app-133' psql -h 127.0.0.1 -p 5513 -U shopapp -d shop "$@"; }
usedb() { export PGHOST=127.0.0.1 PGPORT=5513 PGUSER=shopapp; echo "PGHOST=$PGHOST PGPORT=$PGPORT PGUSER=$PGUSER"; }
