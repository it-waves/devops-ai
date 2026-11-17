# shortcuts135.sh : source this file to get the short names  lab  and  t
lab() { sudo /usr/local/sbin/lab135.sh "$@"; }
t() { ( cd /opt/lab135 && python3 -m pytest "$@" ); }
