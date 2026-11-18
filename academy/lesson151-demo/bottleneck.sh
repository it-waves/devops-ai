#!/bin/sh
# usage: sh bottleneck.sh FILE   (hours of work and of waiting, per stage)
f=${1:-stages.csv}
awk -F, 'NR>1 { t=$2+$3; w+=$2; q+=$3; tot+=t
  name[NR]=$1; hrs[NR]=t; if (t>max) { max=t; slow=$1 } n=NR }
END {
  for (i=2; i<=n; i++) { bar=""; for (k=0; k<hrs[i]; k++) bar=bar "#"; printf "%-9s %5.1f h  %s\n", name[i], hrs[i], bar }
  printf "total     %5.1f h  (work %.1f, waiting %.1f)\n", tot, w, q
  printf "slowest   %s (%.1f h, %.0f%% of the time)\n", slow, max, 100*max/tot
  printf "flow efficiency %.0f%% (work / total)\n", 100*w/tot
}' "$f"
