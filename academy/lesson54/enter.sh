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
# --- MC06 Python base: stock Ubuntu 24.04 python3 is 3.12 (the host default was switched to 3.13), pip through the recording computer's proxy ---
mount -t tmpfs tmpfs $R/usr/local/bin
ln -s /usr/bin/python3.12 $R/usr/local/bin/python3; ln -s /usr/bin/python3.12 $R/usr/local/bin/python
cp /root/.ccr/ca-bundle.crt $E/pip-ca.crt
printf 'export PIP_CERT=/etc/pip-ca.crt REQUESTS_CA_BUNDLE=/etc/pip-ca.crt SSL_CERT_FILE=/etc/pip-ca.crt PIP_DISABLE_PIP_VERSION_CHECK=1 HTTPS_PROXY=%s https_proxy=%s\n' "$HTTPS_PROXY" "$HTTPS_PROXY" >> $E/ps1rc

S=$(cat /tmp/lstage 2>/dev/null)
D=/home/student/m06
chroot $R runuser -u student -- sh -c 'rm -rf /home/student/m06; mkdir -p /home/student/m06'
A=/home/claude/academy/lesson54/demo
PE='env -i HOME=/home/student PATH=/usr/local/bin:/usr/bin:/bin HTTPS_PROXY='"$HTTPS_PROXY"' PIP_CERT=/etc/pip-ca.crt PIP_DISABLE_PIP_VERSION_CHECK=1'
chroot $R runuser -u student -- $PE sh -c "cd /home/student/m06 && python3 -m venv .venv && .venv/bin/pip install -q --no-index --find-links /home/claude/whl54 boto3 moto"
case $S in
 policy) cp $A/policy.json $A/bad.json $A/audit.py $D/;;
 sdk) cp $A/s3list.py $A/s3miss.py $D/;;
esac
chown -R student $D
printf 'cd /home/student/m06\n. .venv/bin/activate\n' >> $E/ps1rc
exec chroot $R "$@"
