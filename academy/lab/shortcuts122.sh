# shortcuts122.sh : source this file to get the short names  lab  and  ng
lab() { sudo /usr/local/sbin/lab122.sh "$@"; }
ng() { nginx -p /opt/lab122 -e /opt/lab122/logs/error.log -c /opt/lab122/nginx.conf "$@"; }
