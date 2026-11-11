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

## MC02 mastery (catch-up) - DEFERRED by owner on 2026-11-10: "after the program we can come back to fix that"
Scenario, lab (lab/lab26.sh, verified end to end) and script are built; sources in academy/deferred_mc02_mastery. Narration not yet generated. Resume after the whole program. Do not renumber it ahead of MC04.

## MC04 Linux Administration (10 objectives + mastery) - locked lesson order
Lesson numbers continue after L25. One lesson per objective, then the mastery scenario. Each lesson: live terminal, vim (not nano), demo + independent task + pass/fail rubric. The mastery lesson shows lab info on screen (repo, files, install, shortcuts).

| Lesson | Objectives | Topic | "Next" line | Status |
|---|---|---|---|---|
| L26 | MC04-O01 | Shell, paths, filesystem hierarchy, system documentation | Next lesson: files and directories | Published Public yal878gZIRo (8:37), captions, end screen, playlist (Learning; real terminal in a standard-layout view of real dirs, sample files disclosed). First upload iXhsSfijDBc was truncated (4:06), set Private; user to discard it |
| L27 | MC04-O02 | Create, inspect, copy, move, search, edit files (vim) | Next lesson: pipes, redirects, grep, find | Published Public EshJVj6YyUo (7:19), playlist, end screen; real terminal and real vim; sample files disclosed; captions published |
| L28 | MC04-O03 | Pipes, redirects, grep, find, archives, text tools | Next lesson: users, permissions, SSH keys | Published Public 5EQUvFenFGc (6:07), captions, end screen, playlist; real terminal; sample files disclosed |
| L29 | MC04-O04 | Users, groups, sudo, permissions, ownership, SSH keys | Next lesson: processes and signals | Built (6:36; real terminal, private etc copy; key demo only, no remote login), delivered, awaiting upload |
| L30 | MC04-O05 | Processes, signals, resource usage, service status | Next lesson: systemd, logs, cron | Not started |
| L31 | MC04-O06 | systemd services, journal, boot, scheduled jobs | Next lesson: packages | Not started |
| L32 | MC04-O07 | Install/update packages, repositories | Next lesson: disks | Not started |
| L33 | MC04-O08 | Disks, filesystems, mounts, free space, expansion | Next lesson: networking and security | Not started |
| L34 | MC04-O09 | Linux networking, SSH, firewall, security | Next lesson: diagnose and recover | Not started |
| L35 | MC04-O10 | Diagnose and recover failed services, permissions, storage, connectivity | Next lesson: MC04 mastery scenario | Not started |
| L36 | MC04 mastery | Mastery scenario with lab info on screen | Next masterclass: MC05 Bash scripting | Not started |
