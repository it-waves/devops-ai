#!/bin/sh
# lab60.sh : Git and GitHub, lesson 60 lab (amend and rebase). Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status        Needs git.
# Mission: four checks must say PASS.
D=/opt/lab60
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
  d 2026-01-07T10:00:00+0000; $G switch -q -c feature; printf '#!/bin/sh\necho ok\n' > health.sh; $G add health.sh; $G commit -q -m "Add health check"
  d 2026-01-07T11:00:00+0000; printf '#!/bin/sh\necho healthy\n' > health.sh; $G commit -q -am "wip"
  d 2026-01-08T10:00:00+0000; $G switch -q main; printf '# Changes\n' > CHANGELOG.md; $G add CHANGELOG.md; $G commit -q -m "Add changelog"
  $G switch -q feature
  chown -R $U $D 2>/dev/null
  cat <<MSG
Lab 60 is ready: a repository in $D/app. You are on the feature branch, which diverged from main. Its last commit says "wip".
  1. On feature, amend the last commit to a clear message (not "wip")
  2. Rebase feature onto main
  3. Switch to main and merge feature, so main gets all the work with NO merge commit
  4. Write in $D/answers.txt (one line): how many commits main has now
Then run: lab check
Tip: if git asks who you are, run: git config --global user.name "Your Name" and git config --global user.email you@example.com
MSG
}
ok() { echo "PASS  $1"; P=$((P+1)); }
no() { echo "FAIL  $1"; }
check() {
  P=0; W=$D/app; [ -d $W/.git ] || { echo "Run: lab up"; exit 1; }
  S=$($G -C $W log -1 --format=%s main 2>/dev/null)
  if [ ${#S} -ge 8 ] && [ "$S" != "wip" ] && [ "$S" != "Add changelog" ]; then ok "1 last commit on main has a clear message (not wip)"; else no "1 last commit on main has a clear message (not wip)"; fi
  M=$($G -C $W rev-list --merges --count main 2>/dev/null); N=$($G -C $W rev-list --count main 2>/dev/null)
  if [ "$M" = 0 ] && [ "$N" = 5 ] && [ ! -d $W/.git/rebase-merge ] && [ ! -d $W/.git/rebase-apply ]; then ok "2 history is a straight line: no merge commit, 5 commits kept"; else no "2 history is a straight line: no merge commit, 5 commits kept"; fi
  if [ -n "$($G -C $W ls-tree -r main --name-only 2>/dev/null | grep -x health.sh)" ] && [ -n "$($G -C $W ls-tree -r main --name-only | grep -x CHANGELOG.md)" ] && [ "$($G -C $W rev-parse main 2>/dev/null)" = "$($G -C $W rev-parse feature 2>/dev/null)" ]; then ok "3 main has the feature work and the changelog"; else no "3 main has the feature work and the changelog"; fi
  if [ "$(sed -n 1p $D/answers.txt 2>/dev/null)" = 5 ]; then ok "4 answers.txt: commits on main"; else no "4 answers.txt: commits on main"; fi
  [ $P = 4 ] && echo "ALL 4 PASS" || echo "$P of 4 pass"
}
case $1 in up) up;; check) check;; down) down;; status) [ -d $D ] && echo "lab60 is up" || echo "lab60 is down";; *) echo "usage: lab60.sh up|check|down|status";; esac
