# builds the clean Nexus state for the Lesson 93 recording: admin password, EULA, anonymous off, repo corp-snapshots, wizard finished
P=Corp-7q4m2-Nexus1; U=http://localhost:8081
sh /tmp/nx/reset.sh
A=$(cat /tmp/nx/sonatype-work/nexus3/admin.password)
curl -s -o /dev/null -u admin:$A -X PUT -H 'Content-Type: text/plain' -d "$P" $U/service/rest/v1/security/users/admin/change-password
curl -s -u admin:$P $U/service/rest/v1/system/eula > /tmp/eula.json
python3 -c "import json;d=json.load(open('/tmp/eula.json'));d['accepted']=True;json.dump(d,open('/tmp/eula.json','w'))"
curl -s -o /dev/null -u admin:$P -H 'Content-Type: application/json' -X POST -d @/tmp/eula.json $U/service/rest/v1/system/eula
curl -s -o /dev/null -u admin:$P -H 'Content-Type: application/json' -X PUT -d '{"enabled":false,"userId":"anonymous","realmName":"NexusAuthorizingRealm"}' $U/service/rest/v1/security/anonymous
curl -s -o /dev/null -u admin:$P -H 'Content-Type: application/json' -X POST -d '{"name":"corp-snapshots","online":true,"storage":{"blobStoreName":"default","strictContentTypeValidation":true,"writePolicy":"ALLOW"},"maven":{"versionPolicy":"SNAPSHOT","layoutPolicy":"STRICT","contentDisposition":"INLINE"}}' $U/service/rest/v1/repositories/maven/hosted
echo prepped
