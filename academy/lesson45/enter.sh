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
mkrel() { for v in v1 v2 v3; do mkdir -p $D/releases/$v; printf '%s\n' $v > $D/releases/$v/version; done; printf 'ok\n' > $D/releases/v1/health; printf 'ok\n' > $D/releases/v2/health; }
cat > $D/release.sh <<'EOT'
#!/bin/bash
set -euo pipefail
new=$1
old=$(readlink current || true)
ln -sfn "releases/$new" current
if curl -fsS localhost:8080/health >/dev/null; then
  echo "deployed $new"
else
  echo "FAILED, rolling back to $old" >&2
  ln -sfn "$old" current
  exit 1
fi
EOT
mkrel
case $S in
 rollback) ln -sfn releases/v2 $D/current ;;
 *) ln -sfn releases/v1 $D/current ;;
esac

chown -R student:student $D
printf 'cd /home/student/m05\nexport SHELLCHECK_OPTS=--wiki-link-count=0\n' >> $E/ps1rc
ip link set lo up
chroot $R runuser -u student -- sh -c 'cd /home/student/m05 && nohup python3 -m http.server 8080 --bind 127.0.0.1 --directory current >/dev/null 2>&1 &'
sleep 1.5
exec chroot $R "$@"

