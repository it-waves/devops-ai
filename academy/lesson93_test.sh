L=/home/claude/devops-ai/academy/lab/lab93.sh
export SUDO_USER=student ACCEPT_NEXUS_EULA=yes
pkill -u nexus java 2>/dev/null; sleep 4
sh $L down >/dev/null; sh $L up > /tmp/up93.out 2>&1; tail -3 /tmp/up93.out
echo "-- start"; sh $L check | tail -7
P=$(cat /opt/lab93/pass.txt)
ed() { curl -s -u admin:$P -H 'Content-Type: application/json' -X POST http://127.0.0.1:8081/service/extdirect -d "$1"; }
ed '{"action":"coreui_Task","method":"create","data":[{"id":"","enabled":true,"name":"Delete old snapshots","typeId":"repository.maven.remove-snapshots","alertEmail":"","notificationCondition":"FAILURE","schedule":"daily","startDate":"'$(date -u +%Y-%m-%d)'T00:00:00.000Z","recurringTime":"02:00","timeZoneOffset":"-05:00","properties":{"repositoryName":"corp-snapshots","minimumRetained":"1","snapshotRetentionDays":"0","gracePeriod":"","removeIfReleased":"false"}}],"type":"rpc","tid":1}' | cut -c1-200
echo "-- task made, not run"; sh $L check | tail -7
T=$(curl -s -u admin:$P http://127.0.0.1:8081/service/rest/v1/tasks | python3 -c "import sys,json;print([t['id'] for t in json.load(sys.stdin)['items'] if t['type']=='repository.maven.remove-snapshots'][0])")
curl -s -u admin:$P -X POST http://127.0.0.1:8081/service/rest/v1/tasks/$T/run -o /dev/null; sleep 12
printf 'keep: 1 snapshot, the newest, because nobody builds on an old snapshot\nwhen: daily at 02:00 with retention 0 so it runs at a quiet hour\n' > /opt/lab93/notes.txt; chown student /opt/lab93/notes.txt
echo "-- solved"; sh $L check | tail -7
sh $L down; ls /opt/lab93 2>&1 | head -1; id nexus93 2>&1 | head -1
echo TESTDONE
