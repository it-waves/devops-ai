# the code way: make the server match desired/, change only what differs
mkdir -p server
for f in $(ls desired); do
  if cmp -s desired/$f server/$f; then
    echo "[ok]      $f"
  else
    cp desired/$f server/$f
    echo "[changed] $f"
  fi
done
