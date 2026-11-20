# MC18 SonarQube: plan (decided 2026-11-20)

Real SonarQube (Community Build 26.11, already used in L159, in /tmp/sq) with the real UI; every UI lesson is a continuous live recording (terminal + Chrome recorder from L162/L163), simple to advanced, Maven only, free resources only, lab info on screen in the mastery lesson. Spoken name: "sonar cube". Dry to calib to ONE live take per lesson.

| Lesson | Objective | UI? | Plan |
|---|---|---|---|
| L164 | O01 static analysis, quality gates, profiles, issue categories | UI tour | Illustrations first; live tour of a real project: Overview, Issues, Measures, Code; name each region; the five issue types |
| L165 | O02 install and connect a compatible lab instance | Terminal + UI | Java version check, unpack, start, first login, change admin password, System info; lab163-style lab165.sh |
| L166 | O03 run analysis for a Java/Maven project | Terminal + UI | sonar-maven-plugin scan of CloudCart, token, project appears, first results |
| L167 | O04 interpret bugs, vulnerabilities, hotspots, duplication, coverage | UI | Seed known defects, read each measure, JaCoCo coverage, fix one and re-scan |
| L168 | O05 quality gate and its limits | UI | Create gate, conditions on new code, fail then pass; limits (new code vs overall, gaming) |
| L169 | O06 scanning and gate in CI | UI + terminal | Jenkins stage with withSonarQubeEnv/waitForQualityGate (builds on L159) |
| L170 | O07 tokens and permissions | UI | User vs analysis token, revoke, project permissions, never in code |
| L171 | O08 diagnose scanner, server and gate failures | UI + terminal | Wrong token, wrong URL, server down, gate error: read the first error |
| L172 | MC18 mastery | UI + terminal | Verifiable scenario + check script (lab172.sh up/check/down), results, troubleshooting, cleanup, lab info on screen |

Next domain after MC18: MC19 Nexus Repository.
