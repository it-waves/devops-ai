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
## Owner notes (2026-11-14)
- Recording must be clear and fully explained.
- Explain the major parts of the Nexus UI to beginners before/while using them: left sidebar (Dashboard, Search, Browse, Upload, Settings gear), Settings > Repository > Repositories list and its columns (Name, Type, Format, Status, URL copy button), repository TYPES (hosted = ours, proxy = cache of Maven Central, group = one address for several), default repos (maven-central proxy, maven-public group, maven-releases/maven-snapshots hosted), Version policy, Deployment policy, Browse tree (group/artifact/version), asset details (path, size, SHA-1, blob created), Copy URL button for settings.xml/pom.
## Verified facts about real Nexus 3.98.1 CE (2026-11-14)
- Do NOT disable onboarding: first run shows the REAL student flow and it is worth recording:
  1. login page shows an info box: first login uses the generated password in sonatype-work/nexus3/admin.password (username admin)
  2. wizard "Let's Get You Set Up" > Get Started > step1 "Set an admin password" (change; session signs out, log in again with the new password, wizard resumes)
  3. step "Welcome to Nexus Repository Community Edition" > Next; step "End User License Agreement" (checkbox I accept) ; step "Configure Anonymous Access" (Enable/Disable; default Disable) ; step "Required base telemetry" (checkbox I understand; community edition goes read-only after 30 days without telemetry) > Finish.
  Owner authorized EULA acceptance for demo instance; the telemetry acknowledgement is the same wizard (disclose to owner).
- Until EULA accepted all uploads return 403. After wizard: PUT 201.
- Demo admin password used: Corp-7q4m2-Nexus1 (throwaway). Reset script: /tmp/nx/reset.sh (wipes data, restarts, ~90 s; writes admin.password).
- Chrome flags for a full clean screen: --no-sandbox --incognito --test-type --disable-infobars --window-size=1080,600 --user-data-dir=/tmp/chr1 ; zoom ctrl+minus x2 (80%). Login URL localhost:8081/#/login ; settings repos list: #admin/repository/repositories ; Create repository button (335,247 at 80% with infobar; ~ (335,191) without) ; recipe list scroll 5 ticks shows maven2 (hosted).
- Create form: Name, Online, Version policy (Release/Snapshot/Mixed), Layout policy, Content Disposition, ... Storage: Blob store, Strict content type validation, Deployment policy (Allow redeploy / Disable redeploy / Allow redeploy only / Deployment policy) further down.
## Standing rule (owner, 2026-11-14): every demo goes from SIMPLE to ADVANCED
Order inside each live demo: orient (tour) > basic action > variation > failure case > advanced (groups, proxy cache, dedicated deployer user/role, automation). Applies to all lessons, labs and mastery scenarios.
