#!/bin/sh
# lab91.sh : publish snapshot and release artifacts to a REAL repository manager, Sonatype Nexus Repository Community Edition (MC10-O07).
#   up | check | down | status        Run with sudo, in your own Ubuntu virtual machine.
# Needs: a JDK, Maven, curl, python3 (sudo apt install -y openjdk-21-jdk-headless maven curl python3), internet access,
#        about 3 GB of free memory, 2 GB of free disk and about 5 minutes the first time (the Nexus download is about 525 MB).
# Mission: set up Nexus in its web page, create a snapshot and a release repository, publish to both, see the refusal to overwrite a release, read the proof in the web page.
D=${LAB91_DIR:-/opt/lab91}
U=${SUDO_USER:-root}
PORT=8081
NV=3.98.1-01
NURL=https://download.sonatype.com/nexus/3/nexus-$NV-linux-x86_64.tar.gz
NU=nexus91
stopnx() { pkill -u $NU -f 'nexus' 2>/dev/null; pkill -u $NU java 2>/dev/null; sleep 3; true; }
down() { stopnx; rm -rf $D /tmp/lab91-chk; id $NU >/dev/null 2>&1 && userdel $NU 2>/dev/null; true; }
startnx() {
  curl -s -o /dev/null http://127.0.0.1:$PORT/service/rest/v1/status && return 0
  : > $D/nexus.log; chown $NU:$NU $D/nexus.log
  su $NU -c "cd $D/nexus/bin && setsid nohup ./nexus run > $D/nexus.log 2>&1 < /dev/null &"
  printf 'starting Nexus (about a minute) '
  for i in $(seq 1 90); do sleep 3; [ "$(curl -s -o /dev/null -w %{http_code} http://127.0.0.1:$PORT/service/rest/v1/status)" = 200 ] && { echo ok; return 0; }; printf '.'; done
  echo; echo "Nexus did not start: see $D/nexus.log"; return 1
}
up() {
  for t in javac mvn curl python3; do command -v $t >/dev/null 2>&1 || { echo "$t not found: run  sudo apt install -y openjdk-21-jdk-headless maven curl python3"; exit 1; }; done
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  down; mkdir -p $D/shop/src/main/java/cloudcart
  id $NU >/dev/null 2>&1 || useradd -r -m -d $D/nexus-home -s /bin/bash $NU
  if [ ! -f $D/nexus/bin/nexus ]; then
    echo "downloading Nexus $NV (about 525 MB) from download.sonatype.com ..."
    curl -fL --progress-bar -o $D/nexus.tgz $NURL || { echo "download failed"; exit 1; }
    mkdir -p $D/nexus.tmp && tar xzf $D/nexus.tgz -C $D/nexus.tmp && mv $D/nexus.tmp/nexus-$NV $D/nexus && mv $D/nexus.tmp/sonatype-work $D/sonatype-work && rm -rf $D/nexus.tgz $D/nexus.tmp
  fi
  mkdir -p $D/sonatype-work/nexus3/etc
  printf 'application-port=%s\n' $PORT > $D/sonatype-work/nexus3/etc/nexus.properties
  sed -i 's/^-Xms.*/-Xms1200m/; s/^-Xmx.*/-Xmx1200m/' $D/nexus/bin/nexus.vmoptions
  chown -R $NU:$NU $D/nexus $D/sonatype-work; chmod 755 $D
  cat > $D/shop/pom.xml <<EOF_P
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
    <repository>
      <id>corp</id>
      <url>http://localhost:$PORT/repository/corp-releases</url>
    </repository>
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
  cat > $D/shop/src/main/java/cloudcart/Cart.java <<'EOF_G'
package cloudcart;

public class Cart {
    public static String banner() {
        return "cloudcart";
    }
}
EOF_G
  cat > $D/shop/settings.xml <<'EOF_X'
<settings>
  <servers>
    <server>
      <id>corp</id>
      <username>admin</username>
      <password>${env.NEXUS_PASS}</password>
    </server>
  </servers>
</settings>
EOF_X
  chmod 600 $D/shop/settings.xml
  cat > $D/TASKS.txt <<'EOF_K'
LAB 91 : publish cart-core to a real repository manager, Sonatype Nexus Repository.   Work in /opt/lab91/shop

Web page: http://localhost:8081     user: admin
The first time, the password is in:   /opt/lab91/sonatype-work/nexus3/admin.password
Then Nexus asks you to choose your own password (write it down). Finish its setup wizard.
After that, in every terminal:   export NEXUS_PASS='your own password'
Always:                           mvn -B -s settings.xml ...      (the login is already in settings.xml)

0  Setup.         Sign in, set your own password, accept the licence, finish the wizard.
1  Repositories.  Settings (the gear), Repository, Repositories, Create repository, maven2 (hosted), twice:
                    name corp-snapshots   Version policy Snapshot   Deployment policy Allow redeploy
                    name corp-releases    Version policy Release    Deployment policy Disable redeploy
2  Snapshot.      Deploy 1.0.0-SNAPSHOT:   mvn -B -s settings.xml deploy      (find it in the web page: Browse, corp-snapshots)
3  Release.       Change the version in pom.xml to 1.0.0 (no SNAPSHOT) and deploy it.
4  Again.         Deploy 1.0.0 a second time. It must fail. Save the error line:
                    mvn -B -s settings.xml deploy 2>&1 | grep -o 'status code.*' > conflict.txt
                  Then in the web page open Browse, corp-releases, the jar, and write its SHA-1 checksum into sha1.txt.
5  Next + why.    Change the version to 1.0.1 and deploy it. Write one sentence in why.txt about why a release is never
                  published twice. It must contain the word  release  and one of  immutable, reproducible, overwrite, changed.

Then:  lab check     (all 5 must pass)       and later:  lab down
(lab check needs your password: the shortcut keeps NEXUS_PASS for it.)
EOF_K
  chown -R $U $D/shop $D/TASKS.txt 2>/dev/null
  startnx || exit 1
  echo "lab91 ready: cd $D/shop   (task list: $D/TASKS.txt)"
  echo "open http://localhost:$PORT   user admin   first password: $(cat $D/sonatype-work/nexus3/admin.password 2>/dev/null)"
}
check() {
  [ -d $D/shop ] || { echo "lab not set up: run  lab up"; exit 1; }
  startnx || exit 1
  [ -n "$NEXUS_PASS" ] || { echo "set NEXUS_PASS first:  export NEXUS_PASS='your own password'   (use the shortcut:  source shortcuts91.sh ; lab check)"; exit 1; }
  cd $D/shop; ok=0
  pass() { echo "PASS  $1"; ok=$((ok+1)); }
  fail() { echo "FAIL  $1"; }
  api() { curl -s -u "admin:$NEXUS_PASS" "http://127.0.0.1:$PORT$1"; }
  api /service/rest/v1/status/check >/dev/null
  R=$(api /service/rest/v1/repositories)
  if echo "$R" | python3 -c "
import json,sys
try: r={x['name']:x for x in json.load(sys.stdin)}
except Exception: sys.exit(1)
a=r.get('corp-snapshots');b=r.get('corp-releases')
sys.exit(0 if a and b and a['format']=='maven2' and a['type']=='hosted' and b['type']=='hosted' else 1)" 2>/dev/null && \
     api /service/rest/v1/repositories/maven/hosted/corp-snapshots | python3 -c "
import json,sys
d=json.load(sys.stdin);sys.exit(0 if d['maven']['versionPolicy']=='SNAPSHOT' and d['storage']['writePolicy']=='ALLOW' else 1)" 2>/dev/null && \
     api /service/rest/v1/repositories/maven/hosted/corp-releases | python3 -c "
import json,sys
d=json.load(sys.stdin);sys.exit(0 if d['maven']['versionPolicy']=='RELEASE' and d['storage']['writePolicy']=='ALLOW_ONCE' else 1)" 2>/dev/null; then pass "1 repositories corp-snapshots and corp-releases exist with the right version and deployment policy"; else fail "1 repositories corp-snapshots and corp-releases exist with the right version and deployment policy"; fi
  assets() { api "/service/rest/v1/search/assets?repository=$1&maven.artifactId=cart-core&maven.extension=jar&maven.baseVersion=$2"; }
  S1=$(assets corp-snapshots 1.0.0-SNAPSHOT); R0=$(assets corp-releases 1.0.0); R1=$(assets corp-releases 1.0.1)
  has() { echo "$1" | python3 -c "import json,sys;sys.exit(0 if json.load(sys.stdin)['items'] else 1)" 2>/dev/null; }
  if has "$S1" && has "$R0"; then pass "2 a snapshot of 1.0.0 and the release 1.0.0 are in Nexus"; else fail "2 a snapshot of 1.0.0 and the release 1.0.0 are in Nexus"; fi
  SHA=$(echo "$R0" | python3 -c "import json,sys;print(json.load(sys.stdin)['items'][0]['checksum']['sha1'])" 2>/dev/null)
  if [ -f conflict.txt ] && grep -q '409' conflict.txt && grep -qi 'redeploy is not allowed' conflict.txt && [ -n "$SHA" ] && [ -f sha1.txt ] && grep -qi "$SHA" sha1.txt; then pass "3 the redeploy was refused (conflict.txt) and sha1.txt has the SHA-1 of the release jar"; else fail "3 the redeploy was refused (conflict.txt) and sha1.txt has the SHA-1 of the release jar"; fi
  if has "$R1" && grep -q '<version>1.0.1</version>' pom.xml; then pass "4 release 1.0.1 is published and the pom says 1.0.1"; else fail "4 release 1.0.1 is published and the pom says 1.0.1"; fi
  if [ -f why.txt ] && grep -qi 'release' why.txt && grep -qiE 'immutable|reproducible|overwrite|changed' why.txt; then pass "5 why.txt explains release immutability"; else fail "5 why.txt explains release immutability"; fi
  echo "$ok/5 checks passed"; [ $ok -eq 5 ]
}
status() { [ -d $D ] && echo "lab91 is set up in $D" || echo "lab91 is not set up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab91 removed";; status) status;; *) echo "usage: lab91.sh up|check|down|status"; exit 2;; esac
