# shortcuts136.sh : source this file to get the short names  lab  and  t
lab() { sudo /usr/local/sbin/lab136.sh "$@"; }
t() { ( cd /opt/lab136 && python3 -m pytest "$@" ); }
