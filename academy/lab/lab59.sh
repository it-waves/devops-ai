#!/bin/sh
# lab59.sh : Git and GitHub, lesson 59 lab (branches, merging and conflicts). Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status        Needs git.
# Mission: four checks must say PASS.
D=/opt/lab59
U=${SUDO_USER:-root}
G="git -c safe.directory=* -c core.hooksPath=/dev/null"
down() { rm -rf $D; true; }
up() {
  down; mkdir -p $D/app; cd $D/app
  export GIT_AUTHOR_NAME="Team Bot" GIT_AUTHOR_EMAIL=bot@example.com GIT_COMMITTER_NAME="Team Bot" GIT_COMMITTER_EMAIL=bot@example.com
  $G init -q -b main .
  d() { export GIT_AUTHOR_DATE="$1" GIT_COMMITTER_DATE="$1"; }
  d 2026-01-05T10:00:00+0000; printf 'port=80\ntimeout=5\n' > app.conf; $G add app.conf; $G commit -q -m "Add app config"
  d 2026-01-06T10:00:00+0000; printf '# app\n' > README.md; $G add README.md; $G commit -q -m "Add readme"
  d 2026-01-07T10:00:00+0000; $G switch -q -c feature/logging; printf 'level=info\n' > logging.conf; $G add logging.conf; $G commit -q -m "Add logging config"
  d 2026-01-07T11:00:00+0000; $G switch -q main; $G switch -q -c feature/port; printf 'port=8080\ntimeout=5\n' > app.conf; $G commit -q -am "Use port 8080"
  d 2026-01-08T10:00:00+0000; $G switch -q main; printf 'port=9090\ntimeout=5\n' > app.conf; $G commit -q -am "Use port 9090"
  chown -R $U $D 2>/dev/null
  cat <<MSG
Lab 59 is ready: a repository in $D/app, on main, with two branches waiting: feature/logging (merges cleanly) and feature/port (conflicts with main on the port line).
  1. Merge feature/logging into main
  2. Merge feature/port into main, resolve the conflict by hand, and keep port=8080 (and timeout=5)
  3. Delete both merged branches
  4. Write in $D/answers.txt (one line): how many merge commits main has now
Then run: lab check
Tip: if git asks who you are, run: git config --global user.name "Your Name" and git config --global user.email you@example.com
MSG
}
ok() { echo "PASS  $1"; P=$((P+1)); }
no() { echo "FAIL  $1"; }
check() {
  P=0; W=$D/app; [ -d $W/.git ] || { echo "Run: lab up"; exit 1; }
  if [ -f $W/logging.conf ] && [ -n "$($G -C $W ls-files logging.conf)" ] && [ ! -f $W/.git/MERGE_HEAD ]; then ok "1 feature/logging is merged into main (logging.conf present)"; else no "1 feature/logging is merged into main (logging.conf present)"; fi
  A=$($G -C $W show HEAD:app.conf 2>/dev/null)
  if [ "$A" = "$(printf 'port=8080\ntimeout=5')" ] && [ ! -f $W/.git/MERGE_HEAD ] && [ -z "$($G -C $W status --porcelain --untracked-files=no)" ]; then ok "2 feature/port merged, conflict resolved, nothing left uncommitted"; else no "2 feature/port merged, conflict resolved, nothing left uncommitted"; fi
  B=$($G -C $W branch --format='%(refname:short)' 2>/dev/null | tr '\n' ' ')
  if [ "$B" = "main " ]; then ok "3 both feature branches deleted, only main remains"; else no "3 both feature branches deleted, only main remains"; fi
  M=$($G -C $W rev-list --merges --count HEAD 2>/dev/null)
  if [ "$(sed -n 1p $D/answers.txt 2>/dev/null)" = 2 ] && [ "$M" = 2 ]; then ok "4 answers.txt: merge commits on main"; else no "4 answers.txt: merge commits on main"; fi
  [ $P = 4 ] && echo "ALL 4 PASS" || echo "$P of 4 pass"
}
case $1 in up) up;; check) check;; down) down;; status) [ -d $D ] && echo "lab59 is up" || echo "lab59 is down";; *) echo "usage: lab59.sh up|check|down|status";; esac
