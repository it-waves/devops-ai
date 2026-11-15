# MC12 Apache Tomcat: plan (drafted 2026-11-15)

Order (simple to advanced, one objective per lesson, UI where it teaches, then a mastery evidence lesson with lab info on screen):
- L104 MC12-O01 servlet container, JVM, WAR, connectors, contexts (what Tomcat is; folders; a real Tomcat started, hello page)
- L105 MC12-O02 install and run Tomcat on a disposable Linux host (real download, startup.sh, catalina.out, port 8080, Manager UI tour)
  (L105 note: the Manager UI tour was cut to the sign-in and 401 page; the secured Manager comes in L110)
- L106 MC12-O03 deploy, verify, redeploy, roll back a WAR (built with Maven, the default build tool)
- L107 MC12-O04 ports, environment, application properties, systemd unit
- L108 MC12-O05 catalina and application logs, diagnose startup failures
- L109 MC12-O06 reverse proxy and TLS termination
- L110 MC12-O07 secure the manager interfaces, service permissions
- L111 MC12-O08 health monitoring, recover a failed deployment
- L112 MC12 mastery evidence, then CloudCart v0 deploy (Maven build; Gradle also per the owner's explicit v0 request)

Build tool rule: Maven for every build unless a lesson says Gradle.
Environment checks before L104: can Tomcat be downloaded (Apache archive host reachable from the sandbox?), is a systemd available for L107.
