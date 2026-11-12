#!/bin/bash
# Lesson 52 checker: bash check52.sh [FOLDER]   (folder holds svc_check.py and api06.py; starts the lab API on port 8099 and stops it again)
d=${1:-.}; cd "$d" || exit 2
python3 api06.py 8099 >/dev/null 2>&1 & api=$!
trap 'kill $api 2>/dev/null' EXIT
sleep 1
chk() { if eval "$2" >/dev/null 2>&1; then echo "PASS  $1"; else echo "FAIL  $1"; fails=$((fails+1)); fi; }
fails=0
python3 svc_check.py http://127.0.0.1:8099/health >/tmp/c52a.out 2>/tmp/c52a.err; rc1=$?
chk "healthy URL: prints UP on standard out, exit 0" "test $rc1 -eq 0 && grep -q '^UP' /tmp/c52a.out"
python3 svc_check.py http://127.0.0.1:8099/missing >/tmp/c52b.out 2>/tmp/c52b.err; rc2=$?
chk "404 page: DOWN on standard error, exit 1, no traceback" "test $rc2 -eq 1 && grep -q '^DOWN' /tmp/c52b.err && ! grep -q Traceback /tmp/c52b.err && test ! -s /tmp/c52b.out"
python3 svc_check.py http://127.0.0.1:1/ >/tmp/c52c.out 2>/tmp/c52c.err; rc3=$?
chk "server down: exit 1, no traceback" "test $rc3 -eq 1 && ! grep -q Traceback /tmp/c52c.err"
python3 svc_check.py >/tmp/c52d.out 2>/tmp/c52d.err; rc4=$?
chk "no URL given: usage error, exit 2" "test $rc4 -eq 2 && grep -qi usage /tmp/c52d.err"
python3 svc_check.py -q http://127.0.0.1:8099/health >/tmp/c52e.out 2>/tmp/c52e.err; rc5=$?
python3 svc_check.py -q http://127.0.0.1:8099/missing >/tmp/c52f.out 2>/tmp/c52f.err; rc6=$?
chk "-q: no output at all, exit codes kept (0 and 1)" "test $rc5 -eq 0 && test $rc6 -eq 1 && test ! -s /tmp/c52e.out && test ! -s /tmp/c52e.err && test ! -s /tmp/c52f.out && test ! -s /tmp/c52f.err"
chk "uses argparse, timeout=, no bare except" "grep -q argparse svc_check.py && grep -q 'timeout=' svc_check.py && ! grep -qE '^[[:space:]]*except[[:space:]]*:' svc_check.py"
exit $((fails>0))
