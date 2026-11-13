#!/bin/sh
# lab78.sh : packages, classpath, dependencies, configuration (MC09-O03). Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status        Needs a JDK (sudo apt install -y openjdk-21-jdk-headless).
# Mission: compile and run a project that depends on a jar, configure it from outside, and break the class path on purpose.
D=/opt/lab78
U=${SUDO_USER:-root}
down() { rm -rf $D; true; }
up() {
  command -v javac >/dev/null 2>&1 && command -v jar >/dev/null 2>&1 || { echo "javac/jar not found: run  sudo apt install -y openjdk-21-jdk-headless"; exit 1; }
  down; mkdir -p $D/src/com/cloudcart $D/lib $D/build.tmp/com/cloudcart/pricing
  cat > $D/build.tmp/Tax.java <<'EOF_X'
package com.cloudcart.pricing;
public class Tax {
    public static double withTax(double price) { return Math.round(price * 108) / 100.0; }
}
EOF_X
  javac -d $D/build.tmp $D/build.tmp/Tax.java && (cd $D/build.tmp && jar cf ../lib/pricing.jar com)
  rm -rf $D/build.tmp
  cat > $D/src/com/cloudcart/Main.java <<'EOF_M'
package com.cloudcart;

import com.cloudcart.pricing.Tax;

public class Main {
    public static void main(String[] args) {
        String store = System.getenv().getOrDefault("STORE_NAME", "unset");
        String cur = System.getProperty("currency", "USD");
        System.out.println("Store: " + store);
        System.out.println("Currency: " + cur);
        System.out.println("Total: " + Tax.withTax(100.0));
    }
}
EOF_M
  cat > $D/TASKS.txt <<'EOF_T'
Tasks (work inside /opt/lab78, then run: lab check)
1  Compile Main with the jar on the class path:        javac -cp lib/pricing.jar -d out src/com/cloudcart/Main.java
2  Run it with the full class path, save the output:   java -cp out:lib/pricing.jar com.cloudcart.Main > run.txt
3  Run it configured, save the output:                 STORE_NAME=Bean java -Dcurrency=EUR -cp out:lib/pricing.jar com.cloudcart.Main > config.txt
4  Run it WITHOUT the jar, save the error:             java -cp out com.cloudcart.Main 2> fail.txt
5  answers.txt, exactly these three lines:
     package: folder path
     classpath: where java looks for classes
     dependency: a jar on the classpath
EOF_T
  chown -R $U $D
}
check() {
  say() { if [ "$1" = ok ]; then echo "PASS  $2"; p=$((p+1)); else echo "FAIL  $2"; fi; }
  magic() { [ "$(head -c 4 "$1" 2>/dev/null | od -An -tx1 | tr -d ' \n')" = cafebabe ]; }
  p=0
  magic $D/out/com/cloudcart/Main.class && r=ok || r=no; say $r "1 Main compiled into out/ with the jar on the class path"
  grep -q '^Total: 108.0$' $D/run.txt 2>/dev/null && r=ok || r=no; say $r "2 run.txt shows Total: 108.0"
  grep -q '^Store: Bean$' $D/config.txt 2>/dev/null && grep -q '^Currency: EUR$' $D/config.txt 2>/dev/null && r=ok || r=no; say $r "3 config.txt shows Store: Bean and Currency: EUR"
  grep -q 'NoClassDefFoundError' $D/fail.txt 2>/dev/null && r=ok || r=no; say $r "4 fail.txt holds the NoClassDefFoundError"
  grep -q '^package: *folder path *$' $D/answers.txt 2>/dev/null && grep -q '^classpath: *where java looks for classes *$' $D/answers.txt 2>/dev/null && grep -q '^dependency: *a jar on the classpath *$' $D/answers.txt 2>/dev/null && r=ok || r=no; say $r "5 answers.txt: three lines"
  echo "$p of 5 pass"
}
case "$1" in
  up) up;; check) check;; down) down; echo "lab removed";; status) ls $D 2>/dev/null || echo "not installed";;
  *) echo "usage: lab78.sh up|check|down|status";;
esac
