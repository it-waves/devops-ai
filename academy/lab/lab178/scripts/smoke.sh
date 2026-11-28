#!/bin/sh
# smoke test: is the application really working? usage: smoke.sh PORT VERSION
PORT=$1; VERSION=$2; FAIL=0
check() { if [ "$2" = "$3" ]; then echo "PASS  $1"; else echo "FAIL  $1 (got $3, expected $2)"; FAIL=1; fi; }
check "health reports $VERSION" "$VERSION" "$(curl -s localhost:$PORT/cloudcart/health | sed -n 's/.*"version":"\([^"]*\)".*/\1/p')"
check "home page answers 200" 200 "$(curl -s -o /dev/null -w '%{http_code}' localhost:$PORT/cloudcart/)"
check "product list answers 200" 200 "$(curl -s -o /dev/null -w '%{http_code}' localhost:$PORT/cloudcart/api/products)"
exit $FAIL
