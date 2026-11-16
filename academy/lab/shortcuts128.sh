# shortcuts128.sh : source this file to get the short names  lab  pg  and  pg_ctl
lab() { sudo /usr/local/sbin/lab128.sh "$@"; }
pg() { psql -h /opt/lab128 -p 5481 -d shop "$@"; }
pg_ctl() { "$(ls -d /usr/lib/postgresql/*/bin | sort -V | tail -n 1)/pg_ctl" "$@"; }
