#!/bin/sh
# usage: sh budget.sh SLO_PERCENT   e.g. 99.9
slo=$1
awk -F, -v slo=$slo 'NR>1 {t+=$2; f+=$3}
END {
  avail=100*(t-f)/t
  allowed=t*(100-slo)/100
  used=100*f/allowed
  printf "requests   %d\nfailed     %d\navailable  %.3f%%\n", t, f, avail
  printf "SLO        %s%%\nbudget     %d failures allowed\n", slo, allowed
  printf "used       %.0f%% of the budget\n", used
  if (used >= 100) print "[FREEZE] budget spent: reliability work first"
  else if (used >= 70) print "[CAREFUL] budget is low: ship small changes"
  else print "[SHIP] budget healthy: keep shipping"
}' data/requests.csv
