#!/bin/sh
# lab97.sh : MC11-O03 Gradle: dependencies, a version catalog, plugins and publishing. Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status
# Needs: a JDK (sudo apt install -y openjdk-21-jdk-headless python3 curl), internet access (the first run downloads Gradle, about 130 MB),
#        about 1 GB of free memory and 1 GB of free disk.
# Mission: put each library in the right scope, move versions into a version catalog, publish the jar with the maven-publish plugin.
D=${LAB97_DIR:-/opt/lab97}
U=${SUDO_USER:-root}
GV=8.14.3
GURL=https://services.gradle.org/distributions/gradle-$GV-bin.zip
BOOT=${LAB97_GRADLE_ZIP_URL:-$GURL}
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
version = '1.2'

repositories {
    mavenCentral()
}

dependencies {
    implementation 'org.apache.commons:commons-text:1.10.0'
    implementation 'org.apache.commons:commons-lang3:3.9'
    implementation 'org.junit.jupiter:junit-jupiter:5.10.2'
    testRuntimeOnly 'org.junit.platform:junit-platform-launcher:1.10.2'
}

test {
    useJUnitPlatform()
    testLogging {
        events 'failed'
        exceptionFormat 'full'
    }
}

jar {
    manifest {
        attributes 'Main-Class': 'cloudcart.Main'
    }
}
EOF_B
  mkdir -p $p/src/test/java/cloudcart
  cat > $p/src/main/java/cloudcart/Cart.java <<'EOF_C'
package cloudcart;

import java.util.ArrayList;
import java.util.List;

public class Cart {
    private final List<Double> prices = new ArrayList<>();

    public void add(double price) {
        prices.add(price);
    }

    public double total() {
        double sum = 0;
        for (double p : prices) {
            sum += p;
        }
        return sum;
    }

    public double totalWithDiscount(double percent) {
        return total() * (1 - percent / 100);
    }
}
EOF_C
  cat > $p/src/main/java/cloudcart/Main.java <<'EOF_M'
package cloudcart;

import org.apache.commons.text.WordUtils;

public class Main {
    public static void main(String[] args) {
        Cart cart = new Cart();
        cart.add(20.00);
        cart.add(30.00);
        System.out.println(WordUtils.capitalizeFully("cloudcart cart core") + ": total " + cart.total());
    }
}
EOF_M
  cat > $p/src/test/java/cloudcart/CartTest.java <<'EOF_T'
package cloudcart;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class CartTest {
    @Test
    void emptyCartIsZero() {
        assertEquals(0.0, new Cart().total(), 0.001);
    }

    @Test
    void totalAddsPrices() {
        Cart c = new Cart();
        c.add(20.00);
        c.add(30.00);
        assertEquals(50.00, c.total(), 0.001);
    }

    @Test
    void tenPercentDiscount() {
        Cart c = new Cart();
        c.add(20.00);
        c.add(30.00);
        assertEquals(45.00, c.totalWithDiscount(10), 0.001);
    }
}
EOF_T
  sha256sum $p/src/test/java/cloudcart/CartTest.java | cut -d' ' -f1 > $D/.testsum
  ( cd $p && env -u JAVA_TOOL_OPTIONS $D/.g/gradle-$GV/bin/gradle wrapper --no-daemon --no-validate-url --gradle-version $GV -q ) || { echo "could not create the wrapper"; exit 1; }
  # keep the Gradle we just downloaded as the wrapper's own copy, so the first ./gradlew does not download it a second time
  mkdir -p "$DIST" && cp -r $D/.g/gradle-$GV "$DIST/" && touch "$DIST/gradle-$GV-bin.zip.ok"; chown -R $U "$UH/.gradle"
  rm -rf $D/.g
  echo "downloading the libraries (JUnit, Commons) from Maven Central ..."
  for t in 1 2 3 4 5 6; do o=$( cd $p && runuser -u $U -- env HOME=$UH env -u JAVA_TOOL_OPTIONS ./gradlew test --console=plain 2>&1 ); echo "$o" | grep -q 'Could not' || break; sleep 20; done
  cat > $D/TASKS.txt <<'EOF_K'
LAB 97 : MC11 Gradle dependencies, version catalog, plugins and publishing.   Work in /opt/lab97/cartcore
Always use the wrapper:  ./gradlew ...

1  Scope. The test library JUnit is declared as  implementation  so it would travel with the app. Make it a test-only dependency
   (testImplementation). Prove it: ./gradlew dependencies --configuration runtimeClasspath must not list junit.
2  Version catalog. Create gradle/libs.versions.toml with a [versions] and a [libraries] table that define commons-text (1.10.0)
   and junit-jupiter (5.10.2). In build.gradle use  libs.commons.text  and  libs.junit.jupiter  and remove the literal
   'org.apache.commons:commons-text:1.10.0' text. The 3 tests must still pass.
3  Plugin and repository. Add the  maven-publish  plugin and this block to build.gradle:
       publishing {
           publications { maven(MavenPublication) { from components.java } }
           repositories { maven { url = layout.buildDirectory.dir('repo') } }
       }
   Run  ./gradlew publish  : the jar and the pom appear under build/repo (this folder plays the part of a Nexus repository).
