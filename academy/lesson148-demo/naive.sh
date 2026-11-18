#!/bin/sh
# the mistake: rebuild for every environment
for env in dev test prod; do
  sh build.sh | tail -1 | sed "s/^/$env  /"
done
