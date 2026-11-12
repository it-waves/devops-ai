#!/bin/sh
# lab46.sh : Bash scripting mastery lab. Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status
# Mission: four checks must say PASS. Four scripts are broken on purpose.
D=/opt/lab46
U=${SUDO_USER:-root}
down() { rm -rf $D; true; }
up() {
  down
  mkdir -p $D/bin $D/notes $D/archive $D/conf $D/logs
  echo "buy milk" > "$D/notes/daily notes.txt"
  printf '2024-05-01 INFO start\n2024-05-01 ERROR disk full\n2024-05-01 INFO retry\n2024-05-02 ERROR timeout, ERROR retry failed\n2024-05-02 INFO done\n2024-05-03 ERROR disk full\n' > $D/logs/app.log
  # fault 1: an unquoted variable breaks on a file name with a space
  printf '#!/bin/bash\n# copy a file into the archive folder\nsrc=$1\ncp $src /opt/lab46/archive/\necho "archived $src"\n' > $D/bin/archive.sh
  # fault 2: the script reports success even when the backup fails
  printf '#!/bin/bash\n# make a compressed backup of a folder\ndir=$1\ntar -czf /opt/lab46/archive/backup.tgz "$dir" 2>/dev/null\necho "backup finished"\n' > $D/bin/backup.sh
  # fault 3: a for loop over $(cat file) splits the log into words, not lines
  printf '#!/bin/bash\n# print how many log lines contain ERROR\nn=0\nfor line in $(cat "$1"); do\n  case $line in *ERROR*) n=$((n+1));; esac\ndone\necho $n\n' > $D/bin/count_errors.sh
  # fault 4: running it twice adds the setting twice
  printf '#!/bin/bash\n# add the app setting to the config file\necho "LAB46_MODE=prod" >> /opt/lab46/conf/app.env\n' > $D/bin/setup.sh
  chmod 755 $D/bin/*.sh; chown -R $U $D 2>/dev/null
  echo "lab is up. Four scripts are wrong. Goal: four PASS lines."
}
chk() { if eval "$2" >/dev/null 2>&1; then echo "PASS  $1"; else echo "FAIL  $1"; fi; }
check() {
  chk "1 archive.sh copes with a space in the name" "rm -f '$D/archive/daily notes.txt'; $D/bin/archive.sh '$D/notes/daily notes.txt' && test -f '$D/archive/daily notes.txt'"
  chk "2 backup.sh fails when the folder is missing" "$D/bin/backup.sh $D/notes && ! $D/bin/backup.sh $D/nothing-here"
  chk "3 count_errors.sh counts lines, not words" "test \$($D/bin/count_errors.sh $D/logs/app.log) = 3"
  chk "4 setup.sh is safe to run twice" "rm -f $D/conf/app.env; $D/bin/setup.sh; $D/bin/setup.sh; test \$(grep -c LAB46_MODE $D/conf/app.env) = 1"
}
case "$1" in up) up;; down) down; echo "lab removed.";; check) check;; status) check;; *) echo "usage: sudo lab46.sh up | check | down";; esac
