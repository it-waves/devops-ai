# shortcuts137.sh : source this file to get the short names  lab  and  t
lab() { sudo /usr/local/sbin/lab137.sh "$@"; }
t() { ( cd /opt/lab137 && python3 -m pytest "$@" ); }
