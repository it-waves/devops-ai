# shortcuts127.sh : source this file to get the short names  lab  and  pg
lab() { sudo /usr/local/sbin/lab127.sh "$@"; }
pg() { psql -h /opt/lab127 -p 5471 -d shop "$@"; }
