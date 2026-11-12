#!/bin/bash
# Lesson 49 checker: bash check49.sh [FOLDER]   (folder holds report.py, servers49.csv, config49.yaml; works in a temporary copy)
d=${1:-.}; cd "$d" || exit 2
t=$(mktemp -d); trap 'rm -rf "$t"' EXIT
cp report.py servers49.csv config49.yaml "$t"/
chk() { if eval "$2" >/dev/null 2>&1; then echo "PASS  $1"; else echo "FAIL  $1"; fails=$((fails+1)); fi; }
fails=0
chk "report.py runs and writes report.json" "cd $t && rm -f report.json && APP_ENV=prod python3 report.py && test -s report.json"
chk "report.json has the right content" "cd $t && APP_ENV=prod python3 report.py && python3 -c \"import json; assert json.load(open('report.json')) == {'env': 'prod', 'limit': 80, 'count': 4, 'busy': ['web2']}\""
chk "APP_ENV defaults to dev" "cd $t && env -u APP_ENV python3 report.py && python3 -c \"import json; assert json.load(open('report.json'))['env'] == 'dev'\""
chk "the limit comes from config49.yaml" "cd $t && sed -i 's/^limit: .*/limit: 60/' config49.yaml && python3 report.py && python3 -c \"import json; r = json.load(open('report.json')); assert r['limit'] == 60 and r['busy'] == ['web1', 'web2']\""
exit $((fails>0))
