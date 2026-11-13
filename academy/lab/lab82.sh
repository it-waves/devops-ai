#!/bin/sh
# lab82.sh : Java tests and build outputs (MC09-O07). Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status        Needs a JDK (sudo apt install -y openjdk-21-jdk-headless).
# Mission: build, run a failing test, fix the bug, see it go green, and package the build output.
D=/opt/lab82
U=${SUDO_USER:-root}
down() { rm -rf $D; true; }
up() {
  command -v javac >/dev/null 2>&1 && command -v jar >/dev/null 2>&1 || { echo "javac/jar not found: run  sudo apt install -y openjdk-21-jdk-headless"; exit 1; }
  down; mkdir -p $D/src/main/com/cloudcart $D/src/test/com/cloudcart
  cat > $D/src/main/com/cloudcart/Cart.java <<'EOF_M'
package com.cloudcart;

public class Cart {
    static int sum(int a, int b) {
        return a + b;
    }

    static int discounted(int total) {
        return total / 10;
    }
}
EOF_M
  cat > $D/src/test/com/cloudcart/CartTest.java <<'EOF_T'
package com.cloudcart;

public class CartTest {
    static int passed = 0;
    static int failed = 0;

    static void check(String name, int expected, int actual) {
        if (expected == actual) {
            passed++;
            System.out.println("PASS " + name);
        } else {
            failed++;
            System.out.println("FAIL " + name + ": expected " + expected + " got " + actual);
        }
    }

    public static void main(String[] args) {
        check("sum of 10 and 20", 30, Cart.sum(10, 20));
        check("sum of zero", 0, Cart.sum(0, 0));
        check("10 percent off 200", 180, Cart.discounted(200));
        System.out.println(passed + " passed, " + failed + " failed");
        if (failed > 0) {
            System.exit(1);
        }
    }
}
EOF_T
  cat > $D/TASKS.txt <<'EOF_K'
Tasks (work inside /opt/lab82, then run: lab check)
1  Compile main into out/main and the test into out/test
     javac -d out/main src/main/com/cloudcart/Cart.java
     javac -cp out/main -d out/test src/test/com/cloudcart/CartTest.java
2  Run the test BEFORE fixing anything and save the output:
     java -cp out/main:out/test com.cloudcart.CartTest > test-before.txt
3  Fix the bug in src/main/com/cloudcart/Cart.java (the 10 percent discount is wrong), then rebuild main
4  Run the test again, saved to test-after.txt, and pack the MAIN classes only into a jar:
     java -cp out/main:out/test com.cloudcart.CartTest > test-after.txt
     jar cf cloudcart.jar -C out/main .
5  answers.txt, exactly these three lines:
     failed test exits with: non-zero
     build output folder: out
     jar holds: compiled classes
EOF_K
  chown -R $U $D
}
check() {
  say() { if [ "$1" = ok ]; then echo "PASS  $2"; p=$((p+1)); else echo "FAIL  $2"; fi; }
  magic() { [ "$(head -c 4 "$1" 2>/dev/null | od -An -tx1 | tr -d ' \n')" = cafebabe ]; }
  p=0
  magic $D/out/main/com/cloudcart/Cart.class && magic $D/out/test/com/cloudcart/CartTest.class && r=ok || r=no; say $r "1 main and test compiled into out/main and out/test"
  grep -q '^FAIL ' $D/test-before.txt 2>/dev/null && grep -q 'failed' $D/test-before.txt 2>/dev/null && r=ok || r=no; say $r "2 test-before.txt shows a failing test"
  T=$(mktemp -d); mkdir -p $T/m $T/t
  javac -d $T/m $D/src/main/com/cloudcart/Cart.java 2>/dev/null && javac -cp $T/m -d $T/t $D/src/test/com/cloudcart/CartTest.java 2>/dev/null && java -cp $T/m:$T/t com.cloudcart.CartTest >/dev/null 2>&1 && r=ok || r=no; rm -rf $T; say $r "3 Cart.java is fixed: the test passes when rebuilt from source"
  grep -q ' 0 failed' $D/test-after.txt 2>/dev/null && jar tf $D/cloudcart.jar 2>/dev/null | grep -qx 'com/cloudcart/Cart.class' && ! jar tf $D/cloudcart.jar 2>/dev/null | grep -q 'CartTest' && r=ok || r=no; say $r "4 test-after.txt is green and cloudcart.jar holds Cart only"
  grep -q '^failed test exits with: *non-zero *$' $D/answers.txt 2>/dev/null && grep -q '^build output folder: *out *$' $D/answers.txt 2>/dev/null && grep -q '^jar holds: *compiled classes *$' $D/answers.txt 2>/dev/null && r=ok || r=no; say $r "5 answers.txt: three lines"
  echo "$p of 5 pass"
}
case "$1" in
  up) up;; check) check;; down) down; echo "lab removed";; status) ls $D 2>/dev/null || echo "not installed";;
  *) echo "usage: lab82.sh up|check|down|status";;
esac
