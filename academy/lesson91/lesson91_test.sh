rm -rf /home/student/.m2
L=/home/claude/devops-ai/academy/lab/lab91.sh
export SUDO_USER=student
P='Corp-7q4m2-Nexus1'
sh $L down >/dev/null; sh $L up > /tmp/up91.out 2>&1; tail -4 /tmp/up91.out
export NEXUS_PASS=$P
A=$(cat /opt/lab91/sonatype-work/nexus3/admin.password)
curl -s -o /dev/null -w "pw %{http_code}\n" -u admin:$A -X PUT -H 'Content-Type: text/plain' -d "$P" http://localhost:8081/service/rest/v1/security/users/admin/change-password
curl -s -u admin:$P http://localhost:8081/service/rest/v1/system/eula > /tmp/e.json; python3 -c "import json;d=json.load(open('/tmp/e.json'));d['accepted']=True;json.dump(d,open('/tmp/e2.json','w'))"
curl -s -o /dev/null -w "eula %{http_code}\n" -u admin:$P -H 'Content-Type: application/json' -X POST -d @/tmp/e2.json http://localhost:8081/service/rest/v1/system/eula
echo "-- start"; sh $L check | tail -7
mk() { curl -s -o /dev/null -w "repo $1 %{http_code}\n" -u admin:$P -H 'Content-Type: application/json' -X POST http://localhost:8081/service/rest/v1/repositories/maven/hosted -d "{\"name\":\"$1\",\"online\":true,\"storage\":{\"blobStoreName\":\"default\",\"strictContentTypeValidation\":true,\"writePolicy\":\"$3\"},\"maven\":{\"versionPolicy\":\"$2\",\"layoutPolicy\":\"STRICT\",\"contentDisposition\":\"ATTACHMENT\"}}"; }
mk corp-snapshots SNAPSHOT ALLOW; mk corp-releases RELEASE ALLOW_ONCE
cd /opt/lab91/shop
d() { runuser -u student -- env NEXUS_PASS=$P HOME=/home/student mvn -B -q -s settings.xml deploy 2>&1 | grep -v "^Picked up"; }
d | tail -3; d | tail -3
sed -i 's/-SNAPSHOT//' pom.xml; d | tail -3
echo "== again"; d 2>&1 | grep -o 'status code.*' | tee conflict.txt
sleep 3
SHA=$(curl -s -u admin:$P "http://localhost:8081/service/rest/v1/search/assets?repository=corp-releases&maven.artifactId=cart-core&maven.extension=jar&maven.baseVersion=1.0.0" | python3 -c "import json,sys;print(json.load(sys.stdin)['items'][0]['checksum']['sha1'])"); echo "$SHA" > sha1.txt
sed -i 's#<version>1.0.0</version>#<version>1.0.1</version>#' pom.xml; grep -m1 '<version>' pom.xml; d | tail -3
sleep 5; echo 'A release is immutable, never overwrite it.' > why.txt; chown student *.txt
echo "-- solved"; sh $L check | tail -7
sh $L down; ls /opt/lab91 2>&1 | head -1; id nexus91 2>&1 | head -1
