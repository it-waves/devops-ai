# shortcuts131.sh : source this file to get the short names  lab  and  ui
lab() { sudo /usr/local/sbin/lab131.sh "$@"; }
ui() { printf '%s\n' 'open    http://localhost:8085' 'system  PostgreSQL' 'server  127.0.0.1:5511' 'user    shopadmin' 'pass    Shop-UI-131' 'db      shop'; }
