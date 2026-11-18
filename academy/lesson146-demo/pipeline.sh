#!/bin/sh
# usage: sh pipeline.sh ci | delivery [approve] | deployment
mode=$1
echo "[build]   compile src"
python3 -m py_compile src/shop.py || exit 1
cd src && python3 check.py || { echo "[stop]    tests failed, nothing released"; exit 1; }
cd ..
echo "[package] build release.tgz"
tar czf release.tgz src/shop.py
if [ "$mode" = ci ]; then echo "[done]    CI: integrated, built and tested"; exit 0; fi
if [ "$mode" = delivery ] && [ "$2" != approve ]; then
  echo "[ready]   deployable. Waiting for a human."; exit 0
fi
mkdir -p prod; n=$(ls prod | wc -l); n=$((n + 1))
cp release.tgz prod/release-$n.tgz
echo "[deploy]  prod now runs release $n"
