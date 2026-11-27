# MC19 Nexus Repository: plan (decided 2026-11-27, restructured with the owner)

Owner decision (2026-11-27): few but very comprehensive lessons per domain, 12 to 20 minutes each, minimal repetition, still highest creativity, innovation and excellence. Each lesson is ONE continuous story with one live recording that goes simple to advanced; chapters carry the objective IDs so the checklist mapping stays clear. No recap loops, no rebuilding the same setup in two lessons: state carries forward. Published lessons stay as they are. Applies to MC19 onward.

Real Nexus Repository Community Edition 3.98.1 (extracted at /tmp/nx, REAL_NEXUS_PLAN.md has the verified UI facts, 409 refusal text, throttling). Maven only, free resources only, same narrator. Spoken name: "Nexus".

| Lesson | Objectives | Story and live recording |
|---|---|---|
| L173 | O01 hosted, proxy, group; O02 install and secure | "The build that downloads the internet": start a fresh Nexus as a non-root user, tour the UI, secure it (admin password, anonymous off, proven by a 401), then the three repository types by doing: resolve one artifact through the group, watch the proxy cache fill (slow first, instant second), hosted holds our own |
| L174 | O03 snapshot and release repos; O04 publish and retrieve; O05 Maven settings and CI credentials | "Ship cart-core": create snapshot and release repos, a dedicated deployer user and role, settings.xml servers and mirror, mvn deploy snapshot then release, Browse and retrieve by coordinates and curl, credentials in Jenkins and never in the pom |
| L175 | O06 immutability, retention, provenance; O07 permissions, backups, storage monitoring | "Make it trustworthy": disable redeploy and watch the 409, cleanup policy and task, checksums and provenance, least-privilege roles, backup task, blob store and health monitoring |
| L176 | O08 troubleshoot; mastery | "Break it, fix it, prove it": four real failures (401, 403, missing artifact or stale metadata, repository offline) read from the first error, then the mastery scenario with lab176.sh up/check/down, results, cleanup, lab info on screen |

Next domain after MC19: MC20 GitHub Actions. CloudCart v1 lands after MC19 (CLOUDCART_ROADMAP.md).

## L174 build notes (in progress)
- Dev assets: /home/claude/jenkins-lab/cart-core (pom with distributionManagement, JUnit test), reset174.sh (fresh Nexus + wizard done via wiz174.py).
- Verified flow: repos cloudcart-snapshots (Snapshot, allow redeploy) and cloudcart-releases (Release, disable redeploy); role cart-deployer (repo view privileges on both + maven-public read/browse); user cart-deployer; settings.xml servers ids must equal distributionManagement ids, mirror of * to maven-public; `mvn deploy` uploads timestamped snapshot to cloudcart-snapshots (plugins fetched through the mirror).
- Live plan: UI create 2 repos, role, user; terminal: cat pom/settings, mvn deploy (grep summary) twice, UI browse, version -> 1.0.0 release deploy, curl retrieve by path and search API, CI variant with env vars (no secrets in pom).
- Create forms are at #preview/admin/repository/repositories (Create Repository), #preview/admin/security/roles, #preview/admin/security/users.
- UI map (Nexus One UI, 1920x1080): repo create wizard at #preview/admin/repository/repositories/create: Select Format (click Maven card; use get_by_text(...).locator('visible=true')) -> Select Type (Proxy/Hosted/Group cards) -> Configure form (#settings-input-name, select name maven-versionPolicy RELEASE/SNAPSHOT, storage-writePolicy ALLOW_ONCE default / ALLOW, button Create Repository). Role create #preview/admin/security/roles/create (#settings-input-id, -name, textarea description, "Edit Privileges" opens a Privileges Selection dialog with a Filter box, checkboxes, Confirm). User create #preview/admin/security/users/create (#settings-input-userId, firstName, lastName, emailAddress, password, passwordConfirm, Roles transfer list Available/Granted).
- Wizard completion for dev: /home/claude/jenkins-lab/wiz174.py; reset174.sh = reset173 + wizard.
- Role flow verified in UI: Edit Privileges -> Filter 'view-maven2-cloudcart' -> tick rows cloudcart-releases-* and cloudcart-snapshots-* (all actions, scoped to two repos); Filter 'view-maven2-maven-public' -> tick maven-public-read and -browse; Confirm (4 selected); Create. User form: Roles transfer list: click role name then 'Move selected to right' arrow; Create. User page shows Privileges / Security Tree preview.
- lesson174 scaffold copied from lesson173 (head/record/jhome etc. sed 173->174); body.py, scenes.py, steps.py still L173 content and must be rewritten.

## L175 notes (Make it trustworthy, O06-O07)
- Narrow the deployer: add/edit/read only (no delete) with a 403 proof on delete.
- Add cloudcart repos to the maven-public group so a consumer resolves cart-core.
- Cleanup policies, provenance, backups.
