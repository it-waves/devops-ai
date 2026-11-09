# DevOps Simplified HQ — DevOps Engineer Competency Checklist

> **Status: Proposed curriculum baseline for review.** Focused on the DevOps engineer role, not specialist certification syllabi. The 48 titles follow Master Directive v4.0; objectives below are newly authored and must be approved before Claude treats them as fixed.

## How to use this checklist

- **Student:** Tick an objective only after completing its associated demonstration or independent check. Watching a video alone is not completion.
- **Claude:** Teach in the listed order, expand each objective into beginner-friendly lessons and labs, and map all lessons to objective IDs. Never silently omit or add required objectives.
- **Verification:** Record lesson/lab links, commands, results, and evidence in a separate progress ledger. Mark unexecuted exercises UNVERIFIED.
- **Scope:** Explain adjacent specialist topics only as necessary to deploy, automate, secure, observe, or troubleshoot software. No switch administration, CCNA-depth routing, full DBA, or general-purpose Java developer curriculum.
- **Cloud:** Do not imply AWS/Azure/EKS/AKS labs were run without real access and evidence.

## Student objective checklists

### MC01 — SDLC & Software Delivery

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 8.

- [ ] **MC01-O01** — Business-to-software journey: identify stakeholders, business outcomes, functional and nonfunctional requirements.
- [ ] **MC01-O02** — Write user stories, acceptance criteria, and a minimal backlog.
- [ ] **MC01-O03** — Distinguish SDLC phases from Waterfall, Agile, Scrum, Kanban, and DevOps.
- [ ] **MC01-O04** — Explain frontend, backend, API, database, source control, build, release, deployment, and operations.
- [ ] **MC01-O05** — Map developer, QA, product, security, operations, and DevOps responsibilities.
- [ ] **MC01-O06** — Trace a change from requirement through code, test, release, deployment, and feedback.
- [ ] **MC01-O07** — Explain environments, approvals, release risk, rollback, and maintenance.
- [ ] **MC01-O08** — Create an SDLC workflow for CloudCart with artifacts and handoffs.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC02 — IT & Computer Fundamentals

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 8.

- [ ] **MC02-O01** — Distinguish client, server, application, operating system, and network.
- [ ] **MC02-O02** — Explain CPU, memory, storage, processes, threads, and resource contention.
- [ ] **MC02-O03** — Use basic command-line and filesystem navigation.
- [ ] **MC02-O04** — Explain virtualization, virtual machines, containers, and their differences.
- [ ] **MC02-O05** — Install and access a disposable Linux VM.
- [ ] **MC02-O06** — Explain binary, text, encodings, files, environment variables, and paths.
- [ ] **MC02-O07** — Identify common server components and their failure symptoms.
- [ ] **MC02-O08** — Trace an HTTP request from browser to application server.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC03 — Computer Networking

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 8.

- [ ] **MC03-O01** — Explain IP addresses, private/public IP, CIDR, subnet, gateway, and DNS.
- [ ] **MC03-O02** — Distinguish TCP, UDP, ports, sockets, and connection states.
- [ ] **MC03-O03** — Explain HTTP methods, status codes, headers, HTTPS, and TLS certificates.
- [ ] **MC03-O04** — Trace name resolution and an application request end to end.
- [ ] **MC03-O05** — Use ping, traceroute, dig/nslookup, curl, ss, and ip for diagnosis.
- [ ] **MC03-O06** — Explain routing, NAT, firewalls, load balancers, and reverse proxies.
- [ ] **MC03-O07** — Identify network boundaries between clients, servers, containers, and cloud subnets.
- [ ] **MC03-O08** — Diagnose DNS, port, firewall, TLS, and routing failures in a lab.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC04 — Linux Administration

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 10.

- [ ] **MC04-O01** — Navigate the shell, paths, filesystem hierarchy, and system documentation.
- [ ] **MC04-O02** — Create, inspect, copy, move, search, and edit files and directories.
- [ ] **MC04-O03** — Use pipes, redirects, grep, find, archives, and text inspection tools.
- [ ] **MC04-O04** — Manage users, groups, sudo, permissions, ownership, and SSH keys.
- [ ] **MC04-O05** — Inspect processes, signals, resource usage, and service status.
- [ ] **MC04-O06** — Manage systemd services, journal logs, boot behavior, and scheduled jobs.
- [ ] **MC04-O07** — Install/update packages and configure repositories for the lab distribution.
- [ ] **MC04-O08** — Inspect disks, filesystems, mounts, free space, and safe storage expansion.
- [ ] **MC04-O09** — Configure basic Linux networking, SSH, firewall, and security controls.
- [ ] **MC04-O10** — Diagnose and recover failed services, permissions, storage, and connectivity.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC05 — Bash Scripting

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 9.

