# MC17 Jenkins: plan (decided 2026-11-18)

Owner directive: switch to a clean, full, well-explained UI whenever Jenkins needs it; highest level of innovation, creativity and smart design.

Decision: Jenkins NEEDS a real lab AND real UI. Use REAL Jenkins LTS (not a stand-in), like the real Nexus CE domain. Every UI lesson is a continuous live screen recording (visible clicks, narrated, cursor highlighted and in sync), the major UI parts are explained first (beginners), demos go simple to advanced, free resources only. Terminal and Maven for builds (Maven, not Gradle). Mastery lesson: independently verifiable scenario with results, troubleshooting, cleanup; show lab info on screen.

External blocker: sandbox cannot reach get.jenkins.io, updates.jenkins.io, mirrors.jenkins.io, repo.jenkins-ci.org (needed for the war and plugins). Needs the owner to allow these hosts (as was done for Nexus).

| Lesson | Objective | UI? | Plan |
|---|---|---|---|
| L154 | O01 controller, agents, executors, plugins, pipeline lifecycle | UI tour | Animated architecture + live tour of the real dashboard: Manage Jenkins, Nodes, Plugins, Build Executor Status; name each UI region |
| L155 | O02 install safely, initial administration | FULL UI | Real install from the war, unlock with initial admin password, plugin choice, first admin, URL, security (no anonymous), users/roles |
| L156 | O03 Jenkinsfile: stages, steps, agents, post | UI + terminal | Write Jenkinsfile in vim; create Pipeline job in UI; Stage View, Console Output, Blue-style views; post always/success/failure |
| L157 | O04 build and test CloudCart with Maven | UI + terminal | Maven tool config, build CloudCart, test reports and JUnit trends in the UI |
| L158 | O05 credentials and env vars securely | FULL UI | Credentials store/domains, withCredentials, masking, env vars; show a leak, then fix |
| L159 | O06 triggers, SonarQube gate, Nexus publish | FULL UI | SCM polling/webhook, Sonar quality gate wait, publish to real Nexus CE |
| L160 | O07 distributed agents, workspace/artifacts | FULL UI | Add an agent node, labels, executors, archiveArtifacts, stash/unstash |
| L161 | O08 approval, promotion, rollback, notifications | FULL UI | input step approval, promote stages, rollback job, notification |
| L162 | O09 backup, upgrade, troubleshoot | UI + terminal | Backup JENKINS_HOME, upgrade, offline agent, failed build triage |
| L163 | MC17 mastery evidence | UI + terminal | Independently verifiable scenario + check script; cleanup; show lab info on screen |

Honest-notes reminders: real recordings labelled, illustrations labelled, no Claude/AI marks in frames, thumbnails bold and not busy, like/share/subscribe at the end, Mastery evidence at the end of the domain.
