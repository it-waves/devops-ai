#!/bin/sh
MO="$JAVA_TOOL_OPTIONS"; unset JAVA_TOOL_OPTIONS
# builds a clean standard-layout root view for the recordings (private copy of /etc with sudo for the student), then runs the command inside it
R=/tmp/lroot; F=/tmp/fixvarlog
mount --make-rprivate / 2>/dev/null
rm -rf $F; mkdir -p $F/apt; for f in syslog auth.log kern.log dpkg.log; do : > $F/$f; done
mkdir -p $R; for d in usr etc var home tmp proc dev sys root boot opt srv mnt media run; do mkdir -p $R/$d; done; chmod 700 $R/root
ln -sfn usr/bin $R/bin; ln -sfn usr/sbin $R/sbin; ln -sfn usr/lib $R/lib; ln -sfn usr/lib64 $R/lib64
E=/tmp/fixetc; rm -rf $E; cp -a /etc $E; mkdir -p $E/sudoers.d; echo 'student ALL=(ALL) NOPASSWD:ALL' > $E/sudoers.d/student; chmod 440 $E/sudoers.d/student; chown root:root $E/sudoers.d/student
sed -i 's#^lab() .*#lab() { sudo /usr/local/sbin/lab107.sh "$@"; }#' $E/ps1rc
sed -i 's#^PATH=.*#PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin#' $E/ps1rc
printf '%s\n' 'PS1=${PS1//\\w/\\W}' >> $E/ps1rc
sed -i 's#http://#https://#' $E/apt/sources.list.d/ubuntu.sources
for d in usr var home; do mount --bind /$d $R/$d; done
mount --bind $E $R/etc
mount --bind $F $R/var/log
mount -t tmpfs tmpfs $R/tmp; chmod 1777 $R/tmp; mount -t tmpfs tmpfs $R/run
mount -t proc proc $R/proc; mount --rbind /dev $R/dev; mount --rbind /sys $R/sys
hostname lab; echo '127.0.0.1 lab' >> $E/hosts
sed -i 's/^student:[^:]*:/student:*:/' $E/shadow
mount -t tmpfs tmpfs $R/usr/local/sbin
mount -t tmpfs tmpfs $R/usr/local/bin
cp /home/claude/devops-ai/academy/lab/lab107.sh $R/usr/local/sbin/lab107.sh; chmod 755 $R/usr/local/sbin/lab107.sh
mkdir -p $R/opt/dist; mount --bind /opt/dist $R/opt/dist
touch /home/student/.ready; chown student /home/student/.ready
mount --rbind $R $R; mkdir -p $R/.old; cd $R; pivot_root . .old; cd /; umount -l /.old 2>/dev/null
exec /usr/lib/systemd/systemd --system --unit=multi-user.target
