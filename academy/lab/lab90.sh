#!/bin/sh
# lab90.sh : repository mirrors and credentials, safely (MC10-O06). Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status        Needs a JDK, Maven and python3 (sudo apt install -y openjdk-21-jdk-headless maven). Maven downloads its own plugins once.
# Mission: the company repository sits behind a login. Route Maven to it with a mirror, and give it the password without ever writing the password in a file.
D=${LAB90_DIR:-/opt/lab90}
U=${SUDO_USER:-root}
PORT=8091
stopsrv() { [ -f $D/srv.pid ] && kill $(cat $D/srv.pid) 2>/dev/null; rm -f $D/srv.pid; true; }
down() { stopsrv; pkill -f "$D/srv.py" 2>/dev/null; rm -rf $D /tmp/lab90-chk; true; }
mkrepo() {
R=$1
G=com/cloudcart/lib
mk() { # artifact version depart depver
  a=$1; v=$2; d=$R/$G/$a/$v; mkdir -p $d
  { echo '<project xmlns="http://maven.apache.org/POM/4.0.0"><modelVersion>4.0.0</modelVersion>'
    echo "<groupId>com.cloudcart.lib</groupId><artifactId>$a</artifactId><version>$v</version>"
    if [ -n "$3" ]; then echo "<dependencies><dependency><groupId>com.cloudcart.lib</groupId><artifactId>$3</artifactId><version>$4</version></dependency></dependencies>"; fi
    echo '</project>'; } > $d/$a-$v.pom
  w=$(mktemp -d); mkdir -p $w/cloudcart/lib
  case "$a" in
   util) cat > $w/cloudcart/lib/Util.java <<EOF
package cloudcart.lib;
public class Util {
    public static String version() { return "$v"; }
$( [ "$v" = 2.0 ] && echo '    public static String shout(String s) { return s.toUpperCase() + "!"; }' )
}
EOF
   ;;
   liba) cat > $w/cloudcart/lib/LibA.java <<EOF
package cloudcart.lib;
public class LibA { public static String name() { return "liba"; } }
EOF
   ;;
   libb) cat > $w/cloudcart/lib/LibB.java <<EOF
