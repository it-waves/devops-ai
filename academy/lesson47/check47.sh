#!/bin/bash
# Lesson 47 checker: bash check47.sh PROJECT_DIR   (prints PASS or FAIL for five checks; changes nothing)
d=${1:-.}
chk() { if eval "$2" >/dev/null 2>&1; then echo "PASS  $1"; else echo "FAIL  $1"; fails=$((fails+1)); fi; }
fails=0
chk "virtual environment in .venv"      "test -x '$d/.venv/bin/python'"
chk "requirements.txt is fully pinned"  "test -s '$d/requirements.txt' && ! grep -vqE '^(#|$|[A-Za-z0-9._-]+==[A-Za-z0-9._+!-]+)' '$d/requirements.txt'"
chk "environment matches requirements"  "test -z \"\$('$d/.venv/bin/python' -m pip freeze | diff - '$d/requirements.txt')\""
chk ".venv is ignored by Git"           "grep -qE '^/?\.venv/?$' '$d/.gitignore'"
chk "src package and tests folder"      "test -d '$d/tests' && ls '$d'/src/*/__init__.py"
exit $((fails>0))
