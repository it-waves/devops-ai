# shortcuts139.sh : source this file to get the short names  lab  and  t , and  B  (the shop's address)
lab() { sudo /usr/local/sbin/lab139.sh "$@"; }
t() { ( cd /opt/lab139 && python3 -m pytest "$@" ); }
export B=localhost:8139/cloudcart
