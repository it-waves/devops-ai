# MC19 Nexus Repository: plan (decided 2026-11-27)

Real Nexus Repository Community Edition 3.98.1 (extracted at /tmp/nx, see REAL_NEXUS_PLAN.md for verified UI facts, wizard, 409 refusal text, throttling). Every UI lesson is a continuous live recording (terminal + Chrome recorder, pipeline from L172), simple to advanced, Maven only, free resources only, same narrator. Spoken name: "Nexus". Lesson text must differ from MC10 (L91-L94 covered deploy basics): MC19 goes deep on repository design, security, operations and failure diagnosis. One dry run, calibrate, ONE live take.

| Lesson | Objective | UI? | Plan |
|---|---|---|---|
| L173 | O01 hosted, proxy, group | UI tour | Illustrations; live: repositories list, hosted vs proxy vs group, resolve one artifact through the group, watch the proxy cache fill |
| L174 | O02 install and secure a lab instance | Terminal + UI | Unpack, run as non-root, first login, wizard, admin password, anonymous off, base URL, lab174.sh |
| L175 | O03 snapshot and release repositories | UI | Create both, version policy, deployment policy, layout; why two repos |
| L176 | O04 publish and retrieve versioned artifacts | Terminal + UI | mvn deploy snapshot and release, Browse, retrieve by coordinates and with curl, search |
| L177 | O05 Maven settings and CI credentials | Terminal + UI | settings.xml servers and mirrors, deployer user, Jenkins credential, never in the pom |
| L178 | O06 immutability, retention, provenance | UI | Disable redeploy, cleanup policies, checksums, build info in the asset |
| L179 | O07 permissions, backups, storage monitoring | UI | Roles and privileges, blob stores, backup task, storage and health checks |
| L180 | O08 troubleshoot 401/403, missing artifact, metadata, repository failures | UI + terminal | Read the first error; four real failures fixed live |
| L181 | MC19 mastery | UI + terminal | Verifiable scenario with lab181.sh up/check/down, results, troubleshooting, cleanup, lab info on screen |

Next domain after MC19: MC20 GitHub Actions. CloudCart v1 lands after MC19 (see CLOUDCART_ROADMAP.md).
