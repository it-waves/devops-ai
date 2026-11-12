#!/bin/bash
# Lesson 55 checker: bash check55.sh [FOLDER]   (folder holds your invcheck.py and test_invcheck.py; needs pytest in your venv)
d=${1:-.}; cd "$d" || exit 2
here=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
fails=0
chk() { if eval "$2" >/dev/null 2>&1; then echo "PASS  $1"; else echo "FAIL  $1"; fails=$((fails+1)); fi; }
t=$(mktemp -d); trap 'rm -rf "$t"' EXIT
echo '[{"name":"web-01","env":"prod","ip":"10.0.0.5"},{"name":"db-01","env":"staging","ip":"10.0.0.6"}]' > "$t/good.json"
echo '[{"name":"a","env":"prod","ip":"10.0.0.1"},{"name":"a","env":"test","ip":"10.0.0.2"},{"name":"b","env":"dev","ip":"300.1.1.1"}]' > "$t/bad.json"
echo 'not json' > "$t/junk.json"
chk "valid file: no output and exit code 0" "out=\$(python3 invcheck.py $t/good.json); rc=\$?; test \$rc -eq 0 && test -z \"\$out\""
chk "bad file: three problems, three lines, exit code 1" "out=\$(python3 invcheck.py $t/bad.json); rc=\$?; test \$rc -eq 1 && test \$(echo \"\$out\" | grep -c .) -eq 3"
chk "missing file and invalid JSON both exit with code 2" "python3 invcheck.py $t/none.json; a=\$?; python3 invcheck.py $t/junk.json; b=\$?; test \$a -eq 2 && test \$b -eq 2"
chk "validate(): name, env, ip rules and one error per problem" "python3 - <<'PY'
from invcheck import validate
ok = {'name': 'w', 'env': 'dev', 'ip': '10.1.2.3'}
assert validate([ok]) == []
assert len(validate([ok, ok])) == 1
assert len(validate([dict(ok, env='qa')])) == 1
assert len(validate([dict(ok, ip='1.2.3')])) == 1
assert len(validate([dict(ok, name='')])) == 1
assert len(validate([{'env': 'dev', 'ip': '10.0.0.1'}])) == 1
assert len(validate([dict(ok, env='qa', ip='x')])) == 2
PY"
python3 -m pytest -q -p no:cacheprovider test_invcheck.py >"$t/o" 2>&1; rc=$?
chk "at least 6 tests, all passing, and parametrize is used" "test $rc -eq 0 && test \$(grep -oE '^[0-9]+ passed' $t/o | grep -oE '[0-9]+') -ge 6 && grep -q parametrize test_invcheck.py"
chk "your tests fail against the broken version (they catch its bugs)" "test $rc -eq 0 && m=\$(mktemp -d) && cp test_invcheck.py \$m/ && cp $here/broken_invcheck.py \$m/invcheck.py && (cd \$m && python3 -m pytest -q -p no:cacheprovider test_invcheck.py >/dev/null 2>&1; test \$? -eq 1); r=\$?; rm -rf \$m; test \$r -eq 0"
exit $((fails>0))
