#!/bin/sh
# lab57.sh : Git and GitHub, lesson 57 mastery lab (distributed version control and repository anatomy).
#   up | check | down | status      Run with sudo, in your own Ubuntu virtual machine. Needs git.
# Mission: clone a repository, add one commit of your own, and prove what Git stored. Four checks must say PASS.
D=/opt/lab57
U=${SUDO_USER:-root}
G="git -c safe.directory=* -c core.hooksPath=/dev/null"
down() { rm -rf $D; true; }
up() {
  down
  mkdir -p $D/work $D/seed
  export GIT_AUTHOR_NAME="Team Bot" GIT_AUTHOR_EMAIL=bot@example.com GIT_COMMITTER_NAME="Team Bot" GIT_COMMITTER_EMAIL=bot@example.com
  export GIT_AUTHOR_DATE="2026-01-05T10:00:00+0000" GIT_COMMITTER_DATE="2026-01-05T10:00:00+0000"
  $G init -q -b main --bare $D/origin.git
  $G init -q -b main $D/seed
  echo "ports: 80 443" > $D/seed/team.txt
  $G -C $D/seed add team.txt; $G -C $D/seed commit -q -m "Add team ports list"
  $G -C $D/seed -c push.negotiate=false push -q $D/origin.git main
  rm -rf $D/seed
  chown -R $U $D 2>/dev/null
  cat <<MSG
Lab 57 is ready. The shared repository is $D/origin.git
Your work folder is $D/work
  1. Clone origin.git into $D/work/team
  2. Inside the clone, create notes.txt and make one commit of your own
  3. Write two lines in $D/work/answers.txt:
       line 1: the first 7 characters of the ROOT commit hash
       line 2: how many commits your clone has now
Then run: lab check
MSG
}
ok() { echo "PASS  $1"; P=$((P+1)); }
no() { echo "FAIL  $1"; }
check() {
  P=0; W=$D/work/team; O=$D/origin.git
  [ -d $D ] || { echo "Run: lab up"; exit 1; }
  if [ -d $W/.git ] && [ "$($G -C $W remote get-url origin 2>/dev/null)" = "$O" ]; then ok "1 clone of origin.git exists, with origin set"; else no "1 clone of origin.git exists, with origin set"; fi
  if [ -d $W/.git ] && [ "$($G -C $W rev-list --count HEAD 2>/dev/null)" = 2 ] && [ -n "$($G -C $W log -1 --format=%P 2>/dev/null)" ] && [ -f $W/notes.txt ]; then ok "2 your commit sits on top of the root commit"; else no "2 your commit sits on top of the root commit"; fi
  if [ "$($G -C $O rev-list --count main 2>/dev/null)" = 1 ]; then ok "3 origin still has 1 commit: nothing is pushed yet"; else no "3 origin still has 1 commit: nothing is pushed yet"; fi
  R=$($G -C $W rev-list --max-parents=0 HEAD 2>/dev/null | cut -c1-7)
  if [ -n "$R" ] && [ "$(sed -n 1p $D/work/answers.txt 2>/dev/null)" = "$R" ] && [ "$(sed -n 2p $D/work/answers.txt 2>/dev/null)" = 2 ]; then ok "4 answers.txt: root hash and commit count"; else no "4 answers.txt: root hash and commit count"; fi
  [ $P = 4 ] && echo "ALL 4 PASS" || echo "$P of 4 pass"
}
case $1 in up) up;; check) check;; down) down;; status) [ -d $D ] && echo "lab57 is up" || echo "lab57 is down";; *) echo "usage: lab57.sh up|check|down|status";; esac
