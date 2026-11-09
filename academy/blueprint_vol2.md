# Academy Blueprint, Volume 2 of 3
Covers checklist items 7 to 11: projects, CloudCart, delivery generations, lab platform, versions. State: DESIGNED (nothing built or tested yet; every cloud lab starts UNVERIFIED).

## 7. Five projects per Masterclass (P1 Beginner, P2 Intermediate, P3 Advanced, P4 Production, P5 Mastery)
Full 21-field specs (directive section 12) are written per Masterclass when it enters production. Summaries:

| MC | P1 | P2 | P3 | P4 | P5 |
|---|---|---|---|---|---|
| 01 SDLC | Requirements doc for CloudCart | Architecture + user stories | Plan sprints, Kanban board | Release plan with test/rollback gates | Audit a flawed project plan |
| 02 IT fundamentals | Inspect hardware/OS of a VM | Processes, memory, storage tour | Build and resize a VM | Capacity report for a server | Diagnose a slow server |
| 03 Networking | Map a small network | Subnet a plan, configure DNS/DHCP | Routing, NAT, firewall rules | TLS + load-balanced site | Find a multi-fault network failure |
| 04 Linux | Users, files, permissions | Services, SSH, storage | LVM, SELinux, firewall | Hardened server baseline | Repair a broken server (RHCSA done) |
| 05 Bash | System info and backup | User/service toolkit | Log analysis and health monitor | Deploy + rollback script | Repair a broken automation set |
| 06 Python | File/JSON tool | REST API client | YAML/log automation with tests | Cloud SDK automation | Debug a failing automation service |
| 07 Git | Versioned app | Branch, merge, PR, conflicts | Release tags and recovery | Protected branches, required checks | Recover a damaged repo |
| 08 App/APIs | Call a REST API | Build CRUD endpoints | Auth + caching | Config, health, versioning | Diagnose API failures |
| 09 Java | Compile/run | Packages, dependencies | Runtime tuning | Production JVM settings | Fix a crashing app |
| 10 Maven | Build a Java app | Dependencies and tests | Profiles, plugins | Publish to Nexus | Fix a failing dependency chain |
| 11 Gradle | Build a Java app | Tasks, tests | Plugins, caching | Multi-module release | Fix a broken build |
| 12 Tomcat | Install, deploy WAR | Config, logging, proxy | Automated deploy/rollback | Secured, monitored env | Recover a failing app |
| 13 Web servers | Serve a site | Virtual hosts, proxy | TLS + load balancing | Caching + hardening | Fix proxy/TLS faults |
| 14 Databases | Create DB, tables | Users, permissions | Migrations, backup/restore | Monitoring + tuning | Recover from failed restore |
| 15 Testing | Unit tests | Integration/API tests | End-to-end + regression | Test gates in CI | Fix a flaky suite |
| 16 DevOps | Map the delivery flow | Automate a build | Add metrics | Delivery metrics review | Redesign a broken process |
| 17 Jenkins | Basic pipeline | Build/test Java | SonarQube + Nexus | Secured multi-stage pipeline | Repair distributed CI |
| 18 SonarQube | Analyze Java | Quality gates | Jenkins integration | Multi-project governance | Fix scanner/gate failures |
| 19 Nexus | Install, Maven repo | Publish/consume | Maven + Jenkins | Secure lifecycle | Fix publish/resolve failures |
| 20 GitHub Actions | First workflow | Build/test matrix | Secrets, OIDC, artifacts | Reusable, protected deploys | Debug failing workflows |
| 21 CI/CD eng. | Linear pipeline | Artifact promotion | Blue-green | Canary + rollback + approvals | Repair a broken release flow |
| 22 Docker | Containerize web app | Multi-container env | Optimize and publish | Secure delivery | Fix a broken multi-service env |
| 23 Compose | Two-service stack | Volumes, networks | Health checks, deps | Config/secrets management | Debug a stack |
| 24 Registry/supply chain | Push/pull images | Scan images | SBOM + signing | Promotion + retention | Investigate a tampered image |
| 25 Cloud basics | Cost/pricing exercise | Region/AZ design | Shared-responsibility audit | Landing zone sketch | Review a flawed design |
| 26 AWS | IAM + S3 | VPC + EC2 | ALB, RDS | Secure multi-tier | Fix IAM/network faults |
| 27 Azure | Entra + RBAC | VNet + VM | App Service, ACR | Secure multi-tier | Fix RBAC/network faults |
| 28 Cloud net/sec | Segment a network | Private connectivity | Encryption, KMS | Zero-trust layout | Find exposure paths |
| 29 Terraform | One resource | Modules | Remote state, envs | Secure prod-style infra | Fix drift/state errors |
| 30 Ansible | Ad-hoc + playbook | Roles, templates | Vault, dynamic inventory | Idempotent fleet config | Repair failing playbooks |
| 31 Secrets/config | Env config | Encrypted secrets | Rotation | Audit + access control | Leak response |
| 32 Kubernetes | Deploy an app | Services, storage, config | RBAC, HPA, security | Resilient observable platform | Multi-fault recovery |
| 33 Helm | Install a chart | Own chart | Dependencies, tests | Release/rollback pipeline | Fix a bad release |
| 34 EKS | Create cluster | Node groups | IAM roles, storage | Autoscale + upgrade | Fix cluster faults |
| 35 AKS | Create cluster | Node pools | Identity, storage | Autoscale + upgrade | Fix cluster faults |
| 36 Argo CD | First GitOps app | Helm/Kustomize | Drift detection | Promotion workflow | Fix sync failures |
| 37 Platform eng. | Golden path | Self-service template | Policy guardrails | Platform reliability | Improve a failing platform |
| 38 DevSecOps | Threat model | SAST/dependency scans | Secrets + IaC scans | Policy as code | Remediate a breach scenario |
| 39 Prometheus | Scrape a target | PromQL | Alert/recording rules | Scale + federation | Fix missing metrics |
| 40 Grafana | First dashboard | Variables, alerts | Provisioned dashboards | Access control | Fix broken dashboards |
| 41 OpenTelemetry | Instrument one service | Collector | Distributed traces | Sampling design | Trace a latency fault |
| 42 SRE | Define SLIs/SLOs | Error budgets | On-call + incidents | Postmortem program | Run an incident |
| 43 Prod troubleshooting | Single-fault incident | Two faults | Cross-tool incident | Timed incident | Unfamiliar incident |
| 44 DR/BC | Backup + restore | RTO/RPO plan | Restore drill | Failover rehearsal | Recover a failed restore |
| 45 FinOps | Cost report | Rightsizing | Autoscale tuning | Budget guardrails | Cut cost without outage |
| 46 Enterprise arch. | Single-env design | Multi-env | Multi-account | Governance + ADRs | Review a flawed architecture |
| 47 Career | README + portfolio | Code review | Mock interview | System-design write-up | Portfolio defense |
| 48 Capstone | Requirements | Architecture | Build + CI/CD | Secure, observable run | Introduced-failure recovery + defense |

