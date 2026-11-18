#!/bin/sh
# usage: sh metrics.sh FILE [WEEKS]   (the four key DevOps metrics)
f=${1:-deploys.csv}; w=${2:-4}
tail -n +2 "$f" | while IFS=, read id c d x r; do
  cs=$(date -d "$c" +%s); ds=$(date -d "$d" +%s)
  rs=0; [ -n "$r" ] && rs=$(date -d "$r" +%s)
  echo "$ds $((ds-cs)) $x $rs"
done | awk -v weeks=$w '
{ n++; lead+=$2
  if ($3=="yes") { bad++; rest+=($4-$1) } }
END {
  printf "deployments        %d in %d weeks\n", n, weeks
  printf "1 frequency        %.1f per week\n", n/weeks
  printf "2 lead time        %.1f hours (commit to live)\n", lead/n/3600
  printf "3 failure rate     %.0f%% (%d of %d)\n", 100*bad/n, bad, n
  if (bad>0) printf "4 time to restore  %.1f hours\n", rest/bad/3600
  else print "4 time to restore  none: no failures"
}'
