#!/bin/sh
# lab91.sh : publish snapshot and release artifacts to a repository (MC10-O07). Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status        Needs a JDK, Maven and python3 (sudo apt install -y openjdk-21-jdk-headless maven python3). Maven downloads its own plugins once.
# Mission: publish a snapshot, then a release, find out why a release can never be published twice, and ship the next version.
D=${LAB91_DIR:-/opt/lab91}
U=${SUDO_USER:-root}
PORT=8092
stopsrv() { [ -f $D/srv.pid ] && kill $(cat $D/srv.pid) 2>/dev/null; rm -f $D/srv.pid; true; }
down() { stopsrv; pkill -f "$D/srv.py" 2>/dev/null; rm -rf $D /tmp/lab91-chk; true; }
startsrv() {
  if ! curl -s -o /dev/null http://127.0.0.1:$PORT/ 2>/dev/null; then
    nohup python3 $D/srv.py $D/store dev "$(cat $D/pass.txt)" $PORT >/dev/null 2>&1 &
    echo $! > $D/srv.pid; sleep 1
  fi
}
up() {
  command -v javac >/dev/null 2>&1 && command -v mvn >/dev/null 2>&1 && command -v python3 >/dev/null 2>&1 || { echo "javac, mvn or python3 not found: run  sudo apt install -y openjdk-21-jdk-headless maven python3"; exit 1; }
  down; mkdir -p $D/shop/src/main/java/cloudcart $D/store
  cat > $D/srv.py <<'EOF_S'
import http.server, base64, sys, os, functools
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
    def do_PUT(self):
        n = int(self.headers.get('Content-Length', 0)); data = self.rfile.read(n)
        if not self._ok(): return
        p = self.translate_path(self.path); rel = self.path.lstrip('/')
        base = os.path.basename(p)
        if rel.startswith('releases/') and os.path.exists(p) and not base.startswith('maven-metadata'):
            self.send_response(409); self.send_header('Content-Length', '0'); self.end_headers(); return
        os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, 'wb').write(data)
        self.send_response(201); self.send_header('Content-Length', '0'); self.end_headers()
    def log_message(self, *a): pass
os.makedirs(os.path.join(ROOT, 'releases'), exist_ok=True); os.makedirs(os.path.join(ROOT, 'snapshots'), exist_ok=True)
http.server.ThreadingHTTPServer(('127.0.0.1', PORT), functools.partial(H, directory=ROOT)).serve_forever()
EOF_S
  printf 'corp-%s\n' "$(date +%s | sha256sum | cut -c1-12)" > $D/pass.txt; chmod 600 $D/pass.txt
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
      <url>http://localhost:$PORT/snapshots</url>
    </snapshotRepository>
    <repository>
      <id>corp</id>
      <url>http://localhost:$PORT/releases</url>
    </repository>
  </distributionManagement>

  <build>
    <plugins>
      <plugin><artifactId>maven-clean-plugin</artifactId><version>3.2.0</version></plugin>
      <plugin><artifactId>maven-resources-plugin</artifactId><version>3.3.0</version></plugin>
      <plugin><artifactId>maven-compiler-plugin</artifactId><version>3.10.1</version></plugin>
      <plugin><artifactId>maven-surefire-plugin</artifactId><version>2.22.3</version></plugin>
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
      <username>dev</username>
      <password>${env.CORP_PASS}</password>
    </server>
  </servers>
</settings>
EOF_X
  chmod 600 $D/shop/settings.xml
  cat > $D/TASKS.txt <<'EOF_K'
LAB 91 : publish cart-core to the company repository (a small local stand-in for a repository manager).   Work in /opt/lab91/shop

First:  export CORP_PASS=$(cat /opt/lab91/pass.txt)
Always: mvn -B -s settings.xml ...      (the login is already in settings.xml)

1  Snapshot.  Deploy 1.0.0-SNAPSHOT:   mvn -B -s settings.xml deploy
2  Release.   Change the version in pom.xml to 1.0.0 (no SNAPSHOT) and deploy it.
3  Again.     Deploy 1.0.0 a second time. It must fail. Save the error line:
             mvn -B -s settings.xml deploy 2>&1 | grep -o 'status code.*' > conflict.txt
4  Next.      Change the version to 1.0.1 and deploy it.
5  Why.       Write one sentence in why.txt about why a release is never published twice.
             It must contain the word  release  and one of  immutable, reproducible, overwrite, changed.

Then:  lab check     (all 5 must pass)       and later:  lab down
EOF_K
  chown -R $U $D 2>/dev/null; chown root:root $D/srv.py $D/store 2>/dev/null; chmod 777 $D/store
  startsrv
  echo "lab91 ready: cd $D/shop   (task list: $D/TASKS.txt)"
}
check() {
  [ -d $D/shop ] || { echo "lab not set up: run  lab up"; exit 1; }
  startsrv
  cd $D/shop; ok=0; S=$D/store
  pass() { echo "PASS  $1"; ok=$((ok+1)); }
  fail() { echo "FAIL  $1"; }
  if ls $S/snapshots/com/cloudcart/cart-core/1.0.0-SNAPSHOT/cart-core-1.0.0-*.jar >/dev/null 2>&1; then pass "1 a snapshot of 1.0.0 is in the snapshot repository"; else fail "1 a snapshot of 1.0.0 is in the snapshot repository"; fi
  if [ -f $S/releases/com/cloudcart/cart-core/1.0.0/cart-core-1.0.0.jar ]; then pass "2 release 1.0.0 is in the release repository"; else fail "2 release 1.0.0 is in the release repository"; fi
  if [ -f conflict.txt ] && grep -q '409' conflict.txt && grep -qi 'conflict' conflict.txt; then pass "3 conflict.txt shows the 409 Conflict"; else fail "3 conflict.txt shows the 409 Conflict"; fi
  if [ -f $S/releases/com/cloudcart/cart-core/1.0.1/cart-core-1.0.1.jar ] && grep -q '<version>1.0.1</version>' pom.xml; then pass "4 release 1.0.1 is published and the pom says 1.0.1"; else fail "4 release 1.0.1 is published and the pom says 1.0.1"; fi
  if [ -f why.txt ] && grep -qi 'release' why.txt && grep -qiE 'immutable|reproducible|overwrite|changed' why.txt; then pass "5 why.txt explains release immutability"; else fail "5 why.txt explains release immutability"; fi
  echo "$ok/5 checks passed"; [ $ok -eq 5 ]
}
status() { [ -d $D ] && echo "lab91 is set up in $D" || echo "lab91 is not set up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab91 removed";; status) status;; *) echo "usage: lab91.sh up|check|down|status"; exit 2;; esac
