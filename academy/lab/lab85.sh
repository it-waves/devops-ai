#!/bin/sh
# lab85.sh : Maven POM coordinates, project layout, dependencies (MC10-O01). Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status        Needs a JDK and Maven (sudo apt install -y openjdk-21-jdk-headless maven) and internet for Maven Central.
# Mission: the shop project will not build. Fix its coordinates, its folder layout and its dependencies.
D=${LAB85_DIR:-/opt/lab85}
U=${SUDO_USER:-root}
down() { rm -rf $D; true; }
up() {
  command -v javac >/dev/null 2>&1 && command -v mvn >/dev/null 2>&1 || { echo "javac/mvn not found: run  sudo apt install -y openjdk-21-jdk-headless maven"; exit 1; }
  down; mkdir -p $D/shop/src/cloudcart $D/shop/test
  cat > $D/shop/pom.xml <<'EOF_P'
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.example</groupId>
  <artifactId>demo</artifactId>
  <version>1</version>
  <packaging>jar</packaging>

  <properties>
    <maven.compiler.release>21</maven.compiler.release>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
  </properties>

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
  cat > $D/shop/src/cloudcart/Greeter.java <<'EOF_G'
package cloudcart;

import org.apache.commons.lang3.StringUtils;

public class Greeter {
    public static String hello(String name) {
        return "Hello, " + StringUtils.capitalize(name) + "!";
    }

    public static void main(String[] args) {
        System.out.println(hello("cloudcart"));
    }
}
EOF_G
  cat > $D/shop/test/GreeterTest.java <<'EOF_T'
package cloudcart;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class GreeterTest {
    @Test
    public void greetsByName() {
        assertEquals("Hello, Alice!", Greeter.hello("alice"));
    }
}
EOF_T
  cat > $D/TASKS.txt <<'EOF_K'
LAB 85 : the shop project will not build.   Work in /opt/lab85/shop

1  Coordinates.  In pom.xml set  groupId com.cloudcart , artifactId cart-api , version 1.0.0
2  Layout.       Move the source to src/main/java/cloudcart/  and the test to src/test/java/cloudcart/
3  Dependencies. Declare commons-lang3 (org.apache.commons) version 3.14.0, and junit (junit:junit) version 4.13.2 with scope test.
4  Build.        mvn -B package   must end with BUILD SUCCESS and make target/cart-api-1.0.0.jar
5  Tree.         mvn -B dependency:tree > tree.txt   (run in the shop folder)

Then:  lab check     (all 5 must pass)       and later:  lab down
EOF_K
  chown -R $U $D 2>/dev/null
  echo "lab85 ready: cd $D/shop   (task list: $D/TASKS.txt)"
}
check() {
  [ -d $D/shop ] || { echo "lab not set up: run  lab up"; exit 1; }
  cd $D/shop; ok=0
  as() { if [ "$U" = root ]; then "$@"; else runuser -u $U -- env HOME=$(getent passwd $U | cut -d: -f6) "$@"; fi; }
  pass() { echo "PASS  $1"; ok=$((ok+1)); }
  fail() { echo "FAIL  $1"; }
  p=$(tr -d '\n ' < pom.xml)
  case "$p" in *"<groupId>com.cloudcart</groupId><artifactId>cart-api</artifactId><version>1.0.0</version>"*) pass "1 coordinates are com.cloudcart:cart-api:1.0.0";; *) fail "1 coordinates are com.cloudcart:cart-api:1.0.0";; esac
  if [ -f src/main/java/cloudcart/Greeter.java ] && [ -f src/test/java/cloudcart/GreeterTest.java ] && [ ! -f src/cloudcart/Greeter.java ] && [ ! -f test/GreeterTest.java ]; then pass "2 standard layout (src/main/java, src/test/java)"; else fail "2 standard layout (src/main/java, src/test/java)"; fi
  case "$p" in *"commons-lang3</artifactId><version>3.14.0</version>"*"junit</artifactId><version>4.13.2</version><scope>test</scope>"*|*"junit</artifactId><version>4.13.2</version><scope>test</scope>"*"commons-lang3</artifactId><version>3.14.0</version>"*) pass "3 dependencies declared (commons-lang3 3.14.0, junit 4.13.2 test)";; *) fail "3 dependencies declared (commons-lang3 3.14.0, junit 4.13.2 test)";; esac
  as mvn -B -q clean package > /tmp/lab85-build.log 2>&1
  if [ -f target/cart-api-1.0.0.jar ] && unzip -l target/cart-api-1.0.0.jar 2>/dev/null | grep -q 'cloudcart/Greeter.class'; then pass "4 build makes cart-api-1.0.0.jar with Greeter.class"; else fail "4 build makes cart-api-1.0.0.jar with Greeter.class"; fi
  if [ -f tree.txt ] && grep -q 'org.apache.commons:commons-lang3:jar:3.14.0:compile' tree.txt && grep -q 'junit:junit:jar:4.13.2:test' tree.txt; then pass "5 tree.txt shows both dependencies and their scopes"; else fail "5 tree.txt shows both dependencies and their scopes"; fi
  echo "$ok/5 checks passed"; [ $ok -eq 5 ]
}
status() { [ -d $D ] && echo "lab85 is set up in $D" || echo "lab85 is not set up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab85 removed";; status) status;; *) echo "usage: lab85.sh up|check|down|status"; exit 2;; esac
