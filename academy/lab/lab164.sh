#!/bin/sh
# Lesson 164 lab: add the demo file with seeded defects to CloudCart, so SonarQube has something to find.
# Usage: lab164.sh files | down      Own machine only. Run it inside your CloudCart folder (CLOUDCART=path to override).
C=${CLOUDCART:-.}; F=$C/src/main/java/academy/cloudcart/LegacyPricing.java
case "$1" in
files) [ -d "$C/src/main/java/academy/cloudcart" ] || { echo "Run this inside your CloudCart folder, or set CLOUDCART"; exit 1; }
cat > $F <<'J'
package academy.cloudcart;

import java.security.MessageDigest;
import java.util.Random;

public class LegacyPricing {
    public String newToken() {
        Random r = new Random();
        return "tok-" + r.nextInt();
    }

    public byte[] fingerprint(String s) throws Exception {
        return MessageDigest.getInstance("MD5").digest(s.getBytes());
    }

    public void loadRates() {
        int unused = 42;
        try {
            Integer.parseInt("x");
        } catch (Exception e) {
        }
    }
}
J
echo "Wrote $F: a weak hash, a weak random generator, an unused variable and an empty catch."
echo "Next lesson you scan it. Then try: lab164.sh down";;
down) rm -f $F; echo "Removed $F";;
*) echo "usage: lab164.sh files|down";;
esac
