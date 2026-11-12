# Progress ledger (objective status)

Baseline: curriculum/CHECKLIST.md (owner-supplied 2026-11-09; approved by owner as the curriculum baseline).
Status values: Not started / Learning / Practiced / Mastered / Blocked. A student tick needs Mastered (demonstration or independent check done), never video-watching alone.
Published videos are "Learning" at most. Nothing is Practiced or Mastered until a lab is run and evidenced.

## Rule: lesson order and every "Next lesson" line follow the checklist order (MCnn-O01..On). A lesson never promises a topic that is not the next planned objective.

## MC01 SDLC & Software Delivery (8 objectives) - locked lesson order

| Lesson | Objectives | Topic | "Next" line it must end with | Status |
|---|---|---|---|---|
| L1 | O03 (phases), O04 (partly) | What is the SDLC (v1 published 4:27; v2 >=5 min planned) | Next lesson: requirements, in depth | Published Public _7EF5PkVKQ8 (v2 5:12, captions published, end screen); v1 09EBDVIryE8 Private |
| L2 | O01, O02 | Requirements, user stories, acceptance criteria, MoSCoW, non-functional | Next lesson: Waterfall, Agile, Scrum, and Kanban | Published WeIneBelLD0, Learning |
| L3 | O03 | SDLC phases vs Waterfall, Agile, Scrum, Kanban, DevOps | Next lesson: the parts of an application | Published Public sgyICCybIVs (v2 6:15, captions published, end screen); v1 -ESjf8NRNng Private |
| L4 | O04 | Frontend, backend, API, database, source control, build, release, deployment, operations | Next lesson: who does what | Published Public rGHYQJZiFQc (v2 6:12, captions published, end screen); v1 E5VgT6n5e7E Private, removed from playlist |
| L5 | O05 | Responsibilities: developer, QA, product, security, operations, DevOps | Next lesson: tracing one change | Published Public 5:30 (IbxM4p_vSoY), Learning |
| L6 | O06 | Trace a change: requirement to code, test, release, deploy, feedback | Next lesson: environments and releases | Published Public EQD7e4ZnWxM (5:01), captions published, playlist order verified |
| L7 | O07 | Environments, approvals, release risk, rollback, maintenance | Next lesson: the CloudCart workflow | Published Public H4rLyJlUcOE (6:19, captions published, end screen), Learning |
| L8 | O08 | Mastery scenario: CloudCart SDLC workflow with artifacts and handoffs | Next masterclass: MC02 IT and computer fundamentals | Published Public H2htKZboJ6A (5:53, captions published, end screen), Learning |

Open items: Lesson 1 v2 (>=5 min, ends with the L2 line above); Intro and DevOps Loop are orientation videos, not mapped to objectives; L2 lab sheet (backlog practice for O02).
Rules in force: from Lesson 11 on, thumbnails (and lesson visuals where useful) use real, clean, openly licensed photos of the subject, with credits in the description (owner request 2026-11-09);  each lesson >=5 min, shows "Objectives covered" in description and recap, has a demonstration, an independent task and a pass/fail rubric; cloud labs UNVERIFIED unless run with evidence; version-specific facts checked against vendor docs before teaching.

## MC02 IT & Computer Fundamentals (8 objectives) - locked lesson order
Lesson numbers continue from MC01 (global numbering, L9-L16). One lesson per objective, in checklist order.

