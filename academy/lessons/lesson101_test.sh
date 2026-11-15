cp /home/claude/devops-ai/academy/lab/lab101.sh /usr/local/sbin/lab101.sh; chmod 755 /usr/local/sbin/lab101.sh
L="env SUDO_USER=student sh /usr/local/sbin/lab101.sh"
$L down >/dev/null; LAB101_GRADLE_ZIP_URL=file:///opt/dist/gradle-8.14.3-bin.zip $L up >/dev/null 2>&1; cd /opt/lab101/cartcore
echo "base: $($L check 2>&1 | tail -1)"
sed -i 's/-Xmx16m/-Xmx512m/' gradle.properties; echo "daemon: $($L check 2>&1 | tail -1)"
sed -i 's/3.99.1/3.12.0/' build.gradle; echo "dep: $($L check 2>&1 | tail -1)"
sed -i 's/cents + (cents/cents - (cents/' src/main/java/com/cloudcart/Cart.java; echo "task: $($L check 2>&1 | tail -1)"
printf 'daemon: the daemon could not start because the heap was tiny\ndependency: the version of commons lang did not exist\ntask: the discount was added instead of subtracted\n' > notes.txt; $L check 2>&1 | tail -6
cd /; $L down; ls /opt/lab101 2>&1 | head -1
