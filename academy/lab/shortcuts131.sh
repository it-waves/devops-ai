# shortcuts131.sh : source this file to get the short names  lab  and  ui
lab() { sudo /usr/local/sbin/lab131.sh "$@"; }
ui() { echo "open http://localhost:8085   server 127.0.0.1:5511   user shopadmin   password Shop-UI-131   database shop"; }
