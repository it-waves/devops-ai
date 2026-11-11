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
 secrets)
  cat > $D/bad.sh <<'EOT'
#!/bin/bash
DB_PASS="hunter2"
echo "connecting as admin"
EOT
  printf 'API_TOKEN=demo-token-9f2c\n' > $D/.env; chmod 644 $D/.env
  cat > $D/good.sh <<'EOT'
#!/bin/bash
set -euo pipefail
source ./.env
echo "token ends in ${API_TOKEN: -4}"
EOT
  ;;
 perms)
  cat > $D/deploy.sh <<'EOT'
#!/bin/bash
echo "deploying"
EOT
  chmod 644 $D/deploy.sh
  ;;
 validate)
  cat > $D/validate.sh <<'EOT'
#!/bin/bash
set -euo pipefail
re='^[a-z0-9_-]{1,20}$'
[[ "${1:-}" =~ $re ]] || { echo invalid >&2; exit 2; }
echo "creating $1"
EOT
  ;;
 inject)
  printf '2026-11-11 09:01:12 INFO login ok user=sam\n' > $D/app.log
  cat > $D/danger.sh <<'EOT'
#!/bin/bash
eval "ls -l $1"
EOT
  cat > $D/quoted.sh <<'EOT'
#!/bin/bash
ls -l -- "$1"
EOT
  ;;
 build)
  printf 'API_TOKEN=demo-token-9f2c\n' > $D/.env; chmod 600 $D/.env
  cat > $D/secure.sh <<'EOT'
#!/bin/bash
set -euo pipefail
umask 077
re='^[a-z0-9_-]{1,20}$'
[[ "${1:-}" =~ $re ]] || { echo invalid >&2; exit 2; }
source ./.env
out=$(mktemp); trap 'rm -f "$out"' EXIT
echo "deploy $1, token ends ${API_TOKEN: -4}" | tee "$out"
EOT
  ;;
esac
chown -R student:student $D
printf 'cd /home/student/m05\n' >> $E/ps1rc
exec chroot $R "$@"
