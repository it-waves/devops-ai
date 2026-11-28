# MC21 CI/CD Engineering: plan (decided 2026-11-27, autonomous)

Why MC21 before MC20: GitHub asset hosts are still blocked for the workspace browser (see MC20_PLAN.md status), so the real Actions UI cannot be recorded sharply. MC21 is tool-agnostic and runs fully on real local tools already built (Jenkins lab, real Nexus CE, Maven, Tomcat). MC20 resumes when the hosts open; its draft narration is in /home/claude/academy/mc20_draft/. Lesson numbers follow production order, so MC21 takes L177-L180; MC20 will take the next numbers.

Same rules as MC19: 12-20 min lessons, one continuous story with one live recording, simple to advanced, Maven only, free/real tools, last lesson is mastery with lab script up/check/down, results, cleanup, lab info on screen.

| Lesson | Objectives | Story |
|---|---|---|
| L177 | O01 end-to-end pipeline; O02 stages | "Commit to production, one picture": design the CloudCart pipeline on a board, then build it in real Jenkins as separate stages (build, test, scan, package, publish to Nexus, deploy, verify), watch each stage go green |
| L178 | O03 immutable versioned artifacts and promotion; O04 quality, security, approval gates | "Build once, promote many": one versioned jar in Nexus, promoted dev to stage to prod without rebuilding; gates: failing test, quality threshold, dependency scan, manual approval input |
| L179 | O05 secrets and least privilege; O06 rolling, blue-green, canary, rollback; O07 smoke tests, verification, notifications | "Deploy without fear": credentials binding, blue-green on two Tomcat instances with a switch, smoke test that fails and triggers rollback, notification |
| L180 | O08 reliability and troubleshooting; O09 deliver CloudCart pipeline (mastery) | "Prove the pipeline": measure success rate and duration, break/fix four failures, lab180.sh up/check/down with independent checks, results, cleanup, lab info on screen |

Status: planned. Next: inspect Jenkins lab state (/home/claude/jenkins-lab, Jenkinsfile172 is the latest) and write L177 body/scenes/steps.
