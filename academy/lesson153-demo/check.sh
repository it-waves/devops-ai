#!/bin/sh
# usage: sh check.sh   (checks report.txt, plan.txt and your cleanup against the data)
m=$(sh metrics.sh shop_deploys.csv 2); b=$(sh bottleneck.sh shop_stages.csv)
get() { sed -n "s/^$1=//p" report.txt | head -1; }
n=0; bad=0
ok() { n=$((n+1)); if [ "$2" = yes ]; then printf "%d  %-22s ok\n" $n "$1"; else printf "%d  %-22s FIX: %s\n" $n "$1" "$3"; bad=$((bad+1)); fi; }
chk() { [ "$(get $2)" = "$3" ] && r=yes || r=no; ok "$1" $r "$2 should be $3"; }
chk "frequency"   frequency "$(echo "$m" | sed -n 's/^1 frequency *\([0-9.]*\) .*/\1/p')"
chk "lead time"   lead      "$(echo "$m" | sed -n 's/^2 lead time *\([0-9.]*\) .*/\1/p')"
chk "failure rate" failure  "$(echo "$m" | sed -n 's/^3 failure rate *\([0-9]*\)%.*/\1/p')"
chk "time to restore" restore "$(echo "$m" | sed -n 's/^4 time to restore *\([0-9.]*\) .*/\1/p')"
chk "bottleneck"  bottleneck "$(echo "$b" | sed -n 's/^slowest *\([a-z]*\) .*/\1/p')"
chk "flow efficiency" flow  "$(echo "$b" | sed -n 's/^flow efficiency \([0-9]*\)%.*/\1/p')"
sh plan.sh plan.txt 2>/dev/null | grep -q 'plan ready' && r=yes || r=no; ok "plan.txt" $r "run sh plan.sh plan.txt"
get found | grep -q 'd07' && r=yes || r=no; ok "troubleshooting note" $r "found= should name the bad row"
[ ! -d scratch ] && r=yes || r=no; ok "cleanup" $r "remove the scratch folder"
if [ $bad -eq 0 ]; then echo "mastery evidence complete"; else echo "$bad to fix"; fi
