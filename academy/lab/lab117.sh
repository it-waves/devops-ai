#!/bin/sh
# lab117.sh : CloudCart v0, lesson 5 (mastery): prove v0 from a clean clone. Run with sudo, on any Linux machine with a JDK, Maven, git, curl and ss.
#   up | check | down | status
# Needs: sudo apt install -y openjdk-21-jdk-headless maven git curl unzip iproute2     internet (Tomcat 14 MB, Maven Central the first time), about 1 GB of memory, ports 8089 and 8099 free.
# Mission: clone the project fresh, build it, deploy the WAR you built, verify it like a customer, tag the commit cloudcart-v0, and write the evidence.
D=${LAB117_DIR:-/opt/lab117}
OWNER=${SUDO_USER:-root}
if [ "$OWNER" = root ]; then RU=""; else RU="runuser -u $OWNER --"; fi
TV=10.1.34
TB=${LAB117_TOMCAT_BASE:-https://archive.apache.org/dist/tomcat/tomcat-10/v$TV/bin}
SRC_URL=${LAB117_SRC_URL:-https://raw.githubusercontent.com/it-waves/devops-ai/main/academy/lab/assets/cloudcart-src-0.2.0.tgz}
F=apache-tomcat-$TV.tar.gz
B=localhost:8089
O=$D/origin.git
W=$D/work
war=$W/target/cloudcart.war
down() {
  pkill -f "catalina.base=$D/tomcat" 2>/dev/null; sleep 1
  rm -rf "${D:?}"; true
}
up() {
  for t in java mvn git curl tar ss unzip; do command -v $t >/dev/null 2>&1 || { echo "$t not found: run  sudo apt install -y openjdk-21-jdk-headless maven git curl unzip iproute2"; exit 1; }; done
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  for p in 8089 8099; do if curl -s -o /dev/null -m 2 localhost:$p; then echo "port $p is already in use: stop what uses it first"; exit 1; fi; done
  down; mkdir -p $D
  echo "downloading Tomcat $TV (about 14 MB) ..."
  curl -fL --progress-bar -o $D/t.tgz "$TB/$F" || { echo "download failed"; exit 1; }
  mkdir -p $D/tomcat && tar xzf $D/t.tgz -C $D/tomcat --strip-components=1 || { echo "unpack failed"; exit 1; }; rm -f $D/t.tgz
  T=$D/tomcat
  sed -i 's#<Connector port="8080"#<Connector port="8089"#; s#<Server port="8005"#<Server port="8099"#' $T/conf/server.xml
  rm -rf $T/webapps/docs $T/webapps/examples $T/webapps/host-manager $T/webapps/manager $T/webapps/ROOT
  printf '%s\n' 'CATALINA_PID=$CATALINA_BASE/tomcat.pid' > $T/bin/setenv.sh; chmod 755 $T/bin/setenv.sh
  echo "downloading the CloudCart source (about 25 KB) ..."
  curl -fL --progress-bar -o $D/src.tgz "$SRC_URL" || { echo "source download failed"; exit 1; }
  mkdir -p $D/seed && tar xzf $D/src.tgz -C $D/seed || { echo "unpack failed"; exit 1; }; rm -f $D/src.tgz
  chown -R $OWNER $D 2>/dev/null
  # the project's "origin": a bare repository holding one commit on main (a stand-in for the team repository)
  ( cd $D/seed/cloudcart && $RU git init -q -b main && $RU git add -A && $RU git -c user.name=CloudCart -c user.email=team@cloudcart.test commit -q -m "CloudCart v0" ) || { echo "git setup failed"; exit 1; }
  $RU git clone -q --bare $D/seed/cloudcart $O || { echo "git setup failed"; exit 1; }
  rm -rf $D/seed
  cat > $D/TASKS.txt <<'EOF_T'
LAB 117  CloudCart v0: prove it from a clean clone  (mastery)
Open a terminal in /opt/lab117. The team repository is  origin.git  (a local copy of the project repository).

1  Clone it fresh into a folder called work:      git clone origin.git work       then  cd work  and  git status
2  Build it:      mvn -q package        (compiles, runs the tests, packs target/cloudcart.war)
3  Deploy the WAR you just built:  cp target/cloudcart.war ../tomcat/webapps/cloudcart.war   then  ../tomcat/bin/startup.sh
4  Verify like a customer:   curl -s localhost:8089/cloudcart/health   and count the products at /cloudcart/api/products
5  Tag the commit you built and publish the tag:    git tag cloudcart-v0       git push origin cloudcart-v0
6  Write evidence.txt (in /opt/lab117) with exactly four lines:
      commit: ...      the first 7 characters of the commit you built   (git rev-parse --short HEAD)
      tests: ...       how many tests Maven ran (the surefire summary lines, added up)
      sha: ...         the first 12 characters of the sha256 of target/cloudcart.war   (sha256sum)
      version: ...     the version the running app reports at /cloudcart/health
7  lab check   (judges you: you need all 5 PASS)
8  lab down    (stops Tomcat and removes everything)
If something does not answer, work the incident method from lesson 116: symptom, evidence, cause, fix, proof.
EOF_T
  : > $D/evidence.txt
  chown -R $OWNER $D 2>/dev/null; chmod -R a+rX $D
  echo "lab 117 ready in $D. Read TASKS.txt, then clone the project."
}
pass=0; total=5
ok() { pass=$((pass+1)); echo "  PASS  $1"; }
no() { echo "  FAIL  $1"; }
ev() { sed -n "s/^$1: *//p" $D/evidence.txt | head -n 1 | tr -d '\r' | sed 's/ *$//'; }
g() { gd=$1; shift; git -c safe.directory='*' -C "$gd" "$@" 2>/dev/null; }
check() {
  [ -d $O ] || { echo "lab is not up: run  lab up"; exit 1; }
  head=$(g $O rev-parse main)
  if [ -d $W/.git ] && [ "$(g $W rev-parse HEAD)" = "$head" ] && [ -z "$(g $W status --porcelain)" ] && [ "$(g $W remote get-url origin)" = "$O" ]; then ok "1 work is a clean clone of origin.git, at its latest commit"; else no "1 work is not a clean clone of origin.git: run  git clone origin.git work"; fi
  t=0; for f in $W/target/surefire-reports/*.txt; do [ -f "$f" ] || continue; n=$(sed -n 's/^Tests run: \([0-9]*\),.*/\1/p' "$f" | head -n 1); t=$((t+${n:-0})); done
  if [ -f $war ] && unzip -tq $war >/dev/null 2>&1 && [ "$t" -gt 0 ]; then ok "2 the clone was built: a valid WAR and $t tests ran"; else no "2 no built WAR with test reports in work/target: run  mvn -q package  inside work"; fi
  dep=$D/tomcat/webapps/cloudcart.war
  h=$(curl -s -m 5 $B/cloudcart/health 2>/dev/null)
  if [ -f $war ] && [ -f $dep ] && cmp -s $war $dep && echo "$h" | grep -q '"status":"UP"'; then ok "3 Tomcat is running the WAR you built, and health is UP"; else no "3 the running app is not the WAR you built: copy target/cloudcart.war into tomcat/webapps and start Tomcat"; fi
  if [ -n "$head" ] && [ "$(g $O rev-parse cloudcart-v0^{commit})" = "$head" ]; then ok "4 origin has the tag cloudcart-v0 on the built commit"; else no "4 origin has no tag cloudcart-v0 on the built commit: git tag, then git push origin cloudcart-v0"; fi
  ver=$(echo "$h" | sed -n 's/.*"version":"\([^"]*\)".*/\1/p')
  sha=$(sha256sum $war 2>/dev/null | cut -c1-12)
  if [ -n "$head" ] && [ "$(ev commit)" = "$(echo $head | cut -c1-7)" ] && [ "$(ev tests)" = "$t" ] && [ -n "$sha" ] && [ "$(ev sha)" = "$sha" ] && [ -n "$ver" ] && [ "$(ev version)" = "$ver" ]; then ok "5 evidence.txt matches commit, tests, WAR and version"; else no "5 evidence.txt does not match: copy the values from git, Maven, sha256sum and the health page"; fi
  echo; echo "$pass / $total passed"; [ $pass -eq $total ]
}
status() { [ -d $D ] && echo "lab 117 is up in $D" || echo "lab 117 is not up"; }
case "$1" in up) up ;; check) check ;; down) down; echo "lab 117 removed" ;; status) status ;; *) echo "usage: lab117.sh up|check|down|status" ;; esac
