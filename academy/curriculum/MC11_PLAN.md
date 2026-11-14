# MC11 Gradle: plan (started 2026-11-14)

Environment check (sandbox): Gradle 8.14.3 at /opt/gradle, JDK 21. Real Maven Central works (occasional HTTP 429, retry after ~20 s).
Blocked: services.gradle.org (wrapper download, 403) and plugins.gradle.org (plugin portal). So: use core plugins only (java, application, maven-publish), delete the generated foojay plugin line from settings.gradle, and show the wrapper files without downloading a new distribution. Use `--no-configuration-cache` if the cache complains during a failed resolution.
Real Nexus CE 3.98.1 is reusable from /tmp/ncache/nexus.tgz for the publishing and CI lessons.

Order (simple to advanced, one objective per lesson, UI where it teaches):
- L95 MC11-O01 projects, wrapper, build scripts, task graph (gradle init, tasks, --dry-run, build.gradle line by line)
- L96 MC11-O02 build, test, dependency inspection (dependencies, dependencyInsight, test report HTML)
- L97 MC11-O03 dependencies, repositories, plugins (implementation vs testImplementation, version catalog, mavenCentral, publish to Nexus)
- L98 MC11-O04 environment config and secrets (gradle.properties, env vars, -P, no password in files; ties to L91 Nexus login)
- L99 MC11-O05 build cache and reproducibility (up-to-date, FROM-CACHE, reproducible archives)
- L100 MC11-O06 Gradle in CI (GitHub Actions workflow, real run if possible)
- L101 MC11-O07 diagnose task, dependency and daemon failures
- L102 MC11-O08 Maven vs Gradle for DevOps, then MC11 mastery evidence lesson with lab info on screen

Thumbnails: state boldly what the lesson teaches (owner rule). Each lesson: demo, independent task with lab (up/check/down tested 0/N to N/N), rubric, honest notes, captions, end screen.
