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
cp -r /home/claude/academy/lesson65/files $R/tmp/l65; chmod -R a+rX $R/tmp/l65
rm -rf $R/srv/git/shop.git /home/student/shop; chown student $R/srv/git
cm2() { $SU env GIT_AUTHOR_DATE="$1" GIT_COMMITTER_DATE="$1" sh -c "cd ~/shop && git add -A && git commit -qm '$2'"; }
seed_shop() {
  $SU sh -c 'git init -q --bare -b main /srv/git/shop.git; git clone -q /srv/git/shop.git ~/shop 2>/dev/null; cd ~/shop && mkdir -p .githooks .github/workflows && cp /tmp/l65/shop.sh /tmp/l65/test.sh /tmp/l65/check.sh . && cp /tmp/l65/pre-push .githooks/ && cp /tmp/l65/ci.yml .github/workflows/'
  cm2 2026-01-05T10:00:00+0000 'Add shop script and checks'; $SU sh -c 'cd ~/shop && git push -q origin main'
}
seed_release() {
  seed_shop; $SU sh -c 'cd ~/shop && git tag -a v1.0.0 -m "First release" && git push -q origin v1.0.0 && cp /tmp/l65/README.md .'
  cm2 2026-01-06T10:00:00+0000 'Add readme'; $SU sh -c 'cd ~/shop && cp /tmp/l65/discount.sh .'; cm2 2026-01-07T10:00:00+0000 'Add discount option'; $SU sh -c 'cd ~/shop && git push -q origin main'
}
case $S in
 checks|gate|ci) seed_id; seed_shop;;
 release) seed_id; seed_release;;
esac
exec chroot $R "$@"
