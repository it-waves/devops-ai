#!/bin/sh
# lab36.sh : Linux administration mastery lab. Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status
# Mission: four checks must say PASS. Four things are broken on purpose.
D=/opt/lab36; DATA=/srv/lab36/data; IMG=/var/lib/lab36/data.img; PORT=8080
U=${SUDO_USER:-root}
rule() { iptables $1 INPUT $2 -p tcp --dport $PORT -j REJECT --reject-with tcp-reset; }
down() {
  [ -f $D/web.pid ] && kill $(cat $D/web.pid) 2>/dev/null
  pkill -f "http.server $PORT --bind 127.0.0.1" 2>/dev/null
  while rule -C 2>/dev/null; do rule -D; done
  mountpoint -q $DATA && umount $DATA
  rm -rf $D /srv/lab36 /var/lib/lab36; true
}
up() {
  down
  mkdir -p $D/bin $D/www $DATA /var/lib/lab36
  # fault 1: a script with no execute bit
  printf '#!/bin/sh\necho report generated\n' > $D/bin/report.sh; chmod 644 $D/bin/report.sh; chown $U $D/bin/report.sh
  # fault 2: a data disk with no space left
  truncate -s 60M $IMG; mkfs.ext4 -q -m 0 $IMG; mount -o loop $IMG $DATA; chown $U $DATA
  dd if=/dev/zero of=$DATA/old-dump.log bs=4k 2>/dev/null; chown $U $DATA/old-dump.log
  # fault 3: a service file with a typo in the program path
  printf '[Unit]\nDescription=Lab 36 shop web server\n\n[Service]\nExecStart=/usr/bin/pythn3 -m http.server %s --bind 127.0.0.1 --directory %s/www\nRestart=on-failure\n' $PORT $D > $D/lab36-web.service; chown $U $D/lab36-web.service
  # fault 4: the web server is running, but a firewall rule rejects its port
  echo "lab36 shop ok" > $D/www/index.html
  nohup python3 -m http.server $PORT --bind 127.0.0.1 --directory $D/www >/dev/null 2>&1 &
  echo $! > $D/web.pid; sleep 1
  rule -I 1
  echo "lab is up. Four things are wrong. Goal: four PASS lines."
}
chk() { if eval "$2" >/dev/null 2>&1; then echo "PASS  $1"; else echo "FAIL  $1"; fi; }
check() {
  chk "1 report script runs" "$D/bin/report.sh"
  chk "2 data disk accepts a write" "echo ok > $DATA/check.txt && rm -f $DATA/check.txt"
  chk "3 service file verifies clean" "! systemd-analyze verify $D/lab36-web.service 2>&1 | grep -q lab36-web"
  chk "4 shop page answers on port $PORT" "curl -s -m 2 http://127.0.0.1:$PORT | grep -q shop"
}
case "$1" in up) up;; down) down; echo "lab removed.";; check) check;; status) check;; *) echo "usage: sudo lab36.sh up | check | down";; esac
