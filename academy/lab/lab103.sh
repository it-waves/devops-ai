#!/bin/sh
# lab103.sh : MC11 mastery evidence: release a Gradle build. Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status
# Needs: a JDK (sudo apt install -y openjdk-21-jdk-headless python3 curl), internet access (Gradle about 130 MB, and a few small libraries from Maven Central),
#        about 1 GB of free memory and 1 GB of free disk.
# Mission: take cartcore 2.0 from a broken build to a safe release: fix the build, make the jar reproducible, publish it without a password in any file, and write a report.
D=${LAB103_DIR:-/opt/lab103}
U=${SUDO_USER:-root}
GV=8.14.3
GURL=https://services.gradle.org/distributions/gradle-$GV-bin.zip
BOOT=${LAB103_GRADLE_ZIP_URL:-$GURL}
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
  p=$D/cartcore; mkdir -p $p/src/main/java/com/cloudcart $p/src/test/java/com/cloudcart $D/repo
  printf 'S3cr3t-r3l3as3-key\n' > $D/pass.txt
  printf "rootProject.name = 'cartcore'\n" > $p/settings.gradle
  cat > $p/build.gradle <<'EOF_B'
plugins {
    id 'java'
    id 'maven-publish'
}

group = 'com.cloudcart'
version = '2.0'

repositories {
    mavenCentral()
}

dependencies {
    implementation 'org.apache.commons:commons-lang3:3.12.0'
    testImplementation 'org.junit.jupiter:junit-jupiter:5.10.99'
    testRuntimeOnly 'org.junit.platform:junit-platform-launcher:1.10.2'
}

test {
    useJUnitPlatform()
}

jar {
    manifest { attributes 'Main-Class': 'com.cloudcart.Main' }
}

// the key that allows a release
def releaseKey = 'S3cr3t-r3l3as3-key'

publishing {
    publications {
        mavenJava(MavenPublication) { from components.java }
    }
    repositories {
        maven { url = uri('/opt/lab103/repo') }
    }
}

tasks.named('publish') {
    doFirst {
        if (!releaseKey) throw new GradleException('no release key: set REPO_PASS')
        println 'releasing with a key ending ' + releaseKey.takeRight(4)
    }
}
EOF_B
  cat > $p/src/main/java/com/cloudcart/Main.java <<'EOF_J'
package com.cloudcart;

import org.apache.commons.lang3.StringUtils;

