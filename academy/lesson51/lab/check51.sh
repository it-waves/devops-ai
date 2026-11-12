#!/bin/bash
# Lesson 51 checker: bash check51.sh [FOLDER]   (folder holds fetch_retry.py and api06.py; starts the lab API on port 8099 and stops it again)
d=${1:-.}; cd "$d" || exit 2
python3 api06.py 8099 >/dev/null 2>&1 & api=$!
trap 'kill $api 2>/dev/null' EXIT
sleep 1
chk() { if eval "$2" >/dev/null 2>&1; then echo "PASS  $1"; else echo "FAIL  $1"; fails=$((fails+1)); fi; }
fails=0
API_URL=http://127.0.0.1:8099 timeout 40 python3 fetch_retry.py >/tmp/c51.out 2>/tmp/c51.err; rc1=$?
chk "recovers after two failures: prints recovered, exit 0" "test $rc1 -eq 0 && grep -qx recovered /tmp/c51.out"
chk "logs each failed attempt as a WARNING (at least two)" "test \$(grep -ci 'warning.*attempt' /tmp/c51.err) -ge 2"
API_URL=http://127.0.0.1:1 timeout 60 python3 fetch_retry.py >/tmp/c51b.out 2>/tmp/c51b.err; rc2=$?
chk "server down: gives up with 'gave up', exit not 0, no traceback" "test $rc2 -ne 0 && grep -qi 'gave up' /tmp/c51b.err && ! grep -q Traceback /tmp/c51b.err"
chk "timeout on the call, no bare except" "grep -q 'timeout=' fetch_retry.py && ! grep -qE '^[[:space:]]*except[[:space:]]*:' fetch_retry.py"
exit $((fails>0))
