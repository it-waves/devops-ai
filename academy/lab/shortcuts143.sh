# shortcuts143.sh : source this file to get the short names  lab  and  t
lab() { sudo /usr/local/sbin/lab143.sh "$@"; }
t() { ( cd /opt/lab143 && python3 -m pytest "$@" ); }
