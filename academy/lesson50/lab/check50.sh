#!/bin/bash
# Lesson 50 checker: bash check50.sh [FOLDER]   (folder holds fetch.py and api06.py; starts the lab API on port 8099 and stops it again)
d=${1:-.}; cd "$d" || exit 2
python3 api06.py 8099 >/dev/null 2>&1 & api=$!
trap 'kill $api 2>/dev/null' EXIT
sleep 1
export API_URL=http://127.0.0.1:8099
chk() { if eval "$2" >/dev/null 2>&1; then echo "PASS  $1"; else echo "FAIL  $1"; fails=$((fails+1)); fi; }
fails=0
chk "prints the expected summary (all pages)" "test \"\$(API_TOKEN=lab-token-123 timeout 30 python3 fetch.py)\" = \"\$(printf 'servers: 10\nstopped: web-05, web-10')\""
chk "missing token: clear message, exit not 0" "out=\$(env -u API_TOKEN timeout 30 python3 fetch.py 2>&1); rc=\$?; test \$rc -ne 0 && echo \"\$out\" | grep -q API_TOKEN"
chk "wrong token: stops with an error, exit not 0" "API_TOKEN=wrong timeout 30 python3 fetch.py"'; test $? -ne 0'
chk "timeout on the call, status checked" "grep -q 'timeout=' fetch.py && grep -q raise_for_status fetch.py"
exit $((fails>0))
