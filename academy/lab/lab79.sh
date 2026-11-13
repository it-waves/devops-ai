#!/bin/sh
# lab79.sh : inspect a running Java process (MC09-O04). Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status        Needs a JDK (sudo apt install -y openjdk-21-jdk-headless).
# Mission: start a small Java server, then read its real command line, JVM flags and properties from outside.
D=/opt/lab79
U=${SUDO_USER:-root}
down() { pkill -f 'java.*Server' 2>/dev/null; sleep 1; rm -rf $D; true; }
up() {
  command -v javac >/dev/null 2>&1 && command -v jcmd >/dev/null 2>&1 || { echo "javac/jcmd not found: run  sudo apt install -y openjdk-21-jdk-headless"; exit 1; }
  down; mkdir -p $D
  cat > $D/Server.java <<'EOF_S'
public class Server {
    public static void main(String[] args) throws Exception {
        String port = System.getProperty("server.port", "8080");
        System.out.println("Server listening on port " + port);
        while (true) Thread.sleep(1000);
    }
}
EOF_S
  javac -d $D $D/Server.java 2>&1 | grep -v 'Picked up'
  cat > $D/TASKS.txt <<'EOF_T'
Tasks (work inside /opt/lab79, then run: lab check)
1  Start the server and leave it running:       java -Xmx192m -Dserver.port=9191 -Dmode=prod Server &
2  Save its REAL command line from /proc:       PID=$(pgrep -f Server)   then   tr '\0' ' ' < /proc/$PID/cmdline > cmdline.txt
3  Save the JVM flags it is using:              jcmd Server VM.flags > flags.txt
4  Save the mode property:                      jcmd Server VM.system_properties | grep mode > property.txt
5  answers.txt, exactly these three lines:
     heap flag: -Xmx
     property flag: -D
     inspect tool: jcmd
EOF_T
  chown -R $U $D
}
check() {
  say() { if [ "$1" = ok ]; then echo "PASS  $2"; p=$((p+1)); else echo "FAIL  $2"; fi; }
  p=0
  pgrep -f 'java.*-Xmx192m.*-Dserver.port=9191.*-Dmode=prod.*Server' >/dev/null 2>&1 && r=ok || r=no; say $r "1 the server is running with the task flags"
  grep -q -- '-Xmx192m' $D/cmdline.txt 2>/dev/null && grep -q -- '-Dserver.port=9191' $D/cmdline.txt 2>/dev/null && grep -q -- '-Dmode=prod' $D/cmdline.txt 2>/dev/null && r=ok || r=no; say $r "2 cmdline.txt holds the real command line"
  grep -q 'MaxHeapSize *= *201326592' $D/flags.txt 2>/dev/null || grep -q -- '-XX:MaxHeapSize=201326592' $D/flags.txt 2>/dev/null; [ $? -eq 0 ] && r=ok || r=no; say $r "3 flags.txt shows MaxHeapSize 201326592 (192m)"
  grep -q 'mode=prod' $D/property.txt 2>/dev/null && r=ok || r=no; say $r "4 property.txt shows mode=prod"
  grep -q '^heap flag: *-Xmx *$' $D/answers.txt 2>/dev/null && grep -q '^property flag: *-D *$' $D/answers.txt 2>/dev/null && grep -q '^inspect tool: *jcmd *$' $D/answers.txt 2>/dev/null && r=ok || r=no; say $r "5 answers.txt: three lines"
  echo "$p of 5 pass"
}
case "$1" in
  up) up;; check) check;; down) down; echo "lab removed";; status) ls $D 2>/dev/null || echo "not installed";;
  *) echo "usage: lab79.sh up|check|down|status";;
esac
