# shortcuts119.sh : source this file to get the short names  lab  and  ng
lab() { sudo /usr/local/sbin/lab119.sh "$@"; }
ng() { nginx -p /opt/lab119 -e /opt/lab119/logs/error.log -c /opt/lab119/nginx.conf "$@"; }
