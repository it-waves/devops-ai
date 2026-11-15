# CloudCart roadmap v0 to v5 (owner direction 2026-11-14)

Owner direction: after Tomcat, do a complete CloudCart v0 deploy built with Maven (Gradle half dropped by the owner on 2026-11-15) and deployed to Tomcat, with a beautiful UI shown as a real user would use it. Keep upgrading the same app each version.

App stack (v0): Java 17, Jakarta Servlet 6, JSON API plus a clean static front end (HTML, CSS, vanilla JS), WAR on Tomcat 10.1. No Spring, so Tomcat and the WAR stay the teaching subject. Modules: catalog, cart, orders, login. Same source tree has pom.xml and build.gradle; both must produce an equivalent WAR (compare file lists and run the same tests).
Rule: earlier versions are tagged and never edited except for logged fixes (cloudcart-vN).

| Version | Place in program | Tech and changes | What the user sees in the UI |
|---|---|---|---|
| v0 | right after MC12 Tomcat (new project block, 5 lessons: L113-L117) | Maven build only, one WAR, deploy to Tomcat (manager, webapps, context path, logs), in-memory/H2 data, /health | Browse products, search, add to cart, checkout, sign in, order history; admin health page |
| v0.1 | MC13 | nginx reverse proxy in front of Tomcat, TLS, static files from nginx | Same app on port 80/443 with a real hostname, faster static assets |
| v0.2 | MC14 | PostgreSQL via JDBC, SQL migrations, backup/restore | Data survives restarts; real order history |
| v1 | after MC19 Nexus | Jenkins pipeline, SonarQube gate, artifact to Nexus, versioned releases | Version and build number in the footer; release notes page |
| v2 | after MC23 Compose | Dockerfile, Compose with PostgreSQL, registry image | Same UI from containers; health dashboard |
| v3 | after MC29 Terraform | Cloud infrastructure from Terraform, deployed to a cloud VM | Public URL, environment badge (dev/stage) |
| v4 | after MC36 GitOps | Kubernetes manifests, Helm chart, Argo CD, rolling update and rollback | Zero-downtime upgrade and rollback shown live |
| v5 | after MC41 OpenTelemetry | Metrics, tracing, dashboards, alerts | Trace of one checkout; error and latency panels |

Open questions for the owner: none blocking. Gradle (MC11) continues first; the v0 build block starts when MC12 finishes.

## Build tool rule (owner, 2026-11-14)
Every build uses Maven except where a lesson specifically says to use Gradle. L102 (Maven vs Gradle) and the explicit "built with both Maven and Gradle" CloudCart v0 deploy are the named Gradle exceptions; all other CloudCart versions build with Maven.

## v0 decisions and acceptance rules (owner, 2026-11-15)
- v0 is Maven only. The Gradle half of the earlier request is dropped.
- The app must be fully functional (every screen and button works end to end, real validation and error states) and well designed (consistent dark teal look, responsive, keyboard and screen-reader friendly, clear empty/error states).
- The UI is the first project students meet, so every region of every screen is explained on screen.
- Every lesson opens with an expectations segment: what we build, what you will learn, what you will have at the end.
- The earlier scaffold (v0.1.0 API only) is tagged cloudcart-scaffold; v0 grows from it in cloudcart/ and keeps the CI workflow working. v0 is tagged cloudcart-v0 when its lessons are verified.
- Planned lessons: L113 Meet CloudCart (UI tour), L114 Project layout and Maven build, L115 Deploy to Tomcat (webapps and Manager), L116 Run it like a customer, fix it like an engineer, L117 v0 mastery evidence.
