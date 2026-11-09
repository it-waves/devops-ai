# DevOps Simplified HQ: Academy Architecture and Production Blueprint
## Volume 1 of 3: Mission, Capabilities, Architecture, Catalog Map, Dependency Graph, Ledger

Status: PLANNED/DESIGNED. Nothing in this volume is a produced lesson. Items marked UNVERIFIED have not been checked against live sources.

### Completion checklist (directive Part 19, 20 items)
| # | Item | Volume |
|---|------|--------|
| 1 | Mission and differentiation | 1 |
| 2 | Competitor benchmark | 1 (framework only; evidence pending) |
| 3 | Curriculum architecture | 1 |
| 4 | All 48 Masterclasses | 1 |
| 5 | Dependency graph | 1 |
| 6 | Learning routes | 1 |
| 7 | Five project summaries per Masterclass | 2 |
| 8 | CloudCart architecture | 2 |
| 9 | Traditional-to-modern delivery architecture | 2 |
| 10 | Lab platform design | 2 |
| 11 | Version and compatibility strategy | 2 |
| 12 | Assessment framework | 3 |
| 13 | Cinematic production standards | 3 |
| 14 | Quality gates | 3 |
| 15 | Resource and cost estimates | 3 |
| 16 | Production workflow | 3 |
| 17 | Risk register | 3 |
| 18 | Detailed SDLC Masterclass plan | 3 |
| 19 | Deliverable ledger | 1 (initial) |
| 20 | Next executable milestone | 1 |

---

## 1. Mission and differentiation
Goal: a beginner-to-job-ready DevOps academy where every claim of skill is backed by a checker that passes, not by watching.

Differentiators we can actually deliver (each is already proven on the RHCSA series):
1. **Checkable practice.** Every lesson ends with a read-only `check.sh` that PASSes or FAILs on the learner's machine, and the same lab runs in CI so we know the lesson works.
2. **Real captured output.** Terminal output in videos comes from a real run (CI lab), never typed by hand. Setup done silently is disclosed.
3. **Exact-objective structure.** One video per objective, with an on-screen explanation of every first-use command.
4. **Kit per video.** README with honest limits, practice, solution, command reference, captions, checker.
5. **Honest labelling.** Illustrations are labelled "ILLUSTRATION"; Rocky is labelled "RHEL-compatible, NOT RHEL".

## 2. Capabilities and constraints (what is real today)
| Directive wants | Reality today | Plan |
|---|---|---|
| Real terminal recordings | Real command output from GitHub Actions lab runs, rendered into terminal scenes (not screen recordings) | Keep; label as "captured from a real run". For GUI tools (Jenkins, SonarQube, AWS console) a headless-browser or screen capture is needed: UNVERIFIED feasibility |
| Human-quality voice | Kokoro af_heart (synthetic, female) | Directive prefers a male voice. Decision needed: keep one consistent voice across the channel, or switch for new courses (see Decisions) |
| Photorealistic 3D, on-screen human | Not available in this environment | Replace with clean diagram and flow animations. Do not promise photorealism |
| Cloud labs (AWS, Azure) | No cloud account or credits here | Use local/free-tier equivalents; mark cloud masterclasses UNVERIFIED until run with the user's account |
| Publishing | Works through the user's Chrome and Studio | Keep |
| Autonomous background execution | Only while a session is running or a scheduled task exists | No claim of unattended running unless a scheduled task is created |

## 3. Curriculum architecture
Academy → Stages A–I → 48 Masterclasses → 5 Levels → Lessons (one objective or one idea per video, 4–6 min) → Projects → Assessments. Each Masterclass gets a playlist, kit folder `docs/<mc>/`, and CI labs `labs/<mc>-*/`.

Already built: the RHCSA EX200 course (62 videos). It maps to Masterclass 04 (Linux Administration) as an exam-aligned track. Other published courses (Git, Docker, Nginx, Ansible, Prometheus, PostgreSQL, CI/CD, Linux) are legacy playlists; they need an audit against the new standard before being counted as Level 1 of their Masterclass (Gate A review, not yet done).

