#!/bin/sh
# lab95.sh : MC11-O01 Gradle: projects, the wrapper, build scripts and the task graph. Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status
# Needs: a JDK (sudo apt install -y openjdk-21-jdk-headless python3 curl), internet access (the first run downloads Gradle, about 130 MB),
#        about 1 GB of free memory and 1 GB of free disk.
# Mission: change the version in the build script, add a task of your own, and show the task graph.
D=${LAB95_DIR:-/opt/lab95}
U=${SUDO_USER:-root}
GV=8.14.3
GURL=https://services.gradle.org/distributions/gradle-$GV-bin.zip
BOOT=${LAB95_GRADLE_ZIP_URL:-$GURL}
UH=$(getent passwd "$U" | cut -d: -f6)
# the wrapper keeps its copy of Gradle in a folder named after a hash of the download address
hashdir() { python3 -c "import hashlib,sys;n=int.from_bytes(hashlib.md5(sys.argv[1].encode()).digest(),'big');a='0123456789abcdefghijklmnopqrstuvwxyz';s=''
while n:
    n,r=divmod(n,36);s=a[r]+s
print(s)" "$GURL"; }
DIST=$UH/.gradle/wrapper/dists/gradle-$GV-bin/$(hashdir)
down() { rm -rf "${D:?}" "${DIST:?}"; rmdir "$(dirname "$DIST")" 2>/dev/null; true; }
up() {
  for t in javac curl python3; do command -v $t >/dev/null 2>&1 || { echo "$t not found: run  sudo apt install -y openjdk-21-jdk-headless curl python3"; exit 1; }; done
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  down; mkdir -p $D/.g
  echo "downloading Gradle $GV (about 130 MB) ..."
  curl -fL --progress-bar -o $D/.g/g.zip "$BOOT" || { echo "download failed"; exit 1; }
  python3 -m zipfile -e $D/.g/g.zip $D/.g && chmod +x $D/.g/gradle-$GV/bin/gradle || { echo "unzip failed"; exit 1; }
  p=$D/cartcore; mkdir -p $p/src/main/java/cloudcart
  printf "rootProject.name = 'cartcore'\n" > $p/settings.gradle
  cat > $p/build.gradle <<'EOF_B'
plugins {
    id 'java'
}

group = 'com.cloudcart'
version = '1.0'

repositories {
    mavenCentral()
}

jar {
    manifest {
        attributes 'Main-Class': 'cloudcart.Main'
    }
}
EOF_B
  printf 'package cloudcart;\n\npublic class Main {\n    public static void main(String[] args) {\n        System.out.println("CloudCart cart core is running");\n    }\n}\n' > $p/src/main/java/cloudcart/Main.java
  ( cd $p && env -u JAVA_TOOL_OPTIONS $D/.g/gradle-$GV/bin/gradle wrapper --no-daemon --no-validate-url --gradle-version $GV -q ) || { echo "could not create the wrapper"; exit 1; }
  # keep the Gradle we just downloaded as the wrapper's own copy, so the first ./gradlew does not download it a second time
  mkdir -p "$DIST" && cp -r $D/.g/gradle-$GV "$DIST/" && touch "$DIST/gradle-$GV-bin.zip.ok"; chown -R $U "$UH/.gradle"
  rm -rf $D/.g
  cat > $D/TASKS.txt <<'EOF_K'
LAB 95 : MC11 Gradle projects, the wrapper, build scripts and the task graph.   Work in /opt/lab95/cartcore
Always use the wrapper:  ./gradlew ...     (never the gradle on your PATH)

1  Open build.gradle. Change the version to 1.1, then build:  ./gradlew build
   The jar in build/libs must now be named cartcore-1.1.jar.
2  Add a task named report to build.gradle. It must print one line with the project name and version, for example:
       tasks.register('report') { doLast { println "report: ${project.name} ${project.version}" } }
   Run it:  ./gradlew -q report     (read the version from the script, do not type it by hand)
3  Make report depend on build:  dependsOn 'build'  inside the task.
4  Save the task graph. Run:  ./gradlew report --dry-run   and save the output in /opt/lab95/graph.txt
   (compileJava, jar, build and report must appear, in that order)
5  Write /opt/lab95/notes.txt with exactly three lines:
     settings: what settings.gradle does          (use the word project)
     wrapper:  what gradlew is for                (use the word version)
     task:     what dependsOn does                (use the word depend)
Then:  lab check     (all 5 must pass)       and later:  lab down
EOF_K
  chown -R $U $D; chmod 755 $D
  echo "lab95 ready: cd $D/cartcore   (task list: $D/TASKS.txt)"
}
check() {
  [ -d $D/cartcore ] || { echo "lab not set up: run  lab up"; exit 1; }
  ok=0
  as() { if [ "$U" = root ]; then "$@"; else runuser -u $U -- env HOME=$UH "$@"; fi; }
  pass() { echo "PASS  $1"; ok=$((ok+1)); }
  fail() { echo "FAIL  $1"; }
  W=/tmp/lab95-chk; rm -rf "${W:?}"; mkdir -p $W; chmod 777 $W
  cp -r $D/cartcore $W/c; rm -rf $W/c/build $W/c/.gradle; chown -R $U $W/c
  gw() { ( cd $W/c && as ./gradlew --no-daemon --console=plain "$@" ) 2>&1 | grep -v '^Picked up' || true; }
  if grep -qE "^version *= *['\"]1\.1['\"]" $D/cartcore/build.gradle && { gw build -q >/dev/null; [ -f $W/c/build/libs/cartcore-1.1.jar ]; }; then pass "1 build.gradle says 1.1 and the build made cartcore-1.1.jar"; else fail "1 set version = '1.1' in build.gradle and run ./gradlew build (the jar must be cartcore-1.1.jar)"; fi
  sed -i -E "s/^version *=.*/version = '9.9'/" $W/c/build.gradle
  if gw -q report | grep -q 'cartcore.*9\.9'; then pass "2 the report task prints the project name and the version from the script"; else fail "2 add a task named report that prints the project name and version (use project.name and project.version)"; fi
  gw report --dry-run > $W/dry.txt
  if awk '/:compileJava/{a=NR} /:jar/{b=NR} /:build/{c=NR} /:report/{d=NR} END{exit !(a&&b&&c&&d&&a<b&&b<c&&c<d)}' $W/dry.txt; then pass "3 report depends on build: the graph runs compileJava, jar, build, then report"; else fail "3 make report depend on build (dependsOn 'build' inside the task)"; fi
  if [ -f $D/graph.txt ] && awk '/:compileJava/{a=NR} /:jar/{b=NR} /:build/{c=NR} /:report/{d=NR} END{exit !(a&&b&&c&&d&&a<b&&b<c&&c<d)}' $D/graph.txt; then pass "4 graph.txt holds the task graph in the right order"; else fail "4 save the output of ./gradlew report --dry-run in /opt/lab95/graph.txt"; fi
  g() { sed -n "$1p" $D/notes.txt 2>/dev/null | tr 'A-Z' 'a-z'; }
  if [ -f $D/notes.txt ] && [ "$(grep -c . $D/notes.txt)" = 3 ] && g 1 | grep -q '^settings:.*project' && g 2 | grep -q '^wrapper:.*version' && g 3 | grep -q '^task:.*depend'; then pass "5 notes.txt has settings, wrapper and task lines"; else fail "5 write notes.txt: three lines starting settings:, wrapper:, task: (words project, version, depend)"; fi
  rm -rf "${W:?}"
  echo "$ok/5 checks passed"; [ $ok -eq 5 ]
}
status() { [ -d $D ] && echo "lab95 is set up in $D" || echo "lab95 is not set up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab95 removed";; status) status;; *) echo "usage: lab95.sh up|check|down|status"; exit 2;; esac
