# Lesson 179 short names. Load with:  source shortcuts179.sh
# Set these first (your lab values): JENKINS_AUTH=user:password  NEXUS_USER  NEXUS_PASSWORD
#   CATALINA_HOME=your Tomcat install   DEV_BASE=your dev Tomcat folder (CATALINA_BASE)
lab() { sh "$(dirname "${BASH_SOURCE[0]:-$0}")/lab179.sh" "$@"; }
nx() { curl -s -u "$NEXUS_USER:$NEXUS_PASSWORD" "$@"; }
versions() { nx 'http://localhost:8081/service/rest/v1/search?repository=cloudcart-releases&name=cloudcart' | sed -n 's/.*"version" *: *"\([^"]*\)".*/\1/p' | sort -u | tr '\n' ' '; echo; }
health() { case $1 in dev) P=9101;; stage) P=9102;; blue) P=9103;; green) P=9104;; live) P=9100;; esac; curl -s localhost:$P/cloudcart/health; echo; }
tomcat() { CATALINA_BASE=$DEV_BASE "$CATALINA_HOME/bin/catalina.sh" "$1"; }
