#!/bin/sh
# lab88.sh : Maven dependency trees and version conflicts (MC10-O04). Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status        Needs a JDK and Maven (sudo apt install -y openjdk-21-jdk-headless maven). No internet needed after Maven's own plugins are downloaded.
# Mission: two libraries need different versions of the same library. Find the conflict, read the tree, and pin the version you need.
D=${LAB88_DIR:-/opt/lab88}
U=${SUDO_USER:-root}
down() { rm -rf $D /tmp/lab88-chk; true; }
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
  command -v javac >/dev/null 2>&1 && command -v mvn >/dev/null 2>&1 || { echo "javac/mvn not found: run  sudo apt install -y openjdk-21-jdk-headless maven"; exit 1; }
  down; mkdir -p $D/shop/src/main/java/cloudcart; mkrepo $D/repo
  cat > $D/shop/pom.xml <<EOF_P
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.cloudcart</groupId>
  <artifactId>cart-libs</artifactId>
  <version>1.0.0</version>

  <properties>
    <maven.compiler.release>21</maven.compiler.release>
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
      <artifactId>liba</artifactId>
      <version>1.0</version>
    </dependency>
    <dependency>
      <groupId>com.cloudcart.lib</groupId>
      <artifactId>libb</artifactId>
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
      <plugin><artifactId>maven-dependency-plugin</artifactId><version>3.5.0</version></plugin>
    </plugins>
  </build>
</project>
EOF_P
  cat > $D/shop/src/main/java/cloudcart/App.java <<'EOF_G'
package cloudcart;

import cloudcart.lib.Util;

public class App {
    public static void main(String[] args) {
        System.out.println(Util.shout("cloudcart"));
    }
}
EOF_G
  cat > $D/TASKS.txt <<'EOF_K'
LAB 88 : the build fails because two libraries disagree about util.   Work in /opt/lab88/shop

1  Find.     Run  mvn -B dependency:tree -Dverbose | grep omitted > conflict.txt   (do this BEFORE you fix anything)
             conflict.txt must show a line with  omitted for conflict
2  Fix.      App.java needs util 2.0. Pin it for the whole project with a  dependencyManagement  block in the pom
             (groupId com.cloudcart.lib, artifactId util, version 2.0). Do not delete liba or libb.
3  Build.    mvn -B clean package   must end with BUILD SUCCESS
4  Tree.     mvn -B dependency:tree > tree.txt   must show util 2.0 and no util 1.0
5  Why.      Write one sentence in why.txt about the rule Maven used to pick util 1.0 first. It must contain the word  nearest  or  first.

Then:  lab check     (all 5 must pass)       and later:  lab down
EOF_K
  chown -R $U $D 2>/dev/null
  echo "lab88 ready: cd $D/shop   (task list: $D/TASKS.txt)"
}
check() {
  [ -d $D/shop ] || { echo "lab not set up: run  lab up"; exit 1; }
  cd $D/shop; ok=0
  as() { if [ "$U" = root ]; then "$@"; else runuser -u $U -- env HOME=$(getent passwd $U | cut -d: -f6) "$@"; fi; }
  pass() { echo "PASS  $1"; ok=$((ok+1)); }
  fail() { echo "FAIL  $1"; }
  if [ -f conflict.txt ] && grep -q 'omitted for conflict' conflict.txt && grep -q 'util' conflict.txt; then pass "1 conflict.txt shows the util conflict"; else fail "1 conflict.txt shows the util conflict"; fi
  W=/tmp/lab88-chk; rm -rf $W; mkdir -p $W; cp -r $D/shop $W/s; rm -rf $W/s/target; chown -R $U $W 2>/dev/null
  ( cd $W/s && as mvn -B clean package > $W/b.log 2>&1 )
  if grep -q 'BUILD SUCCESS' $W/b.log && [ -f $W/s/target/cart-libs-1.0.0.jar ]; then pass "2 mvn clean package builds cart-libs-1.0.0.jar"; else fail "2 mvn clean package builds cart-libs-1.0.0.jar"; fi
  p=$(tr -d '\n ' < pom.xml)
  case "$p" in *"<dependencyManagement>"*"<artifactId>util</artifactId><version>2.0</version>"*"</dependencyManagement>"*) pass "3 dependencyManagement pins util 2.0";; *) fail "3 dependencyManagement pins util 2.0";; esac
  if [ -f tree.txt ] && grep -q 'util:jar:2.0' tree.txt && ! grep -q 'util:jar:1.0' tree.txt; then pass "4 tree.txt shows util 2.0 only"; else fail "4 tree.txt shows util 2.0 only"; fi
  case "$p" in *"<artifactId>liba</artifactId><version>1.0</version>"*"<artifactId>libb</artifactId><version>1.0</version>"*) ;; *) lib=no;; esac
  if [ -z "$lib" ] && [ -f why.txt ] && grep -qiE 'nearest|first' why.txt; then pass "5 liba and libb kept, why.txt explains the rule"; else fail "5 liba and libb kept, why.txt explains the rule"; fi
  rm -rf $W
  echo "$ok/5 checks passed"; [ $ok -eq 5 ]
}
status() { [ -d $D ] && echo "lab88 is set up in $D" || echo "lab88 is not set up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab88 removed";; status) status;; *) echo "usage: lab88.sh up|check|down|status"; exit 2;; esac
