#!/bin/bash
# Lesson 48 checker: bash check48.sh [FOLDER]   (folder holds inventory.py, data48.py, expected48.txt; changes nothing)
d=${1:-.}; cd "$d" || exit 2
chk() { if eval "$2" >/dev/null 2>&1; then echo "PASS  $1"; else echo "FAIL  $1"; fails=$((fails+1)); fi; }
fails=0
chk "inventory.py runs without errors"   "python3 inventory.py"
chk "output matches expected48.txt"      "test -z \"\$(python3 inventory.py | diff - expected48.txt)\""
chk "busy() returns the right names"     "python3 -c \"from inventory import busy; from data48 import SERVERS; assert busy(SERVERS, 80) == ['web2']; assert busy(SERVERS, 10) == ['web1', 'web2', 'db1', 'test1']; assert busy(SERVERS, 99) == []\""
chk "importing inventory prints nothing" "test -z \"\$(python3 -c 'import inventory')\""
exit $((fails>0))
