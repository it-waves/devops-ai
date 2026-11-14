#!/bin/sh
# lab89.sh : package CloudCart as a WAR and verify what is inside (MC10-O05). Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status        Needs a JDK, Maven and unzip (sudo apt install -y openjdk-21-jdk-headless maven unzip). Maven downloads its own plugins once.
# Mission: the project builds a plain jar. Turn it into a deployable web archive (WAR) and prove what is inside.
D=${LAB89_DIR:-/opt/lab89}
U=${SUDO_USER:-root}
down() { rm -rf $D /tmp/lab89-chk; true; }
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
up() {
  command -v javac >/dev/null 2>&1 && command -v mvn >/dev/null 2>&1 || { echo "javac/mvn not found: run  sudo apt install -y openjdk-21-jdk-headless maven unzip"; exit 1; }
  down; mkdir -p $D/shop/src/main/java/cloudcart $D/shop/src/main/webapp/WEB-INF; mkrepo $D/repo
  cat > $D/shop/pom.xml <<EOF_P
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.cloudcart</groupId>
  <artifactId>cart-web</artifactId>
  <version>1.0.0</version>
  <packaging>jar</packaging>

  <properties>
    <maven.compiler.release>21</maven.compiler.release>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
  </properties>

  <repositories>
    <repository>
      <id>labrepo</id>
      <url>file://$D/repo</url>
      <snapshots><enabled>false</enabled></snapshots>
    </repository>
  </repositories>

  <dependencies>
    <dependency>
      <groupId>com.cloudcart.lib</groupId>
      <artifactId>util</artifactId>
      <version>2.0</version>
    </dependency>
    <dependency>
      <groupId>com.cloudcart.lib</groupId>
      <artifactId>liba</artifactId>
      <version>1.0</version>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <plugin><artifactId>maven-clean-plugin</artifactId><version>3.2.0</version></plugin>
      <plugin><artifactId>maven-resources-plugin</artifactId><version>3.3.0</version></plugin>
      <plugin><artifactId>maven-compiler-plugin</artifactId><version>3.10.1</version></plugin>
      <plugin><artifactId>maven-surefire-plugin</artifactId><version>2.22.3</version></plugin>
      <plugin><artifactId>maven-jar-plugin</artifactId><version>3.3.0</version></plugin>
      <plugin><artifactId>maven-war-plugin</artifactId><version>3.3.2</version></plugin>
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
  echo '<html><body><h1>CloudCart</h1></body></html>' > $D/shop/src/main/webapp/index.html
  printf '<?xml version="1.0" encoding="UTF-8"?>\n<web-app xmlns="https://jakarta.ee/xml/ns/jakartaee" version="6.0"/>\n' > $D/shop/src/main/webapp/WEB-INF/web.xml
  cat > $D/TASKS.txt <<'EOF_K'
LAB 89 : the project builds a jar, but CloudCart must be a web archive.   Work in /opt/lab89/shop

1  Packaging.  Set packaging to war in the pom and add  <finalName>cloudcart</finalName>  inside <build>.
2  Build.      mvn -B clean package   must end with BUILD SUCCESS and create target/cloudcart.war
3  Contents.   unzip -l target/cloudcart.war > contents.txt
             It must list index.html, WEB-INF/web.xml and WEB-INF/classes/cloudcart/Cart.class
4  Libraries.  util 2.0 must be inside the WAR (WEB-INF/lib/util-2.0.jar).
             liba is supplied by the server in real life: give it scope provided so it is NOT packaged.
5  Why.        Write one sentence in why.txt about why a provided dependency stays out of the WAR.
             It must contain the word  provided  and the word  server  or  container.

Then:  lab check     (all 5 must pass)       and later:  lab down
EOF_K
  chown -R $U $D 2>/dev/null
  echo "lab89 ready: cd $D/shop   (task list: $D/TASKS.txt)"
}
check() {
  [ -d $D/shop ] || { echo "lab not set up: run  lab up"; exit 1; }
  command -v unzip >/dev/null 2>&1 || { echo "unzip not found: run  sudo apt install -y unzip"; exit 1; }
  cd $D/shop; ok=0
  as() { if [ "$U" = root ]; then "$@"; else runuser -u $U -- env HOME=$(getent passwd $U | cut -d: -f6) "$@"; fi; }
  pass() { echo "PASS  $1"; ok=$((ok+1)); }
  fail() { echo "FAIL  $1"; }
  p=$(tr -d '\n ' < pom.xml)
  W=/tmp/lab89-chk; rm -rf $W; mkdir -p $W; cp -r $D/shop $W/s; rm -rf $W/s/target; chown -R $U $W 2>/dev/null
  ( cd $W/s && as mvn -B clean package > $W/b.log 2>&1 )
  case "$p" in *"<packaging>war</packaging>"*"<finalName>cloudcart</finalName>"*) pass "1 packaging is war and finalName is cloudcart";; *) fail "1 packaging is war and finalName is cloudcart";; esac
  if grep -q 'BUILD SUCCESS' $W/b.log && [ -f $W/s/target/cloudcart.war ]; then pass "2 mvn clean package builds target/cloudcart.war"; else fail "2 mvn clean package builds target/cloudcart.war"; fi
  if [ -f contents.txt ] && grep -q 'index.html' contents.txt && grep -q 'WEB-INF/web.xml' contents.txt && grep -q 'WEB-INF/classes/cloudcart/Cart.class' contents.txt; then pass "3 contents.txt lists the page, web.xml and Cart.class"; else fail "3 contents.txt lists the page, web.xml and Cart.class"; fi
  L=$(unzip -l $W/s/target/cloudcart.war 2>/dev/null)
  if echo "$L" | grep -q 'WEB-INF/lib/util-2.0.jar' && ! echo "$L" | grep -q 'liba-1.0.jar'; then pass "4 util 2.0 is inside the WAR, liba is not"; else fail "4 util 2.0 is inside the WAR, liba is not"; fi
  if [ -f why.txt ] && grep -qi 'provided' why.txt && grep -qiE 'server|container' why.txt; then pass "5 why.txt explains provided"; else fail "5 why.txt explains provided"; fi
  rm -rf $W
  echo "$ok/5 checks passed"; [ $ok -eq 5 ]
}
status() { [ -d $D ] && echo "lab89 is set up in $D" || echo "lab89 is not set up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab89 removed";; status) status;; *) echo "usage: lab89.sh up|check|down|status"; exit 2;; esac
