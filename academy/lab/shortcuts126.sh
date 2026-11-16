# shortcuts126.sh : source this file to get the short names  lab  and  pg
lab() { sudo /usr/local/sbin/lab126.sh "$@"; }
pg() { psql -h /opt/lab126 -p 5461 -d shop "$@"; }
