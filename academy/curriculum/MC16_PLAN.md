# MC16 DevOps Fundamentals: plan (owner rules: little CLI, so thorough illustrations plus one small REAL demo per lesson where possible; mastery scenario at the end)

| Lesson | Objective | Title idea | Style / real demo |
|---|---|---|---|
| L145 | O01 | DevOps principles: collaboration, feedback, shared ownership | Illustrated; real demo: a handoff vs shared-ownership incident timeline built from a real git log |
| L146 | O02 | CI vs continuous delivery vs continuous deployment | Illustrated; real demo: the same pipeline file with a manual gate vs auto deploy (local runner) |
| L147 | O03 | IaC, configuration management, automation | Illustrated; real demo: idempotent script run twice, drift detected and fixed |
| L148 | O04 | Build artifacts, environments, release promotion | Illustrated; real demo: one artifact with checksum promoted dev to test to prod |
| L149 | O05 | DevSecOps, SRE, platform engineering | Illustrated (roles and loops); real demo: error budget calculation |
| L150 | O06 | DORA metrics: frequency, lead time, failure rate, recovery | Real demo: compute the four metrics from a real git log and a deploy log |
| L151 | O07 | Find bottlenecks in a traditional delivery workflow | Illustrated value stream map; real demo: timestamps analysis |
| L152 | O08 | Design a practical DevOps improvement plan for CloudCart | Illustrated plan; written plan file checked by a lab |
| L153 | mastery | DevOps fundamentals mastery scenario (lab up/check/down, 0/N to N/N) | live; lab info on screen |

Each lesson: demo, practice task, self-check list (no lab, see policy below), objective ID in description. Honest labels as always. Next domain after MC16: MC17 Jenkins.

## Lab policy (owner decision, 2026-11-18)
MC16 is conceptual: NO lab judge per lesson. Use illustrations plus one small real terminal demo with published demo files (academy/lessonNNN-demo), and a self-check instead of a lab rubric. A domain needs a lab only when students build, run or break something real (Linux, Git, Docker, databases, testing, Jenkins, Terraform...). Decide per domain; the mastery lesson of a conceptual domain is a documented scenario (written plan checked against a rubric), not a lab.