- [ ] **MC05-O01** — Explain shell execution, quoting, expansion, environment, and exit status.
- [ ] **MC05-O02** — Use variables, positional arguments, input, and command substitution.
- [ ] **MC05-O03** — Write conditions, tests, case statements, loops, and functions.
- [ ] **MC05-O04** — Process text with grep, sed, awk, cut, sort, and find.
- [ ] **MC05-O05** — Use pipes, file descriptors, redirection, and safe temporary files.
- [ ] **MC05-O06** — Implement error handling, traps, logging, and predictable exit codes.
- [ ] **MC05-O07** — Handle secrets, permissions, input validation, and shell injection risks.
- [ ] **MC05-O08** — Write idempotent operational scripts and check with ShellCheck.
- [ ] **MC05-O09** — Build and test a deployment/health-check/rollback automation script.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC06 — Python for DevOps

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 9.

- [ ] **MC06-O01** — Set up Python, virtual environments, dependencies, and project structure.
- [ ] **MC06-O02** — Use types, collections, conditions, loops, functions, and modules.
- [ ] **MC06-O03** — Read/write files, JSON, YAML, CSV, and environment configuration.
- [ ] **MC06-O04** — Call REST APIs with authentication, timeouts, and pagination.
- [ ] **MC06-O05** — Handle exceptions, logging, retries, and structured outputs.
- [ ] **MC06-O06** — Write CLI utilities with arguments and useful exit codes.
- [ ] **MC06-O07** — Test automation using pytest and mocks.
- [ ] **MC06-O08** — Use cloud SDKs or infrastructure APIs with least-privilege credentials.
- [ ] **MC06-O09** — Build a tested inventory or deployment validation utility.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC07 — Git & GitHub

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 9.

- [ ] **MC07-O01** — Explain distributed version control and repository anatomy.
- [ ] **MC07-O02** — Initialize, clone, stage, commit, inspect history, and ignore files.
- [ ] **MC07-O03** — Create branches, merge changes, and resolve conflicts.
- [ ] **MC07-O04** — Explain rebasing and when not to rewrite shared history.
- [ ] **MC07-O05** — Use remotes, fetch, pull, push, tags, and release versions.
- [ ] **MC07-O06** — Create pull requests, reviews, and protected-branch workflows.
- [ ] **MC07-O07** — Recover changes with restore, revert, reflog, and safe reset.
- [ ] **MC07-O08** — Manage secrets, credentials, and repository access safely.
- [ ] **MC07-O09** — Implement a team release workflow with automated checks.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC08 — Application Architecture & APIs

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 8.

- [ ] **MC08-O01** — Distinguish frontend, backend, monolith, service, and database responsibilities.
- [ ] **MC08-O02** — Explain request-response, REST endpoints, HTTP status, and JSON.
- [ ] **MC08-O03** — Use curl or API client to inspect and test an endpoint.
- [ ] **MC08-O04** — Explain authentication, authorization, sessions, tokens, and secrets at a practical level.
- [ ] **MC08-O05** — Identify application configuration, environment variables, and feature flags.
- [ ] **MC08-O06** — Explain stateful versus stateless services and persistent data.
- [ ] **MC08-O07** — Understand health, readiness, logs, metrics, and error propagation.
- [ ] **MC08-O08** — Draw CloudCart architecture and trace a request through it.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC09 — Java Fundamentals for DevOps

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 8.

- [ ] **MC09-O01** — Distinguish JDK, JRE, JVM, source, bytecode, and application process.
- [ ] **MC09-O02** — Compile and run a small Java program.
- [ ] **MC09-O03** — Explain packages, classpath, dependencies, and environment configuration.
- [ ] **MC09-O04** — Inspect Java process startup flags and runtime settings.
- [ ] **MC09-O05** — Distinguish JAR and WAR packaging.
- [ ] **MC09-O06** — Read basic stack traces, exceptions, and application logs.
- [ ] **MC09-O07** — Understand Java application tests and build outputs.
- [ ] **MC09-O08** — Diagnose version mismatch, memory, port, and classpath failures.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC10 — Maven

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 8.

- [ ] **MC10-O01** — Explain POM coordinates, project structure, and dependency resolution.
- [ ] **MC10-O02** — Run clean, compile, test, package, and verify lifecycles.
- [ ] **MC10-O03** — Configure plugins, properties, profiles, and reproducible builds.
- [ ] **MC10-O04** — Inspect dependency trees and resolve version conflicts.
- [ ] **MC10-O05** — Package CloudCart as a WAR and verify artifact contents.
- [ ] **MC10-O06** — Configure repository mirrors and credentials safely.
- [ ] **MC10-O07** — Publish snapshot/release artifacts to a repository manager.
- [ ] **MC10-O08** — Diagnose offline, checksum, authentication, and test failures.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC11 — Gradle

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 8.

