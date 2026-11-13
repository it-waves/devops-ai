#!/bin/sh
# lab83.sh : diagnose Java failures (MC09-O08). Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status        Needs a JDK (sudo apt install -y openjdk-21-jdk-headless).
# Mission: four launcher scripts fail for four different reasons. Read each error, name it, fix it.
D=${LAB83_DIR:-/opt/lab83}
U=${SUDO_USER:-root}
down() { rm -rf $D; true; }
up() {
  command -v javac >/dev/null 2>&1 && command -v jar >/dev/null 2>&1 || { echo "javac/jar not found: run  sudo apt install -y openjdk-21-jdk-headless"; exit 1; }
  down; mkdir -p $D/ver/src/cloudcart $D/ver/classes $D/mem/src/cloudcart $D/mem/classes $D/port/src/cloudcart $D/port/classes $D/cp/src/cloudcart $D/cp/classes $D/cp/lib
  cat > $D/ver/src/cloudcart/Greeter.java <<'EOF_V'
package cloudcart;

public class Greeter {
    public static void main(String[] args) {
        System.out.println("OK version");
    }
}
EOF_V
  cat > $D/mem/src/cloudcart/Hog.java <<'EOF_M'
package cloudcart;

public class Hog {
    public static void main(String[] args) {
        byte[] report = new byte[64 * 1024 * 1024];
        System.out.println("OK memory " + report.length);
    }
}
EOF_M
  cat > $D/port/src/cloudcart/Server.java <<'EOF_P'
package cloudcart;

import java.net.ServerSocket;

public class Server {
    public static void main(String[] args) throws Exception {
        int port = Integer.parseInt(args[0]);
        try (ServerSocket s = new ServerSocket(port)) {
            System.out.println("OK port " + port);
            Thread.sleep(2500);
        }
    }
}
EOF_P
  cat > $D/cp/src/cloudcart/Helper.java <<'EOF_H'
package cloudcart;

public class Helper {
    public static String name() {
        return "classpath";
    }
}
EOF_H
  cat > $D/cp/src/cloudcart/Tool.java <<'EOF_T'
package cloudcart;

public class Tool {
    public static void main(String[] args) {
        System.out.println("OK " + Helper.name());
    }
}
EOF_T
  # version fault: compile for this JDK, then raise the class file version number to 69 (a newer Java than 21)
  javac --release 21 -d $D/ver/classes $D/ver/src/cloudcart/Greeter.java
  printf '\105' | dd of=$D/ver/classes/cloudcart/Greeter.class bs=1 seek=7 conv=notrunc 2>/dev/null
  javac -d $D/mem/classes $D/mem/src/cloudcart/Hog.java
  javac -d $D/port/classes $D/port/src/cloudcart/Server.java
  javac -d $D/cp/lib/tmp $D/cp/src/cloudcart/Helper.java && jar cf $D/cp/lib/helper.jar -C $D/cp/lib/tmp . && rm -rf $D/cp/lib/tmp
  javac -cp $D/cp/lib/helper.jar -d $D/cp/classes $D/cp/src/cloudcart/Tool.java
  cat > $D/run-version.sh <<'EOF_R1'
#!/bin/sh
cd "$(dirname "$0")"
java -cp ver/classes cloudcart.Greeter
EOF_R1
  cat > $D/run-memory.sh <<'EOF_R2'
#!/bin/sh
cd "$(dirname "$0")"
java -Xmx16m -cp mem/classes cloudcart.Hog
EOF_R2
  cat > $D/run-port.sh <<'EOF_R3'
#!/bin/sh
cd "$(dirname "$0")"
java -cp port/classes cloudcart.Server 18083 &
FIRST=$!
sleep 1
java -cp port/classes cloudcart.Server 18083 || exit 1
wait $FIRST
EOF_R3
  cat > $D/run-classpath.sh <<'EOF_R4'
#!/bin/sh
cd "$(dirname "$0")"
java -cp cp/classes cloudcart.Tool
EOF_R4
  chmod +x $D/run-*.sh
  cat > $D/TASKS.txt <<'EOF_K'
Tasks (work inside /opt/lab83, then run: lab check)
Four scripts fail. For each one: run it, read the first error line, find the cause, fix it so it prints OK.
1  sh run-version.sh     the class was built for a newer Java. Rebuild it from ver/src with this JDK:
                         javac -d ver/classes ver/src/cloudcart/Greeter.java
2  sh run-memory.sh      the heap limit is too small. Edit the script: raise -Xmx16m to -Xmx256m
3  sh run-port.sh        two servers want the same port. Edit the script: the second server gets 18084
4  sh run-classpath.sh   a dependency jar is missing from -cp. Edit the script: -cp cp/classes:cp/lib/helper.jar
5  diag.txt, exactly these four lines (exception name per fault):
     version: UnsupportedClassVersionError
     memory: OutOfMemoryError
     port: BindException
     classpath: NoClassDefFoundError
EOF_K
  chown -R $U $D
}
check() {
  say() { if [ "$1" = ok ]; then echo "PASS  $2"; p=$((p+1)); else echo "FAIL  $2"; fi; }
  runs() { o=$(cd $D && timeout 30 sh ./$1 2>&1); c=$?; [ $c -eq 0 ] && echo "$o" | grep -q "^OK $2" && ! grep -q 'echo' $D/$1 2>/dev/null; }
  p=0
  runs run-version.sh version && r=ok || r=no; say $r "1 run-version.sh prints OK (class rebuilt for this JDK)"
  runs run-memory.sh memory && r=ok || r=no; say $r "2 run-memory.sh prints OK (heap limit raised)"
  runs run-port.sh port && r=ok || r=no; say $r "3 run-port.sh prints OK (second server on a free port)"
  runs run-classpath.sh classpath && r=ok || r=no; say $r "4 run-classpath.sh prints OK (jar on the classpath)"
  grep -q '^version: *UnsupportedClassVersionError *$' $D/diag.txt 2>/dev/null && grep -q '^memory: *OutOfMemoryError *$' $D/diag.txt 2>/dev/null && grep -q '^port: *BindException *$' $D/diag.txt 2>/dev/null && grep -q '^classpath: *NoClassDefFoundError *$' $D/diag.txt 2>/dev/null && r=ok || r=no; say $r "5 diag.txt names the four failures"
  echo "$p of 5 pass"
}
case "$1" in
  up) up;; check) check;; down) down; echo "lab removed";; status) ls $D 2>/dev/null || echo "not installed";;
  *) echo "usage: lab83.sh up|check|down|status";;
esac
