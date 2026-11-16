# shortcuts123.sh : source this file to get the short names  lab  and  ng
lab() { sudo /usr/local/sbin/lab123.sh "$@"; }
ng() { nginx -p /opt/lab123 -e /opt/lab123/logs/error.log -c /opt/lab123/nginx.conf "$@"; }
