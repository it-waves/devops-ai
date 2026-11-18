#!/bin/sh
# lab140.sh : Software Testing and QA, lesson 6: test coverage and its limits. Run with sudo.
#   up | check | down | status     Needs: python3, pytest, pytest-cov (sudo apt install -y python3-pytest python3-pytest-cov)
D=${LAB140_DIR:-/opt/lab140}
OWNER=${SUDO_USER:-root}
AS=""; [ "$OWNER" != root ] && AS="runuser -u $OWNER --"
down() { rm -rf "${D:?}" 2>/dev/null; true; }
up() {
  command -v python3 >/dev/null 2>&1 && python3 -m pytest --version >/dev/null 2>&1 && python3 -c "import pytest_cov" >/dev/null 2>&1 || { echo "pytest or pytest-cov not found: run  sudo apt install -y python3-pytest python3-pytest-cov"; exit 1; }
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  down; mkdir -p $D/tests $D/demo $D/out
  cat > $D/cart.py <<'EOF_P'
"""CloudCart pricing rules, in cents."""

def shipping_cents(subtotal):
    if subtotal <= 0:
        return 0
    if subtotal >= 7500:
        return 0
    return 599

def discount_cents(subtotal, code):
    if code is None:
        return 0
    if code == "WELCOME10":
        return subtotal // 10
    if code == "BULK":
        if subtotal >= 20000:
            return subtotal // 5
        return 0
    raise ValueError("unknown code")

def tax_cents(amount):
    return round(amount * 8 / 100)

def total_cents(subtotal, code=None):
    net = subtotal - discount_cents(subtotal, code)
    return net + shipping_cents(net) + tax_cents(net)
EOF_P
  cat > $D/loyalty.py <<'EOF_P'
"""CloudCart loyalty points (used in the video demo)."""

def tier(points):
    if points >= 1000:
        return "gold"
    if points >= 500:
        return "silver"
    return "bronze"

def points_for(cents, tier_name):
    base = cents // 100
    if tier_name == "gold":
        return base * 2
    if tier_name == "silver":
        return base + base // 2
    return base
EOF_P
  cat > $D/tests/test_cart.py <<'EOF_P'
from cart import total_cents, shipping_cents

def test_free_shipping_on_big_orders():
    assert shipping_cents(8000) == 0

def test_total_without_a_code():
    assert total_cents(10000) == 10800
EOF_P
  cat > $D/.coveragerc <<'EOF_P'
[run]
branch = True
omit =
    tests/*
    demo/*
EOF_P
  cat > $D/pytest.ini <<'EOF_P'
[pytest]
pythonpath = .
EOF_P
  cat > $D/TASKS.txt <<'EOF_T'
LAB 140  Coverage: use it, and know its limits
Folder /opt/lab140. cart.py has the CloudCart pricing rules. Do not change cart.py or .coveragerc.
Your tests go in tests/test_cart.py (two tests are there). Run  lab check  after each step.

1  Measure where you start, and save the report:
     pytest --cov=cart --cov-report=term-missing -q | tee out/before.txt
2  Make the HTML report, and open out/htmlcov/index.html in a browser (red lines are not run):
     pytest --cov=cart --cov-report=html:out/htmlcov -q
3  Add tests until cart.py has 90 percent or more (branches count). Read the Missing column.
4  Have at least 6 tests, and every test must assert something.
5  Coverage only says a line ran. So check these four bugs would be caught. lab check changes
   cart.py four ways (a boundary, a divisor, another boundary, a price) and runs YOUR tests:
   at least 3 of the 4 must fail. Test the exact edges: 7500 and 7499, 20000.
6  Save the final report:
     pytest --cov=cart --cov-report=term-missing -q | tee out/after.txt
   lab check   (all 6 PASS to finish)      lab down   (removes everything)
EOF_T
  ( cd $D && sha256sum cart.py .coveragerc > .sha )
  chown -R $OWNER $D 2>/dev/null; chmod -R a+rX $D
  echo "lab 140 ready in $D. Read TASKS.txt"
}
pass=0; total=6
ok() { pass=$((pass+1)); echo "  PASS  $1"; }
no() { echo "  FAIL  $1"; }
pct() { grep -E "^cart.py" "$1" 2>/dev/null | grep -oE "[0-9]+%" | tail -1 | tr -d %; }
check() {
  [ -d $D ] || { echo "lab is not up: run  lab up"; exit 1; }
  O=$D/out; b=$(pct $O/before.txt)
  if [ -n "$b" ] && [ "$b" -lt 80 ]; then ok "1 before.txt: start was $b%"; else no "1 before.txt: save the start report"; fi
  if ls $O/htmlcov/*cart_py.html >/dev/null 2>&1 && [ -f $O/htmlcov/index.html ]; then ok "2 HTML report made"; else no "2 out/htmlcov: make the HTML report"; fi
  s=bad; ( cd $D && sha256sum -c .sha >/dev/null 2>&1 && $AS python3 -m pytest -q -p no:cacheprovider --cov=cart --cov-fail-under=90 tests >/dev/null 2>&1 ) && s=ok
  if [ $s = ok ]; then ok "3 cart.py 90% or more, files untouched"; else no "3 cart.py is under 90%, or a file changed"; fi
  r=$( cd $D && $AS python3 - <<'EOF_Y'
import ast, subprocess, sys
try:
    t = ast.parse(open("tests/test_cart.py").read())
    fs = [n for n in ast.walk(t) if isinstance(n, ast.FunctionDef) and n.name.startswith("test_")]
    good = all(any(isinstance(x, ast.Assert) or (isinstance(x, ast.With)) for x in ast.walk(f)) for f in fs)
    p = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "tests"], capture_output=True).returncode
    print("ok" if len(fs) >= 6 and good and p == 0 else "bad")
except Exception:
    print("bad")
EOF_Y
)
  if [ "$r" = ok ]; then ok "4 six or more tests, all assert, all pass"; else no "4 need 6 passing tests that assert"; fi
  k=0; T=$(mktemp -d); chmod 755 $T
  for m in 's/subtotal >= 7500/subtotal > 7500/' 's#subtotal // 10#subtotal // 100#' 's/subtotal >= 20000/subtotal > 20000/' 's/return 599/return 499/'; do
    rm -rf $T/w; mkdir $T/w; cp -r $D/tests $D/cart.py $D/pytest.ini $T/w/; sed -i "$m" $T/w/cart.py; chmod -R a+rX $T
    if ! ( cd $T/w && $AS python3 -m pytest -q -p no:cacheprovider tests >/dev/null 2>&1 ); then k=$((k+1)); fi
  done; rm -rf $T
  if [ $k -ge 3 ]; then ok "5 tests caught $k of 4 injected bugs"; else no "5 tests caught only $k of 4 bugs (need 3)"; fi
  a=$(pct $O/after.txt)
  if [ -n "$a" ] && [ "$a" -ge 90 ]; then ok "6 after.txt: end was $a%"; else no "6 after.txt: save the final report"; fi
  echo; echo "$pass / $total passed"; [ $pass -eq $total ]
}
status() { [ -d $D ] && echo "lab 140 running in $D" || echo "lab 140 not running"; }
case "$1" in up) up;; check) check;; down) down; echo "lab 140 removed.";; status) status;; *) echo "usage: lab up|check|down|status";; esac
