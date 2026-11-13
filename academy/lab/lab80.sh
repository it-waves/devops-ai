#!/bin/sh
# lab80.sh : JAR vs WAR (MC09-O05). Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status        Needs a JDK (sudo apt install -y openjdk-21-jdk-headless).
# Mission: build a runnable jar, build a war from a web folder, and say what each one needs.
D=/opt/lab80
U=${SUDO_USER:-root}
down() { rm -rf $D; true; }
up() {
  command -v javac >/dev/null 2>&1 && command -v jar >/dev/null 2>&1 || { echo "javac/jar not found: run  sudo apt install -y openjdk-21-jdk-headless"; exit 1; }
  down; mkdir -p $D/src/com/cloudcart $D/war/WEB-INF
  cat > $D/src/com/cloudcart/Hello.java <<'EOF_H'
package com.cloudcart;

public class Hello {
    public static void main(String[] args) {
        System.out.println("CloudCart is ready");
    }
}
EOF_H
  echo '<html><body><h1>CloudCart shop</h1></body></html>' > $D/war/index.html
  cat > $D/war/WEB-INF/web.xml <<'EOF_W'
<web-app version="6.0">
  <display-name>cloudcart</display-name>
  <welcome-file-list>
    <welcome-file>index.html</welcome-file>
  </welcome-file-list>
</web-app>
EOF_W
  cat > $D/TASKS.txt <<'EOF_T'
Tasks (work inside /opt/lab80, then run: lab check)
1  Compile Hello into out/:                         javac -d out src/com/cloudcart/Hello.java
2  Build a RUNNABLE jar, run it, save the output:   jar cfe app.jar com.cloudcart.Hello -C out .     java -jar app.jar > jar-run.txt
3  Build a war from the war folder:                 jar cf shop.war -C war .
4  Save the war's contents:                         jar tf shop.war > war-list.txt
5  answers.txt, exactly these three lines:
     jar runs with: java -jar
     war needs: a servlet container
     manifest holds: main class
EOF_T
  chown -R $U $D
}
check() {
  say() { if [ "$1" = ok ]; then echo "PASS  $2"; p=$((p+1)); else echo "FAIL  $2"; fi; }
  magic() { [ "$(head -c 4 "$1" 2>/dev/null | od -An -tx1 | tr -d ' \n')" = cafebabe ]; }
  p=0
  magic $D/out/com/cloudcart/Hello.class && r=ok || r=no; say $r "1 Hello compiled into out/"
  T=$(mktemp -d); (cd $T && jar xf $D/app.jar META-INF/MANIFEST.MF 2>/dev/null); M=$(cat $T/META-INF/MANIFEST.MF 2>/dev/null); rm -rf $T $PWD/META-INF 2>/dev/null
  echo "$M" | grep -q 'Main-Class: com.cloudcart.Hello' && grep -q '^CloudCart is ready$' $D/jar-run.txt 2>/dev/null && r=ok || r=no; say $r "2 app.jar is runnable and jar-run.txt shows its output"
  jar tf $D/shop.war 2>/dev/null | grep -qx 'WEB-INF/web.xml' && jar tf $D/shop.war 2>/dev/null | grep -qx 'index.html' && r=ok || r=no; say $r "3 shop.war has index.html and WEB-INF/web.xml"
  grep -q 'WEB-INF/web.xml' $D/war-list.txt 2>/dev/null && r=ok || r=no; say $r "4 war-list.txt lists the war contents"
  grep -q '^jar runs with: *java -jar *$' $D/answers.txt 2>/dev/null && grep -q '^war needs: *a servlet container *$' $D/answers.txt 2>/dev/null && grep -q '^manifest holds: *main class *$' $D/answers.txt 2>/dev/null && r=ok || r=no; say $r "5 answers.txt: three lines"
  echo "$p of 5 pass"
}
case "$1" in
  up) up;; check) check;; down) down; echo "lab removed";; status) ls $D 2>/dev/null || echo "not installed";;
  *) echo "usage: lab80.sh up|check|down|status";;
esac
