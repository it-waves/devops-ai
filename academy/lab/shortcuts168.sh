# source this file, then: scan | lab check
lab() { sh "$(dirname "${BASH_SOURCE[0]:-$0}")/lab168.sh" "$@"; }
scan() { mvn -B org.jacoco:jacoco-maven-plugin:0.8.12:prepare-agent verify org.jacoco:jacoco-maven-plugin:0.8.12:report org.sonarsource.scanner.maven:sonar-maven-plugin:sonar -Dsonar.projectKey="${SONAR_KEY:-cloudcart}" -Dsonar.host.url="${SONAR_URL:-http://localhost:9000}" "$@"; }
