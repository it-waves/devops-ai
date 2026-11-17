#!/bin/sh
# lab135.sh : Software Testing and QA, lesson 1: classify tests (unit, integration, API, end-to-end, smoke, regression). Run with sudo.
#   up | check | down | status        Needs: python3 and pytest (sudo apt install -y python3-pytest)
D=${LAB135_DIR:-/opt/lab135}
OWNER=${SUDO_USER:-root}
down() { rm -rf "${D:?}" 2>/dev/null; true; }
up() {
  command -v python3 >/dev/null 2>&1 && python3 -m pytest --version >/dev/null 2>&1 || { echo "pytest not found: run  sudo apt install -y python3-pytest"; exit 1; }
  down; mkdir -p $D/tests
  cat > $D/shop.py <<'EOF_P'
"""CloudCart mini shop: prices, a cart in SQLite, and a small JSON API."""
import json, os, sqlite3, threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PRODUCTS = {1: ("Mug", 999), 2: ("Lamp", 2400), 3: ("Desk", 15900)}

def line_total(price_cents, qty):
    if qty < 0:
        raise ValueError("qty must not be negative")
    return price_cents * qty

def apply_discount(total_cents, pct):
    if os.environ.get("SHOP_BUG") == "1":
        return total_cents - int(total_cents * pct / 100)      # bug 12: rounds the discount down
    return total_cents - round(total_cents * pct / 100)

def open_db(path):
    db = sqlite3.connect(path)
    db.execute("CREATE TABLE IF NOT EXISTS cart (product_id INTEGER, qty INTEGER)")
    return db

def add_to_cart(db, product_id, qty):
    db.execute("INSERT INTO cart VALUES (?, ?)", (product_id, qty)); db.commit()

def cart_total(db):
    return sum(line_total(PRODUCTS[p][1], q) for p, q in db.execute("SELECT product_id, qty FROM cart"))

class Handler(BaseHTTPRequestHandler):
    db = None
    def log_message(self, *a): pass
    def _send(self, code, body):
        data = json.dumps(body).encode(); self.send_response(code)
        self.send_header("Content-Type", "application/json"); self.send_header("Content-Length", str(len(data)))
        self.end_headers(); self.wfile.write(data)
    def do_GET(self):
        if self.path == "/health": return self._send(200, {"status": "ok"})
        if self.path == "/api/products": return self._send(200, [{"id": i, "name": n, "price_cents": c} for i, (n, c) in PRODUCTS.items()])
        if self.path == "/api/cart": return self._send(200, {"total_cents": cart_total(self.db)})
        self._send(404, {"error": "not found"})
    def do_POST(self):
        n = int(self.headers.get("Content-Length", 0)); body = json.loads(self.rfile.read(n) or b"{}")
        if self.path == "/api/cart":
            if body.get("product_id") not in PRODUCTS: return self._send(400, {"error": "unknown product"})
            add_to_cart(self.db, body["product_id"], body.get("qty", 1)); return self._send(201, {"ok": True})
        if self.path == "/api/checkout":
            total = cart_total(self.db)
            if total == 0: return self._send(409, {"error": "cart is empty"})
            self.db.execute("DELETE FROM cart"); self.db.commit(); return self._send(200, {"paid_cents": total})
        self._send(404, {"error": "not found"})

def start_server(db_path=":memory:"):
    Handler.db = sqlite3.connect(db_path, check_same_thread=False)
    Handler.db.execute("CREATE TABLE IF NOT EXISTS cart (product_id INTEGER, qty INTEGER)")
    srv = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv
EOF_P
  cat > $D/conftest.py <<'EOF_P'
import json, urllib.request, pytest, shop

@pytest.fixture
def db(tmp_path):
    return shop.open_db(str(tmp_path / "cart.db"))

@pytest.fixture
def server():
    srv = shop.start_server()
    yield "http://127.0.0.1:%d" % srv.server_address[1]
    srv.shutdown()

def call(base, path, body=None):
    req = urllib.request.Request(base + path, data=None if body is None else json.dumps(body).encode(), method="GET" if body is None else "POST")
    try:
        with urllib.request.urlopen(req) as r: return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e: return e.code, json.loads(e.read())
EOF_P
  cat > $D/tests/test_prices.py <<'EOF_P'
import pytest, shop

def test_line_total():
    assert shop.line_total(999, 3) == 2997

def test_line_total_zero_qty():
    assert shop.line_total(2400, 0) == 0

def test_negative_qty_is_rejected():
    with pytest.raises(ValueError):
        shop.line_total(999, -1)

def test_ten_percent_discount():
    assert shop.apply_discount(2000, 10) == 1800

def test_no_discount():
    assert shop.apply_discount(999, 0) == 999
EOF_P
  cat > $D/tests/test_cart_db.py <<'EOF_P'
import shop

def test_empty_cart_total_is_zero(db):
    assert shop.cart_total(db) == 0

def test_added_items_are_stored(db):
    shop.add_to_cart(db, 1, 2)
    assert db.execute("SELECT count(*) FROM cart").fetchone()[0] == 1

def test_total_reads_the_db(db):
    shop.add_to_cart(db, 1, 2); shop.add_to_cart(db, 2, 1)
    assert shop.cart_total(db) == 999 * 2 + 2400
EOF_P
  cat > $D/tests/test_api.py <<'EOF_P'
from conftest import call

def test_products_endpoint_lists_three(server):
    code, body = call(server, "/api/products")
    assert code == 200 and len(body) == 3

def test_unknown_product_is_rejected(server):
    code, body = call(server, "/api/cart", {"product_id": 99})
    assert code == 400 and "error" in body

def test_checkout_of_empty_cart_conflicts(server):
    code, body = call(server, "/api/checkout", {})
    assert code == 409
EOF_P
  cat > $D/tests/test_journey.py <<'EOF_P'
from conftest import call

def test_buy_a_mug_and_a_lamp(server):
    assert call(server, "/api/products")[0] == 200
    assert call(server, "/api/cart", {"product_id": 1, "qty": 1})[0] == 201
    assert call(server, "/api/cart", {"product_id": 2, "qty": 1})[0] == 201
    assert call(server, "/api/cart")[1]["total_cents"] == 3399
    code, body = call(server, "/api/checkout", {})
    assert code == 200 and body["paid_cents"] == 3399
    assert call(server, "/api/cart")[1]["total_cents"] == 0
EOF_P
  cat > $D/tests/test_health.py <<'EOF_P'
from conftest import call

def test_health_is_ok(server):
    assert call(server, "/health") == (200, {"status": "ok"})

def test_catalog_is_not_empty(server):
    assert len(call(server, "/api/products")[1]) > 0
EOF_P
  cat > $D/README.txt <<'EOF_P'
LAB 135: classify the tests of the CloudCart mini shop
1. Read every file in tests/. Decide the type of each test:
   unit, integration, api, e2e, smoke (or more than one).
2. Create pytest.ini in this folder. Register six markers:
   unit, integration, api, e2e, smoke, regression. Turn on strict markers.
3. Mark every test with its type (pytestmark in each file, or @pytest.mark).
4. Bug 12: 10 percent off 9.99 gave 9.00, not 8.99. Write tests/test_regression.py
   with one test marked regression that catches it. It must fail with the bug
   (SHOP_BUG=1 pytest -m regression) and pass without it.
5. Run:  lab check     (looks at your files, never changes them)
Run tests from this folder:  python3 -m pytest -m unit
EOF_P
  chown -R $OWNER $D
  echo "lab 135 ready in $D"
}
count() { ( cd $D && python3 -m pytest --collect-only -q -m "$1" -p no:cacheprovider 2>/dev/null | grep -c "::" ); }
chk() { if [ "$1" = ok ]; then echo "  PASS  $2"; P=$((P+1)); else echo "  FAIL  $2"; fi; N=$((N+1)); }
check() {
  [ -d $D ] || { echo "lab not running: run  sudo lab up"; exit 1; }
  P=0; N=0; cd $D
  ok=bad; if [ -f pytest.ini ] && grep -q strict pytest.ini; then ok=ok; for m in unit integration api e2e smoke regression; do grep -qw "$m" pytest.ini || ok=bad; done; fi
  chk $ok "pytest.ini registers six markers, strict"
  [ "$(count unit)" = 5 ] && [ "$(count 'unit and not api')" = 5 ] && s=ok || s=bad; chk $s "unit: exactly the 5 price tests"
  [ "$(count integration)" = 3 ] && s=ok || s=bad; chk $s "integration: exactly the 3 database tests"
  [ "$(count api)" = 3 ] && [ "$(count e2e)" = 1 ] && s=ok || s=bad; chk $s "api: 3 tests, e2e: 1 test"
  r=bad; [ "$(count smoke)" = 2 ] && python3 -m pytest -q -m smoke -p no:cacheprovider >/dev/null 2>&1 && r=ok; chk $r "smoke: 2 tests, all pass"
  r=bad; if [ -f tests/test_regression.py ] && [ "$(count regression)" -ge 1 ]; then python3 -m pytest -q -m regression -p no:cacheprovider >/dev/null 2>&1 && ! SHOP_BUG=1 python3 -m pytest -q -m regression -p no:cacheprovider >/dev/null 2>&1 && r=ok; fi
  chk $r "regression test passes, and fails when bug 12 is back"
  echo; echo "$P / $N passed"; [ $P = $N ]
}
status() { [ -d $D ] && echo "lab 135 running in $D" || echo "lab 135 not running"; }
case "$1" in up) up;; check) check;; down) down; echo "lab 135 removed.";; status) status;; *) echo "usage: lab up|check|down|status";; esac
