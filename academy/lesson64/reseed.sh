#!/bin/sh
# resets the private Gitea used for the Lesson 62 recording (runs only on this recording computer, 127.0.0.1)
G=/tmp/gt; B=/tmp/gitea_dl/gitea; R="runuser -u gt -- env GITEA_WORK_DIR=$G HOME=/home/gt"
pkill -u gt gitea 2>/dev/null; sleep 1
rm -rf $G/data $G/repos $G/log; mkdir -p $G/data $G/repos; chown -R gt $G
$R $B migrate -c $G/custom/conf/app.ini >/dev/null 2>&1
PW=$(cat $G/adminpw)
$R $B admin user create --admin --username sam --password "$PW" --email sam@example.com --must-change-password=false -c $G/custom/conf/app.ini >/dev/null 2>&1
$R $B admin user create --username alex --password "$PW" --email alex@example.com --must-change-password=false -c $G/custom/conf/app.ini >/dev/null 2>&1
(nohup $R $B web -c $G/custom/conf/app.ini > $G/gitea.log 2>&1 &)
for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15; do curl -s -o /dev/null http://127.0.0.1:3000/ && break; sleep 1; done
A="curl -s -u sam:$PW -H Content-Type:application/json"
$A -X POST http://127.0.0.1:3000/api/v1/user/repos -d '{"name":"team-app","description":"Practice repository for pull requests","default_branch":"main","auto_init":false,"private":false}' >/dev/null
$A -X PUT http://127.0.0.1:3000/api/v1/repos/sam/team-app/collaborators/alex -d '{"permission":"write"}' >/dev/null
W=/tmp/seedwork; rm -rf $W; mkdir -p $W; cd $W; git init -q -b main .; git config user.name "Sam Lee"; git config user.email sam@example.com
d() { export GIT_AUTHOR_DATE="$1" GIT_COMMITTER_DATE="$1"; }
d "$(date -u -d '5 days ago' +%Y-%m-%dT10:00:00+0000)"; printf '# team-app\nA small demo service.\n' > README.md; printf 'port=80\ntimeout=5\n' > app.conf; git add -A; git commit -qm "Add app config and readme"
d "$(date -u -d '4 days ago' +%Y-%m-%dT10:00:00+0000)"; printf '#!/bin/sh\necho start\n' > start.sh; git add -A; git commit -qm "Add start script"
git remote add origin http://sam:$PW@127.0.0.1:3000/sam/team-app.git; git push -q origin main 2>&1 | tail -1
git switch -q -c feature/health-check
d "$(date -u -d '30 minutes ago' +%Y-%m-%dT%H:%M:00+0000)"; printf '#!/bin/sh\ncurl -s localhost:80 > /dev/null && echo healthy\n' > health.sh; git add -A; git commit -qm "Add health check script"
d "$(date -u -d '10 minutes ago' +%Y-%m-%dT%H:%M:00+0000)"; printf '# team-app\nA small demo service.\n\nRun health.sh to check the service.\n' > README.md; git add -A; git commit -qm "Document the health check"
git push -q origin feature/health-check 2>&1 | tail -1
echo reseeded
