#!/bin/sh
# build once: package the code into one artifact and record its fingerprint
mkdir -p artifacts
date +%s%N > src/BUILDINFO
tar -cf artifacts/shop-1.4.0.tar -C src .
sha256sum artifacts/shop-1.4.0.tar | cut -d' ' -f1 > artifacts/shop-1.4.0.sha256
echo "built shop-1.4.0.tar"
echo "fingerprint $(cut -c1-12 artifacts/shop-1.4.0.sha256)"