- [ ] **MC11-O01** — Explain Gradle projects, wrapper, build scripts, and task graph.
- [ ] **MC11-O02** — Run build, test, and dependency inspection tasks.
- [ ] **MC11-O03** — Declare dependencies, repositories, and plugins.
- [ ] **MC11-O04** — Manage environment-specific configuration and secrets safely.
- [ ] **MC11-O05** — Understand build caching and reproducibility.
- [ ] **MC11-O06** — Integrate a Gradle build into CI.
- [ ] **MC11-O07** — Diagnose task, dependency, and daemon failures.
- [ ] **MC11-O08** — Compare Maven and Gradle for DevOps workflows.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC12 — Apache Tomcat

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 8.

- [ ] **MC12-O01** — Explain servlet container, JVM, WAR, connectors, and application contexts.
- [ ] **MC12-O02** — Install and run Tomcat on a disposable Linux host.
- [ ] **MC12-O03** — Deploy, verify, redeploy, and roll back a WAR.
- [ ] **MC12-O04** — Configure ports, environment, application properties, and systemd.
- [ ] **MC12-O05** — Inspect catalina/application logs and diagnose startup failures.
- [ ] **MC12-O06** — Configure a reverse proxy and TLS termination appropriately.
- [ ] **MC12-O07** — Secure management interfaces and service permissions.
- [ ] **MC12-O08** — Monitor health and recover failed deployments.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC13 — Web Servers & Reverse Proxies

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 8.

- [ ] **MC13-O01** — Explain static web serving versus reverse proxy and application server.
- [ ] **MC13-O02** — Install and configure Nginx or Apache HTTP Server.
- [ ] **MC13-O03** — Route traffic to a backend and preserve useful proxy headers.
- [ ] **MC13-O04** — Configure HTTPS/TLS and validate certificates.
- [ ] **MC13-O05** — Implement health checks and basic load balancing.
- [ ] **MC13-O06** — Inspect access/error logs and status codes.
- [ ] **MC13-O07** — Apply timeouts, request-size limits, and secure defaults.
- [ ] **MC13-O08** — Troubleshoot 502/503/504, TLS, and upstream connectivity.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC14 — Databases for DevOps

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 8.

- [ ] **MC14-O01** — Explain relational database, schema, connection, transaction, and migration.
- [ ] **MC14-O02** — Connect to PostgreSQL and run basic diagnostic SQL.
- [ ] **MC14-O03** — Configure database credentials and least-privilege application access.
- [ ] **MC14-O04** — Provision database configuration and persistent storage for a lab.
- [ ] **MC14-O05** — Run schema migrations in a deployment workflow.
- [ ] **MC14-O06** — Back up and restore a database and validate recovered data.
- [ ] **MC14-O07** — Inspect connections, locks, resource pressure, and slow queries.
- [ ] **MC14-O08** — Troubleshoot app-to-database connectivity and migration failures.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC15 — Software Testing & QA

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 8.

- [ ] **MC15-O01** — Distinguish unit, integration, API, end-to-end, smoke, and regression tests.
- [ ] **MC15-O02** — Explain assertions, fixtures, mocks, test data, and isolation.
- [ ] **MC15-O03** — Run automated tests and interpret reports and exit codes.
- [ ] **MC15-O04** — Add API and application health tests to CloudCart.
- [ ] **MC15-O05** — Use test coverage responsibly and understand its limits.
- [ ] **MC15-O06** — Implement tests in CI with clear pass/fail gates.
- [ ] **MC15-O07** — Explain basic performance, load, and security testing purposes.
- [ ] **MC15-O08** — Diagnose flaky tests and environment-dependent failures.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC16 — DevOps Fundamentals

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 8.

- [ ] **MC16-O01** — Explain DevOps principles, collaboration, feedback, and shared ownership.
- [ ] **MC16-O02** — Distinguish CI, continuous delivery, and continuous deployment.
- [ ] **MC16-O03** — Explain infrastructure as code, configuration management, and automation.
- [ ] **MC16-O04** — Understand build artifacts, environments, and release promotion.
- [ ] **MC16-O05** — Explain DevSecOps, SRE, and platform engineering relationships.
- [ ] **MC16-O06** — Interpret deployment frequency, lead time, failure rate, and recovery metrics.
- [ ] **MC16-O07** — Identify bottlenecks in a traditional delivery workflow.
- [ ] **MC16-O08** — Design a practical DevOps improvement plan for CloudCart.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC17 — Jenkins

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 9.

