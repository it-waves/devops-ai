#!/bin/sh
# usage: sh plan.sh FILE   (checks an improvement plan: key=value lines)
f=${1:-plan_good.txt}
awk -F= '
{ v[$1]=$2 }
function ck(n, key, ok, why) { if (ok) printf "%d  %-10s ok\n", n, key; else { printf "%d  %-10s FIX: %s\n", n, key, why; bad++ } }
END {
  ck(1, "baseline",   v["baseline"]  ~ /[0-9]/,                          "write the number for today")
  ck(2, "bottleneck", length(v["bottleneck"]) > 5 && v["bottleneck"] ~ /[0-9]/, "name one step, with its number")
  ck(3, "change",     length(v["change"]) > 5 && v["change"] !~ / and /, "exactly one change")
  ck(4, "target",     v["target"] ~ /[0-9]/,                             "give a number and a date")
  ck(5, "measure",    length(v["measure"]) > 5,                          "say what you will measure")
  ck(6, "risk",       length(v["risk"]) > 5,                             "say what could go wrong")
  if (bad) printf "plan needs %d fix(es)\n", bad; else print "plan ready: one change, one number, one date"
}' "$f"
