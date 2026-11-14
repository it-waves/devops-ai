# Real resources plan (owner request 2026-11-14: "use real resources in demos")
Hosts now allowed in sandbox: repo1.maven.org, repo.maven.apache.org, download.sonatype.com, *.docker.io, *.docker.com (Docker Hub reachable).
## Real Nexus (verified working in sandbox)
- Tarball: https://download.sonatype.com/nexus/3/nexus-3.98.1-01-linux-x86_64.tar.gz (525 MB, JDK bundled). Extracted at /tmp/nx/nexus-3.98.1-01 ; data /tmp/nx/sonatype-work/nexus3 ; run as user `nexus` (not root): `cd bin && ./nexus run`; ~60-90 s to start.
- sonatype-work/nexus3/etc/nexus.properties: application-port=8081, nexus.security.randompassword=false (admin/admin123), nexus.onboarding.enabled=false. nexus.vmoptions heap 1200m.
- Community Edition EULA must be accepted (owner authorized for demo recordings; students accept it themselves in their lab). Accepted via REST POST /service/rest/v1/system/eula (disclaimer text + accepted:true).
- Default repos: maven-releases, maven-snapshots (hosted), maven-central (proxy), maven-public (group).
- REAL behavior differs from stand-in: redeploy to a release repo with Disable redeploy returns HTTP 400 "Repository does not allow updating assets" (NOT 409). Lesson text and lab must use this. No Events page: ui.txt task becomes "write the SHA-1 of the release jar shown in Browse > asset > Summary".
## Work list
1. L91 redo with real Nexus UI (continuous recording: login, Create repository maven2 hosted corp-snapshots / corp-releases, mvn deploy, Browse, redeploy refusal), lab91 downloads+starts Nexus.
2. L92 build on real Maven Central (no offline mirror), faults offline/checksum/auth(401 from real Nexus)/tests.
3. Later: Docker lessons use real Docker Hub.
