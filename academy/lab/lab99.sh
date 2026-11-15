#!/bin/sh
# lab99.sh : MC11-O05 Gradle: up-to-date checks, the build cache and reproducible builds. Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status
# Needs: a JDK (sudo apt install -y openjdk-21-jdk-headless python3 curl), internet access (the first run downloads Gradle, about 130 MB),
#        about 1 GB of free memory and 1 GB of free disk.
# Mission: make a second build skip its work, make a clean build restore from the cache, and make the jar byte-for-byte reproducible.
D=${LAB99_DIR:-/opt/lab99}
U=${SUDO_USER:-root}
GV=8.14.3
GURL=https://services.gradle.org/distributions/gradle-$GV-bin.zip
BOOT=${LAB99_GRADLE_ZIP_URL:-$GURL}
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
  p=$D/cartcore; mkdir -p $p/src/main/java/com/cloudcart $p/src/main/resources
  printf "rootProject.name = 'cartcore'\n" > $p/settings.gradle
  cat > $p/build.gradle <<'EOF_B'
plugins {
    id 'java'
}

group = 'com.cloudcart'
version = '1.4'

// the jar manifest records who built it, and when
jar {
    manifest {
        attributes 'Implementation-Title': 'cartcore'
        attributes 'Built-At': new Date().toString()
    }
}
EOF_B
  cat > $p/src/main/java/com/cloudcart/Cart.java <<'EOF_J'
package com.cloudcart;

public class Cart {
    public static int totalWithDiscount(int cents, int percent) {
        return cents - (cents * percent / 100);
    }
}
EOF_J
  cat > $p/src/main/java/com/cloudcart/Price.java <<'EOF_J'
package com.cloudcart;

public class Price {
    public static String label(int cents) {
        return String.format("$%d.%02d", cents / 100, cents % 100);
    }
}
EOF_J
  printf 'app=cartcore\nstore=CloudCart\n' > $p/src/main/resources/app.properties
  ( cd $p && env -u JAVA_TOOL_OPTIONS $D/.g/gradle-$GV/bin/gradle wrapper --no-daemon --no-validate-url --gradle-version $GV -q ) || { echo "could not create the wrapper"; exit 1; }
  # keep the Gradle we just downloaded as the wrapper's own copy, so the first ./gradlew does not download it a second time
  mkdir -p "$DIST" && cp -r $D/.g/gradle-$GV "$DIST/" && touch "$DIST/gradle-$GV-bin.zip.ok"; chown -R $U "$UH/.gradle"
  rm -rf $D/.g
  runuser -u $U -- env HOME=$UH env -u JAVA_TOOL_OPTIONS sh -c "cd $p && ./gradlew jar -q --console=plain" >/dev/null 2>&1
  cat > $D/TASKS.txt <<'EOF_K'
LAB 99 : MC11 Gradle up-to-date checks, the build cache and reproducible builds.   Work in /opt/lab99/cartcore
Always use the wrapper:  ./gradlew ...

0  Look first:  ./gradlew jar   twice.  The second run should skip everything. It does not: one task runs again. Find out why (read build.gradle).
1  Turn the build cache on for this project: add  org.gradle.caching=true  to gradle.properties (create the file).
2  Make the second run skip its work. Take the changing value (Built-At) out of the jar manifest in build.gradle.
   Then  ./gradlew jar  twice: the second run must show  :processResources UP-TO-DATE  and  :jar UP-TO-DATE.