## 8. CloudCart (original reference app)
- **v0 (monolith):** Java 17, Maven, WAR on Tomcat. Modules: catalog, cart, orders, auth (session + password hash). PostgreSQL via JDBC, Flyway-style SQL migrations, `/health` and `/ready`, JSON structured logs, config through environment variables, JUnit tests (unit + API).
- **Data model:** users, products, carts, cart_items, orders, order_items.
- **API contract:** `GET /api/products`, `GET /api/products/{id}`, `POST /api/cart/items`, `POST /api/orders`, `GET /api/orders/{id}`; contract file `openapi.yaml` is versioned.
- **Generations:** v0 WAR/Tomcat (G1), v1 adds Jenkins/Sonar/Nexus config (G2), v2 Dockerfile + Compose (G3), v3 Terraform stacks (G4), v4 K8s manifests + Helm chart (G5), v5 metrics/tracing (G6).
- **Governance:** semantic tags (`cloudcart-g1-v1.0.0`), per-Masterclass starter snapshots, a changelog, and a rule that earlier generations are never edited except for logged bug fixes.
- **State:** PLANNED. v0 is built next (M2) and counts only after `mvn verify` and the Tomcat smoke test pass in CI.

## 9. Delivery generations
G1 Git → Maven → WAR → Tomcat · G2 Git → Jenkins → Maven → tests → SonarQube gate → Nexus → Tomcat deploy · G3 CI → image build → registry → Docker run · G4 Terraform → cloud infra → automated deploy · G5 Kubernetes + Helm + Argo CD + security + observability · G6 monitoring → incident → recovery → optimization. Each lesson states why the next generation exists and what it costs; older approaches are not called obsolete.

## 10. Lab platform
- **Runner:** the existing `rhcsa-lab-ok` pattern (GitHub Actions VM, `phase1.sh`/`phase2.sh`, `check.sh`) extends to new repo `academy-labs`, one folder per lab with a manifest (`lab.yaml`: id, tools+versions, cost, verification level, cleanup).
- **Local learner path:** Docker/Compose or a VM; no cloud needed except MC26/27/34/35.
- **Cloud labs:** Terraform with a spend budget alarm, `terraform destroy` cleanup script, estimated cost in the manifest, never run without the owner's approval and an account the owner supplies. Verification level starts UNVERIFIED; local emulation (for example LocalStack) can reach PARTIALLY VERIFIED at best.
- **Evidence:** every CI run keeps the transcript, which becomes the on-screen terminal output.

## 11. Version and compatibility strategy
Pin every tool in `lab.yaml`. Start matrix (to be confirmed against live release pages before use, hence UNVERIFIED): Java 17 LTS, Maven 3.9.x, Tomcat 10.1.x, PostgreSQL 16/17, Docker Engine current stable, Terraform current stable, Kubernetes current minus one. Review quarterly; lessons whose tool moved two majors are flagged "needs review" and removed from the recommended path until rechecked.
