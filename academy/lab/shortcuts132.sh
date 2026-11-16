# shortcuts132.sh : source this file to get the short names  lab  pg  and  usedb
lab() { sudo /usr/local/sbin/lab132.sh "$@"; }
pg() { psql -h /opt/lab132 -p 5512 -d shop "$@"; }
usedb() { export PGHOST=/opt/lab132 PGPORT=5512; echo "PGHOST=$PGHOST PGPORT=$PGPORT"; }
