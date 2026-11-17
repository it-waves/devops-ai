#!/bin/sh
# lab138.sh : Software Testing and QA, lesson 4: browser tests with Playwright, traces and the trace viewer. Run with sudo.
#   up | check | down | status   Needs: python3, pytest, pytest-playwright, pytest-html and Google Chrome (pip install pytest-playwright pytest-html)
D=${LAB138_DIR:-/opt/lab138}
OWNER=${SUDO_USER:-root}
down() { rm -rf "${D:?}" 2>/dev/null; true; }
up() {
  python3 -c "import playwright, pytest_playwright, pytest_html" >/dev/null 2>&1 || { echo "needed: pip install pytest-playwright pytest-html  (and Google Chrome)"; exit 1; }
  down; mkdir -p $D/tests $D/site $D/out
  cat > $D/site/index.html <<'EOF_P'
<!doctype html>
<html><head><meta charset="utf-8"><title>CloudCart Mini Shop</title>
<style>body{font-family:sans-serif;margin:40px}li{margin:6px 0}button{margin-left:8px}</style></head>
<body>
<h1>CloudCart Mini Shop</h1>
<ul id="items">
  <li>Mug, $10 <button data-item="mug" data-price="10">Add mug</button></li>
  <li>Cap, $15 <button data-item="cap" data-price="15">Add cap</button></li>
</ul>
<p>Cart: <span id="count">0</span> items, total $<span id="total">0</span></p>
<button id="clear">Remove all</button>
<button id="checkout" disabled>Checkout</button>
<script src="app.js"></script>
</body></html>
EOF_P
  cat > $D/site/app.js <<'EOF_P'
let count = 0, total = 0;
function show() {
  document.getElementById("count").textContent = count;
  document.getElementById("total").textContent = total;
  document.getElementById("checkout").disabled = count === 0;
}
document.querySelectorAll("[data-item]").forEach(b => b.addEventListener("click", () => {
  count += 1;
  total = Number(b.dataset.price) * count;  // BUG: should add
  show();
}));
document.getElementById("clear").addEventListener("click", () => { count = 0; total = 0; show(); });
EOF_P
  cat > $D/tests/test_shop.py <<'EOF_P'
import pathlib
from playwright.sync_api import Page, expect

SHOP = (pathlib.Path(__file__).parent.parent / "site" / "index.html").as_uri()

def test_page_title(page: Page):
    page.goto(SHOP)
    expect(page).to_have_title("CloudCart Mini Shop")

def test_add_item_updates_count(page: Page):
    page.goto(SHOP)
    page.get_by_role("button", name="Add mug").click()
    expect(page.locator("#count")).to_have_text("1")

def test_total_after_two_items(page: Page):
    page.goto(SHOP)
    page.get_by_role("button", name="Add mug").click()
    page.get_by_role("button", name="Add cap").click()
    expect(page.locator("#total")).to_have_text("25")

def test_remove_all_empties_cart(page: Page):
    page.goto(SHOP)
    page.get_by_role("button", name="Add cap").click()
    page.get_by_role("button", name="Remove all").click()
    expect(page.locator("#count")).to_have_text("0")

def test_checkout_disabled_when_empty(page: Page):
    page.goto(SHOP)
    expect(page.get_by_role("button", name="Checkout")).to_be_disabled()
EOF_P
  cat > $D/pytest.ini <<'EOF_P'
[pytest]
addopts = --browser-channel chrome
EOF_P
  ( cd $D && sha256sum tests/*.py > .tests.sha )
  cat > $D/README.txt <<'EOF_P'
LAB 138: browser tests with Playwright, traces and the trace viewer
Work in this folder. The shop page has 5 browser tests: one fails because of a bug in site/app.js.
Put every file you create in the out/ folder:
 1. Run the tests, save the output:                out/run.txt          (pytest -q | tee ...)
 2. Save the exit code of the FAILING run:          out/exit_failing.txt (echo $? > ...)
 3. Record a trace of every test:                   out/results/         (--tracing on --output out/results)
 4. Also take a screenshot when a test fails:       out/results/*.png    (--screenshot only-on-failure)
 5. Save one self-contained HTML report:            out/report.html      (--html, --self-contained-html)
 6. Fix the bug in site/app.js (NOT in the tests), run again, save the exit code:  out/exit_passing.txt
Steps 1 to 5 can be one run. Open the failing trace with: python3 -m playwright show-trace <trace.zip>
Then: lab check
EOF_P
  chown -R $OWNER $D
  echo "lab 138 ready in $D"
}
chk() { if [ "$1" = ok ]; then echo "  PASS  $2"; P=$((P+1)); else echo "  FAIL  $2"; fi; N=$((N+1)); }
check() {
  [ -d $D ] || { echo "lab not running: run  sudo lab up"; exit 1; }
  P=0; N=0; O=$D/out; AS=""; [ "$OWNER" != root ] && AS="runuser -u $OWNER --"
  s=bad; grep -q "1 failed, 4 passed" $O/run.txt 2>/dev/null && s=ok
  chk $s "run.txt: 1 failed, 4 passed"
  s=bad; [ "$(cat $O/exit_failing.txt 2>/dev/null | tr -d ' \n')" = 1 ] && s=ok
  chk $s "exit_failing.txt holds 1"
  n=$(find $O/results -name trace.zip 2>/dev/null | wc -l)
  s=bad; [ "$n" -ge 5 ] && s=ok
  chk $s "traces: one trace.zip per test"
  s=bad; find $O/results -name '*.png' 2>/dev/null | grep -q . && s=ok
  chk $s "screenshot of the failure saved"
  s=bad; [ -f $O/report.html ] && grep -q "<style" $O/report.html && ! grep -q 'rel="stylesheet"' $O/report.html && grep -q "test_total_after_two_items" $O/report.html && s=ok
  chk $s "report.html: self-contained, shows the failure"
  s=bad; ( cd $D && sha256sum -c .tests.sha >/dev/null 2>&1 ) && [ "$(cat $O/exit_passing.txt 2>/dev/null | tr -d ' \n')" = 0 ] && ( cd $D && $AS python3 -m pytest -q -p no:cacheprovider --output /tmp/lab138chk >/dev/null 2>&1 ) && s=ok
  rm -rf /tmp/lab138chk
  chk $s "app.js fixed, tests untouched, exit 0"
  echo; echo "$P / $N passed"; [ $P = $N ]
}
status() { [ -d $D ] && echo "lab 138 running in $D" || echo "lab 138 not running"; }
case "$1" in up) up;; check) check;; down) down; echo "lab 138 removed.";; status) status;; *) echo "usage: lab up|check|down|status";; esac
