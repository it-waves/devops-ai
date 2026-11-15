lab() { sudo /usr/local/sbin/lab109.sh "$@"; }
ng() { nginx -p /opt/lab109/nginx -c nginx.conf -e /opt/lab109/nginx/logs/error.log "$@"; }