| Lesson | Objectives | Topic | "Next" line it must end with | Status |
|---|---|---|---|---|
| L9 | O01 | Client, server, application, operating system, network | Next lesson: CPU, memory, storage, and processes | Published Public ibqI_dKshYU (6:30, captions published, end screen, playlist order verified), Learning |
| L10 | O02 | CPU, memory, storage, processes, threads, resource contention | Next lesson: the command line and the filesystem | Published Public JLNkuPloShY (5:41, captions published, end screen), Learning |
| L11 | O03 | Command-line and filesystem navigation | Next lesson: virtualization and containers | Published Public 9x_11bcLkd8 (5:13, captions published, end screen, CC0 photo credited), Learning |
| L12 | O04 | Virtualization, virtual machines, containers, and their differences | Next lesson: your own Linux virtual machine | Published Public -A6QOWIphU4 (5:24, captions published, end screen, CC0 photo credited), Learning |
| L13 | O05 | Install and access a disposable Linux VM | Next lesson: files, text, encodings, and paths | Published (Learning; rev 2 live wizard, QEMU stand-in labelled) https://youtu.be/Cccuj7dxwS4 |
| L14 | O06 | Binary, text, encodings, files, environment variables, paths | Next lesson: server components and failure symptoms | Published Public vbSVwbOrqG8 (12:29, Learning; captions published, end screen, playlist) https://youtu.be/vbSVwbOrqG8 |
| L15 | O07 | Common server components and their failure symptoms | Next lesson: tracing one web request | Published Public d-rZpuwyomc (10:33, Learning; captions published, end screen, playlist) https://youtu.be/d-rZpuwyomc |
| L16 | O08 | Trace an HTTP request from browser to application server | Next masterclass: MC03 Computer networking | Published Public SbkjVUt2wAY (8:17, Learning; captions, end screen, playlist; live demos: DNS via curl --resolve, request/response lines, 200/404/500, timing report) |
| L17 | MC03-O01 | Explain IP addresses, private/public IP, CIDR, subnet, gateway, and DNS | Next: MC03-O02 TCP, UDP, ports | Published Public AqUkNak5Ezs (9:51, Learning; captions, end screen, playlist; router is an illustration, real photo pending a working download) |

## MC03-MC48: Not started (see CHECKLIST.md). A lesson-order table like the one above is written before each masterclass begins.
| L18 | MC03-O02 | Ports, TCP, UDP, states | Published Public Wgk24aRIPH4 (9:10, Learning; captions, end screen, playlist; door art is an illustration) |
| L19 | MC03-O03 | HTTP, status codes, HTTPS, TLS | Published Public E41pEPJsl14 (8:09, Learning; captions, end screen, playlist; thumbnail uses real terminal frames) |
| L20 | MC03-O04 | DNS, records, name to page end to end | Published Public Rxx1Q-6tyFs (7:17, Learning; captions, end screen, playlist; real dig/getent/curl against a local lab DNS server; thumbnail uses real terminal frames) |
| L21 | MC03-O05 | ip, ping, traceroute, dig, ss, curl diagnosis | Published Public z3PCHJeU7BI (7:34, Learning; captions, end screen, playlist; real output from a 3-namespace lab on one computer; thumbnail uses real terminal frames) |
| L22 | MC03-O06 | Routing, NAT, firewalls, load balancers, reverse proxies | Published Public NWnBPb-BS2o (9:05, Learning; captions, end screen, playlist; real 3-namespace lab + nginx; thumbnail uses real terminal frames) |
| L23 | MC03-O07 | Network boundaries: clients, servers, containers, cloud subnets | Published Public, youtu.be/QQujGd_dKY4 (Learning; captions, end screen, playlist; real 6-namespace lab + hand-built container network; real AWS console segment, account details blurred, resources deleted afterwards; thumbnail uses real frames) |
| L24 | MC03-O08 | Diagnose DNS, port, firewall, TLS and routing failures in a lab | Next: MC03 mastery scenario (L25) | Published Public S8ZAIQ5Oz7I, captions on (Learning; real 3-namespace lab with 5 faults injected in advance; thumbnail uses real terminal frames) |
| L25 | MC03 mastery | Mastery scenario: independently verifiable network diagnosis lab; document results, troubleshooting, cleanup | Next masterclass: MC04 Linux administration | Published Public sGqq-OVOHL0, captions on, end screen, playlist (6:22, Learning; real 3-namespace lab, 4 faults, checker script; first fault fixed live; report template; lab run end to end with evidence) |

## NEXT MASTERCLASS (owner directive 2026-11-12): Git and GitHub, beginner to mastery. Show the GitHub web UI as a continuous live screen recording (real clicks, narrated), not stills. Applies to all UI domains (GitHub, AWS and Azure consoles).

