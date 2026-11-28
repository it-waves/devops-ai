# MC21 CI/CD Engineering: plan (decided 2026-11-27, autonomous)

Why MC21 before MC20: GitHub asset hosts are still blocked for the workspace browser (see MC20_PLAN.md status), so the real Actions UI cannot be recorded sharply. MC21 is tool-agnostic and runs fully on real local tools already built (Jenkins lab, real Nexus CE, Maven, Tomcat). MC20 resumes when the hosts open; its draft narration is in /home/claude/academy/mc20_draft/. Lesson numbers follow production order, so MC21 takes L177-L180; MC20 will take the next numbers.

Same rules as MC19: 12-20 min lessons, one continuous story with one live recording, simple to advanced, Maven only, free/real tools, last lesson is mastery with lab script up/check/down, results, cleanup, lab info on screen.

| Lesson | Objectives | Story |
|---|---|---|
| L177 | O01 end-to-end pipeline; O02 stages; O03 immutable versioned artifacts and promotion | "Commit to production, built once": design the CloudCart pipeline on a board, build it in real Jenkins as separate stages (build, test, package, publish to Nexus, deploy, verify), then promote the same versioned artifact dev to stage to prod without rebuilding and prove the checksums match |
| L178 | O04 gates; O05 secrets, least privilege; O06 rolling, blue-green, canary, rollback; O07 smoke tests, verification, notifications | "Deploy without fear": failing test and quality gate stop the line, manual approval, credentials binding with a scoped identity, blue-green switch, a smoke test that fails and rolls back, notification |
| L179 | O08 reliability and troubleshooting; O09 deliver CloudCart pipeline (mastery) | "Prove the pipeline": measure success rate and duration, break/fix failures from the first error, lab179.sh up/check/down with independent checks, results, cleanup, lab info on screen |

Restructured 2026-11-27 on the owner's reminder that every domain may be restructured strategically: three comprehensive lessons instead of four. MC21 takes L177-L179.

Status: planned. Next: inspect Jenkins lab state (/home/claude/jenkins-lab, Jenkinsfile172 is the latest) and write L177 body/scenes/steps.

## L177 build notes (2026-11-27, verified working)
- Lab assets in /home/claude/jenkins-lab: tc177.sh (3 Tomcat instances via CATALINA_BASE tc177/{dev,stage,prod}, ports 9101/9102/9103; Tomcat 10.1.34 at /tmp/cct, needs chmod -R a+rX), repo177 (CloudCart 1.0.0 pom with distributionManagement -> cloudcart-releases, settings-ci.xml with env creds, Jenkinsfile, Jenkinsfile.promote, scripts/deploy.sh), mkjobs177.sh (Jenkins credential nexus-deployer + jobs cloudcart-ci and cloudcart-promote with VERSION/TARGET parameters). Copies in devops-ai/academy/lab/lab177/.
- Verified: cloudcart-ci build #1 = Version (versions:set 1.0.$BUILD_NUMBER) -> Build and test (32 tests) -> Publish to Nexus (deployer creds) -> Deploy to dev (download from Nexus, sha1 check, copy war, poll /cloudcart/health for the version). Then cloudcart-promote VERSION=1.0.1 TARGET=stage and prod: no rebuild, same checksum, health reports 1.0.1 on all three.
- Needs running: Jenkins :8080 (run154.sh), Nexus :8081 (start line from reset173.sh without wiping), Tomcats (tc177.sh).
- Next: reset177 (wipe published 1.0.x from Nexus, empty webapps, jobs fresh), body.py/scenes.py/steps.py, record. App health URL: /cloudcart/health returns {"status","version","shop"}.
