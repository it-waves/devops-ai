# shortcuts140.sh : source this file to get the short names  lab  and  t
lab() { sudo /usr/local/sbin/lab140.sh "$@"; }
t() { ( cd /opt/lab140 && python3 -m pytest "$@" ); }
