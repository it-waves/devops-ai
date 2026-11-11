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
hostname lab
ip link set lo up
rm -f /run/netns/gw /var/run/netns/gw; echo '127.0.0.1 lab' >> $E/hosts; ip netns add gw; ip link add eth0 type veth peer name gw0; ip link set gw0 netns gw; ip -n gw addr add 10.0.2.2/24 dev gw0; ip -n gw link set gw0 up; ip -n gw link set lo up; ip addr add 10.0.2.15/24 dev eth0; ip link set eth0 up; ip route add default via 10.0.2.2
sed -i 's/^student:[^:]*:/student:*:/' $E/shadow
mkdir -p $E/ssh/sshd_config.d; printf 'Port 22\nListenAddress 127.0.0.1\nPasswordAuthentication no\nPermitRootLogin no\nPubkeyAuthentication yes\nUsePAM no\n' > $E/ssh/sshd_config.d/lab.conf
chroot $R sh -c 'ssh-keygen -A >/dev/null 2>&1; mkdir -p /run/sshd; /usr/sbin/sshd'
case $S in harden) chroot $R runuser -u student -- sh -c 'mkdir -p /home/student/.ssh; sleep 1; ssh-keyscan localhost 127.0.0.1 >> /home/student/.ssh/known_hosts 2>/dev/null';; esac
exec chroot $R "$@"
