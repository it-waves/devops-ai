# shortcuts124.sh : source this file to get the short names  lab  and  ng
lab() { sudo /usr/local/sbin/lab124.sh "$@"; }
ng() { nginx -p /opt/lab124 -e /opt/lab124/logs/error.log -c /opt/lab124/nginx.conf "$@"; }
