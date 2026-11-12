#!/bin/sh
# team checks: run before every push
for f in *.sh; do sh -n "$f" || { echo "FAIL syntax: $f"; exit 1; }; done
if grep -n '^<<<<<<<\|TO''DO' *.sh; then echo "FAIL leftover marker"; exit 1; fi
sh ./test.sh || exit 1
echo "checks passed"
