#!/bin/sh
# creates credential nexus-deployer and jobs cloudcart-ci and cloudcart-promote in Jenkins
D=$(grep '^NEXUS_DEPLOYER_PASSWORD=' /home/claude/academy/lesson176/pw.env | cut -d= -f2)
J=localhost:8080; JA="-u admin:devops-lab"
curl -s $JA -c /tmp/cj178 $J/crumbIssuer/api/json -o /tmp/crumb178.json; C=$(python3 -c "import json;d=json.load(open('/tmp/crumb178.json'));print(d['crumbRequestField']+':'+d['crumb'])")
for j in cloudcart-ci cloudcart-promote; do curl -s $JA -b /tmp/cj178 -H "$C" -X POST $J/job/$j/doDelete -o /dev/null; done
cat > /tmp/cred178.groovy <<G
import com.cloudbees.plugins.credentials.*; import com.cloudbees.plugins.credentials.domains.*; import com.cloudbees.plugins.credentials.impl.*
def s=SystemCredentialsProvider.getInstance().getStore()
def old=s.getCredentials(Domain.global()).find{it.id=='nexus-deployer'}; if(old) s.removeCredentials(Domain.global(), old)
s.addCredentials(Domain.global(), new UsernamePasswordCredentialsImpl(CredentialsScope.GLOBAL,'nexus-deployer','Nexus deployer for CloudCart','cart-deployer','$D'))
println 'ok'
G
curl -s $JA -b /tmp/cj178 -H "$C" --data-urlencode "script@/tmp/cred178.groovy" $J/scriptText; echo
mk(){ cat > /tmp/job178.xml <<X
<?xml version='1.1' encoding='UTF-8'?>
<flow-definition plugin="workflow-job"><description>$2</description><keepDependencies>false</keepDependencies><properties>$4</properties>
<definition class="org.jenkinsci.plugins.workflow.cps.CpsScmFlowDefinition" plugin="workflow-cps"><scm class="hudson.plugins.git.GitSCM" plugin="git"><configVersion>2</configVersion><userRemoteConfigs><hudson.plugins.git.UserRemoteConfig><url>/home/claude/jenkins-lab/repo178</url></hudson.plugins.git.UserRemoteConfig></userRemoteConfigs><branches><hudson.plugins.git.BranchSpec><name>*/main</name></hudson.plugins.git.BranchSpec></branches><doGenerateSubmoduleConfigurations>false</doGenerateSubmoduleConfigurations><submoduleCfg class="empty-list"/><extensions/></scm><scriptPath>$3</scriptPath><lightweight>true</lightweight></definition><triggers/><disabled>false</disabled></flow-definition>
X
 curl -s $JA -b /tmp/cj178 -H "$C" -H 'Content-Type: application/xml' -X POST "$J/createItem?name=$1" --data-binary @/tmp/job178.xml -o /dev/null -w "$1 %{http_code}\n"; }
mk cloudcart-ci 'CloudCart CI: version, build and test, publish to Nexus, deploy to dev' Jenkinsfile ''
mk cloudcart-promote 'CloudCart promotion: take a version that is already in Nexus to stage or prod, no rebuild' Jenkinsfile.promote '<hudson.model.ParametersDefinitionProperty><parameterDefinitions><hudson.model.StringParameterDefinition><name>VERSION</name><defaultValue></defaultValue></hudson.model.StringParameterDefinition><hudson.model.ChoiceParameterDefinition><name>TARGET</name><choices class="java.util.Arrays$ArrayList"><a class="string-array"><string>stage</string><string>prod</string></a></choices></hudson.model.ChoiceParameterDefinition></parameterDefinitions></hudson.model.ParametersDefinitionProperty>'
