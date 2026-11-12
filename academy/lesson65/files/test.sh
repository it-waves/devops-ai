#!/bin/sh
out=$(sh ./shop.sh 3 4)
[ "$out" = "total: 12" ] && echo "test ok" || { echo "test FAILED: got $out"; exit 1; }
