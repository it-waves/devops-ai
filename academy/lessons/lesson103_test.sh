cp /home/claude/devops-ai/academy/lab/lab103.sh /usr/local/sbin/lab103.sh; chmod 755 /usr/local/sbin/lab103.sh
L="env SUDO_USER=student sh /usr/local/sbin/lab103.sh"
$L down >/dev/null; LAB103_GRADLE_ZIP_URL=file:///opt/dist/gradle-8.14.3-bin.zip $L up >/dev/null 2>&1; cd /opt/lab103/cartcore
tar xzf /opt/dist/gradle-libs-96.tgz -C /home/student 2>/dev/null; chown -R student /home/student/.gradle 2>/dev/null
echo "base: $($L check 2>&1 | tail -1)"
sed -i 's/5.10.99/5.10.2/' build.gradle; sed -i 's/cents + /cents - /' src/main/java/com/cloudcart/Cart.java; echo "build: $($L check 2>&1 | tail -1)"
sed -i "s#^test {#tasks.withType(AbstractArchiveTask).configureEach { preserveFileTimestamps = false; reproducibleFileOrder = true }\ntest {#" build.gradle; echo "repro: $($L check 2>&1 | tail -1)"
sed -i "s#releaseKey = 'S3cr3t-r3l3as3-key'#releaseKey = System.getenv('REPO_PASS')#" build.gradle; echo "secret: $($L check 2>&1 | tail -1)"
printf 'problems: bad junit version and a discount bug\nfixes: set 5.10.2 and subtract the discount\ncleanup: run lab down to remove everything\n' > report.txt; $L check 2>&1 | tail -6


cd /; $L down; ls /opt/lab103 2>&1 | head -1
