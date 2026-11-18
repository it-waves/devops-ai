#!/bin/sh
# lab143.sh : Software Testing and QA, lesson 9: flaky and environment-dependent tests. Run with sudo.
#   up | check | down | status     Needs: python3, pytest (sudo apt install -y python3-pytest)
D=${LAB143_DIR:-/opt/lab143}
OWNER=${SUDO_USER:-root}
down() { rm -rf "${D:?}" /tmp/l143c 2>/dev/null; true; }
up() {
  python3 -c "import pytest" >/dev/null 2>&1 || { echo "need: sudo apt install -y python3-pytest"; exit 1; }
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  down; mkdir -p $D/tests $D/demo
  cat > $D/cartsched.py <<'EOF_P'
"""CloudCart scheduling helpers."""
import json, os
from datetime import datetime

def is_business_hours(now=None):
    now = now or datetime.now()
    return now.weekday() < 5 and 9 <= now.hour < 17

def fetch_with_retry(call, attempts=3):
    last = None
    for _ in range(attempts):
        try:
            return call()
        except ConnectionError as err:
            last = err
    raise last

def load_config(base_dir="."):
    with open(os.path.join(base_dir, "config.json")) as f:
        return json.load(f)
EOF_P
  echo '{"region": "eu", "retries": 3}' > $D/config.json
  printf '[pytest]\npythonpath = .\n' > $D/pytest.ini
  cat > $D/tests/test_cartsched.py <<'EOF_P'
import random
from cartsched import is_business_hours, fetch_with_retry, load_config

STATE = []

def test_open_now():
    assert is_business_hours()

def test_retry_succeeds():
    def call():
        if random.random() < 0.5:
            raise ConnectionError("blip")
        return "ok"
    assert fetch_with_retry(call, attempts=2) == "ok"

def test_config_loads():
    assert load_config()["region"] == "eu"

def test_a_adds():
    STATE.append(1)
    assert STATE == [1]

def test_b_uses_state():
    assert STATE == [1]
EOF_P
  cat > $D/demo/conftest.py <<'EOF_P'
import os, random
random.seed(int(os.environ.get("SEED", "0")))
EOF_P
  cat > $D/demo/test_retry.py <<'EOF_P'
import random
from cartsched import fetch_with_retry

def test_retry_succeeds():
    def call():
        if random.random() < 0.5:
            raise ConnectionError("blip")
        return "ok"
    assert fetch_with_retry(call, attempts=2) == "ok"
EOF_P
  cat > $D/demo/loop.sh <<'EOF_P'
for s in 1 2 3 4 5 6 7 8; do
  printf 'seed %s: ' $s
  SEED=$s python3 -m pytest -q --tb=no demo | tail -1 | cut -d' ' -f1-2
done
EOF_P
  cat > $D/TASKS.txt <<'EOF_P'
LAB 143: make tests/test_cartsched.py reliable. Work in /opt/lab143.
Do NOT change cartsched.py. Fix the tests, in tests/test_cartsched.py.
The tests must be correct, not just green: they must still catch real bugs.

Rules:
 - No real clock, no randomness, no sleeping in the tests (no datetime.now,
   random, time.sleep). Pass a fixed time. Use a fake call that fails on purpose.
 - Every test passes on its own, in any order. No shared state between tests.
 - They pass from any folder, and in any time zone. Use tmp_path for files.
 - No skip, xfail or rerun markers. Keep at least 5 tests.
 - They must prove the behaviour: edges (9:00 open, 17:00 closed, weekend closed),
   a retry that succeeds on the 2nd try, and a retry that gives up.
Then: lab check, until 6 of 6.
EOF_P
  chown -R $OWNER $D 2>/dev/null
  echo "lab143 ready in $D  (read TASKS.txt)"
}
P=0; T=0
ok() { T=$((T+1)); if [ "$2" = 0 ]; then P=$((P+1)); echo "  PASS  $1"; else echo "  FAIL  $1"; fi; }
run() { python3 -m pytest -q -p no:cacheprovider "$@" >/dev/null 2>&1; }
check() {
  [ -d $D ] || { echo "run: lab up"; exit 1; }
  cd $D
  n=0; bad=0; while [ $n -lt 20 ]; do run tests || bad=1; n=$((n+1)); done
  [ $bad = 0 ]; ok "the suite passes 20 runs in a row" $?
  TZ=UTC run tests; a=$?; TZ=Pacific/Kiritimati run tests; b=$?; TZ=America/Los_Angeles run tests; c=$?
  [ $a = 0 ] && [ $b = 0 ] && [ $c = 0 ]; ok "it passes in three time zones" $?
  ( cd / && run $D/tests ); [ $? = 0 ]; ok "it passes from another folder" $?
  ids=$(python3 -m pytest --collect-only -q -p no:cacheprovider tests 2>/dev/null | grep '::'); bad=0; cnt=0
  for i in $ids; do cnt=$((cnt+1)); run "$i" || bad=1; done
  [ $bad = 0 ] && [ $cnt -ge 5 ]; ok "every test passes on its own (5 or more tests)" $?
  ! grep -qE 'datetime\.now|random|sleep|mark\.(skip|xfail|flaky)|reruns|pytest\.skip|pytest\.xfail' tests/*.py; ok "no clock, random, sleep or skip/xfail in the tests" $?
  rm -rf /tmp/l143c; mkdir -p /tmp/l143c/a /tmp/l143c/b
  cp -r cartsched.py pytest.ini config.json tests /tmp/l143c/a/; cp -r cartsched.py pytest.ini config.json tests /tmp/l143c/b/
  sed -i 's/9 <= now.hour < 17/9 <= now.hour < 18/' /tmp/l143c/a/cartsched.py
  sed -i 's/for _ in range(attempts):/for _ in range(attempts - 1):/' /tmp/l143c/b/cartsched.py
  ( cd /tmp/l143c/a && run tests ); x=$?; ( cd /tmp/l143c/b && run tests ); y=$?
  run tests; z=$?; rm -rf /tmp/l143c
  [ $z = 0 ] && [ $x != 0 ] && [ $y != 0 ]; ok "the tests catch 2 planted bugs (hours edge, retry count)" $?
  echo; echo "$P / $T passed"; [ $P = $T ]
}
status() { [ -d $D ] && echo "lab143 up in $D" || echo "lab143 down"; }
case "$1" in up) up;; check) check;; down) down; echo "lab143 removed";; status) status;; *) echo "usage: lab up|check|down|status";; esac
