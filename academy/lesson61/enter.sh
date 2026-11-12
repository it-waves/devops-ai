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
seed_c1() { $SU sh -c 'mkdir ~/site && cd ~/site && git init -q'; w "printf '<h1>Notes</h1>\\n<p>Ports: 80</p>\\n' > index.html"; cm 2026-01-05T10:00:00+0000 'Add index page'; w "printf '<h1>Notes</h1>\\n<p>Ports: 80 443</p>\\n' > index.html"; cm 2026-01-06T09:30:00+0000 'List both ports'; }
# shared repo seeds: bare origin at /srv/git/team.git with two commits, built from a scratch work tree
seed_origin() { rm -rf $R/srv/git/team.git $R/home/student/team; $SU sh -c 'rm -rf /tmp/sw /tmp/team.git; mkdir /tmp/sw && cd /tmp/sw && git init -q && printf "port=80\n" > app.conf && git add -A && GIT_AUTHOR_DATE=2026-01-05T10:00:00+0000 GIT_COMMITTER_DATE=2026-01-05T10:00:00+0000 git commit -qm "Add app config" && printf "#!/bin/sh\necho start\n" > start.sh && git add -A && GIT_AUTHOR_DATE=2026-01-06T09:30:00+0000 GIT_COMMITTER_DATE=2026-01-06T09:30:00+0000 git commit -qm "Add start script" && cd /tmp && git clone -q --bare sw team.git'; cp -a $R/tmp/team.git $R/srv/git/team.git; chown -R student $R/srv/git; }
mate() { $SU sh -c 'rm -rf /tmp/mate; git clone -q /srv/git/team.git /tmp/mate && cd /tmp/mate && git config user.name "Alex Kim" && git config user.email alex@example.com && printf "timeout=5\n" >> app.conf && git add -A && GIT_AUTHOR_DATE=2026-01-07T12:00:00+0000 GIT_COMMITTER_DATE=2026-01-07T12:00:00+0000 git commit -qm "Add timeout setting" && git push -q origin main'; }
myclone() { $SU sh -c 'cd ~ && git clone -q /srv/git/team.git'; }
case $S in
 clone) seed_id; seed_origin;;
 fetch) seed_id; seed_origin; myclone; mate;;
 push) seed_id; seed_origin; myclone; mate;;
 tags) seed_id; seed_origin; myclone;;
esac
exec chroot $R "$@"
