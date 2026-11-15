L="env SUDO_USER=student sh /usr/local/sbin/lab99.sh"
$L down >/dev/null; LAB99_GRADLE_ZIP_URL=file:///opt/dist/gradle-8.14.3-bin.zip $L up >/dev/null 2>&1; cd /opt/lab99/cartcore
echo "base: $($L check 2>&1 | tail -1)"
echo 'org.gradle.caching=true' > gradle.properties; chown -R student /opt/lab99
echo "cache: $($L check 2>&1 | tail -1)"
sed -i "/Built-At/d" build.gradle; echo "stamp: $($L check 2>&1 | tail -1)"
sed -i 's/^jar {/jar {\n    preserveFileTimestamps = false\n    reproducibleFileOrder = true/' build.gradle
printf 'up-to-date: same input so Gradle skips the task\nfrom-cache: the result is stored by key so it survives clean\nreproducible: no timestamp inside the jar\n' > /opt/lab99/notes.txt
echo "final: $($L check 2>&1 | tail -1)"; cd /; $L down
