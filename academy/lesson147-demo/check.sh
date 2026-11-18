# drift check: does the server still match the code?
bad=0
for f in $(ls desired); do
  cmp -s desired/$f server/$f || { echo "[DRIFT]  $f differs from code"; bad=1; }
done
[ $bad = 0 ] && echo "[clean]  no drift"
exit $bad
