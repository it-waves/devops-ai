#!/bin/sh
# lab81.sh : stack traces, exceptions and logs (MC09-O06). Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status        Needs a JDK (sudo apt install -y openjdk-21-jdk-headless).
# Mission: run a crashing program, read its stack trace, and find the same failure in a log file.
D=/opt/lab81
U=${SUDO_USER:-root}
down() { rm -rf $D; true; }
up() {
  command -v javac >/dev/null 2>&1 || { echo "javac not found: run  sudo apt install -y openjdk-21-jdk-headless"; exit 1; }
  down; mkdir -p $D/src/com/cloudcart
  cat > $D/src/com/cloudcart/Checkout.java <<'EOF_J'
package com.cloudcart;

public class Checkout {
    static int price(String item) {
        return Integer.parseInt(item);
    }

    static int total(String[] items) {
        int sum = 0;
        for (String item : items) {
            sum += price(item);
        }
        return sum;
    }

    static int process(String[] items) {
        try {
            return total(items);
        } catch (NumberFormatException e) {
            throw new IllegalStateException("cannot price order", e);
        }
    }

    public static void main(String[] args) {
        String[] cart = {"10", "20", "x5"};
        System.out.println("order total: " + process(cart));
    }
}
EOF_J
  cat > $D/app.log <<'EOF_L'
2026-11-13 09:14:01 INFO  Checkout started order=1041
2026-11-13 09:14:01 INFO  Order paid order=1041 total=30
2026-11-13 09:14:02 INFO  Checkout started order=1042
2026-11-13 09:14:03 WARN  Slow price lookup item=a7 ms=1840
2026-11-13 09:14:04 ERROR Cannot price order order=1042
    at com.cloudcart.Checkout.process(Checkout.java:20)
    at com.cloudcart.Checkout.main(Checkout.java:26)
2026-11-13 09:14:05 INFO  Checkout started order=1043
2026-11-13 09:14:05 INFO  Order paid order=1043 total=45
2026-11-13 09:14:09 WARN  Slow price lookup item=b2 ms=2210
2026-11-13 09:14:12 ERROR Cannot price order order=1044
    at com.cloudcart.Checkout.process(Checkout.java:20)
    at com.cloudcart.Checkout.main(Checkout.java:26)
2026-11-13 09:14:13 INFO  Checkout started order=1045
EOF_L
  cat > $D/TASKS.txt <<'EOF_T'
Tasks (work inside /opt/lab81, then run: lab check)
1  Compile Checkout into out/:                       javac -d out src/com/cloudcart/Checkout.java
2  Run it and save ONLY the error output:            java -cp out com.cloudcart.Checkout 2> crash.txt
3  Save every ERROR line of the log:                 grep ERROR app.log > errors.txt
4  Save how many ERROR lines there are:              grep -c ERROR app.log > count.txt
5  answers.txt, exactly these three lines (read crash.txt to find them):
     top exception: IllegalStateException
     root cause: NumberFormatException
     bad value: x5
EOF_T
  chown -R $U $D
}
check() {
  say() { if [ "$1" = ok ]; then echo "PASS  $2"; p=$((p+1)); else echo "FAIL  $2"; fi; }
  p=0
  [ "$(head -c 4 $D/out/com/cloudcart/Checkout.class 2>/dev/null | od -An -tx1 | tr -d ' \n')" = cafebabe ] && r=ok || r=no; say $r "1 Checkout compiled into out/"
  grep -q 'Caused by: java.lang.NumberFormatException' $D/crash.txt 2>/dev/null && grep -q 'For input string: "x5"' $D/crash.txt 2>/dev/null && ! grep -q 'order total' $D/crash.txt 2>/dev/null && r=ok || r=no; say $r "2 crash.txt holds the stack trace"
  n=$(grep -c ERROR $D/app.log 2>/dev/null); m=$(grep -c ERROR $D/errors.txt 2>/dev/null); l=$(cat $D/errors.txt 2>/dev/null | wc -l)
  [ -n "$n" ] && [ "$n" -gt 0 ] && [ "$m" = "$n" ] && [ "$l" = "$n" ] && r=ok || r=no; say $r "3 errors.txt holds the ERROR lines of the log"
  [ -n "$n" ] && [ "$(cat $D/count.txt 2>/dev/null | tr -d " \n")" = "$n" ] && r=ok || r=no; say $r "4 count.txt has the number of ERROR lines"
  grep -q '^top exception: *IllegalStateException *$' $D/answers.txt 2>/dev/null && grep -q '^root cause: *NumberFormatException *$' $D/answers.txt 2>/dev/null && grep -q '^bad value: *x5 *$' $D/answers.txt 2>/dev/null && r=ok || r=no; say $r "5 answers.txt: three lines"
  echo "$p of 5 pass"
}
case "$1" in
  up) up;; check) check;; down) down; echo "lab removed";; status) ls $D 2>/dev/null || echo "not installed";;
  *) echo "usage: lab81.sh up|check|down|status";;
esac
