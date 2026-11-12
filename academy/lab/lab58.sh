#!/bin/sh
# lab58.sh : Git and GitHub, lesson 58 lab (staging, history and ignore files). Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status        Needs git.
# Mission: four checks must say PASS.
D=/opt/lab58
U=${SUDO_USER:-root}
G="git -c safe.directory=* -c core.hooksPath=/dev/null"
down() { rm -rf $D; true; }
up() {
  down; mkdir -p $D/app; cd $D/app
  export GIT_AUTHOR_NAME="Team Bot" GIT_AUTHOR_EMAIL=bot@example.com GIT_COMMITTER_NAME="Team Bot" GIT_COMMITTER_EMAIL=bot@example.com
  $G init -q -b main .
  d() { export GIT_AUTHOR_DATE="$1" GIT_COMMITTER_DATE="$1"; }
  d 2026-01-05T10:00:00+0000; printf 'port=80\n' > app.conf; $G add app.conf; $G commit -q -m "Add app config"
  d 2026-01-06T10:00:00+0000; printf 'x\n' > cache.tmp; printf '# app\n' > README.md; $G add cache.tmp README.md; $G commit -q -m "Add readme and a cache file"
  d 2026-01-07T10:00:00+0000; printf 'port=80\ntimeout=5\n' > app.conf; $G add app.conf; $G commit -q -m "Raise timeout"
  printf 'port=8080\ntimeout=5\n' > app.conf          # your real change, not yet staged
  printf 'remember: update the docs\n' > notes.txt     # a personal note, NOT for this commit
  printf 'debug line\n' > debug.log; printf 'TOKEN=abc\n' > secrets.env; mkdir build; printf 'bin\n' > build/out.bin
  printf 'changed\n' >> cache.tmp
  chown -R $U $D 2>/dev/null
  cat <<MSG
Lab 58 is ready: a repository in $D/app with a real change to app.conf, a personal notes.txt, junk files, and a cache.tmp that was committed by mistake.
  1. Create .gitignore so debug.log, secrets.env and the build folder are ignored
  2. Stop tracking cache.tmp, but keep the file on disk
  3. Commit ONLY the app.conf change, with a clear message. notes.txt must stay uncommitted
  4. Write in $D/answers.txt (one line): how many commits touched app.conf BEFORE yours
Then run: lab check
MSG
}
ok() { echo "PASS  $1"; P=$((P+1)); }
no() { echo "FAIL  $1"; }
check() {
  P=0; W=$D/app; [ -d $W/.git ] || { echo "Run: lab up"; exit 1; }
  if [ -n "$($G -C $W check-ignore debug.log secrets.env build/out.bin 2>/dev/null | head -1)" ] && [ "$($G -C $W check-ignore debug.log secrets.env build/out.bin 2>/dev/null | wc -l)" = 3 ]; then ok "1 .gitignore covers debug.log, secrets.env, build/"; else no "1 .gitignore covers debug.log, secrets.env, build/"; fi
  if [ -f $W/cache.tmp ] && [ -z "$($G -C $W ls-files cache.tmp)" ]; then ok "2 cache.tmp untracked, file kept on disk"; else no "2 cache.tmp untracked, file kept on disk"; fi
  F=$($G -C $W show --name-only --format= HEAD 2>/dev/null | sort | tr '\n' ' ')
  N=$($G -C $W rev-list --count HEAD 2>/dev/null); S=$($G -C $W log -1 --format=%s 2>/dev/null)
  if [ "$N" -ge 4 ] 2>/dev/null && echo "$F" | grep -q "app.conf" && ! echo "$F" | grep -q "notes.txt\|secrets.env\|debug.log" && [ ${#S} -ge 8 ] && [ -f $W/notes.txt ] && [ -z "$($G -C $W ls-files notes.txt)" ]; then ok "3 your commit has only app.conf; notes.txt left out"; else no "3 your commit has only app.conf; notes.txt left out"; fi
  if [ "$(sed -n 1p $D/answers.txt 2>/dev/null)" = 2 ]; then ok "4 answers.txt: commits that touched app.conf before yours"; else no "4 answers.txt: commits that touched app.conf before yours"; fi
  [ $P = 4 ] && echo "ALL 4 PASS" || echo "$P of 4 pass"
}
case $1 in up) up;; check) check;; down) down;; status) [ -d $D ] && echo "lab58 is up" || echo "lab58 is down";; *) echo "usage: lab58.sh up|check|down|status";; esac
