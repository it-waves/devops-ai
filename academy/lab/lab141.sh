#!/bin/sh
# lab141.sh : Software Testing and QA, lesson 7: tests in CI with pass/fail gates. Run with sudo.
#   up | check | down | status     Needs: python3, pytest, pytest-cov, PyYAML (sudo apt install -y python3-pytest python3-pytest-cov python3-yaml)
D=${LAB141_DIR:-/opt/lab141}
OWNER=${SUDO_USER:-root}
AS=""; [ "$OWNER" != root ] && AS="runuser -u $OWNER --"
down() { rm -rf "${D:?}" 2>/dev/null; true; }
up() {
  python3 -c "import pytest, pytest_cov, yaml" >/dev/null 2>&1 || { echo "need: sudo apt install -y python3-pytest python3-pytest-cov python3-yaml"; exit 1; }
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  down; mkdir -p $D/tests $D/.github/workflows
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
  cat > $D/tests/test_cart.py <<'EOF_P'
import pytest
from cart import total_cents, shipping_cents

def test_free_shipping_edge():
    assert shipping_cents(7500) == 0
    assert shipping_cents(7499) == 599

def test_empty_cart_is_free():
    assert shipping_cents(0) == 0

def test_total_without_code():
    assert total_cents(10000) == 10800

def test_welcome_code():
    assert total_cents(10000, "WELCOME10") == 9720

def test_bulk_edges():
    assert total_cents(20000, "BULK") == 17280
    assert total_cents(19999, "BULK") == 21599

def test_unknown_code():
    with pytest.raises(ValueError):
        total_cents(5000, "NOPE")
EOF_P
  printf '[pytest]\npythonpath = .\n' > $D/pytest.ini
  printf '[run]\nbranch = True\nomit =\n    tests/*\n' > $D/.coveragerc
  cat > $D/TASKS.txt <<'EOF_T'
LAB 141  Tests in CI: a workflow with real gates
Folder /opt/lab141 holds CloudCart pricing code and 6 passing tests. Do not change cart.py or tests/.
Write ONE file: .github/workflows/ci.yml  (use vim). Run  lab check  after each step.

1  The file is valid YAML and has a job.
2  It runs on push and on pull_request.
3  The job runs on ubuntu, has timeout-minutes, and the workflow has a
   permissions block with contents: read (least privilege).
4  Every uses: is pinned to a version (like @v4). Never @main or @master.
   Include actions/checkout.
5  A run step calls pytest with --cov-fail-under=80 or more (the gate), and
   an upload-artifact step with  if: always()  saves the report even on failure.
6  The gate must really work: lab check runs YOUR pytest command here. It must pass
   on this code, and FAIL when lab check plants a bug in a copy.
Try the gate yourself first:  pytest --cov=cart --cov-fail-under=90 -q ; echo $?
lab check   (all 6 PASS to finish)      lab down   (removes everything)
EOF_T
  chown -R $OWNER $D 2>/dev/null; chmod -R a+rX $D
  echo "lab 141 ready in $D. Read TASKS.txt"
}
pass=0; total=6
ok() { pass=$((pass+1)); echo "  PASS  $1"; }
no() { echo "  FAIL  $1"; }
check() {
  [ -d $D ] || { echo "lab is not up: run  lab up"; exit 1; }
  R=$(python3 - "$D" <<'EOF_Y'
import sys, yaml, os, re, subprocess, shutil, tempfile
D = sys.argv[1]; out = {}
p = os.path.join(D, ".github/workflows/ci.yml")
try:
    w = yaml.safe_load(open(p)); jobs = w["jobs"]; assert isinstance(jobs, dict) and jobs
    out[1] = True
except Exception:
    w = {}; jobs = {}; out[1] = False
on = w.get("on", w.get(True, {})) if isinstance(w, dict) else {}
if isinstance(on, str): on = [on]
out[2] = out[1] and "push" in on and "pull_request" in on
perm = w.get("permissions") if isinstance(w, dict) else None
def perm_ok(x): return isinstance(x, dict) and x.get("contents") == "read"
j_ok = False
for j in jobs.values():
    ro = str(j.get("runs-on", ""))
    if ro.startswith("ubuntu") and "timeout-minutes" in j and (perm_ok(perm) or perm_ok(j.get("permissions"))): j_ok = True
out[3] = j_ok
steps = [s for j in jobs.values() for s in j.get("steps", []) if isinstance(s, dict)]
uses = [s["uses"] for s in steps if "uses" in s]
out[4] = any(u.startswith("actions/checkout@") for u in uses) and all("@" in u and not re.search(r"@(main|master|latest)$", u) for u in uses)
runs = [s for s in steps if "pytest" in str(s.get("run", ""))]
gate = None
for s in runs:
    m = re.search(r"--cov-fail-under[= ](\d+)", s["run"])
    if m and int(m.group(1)) >= 80: gate = s["run"]
up_ok = any(str(s.get("uses", "")).startswith("actions/upload-artifact@") and str(s.get("if", "")).replace(" ", "") in ("always()", "${{always()}}") for s in steps)
out[5] = bool(gate) and up_ok
def run_in(src, bug):
    t = tempfile.mkdtemp(); os.chmod(t, 0o755); w2 = os.path.join(t, "w"); shutil.copytree(src, w2, ignore=shutil.ignore_patterns(".github", "__pycache__", ".pytest_cache"))
    if bug:
        f = os.path.join(w2, "cart.py"); s2 = open(f).read().replace("subtotal // 10\n", "subtotal // 100\n"); open(f, "w").write(s2)
    subprocess.run(["chmod", "-R", "a+rwX", t])
    return t, w2
if gate:
    res = []
    for bug in (False, True):
        t, w2 = run_in(D, bug)
        cmd = gate.replace("python -m", "python3 -m")
        pre = ["runuser", "-u", os.environ.get("SUDO_USER", "root"), "--"] if os.environ.get("SUDO_USER", "root") != "root" else []
        rc = subprocess.run(pre + ["sh", "-c", cmd], cwd=w2, capture_output=True).returncode
        res.append(rc); shutil.rmtree(t, ignore_errors=True)
    out[6] = res[0] == 0 and res[1] != 0
else:
    out[6] = False
for i in range(1, 7): print(i, "1" if out[i] else "0")
EOF_Y
)
  msg1="1 ci.yml is valid YAML with a job"; msg2="2 triggers: push and pull_request"; msg3="3 ubuntu, timeout, permissions: contents read"
  msg4="4 every uses: pinned, checkout included"; msg5="5 pytest gate (80+) and upload if: always()"; msg6="6 gate passes now, fails on a planted bug"
  for i in 1 2 3 4 5 6; do
    v=$(echo "$R" | awk -v n=$i '$1==n{print $2}'); eval m=\$msg$i
    if [ "$v" = 1 ]; then ok "$m"; else no "$m"; fi
  done
  echo; echo "$pass / $total passed"; [ $pass -eq $total ]
}
status() { [ -d $D ] && echo "lab 141 running in $D" || echo "lab 141 not running"; }
case "$1" in up) up;; check) check;; down) down; echo "lab 141 removed.";; status) status;; *) echo "usage: lab up|check|down|status";; esac
