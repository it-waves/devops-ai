package academy.cloudcart;

import com.google.gson.Gson;
import com.google.gson.JsonSyntaxException;
import java.io.InputStream;
import java.lang.management.ManagementFactory;
import java.time.Instant;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Properties;
import java.util.regex.Pattern;

/** Servlet-free request handling, so every rule can be unit tested without a server. */
public class Api {
    public record Response(int status, String body) { }

    private static final Pattern EMAIL = Pattern.compile("^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$");
    private static final int MAX_PER_LINE = 10;

    private final Gson gson = new Gson();
    private final Catalog catalog = new Catalog();
    private final Users users = new Users();
    private final OrderService orders = new OrderService(catalog);
    private final Instant started = Instant.now();
    private final Properties build = loadBuild();

    // ---------- routing ----------
    public Response handle(String method, String path, Map<String, String> query, String body, Session s) {
        try {
            String[] p = path.replaceAll("^/+|/+$", "").split("/");
            String r = p[0];
            if (r.equals("health")) return health();
            if (!r.equals("api") || p.length < 2) return error(404, "no such endpoint");
            switch (p[1]) {
                case "products":
                    if (!method.equals("GET")) return error(405, "method not allowed");
                    return p.length == 2 ? listProducts(query) : getProduct(p[2]);
                case "categories": return method.equals("GET") ? ok(catalog.categories()) : error(405, "method not allowed");
                case "cart": return cart(method, p, body, s);
                case "auth": return auth(method, p, body, s);
                case "me": return me(s);
                case "orders": return ordersRoute(method, body, s);
                case "admin": return p.length > 2 && p[2].equals("stats") ? stats() : error(404, "no such endpoint");
                default: return error(404, "no such endpoint");
            }
        } catch (JsonSyntaxException e) {
            return error(400, "that request body is not valid JSON");
        } catch (IllegalArgumentException e) {
            return error(400, e.getMessage());
        }
    }

    // ---------- health and admin ----------
    public Response health() {
        Map<String, Object> m = new LinkedHashMap<>();
        m.put("status", "UP");
        m.put("version", build.getProperty("version", "dev"));
        m.put("shop", "CloudCart");
        return ok(m);
    }

    private Response stats() {
        Runtime rt = Runtime.getRuntime();
        Map<String, Object> m = new LinkedHashMap<>();
        m.put("status", "UP");
        m.put("version", build.getProperty("version", "dev"));
        m.put("builtAt", build.getProperty("builtAt", "unknown"));
        m.put("startedAt", started.toString());
        m.put("uptimeSeconds", ManagementFactory.getRuntimeMXBean().getUptime() / 1000);
        m.put("java", System.getProperty("java.version"));
        m.put("server", System.getProperty("server.info", "servlet container"));
        m.put("memoryUsedMb", (rt.totalMemory() - rt.freeMemory()) / 1_048_576);
        m.put("memoryMaxMb", rt.maxMemory() / 1_048_576);
        m.put("products", catalog.all().size());
        m.put("outOfStock", catalog.all().stream().filter(p -> p.stock() == 0).count());
        m.put("users", users.count());
        m.put("orders", orders.count());
        return ok(m);
    }

    // ---------- catalog ----------
    private Response listProducts(Map<String, String> q) {
        return ok(catalog.search(q.get("q"), q.get("category"), q.get("sort")));
    }

    private Response getProduct(String idText) {
        int id;
        try { id = Integer.parseInt(idText); } catch (NumberFormatException e) { return error(400, "product id must be a number"); }
        return catalog.find(id).<Response>map(this::ok).orElseGet(() -> error(404, "product not found"));
    }

    // ---------- cart ----------
    private record ItemBody(Integer productId, Integer quantity) { }

    private Response cart(String method, String[] p, String body, Session s) {
        if (p.length == 2 && method.equals("GET")) return cartView(s);
        if (p.length == 3 && p[2].equals("items") && method.equals("POST")) {
            ItemBody b = parse(body, ItemBody.class);
            if (b.productId() == null) return error(400, "productId is required");
            int qty = b.quantity() == null ? 1 : b.quantity();
            if (qty < 1) return error(400, "quantity must be at least 1");
            Product prod = catalog.find(b.productId()).orElse(null);
            if (prod == null) return error(404, "product not found");
            if (prod.stock() == 0) return error(409, prod.name() + " is out of stock");
            int now = s.cart.getOrDefault(prod.id(), 0) + qty;
            s.cart.put(prod.id(), Math.min(now, limit(prod)));
            return cartView(s);
        }
        if (p.length == 4 && p[2].equals("items")) {
            int id;
            try { id = Integer.parseInt(p[3]); } catch (NumberFormatException e) { return error(400, "product id must be a number"); }
            if (method.equals("DELETE")) { s.cart.remove(id); return cartView(s); }
            if (method.equals("PUT")) {
                ItemBody b = parse(body, ItemBody.class);
                Product prod = catalog.find(id).orElse(null);
                if (prod == null) return error(404, "product not found");
                int qty = b.quantity() == null ? -1 : b.quantity();
                if (qty < 0) return error(400, "quantity must be 0 or more");
                if (qty == 0) s.cart.remove(id); else s.cart.put(id, Math.min(qty, limit(prod)));
                return cartView(s);
            }
        }
        return error(405, "method not allowed");
    }

