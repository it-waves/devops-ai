#!/bin/sh
# usage: ./layers.sh   asks each layer for one answer: the web page, then the API data
for p in "web 8080 /" "api 5000 /api/products"; do
  set -- $p
  printf '%-4s %s\n' $1 "$(curl -s -o /dev/null --max-time 3 -w '%{http_code}' localhost:$2$3)"
done