4  Read the pom: build/repo/com/cloudcart/cartcore/1.2/cartcore-1.2.pom lists commons-text, and no junit.
5  Write /opt/lab97/notes.txt with exactly three lines:
     catalog:   the path of your version catalog file                      (it ends with libs.versions.toml)
     published: the path of the published pom file                         (it ends with cartcore-1.2.pom)
     scope:     why JUnit is testImplementation, not implementation        (use the word test)
Then:  lab check     (all 5 must pass)       and later:  lab down
EOF_K
  chown -R $U $D; chmod 755 $D
  echo "lab97 ready: cd $D/cartcore   (task list: $D/TASKS.txt)"
}
check() {
  [ -d $D/cartcore ] || { echo "lab not set up: run  lab up"; exit 1; }
  ok=0
  as() { if [ "$U" = root ]; then "$@"; else runuser -u $U -- env HOME=$UH "$@"; fi; }
  pass() { echo "PASS  $1"; ok=$((ok+1)); }
  fail() { echo "FAIL  $1"; }
  W=/tmp/lab97-chk; rm -rf "${W:?}"; mkdir -p $W; chmod 777 $W
  cp -r $D/cartcore $W/c; rm -rf $W/c/build $W/c/.gradle; chown -R $U $W/c
  gw() { ( cd $W/c && as ./gradlew --no-daemon --console=plain "$@" ) 2>&1 | grep -v '^Picked up' || true; }
  if [ "$(sha256sum $D/cartcore/src/test/java/cloudcart/CartTest.java | cut -d' ' -f1)" = "$(cat $D/.testsum)" ] && gw dependencies --configuration runtimeClasspath > $W/rt.txt && ! grep -qi 'junit' $W/rt.txt && grep -q 'commons-text' $W/rt.txt && { gw dependencies --configuration testRuntimeClasspath | grep -q 'junit-jupiter'; }; then pass "1 JUnit is test-only: not on runtimeClasspath, still on testRuntimeClasspath"; else fail "1 declare junit-jupiter with testImplementation so runtimeClasspath has no junit"; fi
  gw test -q >/dev/null; x=$W/c/build/test-results/test/TEST-cloudcart.CartTest.xml
  if [ -f $D/cartcore/gradle/libs.versions.toml ] && grep -q '^\[versions\]' $D/cartcore/gradle/libs.versions.toml && grep -q '^\[libraries\]' $D/cartcore/gradle/libs.versions.toml && grep -q 'libs\.commons\.text' $D/cartcore/build.gradle && grep -q 'libs\.junit\.jupiter' $D/cartcore/build.gradle && ! grep -q 'commons-text:1\.10\.0' $D/cartcore/build.gradle && [ -f $x ] && grep -q 'tests="3"' $x && grep -q 'failures="0"' $x; then pass "2 versions live in gradle/libs.versions.toml and the 3 tests still pass"; else fail "2 create gradle/libs.versions.toml, use libs.commons.text and libs.junit.jupiter, keep the tests green"; fi
  if grep -q 'maven-publish' $D/cartcore/build.gradle && grep -q 'publishing' $D/cartcore/build.gradle && grep -q 'mavenCentral' $D/cartcore/build.gradle; then pass "3 build.gradle applies maven-publish and still reads from mavenCentral"; else fail "3 add id 'maven-publish' and a publishing { } block to build.gradle"; fi
  gw publish -q >/dev/null; P=$W/c/build/repo/com/cloudcart/cartcore/1.2
  if [ -f $P/cartcore-1.2.jar ] && [ -f $P/cartcore-1.2.pom ] && grep -q 'commons-text' $P/cartcore-1.2.pom && ! grep -qi 'junit' $P/cartcore-1.2.pom; then pass "4 ./gradlew publish writes the jar and a pom with commons-text and no junit"; else fail "4 run ./gradlew publish: the pom must list commons-text and no junit"; fi
  g() { sed -n "$1p" $D/notes.txt 2>/dev/null | tr 'A-Z' 'a-z'; }
  if [ -f $D/cartcore/build/repo/com/cloudcart/cartcore/1.2/cartcore-1.2.pom ] && [ -f $D/notes.txt ] && [ "$(grep -c . $D/notes.txt)" = 3 ] && g 1 | grep -q '^catalog:.*libs\.versions\.toml' && g 2 | grep -q '^published:.*cartcore-1\.2\.pom' && g 3 | grep -q '^scope:.*test'; then pass "5 notes.txt names the catalog, the published pom and the scope"; else fail "5 run ./gradlew publish in your own folder, then write the three lines of notes.txt"; fi
  rm -rf "${W:?}"
  echo "$ok/5 checks passed"; [ $ok -eq 5 ]
}
status() { [ -d $D ] && echo "lab97 is set up in $D" || echo "lab97 is not set up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab97 removed";; status) status;; *) echo "usage: lab97.sh up|check|down|status"; exit 2;; esac
