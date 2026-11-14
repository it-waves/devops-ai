#!/bin/sh
# lab93.sh : schedule a REAL Nexus cleanup task (enrichment for MC10-O07): delete old snapshots from corp-snapshots in the Nexus web page. Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status
# Needs: a JDK, Maven, curl, python3 (sudo apt install -y openjdk-21-jdk-headless maven curl python3), internet access,
#        about 3 GB of free memory, 2 GB of free disk and about 5 minutes the first time (the Nexus download is about 525 MB).
# Mission: four snapshot builds pile up in corp-snapshots. In the Nexus web page create a Delete SNAPSHOT task that keeps only the newest build, run it, and schedule it.
D=${LAB92_DIR:-/opt/lab93}
U=${SUDO_USER:-root}
PORT=8081
NV=3.98.1-01
NURL=https://download.sonatype.com/nexus/3/nexus-$NV-linux-x86_64.tar.gz
NU=nexus93
NX=$D/.nx
stopnx() { pkill -u $NU java 2>/dev/null; sleep 3; true; }
down() { stopnx; rm -rf "${D:?}" ; id $NU >/dev/null 2>&1 && { sleep 2; userdel -f $NU 2>/dev/null; }; true; }
startnx() {
  curl -s -o /dev/null http://127.0.0.1:$PORT/service/rest/v1/status && return 0
  : > $NX/nexus.log; chown $NU:$NU $NX/nexus.log
  su $NU -c "cd $NX/nexus/bin && setsid nohup ./nexus run > $NX/nexus.log 2>&1 < /dev/null &"
  printf 'starting Nexus (about a minute) '
  for i in $(seq 1 90); do sleep 3; [ "$(curl -s -o /dev/null -w %{http_code} http://127.0.0.1:$PORT/service/rest/v1/status)" = 200 ] && { echo ok; return 0; }; printf '.'; done
  echo; echo "Nexus did not start: see $NX/nexus.log"; return 1
}
up() {
  for t in javac mvn curl python3; do command -v $t >/dev/null 2>&1 || { echo "$t not found: run  sudo apt install -y openjdk-21-jdk-headless maven curl python3"; exit 1; }; done
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  if [ "$ACCEPT_NEXUS_EULA" != yes ]; then
    echo "This lab installs Sonatype Nexus Repository Community Edition, which has its own license (the Community Edition End User License Agreement from Sonatype). Read it before you continue."
    printf 'Type yes to accept it for this practice machine: '; read ans </dev/tty 2>/dev/null; [ "$ans" = yes ] || { echo "not accepted: nothing was installed"; exit 1; }
  fi
  down; mkdir -p $NX
  id $NU >/dev/null 2>&1 || useradd -r -m -d $NX/nexus-home -s /bin/bash $NU
  echo "downloading Nexus $NV (about 525 MB) from download.sonatype.com ..."
  curl -fL --progress-bar -o $NX/nexus.tgz $NURL || { echo "download failed"; exit 1; }
  mkdir -p $NX/nexus.tmp && tar xzf $NX/nexus.tgz -C $NX/nexus.tmp && mv $NX/nexus.tmp/nexus-$NV $NX/nexus && mv $NX/nexus.tmp/sonatype-work $NX/sonatype-work && rm -rf "${NX:?}/nexus.tgz" "${NX:?}/nexus.tmp"
  mkdir -p $NX/sonatype-work/nexus3/etc
  printf 'application-port=%s\n' $PORT > $NX/sonatype-work/nexus3/etc/nexus.properties
  sed -i 's/^-Xms.*/-Xms1200m/; s/^-Xmx.*/-Xmx1200m/' $NX/nexus/bin/nexus.vmoptions
  chown -R $NU:$NU $NX/nexus $NX/sonatype-work; chmod 755 $D $NX
  startnx || exit 1
  # headless setup: your own admin password, licence accepted, anonymous access OFF (this is what makes the 401 real)
  for i in $(seq 1 40); do [ -f $NX/sonatype-work/nexus3/admin.password ] && break; sleep 3; done
  A=$(cat $NX/sonatype-work/nexus3/admin.password); P="corp-$(date +%s | sha256sum | cut -c1-12)"
  curl -s -o /dev/null -u admin:$A -X PUT -H 'Content-Type: text/plain' -d "$P" http://127.0.0.1:$PORT/service/rest/v1/security/users/admin/change-password
  curl -s -u admin:$P http://127.0.0.1:$PORT/service/rest/v1/system/eula > $D/eula.json
  python3 -c "import json;d=json.load(open('$D/eula.json'));d['accepted']=True;json.dump(d,open('$D/eula.json','w'))"
  curl -s -o /dev/null -u admin:$P -H 'Content-Type: application/json' -X POST -d @$D/eula.json http://127.0.0.1:$PORT/service/rest/v1/system/eula
  curl -s -o /dev/null -u admin:$P -H 'Content-Type: application/json' -X PUT -d '{"enabled":false,"userId":"anonymous","realmName":"NexusAuthorizingRealm"}' http://127.0.0.1:$PORT/service/rest/v1/security/anonymous
  rm -f $D/eula.json; printf '%s\n' "$P" > $D/pass.txt
  # corp-snapshots: a hosted Maven repository for SNAPSHOT versions (the same one you built by hand in lesson 91)
  curl -s -o /dev/null -u admin:$P -H 'Content-Type: application/json' -X POST -d '{"name":"corp-snapshots","online":true,"storage":{"blobStoreName":"default","strictContentTypeValidation":true,"writePolicy":"ALLOW"},"maven":{"versionPolicy":"SNAPSHOT","layoutPolicy":"STRICT","contentDisposition":"INLINE"}}' http://127.0.0.1:$PORT/service/rest/v1/repositories/maven/hosted
  # the project that keeps publishing snapshots
  p=$D/cart-core; mkdir -p $p/src/main/java/cloudcart
  cat > $p/pom.xml <<EOF_P
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.cloudcart</groupId>
  <artifactId>cart-core</artifactId>
  <version>1.0.0-SNAPSHOT</version>

  <properties>
    <maven.compiler.release>21</maven.compiler.release>
  </properties>

  <distributionManagement>
    <snapshotRepository>
      <id>corp</id>
      <url>http://localhost:$PORT/repository/corp-snapshots</url>
    </snapshotRepository>
  </distributionManagement>

  <build>
    <plugins>
      <plugin><artifactId>maven-clean-plugin</artifactId><version>3.2.0</version></plugin>
      <plugin><artifactId>maven-resources-plugin</artifactId><version>3.3.0</version></plugin>
      <plugin><artifactId>maven-compiler-plugin</artifactId><version>3.10.1</version></plugin>
      <plugin><artifactId>maven-surefire-plugin</artifactId><version>2.22.2</version></plugin>
      <plugin><artifactId>maven-jar-plugin</artifactId><version>3.3.0</version></plugin>
      <plugin><artifactId>maven-install-plugin</artifactId><version>3.1.1</version></plugin>
      <plugin><artifactId>maven-deploy-plugin</artifactId><version>3.1.1</version></plugin>
    </plugins>
  </build>
</project>
EOF_P
  printf 'package cloudcart;\n\npublic class Cart {\n    public static String banner() {\n        return "CloudCart";\n    }\n}\n' > $p/src/main/java/cloudcart/Cart.java
  cat > $p/settings.xml <<EOF_X
<settings>
  <servers>
    <server>
      <id>corp</id>
      <username>admin</username>
      <password>\${env.CORP_PASS}</password>
    </server>
  </servers>
</settings>
EOF_X
  chown -R $U $p; chmod 755 $D; chmod 600 $p/settings.xml; printf '%s\n' "$P" > $D/pass.txt; chown $U $D/pass.txt; chmod 600 $D/pass.txt
  as() { if [ "$U" = root ]; then "$@"; else runuser -u $U -- env HOME=$(getent passwd $U | cut -d: -f6) "$@"; fi; }
  echo "publishing four snapshot builds (about a minute) ..."
  for n in 1 2 3 4; do ( cd $p && as env CORP_PASS=$P mvn -B -q -s settings.xml deploy > $D/deploy$n.log 2>&1 ) || { echo "deploy $n failed: see $D/deploy$n.log"; exit 1; }; sleep 2; done
  cat > $D/TASKS.txt <<'EOF_K'
LAB 93 : stop snapshots piling up.   Real Nexus: http://localhost:8081   user admin, password in /opt/lab93/pass.txt
The repository corp-snapshots already holds FOUR builds of cart-core (look in Browse). Nobody needs the old ones.
Do the work in the Nexus web page:  Settings (gear)  >  System  >  Tasks  >  Create task.
(First visit? The welcome wizard may appear: Next through it and keep anonymous access disabled. If the screen looks different, use Switch to Classic UI.)

1  Create a task of type  Maven - Delete SNAPSHOT  for the repository corp-snapshots.
   Keep 1 snapshot (minimum snapshot count 1) and set the retention to 0 days so that the older builds qualify today.
2  Run it by hand (Run, then Yes). Its Last result must say Ok, and Browse must show ONE build left (the newest).
3  Schedule it: frequency Daily (or Weekly) at a quiet hour, not Manual.
4  In /opt/lab93/notes.txt write two lines:
     keep: how many builds your task keeps and why that number is safe for a real team (use the word snapshot)
     when: when it runs and why you chose that time (use the word retention or the word schedule)
Then:  lab check     (all 5 must pass)       and later:  lab down      (the cleanup task is removed with the lab)
EOF_K
  chown $U $D/TASKS.txt
  echo "lab93 ready: cd $D   (task list: $D/TASKS.txt)"
}
check() {
  [ -d $D/cart-core ] || { echo "lab not set up: run  lab up"; exit 1; }
  startnx || exit 1
  ok=0; PW=$(cat $D/pass.txt)
  pass() { echo "PASS  $1"; ok=$((ok+1)); }
  fail() { echo "FAIL  $1"; }
  T=$(curl -s -u admin:$PW http://127.0.0.1:$PORT/service/rest/v1/tasks | python3 -c "
import sys, json
for t in json.load(sys.stdin)['items']:
    if t['type'] == 'repository.maven.remove-snapshots': print(t['id'], t.get('lastRunResult') or '-', t.get('nextRun') or '-', t.get('lastRun') or '-', t.get('schedule') or '-', 'corp-snapshots' in (t.get('message') or '')); break")
  set -- $T
  if [ -n "$1" ] && [ "$6" = True ]; then pass "1 a Maven - Delete SNAPSHOT task exists and it works on corp-snapshots"; else fail "1 a Maven - Delete SNAPSHOT task exists and it works on corp-snapshots (Settings > System > Tasks > Create task)"; fi
  if [ "$2" = OK ] && [ "$4" != - ]; then pass "2 the task ran and its last result is Ok"; else fail "2 the task ran and its last result is Ok (select it, press Run, then Yes)"; fi
  J=$(curl -s -u admin:$PW "http://127.0.0.1:$PORT/service/rest/v1/search/assets?repository=corp-snapshots&maven.extension=jar" | python3 -c "
import sys, json
r = json.load(sys.stdin)['items']; print(len(r), r[0]['path'].rsplit('-', 1)[-1] if r else '')")
  if [ "${J%% *}" = 1 ] && [ "${J#* }" = 4.jar ]; then pass "3 exactly one build is left in corp-snapshots, and it is the newest (build 4)"; else fail "3 exactly one build is left in corp-snapshots, and it is the newest (found: ${J%% *} jar)"; fi
  if [ -n "$1" ] && [ "$5" != manual ] && [ "$5" != - ] && [ "$3" != - ]; then pass "4 the task is scheduled ($5, next run set)"; else fail "4 the task is scheduled (change the frequency from Manual to Daily or Weekly)"; fi
  g() { sed -n "$1p" $D/notes.txt 2>/dev/null | tr 'A-Z' 'a-z'; }
  if [ -f $D/notes.txt ] && g 1 | grep -q '^keep:' && g 1 | grep -q 'snapshot' && g 2 | grep -q '^when:' && g 2 | grep -qE 'retention|schedule'; then pass "5 notes.txt answers keep: and when:"; else fail "5 notes.txt answers keep: and when: (two lines, see TASKS.txt)"; fi
  echo "$ok/5 checks passed"; [ $ok -eq 5 ]
}
status() { [ -d $D ] && echo "lab93 is set up in $D" || echo "lab93 is not set up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab93 removed";; status) status;; *) echo "usage: lab93.sh up|check|down|status"; exit 2;; esac
