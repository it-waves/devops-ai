#!/bin/sh
# lab101.sh : MC11-O07 Diagnose Gradle task, dependency and daemon failures. Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status
# Needs: a JDK (sudo apt install -y openjdk-21-jdk-headless python3 curl), internet access (Gradle about 130 MB, and one small library from Maven Central),
#        about 1 GB of free memory and 1 GB of free disk.
# Mission: a project that will not build. Three different failures hide behind each other: a daemon that cannot start, a dependency that cannot be found, a task that fails. Diagnose each one by its message and fix it.
D=${LAB101_DIR:-/opt/lab101}
U=${SUDO_USER:-root}
GV=8.14.3
GURL=https://services.gradle.org/distributions/gradle-$GV-bin.zip
BOOT=${LAB101_GRADLE_ZIP_URL:-$GURL}
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
  p=$D/cartcore; mkdir -p $p/src/main/java/com/cloudcart
  printf "rootProject.name = 'cartcore'\n" > $p/settings.gradle
  cat > $p/build.gradle <<'EOF_B'
plugins {
    id 'java'
}

group = 'com.cloudcart'
version = '1.6'

repositories {
    mavenCentral()
}

dependencies {
    implementation 'org.apache.commons:commons-lang3:3.99.1'
}

jar {
    manifest { attributes 'Main-Class': 'com.cloudcart.Main' }
}

// a smoke test: run the program and check what it says. check (and so build) depends on it
tasks.register('smoke', JavaExec) {
    classpath = sourceSets.main.runtimeClasspath
    mainClass = 'com.cloudcart.Main'
    standardOutput = new ByteArrayOutputStream()
    doLast {
        def out = standardOutput.toString().trim()
        if (!out.contains('total 1800')) throw new GradleException("smoke test failed: expected 'total 1800' but the program said: " + out)
    }
}
check.dependsOn smoke
EOF_B
  cat > $p/src/main/java/com/cloudcart/Main.java <<'EOF_J'
package com.cloudcart;

import org.apache.commons.lang3.StringUtils;

public class Main {
    public static void main(String[] args) {
        System.out.println(StringUtils.capitalize("cartcore") + " smoke ok, total " + Cart.totalWithDiscount(2000, 10));
    }
}
EOF_J
  cat > $p/src/main/java/com/cloudcart/Cart.java <<'EOF_J'
package com.cloudcart;

public class Cart {
    public static int totalWithDiscount(int cents, int percent) {
        return cents + (cents * percent / 100);
    }
}
EOF_J
  ( cd $p && env -u JAVA_TOOL_OPTIONS $D/.g/gradle-$GV/bin/gradle wrapper --no-daemon --no-validate-url --gradle-version $GV -q ) || { echo "could not create the wrapper"; exit 1; }
  # keep the Gradle we just downloaded as the wrapper's own copy, so the first ./gradlew does not download it a second time
  mkdir -p "$DIST" && cp -r $D/.g/gradle-$GV "$DIST/" && touch "$DIST/gradle-$GV-bin.zip.ok"; chown -R $U "$UH/.gradle"
  rm -rf $D/.g
  runuser -u $U -- env HOME=$UH env -u JAVA_TOOL_OPTIONS sh -c "cd $p && ./gradlew jar -q --console=plain" >/dev/null 2>&1
  printf 'org.gradle.jvmargs=-Xmx16m\n' > $p/gradle.properties
  cat > $D/TASKS.txt <<'EOF_K'
LAB 101 : MC11 Diagnose Gradle task, dependency and daemon failures.   Work in /opt/lab101/cartcore
./gradlew build  does not work. There are three different failures, hidden behind each other. Fix them in the order they appear.
Read each message from "What went wrong" down. Ask: which phase failed (daemon start, dependency resolution, or a task)?

