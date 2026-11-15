#!/bin/sh
MO="$JAVA_TOOL_OPTIONS"; unset JAVA_TOOL_OPTIONS
# builds a clean standard-layout root view for the recordings (private copy of /etc with sudo for the student), then runs the command inside it
R=/tmp/lroot; F=/tmp/fixvarlog
mount --make-rprivate / 2>/dev/null
rm -rf $F; mkdir -p $F/apt; for f in syslog auth.log kern.log dpkg.log; do : > $F/$f; done
mkdir -p $R; for d in usr etc var home tmp proc dev sys root boot opt srv mnt media run; do mkdir -p $R/$d; done; chmod 700 $R/root
ln -sfn usr/bin $R/bin; ln -sfn usr/sbin $R/sbin; ln -sfn usr/lib $R/lib; ln -sfn usr/lib64 $R/lib64
E=/tmp/fixetc; rm -rf $E; cp -a /etc $E; mkdir -p $E/sudoers.d; echo 'student ALL=(ALL) NOPASSWD:ALL' > $E/sudoers.d/student; chmod 440 $E/sudoers.d/student; chown root:root $E/sudoers.d/student
sed -i 's#^PATH=.*#PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin#' $E/ps1rc
printf '%s\n' 'PS1=${PS1//\\w/\\W}' >> $E/ps1rc
sed -i 's#http://#https://#' $E/apt/sources.list.d/ubuntu.sources
for d in usr var home; do mount --bind /$d $R/$d; done
mount --bind $E $R/etc
mount --bind $F $R/var/log
mount -t tmpfs tmpfs $R/tmp; chmod 1777 $R/tmp; mount -t tmpfs tmpfs $R/run
mount -t proc proc $R/proc; mount --rbind /dev $R/dev; mount --rbind /sys $R/sys
S=$(cat /tmp/lstage 2>/dev/null)
hostname lab; echo '127.0.0.1 lab' >> $E/hosts
sed -i 's/^student:[^:]*:/student:*:/' $E/shadow
mount -t tmpfs tmpfs $R/usr/local/sbin
mount -t tmpfs tmpfs $R/usr/local/bin
ln -s /usr/bin/python3.12 $R/usr/local/bin/python3; ln -s /usr/bin/python3.12 $R/usr/local/bin/python
SU="chroot $R runuser -u student -- env -u JAVA_TOOL_OPTIONS HOME=/home/student LANG=C.UTF-8"
# the studio wipes /home/student before every recording: put the wrapper's copy of Gradle back (same folder the wrapper looks in)
GH=$(python3 -c "import hashlib;n=int.from_bytes(hashlib.md5(b'https://services.gradle.org/distributions/gradle-8.14.3-bin.zip').digest(),'big');a='0123456789abcdefghijklmnopqrstuvwxyz';s=''
while n:
    n,r=divmod(n,36);s=a[r]+s
print(s)")
GD=/home/student/.gradle/wrapper/dists/gradle-8.14.3-bin/$GH; mkdir -p $GD && unzip -q /opt/dist/gradle-8.14.3-bin.zip -d $GD && touch $GD/gradle-8.14.3-bin.zip.ok; chown -R student /home/student/.gradle
mkdir -p $R/opt/lab100; mount --bind /opt/lab100 $R/opt/lab100
# the libraries (JUnit, Commons) were downloaded once from Maven Central; put that cache back after the studio wipes the home folder
# warm the Gradle daemon (JIT, caches) on a private copy, so the live demo is quick and the real project stays untouched
$SU sh -c "rm -rf /tmp/w1; cp -r /opt/lab100/cartcore /tmp/w1; cd /tmp/w1 && ./gradlew jar -q >/tmp/warm1.log 2>&1; ./gradlew --version >/tmp/warm2.log 2>&1; rm -rf /tmp/w1"
echo "org.gradle.console=plain" > /home/student/.gradle/gradle.properties; chown student /home/student/.gradle/gradle.properties
touch /home/student/.ready; chown student /home/student/.ready
exec chroot $R "$@"