- [ ] **MC17-O01** — Explain controller, agents, executors, plugins, and pipeline lifecycle.
- [ ] **MC17-O02** — Install Jenkins safely and configure initial administration.
- [ ] **MC17-O03** — Create a Jenkinsfile with stages, steps, agents, and post actions.
- [ ] **MC17-O04** — Build and test CloudCart with Maven.
- [ ] **MC17-O05** — Manage credentials and environment variables securely.
- [ ] **MC17-O06** — Integrate source triggers, SonarQube gates, and Nexus publishing.
- [ ] **MC17-O07** — Configure distributed agents and workspace/artifact handling.
- [ ] **MC17-O08** — Implement deployment approval, promotion, rollback, and notifications.
- [ ] **MC17-O09** — Back up, upgrade, and troubleshoot Jenkins and failed agents.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC18 — SonarQube

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 8.

- [ ] **MC18-O01** — Explain static analysis, quality gates, quality profiles, and issue categories.
- [ ] **MC18-O02** — Install and connect a compatible SonarQube lab instance.
- [ ] **MC18-O03** — Run analysis for a Java/Maven project.
- [ ] **MC18-O04** — Interpret bugs, vulnerabilities, hotspots, duplication, and coverage.
- [ ] **MC18-O05** — Configure an appropriate quality gate and explain its limitations.
- [ ] **MC18-O06** — Integrate scanning and gate enforcement into CI.
- [ ] **MC18-O07** — Secure tokens and permissions.
- [ ] **MC18-O08** — Diagnose scanner, server, and quality-gate failures.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC19 — Nexus Repository

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 8.

- [ ] **MC19-O01** — Explain hosted, proxy, and group repositories.
- [ ] **MC19-O02** — Install and secure a repository manager in a lab.
- [ ] **MC19-O03** — Create Maven snapshot and release repositories.
- [ ] **MC19-O04** — Publish and retrieve versioned build artifacts.
- [ ] **MC19-O05** — Configure Maven settings and CI credentials securely.
- [ ] **MC19-O06** — Explain artifact immutability, retention, and provenance.
- [ ] **MC19-O07** — Configure access permissions, backups, and storage monitoring.
- [ ] **MC19-O08** — Troubleshoot 401/403, missing artifact, metadata, and repository failures.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC20 — GitHub Actions

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 8.

- [ ] **MC20-O01** — Explain workflows, events, jobs, steps, actions, and runners.
- [ ] **MC20-O02** — Write a workflow that builds and tests CloudCart.
- [ ] **MC20-O03** — Use caching, artifacts, matrices, and reusable workflows appropriately.
- [ ] **MC20-O04** — Configure branch protections and required status checks.
- [ ] **MC20-O05** — Manage secrets, environments, and permissions safely.
- [ ] **MC20-O06** — Use OIDC for cloud authentication where supported.
- [ ] **MC20-O07** — Implement deployment approvals and release promotion.
- [ ] **MC20-O08** — Diagnose failed workflows, runner issues, and permission errors.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC21 — CI/CD Engineering

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 9.

- [ ] **MC21-O01** — Design an end-to-end commit-to-deployment pipeline.
- [ ] **MC21-O02** — Separate build, test, scan, package, publish, deploy, and verify stages.
- [ ] **MC21-O03** — Use immutable versioned artifacts and environment promotion.
- [ ] **MC21-O04** — Implement quality, security, and approval gates.
- [ ] **MC21-O05** — Configure secure secrets and least-privilege identities.
- [ ] **MC21-O06** — Explain rolling, blue-green, canary, and rollback strategies.
- [ ] **MC21-O07** — Add smoke tests, deployment verification, and notifications.
- [ ] **MC21-O08** — Measure pipeline reliability and troubleshoot failures.
- [ ] **MC21-O09** — Deliver a tested pipeline for CloudCart.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC22 — Docker

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 8.

- [ ] **MC22-O01** — Explain images, containers, registries, layers, and isolation.
- [ ] **MC22-O02** — Run and inspect containers, logs, processes, and resource use.
- [ ] **MC22-O03** — Write a Dockerfile with sensible layers and build context.
- [ ] **MC22-O04** — Build, tag, run, and push a CloudCart image.
- [ ] **MC22-O05** — Configure ports, environment variables, volumes, and networks.
- [ ] **MC22-O06** — Use multi-stage builds and small supported base images.
- [ ] **MC22-O07** — Apply nonroot execution, secrets hygiene, and image scanning.
- [ ] **MC22-O08** — Diagnose image, startup, networking, and storage failures.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC23 — Docker Compose

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 7.

- [ ] **MC23-O01** — Define multi-service applications in Compose YAML.
- [ ] **MC23-O02** — Configure services, ports, networks, and named volumes.
- [ ] **MC23-O03** — Start CloudCart and PostgreSQL with appropriate dependencies.
- [ ] **MC23-O04** — Use health checks and environment configuration.
- [ ] **MC23-O05** — Persist and inspect database data safely.
- [ ] **MC23-O06** — Inspect logs, exec into services, and troubleshoot connectivity.
- [ ] **MC23-O07** — Validate configuration and clean up reproducibly.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC24 — Container Registries & Software Supply Chain

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 8.

