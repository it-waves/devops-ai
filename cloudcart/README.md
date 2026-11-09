# CloudCart v0.1.0 (DevOps Simplified HQ reference application)

Small Java e-commerce API packaged as a WAR for Apache Tomcat 10.1.

## Prerequisites
JDK 17, Maven 3.9.x, Apache Tomcat 10.1.x (Jakarta Servlet 6). Check: `java -version`, `mvn -v`.

## Build and test
```
cd cloudcart
mvn verify
```
Produces `target/cloudcart.war` and test reports in `target/surefire-reports/`.

## Deploy and run
```
cp target/cloudcart.war $CATALINA_HOME/webapps/
$CATALINA_HOME/bin/startup.sh
curl localhost:8080/cloudcart/health
curl localhost:8080/cloudcart/api/products
curl -X POST -d '{"items":[{"productId":2,"quantity":2}]}' localhost:8080/cloudcart/api/orders
```

## API
`GET /health` · `GET /api/products` · `GET /api/products/{id}` · `POST /api/orders` (JSON `{"items":[{"productId":1,"quantity":2}]}` returns `totalCents`).

## Known v0 limits (honest scope)
- Data is in memory. PostgreSQL, authentication, metrics and tracing are NOT in v0 (planned v0.2+); the blueprint's v0 list is reduced accordingly.
- No security hardening beyond input validation.
- Verification: unit tests and a CI runtime smoke test against Tomcat. See CI results; nothing else is claimed.
