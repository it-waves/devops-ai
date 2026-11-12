#!/bin/bash
# Lesson 53 checker: bash check53.sh [FOLDER]   (folder holds inventory_tools.py and your test_tools.py; needs pytest and requests in your venv)
d=${1:-.}; cd "$d" || exit 2
chk() { if eval "$2" >/dev/null 2>&1; then echo "PASS  $1"; else echo "FAIL  $1"; fails=$((fails+1)); fi; }
fails=0
mut() { # $1 = sed expression that breaks the module; runs your tests against the broken copy
  m=$(mktemp -d); cp test_tools.py "$m"/; sed "$1" inventory_tools.py > "$m"/inventory_tools.py
  (cd "$m" && python3 -m pytest -q -p no:cacheprovider test_tools.py >/dev/null 2>&1); r=$?; rm -rf "$m"; return $r; }
python3 -m pytest -q -p no:cacheprovider test_tools.py >/tmp/c53.out 2>&1; rc=$?
chk "at least 5 tests, all passing, with no server running" "test $rc -eq 0 && test \$(grep -oE '^[0-9]+ passed' /tmp/c53.out | grep -oE '[0-9]+') -ge 5"
chk "your tests catch a wrong count (broken count_by_env)" "test $rc -eq 0 && { mut 's/+ 1/+ 2/'; test \$? -eq 1; }"
chk "your tests catch a missing status check (no raise_for_status)" "test $rc -eq 0 && { mut '/raise_for_status/d'; test \$? -eq 1; }"
chk "your tests catch a wrong JSON key" "test $rc -eq 0 && { mut 's/\"status\"\\]/\"state\"]/'; test \$? -eq 1; }"
chk "uses parametrize and pytest.raises" "grep -q 'parametrize' test_tools.py && grep -q 'pytest.raises' test_tools.py"
chk "fakes the network with Mock, patch or monkeypatch" "grep -qE 'Mock|patch|monkeypatch|mocker' test_tools.py"
exit $((fails>0))
