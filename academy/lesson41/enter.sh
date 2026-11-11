#!/bin/sh
# builds a clean standard-layout root view for the recordings (private copy of /etc with sudo for the student), then runs the command inside it
R=/tmp/lroot; F=/tmp/fixvarlog
mount --make-rprivate / 2>/dev/null
rm -rf $F; mkdir -p $F/apt; for f in syslog auth.log kern.log dpkg.log; do : > $F/$f; done
mkdir -p $R; for d in usr etc var home tmp proc dev sys root boot opt srv mnt media run; do mkdir -p $R/$d; done; chmod 700 $R/root
ln -sfn usr/bin $R/bin; ln -sfn usr/sbin $R/sbin; ln -sfn usr/lib $R/lib; ln -sfn usr/lib64 $R/lib64
E=/tmp/fixetc; rm -rf $E; cp -a /etc $E; mkdir -p $E/sudoers.d; echo 'student ALL=(ALL) NOPASSWD:ALL' > $E/sudoers.d/student; chmod 440 $E/sudoers.d/student; chown root:root $E/sudoers.d/student
sed -i 's#^PATH=.*#PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin#' $E/ps1rc
sed -i 's#http://#https://#' $E/apt/sources.list.d/ubuntu.sources
for d in usr var home; do mount --bind /$d $R/$d; done
mount --bind $E $R/etc
mount --bind $F $R/var/log
mount -t tmpfs tmpfs $R/tmp; chmod 1777 $R/tmp; mount -t tmpfs tmpfs $R/run
mount -t proc proc $R/proc; mount --rbind /dev $R/dev; mount --rbind /sys $R/sys
S=$(cat /tmp/lstage 2>/dev/null)
hostname lab; echo '127.0.0.1 lab' >> $E/hosts
sed -i 's/^student:[^:]*:/student:*:/' $E/shadow
D=/home/student/m05
chroot $R runuser -u student -- sh -c 'rm -rf /home/student/m05; mkdir -p /home/student/m05'
case $S in
 streams) :;;
 redir) :;;
 pipes) printf '2026-11-11 09:01:12 INFO login ok user=sam\n2026-11-11 09:02:40 ERROR disk full path=/var\n2026-11-11 09:03:05 INFO login ok user=lee\n2026-11-11 09:04:51 WARN slow query ms=870\n2026-11-11 09:05:19 ERROR timeout host=db1\n2026-11-11 09:06:33 INFO logout user=sam\n' > $D/app.log;;
 tmp) printf '2026-11-11 09:01:12 INFO login ok user=sam\n2026-11-11 09:02:40 ERROR disk full path=/var\n2026-11-11 09:03:05 INFO login ok user=lee\n2026-11-11 09:04:51 WARN slow query ms=870\n2026-11-11 09:05:19 ERROR timeout host=db1\n2026-11-11 09:06:33 INFO logout user=sam\n' > $D/app.log;;
 build) printf '2026-11-11 09:01:12 INFO login ok user=sam\n2026-11-11 09:02:40 ERROR disk full path=/var\n2026-11-11 09:03:05 INFO login ok user=lee\n2026-11-11 09:04:51 WARN slow query ms=870\n2026-11-11 09:05:19 ERROR timeout host=db1\n2026-11-11 09:06:33 INFO logout user=sam\n' > $D/app.log;;
esac
chown -R student $D
printf 'cd /home/student/m05\n' >> $E/ps1rc
exec chroot $R "$@"
