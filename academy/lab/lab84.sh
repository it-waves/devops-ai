#!/bin/sh
# lab84.sh : Java mastery lab, release triage for the CloudCart orders service (MC09). Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status        Needs a JDK (sudo apt install -y openjdk-21-jdk-headless).
# Mission: release 1.4 of the orders service will not ship. Four faults hide in the build, the jar and the launcher. Find each from its error, fix it, write a report.
D=${LAB84_DIR:-/opt/lab84}
U=${SUDO_USER:-root}
down() { rm -rf $D; true; }
up() {
  command -v javac >/dev/null 2>&1 && command -v jar >/dev/null 2>&1 || { echo "javac/jar not found: run  sudo apt install -y openjdk-21-jdk-headless"; exit 1; }
  down; mkdir -p $D/src/cloudcart $D/test/cloudcart $D/logs
  cat > $D/src/cloudcart/Orders.java <<'EOF_O'
package cloudcart;

import java.net.ServerSocket;

public class Orders {
    static final int SHIPPING = 250;

    static int total(int price, int qty) {
        return price * qty - SHIPPING;
    }

    public static void main(String[] args) throws Exception {
        int port = Integer.parseInt(System.getenv("ORDERS_PORT"));
        byte[] catalog = new byte[24 * 1024 * 1024];
        try (ServerSocket s = new ServerSocket(port)) {
            System.out.println("OK orders listening on " + port + " (catalog " + catalog.length / (1024 * 1024) + " MB)");
        }
    }
}
EOF_O
  cat > $D/test/cloudcart/OrdersTest.java <<'EOF_T'
package cloudcart;

public class OrdersTest {
    static int failed = 0;

    static void check(String name, int expected, int got) {
        if (expected == got) System.out.println("PASS " + name);
        else { System.out.println("FAIL " + name + ": expected " + expected + " got " + got); failed++; }
    }

    public static void main(String[] args) {
        check("total two items", 1250, Orders.total(500, 2));
        check("total one item", 350, Orders.total(100, 1));
        System.exit(failed == 0 ? 0 : 1);
    }
}
EOF_T
  cat > $D/build.sh <<'EOF_B'
#!/bin/sh
cd "$(dirname "$0")"
rm -rf out out-test build; mkdir -p out out-test build
javac -d out src/cloudcart/Orders.java || exit 1
javac -cp out -d out-test test/cloudcart/OrdersTest.java || exit 1
java -cp out:out-test cloudcart.OrdersTest || { echo "BUILD FAILED: tests"; exit 1; }
jar cf build/orders.jar -C out .
echo "BUILD OK build/orders.jar"
EOF_B
  cat > $D/orders.env <<'EOF_E'
ORDERS_PORT=eighty
JAVA_OPTS=-Xmx8m
EOF_E
  cat > $D/run-orders.sh <<'EOF_R'
#!/bin/sh
cd "$(dirname "$0")"
mkdir -p logs
. ./orders.env
export ORDERS_PORT
java $JAVA_OPTS -jar build/orders.jar > logs/orders.log 2>&1
c=$?
if [ $c -eq 0 ]; then cat logs/orders.log; else echo "orders failed (exit $c), see logs/orders.log"; fi
exit $c
EOF_R
  chmod +x $D/build.sh $D/run-orders.sh
  cat > $D/TASKS.txt <<'EOF_K'
Tasks (work inside /opt/lab84, then run: lab check)
Release 1.4 of the orders service will not ship. Run sh build.sh, then sh run-orders.sh, and keep going until it prints OK.
Read the error each time, name the cause, change one thing, run again. The log is logs/orders.log.
1  sh build.sh        a unit test fails. The total must add shipping, not subtract it. Edit src/cloudcart/Orders.java
2  sh run-orders.sh   the jar has no Main-Class. Fix build.sh so the jar is made with an entry point: jar cfe build/orders.jar cloudcart.Orders -C out .   then sh build.sh
3  sh run-orders.sh   the port in orders.env is not a number. Give ORDERS_PORT a real port, for example 18090
4  sh run-orders.sh   the heap limit in orders.env is too small. Raise JAVA_OPTS to -Xmx128m
5  report.txt         four lines, one per fault: what you saw, the cause, your fix. Mention test, manifest, port and heap.
6  cleanup            when done: lab down, then prove nothing is left (ls /opt/lab84 and pgrep java show nothing)
EOF_K
  chown -R $U $D
}
check() {
  say() { if [ "$1" = ok ]; then echo "PASS  $2"; p=$((p+1)); else echo "FAIL  $2"; fi; }
  as() { if [ "$U" = root ]; then "$@"; else runuser -u $U -- "$@"; fi; }
  p=0
  b=$(cd $D && as timeout 60 sh ./build.sh 2>&1); bc=$?
  [ $bc -eq 0 ] && echo "$b" | grep -q '^BUILD OK' && r=ok || r=no; say $r "1 sh build.sh passes (tests green)"
  [ -f $D/build/orders.jar ] && unzip -p $D/build/orders.jar META-INF/MANIFEST.MF 2>/dev/null | grep -q '^Main-Class: cloudcart.Orders' && r=ok || r=no; say $r "2 the jar has a Main-Class"
  grep -Eq '^ORDERS_PORT=[0-9]+ *$' $D/orders.env 2>/dev/null && r=ok || r=no; say $r "3 ORDERS_PORT is a number"
  m=$(sed -n 's/^JAVA_OPTS=.*-Xmx\([0-9]*\)m.*/\1/p' $D/orders.env 2>/dev/null | head -1); [ -n "$m" ] && [ "$m" -ge 64 ] && r=ok || r=no; say $r "4 heap limit is 64 MB or more"
  o=$(cd $D && as timeout 30 sh ./run-orders.sh 2>&1); c=$?
  [ $c -eq 0 ] && echo "$o" | grep -Eq '^OK orders listening on [0-9]+' && r=ok || r=no; say $r "5 sh run-orders.sh prints OK"
  R=$D/report.txt
  [ -f $R ] && [ "$(grep -c . $R)" -ge 4 ] && grep -qi 'test' $R && grep -qi 'manifest' $R && grep -qi 'port' $R && grep -Eqi 'heap|xmx|memory' $R && r=ok || r=no; say $r "6 report.txt covers test, manifest, port and heap"
  echo "$p of 6 pass"
}
case "$1" in
  up) up;; check) check;; down) down; echo "lab removed";; status) ls $D 2>/dev/null || echo "not installed";;
  *) echo "usage: lab84.sh up|check|down|status";;
esac
