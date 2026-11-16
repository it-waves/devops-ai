# shortcuts129.sh : source this file to get the short names  lab  and  pg
lab() { sudo /usr/local/sbin/lab129.sh "$@"; }
pg() { psql -h /opt/lab129 -p 5491 -d shop "$@"; }
