# shortcuts121.sh : source this file to get the short names  lab  and  ng
lab() { sudo /usr/local/sbin/lab121.sh "$@"; }
ng() { nginx -p /opt/lab121 -e /opt/lab121/logs/error.log -c /opt/lab121/nginx.conf "$@"; }
