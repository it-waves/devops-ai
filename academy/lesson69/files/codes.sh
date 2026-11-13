#!/bin/sh
# a tiny API client: print the status code of each endpoint
for p in /api/products /api/products/1 /api/products/99 /api/fast; do
  printf '%s  %s\n' "$(curl -s -o /dev/null -w '%{http_code}' localhost:5000$p)" "$p"
done