- [ ] **MC24-O01** — Explain registry, repository, image tag, digest, and promotion.
- [ ] **MC24-O02** — Authenticate to a registry using scoped credentials.
- [ ] **MC24-O03** — Build and push versioned container images.
- [ ] **MC24-O04** — Explain vulnerabilities, dependency scanning, and SBOMs.
- [ ] **MC24-O05** — Inspect image provenance and understand signing concepts.
- [ ] **MC24-O06** — Enforce basic scanning and promotion policy in CI.
- [ ] **MC24-O07** — Configure retention, access control, and immutable release references.
- [ ] **MC24-O08** — Diagnose registry authentication and pull failures.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC25 — Cloud Computing Fundamentals

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 8.

- [ ] **MC25-O01** — Explain IaaS, PaaS, managed services, and shared responsibility.
- [ ] **MC25-O02** — Distinguish regions, zones, availability, and resilience.
- [ ] **MC25-O03** — Compare compute, object/block storage, networking, and databases.
- [ ] **MC25-O04** — Explain IAM principals, roles, policies, and least privilege.
- [ ] **MC25-O05** — Understand cloud virtual networks, subnets, routing, and firewalls.
- [ ] **MC25-O06** — Estimate basic cloud costs and identify chargeable resources.
- [ ] **MC25-O07** — Apply tagging, budgets, and safe resource cleanup.
- [ ] **MC25-O08** — Select an appropriate cloud service for a deployment scenario.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC26 — AWS Cloud Engineering

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 9.

- [ ] **MC26-O01** — Set up account security, IAM roles, MFA, and cost safeguards.
- [ ] **MC26-O02** — Explain VPC, subnets, routes, internet/NAT gateways, and security groups.
- [ ] **MC26-O03** — Launch, access, monitor, and terminate EC2 instances safely.
- [ ] **MC26-O04** — Use EBS, S3, and backup/restore in deployment scenarios.
- [ ] **MC26-O05** — Configure ALB, DNS, and TLS for an application.
- [ ] **MC26-O06** — Deploy a container with ECR and an appropriate AWS compute service.
- [ ] **MC26-O07** — Use CloudWatch, CloudTrail, Secrets Manager, and KMS at a practical level.
- [ ] **MC26-O08** — Provision and clean up a small application environment reproducibly.
- [ ] **MC26-O09** — Diagnose IAM, network, compute, and deployment failures.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC27 — Microsoft Azure Engineering

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 9.

- [ ] **MC27-O01** — Set up subscription safeguards, RBAC, identities, and budgets.
- [ ] **MC27-O02** — Explain VNets, subnets, NSGs, routing, and private connectivity.
- [ ] **MC27-O03** — Deploy and manage a VM or App Service for an application.
- [ ] **MC27-O04** — Use managed disks, storage accounts, and backup concepts.
- [ ] **MC27-O05** — Configure application ingress, DNS, and TLS.
- [ ] **MC27-O06** — Build/push an image with ACR and deploy to suitable compute.
- [ ] **MC27-O07** — Use Azure Monitor, Key Vault, and managed identities.
- [ ] **MC27-O08** — Provision and clean up a small environment reproducibly.
- [ ] **MC27-O09** — Diagnose identity, network, compute, and deployment failures.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC28 — Cloud Networking & Security

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 8.

- [ ] **MC28-O01** — Map application traffic across public/private cloud boundaries.
- [ ] **MC28-O02** — Explain cloud subnets, route tables, NAT, and security rules.
- [ ] **MC28-O03** — Configure application ingress with TLS and load balancing.
- [ ] **MC28-O04** — Explain private endpoints and service-to-service access.
- [ ] **MC28-O05** — Apply least-privilege IAM and workload identities.
- [ ] **MC28-O06** — Secure secrets and encryption in transit/at rest.
- [ ] **MC28-O07** — Diagnose cloud DNS, routing, firewall, and TLS problems.
- [ ] **MC28-O08** — Review a small cloud deployment for exposure and misconfiguration.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC29 — Terraform

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 9.

- [ ] **MC29-O01** — Explain declarative IaC, providers, resources, and dependency graph.
- [ ] **MC29-O02** — Write and validate HCL resources, variables, outputs, and locals.
- [ ] **MC29-O03** — Use plan, apply, destroy, and state inspection safely.
- [ ] **MC29-O04** — Build reusable modules with clear interfaces.
- [ ] **MC29-O05** — Configure remote state and locking appropriately.
- [ ] **MC29-O06** — Manage environments and sensitive values without committing secrets.
- [ ] **MC29-O07** — Detect drift and import existing resources when justified.
- [ ] **MC29-O08** — Run fmt, validate, and appropriate automated checks in CI.
- [ ] **MC29-O09** — Provision and safely destroy a CloudCart lab environment.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC30 — Ansible

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 8.

