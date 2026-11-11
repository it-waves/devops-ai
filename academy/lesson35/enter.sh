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
case $S in
 perms) chroot $R runuser -u student -- sh -c 'cd /home/student; printf "#!/bin/sh\necho backup complete\n" > backup.sh; chmod 644 backup.sh';;
 disk) chroot $R runuser -u student -- sh -c 'cd /home/student; truncate -s 100M disk.img; mkfs.ext4 -q -m 0 disk.img'
  chroot $R sh -c 'mkdir -p /home/student/mnt; mount -o loop /home/student/disk.img /home/student/mnt; chown student /home/student/mnt'
  chroot $R runuser -u student -- sh -c 'cd /home/student/mnt; echo "port=80" > app.conf; echo "todo" > notes.txt; dd if=/dev/zero of=old-dump.log bs=4k 2>/dev/null; true';;
 net) ip link set lo up;;
 svc) chroot $R runuser -u student -- sh -c 'cd /home/student; printf "[Unit]\nDescription=Demo web server\n\n[Service]\nExecStart=/usr/bin/pythn3 -m http.server 8080\nRestart=on-failure\n" > web.service';;
esac
exec chroot $R "$@"
