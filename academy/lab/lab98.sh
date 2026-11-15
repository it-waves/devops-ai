#!/bin/sh
# lab98.sh : MC11-O04 Gradle: environment settings and secrets. Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status
# Needs: a JDK (sudo apt install -y openjdk-21-jdk-headless python3 curl), internet access (the first run downloads Gradle, about 130 MB),
#        about 1 GB of free memory and 1 GB of free disk.
# Mission: keep settings in gradle.properties, override them with -P, and pass a secret through the environment, never in a file.
D=${LAB98_DIR:-/opt/lab98}
U=${SUDO_USER:-root}
GV=8.14.3
GURL=https://services.gradle.org/distributions/gradle-$GV-bin.zip
BOOT=${LAB98_GRADLE_ZIP_URL:-$GURL}
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
  p=$D/cartcore; mkdir -p $p
  printf "rootProject.name = 'cartcore'\n" > $p/settings.gradle
  cat > $p/build.gradle <<'EOF_B'
plugins {
    id 'java'
}

group = 'com.cloudcart'
version = '1.3'

// prints the settings this build sees. It never prints the password itself.
tasks.register('showConfig') {
    doLast {
        println "greeting=" + (findProperty('greeting') ?: 'unset')
        println "password=" + (findProperty('repoPassword') ? 'set' : 'missing')
    }
}
EOF_B
  printf 'repoPassword=Pa55-plain\n' > $p/gradle.properties
  ( cd $p && env -u JAVA_TOOL_OPTIONS $D/.g/gradle-$GV/bin/gradle wrapper --no-daemon --no-validate-url --gradle-version $GV -q ) || { echo "could not create the wrapper"; exit 1; }
  # keep the Gradle we just downloaded as the wrapper's own copy, so the first ./gradlew does not download it a second time
  mkdir -p "$DIST" && cp -r $D/.g/gradle-$GV "$DIST/" && touch "$DIST/gradle-$GV-bin.zip.ok"; chown -R $U "$UH/.gradle"
  rm -rf $D/.g
  runuser -u $U -- env HOME=$UH env -u JAVA_TOOL_OPTIONS sh -c "cd $p && ./gradlew showConfig -q --console=plain" >/dev/null 2>&1
  cat > $D/TASKS.txt <<'EOF_K'
LAB 98 : MC11 Gradle environment settings and secrets.   Work in /opt/lab98/cartcore
Always use the wrapper:  ./gradlew ...

0  Look first:  cat gradle.properties   and   ./gradlew -q showConfig      The build reads a password from a file. That is the mistake.
1  Secret out of the files. Remove the password line from gradle.properties. No file in /opt/lab98 may contain that password text any more.
2  Setting in a file. Add  greeting=Welcome to CloudCart  (or your own words) to gradle.properties.
   ./gradlew -q showConfig  must print your greeting.
3  Override on the command line. Run  ./gradlew -q showConfig -Pgreeting=Hello  (or another word) and save the output in /opt/lab98/override.txt.
4  Secret in the environment. Run showConfig with the variable  ORG_GRADLE_PROJECT_repoPassword  set to any test value, for one command only:
       ORG_GRADLE_PROJECT_repoPassword=test123 ./gradlew -q showConfig      and save the output in /opt/lab98/secret.txt.
   It must say  password=set.  The value itself must not appear in any file.
5  Write /opt/lab98/notes.txt with exactly three lines:
     where:    where the secret lives                                       (use the word environment)
     why:      why a secret must not be committed in a file                 (use the word git)
     override: the command line flag that overrides a property             (for example -P)
Then:  lab check     (all 5 must pass)       and later:  lab down
EOF_K
  chown -R $U $D; chmod 755 $D
  echo "lab98 ready: cd $D/cartcore   (task list: $D/TASKS.txt)"
}
check() {
  [ -d $D/cartcore ] || { echo "lab not set up: run  lab up"; exit 1; }
  ok=0
  as() { if [ "$U" = root ]; then "$@"; else runuser -u $U -- env HOME=$UH "$@"; fi; }
  pass() { echo "PASS  $1"; ok=$((ok+1)); }
  fail() { echo "FAIL  $1"; }
  W=/tmp/lab98-chk; rm -rf "${W:?}"; mkdir -p $W; chmod 777 $W
  cp -r $D/cartcore $W/c; rm -rf $W/c/build $W/c/.gradle; chown -R $U $W/c
  gw() { ( cd $W/c && as ./gradlew --no-daemon --console=plain "$@" ) 2>&1 | grep -v '^Picked up' || true; }
  if ! grep -rIl 'Pa55-plain' $D --exclude-dir=.gradle --exclude-dir=build >/dev/null 2>&1; then pass "1 the password text is no longer in any file"; else fail "1 remove the password line from gradle.properties: no file may contain that password"; fi
  gv=$(grep -m1 '^greeting=' $D/cartcore/gradle.properties 2>/dev/null | cut -d= -f2-)
  out=$(gw -q showConfig | grep '^greeting=')
  if [ -n "$gv" ] && [ "$out" = "greeting=$gv" ]; then pass "2 gradle.properties holds the greeting and showConfig prints it"; else fail "2 add a greeting=... line to gradle.properties so showConfig prints it"; fi
  ov=$(grep -m1 '^greeting=' $D/override.txt 2>/dev/null | cut -d= -f2-)
  if [ -n "$ov" ] && [ "$ov" != "$gv" ]; then pass "3 override.txt shows a greeting set with -P that differs from the file"; else fail "3 run ./gradlew -q showConfig -Pgreeting=Hello and save the output in override.txt"; fi
  sx=$( cd $W/c && as env ORG_GRADLE_PROJECT_repoPassword=lab98-check-value ./gradlew --no-daemon --console=plain -q showConfig 2>&1 | grep '^password=' )
  if [ "$sx" = "password=set" ] && grep -q '^password=set' $D/secret.txt 2>/dev/null && ! grep -rIq 'lab98-check-value' $D --exclude-dir=.gradle --exclude-dir=build; then pass "4 the secret comes from the environment: password=set, and it is saved in secret.txt"; else fail "4 run ORG_GRADLE_PROJECT_repoPassword=test123 ./gradlew -q showConfig and save the output in secret.txt"; fi
  g() { sed -n "$1p" $D/notes.txt 2>/dev/null | tr 'A-Z' 'a-z'; }
  if [ -f $D/notes.txt ] && [ "$(grep -c . $D/notes.txt)" = 3 ] && g 1 | grep -q '^where:.*environment' && g 2 | grep -q '^why:.*git' && g 3 | grep -q '^override:.*-p'; then pass "5 notes.txt says where the secret lives, why, and the override flag"; else fail "5 write notes.txt: where: (word environment), why: (word git), override: (flag -P)"; fi
  rm -rf "${W:?}"
  echo "$ok/5 checks passed"; [ $ok -eq 5 ]
}
status() { [ -d $D ] && echo "lab98 is set up in $D" || echo "lab98 is not set up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab98 removed";; status) status;; *) echo "usage: lab98.sh up|check|down|status"; exit 2;; esac
