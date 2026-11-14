#!/bin/sh
# lab92.sh : diagnose four REAL Maven build failures (MC10-O08): wrong version (404 from Maven Central), offline flag, failing test, and a 401 from a real Nexus. Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status
# Needs: a JDK, Maven, curl, python3 (sudo apt install -y openjdk-21-jdk-headless maven curl python3), internet access,
#        about 3 GB of free memory, 2 GB of free disk and about 5 minutes the first time (the Nexus download is about 525 MB).
# Mission: four small projects each fail for a different reason. Read the error, name the cause, fix the cause (never hide it).
D=${LAB92_DIR:-/opt/lab92}
U=${SUDO_USER:-root}
PORT=8081
NV=3.98.1-01
NURL=https://download.sonatype.com/nexus/3/nexus-$NV-linux-x86_64.tar.gz
NU=nexus92
stopnx() { pkill -u $NU java 2>/dev/null; sleep 3; true; }
down() { stopnx; rm -rf "${D:?}" /tmp/lab92-chk; id $NU >/dev/null 2>&1 && userdel $NU 2>/dev/null; true; }
startnx() {
  curl -s -o /dev/null http://127.0.0.1:$PORT/service/rest/v1/status && return 0
  : > $D/nexus.log; chown $NU:$NU $D/nexus.log
  su $NU -c "cd $D/nexus/bin && setsid nohup ./nexus run > $D/nexus.log 2>&1 < /dev/null &"
  printf 'starting Nexus (about a minute) '
  for i in $(seq 1 90); do sleep 3; [ "$(curl -s -o /dev/null -w %{http_code} http://127.0.0.1:$PORT/service/rest/v1/status)" = 200 ] && { echo ok; return 0; }; printf '.'; done
  echo; echo "Nexus did not start: see $D/nexus.log"; return 1
}
proj() { # dir [dependency version] : a project skeleton in $D/<dir>
  p=$D/$1; mkdir -p $p/src/main/java/cloudcart
  cat > $p/pom.xml <<EOF_P
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.cloudcart</groupId>
  <artifactId>cart-$1</artifactId>
  <version>1.0.0</version>

  <properties>
    <maven.compiler.release>21</maven.compiler.release>
  </properties>

  <dependencies>
    <dependency>
      <groupId>org.apache.commons</groupId>
      <artifactId>commons-lang3</artifactId>
      <version>${2:-3.14.0}</version>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <plugin><artifactId>maven-clean-plugin</artifactId><version>3.2.0</version></plugin>
      <plugin><artifactId>maven-resources-plugin</artifactId><version>3.3.0</version></plugin>
      <plugin><artifactId>maven-compiler-plugin</artifactId><version>3.10.1</version></plugin>
      <plugin><artifactId>maven-surefire-plugin</artifactId><version>2.22.2</version></plugin>
      <plugin><artifactId>maven-jar-plugin</artifactId><version>3.3.0</version></plugin>
    </plugins>
  </build>
</project>
EOF_P
  printf 'package cloudcart;\n\nimport org.apache.commons.lang3.StringUtils;\n\npublic class Cart {\n    public static String banner() {\n        return StringUtils.capitalize("cloudcart");\n    }\n}\n' > $p/src/main/java/cloudcart/Cart.java
}
up() {
  for t in javac mvn curl python3; do command -v $t >/dev/null 2>&1 || { echo "$t not found: run  sudo apt install -y openjdk-21-jdk-headless maven curl python3"; exit 1; }; done
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  down; mkdir -p $D
  id $NU >/dev/null 2>&1 || useradd -r -m -d $D/nexus-home -s /bin/bash $NU
  echo "downloading Nexus $NV (about 525 MB) from download.sonatype.com ..."
  curl -fL --progress-bar -o $D/nexus.tgz $NURL || { echo "download failed"; exit 1; }
  mkdir -p $D/nexus.tmp && tar xzf $D/nexus.tgz -C $D/nexus.tmp && mv $D/nexus.tmp/nexus-$NV $D/nexus && mv $D/nexus.tmp/sonatype-work $D/sonatype-work && rm -rf "${D:?}/nexus.tgz" "${D:?}/nexus.tmp"
  mkdir -p $D/sonatype-work/nexus3/etc
  printf 'application-port=%s\n' $PORT > $D/sonatype-work/nexus3/etc/nexus.properties
  sed -i 's/^-Xms.*/-Xms1200m/; s/^-Xmx.*/-Xmx1200m/' $D/nexus/bin/nexus.vmoptions
  chown -R $NU:$NU $D/nexus $D/sonatype-work; chmod 755 $D
  startnx || exit 1
  # headless setup: your own admin password, licence accepted, anonymous access OFF (this is what makes the 401 real)
  for i in $(seq 1 40); do [ -f $D/sonatype-work/nexus3/admin.password ] && break; sleep 3; done
  A=$(cat $D/sonatype-work/nexus3/admin.password); P="corp-$(date +%s | sha256sum | cut -c1-12)"
  curl -s -o /dev/null -u admin:$A -X PUT -H 'Content-Type: text/plain' -d "$P" http://127.0.0.1:$PORT/service/rest/v1/security/users/admin/change-password
  curl -s -u admin:$P http://127.0.0.1:$PORT/service/rest/v1/system/eula > $D/eula.json
  python3 -c "import json;d=json.load(open('$D/eula.json'));d['accepted']=True;json.dump(d,open('$D/eula.json','w'))"
  curl -s -o /dev/null -u admin:$P -H 'Content-Type: application/json' -X POST -d @$D/eula.json http://127.0.0.1:$PORT/service/rest/v1/system/eula
  curl -s -o /dev/null -u admin:$P -H 'Content-Type: application/json' -X PUT -d '{"enabled":false,"userId":"anonymous","realmName":"NexusAuthorizingRealm"}' http://127.0.0.1:$PORT/service/rest/v1/security/anonymous
  rm -f $D/eula.json; printf '%s\n' "$P" > $D/pass.txt
  # 1 notfound: a version that does not exist on Maven Central
  proj notfound 3.14.99
  # 2 offline: a hidden maven.config holds -o
  proj offline; mkdir -p $D/offline/.mvn; printf -- '-o\n' > $D/offline/.mvn/maven.config
  # 3 tests: a rounding bug
  proj tests
  sed -i 's#  <dependencies>#  <dependencies>\n    <dependency>\n      <groupId>junit</groupId>\n      <artifactId>junit</artifactId>\n      <version>4.13.2</version>\n      <scope>test</scope>\n    </dependency>#' $D/tests/pom.xml
  mkdir -p $D/tests/src/test/java/cloudcart
  printf 'package cloudcart;\n\npublic class Cart {\n    public static int discounted(int cents, int percent) {\n        int off = cents * percent / 1000;\n        return cents - off;\n    }\n}\n' > $D/tests/src/main/java/cloudcart/Cart.java
  printf 'package cloudcart;\n\nimport static org.junit.Assert.assertEquals;\nimport org.junit.Test;\n\npublic class CartTest {\n    @Test\n    public void tenPercentOff() {\n        assertEquals(900, Cart.discounted(1000, 10));\n    }\n\n    @Test\n    public void noDiscount() {\n        assertEquals(500, Cart.discounted(500, 0));\n    }\n}\n' > $D/tests/src/test/java/cloudcart/CartTest.java
  sha1sum $D/tests/src/test/java/cloudcart/CartTest.java | cut -d' ' -f1 > $D/.testsum
  # 4 login: the server id does not match the mirror id (the mirror is your Nexus, which needs a login)
  proj login
  cat > $D/login/settings.xml <<EOF_X
<settings>
  <servers>
    <server>
      <id>corp-repo</id>
      <username>admin</username>
      <password>\${env.CORP_PASS}</password>
    </server>
  </servers>
  <mirrors>
    <mirror>
      <id>corp</id>
      <mirrorOf>*</mirrorOf>
      <url>http://localhost:$PORT/repository/maven-public/</url>
    </mirror>
  </mirrors>
</settings>
EOF_X
  cat > $D/TASKS.txt <<'EOF_K'
LAB 92 : four projects, four different failures.   Work in /opt/lab92
Your company repository is a real Nexus:  http://localhost:8081   user admin, password in /opt/lab92/pass.txt
First, in a terminal:  export CORP_PASS=$(cat /opt/lab92/pass.txt)
In every project:       mvn -B clean package      (the login project needs  -s settings.xml )

1  notfound/   The build says it could not find an artifact (404). Read which one. Fix the cause (do not delete the dependency).
2  offline/    The build says it cannot reach the repository in offline mode. Find why, and fix the cause.
3  tests/      A test fails. Read the report, fix the CODE. Do NOT skip the tests and do NOT edit the test.
4  login/      The build says 401 Unauthorized. Compare the id in settings.xml with the mirror id. Fix the id,
               and keep the password in the environment variable.
5  Notes.      In /opt/lab92/diag.txt write four lines, one per failure, each starting with its number and naming
               the cause in your own words, like:   1 notfound: ...

Then:  lab check     (all 5 must pass)       and later:  lab down
EOF_K
  chown -R $U $D/notfound $D/offline $D/tests $D/login $D/TASKS.txt $D/pass.txt 2>/dev/null; chmod 600 $D/pass.txt $D/login/settings.xml
  echo "lab92 ready: cd $D   (task list: $D/TASKS.txt)"
}
check() {
  [ -d $D/offline ] || { echo "lab not set up: run  lab up"; exit 1; }
  startnx || exit 1
  ok=0; PW=$(cat $D/pass.txt)
  as() { if [ "$U" = root ]; then "$@"; else runuser -u $U -- env HOME=$(getent passwd $U | cut -d: -f6) "$@"; fi; }
  pass() { echo "PASS  $1"; ok=$((ok+1)); }
  fail() { echo "FAIL  $1"; }
  W=/tmp/lab92-chk; rm -rf "${W:?}"; mkdir -p $W; chmod 777 $W
  bld() { # dir with-settings?
    cp -r $D/$1 $W/$1; rm -rf "${W:?}/$1/target"; chown -R $U $W/$1 2>/dev/null
    if [ "$2" = s ]; then ( cd $W/$1 && as env CORP_PASS=$PW mvn -B -s settings.xml -Dmaven.repo.local=$W/repo$1 clean package > $W/$1.log 2>&1 )
    else ( cd $W/$1 && as mvn -B -Dmaven.repo.local=$W/repo$1 clean package > $W/$1.log 2>&1 ); fi
    grep -q 'BUILD SUCCESS' $W/$1.log
  }
  if grep -q 'commons-lang3' $D/notfound/pom.xml && ! grep -q '3.14.99' $D/notfound/pom.xml && bld notfound n; then pass "1 notfound: the dependency is kept, a real version is used, the build works"; else fail "1 notfound: the dependency is kept, a real version is used, the build works"; fi
  if ! grep -qE '(^|[[:space:]])(-o|--offline)([[:space:]]|$)' $D/offline/.mvn/maven.config 2>/dev/null && bld offline n; then pass "2 offline: -o is gone from .mvn/maven.config and the build works"; else fail "2 offline: -o is gone from .mvn/maven.config and the build works"; fi
  T=$(sha1sum $D/tests/src/test/java/cloudcart/CartTest.java | cut -d' ' -f1)
  if [ "$T" = "$(cat $D/.testsum)" ] && ! grep -rqiE 'skipTests|maven.test.skip|testFailureIgnore' $D/tests/pom.xml $D/tests/.mvn 2>/dev/null && bld tests n && grep -q 'Tests run: 2, Failures: 0' $W/tests.log; then pass "3 tests: the code is fixed, the test is untouched, 2 tests pass"; else fail "3 tests: the code is fixed, the test is untouched, 2 tests pass"; fi
  if ! grep -qF "$PW" $D/login/settings.xml && grep -q 'env.CORP_PASS' $D/login/settings.xml && bld login s; then pass "4 login: ids match and the password still comes from CORP_PASS"; else fail "4 login: ids match and the password still comes from CORP_PASS"; fi
  g() { sed -n "$1p" $D/diag.txt 2>/dev/null | tr 'A-Z' 'a-z'; }
  if [ -f $D/diag.txt ] && g 1 | grep -qE 'version|404|not found' && g 2 | grep -q 'offline' && g 2 | grep -qE -- '-o|maven.config' && g 3 | grep -qE 'test|round|divide|1000|100' && g 4 | grep -q '401' && g 4 | grep -q 'id'; then pass "5 diag.txt names the four causes"; else fail "5 diag.txt names the four causes (one line each, 1 to 4)"; fi
  rm -rf "${W:?}"
  echo "$ok/5 checks passed"; [ $ok -eq 5 ]
}
status() { [ -d $D ] && echo "lab92 is set up in $D" || echo "lab92 is not set up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab92 removed";; status) status;; *) echo "usage: lab92.sh up|check|down|status"; exit 2;; esac
