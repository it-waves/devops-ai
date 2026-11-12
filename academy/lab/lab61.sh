#!/bin/sh
# lab61.sh : Git and GitHub, lesson 61 lab (remotes, fetch, pull, push, tags). Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status        Needs git.
# Mission: four checks must say PASS.
D=/opt/lab61
U=${SUDO_USER:-root}
G="git -c safe.directory=* -c core.hooksPath=/dev/null"
down() { rm -rf $D; true; }
up() {
  down; mkdir -p $D/seed; cd $D/seed
  export GIT_AUTHOR_NAME="Team Bot" GIT_AUTHOR_EMAIL=bot@example.com GIT_COMMITTER_NAME="Team Bot" GIT_COMMITTER_EMAIL=bot@example.com
  d() { export GIT_AUTHOR_DATE="$1" GIT_COMMITTER_DATE="$1"; }
  $G init -q -b main .
  d 2026-01-05T10:00:00+0000; printf 'port=80\n' > app.conf; $G add app.conf; $G commit -q -m "Add app config"
  d 2026-01-06T10:00:00+0000; printf '# app\n' > README.md; $G add README.md; $G commit -q -m "Add readme"
  cd $D; $G clone -q --bare seed origin.git; $G clone -q origin.git work
  # a teammate pushes while you are away
  cd $D/seed; $G remote add origin $D/origin.git; $G fetch -q origin
  d 2026-01-07T12:00:00+0000; printf 'timeout=5\n' >> app.conf; export GIT_AUTHOR_NAME="Alex Kim" GIT_COMMITTER_NAME="Alex Kim"; $G commit -q -am "Add timeout setting"; $G push -q origin main
  rm -rf $D/seed
  chown -R $U $D 2>/dev/null
  cat <<MSG
Lab 61 is ready: the shared repository is $D/origin.git and your clone is $D/work. While you were away, a teammate pushed a commit that you do not have yet.
  1. In $D/work create release-notes.txt with one line of text, and commit it
  2. Push it. Git will reject the push: pull your teammate's work first (use a rebase), then push again
  3. Create an annotated tag v1.0 and push it to origin
  4. Write in $D/answers.txt (one line): how many commits origin main has now
Then run: lab check
Tip: if git asks who you are, run: git config --global user.name "Your Name" and git config --global user.email you@example.com
MSG
}
ok() { echo "PASS  $1"; P=$((P+1)); }
no() { echo "FAIL  $1"; }
check() {
  P=0; O=$D/origin.git; [ -d $O ] || { echo "Run: lab up"; exit 1; }
  if $G -C $O ls-tree -r main --name-only 2>/dev/null | grep -qx release-notes.txt; then ok "1 release-notes.txt is on origin main"; else no "1 release-notes.txt is on origin main"; fi
  M=$($G -C $O rev-list --merges --count main 2>/dev/null); N=$($G -C $O rev-list --count main 2>/dev/null)
  if [ "$M" = 0 ] && [ "$N" = 4 ] && $G -C $O log main --format=%s | grep -qx "Add timeout setting"; then ok "2 origin history is a straight line with your teammate's commit and yours"; else no "2 origin history is a straight line with your teammate's commit and yours"; fi
  if [ "$($G -C $O cat-file -t refs/tags/v1.0 2>/dev/null)" = tag ]; then ok "3 annotated tag v1.0 is on origin"; else no "3 annotated tag v1.0 is on origin"; fi
  if [ "$(sed -n 1p $D/answers.txt 2>/dev/null)" = 4 ]; then ok "4 answers.txt: commits on origin main"; else no "4 answers.txt: commits on origin main"; fi
  [ $P = 4 ] && echo "ALL 4 PASS" || echo "$P of 4 pass"
}
case $1 in up) up;; check) check;; down) down;; status) [ -d $D ] && echo "lab61 is up" || echo "lab61 is down";; *) echo "usage: lab61.sh up|check|down|status";; esac
