#!/bin/sh
# a tiny security gate: fail the build if a password is written into the code
if grep -nE "PASSWORD *= *\"[^\"]+\"" src/*.py; then
  echo "[FAIL] secret found in code: move it to the environment"
  exit 1
fi
echo "[PASS] no secrets in code"
