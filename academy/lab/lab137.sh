#!/bin/sh
# lab137.sh : Software Testing and QA, lesson 3: run tests, read reports, exit codes. Run with sudo.
#   up | check | down | status        Needs: python3, pytest and pytest-html (sudo apt install -y python3-pytest python3-pytest-html)
D=${LAB137_DIR:-/opt/lab137}
OWNER=${SUDO_USER:-root}
down() { rm -rf "${D:?}" 2>/dev/null; true; }
up() {
  command -v python3 >/dev/null 2>&1 && python3 -m pytest --version >/dev/null 2>&1 && python3 -c "import pytest_html" >/dev/null 2>&1 || { echo "pytest or pytest-html not found: run  sudo apt install -y python3-pytest python3-pytest-html"; exit 1; }
  down; mkdir -p $D/tests $D/out
  cat > $D/stock.py <<'EOF_P'
"""CloudCart mini warehouse: stock levels and prices, in cents."""

def add_item(stock, name, qty):
    stock[name] = qty

def restock(stock, name, qty):
    stock[name] = qty  # BUG: replaces, should add

def remove(stock, name, qty):
    if stock.get(name, 0) < qty:
        raise ValueError("not enough stock")
    stock[name] -= qty

def price_with_tax(cents, pct):
    return round(cents * (100 + pct) / 100)

def price_discounted(cents, pct):
    return cents * (100 - pct) // 100
EOF_P
  cat > $D/tests/test_stock.py <<'EOF_P'
import pytest, stock

def test_stock_add_new_item():
    s = {}
    stock.add_item(s, "mug", 5)
    assert s["mug"] == 5

def test_stock_restock_adds():
    s = {"mug": 5}
    stock.restock(s, "mug", 3)
    assert s["mug"] == 8

def test_stock_remove_reduces():
    s = {"mug": 5}
    stock.remove(s, "mug", 2)
    assert s["mug"] == 3

def test_stock_cannot_go_negative():
    with pytest.raises(ValueError):
        stock.remove({"mug": 1}, "mug", 2)
EOF_P
  cat > $D/tests/test_prices.py <<'EOF_P'
import stock

def test_price_with_tax():
    assert stock.price_with_tax(1000, 8) == 1080

def test_price_rounds_to_nearest_cent():
    assert stock.price_with_tax(999, 8) == 1079

def test_price_discount():
    assert stock.price_discounted(1000, 10) == 900
EOF_P
  cat > $D/tests/test_extras.py <<'EOF_P'
import time, pytest

def test_report_builds_slowly():
    time.sleep(0.4)                          # a slow test: find it with --durations
    assert True

@pytest.mark.skip(reason="gift wrap is not built yet")
def test_gift_wrap_total():
    assert False

@pytest.mark.xfail(reason="known gap: multi-currency")
def test_multi_currency_total():
    assert 1 + 1 == 3
EOF_P
  ( cd $D && sha256sum tests/*.py > .tests.sha )
  cat > $D/README.txt <<'EOF_P'
LAB 137: run tests, read the reports, use the exit codes
Work in this folder. The project has 10 tests: one fails because of a bug in stock.py.
Put every file you create in the out/ folder:
 1. Run pytest and save a JUnit XML report:        out/junit.xml        (--junitxml)
 2. Save one self-contained HTML report:            out/report.html      (--html, --self-contained-html)
 3. Save the exit code of the FAILING run:          out/exit_failing.txt (echo $? > ...)
 4. Find the slowest tests, save the output:        out/slow.txt         (--durations=3)
 5. Run only the stock tests, verbose, save output: out/selected.txt     (-k stock -v)
 6. Fix the bug in stock.py (NOT in the tests), run again, save the exit code:  out/exit_passing.txt
Steps 1 to 4 are best done while the test still fails. Then: lab check
EOF_P
  chown -R $OWNER $D
  echo "lab 137 ready in $D"
}
chk() { if [ "$1" = ok ]; then echo "  PASS  $2"; P=$((P+1)); else echo "  FAIL  $2"; fi; N=$((N+1)); }
check() {
  [ -d $D ] || { echo "lab not running: run  sudo lab up"; exit 1; }
  P=0; N=0; O=$D/out
  s=bad; python3 - "$O/junit.xml" <<'EOF_P' 2>/dev/null && s=ok
import sys, xml.etree.ElementTree as ET
r = ET.parse(sys.argv[1]).getroot()
t = r if r.tag == "testsuite" else r.find("testsuite")
sys.exit(0 if (t.get("tests"), t.get("failures"), t.get("skipped")) == ("10", "1", "2") else 1)
EOF_P
  chk $s "junit.xml: JUnit report of the failing run"
  s=bad; [ -f $O/report.html ] && grep -q "<style" $O/report.html && ! grep -q 'rel="stylesheet"' $O/report.html && grep -q "test_stock_restock_adds" $O/report.html && s=ok
  chk $s "report.html: self-contained, shows the failure"
  s=bad; [ "$(cat $O/exit_failing.txt 2>/dev/null | tr -d ' \n')" = 1 ] && s=ok
  chk $s "exit_failing.txt holds 1 (the failing run)"
  s=bad; grep -q "slowest" $O/slow.txt 2>/dev/null && grep -q "test_report_builds_slowly" $O/slow.txt && s=ok
  chk $s "slow.txt lists the slowest tests"
  n=$(grep -c "::" $O/selected.txt 2>/dev/null); a=$(grep "::" $O/selected.txt 2>/dev/null | grep -vc stock)
  s=bad; [ "${n:-0}" -ge 4 ] && [ "${a:-1}" = 0 ] && grep -q "PASSED\|FAILED" $O/selected.txt && s=ok
  chk $s "selected.txt: only the stock tests, verbose"
  s=bad; ( cd $D && sha256sum -c .tests.sha >/dev/null 2>&1 && python3 -m pytest -q -p no:cacheprovider tests >/dev/null 2>&1 ) && [ "$(cat $O/exit_passing.txt 2>/dev/null | tr -d ' \n')" = 0 ] && s=ok
  chk $s "stock.py fixed, tests untouched, exit_passing.txt 0"
  echo; echo "$P / $N passed"; [ $P = $N ]
}
status() { [ -d $D ] && echo "lab 137 running in $D" || echo "lab 137 not running"; }
case "$1" in up) up;; check) check;; down) down; echo "lab 137 removed.";; status) status;; *) echo "usage: lab up|check|down|status";; esac
