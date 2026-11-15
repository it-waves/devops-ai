cp /home/claude/devops-ai/academy/lab/lab102.sh /usr/local/sbin/lab102.sh; chmod 755 /usr/local/sbin/lab102.sh
L="env SUDO_USER=student sh /usr/local/sbin/lab102.sh"
$L down >/dev/null; LAB102_GRADLE_ZIP_URL=file:///opt/dist/gradle-8.14.3-bin.zip $L up >/dev/null 2>&1; cd /opt/lab102/cartcore
echo "base: $($L check 2>&1 | tail -1)"
sed -i 's#<dependencies>#<dependencies><dependency><groupId>org.apache.commons</groupId><artifactId>commons-lang3</artifactId><version>3.12.0</version></dependency>#' pom.xml; echo "maven: $($L check 2>&1 | tail -1)"
sed -i "s#^dependencies {#dependencies {\n    implementation 'org.apache.commons:commons-lang3:3.12.0'#" build.gradle; echo "gradle: $($L check 2>&1 | tail -1)"
tar xzf /opt/dist/gradle-libs-96.tgz -C /home/student 2>/dev/null
runuser -u student -- sh -c 'cd /opt/lab102/cartcore && ./gradlew build -q >/dev/null 2>&1; ./gradlew build > gradle-second.txt 2>&1'
echo "evidence: $($L check 2>&1 | tail -1)"
printf 'maven: strict conventions and a huge shared plugin base\ngradle: fast incremental builds with flexible scripts\nchoice: gradle for build speed in CI, maven for simple standard apps\n' > decision.txt; $L check 2>&1 | tail -6
cd /; $L down; ls /opt/lab102 2>&1 | head -1
