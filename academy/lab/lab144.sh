#!/bin/sh
# lab144.sh : Software Testing and QA MASTERY: ship a feature safely. Run with sudo.
#   up | check | down | status     Needs: python3, pytest, pytest-cov (sudo apt install -y python3-pytest python3-pytest-cov)
D=${LAB144_DIR:-/opt/lab144}
OWNER=${SUDO_USER:-root}
down() { rm -rf "${D:?}" /tmp/l144c 2>/dev/null; true; }
up() {
  python3 -c "import pytest, pytest_cov" >/dev/null 2>&1 || { echo "need: sudo apt install -y python3-pytest python3-pytest-cov"; exit 1; }
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  down; mkdir -p $D/tests $D/demo
  cat > $D/shop.py <<'EOF_P'
"""CloudCart pricing. Money is in cents."""
from datetime import datetime

COUPONS = {"SAVE10": 10, "SAVE20": 20}

def cart_total(items):
    """items: a list of (price_cents, quantity)."""
    return sum(price for price, qty in items)

def apply_coupon(total, code):
    pct = COUPONS.get(code)
    if pct is None:
        raise ValueError("unknown coupon")
    return total - total * pct // 100

def free_shipping(total):
    return total >= 5000

def is_weekend_sale(now=None):
    now = now or datetime.now()
    return now.weekday() >= 5

def checkout(items, code=None, now=None):
    total = cart_total(items)
    if code:
        total = apply_coupon(total, code)
    if is_weekend_sale(now):
        total = total - total * 5 // 100
    shipping = 0 if free_shipping(total) else 499
    return {"total": total, "shipping": shipping}
EOF_P
  printf '[pytest]\npythonpath = .\n' > $D/pytest.ini
  cat > $D/tests/test_shop.py <<'EOF_P'
from shop import cart_total, apply_coupon, is_weekend_sale

def test_total_of_two_lines():
    assert cart_total([(1000, 2), (500, 1)]) == 2500

def test_coupon_ten_percent():
    assert apply_coupon(1000, "SAVE10") == 900

def test_not_weekend_today():
    assert not is_weekend_sale()
EOF_P
  cat > $D/demo/tiny.py <<'EOF_P'
def add_tax(cents):
    return cents + cents * 20 // 100

def label(cents):
    return "free" if cents == 0 else "paid"
EOF_P
  cat > $D/demo/test_tiny.py <<'EOF_P'
from tiny import add_tax

def test_add_tax():
    assert add_tax(1000) == 1200
EOF_P
  cat > $D/TASKS.txt <<'EOF_P'
LAB 144 (MASTERY): ship the checkout feature safely. Work in /opt/lab144.
The app code is shop.py. The tests are tests/test_shop.py. Do the missions in order.

 1. FIND THE BUG. Run the tests. One fails for a real reason. The test is right and
    the code is wrong: fix it in shop.py. Do not touch the other functions.
 2. FIX THE FLAKY TEST. One test passes on weekdays and fails on weekends. Pass a fixed
    date (datetime(2025, 1, 4) is a Saturday). No real clock, random or sleep in tests.
 3. COVER THE CODE. Add tests until line coverage of shop.py is 90% or more.
    Test the edges: 5000 cents is free shipping, 4999 is not; Saturday is a sale day,
    Friday is not; an unknown coupon raises ValueError (pytest.raises).
 4. WRITE THE GATE. Create ci.sh in this folder. It must run the tests with a coverage
    gate (--cov=shop --cov-fail-under=90), fail (non-zero) if any test fails or if
    coverage is under 90, and also fail if any .py file contains password=
 5. WRITE THE REPORT. Create report.txt with four lines (one value per line):
       bug=<function that had the bug>
       flaky=<cause of the flaky test: clock>
       coverage=<your coverage, whole percent>
       tests=<how many tests you have>
Then: lab check, until 6 of 6. Then lab down.
EOF_P
  chown -R $OWNER $D 2>/dev/null
  echo "lab144 ready in $D  (read TASKS.txt)"
}
P=0; T=0
ok() { T=$((T+1)); if [ "$2" = 0 ]; then P=$((P+1)); echo "  PASS  $1"; else echo "  FAIL  $1"; fi; }
run() { python3 -m pytest -q -p no:cacheprovider "$@" >/dev/null 2>&1; }
check() {
  [ -d $D ] || { echo "run: lab up"; exit 1; }
  cd $D
  python3 - <<'EOF_C' >/dev/null 2>&1
import sys; sys.path.insert(0, ".")
from shop import cart_total, checkout
from datetime import datetime
assert cart_total([(1000, 2), (500, 1)]) == 2500
assert checkout([(2500, 2)], now=datetime(2025, 1, 6)) == {"total": 5000, "shipping": 0}
assert checkout([(1000, 3)], "SAVE10", datetime(2025, 1, 6)) == {"total": 2700, "shipping": 499}
EOF_C
  ok "the bug is fixed: totals count the quantity" $?
  n=0; bad=0; while [ $n -lt 10 ]; do run tests || bad=1; n=$((n+1)); done
  TZ=Pacific/Kiritimati run tests || bad=1; TZ=America/Los_Angeles run tests || bad=1
  ! grep -qE 'datetime\.now|random|sleep|mark\.(skip|xfail)|pytest\.(skip|xfail)' tests/*.py || bad=1
  [ $bad = 0 ]; ok "the suite is reliable: 12 runs, 3 zones, no clock/random" $?
  cov=$(python3 -m pytest -q -p no:cacheprovider --cov=shop --cov-report=term tests 2>/dev/null | awk '$1=="shop.py"{gsub("%","",$NF); print $NF}')
  [ -n "$cov" ] && [ "$cov" -ge 90 ] 2>/dev/null; ok "coverage of shop.py is 90% or more" $?
  rm -rf /tmp/l144c; mkdir -p /tmp/l144c/a /tmp/l144c/b /tmp/l144c/c
  for m in a b c; do cp -r shop.py pytest.ini tests /tmp/l144c/$m/; done
  printf '\ndef cart_total(items):\n    return sum(p for p, q in items)\n' >> /tmp/l144c/a/shop.py
  printf '\ndef free_shipping(total):\n    return total > 5000\n' >> /tmp/l144c/b/shop.py
  printf '\ndef is_weekend_sale(now=None):\n    now = now or datetime.now()\n    return now.weekday() > 5\n' >> /tmp/l144c/c/shop.py
  ( cd /tmp/l144c/a && run tests ); x=$?; ( cd /tmp/l144c/b && run tests ); y=$?; ( cd /tmp/l144c/c && run tests ); z=$?
  run tests; w=$?
  [ $w = 0 ] && [ $x != 0 ] && [ $y != 0 ] && [ $z != 0 ]; ok "the tests catch 3 planted bugs (quantity, two edges)" $?
  g=1
  if [ -f ci.sh ]; then
    sh ci.sh >/dev/null 2>&1; c0=$?
    cp ci.sh /tmp/l144c/a/; ( cd /tmp/l144c/a && sh ci.sh >/dev/null 2>&1 ); c1=$?
    cp ci.sh /tmp/l144c/b/; rm -f /tmp/l144c/b/tests/*.py; printf 'def test_one():\n    assert True\n' > /tmp/l144c/b/tests/test_one.py
    ( cd /tmp/l144c/b && sh ci.sh >/dev/null 2>&1 ); c2=$?
    cp ci.sh /tmp/l144c/c/; printf 'password="x"\n' > /tmp/l144c/c/leak.py
    ( cd /tmp/l144c/c && sh ci.sh >/dev/null 2>&1 ); c3=$?
    [ $c0 = 0 ] && [ $c1 != 0 ] && [ $c2 != 0 ] && [ $c3 != 0 ] && g=0
  fi
  ok "ci.sh: passes clean, fails on bug, low coverage, secret" $g
  rm -rf /tmp/l144c
  r=1
  if [ -f report.txt ]; then
    b=$(sed -n 's/^bug=//p' report.txt | head -1); f=$(sed -n 's/^flaky=//p' report.txt | head -1)
    c=$(sed -n 's/^coverage=//p' report.txt | head -1 | tr -d '% '); t=$(sed -n 's/^tests=//p' report.txt | head -1 | tr -d ' ')
    nt=$(python3 -m pytest --collect-only -q -p no:cacheprovider tests 2>/dev/null | grep -c '::')
    d=$(( ${c:-0} - ${cov:-0} )); [ $d -lt 0 ] && d=$((0-d))
    [ "$b" = cart_total ] && echo "$f" | grep -qiE 'clock|time|date|weekend' && [ "$d" -le 2 ] && [ "$t" = "$nt" ] && r=0
  fi
  ok "report.txt is true: bug, flaky, coverage, tests" $r
  echo; echo "$P / $T passed"; [ $P = $T ]
}
status() { [ -d $D ] && echo "lab144 up in $D" || echo "lab144 down"; }
case "$1" in up) up;; check) check;; down) down; echo "lab144 removed";; status) status;; *) echo "usage: lab up|check|down|status";; esac
