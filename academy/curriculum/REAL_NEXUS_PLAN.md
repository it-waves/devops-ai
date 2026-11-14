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
## Standing rule (owner, 2026-11-14): same explanation + illustration quality for ALL demo/practical lessons
Owner praised the explanations and illustrations; keep that level in every demo lesson going forward (DevOps is mostly practical): explain each major screen/command for beginners, add a diagram or illustrated card next to the live recording, keep lessons practical-first.

## Verified facts (lab91 real-Nexus test, 0/5 -> 5/5)
- "Disable redeploy" = REST writePolicy ALLOW_ONCE (DENY = read-only; even the first release deploy fails with 400 "is read-only").
- Real refusal text: `status code: 409 ... cannot be updated as asset already exists and redeploy is not allowed (409)` (NOT 400). Lab check 3 expects 409 + "redeploy is not allowed".
- maven-surefire-plugin 2.22.3 does not exist on Central; use 2.22.2.
- Failed admin logins trigger HTTP 429 throttling: change the password/accept EULA before any authenticated REST call.
- Java in this sandbox needs JAVA_TOOL_OPTIONS (proxy); keep it set, filter the "Picked up" line.
- Start Nexus with setsid nohup ... < /dev/null so pipes (| tail) do not hang; wipe /home/student/.m2 for clean runs.
- Search index lags a few seconds after deploy (sleep 3-5 before search API).

## Real UI coordinates (Chrome incognito, 1080x600, zoom 80%) - L91
- Processes die between turns: restart Xvfb (setsid nohup Xvfb :97 -screen 0 1080x600x24) + /tmp/nx/reset.sh each turn; do recording in one turn.
- Login (no info box): user (540,384); with first-login info box (540,465). Wizard: Get Started (719,531); set password New (540,314), Confirm (540,380), Next (738,531) -> signed out; log in again; Get Started; Welcome Next (738,531); EULA box (338,481), Next (738,531); Anonymous Next (737,531); Telemetry: scroll down 6 clicks at (540,400), box (338,483), Finish (733,531). Telemetry text: read-only after 30 days without telemetry.
- Repositories page: localhost:8081/#admin/repository/repositories ; Create repository (335,191). Recipe list: scroll wheel at (660,400); maven2 (hosted) row around y=312 after [12 down, 7 up, 4 down, 1 up] from top (list is alphabetical; ~4.7 rows/click) -> click (350,312).
- Form (top): Name (652,223) [(652,223) both before/after error]; Version policy select (610,356) after name typed -> options Release(320,377) Snapshot(323,396) Mixed(314,416); defaults Release + Disable redeploy. After 3 wheel clicks: Deployment policy select (610,399): Allow redeploy (345,418), Disable redeploy (345,438), Read-only (345,458). After 12+ wheel clicks: Create repository (339,560).
- Repos list after create: toast "Repository updated: corp-snapshots"; Name column truncated at 80% zoom.

## Owner request (2026-11-14 10:01): Nexus "job" (scheduled task) UI demo
- Create a Nexus job (Settings > System > Tasks: e.g. "Delete unused snapshot", "Admin - Compact blob store", cleanup policy) as a very illustrative, fully visible UI demo; show every screen on the UI.
- Standing rule for ALL UI demos going forward: highest creativity, accuracy, excellence; something never seen before (annotated callouts, zoomed regions, before/after states, live results, clear narration). Queue after L92 (candidate: extra lesson in MC10 or inside the MC10 Mastery lesson).

## Owner instruction (2026-11-14 10:13): keep reusable resources in the sandbox
Do NOT delete resources needed by future lessons (Nexus tarball /tmp/ncache/nexus.tgz, extracted /tmp/nx, ~/.m2 caches, Docker images later, base images, tool downloads). Only remove what a lab's own `down` removes. Reuse when the later lesson (e.g. Nexus job/tasks UI demo, MC10 Mastery, Docker) arrives.
## Owner feedback (2026-11-14 10:03) for all UI/terminal demos
- Cursor/UI element sync: the cursor must be easy to follow (highlight halo + click ripple), move to the element BEFORE it is named/clicked, and each highlight/callout must be in sync with the narration.
- Text must never spill outside its box/card/frame (measure and wrap/shrink; check every card in QA).

## QUALITY GATES (owner 10:23): run BEFORE every recording so nothing is re-recorded
1. `python3 common/preflight.py lessonNN --fix` : typing fits its cue (+0.7 s slack; writes extra.json), cmd order = script order, HL rows match real output rows (wrap at 71 cols), commands wrapping >2 rows flagged. Must print PASSED.
2. Lab: lab test script 0/N -> N/N, down clean (run before recording).
3. Resources warmed in enter.sh (caches primed, only the demo's own downloads cold); reuse /tmp/ncache, /tmp/nx.
4. After recording: contact-sheet review of every clip, then render, QA frames (text inside boxes, highlights on the right row), listen to narration spot checks.
5. UI demos: cursor halo + click ripple, cursor moves before the element is named, callouts synced, no text spill.

## TIME MANAGEMENT (owner 11:09): get it right the first time
Budget per lesson (typical): script+scenes 20 min, lab build+test 15, preflight 2, record 10, render 10, QA 10, metadata+upload+captions 25 = ~90 min. Log start/end time of every stage in LEDGER notes. Run slow jobs (render, lab test, download) in parallel with writing the next step; poll with `until` loops, never fixed sleeps. Do every check BEFORE the slow step (preflight, text-fit, badge widths, lab test) so no stage repeats. Lessons learned L92: badge text clipped (check width of every label), EXTRA timing (preflight gate), lab clutter (hide helper dirs), line numbers in narration (verify against real output).
