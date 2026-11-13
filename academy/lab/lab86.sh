#!/bin/sh
# lab86.sh : Maven build lifecycle: clean, compile, test, package, verify (MC10-O02). Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status        Needs a JDK and Maven (sudo apt install -y openjdk-21-jdk-headless maven) and internet for Maven Central.
# Mission: the pricing project fails its tests. Fix it, then prove you understand which goal runs in which phase.
D=${LAB86_DIR:-/opt/lab86}
U=${SUDO_USER:-root}
down() { rm -rf $D /tmp/lab86-chk; true; }
up() {
  command -v javac >/dev/null 2>&1 && command -v mvn >/dev/null 2>&1 || { echo "javac/mvn not found: run  sudo apt install -y openjdk-21-jdk-headless maven"; exit 1; }
  down; mkdir -p $D/shop/src/main/java/cloudcart $D/shop/src/test/java/cloudcart
  cat > $D/shop/pom.xml <<'EOF_P'
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.cloudcart</groupId>
  <artifactId>cart-pricing</artifactId>
  <version>1.0.0</version>
  <packaging>jar</packaging>

  <properties>
    <maven.compiler.release>21</maven.compiler.release>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
  </properties>

  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>4.13.2</version>
      <scope>test</scope>
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
  cat > $D/shop/src/main/java/cloudcart/Price.java <<'EOF_G'
package cloudcart;

public class Price {
    public static int total(int quantity, int unitCents) {
        return quantity + unitCents;
    }

    public static int withTax(int cents) {
        return cents + cents / 10;
    }
}
EOF_G
  cat > $D/shop/src/test/java/cloudcart/PriceTest.java <<'EOF_T'
package cloudcart;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class PriceTest {
    @Test
    public void totalMultipliesQuantityByUnit() {
        assertEquals(1500, Price.total(3, 500));
    }

    @Test
    public void taxIsTenPercent() {
        assertEquals(1100, Price.withTax(1000));
    }

    @Test
    public void zeroStaysZero() {
        assertEquals(0, Price.withTax(0));
    }
}
EOF_T
  cat > $D/TASKS.txt <<'EOF_K'
LAB 86 : the pricing project fails its tests.   Work in /opt/lab86/shop

1  Fix.      Run  mvn -B test  and read the failure. Fix the bug in src/main/java/cloudcart/Price.java
             until  mvn -B clean test  ends with BUILD SUCCESS and Tests run: 3, Failures: 0
2  Goals.    Run  mvn -B package | grep -E '^\[INFO\] --- ' > goals.txt
             goals.txt must show the goals in order: resources, compiler, testResources, testCompile, surefire test, jar
3  Skip.     Run  mvn -B package -DskipTests | grep -E 'skipped|Tests run' > skip.txt
             skip.txt must say that tests are skipped and must not contain a Tests run line
4  Package.  mvn -B clean verify   must make target/cart-pricing-1.0.0.jar (the checker builds this itself)
5  Clean.    Last step: mvn -B clean   so that the target folder is gone

Then:  lab check     (all 5 must pass)       and later:  lab down
EOF_K
  chown -R $U $D 2>/dev/null
  echo "lab86 ready: cd $D/shop   (task list: $D/TASKS.txt)"
}
check() {
  [ -d $D/shop ] || { echo "lab not set up: run  lab up"; exit 1; }
  cd $D/shop; ok=0
  as() { if [ "$U" = root ]; then "$@"; else runuser -u $U -- env HOME=$(getent passwd $U | cut -d: -f6) "$@"; fi; }
  pass() { echo "PASS  $1"; ok=$((ok+1)); }
  fail() { echo "FAIL  $1"; }
  rm -rf /tmp/lab86-chk; mkdir -p /tmp/lab86-chk; cp -r $D/shop /tmp/lab86-chk/ ; chown -R $U /tmp/lab86-chk 2>/dev/null; rm -rf /tmp/lab86-chk/shop/target
  ( cd /tmp/lab86-chk/shop && as mvn -B clean test > /tmp/lab86-chk/test.log 2>&1 )
  if grep -q 'BUILD SUCCESS' /tmp/lab86-chk/test.log && grep -q 'Tests run: 3, Failures: 0' /tmp/lab86-chk/test.log; then pass "1 tests pass: mvn clean test ends BUILD SUCCESS, 3 tests"; else fail "1 tests pass: mvn clean test ends BUILD SUCCESS, 3 tests"; fi
  g=$(grep -n 'resources:3.3.0:resources \|compiler:3.10.1:compile \|resources:3.3.0:testResources \|compiler:3.10.1:testCompile \|surefire:2.22.3:test \|jar:3.3.0:jar ' goals.txt 2>/dev/null | sed 's/^[0-9]*:.*--- \(maven-\)\{0,1\}\([a-zA-Z]*\)[a-z-]*:[0-9.]*:\([a-zA-Z]*\).*/\2:\3/' | tr '\n' ' ')
  if [ "$g" = "resources:resources compiler:compile resources:testResources compiler:testCompile surefire:test jar:jar " ]; then pass "2 goals.txt shows the six goals in lifecycle order"; else fail "2 goals.txt shows the six goals in lifecycle order"; fi
  if [ -f skip.txt ] && grep -qi 'tests are skipped' skip.txt && ! grep -q 'Tests run:' skip.txt; then pass "3 skip.txt shows tests skipped, no Tests run line"; else fail "3 skip.txt shows tests skipped, no Tests run line"; fi
  ( cd /tmp/lab86-chk/shop && as mvn -B clean verify > /tmp/lab86-chk/verify.log 2>&1 )
  if [ -f /tmp/lab86-chk/shop/target/cart-pricing-1.0.0.jar ] && unzip -l /tmp/lab86-chk/shop/target/cart-pricing-1.0.0.jar 2>/dev/null | grep -q 'cloudcart/Price.class'; then pass "4 clean verify makes cart-pricing-1.0.0.jar with Price.class"; else fail "4 clean verify makes cart-pricing-1.0.0.jar with Price.class"; fi
  if [ ! -d target ] && [ -f goals.txt ]; then pass "5 target folder is gone (mvn clean was the last step)"; else fail "5 target folder is gone (mvn clean was the last step)"; fi
  rm -rf /tmp/lab86-chk
  echo "$ok/5 checks passed"; [ $ok -eq 5 ]
}
status() { [ -d $D ] && echo "lab86 is set up in $D" || echo "lab86 is not set up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab86 removed";; status) status;; *) echo "usage: lab86.sh up|check|down|status"; exit 2;; esac
