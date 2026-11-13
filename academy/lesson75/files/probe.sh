#!/bin/sh
# usage: ./probe.sh [port]   asks the two probe questions an orchestrator asks: is it alive, is it ready
P=${1:-5000}
for e in healthz readyz; do
  r=$(curl -s -w '\n%{http_code}' localhost:$P/$e)
  printf '%-8s %s  %s\n' $e "$(echo "$r" | tail -1)" "$(echo "$r" | head -1)"
done
