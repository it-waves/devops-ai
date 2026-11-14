L=/home/claude/devops-ai/academy/lab/lab95.sh
export SUDO_USER=student LAB95_GRADLE_ZIP_URL=file:///opt/dist/gradle-8.14.3-bin.zip
sh $L down >/dev/null; sh $L up 2>&1 | tail -n 2
echo "-- start"; sh $L check | tail -n 7
cd /opt/lab95/cartcore
sed -i "s/^version = .*/version = '1.1'/" build.gradle
printf "\ntasks.register('report') {\n    dependsOn 'build'\n    doLast { println \"report: \${project.name} \${project.version}\" }\n}\n" >> build.gradle
echo "-- mid"; sh $L check | tail -n 7
runuser -u student -- env HOME=/home/student ./gradlew report --dry-run --console=plain 2>&1 | grep -v Picked > ../graph.txt; cat ../graph.txt | head -n 12
printf 'settings: sets the project name and lists the projects in the build\nwrapper: gradlew runs the exact Gradle version the project asks for\ntask: dependsOn makes one task depend on another so it runs first\n' > ../notes.txt; chown student ../graph.txt ../notes.txt
echo "-- solved"; sh $L check | tail -n 7
sh $L down; ls /opt/lab95 2>&1 | head -n 1; ls /home/student/.gradle/wrapper/dists 2>&1 | head -n 3
echo TESTDONE
