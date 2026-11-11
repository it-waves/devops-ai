#!/bin/sh
# builds a clean standard-layout root view for the recordings, then runs the command inside it
R=/tmp/lroot; F=/tmp/fixvarlog
mount --make-rprivate / 2>/dev/null
rm -rf $F; mkdir -p $F/apt; for f in syslog auth.log kern.log dpkg.log; do : > $F/$f; done
mkdir -p $R; for d in usr etc var home tmp proc dev sys root boot opt srv mnt media run; do mkdir -p $R/$d; done; chmod 700 $R/root
ln -sfn usr/bin $R/bin; ln -sfn usr/sbin $R/sbin; ln -sfn usr/lib $R/lib; ln -sfn usr/lib64 $R/lib64
for d in usr etc var home; do mount --bind /$d $R/$d; done
mount --bind $F $R/var/log
mount -t tmpfs tmpfs $R/tmp; chmod 1777 $R/tmp; mount -t tmpfs tmpfs $R/run
mount -t proc proc $R/proc; mount --bind /dev $R/dev
H=/home/student
printf '[Unit]\nDescription=Demo web server\n\n[Service]\nExecStart=/usr/bin/python3 -m http.server 8080\nRestart=on-failure\n\n[Install]\nWantedBy=multi-user.target\n' > $H/web.service
printf '[Unit]\nDescription=Demo web server\n\n[Service]\nExecStart=/usr/bin/pyton3 -m http.server 8080\nRestrat=on-failure\n\n[Install]\nWantedBy=multi-user.target\n' > $H/bad.service
chown student:student $H/web.service $H/bad.service
exec chroot $R "$@"
