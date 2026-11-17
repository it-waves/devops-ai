#!/bin/sh
# lab139.sh : Software Testing and QA, lesson 5: API and health tests for CloudCart. Run with sudo.
#   up | check | down | status     Needs: java, curl, python3, pytest (sudo apt install -y openjdk-21-jdk-headless curl python3-pytest)
#   Internet for Tomcat (14 MB) and the CloudCart WAR (0.3 MB). Ports 8139 and 8159 must be free.
D=${LAB139_DIR:-/opt/lab139}
OWNER=${SUDO_USER:-root}
TV=10.1.34
TB=${LAB139_TOMCAT_BASE:-https://archive.apache.org/dist/tomcat/tomcat-10/v$TV/bin}
WAR_URL=${LAB139_WAR_URL:-https://raw.githubusercontent.com/it-waves/devops-ai/main/academy/lab/assets/cloudcart-0.2.0.war}
B=localhost:8139/cloudcart
down() { pkill -f "catalina.base=$D/tomcat" 2>/dev/null; pkill -f "lab139-stub" 2>/dev/null; sleep 1; rm -rf "${D:?}" 2>/dev/null; true; }
up() {
  for t in java curl tar; do command -v $t >/dev/null 2>&1 || { echo "$t not found: run  sudo apt install -y openjdk-21-jdk-headless curl"; exit 1; }; done
  python3 -m pytest --version >/dev/null 2>&1 || { echo "pytest not found: run  sudo apt install -y python3-pytest"; exit 1; }
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  for p in 8139 8149; do if curl -s -o /dev/null -m 2 localhost:$p; then echo "port $p is already in use: stop what uses it first"; exit 1; fi; done
  down; mkdir -p $D/tests $D/out
  if [ -n "$LAB139_TOMCAT_TGZ" ] && [ -f "$LAB139_TOMCAT_TGZ" ]; then cp "$LAB139_TOMCAT_TGZ" $D/t.tgz
  else echo "downloading Tomcat $TV (about 14 MB) ..."; curl -fL --progress-bar -o $D/t.tgz "$TB/apache-tomcat-$TV.tar.gz" || { echo "download failed"; exit 1; }; fi
  mkdir -p $D/tomcat && tar xzf $D/t.tgz -C $D/tomcat --strip-components=1 || { echo "unpack failed"; exit 1; }; rm -f $D/t.tgz
  T=$D/tomcat
  sed -i 's#<Connector port="8080"#<Connector port="8139"#; s#<Server port="8005"#<Server port="8159"#' $T/conf/server.xml
  rm -rf $T/webapps/docs $T/webapps/examples $T/webapps/host-manager $T/webapps/manager $T/webapps/ROOT
  printf '%s\n' 'CATALINA_PID=$CATALINA_BASE/tomcat.pid' > $T/bin/setenv.sh; chmod 755 $T/bin/setenv.sh
  if [ -n "$LAB139_WAR" ] && [ -f "$LAB139_WAR" ]; then cp "$LAB139_WAR" $T/webapps/cloudcart.war
  else echo "downloading CloudCart 0.2.0 ..."; curl -fL --progress-bar -o $T/webapps/cloudcart.war "$WAR_URL" || { echo "app download failed"; exit 1; }; fi
  cat > $D/client.py <<'EOF_P'
import json, os, urllib.request as U, urllib.error as E
from http.cookiejar import CookieJar
BASE = os.environ.get("LAB139_BASE", "http://localhost:8139/cloudcart")

class Client:
    """One client = one browser session (its own cookies)."""
    def __init__(self):
        self.o = U.build_opener(U.HTTPCookieProcessor(CookieJar()))
    def call(self, method, path, data=None):
        body = json.dumps(data).encode() if data is not None else None
        req = U.Request(BASE + path, body, method=method)
        req.add_header("Content-Type", "application/json")
        try:
            r = self.o.open(req, timeout=5)
        except E.HTTPError as e:
            r = e
        except OSError:
            raise RuntimeError("shop is not answering") from None
        text = r.read().decode()
        return r.code, json.loads(text or "null")
    def get(self, p): return self.call("GET", p)
    def post(self, p, d=None): return self.call("POST", p, d)
EOF_P
  cat > $D/tests/test_health.py <<'EOF_P'
from client import Client

def test_health_answers_200():
    status, body = Client().get("/health")
    assert status == 200
EOF_P
  cat > $D/pytest.ini <<'EOF_P'
[pytest]
pythonpath = .
EOF_P
  cat > $D/TASKS.txt <<'EOF_T'
LAB 139  CloudCart: test its API and its health
Open a terminal in /opt/lab139. client.py is given: read it, it is 20 lines.
The shop's address is in $B  (localhost:8139/cloudcart). Run  lab check  after each step.

Start the shop:  tomcat/bin/startup.sh  then wait until  curl -s $B/health  answers UP.

1  tests/test_health.py: keep the first test, add two more (3 in all):
     /health says status UP and a version that is not empty
     /api/admin/stats has uptimeSeconds that is a number
2  tests/test_products.py (3 tests or more):
     /api/products returns 12 products, each with id, name and priceCents above 0
     /api/products?category=Audio returns only Audio products
     /api/products?sort=price-asc is sorted by priceCents, lowest first
3  tests/test_cart.py (3 tests or more), one new Client() per test:
     a new cart is empty (count 0)
     2 keyboards (product 1) cost 17800 and ship free (shippingCents 0)
     1 USB-C hub (product 2) pays shipping, and totalCents = subtotal + shipping + tax
     Add with:  c.post("/api/cart/items", {"productId": 1, "quantity": 2})
4  tests/test_errors.py (4 tests or more), checking these status codes:
     unknown path 404, product 7 is out of stock 409, checkout without signing in 401,
     checkout with ZIP "12" after signing in 400
     Sign in with:  c.post("/api/auth/login", {"email": "student@cloudcart.test", "password": "learn-cloudcart"})
     Checkout:      c.post("/api/orders", {"name": "Sam", "address": "1 Main St", "city": "Austin", "zip": "12"})
5  Your tests must be able to fail. lab check runs them against a fake shop that
   answers 200 and {} to everything. At least 8 of your tests must fail there.
6  lab check   (all 6 PASS to finish)      lab down   (stops Tomcat and removes everything)
EOF_T
  chown -R $OWNER $D 2>/dev/null; chmod -R a+rX $D
  echo "lab 139 ready in $D. Read TASKS.txt, then start Tomcat."
}
pass=0; total=6
ok() { pass=$((pass+1)); echo "  PASS  $1"; }
no() { echo "  FAIL  $1"; }
# runs one test file as the owner; prints: tests failures
runf() {
  [ -f "$1" ] || { echo "0 0"; return; }
  AS=""; [ "$OWNER" != root ] && AS="runuser -u $OWNER --"
  x=/tmp/lab139chk.xml; rm -f $x
  ( cd $D && LAB139_BASE=${2:-http://localhost:8139/cloudcart} $AS python3 -m pytest -q -p no:cacheprovider --junitxml=$x "$1" >/dev/null 2>&1 )
  python3 - $x <<'EOF_Y'
import sys, xml.etree.ElementTree as X
try:
    s = X.parse(sys.argv[1]).getroot(); s = s if s.tag == 'testsuite' else s[0]
    print(s.get('tests'), int(s.get('failures')) + int(s.get('errors')))
except Exception: print('0 0')
EOF_Y
}
check() {
  [ -d $D/tomcat ] || { echo "lab is not up: run  lab up"; exit 1; }
  h=$(curl -s -m 3 http://$B/health)
  case "$h" in *'"status":"UP"'*) ok "1 Tomcat is running and CloudCart says UP" ;; *) no "1 CloudCart is not answering: start Tomcat" ;; esac
  chk() { n=$1; f=$2; min=$3; msg=$4; r=$(runf tests/$f); set -- $r; if [ "$1" -ge "$min" ] && [ "$2" = 0 ] && grep -q "assert" $D/tests/$f 2>/dev/null; then ok "$n $f: $1 tests pass"; else no "$n $msg"; fi; }
  chk 2 test_health.py 3 "test_health.py needs 3 passing tests"
  chk 3 test_products.py 3 "test_products.py needs 3 passing tests"
  chk 4 test_cart.py 3 "test_cart.py needs 3 passing tests"
  r=$(runf tests/test_errors.py); set -- $r
  cov=1; for c in 404 409 401 400; do grep -q "$c" $D/tests/test_errors.py 2>/dev/null || cov=0; done
  if [ "$1" -ge 4 ] && [ "$2" = 0 ] && [ $cov = 1 ]; then ok "5 test_errors.py: $1 tests pass"; else no "5 test_errors.py: 4 tests, codes 404 409 401 400"; fi
  # the fake shop: 200 and {} for everything
  python3 -c '
import http.server, sys
class H(http.server.BaseHTTPRequestHandler):
    def _a(self):
        self.send_response(200); self.send_header("Content-Type","application/json"); self.send_header("Content-Length","2"); self.end_headers(); self.wfile.write(b"{}")
    do_GET = do_POST = do_PUT = do_DELETE = _a
    def log_message(self, *a): pass
http.server.HTTPServer(("127.0.0.1", 8149), H).serve_forever()  # lab139-stub
' >/dev/null 2>&1 &
  sp=$!; sleep 1
  AS=""; [ "$OWNER" != root ] && AS="runuser -u $OWNER --"
  x=/tmp/lab139fake.xml; rm -f $x
  ( cd $D && LAB139_BASE=http://127.0.0.1:8149/cloudcart $AS python3 -m pytest -q -p no:cacheprovider --junitxml=$x tests >/dev/null 2>&1 )
  kill $sp 2>/dev/null
  nf=$(python3 - $x <<'EOF_Y'
import sys, xml.etree.ElementTree as X
try:
    s = X.parse(sys.argv[1]).getroot(); s = s if s.tag == 'testsuite' else s[0]
    print(int(s.get('failures')) + int(s.get('errors')))
except Exception: print(0)
EOF_Y
)
  if [ "$nf" -ge 8 ]; then ok "6 tests catch a fake shop: $nf fail against it"; else no "6 fake shop: $nf of your tests fail (need 8)"; fi
  rm -f /tmp/lab139chk.xml /tmp/lab139fake.xml
  echo; echo "$pass / $total passed"; [ $pass -eq $total ]
}
status() { [ -d $D ] && echo "lab 139 running in $D" || echo "lab 139 not running"; }
case "$1" in up) up;; check) check;; down) down; echo "lab 139 removed.";; status) status;; *) echo "usage: lab up|check|down|status";; esac
