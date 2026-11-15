#!/bin/sh
# lab106.sh : MC12-O03 Deploy, verify, redeploy and roll back a WAR built with Maven. Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status
# Needs: JDK, Maven, curl, unzip (sudo apt install -y openjdk-21-jdk-headless maven curl unzip), internet (Tomcat 14 MB, Maven downloads), about 1 GB of memory.
# Mission: build cart 1.0 with Maven, deploy it, verify it, deploy the bad cart 2.0, see it fail, and roll back to 1.0.
D=${LAB106_DIR:-/opt/lab106}
U=${SUDO_USER:-root}
TV=10.1.34
TB=${LAB106_TOMCAT_BASE:-https://archive.apache.org/dist/tomcat/tomcat-10/v$TV/bin}
F=apache-tomcat-$TV.tar.gz
as() { if [ "$U" = root ]; then "$@"; else runuser -u $U -- "$@"; fi; }
down() {
  [ -x $D/tomcat/bin/shutdown.sh ] && as env -u JAVA_TOOL_OPTIONS $D/tomcat/bin/shutdown.sh >/dev/null 2>&1; sleep 3
  pkill -f "catalina.base=$D/tomcat" 2>/dev/null; sleep 1; rm -rf "${D:?}"; true
}
mkproj() { # dir version broken
  p=$1; v=$2; b=$3; mkdir -p $p/src/main/java/com/cloudcart $p/src/main/resources
  cat > $p/pom.xml <<EOF_P
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.cloudcart</groupId>
  <artifactId>cart</artifactId>
  <version>$v</version>
  <packaging>war</packaging>
  <properties>
    <maven.compiler.release>17</maven.compiler.release>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <failOnMissingWebXml>false</failOnMissingWebXml>
  </properties>
  <dependencies>
    <dependency><groupId>jakarta.servlet</groupId><artifactId>jakarta.servlet-api</artifactId><version>6.0.0</version><scope>provided</scope></dependency>
  </dependencies>
  <build>
    <finalName>cart</finalName>
    <resources><resource><directory>src/main/resources</directory><filtering>true</filtering></resource></resources>
    <plugins><plugin><groupId>org.apache.maven.plugins</groupId><artifactId>maven-war-plugin</artifactId><version>3.4.0</version></plugin></plugins>
  </build>
</project>
EOF_P
  printf 'version=${project.version}\n' > $p/src/main/resources/app.properties
  cat > $p/src/main/java/com/cloudcart/HomeServlet.java <<'EOF_H'
package com.cloudcart;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.*;
import java.io.*;
import java.util.Properties;
@WebServlet("/")
public class HomeServlet extends HttpServlet {
  protected void doGet(HttpServletRequest req, HttpServletResponse res) throws IOException {
    Properties p = new Properties();
    try (InputStream in = getClass().getResourceAsStream("/app.properties")) { p.load(in); }
    res.setContentType("text/plain");
    res.getWriter().println("CloudCart " + p.getProperty("version"));
  }
}
EOF_H
  if [ "$b" = bad ]; then
    cat > $p/src/main/java/com/cloudcart/HealthServlet.java <<'EOF_B'
package com.cloudcart;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.*;
import java.io.*;
@WebServlet("/health")
public class HealthServlet extends HttpServlet {
  protected void doGet(HttpServletRequest req, HttpServletResponse res) throws IOException {
    res.sendError(500, "database not configured");
  }
}
EOF_B
  else
    cat > $p/src/main/java/com/cloudcart/HealthServlet.java <<'EOF_G'
package com.cloudcart;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.*;
import java.io.*;
@WebServlet("/health")
public class HealthServlet extends HttpServlet {
  protected void doGet(HttpServletRequest req, HttpServletResponse res) throws IOException {
    res.setContentType("text/plain");
    res.getWriter().println("OK");
  }
}
EOF_G
  fi
}
up() {
  for t in java javac mvn curl unzip tar; do command -v $t >/dev/null 2>&1 || { echo "$t not found: run  sudo apt install -y openjdk-21-jdk-headless maven curl unzip"; exit 1; }; done
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  down; mkdir -p $D/releases
  echo "downloading Tomcat $TV (about 14 MB) ..."
  curl -fL --progress-bar -o $D/t.tgz "$TB/$F" || { echo "download failed"; exit 1; }
  mkdir -p $D/tomcat && tar xzf $D/t.tgz -C $D/tomcat --strip-components=1 || { echo "unpack failed"; exit 1; }; rm -f $D/t.tgz
  mkproj $D/cart-1.0 1.0 good; mkproj $D/cart-2.0 2.0 bad
  cat > $D/TASKS.txt <<'EOF_K'
LAB 106 : MC12 Deploy, verify, redeploy, roll back.   Everything is in /opt/lab106
Tomcat is unpacked in tomcat/ (not running). cart-1.0 is a good release and cart-2.0 is a bad one, both Maven projects. releases/ is empty.

1  Build 1.0:  cd cart-1.0 ; mvn -B -q package ; cp target/cart.war ../releases/cart-1.0.war      (cart.war is the name Tomcat uses for the path /cart)
2  Start Tomcat (tomcat/bin/startup.sh) and deploy: cp releases/cart-1.0.war tomcat/webapps/cart.war   Wait up to 20 s.   curl localhost:8080/cart/ says CloudCart 1.0
3  Verify:  curl -s -o /dev/null -w '%{http_code}\n' localhost:8080/cart/health   must be 200
4  Build 2.0 (cd cart-2.0, same steps), keep it as releases/cart-2.0.war, deploy it over webapps/cart.war, wait, and verify. It fails: /cart/health answers 500.
5  Roll back: copy releases/cart-1.0.war over webapps/cart.war, wait, and verify that 1.0 works again.
6  Write history.txt in /opt/lab106, three lines:   v1: 200    v2: 500    rollback: 200      (the real health codes you saw, after each deploy)
Then:  lab check     (all 5 must pass)       and later:  lab down   (it stops Tomcat and removes everything)
EOF_K
  chown -R $U $D; chmod 755 $D
  echo "lab106 ready: cd $D   (task list: $D/TASKS.txt)"
}
ver() { unzip -p "$1" META-INF/maven/com.cloudcart/cart/pom.properties 2>/dev/null | grep '^version=' | cut -d= -f2; }
check() {
  [ -d $D/releases ] || { echo "lab not set up: run  lab up"; exit 1; }
  ok=0
  pass() { echo "PASS  $1"; ok=$((ok+1)); }
  fail() { echo "FAIL  $1"; }
  if [ "$(ver $D/releases/cart-1.0.war)" = 1.0 ]; then pass "1 releases/cart-1.0.war was built by Maven (version 1.0)"; else fail "1 build 1.0 with mvn package and copy target/cart.war to releases/cart-1.0.war"; fi
  if [ "$(ver $D/releases/cart-2.0.war)" = 2.0 ]; then pass "2 releases/cart-2.0.war was built by Maven (version 2.0)"; else fail "2 build 2.0 the same way and keep it as releases/cart-2.0.war"; fi
  b=$(curl -s -m 5 localhost:8080/cart/ 2>/dev/null); if [ "$b" = "CloudCart 1.0" ]; then pass "3 /cart/ serves CloudCart 1.0: the rollback worked"; else fail "3 /cart/ must serve CloudCart 1.0 now (it says: ${b:-nothing}); Tomcat running? rolled back?"; fi
  c=$(curl -s -m 5 -o /dev/null -w '%{http_code}' localhost:8080/cart/health 2>/dev/null); if [ "$c" = 200 ]; then pass "4 /cart/health answers 200"; else fail "4 /cart/health answers $c, it must be 200"; fi
  H=$D/history.txt
  if grep -qE '^v1: *200$' $H 2>/dev/null && grep -qE '^v2: *500$' $H && grep -qE '^rollback: *200$' $H; then pass "5 history.txt records v1: 200, v2: 500 and rollback: 200"; else fail "5 history.txt needs three lines: v1: 200   v2: 500   rollback: 200"; fi
  echo "$ok/5 checks passed"; [ $ok -eq 5 ]
}
status() { [ -d $D ] && echo "lab106 is set up in $D" || echo "lab106 is not set up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab106 removed";; status) status;; *) echo "usage: lab106.sh up|check|down|status"; exit 2;; esac
