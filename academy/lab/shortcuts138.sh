# shortcuts138.sh : source this file to get the short names  lab  and  t
lab() { sudo /usr/local/sbin/lab138.sh "$@"; }
t() { ( cd /opt/lab138 && python3 -m pytest "$@" ); }
