# shortcuts130.sh : source this file to get the short names  lab  pg  and  usedb
lab() { sudo /usr/local/sbin/lab130.sh "$@"; }
pg() { psql -h /opt/lab130 -p 5501 -d shop "$@"; }
usedb() { export PGHOST=/opt/lab130 PGPORT=5501; echo "PGHOST=$PGHOST PGPORT=$PGPORT"; }
