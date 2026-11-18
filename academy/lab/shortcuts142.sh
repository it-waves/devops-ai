# shortcuts142.sh : source this file to get the short names  lab  and  t
lab() { sudo /usr/local/sbin/lab142.sh "$@"; }
t() { ( cd /opt/lab142 && python3 load.py "$@" ); }
