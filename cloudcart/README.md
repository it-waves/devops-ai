# CloudCart v0

A small, fully working online store used as the practice project in the DevOps Engineering Bootcamp.
You build it with **Maven**, deploy it to **Tomcat**, and use it like a customer.

## What you get
- Storefront with search, category filter and sorting (12 products, drawn illustrations)
- Product pages, cart with live totals and a free-shipping meter, checkout with validation
- Sign in / create account, order history, out-of-stock handling
- Admin & health page (`admin.html`) and a `/health` endpoint for operators

Demo account: `student@cloudcart.test` / `learn-cloudcart` (lab value only). Nothing is charged or shipped.

## Stack
Java 17, Jakarta Servlet 6 (no framework), Gson, vanilla HTML/CSS/JavaScript, WAR on Tomcat 10.1, in-memory data seeded at startup.

## Build, test, run
```
mvn package                      # compiles, runs 32 JUnit tests, builds target/cloudcart.war
cp target/cloudcart.war $CATALINA_HOME/webapps/
$CATALINA_HOME/bin/startup.sh    # then open http://localhost:8080/cloudcart/
```
End-to-end browser test (needs Node and Playwright): `BASE=http://localhost:8080/cloudcart/ node e2e/e2e.js`

## Honest scope
Data lives in memory and resets when Tomcat restarts. There is no real payment and no email. Those arrive in later versions (see `academy/curriculum/CLOUDCART_ROADMAP.md`).
