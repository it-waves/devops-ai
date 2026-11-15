package academy.cloudcart;

import java.util.LinkedHashMap;
import java.util.Map;

/** Per-visitor state: the cart and who is signed in. Lives in the HTTP session. */
public class Session {
    public final Map<Integer, Integer> cart = new LinkedHashMap<>();
    public String userEmail;
}
