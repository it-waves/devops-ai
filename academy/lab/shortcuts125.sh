# shortcuts125.sh : source this file to get the short names  lab  and  ng
lab() { sudo /usr/local/sbin/lab125.sh "$@"; }
ng() { nginx -p /opt/lab125 -e /opt/lab125/logs/error.log -c /opt/lab125/nginx.conf "$@"; }
