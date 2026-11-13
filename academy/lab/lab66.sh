#!/bin/sh
# lab66.sh : Git and GitHub mastery lab (MC07). Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status        Needs git.
# Mission: four checks must say PASS.
D=/opt/lab66
U=${SUDO_USER:-root}
G="git -c safe.directory=* -c core.hooksPath=/dev/null"
down() { rm -rf $D; true; }
up() {
  down; mkdir -p $D; cd $D
  export GIT_AUTHOR_NAME="Team Bot" GIT_AUTHOR_EMAIL=bot@example.com GIT_COMMITTER_NAME="Team Bot" GIT_COMMITTER_EMAIL=bot@example.com
  d() { export GIT_AUTHOR_DATE="$1" GIT_COMMITTER_DATE="$1"; }
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
  printf 'price=10\n' > price.txt
  chmod +x *.sh .githooks/pre-push
  d 2026-01-05T10:00:00+0000; $G add -A; $G commit -q -m "Add shop script and checks"; $G push -q origin main 2>/dev/null
  $G checkout -q -b feature/discount
  d 2026-01-06T10:00:00+0000; printf 'price=10\ndiscount=5\n' > price.txt; $G commit -q -am "Add discount"
  $G checkout -q main
  d 2026-01-07T10:00:00+0000; printf 'price=12\n' > price.txt; $G commit -q -am "Raise the price to 12"
  d 2026-01-08T10:00:00+0000; printf '#!/bin/sh\n# TODO remove the debug line\necho deploying\n' > deploy.sh; chmod +x deploy.sh; $G add deploy.sh; $G commit -q -m "Add deploy script"
  d 2026-01-09T10:00:00+0000; printf 'url=https://api.example.com\n' > api.conf; printf 'API_KEY=demo-secret-4f9a\n' > .env; $G add -A; $G commit -q -m "Add API settings"
  chown -R $U $D 2>/dev/null
  cat <<MSG
Lab 66 is ready: your repository is $D/work, and the shared copy is $D/origin.git. Four things need your work:
  1. A secret (.env) was committed by mistake in the last commit: take it out of history and make Git ignore it, but keep the commit Add API settings
  2. The branch feature/discount must be merged into main (expect a conflict in price.txt: keep both the new price and the discount)
  3. The team checks fail: run ./check.sh, fix what it says, and turn on the gate (git config core.hooksPath .githooks)
  4. Push main to origin, then tag it with an annotated tag v1.0.0 and push the tag
Then run: lab check
Tip: if git asks who you are, run: git config --global user.name "Your Name" and git config --global user.email you@example.com
MSG
}
ok() { echo "PASS  $1"; P=$((P+1)); }
no() { echo "FAIL  $1"; }
check() {
  P=0; W=$D/work; O=$D/origin.git; [ -d $W/.git ] || { echo "Run: lab up"; exit 1; }
  if [ -z "$($G -C $W log --all -S demo-secret --oneline 2>/dev/null)" ] && grep -qx '.env' $W/.gitignore 2>/dev/null && ! $G -C $W ls-files --error-unmatch .env >/dev/null 2>&1 && $G -C $W log --format=%s main | grep -qx "Add API settings" && [ -f $W/api.conf ]; then ok "1 the secret is gone from history, .env is ignored, Add API settings is kept"; else no "1 the secret is gone from history, .env is ignored, Add API settings is kept"; fi
  if $G -C $W merge-base --is-ancestor feature/discount main 2>/dev/null && [ -n "$($G -C $W rev-list --merges main 2>/dev/null | head -n1)" ] && grep -qx 'price=12' $W/price.txt 2>/dev/null && grep -qx 'discount=5' $W/price.txt 2>/dev/null && ! $G -C $W grep -q '^<<<<<<<' 2>/dev/null; then ok "2 feature/discount is merged, and price.txt keeps both changes"; else no "2 feature/discount is merged, and price.txt keeps both changes"; fi
  if (cd $W && sh ./check.sh >/dev/null 2>&1) && [ "$(git -C $W config core.hooksPath 2>/dev/null)" = ".githooks" ]; then ok "3 the team checks pass and the gate is on"; else no "3 the team checks pass and the gate is on"; fi
  if [ "$($G -C $W rev-parse HEAD 2>/dev/null)" = "$($G -C $O rev-parse main 2>/dev/null)" ] && [ -z "$($G -C $W status --porcelain)" ] && [ "$($G -C $O cat-file -t refs/tags/v1.0.0 2>/dev/null)" = "tag" ] && [ "$($G -C $O rev-parse 'v1.0.0^{commit}' 2>/dev/null)" = "$($G -C $O rev-parse main 2>/dev/null)" ]; then ok "4 main and the annotated tag v1.0.0 are on origin"; else no "4 main and the annotated tag v1.0.0 are on origin"; fi
  [ $P = 4 ] && echo "ALL 4 PASS" || echo "$P of 4 pass"
}
case $1 in up) up;; check) check;; down) down;; status) [ -d $D ] && echo "lab66 is up" || echo "lab66 is down";; *) echo "usage: lab66.sh up|check|down|status";; esac
