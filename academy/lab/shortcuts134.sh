# shortcuts134.sh : source this file to get the short names  lab  pg  and  usedb
lab() { sudo /usr/local/sbin/lab134.sh "$@"; }
pg() { psql -h /opt/lab134 -p 5514 -U postgres -d cloudcart "$@"; }
usedb() { export PGHOST=/opt/lab134 PGPORT=5514 PGUSER=postgres; echo "PGHOST=$PGHOST PGPORT=$PGPORT PGUSER=$PGUSER"; }
