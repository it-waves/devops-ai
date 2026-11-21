# source this file, then: lab check | scan
lab() { sh "$(dirname "${BASH_SOURCE[0]:-$0}")/lab166.sh" "$@"; }
scan() { mvn -B verify org.sonarsource.scanner.maven:sonar-maven-plugin:sonar -Dsonar.projectKey="${SONAR_KEY:-cloudcart}" -Dsonar.host.url="${SONAR_URL:-http://localhost:9000}" "$@"; }