public class Main {
    public static void main(String[] args) {
        System.out.println(StringUtils.capitalize("cartcore") + " total " + Cart.totalWithDiscount(2000, 10));
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
  cat > $p/src/test/java/com/cloudcart/CartTest.java <<'EOF_J'
package com.cloudcart;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class CartTest {
    @Test
    void tenPercentOff() {
        assertEquals(1800, Cart.totalWithDiscount(2000, 10));
    }

    @Test
    void noDiscount() {
        assertEquals(500, Cart.totalWithDiscount(500, 0));
    }
}
EOF_J
  ( cd $p && env -u JAVA_TOOL_OPTIONS $D/.g/gradle-$GV/bin/gradle wrapper --no-daemon --no-validate-url --gradle-version $GV -q ) || { echo "could not create the wrapper"; exit 1; }
  # keep the Gradle we just downloaded as the wrapper's own copy, so the first ./gradlew does not download it a second time
  mkdir -p "$DIST" && cp -r $D/.g/gradle-$GV "$DIST/" && touch "$DIST/gradle-$GV-bin.zip.ok"; chown -R $U "$UH/.gradle"
  rm -rf $D/.g
  cat > $D/TASKS.txt <<'EOF_K'
LAB 103 : MC11 Gradle mastery evidence. Release cartcore 2.0.   Work in /opt/lab103/cartcore
./gradlew build does not work yet. Fix it, make it safe to release, and write down what you did.

1  Build: ./gradlew build fails. Read the messages from "What went wrong" down and fix each failure in turn (a library version that does not exist, then a failing test: a discount is taken off, not added). Use junit-jupiter 5.10.2.
2  Reproducible: build twice with ./gradlew clean build and compare  sha256sum build/libs/cartcore-2.0.jar . The two hashes must be the same. Make the jar tasks ignore file timestamps and use a fixed file order.
3  Publish: ./gradlew publish must put cartcore-2.0.jar and its .pom in /opt/lab103/repo (the release repository).
4  No secret in a file: the release password is in /opt/lab103/pass.txt. Today it is typed into build.gradle (releaseKey). Read it from an environment variable instead: def releaseKey = System.getenv('REPO_PASS'), then run the publish with  REPO_PASS=$(cat ../pass.txt) ./gradlew publish
5  Write report.txt in cartcore, three lines, in your own words:   problems: ...    fixes: ...    cleanup: ...   (what broke, what you changed, and how you clean up: lab down)
Then:  lab check     (all 5 must pass)       and later:  lab down
EOF_K
  chown -R $U $D; chmod 755 $D
  echo "lab103 ready: cd $D/cartcore   (task list: $D/TASKS.txt)"
}
check() {
  [ -d $D/cartcore ] || { echo "lab not set up: run  lab up"; exit 1; }
  ok=0
  as() { if [ "$U" = root ]; then "$@"; else runuser -u $U -- env HOME=$UH "$@"; fi; }
  pass() { echo "PASS  $1"; ok=$((ok+1)); }
  fail() { echo "FAIL  $1"; }
  W=/tmp/lab103-chk; rm -rf "${W:?}"; mkdir -p $W; chmod 777 $W
  cp -r $D/cartcore $W/c; rm -rf $W/c/build $W/c/.gradle; chown -R $U $W/c
  gw() { ( cd $W/c && as env "REPO_PASS=${RP:-x}" ./gradlew --console=plain "$@" ) 2>&1 | grep -v '^Picked up' || true; }
  bo=$(gw build); if echo "$bo" | grep -q 'BUILD SUCCESSFUL' && [ -f $W/c/build/libs/cartcore-2.0.jar ]; then pass "1 ./gradlew build passes (tests green) and makes cartcore-2.0.jar"; else fail "1 ./gradlew build must pass: fix the library version and the failing test (a discount is taken off)"; fi
  h1=$(gw clean build >/dev/null; sha256sum $W/c/build/libs/cartcore-2.0.jar 2>/dev/null | cut -c1-64); sleep 2
  h2=$(gw clean build >/dev/null; sha256sum $W/c/build/libs/cartcore-2.0.jar 2>/dev/null | cut -c1-64)
  if [ -n "$h1" ] && [ "$h1" = "$h2" ]; then pass "2 two clean builds give the same jar hash (reproducible)"; else fail "2 the jar changes on every build: ignore file timestamps and use a fixed file order in the archive tasks"; fi
  rm -rf "${D:?}/repo"; mkdir -p $D/repo; chown $U $D/repo; RP=$(cat $D/pass.txt); po=$(gw build publish)
  if [ -f $D/repo/com/cloudcart/cartcore/2.0/cartcore-2.0.jar ] && [ -f $D/repo/com/cloudcart/cartcore/2.0/cartcore-2.0.pom ]; then pass "3 ./gradlew publish puts the jar and pom in the release repository"; else fail "3 ./gradlew publish must create cartcore-2.0.jar and cartcore-2.0.pom in $D/repo (run it with REPO_PASS set)"; fi
  if ! grep -rqF "$RP" $D/cartcore --include='*.gradle' --include='*.properties' --include='*.txt' --include='*.java' 2>/dev/null && grep -q 'getenv' $D/cartcore/build.gradle; then pass "4 no password in any project file; build.gradle reads REPO_PASS from the environment"; else fail "4 the release password is still in a file, or build.gradle does not use System.getenv('REPO_PASS')"; fi
  N=$D/cartcore/report.txt; if grep -qiE '^problems:.{12,}' $N 2>/dev/null && grep -qiE '^fixes:.{12,}' $N 2>/dev/null && grep -qiE '^cleanup:.{12,}' $N 2>/dev/null; then pass "5 report.txt answers problems, fixes and cleanup"; else fail "5 report.txt needs three lines: problems: ...  fixes: ...  cleanup: ...  (12+ characters each)"; fi
  rm -rf "${W:?}"
  echo "$ok/5 checks passed"; [ $ok -eq 5 ]
}
status() { [ -d $D ] && echo "lab103 is set up in $D" || echo "lab103 is not set up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab103 removed";; status) status;; *) echo "usage: lab103.sh up|check|down|status"; exit 2;; esac
