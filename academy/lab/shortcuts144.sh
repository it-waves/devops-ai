# shortcuts144.sh : source this file to get the short names  lab  and  t
lab() { sudo /usr/local/sbin/lab144.sh "$@"; }
t() { ( cd /opt/lab144 && python3 -m pytest "$@" ); }
