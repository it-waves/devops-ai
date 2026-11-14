# CloudCart roadmap v0 to v5 (owner direction 2026-11-14)

Owner direction: after Tomcat, do a complete CloudCart v0 deploy built with BOTH Maven and Gradle, deployed to Tomcat, with a beautiful UI shown as a real user would use it. Keep upgrading the same app each version.

App stack (v0): Java 17, Jakarta Servlet 6, JSON API plus a clean static front end (HTML, CSS, vanilla JS), WAR on Tomcat 10.1. No Spring, so Tomcat and the WAR stay the teaching subject. Modules: catalog, cart, orders, login. Same source tree has pom.xml and build.gradle; both must produce an equivalent WAR (compare file lists and run the same tests).
Rule: earlier versions are tagged and never edited except for logged fixes (cloudcart-vN).

| Version | Place in program | Tech and changes | What the user sees in the UI |
|---|---|---|---|
| v0 | right after MC12 Tomcat (new project block, about 5 lessons) | Maven build, Gradle build, same WAR, deploy to Tomcat (manager, webapps, context path, logs), in-memory/H2 data, /health | Browse products, search, add to cart, checkout, sign in, order history; admin health page |
| v0.1 | MC13 | nginx reverse proxy in front of Tomcat, TLS, static files from nginx | Same app on port 80/443 with a real hostname, faster static assets |
| v0.2 | MC14 | PostgreSQL via JDBC, SQL migrations, backup/restore | Data survives restarts; real order history |
| v1 | after MC19 Nexus | Jenkins pipeline, SonarQube gate, artifact to Nexus, versioned releases | Version and build number in the footer; release notes page |
| v2 | after MC23 Compose | Dockerfile, Compose with PostgreSQL, registry image | Same UI from containers; health dashboard |
| v3 | after MC29 Terraform | Cloud infrastructure from Terraform, deployed to a cloud VM | Public URL, environment badge (dev/stage) |
| v4 | after MC36 GitOps | Kubernetes manifests, Helm chart, Argo CD, rolling update and rollback | Zero-downtime upgrade and rollback shown live |
| v5 | after MC41 OpenTelemetry | Metrics, tracing, dashboards, alerts | Trace of one checkout; error and latency panels |

Open questions for the owner: none blocking. Gradle (MC11) continues first; the v0 build block starts when MC12 finishes.
