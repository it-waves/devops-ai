L="env SUDO_USER=student sh /usr/local/sbin/lab100.sh"
$L down >/dev/null; LAB100_GRADLE_ZIP_URL=file:///opt/dist/gradle-8.14.3-bin.zip $L up >/dev/null 2>&1; cd /opt/lab100/cartcore; Y=.github/workflows/ci.yml
echo "base: $($L check 2>&1 | tail -1)"
sed -i 's/^    branches: \[main\]/    branches: [main]\n  pull_request:/' $Y; echo "trigger: $($L check 2>&1 | tail -1)"
sed -i "s/java-version: '8'/java-version: '21'/" $Y; echo "java: $($L check 2>&1 | tail -1)"
sed -i 's#^      - run: ./gradlew build#      - uses: gradle/actions/setup-gradle@v4\n      - run: ./gradlew build#' $Y; echo "gradle: $($L check 2>&1 | tail -1)"
sed -i 's#Pa55-plain#${{ secrets.REPO_PASSWORD }}#' $Y; echo "secret: $($L check 2>&1 | tail -1)"
printf '      - uses: actions/upload-artifact@v4\n        with:\n          name: cartcore-jar\n          path: build/libs/*.jar\n' >> $Y; cat $Y | head -30; echo "final: $($L check 2>&1 | tail -6)"; cd /; $L down; ls /opt/lab100 2>&1 | head -1
