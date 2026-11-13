#!/bin/sh
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
mkdir -p $R/srv/git
SU="chroot $R runuser -u student -- env HOME=/home/student LANG=C.UTF-8"
seed_id() { $SU sh -c 'git config --global user.name "Sam Lee"; git config --global user.email sam@example.com; git config --global init.defaultBranch main'; }
cm() { $SU env GIT_AUTHOR_DATE="$1" GIT_COMMITTER_DATE="$1" sh -c "cd ~/site && git add -A && git commit -qm '$2'"; }
w() { $SU sh -c "cd ~/site && $1"; }
cp -r /home/claude/academy/lesson69/files $R/tmp/l69; chmod -R a+rX $R/tmp/l69
rm -rf /home/student/cloudcart
seed_id() { $SU sh -c 'git config --global user.name "Sam Lee"; git config --global user.email sam@example.com'; }
seed_app() { $SU sh -c 'mkdir -p ~/cloudcart && cp /tmp/l69/* ~/cloudcart/ && cd ~/cloudcart && python3 initdb.py'; }
seed_id; seed_app
exec chroot $R "$@"
