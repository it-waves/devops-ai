#!/bin/sh
# lab94.sh : MC10 mastery scenario: ship cart-core to a REAL Nexus (build, fix, make reproducible, publish, report). Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status
# Needs: a JDK, Maven, curl, python3 (sudo apt install -y openjdk-21-jdk-headless maven curl python3), internet access,
#        about 3 GB of free memory, 2 GB of free disk and about 5 minutes the first time (the Nexus download is about 525 MB).
# Mission: cart-core must be shipped as a snapshot to your company Nexus. It has hidden problems: fix them with what you learned in MC10, publish, and write the report.
D=${LAB94_DIR:-/opt/lab94}
U=${SUDO_USER:-root}
PORT=8081
NV=3.98.1-01
NURL=https://download.sonatype.com/nexus/3/nexus-$NV-linux-x86_64.tar.gz
NU=nexus94
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
  # the project to ship (it has three planted problems)
  p=$D/cart-core; mkdir -p $p/src/main/java/cloudcart $p/src/test/java/cloudcart
  cat > $p/pom.xml <<EOF_P
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.cloudcart</groupId>
  <artifactId>cart-core</artifactId>
  <version>1.0.0-SNAPSHOT</version>

  <properties>
    <maven.compiler.release>21</maven.compiler.release>
  </properties>

  <dependencies>
    <dependency>
      <groupId>org.apache.commons</groupId>
      <artifactId>commons-lang3</artifactId>
      <version>3.4</version>
    </dependency>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>4.13.2</version>
      <scope>test</scope>
    </dependency>
  </dependencies>

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
  printf 'package cloudcart;\n\nimport org.apache.commons.lang3.StringUtils;\n\npublic class Cart {\n    public static String shortName(String name) {\n        return StringUtils.truncate(name, 4);\n    }\n}\n' > $p/src/main/java/cloudcart/Cart.java
  printf 'package cloudcart;\n\nimport static org.junit.Assert.assertEquals;\nimport org.junit.Test;\n\npublic class CartTest {\n    @Test\n    public void shortNameKeepsFiveLetters() {\n        assertEquals("Cloud", Cart.shortName("CloudCart"));\n    }\n}\n' > $p/src/test/java/cloudcart/CartTest.java
  sha1sum $p/src/test/java/cloudcart/CartTest.java | cut -d' ' -f1 > $D/.testsum
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
  cat > $D/TASKS.txt <<'EOF_K'
LAB 94 : MC10 mastery.   Ship cart-core as a snapshot to your company Nexus.   Work in /opt/lab94/cart-core
Real Nexus: http://localhost:8081   user admin, password in /opt/lab94/pass.txt     First:  export CORP_PASS=$(cat /opt/lab94/pass.txt)

1  Build it:  mvn -B clean package.  It does not compile. Read the first ERROR, find the cause, fix the cause
   (keep the dependency, use a real version of it that has the method).
2  A test fails. Fix the CODE. Do NOT edit the test and do NOT skip tests.
3  Make the build reproducible: two builds, a few seconds apart, must give a jar with the SAME sha256sum.
   (Set the output timestamp as a property in the pom.)
4  Publish:  mvn -B -s settings.xml clean deploy.  The jar must appear in corp-snapshots (look in Browse, or the search API).
   The password stays in the environment variable, never in a file.
5  Write /opt/lab94/report.txt, three lines:
     result:  what you published and where
     trouble: the problems you found and how you fixed them (use the words version and timestamp)
     cleanup: how you remove everything when you are done (use the words lab down)
