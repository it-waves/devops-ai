#!/bin/sh
# lab65.sh : Git and GitHub, lesson 65 lab (team release workflow with automated checks). Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status        Needs git.
# Mission: five checks must say PASS.
D=/opt/lab65
U=${SUDO_USER:-root}
G="git -c safe.directory=* -c core.hooksPath=/dev/null"
down() { rm -rf $D; true; }
up() {
  down; mkdir -p $D; cd $D
  export GIT_AUTHOR_NAME="Team Bot" GIT_AUTHOR_EMAIL=bot@example.com GIT_COMMITTER_NAME="Team Bot" GIT_COMMITTER_EMAIL=bot@example.com
  $G init -q --bare -b main origin.git
  $G clone -q origin.git work 2>/dev/null; cd work
  mkdir -p .githooks
  printf '#!/bin/sh\necho "total: $(( $1 * $2 ))"\n' > shop.sh
  printf '#!/bin/sh\nout=$(sh ./shop.sh 3 4)\n[ "$out" = "total: 12" ] && echo "test ok" || { echo "test FAILED: got $out"; exit 1; }\n' > test.sh
  cat > check.sh <<'CHK'
#!/bin/sh
# team checks: run before every push
for f in *.sh; do sh -n "$f" || { echo "FAIL syntax: $f"; exit 1; }; done
if grep -n '^<<<<<<<\|TO''DO' *.sh; then echo "FAIL leftover marker"; exit 1; fi
sh ./test.sh || exit 1
echo "checks passed"
CHK
  printf '#!/bin/sh\n./check.sh || { echo "push blocked: fix the checks first"; exit 1; }\n' > .githooks/pre-push
  chmod +x *.sh .githooks/pre-push
  export GIT_AUTHOR_DATE=2026-01-05T10:00:00+0000 GIT_COMMITTER_DATE=2026-01-05T10:00:00+0000
  $G add -A; $G commit -q -m "Add shop script and checks"
  $G push -q origin main 2>/dev/null
  # a new change that broke the shop script (the bug): plus instead of times
  export GIT_AUTHOR_DATE=2026-01-06T10:00:00+0000 GIT_COMMITTER_DATE=2026-01-06T10:00:00+0000
  printf '#!/bin/sh\necho "total: $(( $1 + $2 ))"\n' > shop.sh
  $G commit -q -am "Speed up the total"
  chown -R $U $D 2>/dev/null
  cat <<MSG
Lab 65 is ready: your repository is $D/work, and the shared copy is $D/origin.git. The last commit broke the shop script, so the team checks fail.
  1. Run ./check.sh and read the failure, then fix the bug in shop.sh and commit the fix (a new commit)
  2. Turn on the team gate: git config core.hooksPath .githooks
  3. Push main to origin (the gate must let it through)
  4. Create an annotated tag v1.0.0 on that commit and push the tag to origin
  5. Write in $D/answers.txt (one line): which part of the version number you raise for a bug fix only: major, minor or patch
Then run: lab check
Tip: if git asks who you are, run: git config --global user.name "Your Name" and git config --global user.email you@example.com
MSG
}
ok() { echo "PASS  $1"; P=$((P+1)); }
no() { echo "FAIL  $1"; }
check() {
  P=0; W=$D/work; O=$D/origin.git; [ -d $W/.git ] || { echo "Run: lab up"; exit 1; }
  if (cd $W && sh ./check.sh >/dev/null 2>&1) && [ "$($G -C $W rev-list --count HEAD)" -ge 3 ]; then ok "1 the checks pass, with the bug fixed in a new commit"; else no "1 the checks pass, with the bug fixed in a new commit"; fi
  if [ "$(git -C $W config core.hooksPath 2>/dev/null)" = ".githooks" ]; then ok "2 the team gate is on (core.hooksPath is .githooks)"; else no "2 the team gate is on (core.hooksPath is .githooks)"; fi
  if [ "$($G -C $W rev-parse HEAD 2>/dev/null)" = "$($G -C $O rev-parse main 2>/dev/null)" ] && [ -z "$($G -C $W status --porcelain)" ] && (cd $W && sh ./check.sh >/dev/null 2>&1); then ok "3 main is pushed to origin and the tree is clean"; else no "3 main is pushed to origin and the tree is clean"; fi
  if [ "$($G -C $O cat-file -t refs/tags/v1.0.0 2>/dev/null)" = "tag" ] && [ "$($G -C $O rev-parse 'v1.0.0^{commit}' 2>/dev/null)" = "$($G -C $O rev-parse main 2>/dev/null)" ]; then ok "4 annotated tag v1.0.0 is on origin, on the pushed commit"; else no "4 annotated tag v1.0.0 is on origin, on the pushed commit"; fi
  if [ "$(sed -n 1p $D/answers.txt 2>/dev/null | tr 'A-Z' 'a-z' | tr -d ' ')" = "patch" ]; then ok "5 answers.txt: patch"; else no "5 answers.txt: patch"; fi
  [ $P = 5 ] && echo "ALL 5 PASS" || echo "$P of 5 pass"
}
case $1 in up) up;; check) check;; down) down;; status) [ -d $D ] && echo "lab65 is up" || echo "lab65 is down";; *) echo "usage: lab65.sh up|check|down|status";; esac
