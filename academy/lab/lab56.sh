#!/bin/sh
# lab56.sh : Python for DevOps mastery lab. Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status
# Mission: four checks must say PASS. Four Python scripts are broken on purpose. Needs python3 only.
D=/opt/lab56
U=${SUDO_USER:-root}
down() { rm -rf $D; true; }
up() {
  down
  mkdir -p $D/bin $D/conf
  echo '{"host": "web01"}' > $D/conf/app.json
  # fault 1: ports are sorted as text, so 443 comes before 80
  cat > $D/bin/top.py <<'EOF'
import sys
# print the ports in order, smallest first
print(*sorted(sys.argv[1:]))
EOF
  # fault 2: a missing key ends in a traceback and exit 1, not a clear message and exit 2
  cat > $D/bin/load_cfg.py <<'EOF'
import json, sys
# read the port from the config file
cfg = json.load(open(sys.argv[1]))
print("port", cfg["port"])
EOF
  # fault 3: the retry loop hides the failure, so the script exits 0 even when it gave up
  cat > $D/bin/fetch.py <<'EOF'
import os, sys
# try three times to find the flag file, then report
for attempt in range(3):
    try:
        open(sys.argv[1]).close()
        print("fetched")
        break
    except Exception:
        pass
else:
    print("gave up")
EOF
  # fault 4: a mutable default argument keeps its list between calls
  cat > $D/bin/tags.py <<'EOF'
def add(item, bucket=[]):
    bucket.append(item)
    return bucket

print(add("a"))
print(add("b"))
EOF
  chmod 755 $D/bin/*.py; chown -R $U $D 2>/dev/null
  echo "lab is up. Four scripts are wrong. Goal: four PASS lines."
}
chk() { if eval "$2" >/dev/null 2>&1; then echo "PASS  $1"; else echo "FAIL  $1"; fi; }
check() {
  chk "1 top.py sorts ports as numbers" "test \"\$(python3 $D/bin/top.py 80 443 8080)\" = '80 443 8080'"
  chk "2 load_cfg.py: clear error, exit 2" "python3 $D/bin/load_cfg.py $D/conf/app.json 2>$D/err.txt; test \$? = 2 && ! grep -q Traceback $D/err.txt"
  chk "3 fetch.py exits 1 when it gives up" "touch $D/conf/up.flag; python3 $D/bin/fetch.py $D/conf/up.flag && rm $D/conf/up.flag && ! python3 $D/bin/fetch.py $D/conf/up.flag"
  chk "4 tags.py: each call gets a fresh list" "test \"\$(python3 $D/bin/tags.py | tail -1)\" = \"['b']\""
}
case "$1" in up) up;; down) down; echo "lab removed.";; check) check;; status) check;; *) echo "usage: sudo lab56.sh up | check | down";; esac