package cloudcart.lib;
public class LibB { public static String name() { return "libb"; } }
EOF
   ;;
  esac
  ( cd $w && javac --release 21 -d out cloudcart/lib/*.java && jar cf $d/$a-$v.jar -C out . )
  rm -rf $w
}
mk util 1.0; mk util 2.0; mk liba 1.0 util 1.0; mk libb 1.0 util 2.0
}
startsrv() {
  if ! curl -s -o /dev/null http://127.0.0.1:$PORT/ 2>/dev/null; then
    nohup python3 $D/srv.py $D/repo dev "$(cat $D/pass.txt)" $PORT >/dev/null 2>&1 &
    echo $! > $D/srv.pid; sleep 1
  fi
}
up() {
  command -v javac >/dev/null 2>&1 && command -v mvn >/dev/null 2>&1 && command -v python3 >/dev/null 2>&1 || { echo "javac, mvn or python3 not found: run  sudo apt install -y openjdk-21-jdk-headless maven python3"; exit 1; }
  down; mkdir -p $D/shop/src/main/java/cloudcart; mkrepo $D/repo
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
  cat > $D/shop/pom.xml <<'EOF_P'
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.cloudcart</groupId>
  <artifactId>cart-secure</artifactId>
  <version>1.0.0</version>

  <properties>
    <maven.compiler.release>21</maven.compiler.release>
  </properties>

  <repositories>
    <repository>
      <id>libs</id>
      <url>https://repo.cloudcart.example/libs</url>
      <snapshots><enabled>false</enabled></snapshots>
    </repository>
  </repositories>

  <dependencies>
    <dependency>
      <groupId>com.cloudcart.lib</groupId>
      <artifactId>util</artifactId>
      <version>2.0</version>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <plugin><artifactId>maven-clean-plugin</artifactId><version>3.2.0</version></plugin>
      <plugin><artifactId>maven-resources-plugin</artifactId><version>3.3.0</version></plugin>
      <plugin><artifactId>maven-compiler-plugin</artifactId><version>3.10.1</version></plugin>
      <plugin><artifactId>maven-surefire-plugin</artifactId><version>2.22.3</version></plugin>
      <plugin><artifactId>maven-jar-plugin</artifactId><version>3.3.0</version></plugin>
    </plugins>
  </build>
</project>
EOF_P
  cat > $D/shop/src/main/java/cloudcart/Cart.java <<'EOF_G'
package cloudcart;

import cloudcart.lib.Util;

public class Cart {
    public static String banner() {
        return Util.shout("cloudcart");
    }
}
EOF_G
  cat > $D/shop/settings.xml <<'EOF_X'
<settings>
  <!-- TODO: add the credentials (a server block) and the mirror here -->
</settings>
EOF_X
  cat > $D/TASKS.txt <<'EOF_K'
LAB 90 : the pom points at https://repo.cloudcart.example/libs, which you cannot reach.
The company mirror is  http://localhost:8091  and it needs a login.   Work in /opt/lab90/shop

The user name is dev. The password is in /opt/lab90/pass.txt. Never write the password in any file of the project.

1  Server.    In settings.xml add a server with id corp, username dev and
             <password>${env.CORP_PASS}</password>      (the password comes from an environment variable)
2  Mirror.    In settings.xml add a mirror with id corp, mirrorOf libs and url http://localhost:8091
3  Lock.      chmod 600 settings.xml
4  Build.     export CORP_PASS=$(cat /opt/lab90/pass.txt)
             mvn -B -s settings.xml clean package      must end with BUILD SUCCESS
5  Why.       Write one sentence in why.txt about why the password must not be in the pom.
             It must contain the word  pom  and the word  git  or  commit.

Then:  lab check     (all 5 must pass)       and later:  lab down
EOF_K
  chmod 644 $D/shop/settings.xml
  chown -R $U $D 2>/dev/null; chown root:root $D/srv.py
  startsrv
  echo "lab90 ready: cd $D/shop   (task list: $D/TASKS.txt)"
}
check() {
  [ -d $D/shop ] || { echo "lab not set up: run  lab up"; exit 1; }
  startsrv
  cd $D/shop; ok=0
  as() { if [ "$U" = root ]; then "$@"; else runuser -u $U -- env HOME=$(getent passwd $U | cut -d: -f6) "$@"; fi; }
  pass() { echo "PASS  $1"; ok=$((ok+1)); }
  fail() { echo "FAIL  $1"; }
  S=$(tr -d '\n ' < settings.xml); PW=$(cat $D/pass.txt)
  case "$S" in *"<server><id>corp</id><username>dev</username><password>\${env.CORP_PASS}</password></server>"*) pass "1 server corp takes its password from CORP_PASS";; *) fail "1 server corp takes its password from CORP_PASS";; esac
  case "$S" in *"<mirror><id>corp</id><mirrorOf>libs</mirrorOf><url>http://localhost:$PORT</url></mirror>"*) pass "2 mirror corp sends libs to http://localhost:$PORT";; *) fail "2 mirror corp sends libs to http://localhost:$PORT";; esac
  m=$(stat -c %a settings.xml); if [ "$m" = 600 ] && ! grep -rqF "$PW" settings.xml pom.xml why.txt 2>/dev/null; then pass "3 settings.xml is mode 600 and holds no password"; else fail "3 settings.xml is mode 600 and holds no password"; fi
  W=/tmp/lab90-chk; rm -rf $W; mkdir -p $W; cp -r $D/shop $W/s; rm -rf $W/s/target; chown -R $U $W 2>/dev/null
  ( cd $W/s && CORP_PASS=$PW as env CORP_PASS=$PW mvn -B -s settings.xml -Dmaven.repo.local=$W/repo clean package > $W/b.log 2>&1 )
  if grep -q 'BUILD SUCCESS' $W/b.log && [ -f $W/s/target/cart-secure-1.0.0.jar ]; then pass "4 mvn -s settings.xml clean package succeeds"; else fail "4 mvn -s settings.xml clean package succeeds"; fi
  if [ -f why.txt ] && grep -qi 'pom' why.txt && grep -qiE 'git|commit' why.txt; then pass "5 why.txt explains the risk"; else fail "5 why.txt explains the risk"; fi
  rm -rf $W
  echo "$ok/5 checks passed"; [ $ok -eq 5 ]
}
status() { [ -d $D ] && echo "lab90 is set up in $D" || echo "lab90 is not set up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab90 removed";; status) status;; *) echo "usage: lab90.sh up|check|down|status"; exit 2;; esac
