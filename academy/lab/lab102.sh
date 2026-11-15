#!/bin/sh
# lab102.sh : MC11-O08 Compare Maven and Gradle for DevOps workflows. Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status
# Needs: a JDK and Maven (sudo apt install -y openjdk-21-jdk-headless maven python3 curl), internet access (Gradle about 130 MB, and one small library from Maven Central),
#        about 1 GB of free memory and 1 GB of free disk.
# Mission: one project with BOTH a pom.xml and a build.gradle. Make both builds work, collect evidence from each, and write down which one you would choose for a team and why.
D=${LAB102_DIR:-/opt/lab102}
U=${SUDO_USER:-root}
GV=8.14.3
GURL=https://services.gradle.org/distributions/gradle-$GV-bin.zip
BOOT=${LAB102_GRADLE_ZIP_URL:-$GURL}
UH=$(getent passwd "$U" | cut -d: -f6)
# the wrapper keeps its copy of Gradle in a folder named after a hash of the download address
hashdir() { python3 -c "import hashlib,sys;n=int.from_bytes(hashlib.md5(sys.argv[1].encode()).digest(),'big');a='0123456789abcdefghijklmnopqrstuvwxyz';s=''
while n:
    n,r=divmod(n,36);s=a[r]+s
print(s)" "$GURL"; }
DIST=$UH/.gradle/wrapper/dists/gradle-$GV-bin/$(hashdir)
down() { rm -rf "${D:?}" "${DIST:?}"; rmdir "$(dirname "$DIST")" 2>/dev/null; true; }
up() {
  for t in javac mvn curl python3; do command -v $t >/dev/null 2>&1 || { echo "$t not found: run  sudo apt install -y openjdk-21-jdk-headless maven curl python3"; exit 1; }; done
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
version = '1.7'

repositories {
    mavenCentral()
}

dependencies {
}
EOF_B
  cat > $p/pom.xml <<'EOF_P'
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.cloudcart</groupId>
  <artifactId>cartcore</artifactId>
  <version>1.7</version>

  <properties>
    <maven.compiler.release>21</maven.compiler.release>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
  </properties>

  <dependencies>
  </dependencies>
</project>
EOF_P
  cat > $p/src/main/java/com/cloudcart/Main.java <<'EOF_J'
package com.cloudcart;

import org.apache.commons.lang3.StringUtils;

public class Main {
    public static void main(String[] args) {
        System.out.println(StringUtils.capitalize("cartcore") + " " + Cart.totalWithDiscount(2000, 10));
    }
}
EOF_J
  cat > $p/src/main/java/com/cloudcart/Cart.java <<'EOF_J'
package com.cloudcart;

public class Cart {
    public static int totalWithDiscount(int cents, int percent) {
        return cents - (cents * percent / 100);
    }
}
EOF_J
  ( cd $p && env -u JAVA_TOOL_OPTIONS $D/.g/gradle-$GV/bin/gradle wrapper --no-daemon --no-validate-url --gradle-version $GV -q ) || { echo "could not create the wrapper"; exit 1; }
  # keep the Gradle we just downloaded as the wrapper's own copy, so the first ./gradlew does not download it a second time
  mkdir -p "$DIST" && cp -r $D/.g/gradle-$GV "$DIST/" && touch "$DIST/gradle-$GV-bin.zip.ok"; chown -R $U "$UH/.gradle"
  rm -rf $D/.g
  cat > $D/TASKS.txt <<'EOF_K'
LAB 102 : MC11 Maven or Gradle?   Work in /opt/lab102/cartcore   (it has a pom.xml AND a build.gradle)
The code uses commons-lang3, but neither build file lists it yet, so both builds fail. Make both work, then compare.

1  Maven: add commons-lang3 version 3.12.0 to pom.xml (inside <dependencies>), then  mvn -q package  must give target/cartcore-1.7.jar
2  Gradle: add  implementation 'org.apache.commons:commons-lang3:3.12.0'  to build.gradle, then  ./gradlew build  must give build/libs/cartcore-1.7.jar
3  Evidence: run  ./gradlew build  a second time and save it:   ./gradlew build > gradle-second.txt   (it must say UP-TO-DATE)
4  Both jars must contain the same classes (Main and Cart). Check with:  unzip -l target/cartcore-1.7.jar   and   unzip -l build/libs/cartcore-1.7.jar
5  Write decision.txt, three lines in your own words:   maven: ...    gradle: ...    choice: ...   (what each is good at, and which you would pick for a team, and why)
Then:  lab check     (all 5 must pass)       and later:  lab down
EOF_K
  chown -R $U $D; chmod 755 $D
  echo "lab102 ready: cd $D/cartcore   (task list: $D/TASKS.txt)"
}
check() {
  [ -d $D/cartcore ] || { echo "lab not set up: run  lab up"; exit 1; }
  ok=0
  as() { if [ "$U" = root ]; then "$@"; else runuser -u $U -- env HOME=$UH "$@"; fi; }
  pass() { echo "PASS  $1"; ok=$((ok+1)); }
  fail() { echo "FAIL  $1"; }
  W=/tmp/lab102-chk; rm -rf "${W:?}"; mkdir -p $W; chmod 777 $W
  cp -r $D/cartcore $W/c; rm -rf $W/c/build $W/c/.gradle $W/c/target; chown -R $U $W/c
  gw() { ( cd $W/c && as ./gradlew --console=plain "$@" ) 2>&1 | grep -v '^Picked up' || true; }
  mo=$( cd $W/c && as mvn -q -B package 2>&1 | grep -v '^Picked up' ); if ls $W/c/target/cartcore-1.7.jar >/dev/null 2>&1; then pass "1 Maven builds target/cartcore-1.7.jar"; else fail "1 mvn package must work: add commons-lang3 3.12.0 to pom.xml"; fi
  bo=$(gw build); if echo "$bo" | grep -q 'BUILD SUCCESSFUL' && ls $W/c/build/libs/cartcore-1.7.jar >/dev/null 2>&1; then pass "2 Gradle builds build/libs/cartcore-1.7.jar"; else fail "2 ./gradlew build must work: add commons-lang3 3.12.0 to build.gradle"; fi
  if grep -q 'UP-TO-DATE' $D/cartcore/gradle-second.txt 2>/dev/null && grep -q 'BUILD SUCCESSFUL' $D/cartcore/gradle-second.txt 2>/dev/null; then pass "3 gradle-second.txt shows a second run with UP-TO-DATE"; else fail "3 run ./gradlew build twice and save the second run:  ./gradlew build > gradle-second.txt"; fi
  if unzip -l $W/c/target/cartcore-1.7.jar 2>/dev/null | grep -q 'Cart.class' && unzip -l $W/c/build/libs/cartcore-1.7.jar 2>/dev/null | grep -q 'Cart.class' && unzip -l $W/c/target/cartcore-1.7.jar 2>/dev/null | grep -q 'Main.class' && unzip -l $W/c/build/libs/cartcore-1.7.jar 2>/dev/null | grep -q 'Main.class'; then pass "4 both jars contain Main and Cart"; else fail "4 both jars must contain Main.class and Cart.class"; fi
  N=$D/cartcore/decision.txt; if grep -qiE '^maven:.{12,}' $N 2>/dev/null && grep -qiE '^gradle:.{12,}' $N 2>/dev/null && grep -qiE '^choice:.{12,}' $N 2>/dev/null; then pass "5 decision.txt has maven, gradle and choice"; else fail "5 decision.txt needs three lines: maven: ...  gradle: ...  choice: ...  (12+ characters each)"; fi
  rm -rf "${W:?}"
  echo "$ok/5 checks passed"; [ $ok -eq 5 ]
}
status() { [ -d $D ] && echo "lab102 is set up in $D" || echo "lab102 is not set up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab102 removed";; status) status;; *) echo "usage: lab102.sh up|check|down|status"; exit 2;; esac
