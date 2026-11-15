#!/bin/sh
# lab114.sh : CloudCart v0, lesson 2: the project layout and the Maven build. Run with sudo, on any Linux machine with a JDK, Maven, curl and unzip.
#   up | check | down | status
# Needs: sudo apt install -y openjdk-21-jdk-headless maven curl unzip     internet (Maven Central, about 25 MB the first time), about 1 GB of memory.
# Mission: build the real CloudCart WAR with Maven, bump its version to 0.2.1, and answer four questions about what is inside the WAR.
D=${LAB114_DIR:-/opt/lab114}
OWNER=${SUDO_USER:-root}
SRC_URL=${LAB114_SRC_URL:-https://raw.githubusercontent.com/it-waves/devops-ai/main/academy/lab/assets/cloudcart-src-0.2.0.tgz}
P=$D/cloudcart
W=$P/target/cloudcart.war
down() { rm -rf "${D:?}"; true; }
up() {
  for t in java mvn curl unzip tar; do command -v $t >/dev/null 2>&1 || { echo "$t not found: run  sudo apt install -y openjdk-21-jdk-headless maven curl unzip"; exit 1; }; done
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  down; mkdir -p $D
  echo "downloading the CloudCart source (about 25 KB) ..."
  curl -fL --progress-bar -o $D/src.tgz "$SRC_URL" || { echo "download failed"; exit 1; }
  tar xzf $D/src.tgz -C $D || { echo "unpack failed"; exit 1; }; rm -f $D/src.tgz
  cat > $D/TASKS.txt <<'EOF_T'
LAB 114  CloudCart v0: the project layout and the Maven build
Open a terminal in /opt/lab114/cloudcart. You need Maven and a JDK.

1  Look at the project:  ls, and  find src -type f  (find the pom.xml, the servlet, the web.xml)
2  Build it as it is:  mvn package        (it compiles, runs the tests, and packs the WAR)
3  Bump the version: edit pom.xml (vim) so the project version is 0.2.1, then build again
4  Open the WAR without Tomcat:  unzip -l target/cloudcart.war   and  unzip -p target/cloudcart.war WEB-INF/classes/version.properties
5  Write answers.txt (in /opt/lab114) with exactly four lines:
      tests: ...        how many tests Maven ran (the surefire summary line)
      lib: ...          the one jar inside WEB-INF/lib
      provided: ...     the dependency that Tomcat supplies, so it is NOT inside the WAR
      built: ...        the builtAt value inside the WAR
6  lab check   (judges you: 5 lines, you need all 5 PASS)
7  lab down    (removes everything)
EOF_T
  : > $D/answers.txt
  chown -R $OWNER $D 2>/dev/null; chmod -R a+rX $D
  echo "lab 114 ready in $D. Read TASKS.txt, then open the project."
}
pass=0; total=5
ok() { pass=$((pass+1)); echo "  PASS  $1"; }
no() { echo "  FAIL  $1"; }
ans() { sed -n "s/^$1: *//p" $D/answers.txt | head -n 1 | tr -d '\r' | sed 's/ *$//'; }
check() {
  [ -d $P ] || { echo "lab is not up: run  lab up"; exit 1; }
  if [ -f $W ] && unzip -tq $W >/dev/null 2>&1; then ok "1 target/cloudcart.war exists and is a valid WAR"; else no "1 no valid target/cloudcart.war: run  mvn package  in $P"; fi
  v=$(unzip -p $W WEB-INF/classes/version.properties 2>/dev/null | sed -n 's/^version=//p' | tr -d '\r')
  if [ "$v" = 0.2.1 ] && grep -q '<version>0.2.1</version>' $P/pom.xml; then ok "2 pom.xml and the WAR say version 0.2.1"; else no "2 the WAR says version '${v:-none}': set 0.2.1 in pom.xml, then build again"; fi
  t=0; for f in $P/target/surefire-reports/*.txt; do [ -f "$f" ] || continue; n=$(sed -n 's/^Tests run: \([0-9]*\),.*/\1/p' "$f" | head -n 1); t=$((t+${n:-0})); done
  if [ "$t" -gt 0 ] && [ "$(ans tests)" = "$t" ]; then ok "3 tests: $t matches the surefire reports"; else no "3 tests: answers.txt does not match what Maven ran"; fi
  lib=$(unzip -Z1 $W 2>/dev/null | sed -n 's#^WEB-INF/lib/##p' | grep . | tr '\n' ' ' | sed 's/ *$//')
  if [ -n "$lib" ] && [ "$(ans lib)" = "$lib" ] && [ "$(ans provided)" = jakarta.servlet-api ] && ! unzip -Z1 $W 2>/dev/null | grep -q servlet-api; then ok "4 lib and provided are right"; else no "4 lib or provided is wrong: look inside the WAR, and at the scope in pom.xml"; fi
  b=$(unzip -p $W WEB-INF/classes/version.properties 2>/dev/null | sed -n 's/^builtAt=//p' | tr -d '\r')
  if [ -n "$b" ] && [ "$(ans built)" = "$b" ]; then ok "5 built matches the builtAt inside the WAR"; else no "5 built: copy builtAt from the WAR, not from the clock"; fi
  echo; echo "$pass / $total passed"; [ $pass -eq $total ]
}
status() { [ -d $D ] && echo "lab 114 is up in $D" || echo "lab 114 is not up"; }
case "$1" in up) up ;; check) check ;; down) down; echo "lab 114 removed" ;; status) status ;; *) echo "usage: lab114.sh up|check|down|status" ;; esac
