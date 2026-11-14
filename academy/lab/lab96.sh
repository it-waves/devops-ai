#!/bin/sh
# lab96.sh : MC11-O02 Gradle: build, test and dependency inspection. Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status
# Needs: a JDK (sudo apt install -y openjdk-21-jdk-headless python3 curl), internet access (the first run downloads Gradle, about 130 MB),
#        about 1 GB of free memory and 1 GB of free disk.
# Mission: make a failing test pass, then read the dependency tree and explain which version Gradle chose and why.
D=${LAB96_DIR:-/opt/lab96}
U=${SUDO_USER:-root}
GV=8.14.3
GURL=https://services.gradle.org/distributions/gradle-$GV-bin.zip
BOOT=${LAB96_GRADLE_ZIP_URL:-$GURL}
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
version = '1.1'

repositories {
    mavenCentral()
}

dependencies {
    implementation 'org.apache.commons:commons-text:1.10.0'
    implementation 'org.apache.commons:commons-lang3:3.9'
    testImplementation 'org.junit.jupiter:junit-jupiter:5.10.2'
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
        return total() - percent;
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
LAB 96 : MC11 Gradle build, test and dependency inspection.   Work in /opt/lab96/cartcore
Always use the wrapper:  ./gradlew ...

1  Run the tests:  ./gradlew test      One test fails. Read the failure message, find the bug in src/main (NOT in the test) and fix it.
   Run ./gradlew test again: all 3 tests must pass.
2  Open the HTML test report (build/reports/tests/test/index.html). Write its path under  report:  in notes.txt (step 5).
3  Save the dependency tree of the runtime classpath. Run:
       ./gradlew dependencies --configuration runtimeClasspath      and save the output in /opt/lab96/deps.txt
4  Ask Gradle why one library has the version it has. Run:
       ./gradlew dependencyInsight --dependency commons-lang3 --configuration runtimeClasspath      and save the output in /opt/lab96/insight.txt
5  Write /opt/lab96/notes.txt with exactly three lines:
     version: the version of commons-lang3 that Gradle really used          (for example  version: 1.2.3)
     why:     why Gradle chose it                                          (use the word conflict)
     report:  the path of the HTML test report                              (it contains reports/tests)
Then:  lab check     (all 5 must pass)       and later:  lab down
EOF_K
  chown -R $U $D; chmod 755 $D
  echo "lab96 ready: cd $D/cartcore   (task list: $D/TASKS.txt)"
}
check() {
  [ -d $D/cartcore ] || { echo "lab not set up: run  lab up"; exit 1; }
  ok=0
  as() { if [ "$U" = root ]; then "$@"; else runuser -u $U -- env HOME=$UH "$@"; fi; }
  pass() { echo "PASS  $1"; ok=$((ok+1)); }
  fail() { echo "FAIL  $1"; }
  W=/tmp/lab96-chk; rm -rf "${W:?}"; mkdir -p $W; chmod 777 $W
  cp -r $D/cartcore $W/c; rm -rf $W/c/build $W/c/.gradle; chown -R $U $W/c
  gw() { ( cd $W/c && as ./gradlew --no-daemon --console=plain "$@" ) 2>&1 | grep -v '^Picked up' || true; }
  if [ "$(sha256sum $D/cartcore/src/test/java/cloudcart/CartTest.java | cut -d' ' -f1)" = "$(cat $D/.testsum)" ] && { gw test -q >/dev/null; [ -f $W/c/build/test-results/test/TEST-cloudcart.CartTest.xml ] && grep -q 'tests="3"' $W/c/build/test-results/test/TEST-cloudcart.CartTest.xml && grep -q 'failures="0"' $W/c/build/test-results/test/TEST-cloudcart.CartTest.xml && grep -q 'errors="0"' $W/c/build/test-results/test/TEST-cloudcart.CartTest.xml; }; then pass "1 all 3 tests pass and the test file is unchanged"; else fail "1 fix the bug in src/main (not in the test) so ./gradlew test passes all 3 tests"; fi
  if [ -f $W/c/build/reports/tests/test/index.html ] && grep -q 'reports/tests' $D/notes.txt 2>/dev/null; then pass "2 the HTML test report exists and notes.txt names it"; else fail "2 run ./gradlew test and name the HTML report path on the report: line of notes.txt"; fi
  gw dependencies --configuration runtimeClasspath > $W/deps.txt
  if [ -f $D/deps.txt ] && grep -q 'runtimeClasspath' $D/deps.txt && grep -q 'commons-text' $D/deps.txt && grep -q 'commons-lang3' $D/deps.txt; then pass "3 deps.txt holds the runtimeClasspath dependency tree"; else fail "3 save ./gradlew dependencies --configuration runtimeClasspath in /opt/lab96/deps.txt"; fi
  if [ -f $D/insight.txt ] && grep -q 'commons-lang3' $D/insight.txt && grep -qi 'selected\|Selection reasons\|conflict' $D/insight.txt; then pass "4 insight.txt holds the dependencyInsight answer for commons-lang3"; else fail "4 save ./gradlew dependencyInsight --dependency commons-lang3 --configuration runtimeClasspath in /opt/lab96/insight.txt"; fi
  real=$(gw dependencyInsight --dependency commons-lang3 --configuration runtimeClasspath | grep -m1 -oE 'commons-lang3:[0-9][0-9A-Za-z.]*' | cut -d: -f2)
  g() { sed -n "$1p" $D/notes.txt 2>/dev/null | tr 'A-Z' 'a-z'; }
  if [ -n "$real" ] && [ -f $D/notes.txt ] && [ "$(grep -c . $D/notes.txt)" = 3 ] && g 1 | grep -qE "^version: *$(echo $real | sed 's/\./\\./g')\$" && g 2 | grep -q '^why:.*conflict' && g 3 | grep -q '^report:.*reports/tests'; then pass "5 notes.txt names the real version, the conflict and the report"; else fail "5 write notes.txt: version: <the version Gradle used>, why: (word conflict), report: (path with reports/tests)"; fi
  rm -rf "${W:?}"
  echo "$ok/5 checks passed"; [ $ok -eq 5 ]
}
status() { [ -d $D ] && echo "lab96 is set up in $D" || echo "lab96 is not set up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab96 removed";; status) status;; *) echo "usage: lab96.sh up|check|down|status"; exit 2;; esac