- [ ] **MC30-O01** — Explain control node, managed host, inventory, and SSH connection.
- [ ] **MC30-O02** — Run ad hoc commands and basic modules.
- [ ] **MC30-O03** — Write playbooks with variables, tasks, handlers, and templates.
- [ ] **MC30-O04** — Use roles and collections for reusable automation.
- [ ] **MC30-O05** — Apply privilege escalation and Ansible Vault safely.
- [ ] **MC30-O06** — Write idempotent playbooks and verify repeated runs.
- [ ] **MC30-O07** — Configure a Linux/Tomcat deployment with Ansible.
- [ ] **MC30-O08** — Diagnose inventory, authentication, and playbook failures.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC31 — Secrets & Configuration Management

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 8.

- [ ] **MC31-O01** — Distinguish public configuration, credentials, tokens, and certificates.
- [ ] **MC31-O02** — Identify hardcoded-secret risks and leakage paths.
- [ ] **MC31-O03** — Use environment configuration and secret injection safely.
- [ ] **MC31-O04** — Apply least privilege and scoped machine identities.
- [ ] **MC31-O05** — Explain secret rotation, revocation, and audit trails.
- [ ] **MC31-O06** — Integrate a supported secret store with CI or runtime.
- [ ] **MC31-O07** — Handle certificates and configuration changes safely.
- [ ] **MC31-O08** — Recover from an intentionally leaked lab credential.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC32 — Kubernetes

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 10.

- [ ] **MC32-O01** — Explain cluster control plane, nodes, Pods, and reconciliation.
- [ ] **MC32-O02** — Use kubectl contexts, namespaces, and resource inspection.
- [ ] **MC32-O03** — Create and troubleshoot Pods, Deployments, and ReplicaSets.
- [ ] **MC32-O04** — Expose applications with Services and appropriate ingress.
- [ ] **MC32-O05** — Configure ConfigMaps, Secrets, probes, and resource requests/limits.
- [ ] **MC32-O06** — Use persistent volumes/claims and understand storage classes.
- [ ] **MC32-O07** — Implement RBAC, service accounts, and workload security basics.
- [ ] **MC32-O08** — Perform rollout, rollback, scaling, and controlled updates.
- [ ] **MC32-O09** — Diagnose Pending, CrashLoopBackOff, image pull, DNS, and endpoint failures.
- [ ] **MC32-O10** — Deploy and verify CloudCart on a local cluster.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC33 — Helm

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 7.

- [ ] **MC33-O01** — Explain chart structure, templates, values, and releases.
- [ ] **MC33-O02** — Install, inspect, upgrade, and roll back a chart.
- [ ] **MC33-O03** — Parameterize CloudCart configuration across environments.
- [ ] **MC33-O04** — Use templates, helpers, and dependencies responsibly.
- [ ] **MC33-O05** — Lint and render charts before deployment.
- [ ] **MC33-O06** — Manage secrets without exposing them in values files.
- [ ] **MC33-O07** — Diagnose failed releases and template errors.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC34 — Amazon EKS

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 7.

- [ ] **MC34-O01** — Explain managed control plane, nodes, networking, and cluster costs.
- [ ] **MC34-O02** — Provision a minimal EKS cluster using documented automation.
- [ ] **MC34-O03** — Configure kubectl access and workload IAM safely.
- [ ] **MC34-O04** — Deploy CloudCart with registry, ingress, and storage.
- [ ] **MC34-O05** — Configure logging, metrics, and basic autoscaling.
- [ ] **MC34-O06** — Plan cluster/node upgrades and safe cleanup.
- [ ] **MC34-O07** — Diagnose EKS-specific IAM, networking, and scheduling failures.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC35 — Azure AKS

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 7.

- [ ] **MC35-O01** — Explain AKS control plane, node pools, networking, and costs.
- [ ] **MC35-O02** — Provision a minimal AKS cluster using documented automation.
- [ ] **MC35-O03** — Configure kubectl access and workload identity.
- [ ] **MC35-O04** — Deploy CloudCart with ACR, ingress, and storage.
- [ ] **MC35-O05** — Configure monitoring and basic autoscaling.
- [ ] **MC35-O06** — Plan upgrades and safe resource cleanup.
- [ ] **MC35-O07** — Diagnose AKS identity, networking, and scheduling failures.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC36 — Argo CD & GitOps

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 8.

