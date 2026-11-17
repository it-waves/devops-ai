#!/bin/sh
# lab136.sh : Software Testing and QA, lesson 2: assertions, fixtures, mocks, test data, isolation. Run with sudo.
#   up | check | down | status        Needs: python3 and pytest (sudo apt install -y python3-pytest)
D=${LAB136_DIR:-/opt/lab136}
OWNER=${SUDO_USER:-root}
down() { rm -rf "${D:?}" 2>/dev/null; true; }
up() {
  command -v python3 >/dev/null 2>&1 && python3 -m pytest --version >/dev/null 2>&1 || { echo "pytest not found: run  sudo apt install -y python3-pytest"; exit 1; }
  down; mkdir -p $D/tests
  cat > $D/shop.py <<'EOF_P'
"""CloudCart mini shop, part 2: tax, discounts, a cart, and a receipt e-mail."""
import os

BUG = os.environ.get("SHOP_BUG", "")      # the judge switches bugs on to see if YOUR tests notice

def total_with_tax(cents, pct):
    """Total in cents, rounded to the nearest cent."""
    if BUG == "tax":
        return cents + cents * pct // 100
    return round(cents * (100 + pct) / 100)

TIERS = {"none": 0, "silver": 5, "gold": 10, "vip": 15}

def discounted(cents, tier):
    pct = TIERS[tier]
    if BUG == "discount" and tier == "gold":
        pct = 5
    return cents * (100 - pct) // 100

class Cart:
    _shared = []
    def __init__(self):
        self.items = Cart._shared if BUG == "shared" else []
    def add(self, name, qty=1):
        if qty <= 0 and BUG != "noerr":
            raise ValueError("qty must be positive")
        self.items.append((name, qty))
    def count(self):
        return sum(q for _, q in self.items)

class SmtpMailer:
    """The real mailer. It needs a mail server, which a test must never use."""
    def send(self, to, body):
        raise RuntimeError("no mail server here: a test must not send real e-mail")

def send_receipt(order, mailer):
    body = "Thanks %s, you paid %d cents" % (order["name"], order["total"])
    mailer.send(order["email"], body)
    if BUG == "mail":
        mailer.send(order["email"], body)
EOF_P
  cat > $D/conftest.py <<'EOF_P'
# shared fixtures go here
EOF_P
  cat > $D/tests/test_shop.py <<'EOF_P'
# YOUR tests go here. Read ../README.txt
EOF_P
  cat > $D/README.txt <<'EOF_P'
LAB 136: write tests that CATCH bugs (shop.py)
Rules of the shop: total_with_tax rounds to the nearest cent; tiers none 0%, silver 5%,
gold 10%, vip 15%; a cart rejects qty 0 or less; send_receipt e-mails the customer ONCE.
Write tests/test_shop.py (and conftest.py) with:
 1. an assertion for tax (one case must catch rounding),
 2. a mock mailer: assert the receipt is sent exactly once (use unittest.mock),
 3. test data with @pytest.mark.parametrize: at least 3 discount tiers,
 4. a fixture for a fresh Cart, and two tests that each add items and check the count,
 5. pytest.raises for a bad quantity.
lab check turns bugs on, one at a time (SHOP_BUG=tax, mail, discount, shared, noerr).
A good test passes on correct code AND fails when its bug is switched on.
Run tests from this folder:  python3 -m pytest -q
EOF_P
  chown -R $OWNER $D
  echo "lab 136 ready in $D"
}
py() { ( cd $D && env "$@" python3 -m pytest -q -p no:cacheprovider tests ) >/dev/null 2>&1; }
chk() { if [ "$1" = ok ]; then echo "  PASS  $2"; P=$((P+1)); else echo "  FAIL  $2"; fi; N=$((N+1)); }
check() {
  [ -d $D ] || { echo "lab not running: run  sudo lab up"; exit 1; }
  P=0; N=0; F=$D/tests/test_shop.py; ALL="$D/tests/test_shop.py $D/conftest.py"
  n=$(cd $D && python3 -m pytest --collect-only -q -p no:cacheprovider tests 2>/dev/null | grep -c "::")
  s=bad; [ "$n" -ge 6 ] && py X=1 && s=ok; chk $s "at least 6 tests, all pass on correct code"
  s=bad; py X=1 && ! py SHOP_BUG=tax && s=ok; chk $s "tests catch the tax rounding bug"
  s=bad; py X=1 && ! py SHOP_BUG=mail && grep -q "Mock\|patch" $F && s=ok; chk $s "mock mailer catches the double e-mail"
  m=$(cd $D && python3 -m pytest --collect-only -q -p no:cacheprovider -k discount tests 2>/dev/null | grep -c "::")
  s=bad; py X=1 && ! py SHOP_BUG=discount && [ "$m" -ge 3 ] && grep -q parametrize $F && s=ok; chk $s "parametrized data: 3+ discount cases catch the bad tier"
  s=bad; py X=1 && ! py SHOP_BUG=shared && grep -q "pytest.fixture" $ALL && s=ok; chk $s "a fixture gives a fresh cart: shared state is caught"
  s=bad; py X=1 && ! py SHOP_BUG=noerr && grep -q "pytest.raises" $F && s=ok; chk $s "pytest.raises catches the missing error"
  echo; echo "$P / $N passed"; [ $P = $N ]
}
status() { [ -d $D ] && echo "lab 136 running in $D" || echo "lab 136 not running"; }
case "$1" in up) up;; check) check;; down) down; echo "lab 136 removed.";; status) status;; *) echo "usage: lab up|check|down|status";; esac