## MC02 mastery (catch-up) - DEFERRED by owner on 2026-11-10: "after the program we can come back to fix that"
Scenario, lab (lab/lab26.sh, verified end to end) and script are built; sources in academy/deferred_mc02_mastery. Narration not yet generated. Resume after the whole program. Do not renumber it ahead of MC04.

## MC04 Linux Administration (10 objectives + mastery) - locked lesson order
Lesson numbers continue after L25. One lesson per objective, then the mastery scenario. Each lesson: live terminal, vim (not nano), demo + independent task + pass/fail rubric. The mastery lesson shows lab info on screen (repo, files, install, shortcuts).

| Lesson | Objectives | Topic | "Next" line | Status |
|---|---|---|---|---|
| L26 | MC04-O01 | Shell, paths, filesystem hierarchy, system documentation | Next lesson: files and directories | Published Public yal878gZIRo (8:37), captions, end screen, playlist (Learning; real terminal in a standard-layout view of real dirs, sample files disclosed). First upload iXhsSfijDBc was truncated (4:06), set Private; user to discard it |
| L27 | MC04-O02 | Create, inspect, copy, move, search, edit files (vim) | Next lesson: pipes, redirects, grep, find | Published Public EshJVj6YyUo (7:19), playlist, end screen; real terminal and real vim; sample files disclosed; captions published |
| L28 | MC04-O03 | Pipes, redirects, grep, find, archives, text tools | Next lesson: users, permissions, SSH keys | Published Public 5EQUvFenFGc (6:07), captions, end screen, playlist; real terminal; sample files disclosed |
| L29 | MC04-O04 | Users, groups, sudo, permissions, ownership, SSH keys | Next lesson: processes and signals | Published Public N9IYS05Ysao (6:36), captions, end screen, playlist; real terminal, private etc copy; key demo only, no remote login |
| L30 | MC04-O05 | Processes, signals, resource usage, service status | Next lesson: systemd, logs, cron | Published (H0MuFuuOqYA, 5:46; real terminal with its own process list; host uptime/load/memory numbers) |
| L31 | MC04-O06 | systemd services, journal, boot, scheduled jobs | Next lesson: packages | Published (8fIFbG-4xuY, 7:07; real unit-file reads, verify and calendar checks; systemctl, journalctl, boot and cron screens are labelled illustrations because the sandbox does not run systemd) |
| L32 | MC04-O07 | Install/update packages, repositories | Next lesson: disks | Built (6:44; every terminal segment is a real Ubuntu 24.04 recording incl. real sudo apt-get update/install/remove/autoremove of cowsay; no illustrations), Published (88z8drNqD_0, 6:44) |
| L33 | MC04-O08 | Disks, filesystems, mounts, free space, expansion | Next lesson: networking and security | Built (9:02; every terminal segment is a real Ubuntu 24.04 recording on a loop-mounted practice disk; only the fstab line card is a labelled illustration), Published (auXXBOCxi8g, 9:02) |
| L34 | MC04-O09 | Linux networking, SSH, firewall, security | Next lesson: diagnose and recover | Published (ArJrv4aabnM, 8:55, https://youtu.be/ArJrv4aabnM; every terminal segment is a real Ubuntu 24.04 recording on a private practice network: ip, ping, ss, SSH keys, sshd hardening, ufw) |
| L35 | MC04-O10 | Diagnose and recover failed services, permissions, storage, connectivity | Next lesson: MC04 mastery scenario | Published (ukSEbfyFEPM, 9:20, https://youtu.be/ukSEbfyFEPM; real Ubuntu 24.04 recordings of permission denied, disk full, connection refused; broken unit file checked offline with systemd-analyze; systemctl/journalctl screen is a labelled illustration) |
| L36 | MC04 mastery | Mastery scenario with lab info on screen | Next masterclass: MC05 Bash scripting | Published (nFPZviAM-yE, 7:23, https://youtu.be/nFPZviAM-yE; captions uploaded; lab36.sh run end to end: 4 FAIL, 4 PASS after fixes, clean removal; real Ubuntu 24.04 recordings of install, lab up/check, fault 1 fixed live and cleanup proof; getlab, scenario and report screens are labelled illustrations) |

## MC05 Bash Scripting (9 objectives + mastery) - locked lesson order
One lesson per objective, then the mastery scenario. Real Ubuntu 24.04 terminal, vim, demo + independent task + rubric.

| Lesson | Objectives | Topic | "Next" line | Status |
|---|---|---|---|---|
| L37 | MC05-O01 | Shell execution, quoting, expansion, environment, exit status | Next lesson: variables, arguments, input | Published (GoieJXqMSqk, 9:17, https://youtu.be/GoieJXqMSqk; captions uploaded; five real Ubuntu 24.04 terminal demos: how a script runs, quoting, expansion, environment, exit status; four-step diagram labelled illustration |
| L38 | MC05-O02 | Variables, positional arguments, input, command substitution | Next lesson: conditions, loops, functions | Published (iCJD8btV7yc, 7:42, https://youtu.be/iCJD8btV7yc; five real Ubuntu 24.04 terminal demos: variables, positional arguments, read, command substitution, a backup script; captions published) |
| L39 | MC05-O03 | Conditions, tests, case, loops, functions | Next lesson: text processing | Published (-scspi2DLUU, 9:33, https://youtu.be/-scspi2DLUU; six real Ubuntu 24.04 terminal demos: if/else, tests, case, loops, functions, health-check script; captions published) |
| L40 | MC05-O04 | grep, sed, awk, cut, sort, find | Next lesson: pipes, file descriptors, temp files | Published (3mWfNoWRf1Y, 9:49, https://youtu.be/3mWfNoWRf1Y; six real demos; captions published) |
| L41 | MC05-O05 | Pipes, file descriptors, redirection, safe temp files | Next lesson: error handling and traps | Published (heCG-klUYFc, 8:40, https://youtu.be/heCG-klUYFc; five real demos; captions published) |
| L42 | MC05-O06 | Error handling, traps, logging, exit codes | Next lesson: secrets and safe input | Published (RedniqKyMX0, 7:36, https://youtu.be/RedniqKyMX0; five real demos; captions published) |
| L43 | MC05-O07 | Secrets, permissions, input validation, injection risks | Next lesson: idempotent scripts and ShellCheck | Published (15YDY5MxKgQ, 8:56, https://youtu.be/15YDY5MxKgQ; five real demos; captions published) |
| L44 | MC05-O08 | Idempotent operational scripts, ShellCheck | Next lesson: deploy, health check, rollback script | Published (T6ejuN7cANU, 8:00, https://youtu.be/T6ejuN7cANU; six real demos; captions published) |
| L45 | MC05-O09 | Deployment/health-check/rollback automation script | Next lesson: MC05 mastery scenario | Published (3GBH18iO0So, 6:05, https://youtu.be/3GBH18iO0So; real Ubuntu 24.04 terminal demos plus real Chrome screenshots of the demo page; labs unverified; captions published) |
| L46 | MC05 mastery | Mastery scenario with lab info on screen | Next masterclass: MC06 Python for DevOps | Published (Q4zXrtMexfg, 8:03, https://youtu.be/Q4zXrtMexfg; real Ubuntu 24.04 terminal demos; lab46.sh with four faults tested end to end; labs unverified; captions published) |
| L47 | MC06-O01 | Python setup, virtual environments, dependencies, project structure | Next: types, collections, conditions, loops, functions | Published (zL0ZJw9CgkI, 9:36, https://youtu.be/zL0ZJw9CgkI; real Ubuntu 24.04 terminal demos with real pip installs; check47.sh checker tested on passing and failing projects; labs unverified; captions published) |
| L48 | MC06-O02 | Types, collections, conditions, loops, functions, modules | Next: files, JSON, YAML, CSV, env config | Published (tyv361iy6To, 8:44, https://youtu.be/tyv361iy6To; real Ubuntu 24.04 REPL and script demos; check48.sh tested with reference solution and failing file; labs unverified; uploaded by me via Studio; captions published) |
| L49 | MC06-O03 | Files, JSON, YAML, CSV, environment variables | Next: REST APIs, auth, timeouts, pagination | Built (9:22; real Ubuntu 24.04 REPL and script demos; check49.sh tested with reference solution, failing file and hard-coded limit; PyYAML preinstalled, pip step described; labs unverified); uploaded by me via Studio; Published (2C4w8AgD_0Q, 9:22, https://youtu.be/2C4w8AgD_0Q); captions published |
| L50 | MC06-O04 | REST APIs: requests, Bearer token, timeouts, pagination | Next: exceptions, logging, retries | Published (YopPEShN3ck, 8:11, https://youtu.be/YopPEShN3ck; real Ubuntu 24.04 demos against local lab API; check50.sh tested with reference solution and failing files; labs unverified); uploaded by me via Studio; captions published |
| L51 | MC06-O05 | Exceptions, logging, retries | Next: CLI tools and exit codes | Published (NH2altszb-k, 7:35, https://youtu.be/NH2altszb-k; uploaded by me via Studio; captions published) |
| L52 | MC06-O06 | CLI tools and exit codes (argparse, 0/1/2, stdout vs stderr) | Next: pytest and mocks | Published (_SfHfOcdpuo, 7:05, https://youtu.be/_SfHfOcdpuo; uploaded by me via Studio; captions published) |
| L53 | MC06-O07 | pytest and mocks (assert, parametrize, patch) | Next: cloud SDKs with least privilege | Published (kTAizqRfkx0, 6:58, https://youtu.be/kTAizqRfkx0; uploaded by me via Studio; captions published) |
| L54 | MC06-O08 | Cloud SDKs with least privilege (boto3, moto, IAM policy audit) | Next: tested inventory validation utility | Published (nGNe5xhQ6hk, 6:47, https://youtu.be/nGNe5xhQ6hk; uploaded by me via Studio; captions published) |
| L55 | MC06-O09 | Tested inventory validation utility (exit codes, edges, pytest) | Next: Python for DevOps mastery evidence | Published (n8so-RBKj7o, 6:58, https://youtu.be/n8so-RBKj7o; uploaded by me via Studio; captions published) |
| L56 | MC06 mastery | Mastery scenario with lab info on screen | Next masterclass: Git and GitHub (beginner to mastery; show GitHub UI live) | Published (1hZTi5THEWo, 8:20, https://youtu.be/1hZTi5THEWo; uploaded by me via Studio; captions published; lab56.sh run end to end: 4 FAIL, 4 PASS after fixes, clean removal; real Ubuntu 24.04 recordings of install, lab up/check, fault 1 fixed live and cleanup proof; getlab, scenario and report screens are labelled illustrations; labs unverified) |
| L57 | MC07-O01 Git: distributed version control and repository anatomy | Published (rSyxwdl_NPE, 11:56, https://youtu.be/rSyxwdl_NPE; uploaded by me via Studio; Public, playlist, end screen done; captions published; UI scene = real GitHub frames on private demo repo it-waves/git-lab-demo; lab57.sh run end to end; labs unverified) |
| L58 | MC07-O02 Git: staging, history and ignore files | Published (HYXZSB9D_Cg, 9:10, https://youtu.be/HYXZSB9D_Cg; uploaded by me via Studio; Public, playlist, end screen done; captions published; lab58.sh run end to end; labs unverified) |
| L59 | MC07-O03 Git: branches, merging and conflicts | Published (Fg_H2BBJRM8, 9:05, https://youtu.be/Fg_H2BBJRM8; uploaded by me via Studio; Public, playlist, end screen done; captions published; lab59.sh run end to end; labs unverified) |
| L60 | MC07-O04 Git: rebasing | Published (OoYo0hVqvVo, 7:52, https://youtu.be/OoYo0hVqvVo; uploaded by me via Studio; Public, playlist, end screen done; captions published; lab60.sh run end to end; labs unverified) |
| L61 | MC07-O05 Git: remotes, fetch, pull, push, tags | Published (Q8FPBQyvBAA, 7:22, https://youtu.be/Q8FPBQyvBAA; uploaded by me via Studio; Public, playlist, end screen done; captions published|
| L62 | MC07-O06 Git: pull requests, reviews, protected branches | Published (JwolVMgWCkk, 6:18, Public, playlist, end screen); live full-screen recording on a local Gitea; lab62.sh tested only against a simulated GitHub API; captions pending |