1  Daemon: Gradle cannot even start its background process. Find the setting in gradle.properties and give the daemon enough memory (for example -Xmx512m).
2  Dependency: a library cannot be found. Find the wrong version in build.gradle (hint: ./gradlew dependencies --configuration compileClasspath) and use  3.12.0  of commons-lang3.
3  Task: the smoke task fails. Read what the program said, find the bug in the Java code, and fix it. (A discount must be taken off, not added.)
4  ./gradlew build must pass and produce build/libs/cartcore-1.6.jar.
5  Write notes.txt in cartcore, three lines, in your own words:   daemon: ...    dependency: ...    task: ...    (what failed, and how you knew which kind of failure it was)
Then:  lab check     (all 5 must pass)       and later:  lab down
EOF_K
  chown -R $U $D; chmod 755 $D
  echo "lab101 ready: cd $D/cartcore   (task list: $D/TASKS.txt)"
}
check() {
  [ -d $D/cartcore ] || { echo "lab not set up: run  lab up"; exit 1; }
  ok=0
  as() { if [ "$U" = root ]; then "$@"; else runuser -u $U -- env HOME=$UH "$@"; fi; }
  pass() { echo "PASS  $1"; ok=$((ok+1)); }
  fail() { echo "FAIL  $1"; }
  W=/tmp/lab101-chk; rm -rf "${W:?}"; mkdir -p $W; chmod 777 $W
  cp -r $D/cartcore $W/c; rm -rf $W/c/build $W/c/.gradle; chown -R $U $W/c
  gw() { ( cd $W/c && as ./gradlew --console=plain "$@" ) 2>&1 | grep -v '^Picked up' || true; }
  P=$D/cartcore/gradle.properties
  mx=$(sed -n 's/.*-Xmx\([0-9]*\)\([mMgG]\).*/\1\2/p' $P 2>/dev/null | head -1); mxm=0
  case "$mx" in *[mM]) mxm=${mx%[mM]};; *[gG]) mxm=$(( ${mx%[gG]} * 1024 ));; esac
  vo=$(gw -q help); if [ "${mxm:-0}" -ge 128 ] && ! echo "$vo" | grep -q 'Unable to start the daemon'; then pass "1 the daemon starts (enough memory in gradle.properties)"; else fail "1 the daemon cannot start: give org.gradle.jvmargs enough memory (-Xmx512m)"; fi
  do=$(gw dependencies --configuration compileClasspath); if echo "$do" | grep -q 'commons-lang3:3.12.0' && ! echo "$do" | grep -q 'FAILED'; then pass "2 the dependency resolves (commons-lang3 3.12.0)"; else fail "2 commons-lang3 cannot be resolved: use a version that exists (3.12.0)"; fi
  so=$(gw smoke); if echo "$so" | grep -q 'BUILD SUCCESSFUL'; then pass "3 the smoke task passes"; else fail "3 the smoke task fails: read what the program said, fix the Java code (a discount is taken off)"; fi
  bo=$(gw build); if echo "$bo" | grep -q 'BUILD SUCCESSFUL' && ls $W/c/build/libs/cartcore-1.6.jar >/dev/null 2>&1; then pass "4 ./gradlew build passes and produces cartcore-1.6.jar"; else fail "4 ./gradlew build must pass and produce build/libs/cartcore-1.6.jar"; fi
  N=$D/cartcore/notes.txt; if grep -qiE '^daemon:.{12,}' $N 2>/dev/null && grep -qiE '^dependency:.{12,}' $N 2>/dev/null && grep -qiE '^task:.{12,}' $N 2>/dev/null; then pass "5 notes.txt answers daemon, dependency and task"; else fail "5 notes.txt needs three lines: daemon: ...  dependency: ...  task: ...  (12+ characters each)"; fi
  rm -rf "${W:?}"
  echo "$ok/5 checks passed"; [ $ok -eq 5 ]
}
status() { [ -d $D ] && echo "lab101 is set up in $D" || echo "lab101 is not set up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab101 removed";; status) status;; *) echo "usage: lab101.sh up|check|down|status"; exit 2;; esac
