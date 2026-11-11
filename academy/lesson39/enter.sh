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
 'if') printf '#!/bin/bash\nn=$1\nif [ "$n" -ge 18 ]; then\n  echo "adult"\nelse\n  echo "minor"\nfi\n' > $D/age.sh; chmod 755 $D/age.sh;;
 tests) : > $D/notes.txt; mkdir $D/docs;;
 'case') printf '#!/bin/bash\ncase "$1" in\n  start) echo "starting" ;;\n  stop)  echo "stopping" ;;\n  *)     echo "usage: $0 start|stop" ;;\nesac\n' > $D/menu.sh; chmod 755 $D/menu.sh;;
 loops) printf '#!/bin/bash\nfor name in web db cache; do\n  echo "checking $name"\ndone\n' > $D/for.sh; printf '#!/bin/bash\ni=1\nwhile [ "$i" -le 3 ]; do\n  echo "round $i"\n  i=$((i+1))\ndone\n' > $D/count.sh; chmod 755 $D/for.sh $D/count.sh; : > $D/app.log; : > $D/web.log;;
 func) : > $D/notes.txt; printf '#!/bin/bash\ngreet() {\n  echo "Hello, $1"\n}\ncheck() {\n  [ -f "$1" ] && echo "$1 found" || echo "$1 missing"\n}\ngreet Sam\ncheck notes.txt\ncheck nope.txt\n' > $D/func.sh; chmod 755 $D/func.sh;;
 build) : > $D/notes.txt; : > $D/app.log; printf '#!/bin/bash\nbad=0\ncheck_file() {\n  if [ -f "$1" ]; then\n    echo "OK    $1"\n  else\n    echo "FAIL  $1"\n    bad=$((bad+1))\n  fi\n}\nfor f in "$@"; do\n  check_file "$f"\ndone\n[ "$bad" -eq 0 ] && echo "all good" || echo "$bad missing"\n' > $D/health.sh; chmod 755 $D/health.sh;;
esac
chown -R student $D
printf 'cd /home/student/m05\n' >> $E/ps1rc
exec chroot $R "$@"
