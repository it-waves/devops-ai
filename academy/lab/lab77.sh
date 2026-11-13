#!/bin/sh
# lab77.sh : compile and run lab (MC09-O02). Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status        Needs a JDK (sudo apt install -y openjdk-21-jdk-headless).
# Mission: compile and run a program, read its exit code, capture and fix a compile error.
D=/opt/lab77
U=${SUDO_USER:-root}
down() { rm -rf $D; true; }
put() { cat > "$D/$1"; }
up() {
  command -v javac >/dev/null 2>&1 || { echo "javac not found: run  sudo apt install -y openjdk-21-jdk-headless"; exit 1; }
  down; mkdir -p $D
  put Greeter.java <<'EOF_G'
public class Greeter {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.err.println("usage: java Greeter NAME");
            System.exit(2);
        }
        System.out.println("Hello, " + args[0] + "!");
    }
}
EOF_G
  put Broken.java <<'EOF_B'
public class Broken {
    public static void main(String[] args) {
        System.out.println("Fixed: it compiles now")
    }
}
EOF_B
  put TASKS.txt <<'EOF_T'
Tasks (work inside /opt/lab77, then run: lab check)
1  Compile Greeter, then run it with the name Ada and save the output:      javac Greeter.java       java Greeter Ada > run.txt
2  Run Greeter with no name and save its exit code:                         java Greeter             echo $? > exit.txt
3  Compile Broken and save the error message (javac writes it to stderr):    javac Broken.java 2> error.txt
4  Fix Broken.java (one character), compile it, run it, save the output:    java Broken > broken.txt
5  answers.txt, exactly these three lines:
     public class: file name
     exit code: 0
     java takes: class name
EOF_T
  chown -R $U $D
}
check() {
  say() { if [ "$1" = ok ]; then echo "PASS  $2"; p=$((p+1)); else echo "FAIL  $2"; fi; }
  magic() { [ "$(head -c 4 "$1" 2>/dev/null | od -An -tx1 | tr -d ' \n')" = cafebabe ]; }
  p=0
  magic $D/Greeter.class && [ "$(cat $D/run.txt 2>/dev/null)" = "Hello, Ada!" ] && r=ok || r=no; say $r "1 Greeter compiled, and run.txt says Hello, Ada!"
  [ "$(cat $D/exit.txt 2>/dev/null | tr -d ' \n')" = 2 ] && r=ok || r=no; say $r "2 exit.txt holds the exit code 2"
  grep -q "';' expected" $D/error.txt 2>/dev/null && grep -q 'Broken.java:3' $D/error.txt 2>/dev/null && r=ok || r=no; say $r "3 error.txt holds the original compile error"
  magic $D/Broken.class && grep -q 'Fixed: it compiles now' $D/broken.txt 2>/dev/null && r=ok || r=no; say $r "4 Broken is fixed, compiled, and broken.txt has its output"
  grep -q '^public class: *file name *$' $D/answers.txt 2>/dev/null && grep -q '^exit code: *0 *$' $D/answers.txt 2>/dev/null && grep -q '^java takes: *class name *$' $D/answers.txt 2>/dev/null && r=ok || r=no; say $r "5 answers.txt: three lines"
  echo "$p of 5 pass"
}
case "$1" in
  up) up;; check) check;; down) down; echo "lab removed";; status) ls $D 2>/dev/null || echo "not installed";;
  *) echo "usage: lab77.sh up|check|down|status";;
esac
