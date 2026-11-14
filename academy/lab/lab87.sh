#!/bin/sh
# lab87.sh : Maven plugins, properties, profiles, reproducible builds (MC10-O03). Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status        Needs a JDK and Maven (sudo apt install -y openjdk-21-jdk-headless maven) and internet for Maven Central.
# Mission: the greeter jar cannot run, hard-codes its settings, and builds a different file every time. Fix all of it in the pom.
D=${LAB87_DIR:-/opt/lab87}
U=${SUDO_USER:-root}
down() { rm -rf $D /tmp/lab87-chk; true; }
up() {
  command -v javac >/dev/null 2>&1 && command -v mvn >/dev/null 2>&1 || { echo "javac/mvn not found: run  sudo apt install -y openjdk-21-jdk-headless maven"; exit 1; }
  down; mkdir -p $D/shop/src/main/java/cloudcart $D/shop/src/main/resources
  cat > $D/shop/pom.xml <<'EOF_P'
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.cloudcart</groupId>
  <artifactId>cart-config</artifactId>
  <version>1.0.0</version>

  <properties>
    <maven.compiler.release>21</maven.compiler.release>
  </properties>

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
  cat > $D/shop/src/main/resources/app.properties <<'EOF_R'
env=${app.env}
greeting=${app.greeting}
EOF_R
  cat > $D/shop/src/main/java/cloudcart/Hello.java <<'EOF_G'
package cloudcart;

import java.io.InputStream;
import java.util.Properties;

public class Hello {
    public static void main(String[] args) throws Exception {
        Properties p = new Properties();
        try (InputStream in = Hello.class.getResourceAsStream("/app.properties")) { p.load(in); }
        System.out.println("[" + p.getProperty("env") + "] " + p.getProperty("greeting") + " from CloudCart");
    }
}
EOF_G
  cat > $D/TASKS.txt <<'EOF_K'
LAB 87 : the cart-config jar cannot run, and its settings are not set.   Work in /opt/lab87/shop

1  Plugin.     Configure maven-jar-plugin so the jar's manifest has  mainClass  cloudcart.Hello
               then  mvn -B package  and  java -jar target/cart-config-1.0.0.jar  must print a line
2  Property.   Add properties  app.env = dev  and  app.greeting = Welcome  to the pom, and turn on
               resource filtering (<filtering>true</filtering> for src/main/resources)
               the jar must print  [dev] Welcome from CloudCart
3  Profile.    Add a profile with id  prod  that sets  app.env  to  prod
               mvn -B clean package -Pprod  then prints  [prod] Welcome from CloudCart
4  Reproduce.  Add the property  project.build.outputTimestamp  with a fixed date, for example 2024-01-01T00:00:00Z
               two clean builds must then make a byte-identical jar
5  Prove it.   Run  mvn -B clean package  and then  sha256sum target/cart-config-1.0.0.jar > sha.txt

Then:  lab check     (all 5 must pass)       and later:  lab down
EOF_K
  chown -R $U $D 2>/dev/null
  echo "lab87 ready: cd $D/shop   (task list: $D/TASKS.txt)"
}
check() {
  [ -d $D/shop ] || { echo "lab not set up: run  lab up"; exit 1; }
  cd $D/shop; ok=0
  as() { if [ "$U" = root ]; then "$@"; else runuser -u $U -- env HOME=$(getent passwd $U | cut -d: -f6) "$@"; fi; }
  pass() { echo "PASS  $1"; ok=$((ok+1)); }
  fail() { echo "FAIL  $1"; }
  W=/tmp/lab87-chk; rm -rf $W; mkdir -p $W; cp -r $D/shop $W/a; cp -r $D/shop $W/b; cp -r $D/shop $W/c; rm -rf $W/*/target $W/*/sha.txt; chown -R $U $W 2>/dev/null
  ( cd $W/a && as mvn -B -q clean package > $W/a.log 2>&1 ); J=$W/a/target/cart-config-1.0.0.jar
  o=$(as java -jar $J 2>&1 | tail -1)
  case "$o" in *"from CloudCart"*) pass "1 java -jar runs the jar (mainClass in the manifest)";; *) fail "1 java -jar runs the jar (mainClass in the manifest)";; esac
  if [ "$o" = "[dev] Welcome from CloudCart" ]; then pass "2 properties filled in: [dev] Welcome from CloudCart"; else fail "2 properties filled in: [dev] Welcome from CloudCart"; fi
  ( cd $W/b && as mvn -B -q clean package -Pprod > $W/b.log 2>&1 ); o=$(as java -jar $W/b/target/cart-config-1.0.0.jar 2>&1 | tail -1)
  if [ "$o" = "[prod] Welcome from CloudCart" ]; then pass "3 profile prod prints [prod] Welcome from CloudCart"; else fail "3 profile prod prints [prod] Welcome from CloudCart"; fi
  sleep 2; ( cd $W/c && as mvn -B -q clean package > $W/c.log 2>&1 )
  if [ -f $J ] && [ -f $W/c/target/cart-config-1.0.0.jar ] && [ "$(sha256sum < $J)" = "$(sha256sum < $W/c/target/cart-config-1.0.0.jar)" ]; then pass "4 two builds make a byte-identical jar"; else fail "4 two builds make a byte-identical jar"; fi
  if [ -f sha.txt ] && [ -f $J ] && [ "$(cut -d' ' -f1 sha.txt)" = "$(sha256sum < $J | cut -d' ' -f1)" ]; then pass "5 sha.txt matches the rebuilt jar"; else fail "5 sha.txt matches the rebuilt jar"; fi
  rm -rf $W
  echo "$ok/5 checks passed"; [ $ok -eq 5 ]
}
status() { [ -d $D ] && echo "lab87 is set up in $D" || echo "lab87 is not set up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab87 removed";; status) status;; *) echo "usage: lab87.sh up|check|down|status"; exit 2;; esac
