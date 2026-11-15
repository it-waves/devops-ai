#!/bin/sh
# lab100.sh : MC11-O06 Gradle in CI: a GitHub Actions workflow that builds, caches and keeps secrets safe. Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status
# Needs: a JDK (sudo apt install -y openjdk-21-jdk-headless python3 curl), internet access (the first run downloads Gradle, about 130 MB),
#        about 1 GB of free memory and 1 GB of free disk.
# Mission: repair a broken GitHub Actions workflow (.github/workflows/ci.yml) so a CI run would build the project right: triggers, Java, Gradle cache, secrets, artifact.
D=${LAB100_DIR:-/opt/lab100}
U=${SUDO_USER:-root}
GV=8.14.3
GURL=https://services.gradle.org/distributions/gradle-$GV-bin.zip
BOOT=${LAB100_GRADLE_ZIP_URL:-$GURL}
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
  p=$D/cartcore; mkdir -p $p/src/main/java/com/cloudcart $p/.github/workflows
  printf "rootProject.name = 'cartcore'\n" > $p/settings.gradle
  cat > $p/build.gradle <<'EOF_B'
plugins {
    id 'java'
}

group = 'com.cloudcart'
version = '1.5'

jar {
    manifest { attributes 'Main-Class': 'com.cloudcart.Main' }
}

// a smoke test: run the jar and check what it says. check (and so build) depends on it
tasks.register('smoke', Exec) {
    dependsOn jar
    commandLine 'java', '-jar', jar.archiveFile.get().asFile.path
    standardOutput = new ByteArrayOutputStream()
    doLast { if (!standardOutput.toString().contains('smoke ok')) throw new GradleException('smoke test failed') }
}
check.dependsOn smoke
EOF_B
  cat > $p/src/main/java/com/cloudcart/Main.java <<'EOF_J'
package com.cloudcart;

public class Main {
    public static void main(String[] args) {
        System.out.println("cartcore smoke ok, total " + Cart.totalWithDiscount(2000, 10));
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
  cat > $p/.github/workflows/ci.yml <<'EOF_Y'
name: ci
on:
  push:
    branches: [main]
jobs:
  build:
    runs-on: ubuntu-latest
    env:
      REPO_PASSWORD: Pa55-plain
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: '8'
      - run: ./gradlew build
EOF_Y
  ( cd $p && env -u JAVA_TOOL_OPTIONS $D/.g/gradle-$GV/bin/gradle wrapper --no-daemon --no-validate-url --gradle-version $GV -q ) || { echo "could not create the wrapper"; exit 1; }
  # keep the Gradle we just downloaded as the wrapper's own copy, so the first ./gradlew does not download it a second time
  mkdir -p "$DIST" && cp -r $D/.g/gradle-$GV "$DIST/" && touch "$DIST/gradle-$GV-bin.zip.ok"; chown -R $U "$UH/.gradle"
  rm -rf $D/.g
  runuser -u $U -- env HOME=$UH env -u JAVA_TOOL_OPTIONS sh -c "cd $p && ./gradlew jar -q --console=plain" >/dev/null 2>&1
  cat > $D/TASKS.txt <<'EOF_K'
LAB 100 : MC11 Gradle in CI with GitHub Actions.   Work in /opt/lab100/cartcore   (the workflow is .github/workflows/ci.yml)
The workflow is the build script of a CI server. It is broken in five ways. Read it first:  cat .github/workflows/ci.yml
Edit it with vim (or nano). You cannot run it here: a lab check reads it, and also runs the same  ./gradlew build  a runner would.

1  Triggers: it must run on  push  and on  pull_request.
2  Java: the project needs Java 21. Use actions/setup-java@v4 with distribution temurin and java-version '21'. (actions/checkout@v4 stays.)
3  Gradle: add  gradle/actions/setup-gradle@v4  after setup-java. It caches Gradle files between runs.
4  Secret: REPO_PASSWORD must not be written in the file. Read it from the secret store:  ${{ secrets.REPO_PASSWORD }}   No file may contain the old password text.
5  Artifact: after the build, upload the jar with  actions/upload-artifact@v4  (path: build/libs/*.jar).
   lab check also runs  ./gradlew build  here, as a runner would: it must pass and produce the jar.
Then:  lab check     (all 5 must pass)       and later:  lab down
EOF_K
  chown -R $U $D; chmod 755 $D
  echo "lab100 ready: cd $D/cartcore   (task list: $D/TASKS.txt)"
}
check() {
  [ -d $D/cartcore ] || { echo "lab not set up: run  lab up"; exit 1; }
  ok=0
  as() { if [ "$U" = root ]; then "$@"; else runuser -u $U -- env HOME=$UH "$@"; fi; }
  pass() { echo "PASS  $1"; ok=$((ok+1)); }
  fail() { echo "FAIL  $1"; }
  W=/tmp/lab100-chk; rm -rf "${W:?}"; mkdir -p $W; chmod 777 $W
  cp -r $D/cartcore $W/c; rm -rf $W/c/build $W/c/.gradle; chown -R $U $W/c
  gw() { ( cd $W/c && as ./gradlew --no-daemon --console=plain "$@" ) 2>&1 | grep -v '^Picked up' || true; }
  Y=$D/cartcore/.github/workflows/ci.yml
  if grep -qE '^ *(push|"?on"?: *\[.*push)' $Y 2>/dev/null && grep -qE '^ *pull_request' $Y 2>/dev/null; then pass "1 the workflow runs on push and on pull_request"; else fail "1 the workflow must run on push and on pull_request"; fi
  if grep -q 'actions/checkout@v4' $Y 2>/dev/null && grep -q 'actions/setup-java@v4' $Y 2>/dev/null && grep -qE "java-version: *['\"]?21['\"]?" $Y 2>/dev/null; then pass "2 checkout and setup-java with Java 21"; else fail "2 use actions/setup-java@v4 with java-version 21"; fi
  if grep -q 'gradle/actions/setup-gradle@v4' $Y 2>/dev/null; then pass "3 setup-gradle caches the Gradle files"; else fail "3 add the step: uses: gradle/actions/setup-gradle@v4"; fi
  if grep -q 'secrets\.REPO_PASSWORD' $Y 2>/dev/null && ! grep -rIq 'Pa55-plain' $D --exclude-dir=.gradle --exclude-dir=build; then pass "4 the password comes from secrets.REPO_PASSWORD, not from the file"; else fail "4 read REPO_PASSWORD from the secret store (\${{ secrets.REPO_PASSWORD }}); the old text must be in no file"; fi
  bo=$(gw build); if grep -q 'actions/upload-artifact@v4' $Y 2>/dev/null && grep -q 'build/libs' $Y 2>/dev/null && echo "$bo" | grep -q 'BUILD SUCCESSFUL' && ls $W/c/build/libs/*.jar >/dev/null 2>&1; then pass "5 the jar is uploaded as an artifact, and ./gradlew build passes here"; else fail "5 add actions/upload-artifact@v4 with path build/libs/*.jar (and ./gradlew build must pass)"; fi
  rm -rf "${W:?}"
  echo "$ok/5 checks passed"; [ $ok -eq 5 ]
}
status() { [ -d $D ] && echo "lab100 is set up in $D" || echo "lab100 is not set up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab100 removed";; status) status;; *) echo "usage: lab100.sh up|check|down|status"; exit 2;; esac
