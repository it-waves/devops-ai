#!/bin/sh
# usage: sh promote.sh ENV   (same artifact, that environment's own config)
env=$1
art=artifacts/shop-1.4.0.tar
want=$(cat artifacts/shop-1.4.0.sha256)
have=$(sha256sum $art | cut -d' ' -f1)
if [ "$want" != "$have" ]; then echo "[STOP] artifact changed, not promoting"; exit 1; fi
rm -rf envs/$env; mkdir -p envs/$env
tar -xf $art -C envs/$env
echo "[ok] $env gets fingerprint $(echo $have | cut -c1-12)"
python3 envs/$env/app.py $env config/$env.conf
