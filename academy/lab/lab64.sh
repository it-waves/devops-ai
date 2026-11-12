#!/bin/sh
# lab64.sh : Git and GitHub, lesson 64 lab (secrets, credentials, access). Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status        Needs git, git-filter-repo (sudo apt install -y git-filter-repo) and ssh-keygen.
# Mission: four checks must say PASS.
D=/opt/lab64
U=${SUDO_USER:-root}
HD=${LAB64_HOME:-$(getent passwd $U | cut -d: -f6)}
G="git -c safe.directory=* -c core.hooksPath=/dev/null"
down() { rm -rf $D; rm -f $HD/.ssh/lab64_key $HD/.ssh/lab64_key.pub; true; }
up() {
  down; mkdir -p $D/work; cd $D/work
  export GIT_AUTHOR_NAME="Team Bot" GIT_AUTHOR_EMAIL=bot@example.com GIT_COMMITTER_NAME="Team Bot" GIT_COMMITTER_EMAIL=bot@example.com
  d() { export GIT_AUTHOR_DATE="$1" GIT_COMMITTER_DATE="$1"; }
  $G init -q -b main .
  d 2026-01-05T10:00:00+0000; printf 'port=80\n' > app.conf; $G add app.conf; $G commit -q -m "Add app config"
  d 2026-01-06T10:00:00+0000; printf 'DB_PASSWORD=demo-secret-9f3k\n' > .env; $G add .env; $G commit -q -m "Add database settings"
  d 2026-01-07T10:00:00+0000; printf '#!/bin/sh\necho healthy\n' > health.sh; $G add health.sh; $G commit -q -m "Add health script"
  chown -R $U $D 2>/dev/null
  cat <<MSG
Lab 64 is ready: your repository is $D/work. A fake password was committed by mistake (in a real case you would rotate it first).
  1. Stop tracking .env and list it in .gitignore (commit this)
  2. Rewrite the history so the secret is gone from every commit (git filter-repo --path .env --invert-paths --force)
  3. Make an ed25519 SSH key named lab64_key in ~/.ssh (ssh-keygen -t ed25519 -f ~/.ssh/lab64_key)
  4. Write in $D/answers.txt (one word): the first thing you do when a secret leaks
Then run: lab check
Tip: if git asks who you are, run: git config --global user.name "Your Name" and git config --global user.email you@example.com
MSG
}
ok() { echo "PASS  $1"; P=$((P+1)); }
no() { echo "FAIL  $1"; }
check() {
  P=0; W=$D/work; [ -d $W/.git ] || { echo "Run: lab up"; exit 1; }
  if grep -qx '.env' $W/.gitignore 2>/dev/null && [ -z "$($G -C $W ls-files .env 2>/dev/null)" ]; then ok "1 .env is ignored and no longer tracked"; else no "1 .env is ignored and no longer tracked"; fi
  if [ -z "$($G -C $W log --all -S demo-secret --oneline 2>/dev/null)" ] && $G -C $W log --format=%s 2>/dev/null | grep -qx "Add app config"; then ok "2 the secret is gone from every commit"; else no "2 the secret is gone from every commit"; fi
  K=$HD/.ssh/lab64_key
  if [ -f $K ] && [ -f $K.pub ] && ssh-keygen -l -f $K.pub 2>/dev/null | grep -q ED25519 && [ "$(stat -c %a $K)" = 600 ] && [ -z "$($G -C $W ls-files lab64_key 2>/dev/null)" ]; then ok "3 SSH key lab64_key: ed25519, private half protected"; else no "3 SSH key lab64_key: ed25519, private half protected"; fi
  A=$(sed -n 1p $D/answers.txt 2>/dev/null | tr 'A-Z' 'a-z' | tr -d ' ')
  if [ "$A" = rotate ]; then ok "4 answers.txt: rotate first"; else no "4 answers.txt: rotate first"; fi
  [ $P = 4 ] && echo "ALL 4 PASS" || echo "$P of 4 pass"
}
case $1 in up) up;; check) check;; down) down;; status) [ -d $D ] && echo "lab64 is up" || echo "lab64 is down";; *) echo "usage: lab64.sh up|check|down|status";; esac