- [ ] **MC36-O01** — Explain declarative desired state and reconciliation.
- [ ] **MC36-O02** — Install Argo CD in a disposable cluster.
- [ ] **MC36-O03** — Connect a Git repository and define an application.
- [ ] **MC36-O04** — Deploy CloudCart from version-controlled manifests or Helm.
- [ ] **MC36-O05** — Inspect sync, health, drift, and rollback behavior.
- [ ] **MC36-O06** — Manage environments and promotions safely.
- [ ] **MC36-O07** — Secure access and repository credentials.
- [ ] **MC36-O08** — Diagnose out-of-sync, unhealthy, and permission failures.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC37 — Platform Engineering

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 7.

- [ ] **MC37-O01** — Explain internal platforms, golden paths, and developer self-service.
- [ ] **MC37-O02** — Identify repetitive developer workflows suitable for standardization.
- [ ] **MC37-O03** — Design a simple self-service deployment template.
- [ ] **MC37-O04** — Provide sensible defaults for security, observability, and cost.
- [ ] **MC37-O05** — Explain ownership, service catalogs, and platform boundaries.
- [ ] **MC37-O06** — Measure developer experience and operational burden.
- [ ] **MC37-O07** — Evaluate build-versus-buy tradeoffs for a small platform.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC38 — DevSecOps

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 9.

- [ ] **MC38-O01** — Explain shift-left and shared security responsibilities.
- [ ] **MC38-O02** — Integrate SAST, dependency, and secret scanning into CI.
- [ ] **MC38-O03** — Scan container images and infrastructure definitions.
- [ ] **MC38-O04** — Interpret findings and prioritize remediation.
- [ ] **MC38-O05** — Apply least privilege to pipelines and workloads.
- [ ] **MC38-O06** — Explain SBOM, artifact provenance, and signed releases.
- [ ] **MC38-O07** — Secure runtime configuration and Kubernetes basics.
- [ ] **MC38-O08** — Handle false positives and risk acceptance transparently.
- [ ] **MC38-O09** — Demonstrate a pipeline that blocks a critical issue.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC39 — Prometheus

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 7.

- [ ] **MC39-O01** — Explain metrics, targets, scraping, exporters, and labels.
- [ ] **MC39-O02** — Expose and scrape CloudCart and infrastructure metrics.
- [ ] **MC39-O03** — Write basic PromQL queries and interpret results.
- [ ] **MC39-O04** — Configure recording and alerting rules.
- [ ] **MC39-O05** — Distinguish counters, gauges, histograms, and rates.
- [ ] **MC39-O06** — Troubleshoot missing targets and misleading metrics.
- [ ] **MC39-O07** — Explain retention and scaling limits.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC40 — Grafana

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 7.

- [ ] **MC40-O01** — Connect a supported metrics data source.
- [ ] **MC40-O02** — Build dashboards for service health, latency, errors, and saturation.
- [ ] **MC40-O03** — Use variables, panels, and meaningful units.
- [ ] **MC40-O04** — Configure alerting and notification basics.
- [ ] **MC40-O05** — Manage access permissions and dashboard versioning.
- [ ] **MC40-O06** — Investigate a CloudCart incident using dashboards.
- [ ] **MC40-O07** — Avoid misleading visualization and alert noise.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC41 — OpenTelemetry & Distributed Tracing

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 7.

- [ ] **MC41-O01** — Explain logs, metrics, traces, spans, and correlation IDs.
- [ ] **MC41-O02** — Instrument a request path in CloudCart.
- [ ] **MC41-O03** — Configure a collector and compatible trace backend.
- [ ] **MC41-O04** — Trace a request across application components.
- [ ] **MC41-O05** — Interpret span timings, errors, and sampling.
- [ ] **MC41-O06** — Protect sensitive telemetry and control cardinality.
- [ ] **MC41-O07** — Diagnose missing spans and broken context propagation.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC42 — Site Reliability Engineering

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 7.

- [ ] **MC42-O01** — Explain reliability, availability, toil, and service ownership.
- [ ] **MC42-O02** — Define useful SLIs, SLOs, and error budgets.
- [ ] **MC42-O03** — Create actionable alerts and basic runbooks.
- [ ] **MC42-O04** — Practice incident roles, escalation, and communications.
- [ ] **MC42-O05** — Perform blameless postmortem and corrective action tracking.
- [ ] **MC42-O06** — Explain capacity, saturation, and graceful degradation.
- [ ] **MC42-O07** — Evaluate operational tradeoffs with CloudCart.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC43 — Production Troubleshooting

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 8.

- [ ] **MC43-O01** — Use a hypothesis-driven incident investigation workflow.
- [ ] **MC43-O02** — Collect logs, metrics, traces, and recent-change evidence.
- [ ] **MC43-O03** — Diagnose Linux process, memory, disk, and service failures.
- [ ] **MC43-O04** — Diagnose DNS, TLS, firewall, proxy, and HTTP failures.
- [ ] **MC43-O05** — Diagnose build, CI/CD, and artifact delivery failures.
- [ ] **MC43-O06** — Diagnose container and Kubernetes rollout failures.
- [ ] **MC43-O07** — Diagnose database connection and application configuration failures.
- [ ] **MC43-O08** — Restore service, verify recovery, and document root cause.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC44 — Disaster Recovery & Business Continuity

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 7.

