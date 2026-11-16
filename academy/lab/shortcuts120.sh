# shortcuts120.sh : source this file to get the short names  lab  and  ng
lab() { sudo /usr/local/sbin/lab120.sh "$@"; }
ng() { nginx -p /opt/lab120 -e /opt/lab120/logs/error.log -c /opt/lab120/nginx.conf "$@"; }
