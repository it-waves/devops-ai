#!/bin/sh
# lab122.sh : Web servers and reverse proxies, lesson 5: read nginx access and error logs and understand status codes. Run with sudo, on any Linux machine with nginx and curl.
#   up | check | down | status | traffic
# Needs: sudo apt install -y nginx curl iproute2     port 8221 free. (The lab runs its own private nginx from /opt/lab122; it does not touch the system nginx.)
# Mission: nginx is serving a small site. Send it traffic, read the logs like an operator, and answer three questions from the evidence.
D=${LAB122_DIR:-/opt/lab122}
OWNER=${SUDO_USER:-root}
if [ "$OWNER" = root ]; then RU=""; else RU="runuser -u $OWNER --"; fi
NG="nginx -p $D -e $D/logs/error.log -c $D/nginx.conf"
down() {
  [ -f $D/nginx.pid ] && kill "$(cat $D/nginx.pid)" 2>/dev/null; sleep 1
  rm -rf "${D:?}"/* "${D:?}"/.[!.]* 2>/dev/null; rmdir "$D" 2>/dev/null; true
}
up() {
  for t in nginx curl; do command -v $t >/dev/null 2>&1 || { echo "$t not found: run  sudo apt install -y nginx curl iproute2"; exit 1; }; done
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  [ -f /etc/nginx/mime.types ] || { echo "/etc/nginx/mime.types not found: run  sudo apt install -y nginx"; exit 1; }
  if curl -s -o /dev/null -m 2 localhost:8221; then echo "port 8221 is already in use: stop what uses it first"; exit 1; fi
  down; mkdir -p $D/site $D/logs $D/tmp
  cp /etc/nginx/mime.types $D/mime.types
  cat > $D/site/index.html <<'EOF_H'
<!doctype html>
<html><head><meta charset="utf-8"><title>CloudCart</title></head>
<body><h1>Welcome to CloudCart</h1></body></html>
EOF_H
  echo "<h1>Products</h1>" > $D/site/products.html
  N404=$(( $(od -An -N1 -tu1 /dev/urandom | tr -d ' ') % 5 + 3 ))
  { echo "#!/bin/sh"; echo "# sends a fixed mix of requests to nginx on port 8221"
    echo 'u=localhost:8221'
    echo 'for i in 1 2 3 4 5; do curl -s -o /dev/null $u/; done'
    echo 'curl -s -o /dev/null $u/products.html'
    i=0; while [ $i -lt $N404 ]; do echo "curl -s -o /dev/null \$u/missing$i.html"; i=$((i+1)); done
    echo 'curl -s -o /dev/null $u/admin/'
    echo 'curl -s -o /dev/null $u/old'
    echo 'curl -s -o /dev/null $u/broken'
    echo 'curl -s -o /dev/null $u/broken'
    echo 'echo "traffic sent"'; } > $D/traffic.sh; chmod +x $D/traffic.sh
  cat > $D/nginx.conf <<EOF_C
worker_processes 1;
pid $D/nginx.pid;
events { worker_connections 64; }
http {
    include mime.types;
    server_tokens off;
    log_format main '\$remote_addr "\$request" \$status \$body_bytes_sent "\$http_user_agent"';
    access_log $D/logs/access.log main;
    client_body_temp_path $D/tmp/body;
    proxy_temp_path $D/tmp/proxy;
    fastcgi_temp_path $D/tmp/fcgi;
    uwsgi_temp_path $D/tmp/uwsgi;
    scgi_temp_path $D/tmp/scgi;
    server {
        listen 8221;
        root $D/site;
        location /admin/ { return 403; }
        location = /old { return 301 /products.html; }
        location /broken { proxy_pass http://127.0.0.1:8229; }
    }
}
EOF_C
  cat > $D/TASKS.txt <<'EOF_T'
LAB 122  Access logs, error logs and status codes
Open a terminal in /opt/lab122. The short name  ng  runs nginx with this lab's own config (/opt/lab122/nginx.conf).  Load it with: source shortcuts122.sh
nginx is already running on port 8221. Its logs are in /opt/lab122/logs/ : access.log (one line per request) and error.log (what went wrong).

1  Send the traffic:   ./traffic.sh      (a fixed mix of requests: it never changes while the lab is up)
2  Read the access log:   cat logs/access.log      Find the status code in each line (the number after the quoted request). The format is:  client "request" status bytes "user agent"
3  Count requests per status code:   awk '{print $5}' logs/access.log | sort | uniq -c
4  Make the log more useful. In nginx.conf, in the http block, above the  server {  line, add a named format that also records how long each request took:
     log_format timed '$request $status rt=$request_time';
   and change the access_log line (it ends with  main;  now) so that it ends with  timed;   like this:   access_log /opt/lab122/logs/access.log timed;
   Test and apply:   ng -t && ng -s reload
5  Empty the log and send the traffic again, so every line uses the new format:   : > logs/access.log ; ./traffic.sh
6  Read the log again. Each line now ends with rt= and a number.
7  Read the error log:   cat logs/error.log      Find the message about the failed request. A shorter view:   grep -o 'connect() failed ([^)]*)' logs/error.log
8  Write three answers into the file  answers.txt , one per line (no extra words):
     line 1: how many requests got 404 Not Found
     line 2: the path that produced the 502 Bad Gateway responses (for example /something)
     line 3: the one-word reason nginx gives in error.log for the 502 (the word after the number in brackets)
9  lab check   (judges you: you need all 5 PASS)
10 lab down    (stops nginx and removes everything)
If something fails, read the nginx error: it names the file and the line.
EOF_T
  chown -R $OWNER $D 2>/dev/null; chmod -R a+rX $D
  $RU $NG; sleep 0.5
  echo "lab 122 ready in $D. Read TASKS.txt, then run: ./traffic.sh"
}
pass=0; total=5
ok() { pass=$((pass+1)); echo "  PASS  $1"; }
no() { echo "  FAIL  $1"; }
check() {
  [ -d $D ] || { echo "lab is not up: run  lab up"; exit 1; }
  A=$D/logs/access.log
  conf=$($RU $NG -T 2>/dev/null); pid=$(cat $D/nginx.pid 2>/dev/null)
  fmt=$(echo "$conf" | sed -n 's/^ *log_format  *\([a-z_]*\) .*\$request_time.*/\1/p' | head -n 1)
  if $RU $NG -t >/dev/null 2>&1 && [ -n "$pid" ] && kill -0 "$pid" 2>/dev/null && [ -n "$fmt" ] && echo "$conf" | grep -Eq "^ *access_log +[^ ]+ +$fmt;"; then ok "1 nginx runs and access_log uses a format that records \$request_time"; else no "1 add a log_format with rt=\$request_time and end the access_log line with its name (TASKS.txt step 4)"; fi
  n404=$(grep -c ' 404 ' $A 2>/dev/null); n502=$(grep -c ' 502 ' $A 2>/dev/null)
  if [ "$n404" -ge 3 ] && [ "$n502" -ge 2 ] && grep -q ' 301 ' $A && grep -q ' 403 ' $A && grep -Eq 'rt=[0-9]+\.[0-9]+$' $A && ! grep -Evq 'rt=[0-9]+\.[0-9]+$' $A; then ok "2 the access log holds the traffic, every line in the new format"; else no "2 empty the log, run ./traffic.sh again after the format change (steps 4 and 5)"; fi
  a1=$(sed -n 1p $D/answers.txt 2>/dev/null | tr -d ' \r'); a2=$(sed -n 2p $D/answers.txt 2>/dev/null | tr -d ' \r'); a3=$(sed -n 3p $D/answers.txt 2>/dev/null | tr -d ' \r' | tr A-Z a-z)
  if [ -n "$a1" ] && [ "$a1" = "$n404" ]; then ok "3 line 1 of answers.txt: the number of 404 responses is right"; else no "3 line 1 of answers.txt must be the number of 404 responses (count them in the log), got '$a1'"; fi
  if [ "$a2" = "/broken" ]; then ok "4 line 2 of answers.txt: the path behind the 502 is right"; else no "4 line 2 of answers.txt must be the path that gave 502 Bad Gateway, got '$a2'"; fi
  if [ "$a3" = "refused" ] && grep -q 'Connection refused' $D/logs/error.log 2>/dev/null; then ok "5 line 3 of answers.txt: the reason in error.log is right"; else no "5 line 3 of answers.txt must be the one-word reason in error.log after (111: , got '$a3'"; fi
  echo; echo "$pass / $total passed"; [ $pass -eq $total ]
}
status() { [ -d $D ] && echo "lab 122 is up in $D" || echo "lab 122 is not up"; }
case "$1" in up) up ;; check) check ;; down) down; echo "lab 122 removed" ;; status) status ;; traffic) sh $D/traffic.sh ;; *) echo "usage: lab122.sh up|check|down|status" ;; esac
