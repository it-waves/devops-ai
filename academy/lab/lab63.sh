#!/bin/sh
# lab63.sh : Git and GitHub, lesson 63 lab (restore, revert, reset, reflog). Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status        Needs git.
# Mission: four checks must say PASS.
D=/opt/lab63
U=${SUDO_USER:-root}
G="git -c safe.directory=* -c core.hooksPath=/dev/null"
down() { rm -rf $D; true; }
up() {
  down; mkdir -p $D/work; cd $D/work
  export GIT_AUTHOR_NAME="Team Bot" GIT_AUTHOR_EMAIL=bot@example.com GIT_COMMITTER_NAME="Team Bot" GIT_COMMITTER_EMAIL=bot@example.com
  d() { export GIT_AUTHOR_DATE="$1" GIT_COMMITTER_DATE="$1"; }
  $G init -q -b main .
  d 2026-01-05T10:00:00+0000; printf 'port=80\n' > app.conf; $G add app.conf; $G commit -q -m "Add app config"
  d 2026-01-06T10:00:00+0000; printf '#!/bin/sh\necho start\n' > start.sh; $G add start.sh; $G commit -q -m "Add start script"
  d 2026-01-07T10:00:00+0000; printf 'debug=true\n' >> app.conf; $G commit -q -am "Add debug flag"
  d 2026-01-08T10:00:00+0000; printf 'timeout=5\n' > limits.conf; $G add limits.conf; $G commit -q -m "Add timeout setting"
  # a commit that gets lost by a hard reset, but stays in the reflog
  d 2026-01-09T10:00:00+0000; printf 'retry=3\n' > retry.conf; $G add retry.conf; $G commit -q -m "Add retry setting"
  $G reset -q --hard HEAD~1
  # junk edit that was never committed
  echo 'echo JUNK' >> start.sh
  # remember the shared commit so the checker can prove history was not rewritten
  $G -C $D/work log --format=%H --grep='^Add debug flag$' -n1 > $D/.debug_sha
  chown -R $U $D 2>/dev/null
  cat <<MSG
Lab 63 is ready: your repository is $D/work. Something is messy:
  1. start.sh has a junk edit that was never committed: discard it, and leave the working folder clean
  2. a commit called "Add retry setting" was lost by a hard reset: find it in the reflog and bring it back
  3. the commit "Add debug flag" is already shared with the team and was a mistake: revert it (do not rewrite history)
  4. Write in $D/answers.txt (one line): how many commits main has now
Then run: lab check
Tip: if git asks who you are, run: git config --global user.name "Your Name" and git config --global user.email you@example.com
MSG
}
ok() { echo "PASS  $1"; P=$((P+1)); }
no() { echo "FAIL  $1"; }
check() {
  P=0; W=$D/work; [ -d $W/.git ] || { echo "Run: lab up"; exit 1; }
  if [ -z "$($G -C $W status --porcelain 2>/dev/null)" ] && ! grep -q JUNK $W/start.sh 2>/dev/null; then ok "1 start.sh is restored and the working folder is clean"; else no "1 start.sh is restored and the working folder is clean"; fi
  if $G -C $W log --format=%s main 2>/dev/null | grep -qx "Add retry setting" && [ "$(cat $W/retry.conf 2>/dev/null)" = "retry=3" ]; then ok "2 the lost commit Add retry setting is back"; else no "2 the lost commit Add retry setting is back"; fi
  S=$(cat $D/.debug_sha 2>/dev/null)
  if [ -n "$S" ] && $G -C $W merge-base --is-ancestor $S main 2>/dev/null && $G -C $W log --format=%s main | grep -q '^Revert "Add debug flag"' && ! grep -q 'debug=true' $W/app.conf 2>/dev/null; then ok "3 Add debug flag was reverted, and history was not rewritten"; else no "3 Add debug flag was reverted, and history was not rewritten"; fi
  N=$($G -C $W rev-list --count main 2>/dev/null)
  if [ "$(sed -n 1p $D/answers.txt 2>/dev/null)" = "$N" ] && [ "$N" = 6 ]; then ok "4 answers.txt: commits on main"; else no "4 answers.txt: commits on main"; fi
  [ $P = 4 ] && echo "ALL 4 PASS" || echo "$P of 4 pass"
}
case $1 in up) up;; check) check;; down) down;; status) [ -d $D ] && echo "lab63 is up" || echo "lab63 is down";; *) echo "usage: lab63.sh up|check|down|status";; esac
