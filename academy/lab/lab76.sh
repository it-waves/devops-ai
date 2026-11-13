#!/bin/sh
# lab76.sh : Java basics lab (MC09-O01). Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status        Needs a JDK (sudo apt install -y openjdk-21-jdk-headless).
# Mission: see the versions, compile source into bytecode, read the bytecode, start the application and find its process.
D=/opt/lab76
U=${SUDO_USER:-root}
stopall() { pkill -f "java ShopApp" 2>/dev/null; sleep 0.5; true; }
down() { stopall; rm -rf $D; true; }
put() { cat > "$D/$1"; }
up() {
  command -v javac >/dev/null 2>&1 || { echo "javac not found: run  sudo apt install -y openjdk-21-jdk-headless"; exit 1; }
  down; mkdir -p $D
  put Hello.java <<'EOF_Hello'
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello from CloudCart");
        System.out.println("Running on Java " + Runtime.version().feature());
    }
}
EOF_Hello
  put ShopApp.java <<'EOF_ShopApp'
public class ShopApp {
    public static void main(String[] args) throws Exception {
        System.out.println("ShopApp started, process id " + ProcessHandle.current().pid());
        while (true) { Thread.sleep(1000); }
    }
}
EOF_ShopApp
  put TASKS.txt <<'EOF_T'
Tasks (work inside /opt/lab76, then run: lab check)
1  versions.txt  : the output of  java -version  and  javac -version  (both, 2>&1 is needed for java)
2  Compile both programs so the .class files exist:  javac Hello.java ShopApp.java   then run:  java Hello
3  bytecode.txt  : the output of  javap -c Hello
4  Start ShopApp in the background:  java ShopApp > app.log &   then save  jps -l  into  process.txt
5  answers.txt, exactly these three lines, with your answers:
     javac comes with: JDK or JRE
     bytecode lives in: a file ending in .java or .class
     the program runs as: a process
   (write them as   javac: JDK   bytecode: .class   process: java )
Leave ShopApp running when you run lab check.
EOF_T
  chown -R $U $D
}
check() {
  say() { if [ "$1" = ok ]; then echo "PASS  $2"; p=$((p+1)); else echo "FAIL  $2"; fi; }
  p=0
  grep -q 'version "' $D/versions.txt 2>/dev/null && grep -q '^javac ' $D/versions.txt 2>/dev/null && r=ok || r=no; say $r "1 versions.txt: java and javac versions"
  [ "$(head -c 4 $D/Hello.class 2>/dev/null | od -An -tx1 | tr -d ' \n')" = cafebabe ] && r=ok || r=no; say $r "2 Hello.class exists and is real bytecode"
  grep -q 'invokevirtual' $D/bytecode.txt 2>/dev/null && grep -q 'Compiled from "Hello.java"' $D/bytecode.txt 2>/dev/null && r=ok || r=no; say $r "3 bytecode.txt: javap output for Hello"
  pid=$(pgrep -f "java ShopApp" | head -1); [ -n "$pid" ] && grep -q "^$pid ShopApp" $D/process.txt 2>/dev/null && r=ok || r=no; say $r "4 ShopApp is running and process.txt lists it"
  grep -q '^javac: *JDK *$' $D/answers.txt 2>/dev/null && grep -q '^bytecode: *\.class *$' $D/answers.txt 2>/dev/null && grep -q '^process: *java *$' $D/answers.txt 2>/dev/null && r=ok || r=no; say $r "5 answers.txt: javac: JDK, bytecode: .class, process: java"
  echo "$p of 5 pass"
}
case "$1" in
  up) up;; check) check;; down) down; echo "lab removed";; status) ls $D 2>/dev/null || echo "not installed";;
  *) echo "usage: lab76.sh up|check|down|status";;
esac