    private static int limit(Product p) { return Math.min(p.stock(), MAX_PER_LINE); }

    private Response cartView(Session s) {
        List<Map<String, Object>> items = new ArrayList<>();
        int subtotal = 0, count = 0;
        for (var e : s.cart.entrySet()) {
            Product p = catalog.find(e.getKey()).orElseThrow();
            int line = p.priceCents() * e.getValue();
            Map<String, Object> m = new LinkedHashMap<>();
            m.put("productId", p.id());
            m.put("name", p.name());
            m.put("art", p.art());
            m.put("priceCents", p.priceCents());
            m.put("quantity", e.getValue());
            m.put("maxQuantity", limit(p));
            m.put("lineCents", line);
            items.add(m);
            subtotal += line;
            count += e.getValue();
        }
        Map<String, Object> m = new LinkedHashMap<>();
        m.put("items", items);
        m.put("count", count);
        m.put("subtotalCents", subtotal);
        m.put("shippingCents", Pricing.shipping(subtotal));
        m.put("taxCents", Pricing.tax(subtotal));
        m.put("totalCents", Pricing.total(subtotal));
        m.put("freeShippingGapCents", subtotal == 0 ? Pricing.FREE_SHIPPING_CENTS : Math.max(0, Pricing.FREE_SHIPPING_CENTS - subtotal));
        return ok(m);
    }

    // ---------- accounts ----------
    private record AuthBody(String name, String email, String password) { }

    private Response auth(String method, String[] p, String body, Session s) {
        if (p.length != 3 || !method.equals("POST")) return error(405, "method not allowed");
        switch (p[2]) {
            case "login": {
                AuthBody b = parse(body, AuthBody.class);
                var u = users.login(b.email(), b.password());
                if (u.isEmpty()) return error(401, "email or password is wrong");
                s.userEmail = u.get().email();
                return me(s);
            }
            case "register": {
                AuthBody b = parse(body, AuthBody.class);
                if (b.name() == null || b.name().isBlank()) return error(400, "name is required");
                if (b.email() == null || !EMAIL.matcher(b.email().trim()).matches()) return error(400, "enter a valid email address");
                if (b.password() == null || b.password().length() < 8) return error(400, "password must be at least 8 characters");
                s.userEmail = users.register(b.name(), b.email(), b.password()).email();
                return me(s);
            }
            case "logout": s.userEmail = null; return ok(Map.of("signedIn", false));
            default: return error(404, "no such endpoint");
        }
    }

    private Response me(Session s) {
        var u = users.find(s.userEmail);
        if (u.isEmpty()) return ok(Map.of("signedIn", false));
        return ok(Map.of("signedIn", true, "name", u.get().name(), "email", u.get().email()));
    }

    // ---------- orders ----------
    private record CheckoutBody(String name, String address, String city, String zip) { }

    private Response ordersRoute(String method, String body, Session s) {
        if (users.find(s.userEmail).isEmpty()) return error(401, "please sign in first");
        if (method.equals("GET")) return ok(orders.forUser(s.userEmail));
        if (!method.equals("POST")) return error(405, "method not allowed");
        CheckoutBody b = parse(body, CheckoutBody.class);
        if (blank(b.name())) return error(400, "name is required");
        if (blank(b.address())) return error(400, "address is required");
        if (blank(b.city())) return error(400, "city is required");
        if (b.zip() == null || !b.zip().trim().matches("\\d{5}")) return error(400, "ZIP code must be 5 digits");
        var order = orders.place(s.userEmail, s.cart, b.name().trim(), b.address().trim(), b.city().trim(), b.zip().trim());
        s.cart.clear();
        return new Response(201, gson.toJson(order));
    }

    // ---------- helpers ----------
    private static boolean blank(String v) { return v == null || v.isBlank(); }

    private <T> T parse(String body, Class<T> type) {
        T v = gson.fromJson(body == null || body.isBlank() ? "{}" : body, type);
        if (v == null) throw new IllegalArgumentException("empty body");
        return v;
    }

    private Response ok(Object o) { return new Response(200, gson.toJson(o)); }
    private Response error(int status, String message) { return new Response(status, gson.toJson(Map.of("error", message))); }

    private static Properties loadBuild() {
        Properties p = new Properties();
        try (InputStream in = Api.class.getResourceAsStream("/version.properties")) {
            if (in != null) p.load(in);
        } catch (Exception ignored) { }
        return p;
    }
}
