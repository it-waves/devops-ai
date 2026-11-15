L=/home/claude/devops-ai/academy/lab/lab97.sh
export SUDO_USER=student LAB97_GRADLE_ZIP_URL=file:///opt/dist/gradle-8.14.3-bin.zip
sh $L down >/dev/null; sh $L up 2>&1 | tail -n 3
echo "-- start"; sh $L check | tail -n 7
cd /opt/lab97/cartcore
G="runuser -u student -- env HOME=/home/student ./gradlew --console=plain"
sed -i "s/implementation 'org.junit.jupiter:junit-jupiter:5.10.2'/testImplementation 'org.junit.jupiter:junit-jupiter:5.10.2'/" build.gradle
echo "-- mid1"; sh $L check | tail -n 7
mkdir -p gradle; cat > gradle/libs.versions.toml <<'T'
[versions]
commons-text = "1.10.0"
junit = "5.10.2"

[libraries]
commons-text = { module = "org.apache.commons:commons-text", version.ref = "commons-text" }
junit-jupiter = { module = "org.junit.jupiter:junit-jupiter", version.ref = "junit" }
T
sed -i "s/'org.apache.commons:commons-text:1.10.0'/libs.commons.text/; s/'org.junit.jupiter:junit-jupiter:5.10.2'/libs.junit.jupiter/; s/id 'java'/id 'java'\n    id 'maven-publish'/" build.gradle
cat >> build.gradle <<'T'

publishing {
    publications { maven(MavenPublication) { from components.java } }
    repositories { maven { url = layout.buildDirectory.dir('repo') } }
}
T
chown -R student /opt/lab97
$G publish 2>&1 | grep -v Picked | tail -n 4
cat build.gradle | sed -n 1,20p
echo "-- mid2"; sh $L check | tail -n 7
printf "catalog: /opt/lab97/cartcore/gradle/libs.versions.toml\npublished: /opt/lab97/cartcore/build/repo/com/cloudcart/cartcore/1.2/cartcore-1.2.pom\nscope: junit is only needed to test, so it stays out of the shipped app\n" > ../notes.txt; chown student ../notes.txt
echo "-- solved"; sh $L check | tail -n 7
sh $L down; ls /opt/lab97 2>&1 | head -n 1
echo TESTDONE
