# shortcuts141.sh : source this file to get the short names  lab  and  t
lab() { sudo /usr/local/sbin/lab141.sh "$@"; }
t() { ( cd /opt/lab141 && python3 -m pytest "$@" ); }
