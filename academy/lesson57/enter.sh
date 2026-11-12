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
DT=2026-01-05T10:00:00+0000
printf 'export GIT_AUTHOR_DATE=%s GIT_COMMITTER_DATE=%s\n' $DT $DT >> $E/ps1rc
SU="chroot $R runuser -u student -- env HOME=/home/student LANG=C.UTF-8 GIT_AUTHOR_DATE=$DT GIT_COMMITTER_DATE=$DT"
seed_id() { $SU sh -c 'git config --global user.name "Sam Lee"; git config --global user.email sam@example.com; git config --global init.defaultBranch main'; }
seed_init() { $SU sh -c 'cd ~ && mkdir notes && cd notes && git init -q'; }
seed_c1() { $SU sh -c 'cd ~/notes && echo "# ports" > README.md && git add README.md && git commit -qm "Start the notes"'; }
seed_c2() { $SU sh -c 'cd ~/notes && echo "ports: 80 443" > ports.txt && git add ports.txt && git commit -qm "Add ports list"'; }
case $S in
 init) :;;
 commit) seed_id; seed_init;;
 objs) seed_id; seed_init; seed_c1; seed_c2;;
 clone) seed_id; seed_init; seed_c1; seed_c2; $SU sh -c 'git clone -q --bare ~/notes /tmp/notes.git' && cp -a $R/tmp/notes.git $R/srv/git/notes.git; chown -R student $R/srv/git; rm -rf $R/home/student/notes;;
esac
exec chroot $R "$@"