Then:  lab check     (all 5 must pass)       and later:  lab down
EOF_K
  chown $U $D/TASKS.txt
  echo "lab94 ready: cd $D/cart-core   (task list: $D/TASKS.txt)"
}
check() {
  [ -d $D/cart-core ] || { echo "lab not set up: run  lab up"; exit 1; }
  startnx || exit 1
  ok=0; PW=$(cat $D/pass.txt)
  as() { if [ "$U" = root ]; then "$@"; else runuser -u $U -- env HOME=$(getent passwd $U | cut -d: -f6) "$@"; fi; }
  pass() { echo "PASS  $1"; ok=$((ok+1)); }
  fail() { echo "FAIL  $1"; }
  W=/tmp/lab94-chk; rm -rf "${W:?}"; mkdir -p $W; chmod 777 $W
  bld() { # name goal... : copy the project, build it with its own empty local repository
    n=$1; shift; cp -r $D/cart-core $W/$n; rm -rf "${W:?}/$n/target"; chown -R $U $W/$n 2>/dev/null
    ( cd $W/$n && as mvn -B -Dmaven.repo.local=$W/repo "$@" > $W/$n.log 2>&1 )
  }
  if grep -q 'commons-lang3' $D/cart-core/pom.xml && ! grep -qE '<version>3\.4(\.0)?</version>' $D/cart-core/pom.xml && bld c clean compile; then pass "1 it compiles: the dependency is kept and its version is fixed"; else fail "1 it compiles: keep commons-lang3 and use a version that has the method (read the first ERROR)"; fi
  T=$(sha1sum $D/cart-core/src/test/java/cloudcart/CartTest.java | cut -d' ' -f1)
  if [ "$T" = "$(cat $D/.testsum)" ] && ! grep -rqiE 'skipTests|maven.test.skip|testFailureIgnore' $D/cart-core/pom.xml $D/cart-core/.mvn 2>/dev/null && bld t clean package && grep -q 'Tests run: 1, Failures: 0' $W/t.log; then pass "2 the test passes because the code is fixed (test untouched, not skipped)"; else fail "2 the test passes because the code is fixed (do not edit or skip the test)"; fi
  if grep -q 'project.build.outputTimestamp' $D/cart-core/pom.xml && bld r1 clean package && sleep 3 && bld r2 clean package && [ "$(sha256sum $W/r1/target/cart-core-1.0.0-SNAPSHOT.jar | cut -d' ' -f1)" = "$(sha256sum $W/r2/target/cart-core-1.0.0-SNAPSHOT.jar | cut -d' ' -f1)" ]; then pass "3 two builds give the same sha256: the build is reproducible"; else fail "3 two builds give the same sha256 (set project.build.outputTimestamp in the pom)"; fi
  J=$(curl -s -u admin:$PW "http://127.0.0.1:$PORT/service/rest/v1/search/assets?repository=corp-snapshots&maven.artifactId=cart-core&maven.extension=jar" | python3 -c "
import sys, json
print(len(json.load(sys.stdin)['items']))")
  if [ "${J:-0}" -ge 1 ] && ! grep -rqF "$PW" $D/cart-core/pom.xml $D/cart-core/settings.xml $D/cart-core/.mvn 2>/dev/null && grep -q 'env.CORP_PASS' $D/cart-core/settings.xml; then pass "4 cart-core is published in corp-snapshots and the password is in no file"; else fail "4 cart-core is published in corp-snapshots (mvn -s settings.xml clean deploy) and the password is in no file"; fi
  g() { sed -n "$1p" $D/report.txt 2>/dev/null | tr 'A-Z' 'a-z'; }
  if [ -f $D/report.txt ] && g 1 | grep -q '^result:' && g 2 | grep -q '^trouble:' && g 2 | grep -q 'version' && g 2 | grep -q 'timestamp' && g 3 | grep -q '^cleanup:' && g 3 | grep -q 'down'; then pass "5 report.txt has result, trouble and cleanup"; else fail "5 report.txt has result:, trouble: (version, timestamp) and cleanup: (lab down) lines"; fi
  rm -rf "${W:?}"
  echo "$ok/5 checks passed"; [ $ok -eq 5 ]
}
status() { [ -d $D ] && echo "lab94 is set up in $D" || echo "lab94 is not set up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab94 removed";; status) status;; *) echo "usage: lab94.sh up|check|down|status"; exit 2;; esac
