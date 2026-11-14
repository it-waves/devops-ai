#!/bin/sh
# lab92.sh : diagnose four Maven build failures, offline, checksum, login and test (MC10-O08). Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status        Needs a JDK, Maven and python3 (sudo apt install -y openjdk-21-jdk-headless maven python3). Maven downloads its own plugins once.
# Mission: four small projects each fail for a different reason. Read the error, name the cause, fix the cause (never hide it).
D=${LAB92_DIR:-/opt/lab92}
U=${SUDO_USER:-root}
PORT=8093
stopsrv() { [ -f $D/srv.pid ] && kill $(cat $D/srv.pid) 2>/dev/null; rm -f $D/srv.pid; true; }
down() { stopsrv; pkill -f "$D/srv.py" 2>/dev/null; rm -rf $D /tmp/lab92-chk; true; }
mklib() { # artifact version  (writes jar, pom, sha1 files)
  a=$1; v=$2; R=$D/repo; d=$R/com/cloudcart/lib/$a/$v; mkdir -p $d
  printf '<project xmlns="http://maven.apache.org/POM/4.0.0"><modelVersion>4.0.0</modelVersion><groupId>com.cloudcart.lib</groupId><artifactId>%s</artifactId><version>%s</version></project>\n' $a $v > $d/$a-$v.pom
  w=$(mktemp -d); mkdir -p $w/cloudcart/lib; C=$(printf '%s' "$a" | sed 's/./\U&/')
  printf 'package cloudcart.lib;\npublic class %s { public static String name() { return "%s %s"; } }\n' $C $a $v > $w/cloudcart/lib/$C.java
  ( cd $w && javac --release 21 -d out cloudcart/lib/$C.java && jar cf $d/$a-$v.jar -C out . )
  rm -rf $w
  for f in $d/$a-$v.jar $d/$a-$v.pom; do sha1sum $f | cut -d' ' -f1 | tr -d '\n' > $f.sha1; done
}
startsrv() {
  if ! curl -s -o /dev/null http://127.0.0.1:$PORT/ 2>/dev/null; then
    nohup python3 $D/srv.py $D/repo dev "$(cat $D/pass.txt)" $PORT >/dev/null 2>&1 &
    echo $! > $D/srv.pid; sleep 1
  fi
}
proj() { # dir artifact  : a project skeleton in $D/<dir>
  p=$D/$1; mkdir -p $p/src/main/java/cloudcart
  cat > $p/settings.xml <<'EOF_X'
<settings>
  <servers>
    <server>
      <id>corp</id>
      <username>dev</username>
      <password>${env.CORP_PASS}</password>
    </server>
  </servers>
  <mirrors>
    <mirror>
      <id>corp</id>
      <mirrorOf>libs</mirrorOf>
      <url>http://localhost:8093</url>
    </mirror>
  </mirrors>
</settings>
EOF_X
  cat > $p/pom.xml <<EOF_P
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.cloudcart</groupId>
  <artifactId>cart-$1</artifactId>
  <version>1.0.0</version>

  <properties>
    <maven.compiler.release>21</maven.compiler.release>
  </properties>

  <repositories>
    <repository>
      <id>libs</id>
      <url>https://repo.cloudcart.example/libs</url>
      <releases><checksumPolicy>fail</checksumPolicy></releases>
      <snapshots><enabled>false</enabled></snapshots>
    </repository>
  </repositories>

  <dependencies>
    <dependency>
      <groupId>com.cloudcart.lib</groupId>
      <artifactId>$2</artifactId>
      <version>${3:-1.0}</version>
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
  C=$(printf '%s' "$2" | sed 's/./\U&/')
  printf 'package cloudcart;\n\nimport cloudcart.lib.%s;\n\npublic class Cart {\n    public static String banner() {\n        return %s.name();\n    }\n}\n' $C $C > $p/src/main/java/cloudcart/Cart.java
}
up() {
  command -v javac >/dev/null 2>&1 && command -v mvn >/dev/null 2>&1 && command -v python3 >/dev/null 2>&1 || { echo "javac, mvn or python3 not found: run  sudo apt install -y openjdk-21-jdk-headless maven python3"; exit 1; }
  down; mkdir -p $D
  mklib fresh 1.0; mklib badsum 1.0; mklib badsum 1.0.1; mklib util 2.0
  printf '0000000000000000000000000000000000000000' > $D/repo/com/cloudcart/lib/badsum/1.0/badsum-1.0.jar.sha1
  cat > $D/srv.py <<'EOF_S'
import http.server, base64, sys, functools
ROOT, USER, PW, PORT = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
tok = 'Basic ' + base64.b64encode((USER + ':' + PW).encode()).decode()
class H(http.server.SimpleHTTPRequestHandler):
    def _ok(self):
        if self.headers.get('Authorization') == tok: return True
        self.send_response(401); self.send_header('WWW-Authenticate', 'Basic realm="corp"'); self.send_header('Content-Length', '0'); self.end_headers(); return False
    def do_GET(self):
        if self._ok(): super().do_GET()
    def do_HEAD(self):
        if self._ok(): super().do_HEAD()
    def log_message(self, *a): pass
http.server.ThreadingHTTPServer(('127.0.0.1', PORT), functools.partial(H, directory=ROOT)).serve_forever()
EOF_S
  printf 'corp-%s\n' "$(date +%s | sha256sum | cut -c1-12)" > $D/pass.txt; chmod 600 $D/pass.txt
  # 1 offline: a hidden maven.config holds -o
  proj offline fresh 1.0; mkdir -p $D/offline/.mvn; printf -- '-o\n' > $D/offline/.mvn/maven.config
  # 2 checksum: the repository holds a bad checksum for badsum 1.0 (1.0.1 is good)
  proj checksum badsum 1.0
  # 3 login: the server id does not match the mirror id
  proj login util 2.0; sed -i '0,/<id>corp<\/id>/s//<id>corp-repo<\/id>/' $D/login/settings.xml
  # 4 test: a rounding bug
  proj tests util 2.0
  sed -i '/<dependencies>/,/<\/dependencies>/d' $D/tests/pom.xml
  sed -i 's#  <build>#  <dependencies>\n    <dependency>\n      <groupId>junit</groupId>\n      <artifactId>junit</artifactId>\n      <version>4.13.2</version>\n      <scope>test</scope>\n    </dependency>\n  </dependencies>\n\n  <build>#' $D/tests/pom.xml
  mkdir -p $D/tests/src/test/java/cloudcart
  printf 'package cloudcart;\n\npublic class Cart {\n    public static int discounted(int cents, int percent) {\n        int off = cents * percent / 1000;\n        return cents - off;\n    }\n}\n' > $D/tests/src/main/java/cloudcart/Cart.java
  printf 'package cloudcart;\n\nimport static org.junit.Assert.assertEquals;\nimport org.junit.Test;\n\npublic class CartTest {\n    @Test\n    public void tenPercentOff() {\n        assertEquals(900, Cart.discounted(1000, 10));\n    }\n\n    @Test\n    public void noDiscount() {\n        assertEquals(500, Cart.discounted(500, 0));\n    }\n}\n' > $D/tests/src/test/java/cloudcart/CartTest.java
  sha1sum $D/tests/src/test/java/cloudcart/CartTest.java | cut -d' ' -f1 > $D/.testsum
  cat > $D/TASKS.txt <<'EOF_K'
LAB 92 : four projects, four different failures.   Work in /opt/lab92
The company repository is  http://localhost:8093  and needs a login.   user dev, password in /opt/lab92/pass.txt
First, in a terminal:  export CORP_PASS=$(cat /opt/lab92/pass.txt)
In every project:       mvn -B -s settings.xml clean package      (the test project has no mirror: just  mvn -B clean package)

1  offline/    The build says it cannot reach the repository in offline mode. Find why, and fix the cause.
2  checksum/   The build says a checksum validation failed. The repository copy of that version is bad.
               Move to the good version. Do NOT turn checksum checking off.
3  login/      The build says 401 Unauthorized. Compare the id in settings.xml with the mirror id. Fix the id,
               and keep the password in the environment variable.
4  tests/      A test fails. Read the report, fix the CODE. Do NOT skip the tests and do NOT edit the test.
5  Notes.      In /opt/lab92/diag.txt write four lines, one per failure, each starting with its number and naming
               the cause in your own words, like:   1 offline: ...

Then:  lab check     (all 5 must pass)       and later:  lab down
EOF_K
  chown -R $U $D 2>/dev/null; chown root:root $D/srv.py $D/repo
  startsrv
  echo "lab92 ready: cd $D   (task list: $D/TASKS.txt)"
}
check() {
  [ -d $D/offline ] || { echo "lab not set up: run  lab up"; exit 1; }
  startsrv
  ok=0; PW=$(cat $D/pass.txt)
  as() { if [ "$U" = root ]; then "$@"; else runuser -u $U -- env HOME=$(getent passwd $U | cut -d: -f6) "$@"; fi; }
  pass() { echo "PASS  $1"; ok=$((ok+1)); }
  fail() { echo "FAIL  $1"; }
  W=/tmp/lab92-chk; rm -rf $W; mkdir -p $W; chmod 777 $W
  bld() { # dir with-settings?
    rm -rf $W/$1; cp -r $D/$1 $W/$1; rm -rf $W/$1/target; chown -R $U $W/$1 2>/dev/null
    if [ "$2" = s ]; then ( cd $W/$1 && as env CORP_PASS=$PW mvn -B -s settings.xml -Dmaven.repo.local=$W/repo$1 clean package > $W/$1.log 2>&1 )
    else ( cd $W/$1 && as mvn -B -Dmaven.repo.local=$W/repo$1 clean package > $W/$1.log 2>&1 ); fi
    grep -q 'BUILD SUCCESS' $W/$1.log
  }
  if ! grep -qE '(^|[[:space:]])(-o|--offline)([[:space:]]|$)' $D/offline/.mvn/maven.config 2>/dev/null && bld offline s; then pass "1 offline: the build works and -o is gone from .mvn/maven.config"; else fail "1 offline: the build works and -o is gone from .mvn/maven.config"; fi
  if grep -q '<checksumPolicy>fail</checksumPolicy>' $D/checksum/pom.xml && grep -q '<version>1.0.1</version>' $D/checksum/pom.xml && bld checksum s; then pass "2 checksum: the good version 1.0.1 builds with strict checksums"; else fail "2 checksum: the good version 1.0.1 builds with strict checksums"; fi
  if ! grep -qF "$PW" $D/login/settings.xml && grep -q 'env.CORP_PASS' $D/login/settings.xml && bld login s; then pass "3 login: ids match and the password still comes from CORP_PASS"; else fail "3 login: ids match and the password still comes from CORP_PASS"; fi
  T=$(sha1sum $D/tests/src/test/java/cloudcart/CartTest.java | cut -d' ' -f1)
  if [ "$T" = "$(cat $D/.testsum)" ] && ! grep -rqiE 'skipTests|maven.test.skip|testFailureIgnore' $D/tests/pom.xml $D/tests/.mvn 2>/dev/null && bld tests n && grep -q 'Tests run: 2, Failures: 0' $W/tests.log; then pass "4 tests: both tests pass, the test file is unchanged and nothing is skipped"; else fail "4 tests: both tests pass, the test file is unchanged and nothing is skipped"; fi
  g() { sed -n "$1p" $D/diag.txt 2>/dev/null | tr 'A-Z' 'a-z'; }
  if [ -f $D/diag.txt ] && g 1 | grep -q 'offline' && g 1 | grep -qE -- '-o|maven.config' && g 2 | grep -q 'checksum' && g 3 | grep -q '401' && g 3 | grep -q 'id' && g 4 | grep -q 'test' && g 4 | grep -qE 'bug|expected|assert|code|rounding'; then pass "5 diag.txt names the four causes"; else fail "5 diag.txt names the four causes"; fi
  rm -rf $W
  echo "$ok/5 checks passed"; [ $ok -eq 5 ]
}
status() { [ -d $D ] && echo "lab92 is set up in $D" || echo "lab92 is not set up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab92 removed";; status) status;; *) echo "usage: lab92.sh up|check|down|status"; exit 2;; esac
