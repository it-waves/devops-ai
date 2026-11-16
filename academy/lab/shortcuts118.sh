# shortcuts118.sh : source this file to get the short names  lab  and  ng
lab() { sudo /usr/local/sbin/lab118.sh "$@"; }
ng() { nginx -p /opt/lab118 -e /opt/lab118/logs/error.log -c /opt/lab118/nginx.conf "$@"; }