3  Prove the cache works after clean:  ./gradlew jar  then  ./gradlew clean jar  must show  :compileJava FROM-CACHE.
4  Make the jar reproducible: two clean builds must give a jar with the same sha256sum.
   Hint: a jar remembers file times and file order. In build.gradle:  jar { preserveFileTimestamps = false ; reproducibleFileOrder = true }
   Compare:  ./gradlew -q clean jar && sha256sum build/libs/*.jar     run it twice.
5  Write /opt/lab99/notes.txt with exactly three lines:
     up-to-date:  why Gradle can skip a task                                  (use the word input)
     from-cache:  why a task can be restored even after clean                 (use the word clean)
     reproducible: what must not be stored in the jar                         (use the word timestamp)
Then:  lab check     (all 5 must pass)       and later:  lab down
EOF_K
  chown -R $U $D; chmod 755 $D
  echo "lab99 ready: cd $D/cartcore   (task list: $D/TASKS.txt)"
}
check() {
  [ -d $D/cartcore ] || { echo "lab not set up: run  lab up"; exit 1; }
  ok=0
  as() { if [ "$U" = root ]; then "$@"; else runuser -u $U -- env HOME=$UH "$@"; fi; }
  pass() { echo "PASS  $1"; ok=$((ok+1)); }
  fail() { echo "FAIL  $1"; }
  W=/tmp/lab99-chk; rm -rf "${W:?}"; mkdir -p $W; chmod 777 $W
  cp -r $D/cartcore $W/c; rm -rf $W/c/build $W/c/.gradle; chown -R $U $W/c
  gw() { ( cd $W/c && as ./gradlew --no-daemon --console=plain "$@" ) 2>&1 | grep -v '^Picked up' || true; }
  if grep -qE '^org\.gradle\.caching *= *true' $D/cartcore/gradle.properties 2>/dev/null; then pass "1 the build cache is switched on in gradle.properties"; else fail "1 add org.gradle.caching=true to gradle.properties"; fi
  gw build >/dev/null; r2=$(gw build)
  if echo "$r2" | grep -q ':processResources UP-TO-DATE' && echo "$r2" | grep -q ':jar UP-TO-DATE' && echo "$r2" | grep -q ':compileJava UP-TO-DATE'; then pass "2 a second build skips compileJava, processResources and jar (UP-TO-DATE)"; else fail "2 the second build still runs a task: remove the Built-At line from the jar manifest"; fi
  gw build >/dev/null; gw clean >/dev/null; r3=$(gw build)
  if echo "$r3" | grep -q ':compileJava FROM-CACHE'; then pass "3 after clean, compileJava is restored FROM-CACHE"; else fail "3 after ./gradlew clean, compileJava must say FROM-CACHE: switch the cache on in gradle.properties"; fi
  gw -q clean jar --no-build-cache >/dev/null; h1=$(sha256sum $W/c/build/libs/*.jar 2>/dev/null | cut -d' ' -f1); sleep 3
  gw -q clean jar --no-build-cache >/dev/null; h2=$(sha256sum $W/c/build/libs/*.jar 2>/dev/null | cut -d' ' -f1)
  if [ -n "$h1" ] && [ "$h1" = "$h2" ]; then pass "4 two clean builds give the same jar (sha256 identical)"; else fail "4 the jar changes between builds: stop it storing times (preserveFileTimestamps = false) and file order (reproducibleFileOrder = true), and remove the Built-At line"; fi
  g() { sed -n "$1p" $D/notes.txt 2>/dev/null | tr 'A-Z' 'a-z'; }
  if [ -f $D/notes.txt ] && [ "$(grep -c . $D/notes.txt)" = 3 ] && g 1 | grep -q '^up-to-date:.*input' && g 2 | grep -q '^from-cache:.*clean' && g 3 | grep -q '^reproducible:.*timestamp'; then pass "5 notes.txt answers the three questions"; else fail "5 write notes.txt: up-to-date: (word input), from-cache: (word clean), reproducible: (word timestamp)"; fi
  rm -rf "${W:?}"
  echo "$ok/5 checks passed"; [ $ok -eq 5 ]
}
status() { [ -d $D ] && echo "lab99 is set up in $D" || echo "lab99 is not set up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab99 removed";; status) status;; *) echo "usage: lab99.sh up|check|down|status"; exit 2;; esac
