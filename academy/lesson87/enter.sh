#!/bin/sh
unset JAVA_TOOL_OPTIONS
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
ip link set lo up
mount -t tmpfs tmpfs $R/usr/local/sbin
mount -t tmpfs tmpfs $R/usr/local/bin
ln -s /usr/bin/python3.12 $R/usr/local/bin/python3; ln -s /usr/bin/python3.12 $R/usr/local/bin/python
SU="chroot $R runuser -u student -- env -u JAVA_TOOL_OPTIONS HOME=/home/student LANG=C.UTF-8"
mkdir -p $R/opt/maven $R/opt/m2mirror; mount --bind /opt/maven $R/opt/maven; mount --bind /opt/m2mirror $R/opt/m2mirror
ln -sf /opt/maven/bin/mvn $R/usr/local/bin/mvn
rm -rf /home/student/.m2 /home/student/demo; mkdir -p /home/student/.m2; cp /home/claude/academy/lesson87/settings.xml.src /home/student/.m2/settings.xml; chown -R student /home/student/.m2
cp -r /home/claude/academy/lesson87/files/demo $R/tmp/demo87; chmod -R a+rX $R/tmp/demo87
$SU sh -c 'mkdir -p ~/demo && cp -r /tmp/demo87/. ~/demo/'
case $S in cfg|repro) $SU sh -c 'cp -r ~/demo /tmp/warm && cd /tmp/warm && mvn -B -q package >/dev/null 2>&1; rm -rf /tmp/warm' ;; esac
exec chroot $R "$@"