## 4. The 48 Masterclasses by stage (full descriptions are in the directive; this is the working map)
- **A Foundations:** 01 SDLC · 02 IT and computer fundamentals · 03 Networking · 04 Linux (RHCSA done) · 05 Bash · 06 Python · 07 Git and GitHub
- **B Applications:** 08 App architecture and APIs · 09 Java · 10 Maven · 11 Gradle · 12 Tomcat · 13 Web servers and proxies · 14 Databases · 15 Testing and QA
- **C CI/CD:** 16 DevOps fundamentals · 17 Jenkins · 18 SonarQube · 19 Nexus · 20 GitHub Actions · 21 CI/CD engineering
- **D Containers:** 22 Docker · 23 Compose · 24 Registries and supply chain
- **E Cloud:** 25 Cloud fundamentals · 26 AWS · 27 Azure · 28 Cloud networking and security
- **F Automation:** 29 Terraform · 30 Ansible · 31 Secrets and config
- **G Kubernetes:** 32 Kubernetes · 33 Helm · 34 EKS · 35 AKS · 36 Argo CD/GitOps · 37 Platform engineering
- **H Reliability:** 38 DevSecOps · 39 Prometheus · 40 Grafana · 41 OpenTelemetry · 42 SRE · 43 Production troubleshooting · 44 DR/BC · 45 FinOps
- **I Graduation:** 46 Enterprise architecture · 47 Career practice · 48 Capstone

## 5. Competency dependency graph (prerequisite edges)
```
01 → 16
02 → 04 → 05 → 06
03 → 04, 13, 25, 28
04 → 05, 12, 13, 17, 22, 30
05 → 17, 20, 30
06 → 26, 27, 29, 41
07 → 17, 20, 21, 36
08 → 09, 14, 15
09 → 10 → 11, 12, 17, 18, 19
10 → 18, 19
12, 13 → 21
14 → 43, 44
15 → 18, 21
16 → 17, 20, 21, 42
17 + 18 + 19 → 21
22 → 23, 24, 32
24 → 38
25 → 26, 27, 28
26/27 → 29, 34/35
28 → 38
29 → 31, 34, 35, 46
30 → 31
32 → 33, 34, 35, 36, 37, 38
39 → 40, 41, 42
38, 42 → 43 → 44 → 45
all of A–H → 46 → 47 → 48
```

## 6. Learning routes
| Audience | Route | Skips (with placement check) |
|---|---|---|
| Absolute beginner | 01, 02, 03, 04, 05, 07, 06, 08… in numeric order | none |
| Experienced IT admin | 01, 16, 07, 05, 06, 22, 29, 30, 32, 39 | 02, 03, 04 after a placement check |
| Developer to DevOps | 04 (core), 05, 16, 17, 20, 22, 29, 32, 38 | 08, 09, 10, 15 |
| Cloud engineer to DevOps | 04, 05, 07, 17, 20, 22, 30, 32, 38, 39 | 25–28 |
| Experienced DevOps | 38, 41, 42, 43, 44, 46, 48 | placement via Level 5 challenges |
Every skip requires passing that Masterclass's Level 5 challenge or a placement check.

## 7. Initial ledger (state machine: PLANNED → RESEARCHED → DESIGNED → IMPLEMENTED → TESTED → EDU-REVIEWED → VIDEO → QA-APPROVED → PUBLISHED)
| ID | Deliverable | State | Evidence |
|---|---|---|---|
| MC04-RHCSA | 62 videos + kits + CI labs | PUBLISHED | `rhcsa-lab-ok` repo, YouTube playlist; captions V35–V62 and some thumbnails pending upload by user |
| MC01-SDLC | SDLC Masterclass | PLANNED | this blueprint |
| Legacy courses | Git, Docker, Nginx, Ansible, Prometheus, PostgreSQL, CI/CD, Linux, Network+ | PUBLISHED (legacy standard) | need Gate A audit |
| Learner comprehension testing | all | PENDING | no representative learners available |

## 8. Decisions needed from you (so I do not guess)
1. **Voice:** keep Kokoro af_heart across the channel, or use a different voice for new courses?
2. **Order:** the directive starts at Masterclass 01 (SDLC). Alternatively continue by tool (Bash, Git audit, Docker…). Default if you do not say: follow the directive, 01 first.
3. **Visuals:** no photorealistic 3D here. Confirm clean animated diagrams plus real captured output is acceptable.
4. **Cloud:** can you provide an AWS or Azure free-tier account later, or should cloud Masterclasses be marked UNVERIFIED?

## 9. Next executable milestone
**M1: Volume 2** (project summaries for all 48, CloudCart spec, delivery-generation diagram, lab platform design, version matrix). Then **M2:** CloudCart v0 (Java/Maven WAR, tests) built and verified in CI, which is the first dependency for the Maven, Tomcat and Jenkins Masterclasses. No lesson videos before the SDLC pilot plan (Volume 3) is approved.

Not yet done: competitor benchmark evidence (needs live research of public syllabi; nothing here is claimed about any competitor).