- [ ] **MC44-O01** — Explain backups, snapshots, redundancy, RTO, and RPO.
- [ ] **MC44-O02** — Identify critical application state and recovery dependencies.
- [ ] **MC44-O03** — Implement a reproducible backup of CloudCart data/configuration.
- [ ] **MC44-O04** — Perform an actual restore and verify integrity.
- [ ] **MC44-O05** — Write a recovery runbook and ownership matrix.
- [ ] **MC44-O06** — Test recovery under a realistic failure scenario.
- [ ] **MC44-O07** — Explain regional disaster and provider-outage tradeoffs.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC45 — FinOps & Performance Optimization

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 7.

- [ ] **MC45-O01** — Explain cloud cost drivers and shared ownership.
- [ ] **MC45-O02** — Estimate and monitor compute, storage, network, and managed-service costs.
- [ ] **MC45-O03** — Use budgets, alerts, tags, and cost allocation.
- [ ] **MC45-O04** — Right-size workloads using measured resource data.
- [ ] **MC45-O05** — Distinguish performance bottlenecks from resource waste.
- [ ] **MC45-O06** — Evaluate autoscaling and reserved/committed capacity tradeoffs.
- [ ] **MC45-O07** — Document cost-performance choices for CloudCart.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC46 — Enterprise DevOps Architecture

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 8.

- [ ] **MC46-O01** — Design dev/test/stage/prod environments and promotion boundaries.
- [ ] **MC46-O02** — Explain multi-account/subscription isolation and identity boundaries.
- [ ] **MC46-O03** — Design secure networking, secrets, and deployment access.
- [ ] **MC46-O04** — Choose appropriate CI/CD, IaC, and orchestration patterns.
- [ ] **MC46-O05** — Define observability, recovery, governance, and operational ownership.
- [ ] **MC46-O06** — Record architecture decisions and meaningful tradeoffs.
- [ ] **MC46-O07** — Review a design for cost, security, reliability, and maintainability.
- [ ] **MC46-O08** — Present and defend a CloudCart reference architecture.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC47 — DevOps Career & Engineering Practice

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 7.

- [ ] **MC47-O01** — Build a portfolio with reproducible projects and credible evidence.
- [ ] **MC47-O02** — Write clear READMEs, runbooks, and architecture diagrams.
- [ ] **MC47-O03** — Explain pull requests, reviews, and engineering collaboration.
- [ ] **MC47-O04** — Practice incident communication and concise status updates.
- [ ] **MC47-O05** — Prepare for DevOps troubleshooting and design interviews.
- [ ] **MC47-O06** — Evaluate job descriptions and identify realistic skill gaps.
- [ ] **MC47-O07** — Explain ethical use of automation and truthful experience claims.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

### MC48 — Enterprise DevOps Capstone

**Outcome:** Demonstrate the following DevOps-relevant capabilities. **Objectives:** 10.

- [ ] **MC48-O01** — Interpret unfamiliar business and nonfunctional requirements.
- [ ] **MC48-O02** — Select and justify a fit-for-purpose architecture.
- [ ] **MC48-O03** — Provision infrastructure reproducibly with safe defaults.
- [ ] **MC48-O04** — Build secure CI/CD with testing and artifact promotion.
- [ ] **MC48-O05** — Deploy CloudCart with configuration and rollback controls.
- [ ] **MC48-O06** — Implement monitoring, alerts, and operational runbooks.
- [ ] **MC48-O07** — Diagnose and recover from injected production-style failures.
- [ ] **MC48-O08** — Demonstrate backup/restore and verify recovery.
- [ ] **MC48-O09** — Document cost, security, architecture, and tradeoffs.
- [ ] **MC48-O10** — Complete an independent technical defense with evidence.

**Mastery evidence:** Complete an independently verifiable scenario applying the objectives above; document results, troubleshooting, and cleanup.

## Required teaching and completion contract

For each objective Claude must create: prerequisite references; plain-English explanation; precise technical explanation; genuine demonstration; complete runnable files/commands where relevant; verification; common errors; guided practice; independent task; and a pass/fail rubric. Group tightly related objectives into lessons without losing mapping.

For each objective record **Not started / Learning / Practiced / Mastered / Blocked**, with evidence links and verification date. The student checklist above is ticked only at **Mastered**.

The list is a curated DevOps core. Specialist elective material may be added separately, not as required core objectives. Validate version-specific technical details against current vendor documentation before teaching.
