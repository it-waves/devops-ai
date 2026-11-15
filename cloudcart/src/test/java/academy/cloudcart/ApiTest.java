package academy.cloudcart;

import static org.junit.jupiter.api.Assertions.*;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import java.util.Map;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class ApiTest {
    private Api api;
    private Session s;

    @BeforeEach void fresh() { api = new Api(); s = new Session(); }

    private Api.Response call(String method, String path, String body) { return api.handle(method, path, Map.of(), body, s); }
    private JsonObject obj(Api.Response r) { return JsonParser.parseString(r.body()).getAsJsonObject(); }
    private void login() { assertEquals(200, call("POST", "/api/auth/login", "{\"email\":\"student@cloudcart.test\",\"password\":\"learn-cloudcart\"}").status()); }

    @Test void healthIsUp() {
        var r = call("GET", "/health", null);
        assertEquals(200, r.status());
        assertEquals("UP", obj(r).get("status").getAsString());
    }
    @Test void listsTwelveProducts() {
        var arr = JsonParser.parseString(call("GET", "/api/products", null).body()).getAsJsonArray();
        assertEquals(12, arr.size());
    }
    @Test void searchAndCategoryFilter() {
        var r = api.handle("GET", "/api/products", Map.of("q", "keyboard"), null, s);
        assertEquals(1, JsonParser.parseString(r.body()).getAsJsonArray().size());
        var audio = api.handle("GET", "/api/products", Map.of("category", "Audio"), null, s);
        assertEquals(3, JsonParser.parseString(audio.body()).getAsJsonArray().size());
    }
    @Test void sortsByPrice() {
        JsonArray a = JsonParser.parseString(api.handle("GET", "/api/products", Map.of("sort", "price-asc"), null, s).body()).getAsJsonArray();
        assertEquals(1600, a.get(0).getAsJsonObject().get("priceCents").getAsInt());
    }
    @Test void unknownProductIs404() { assertEquals(404, call("GET", "/api/products/42", null).status()); }
    @Test void badProductIdIs400() { assertEquals(400, call("GET", "/api/products/abc", null).status()); }
    @Test void unknownEndpointIs404() { assertEquals(404, call("GET", "/api/nothing", null).status()); }

    @Test void cartAddUpdateRemove() {
        call("POST", "/api/cart/items", "{\"productId\":2,\"quantity\":2}");
        var v = obj(call("POST", "/api/cart/items", "{\"productId\":2}"));
        assertEquals(3, v.get("count").getAsInt());
        assertEquals(10500, v.get("subtotalCents").getAsInt());
        assertEquals(0, v.get("shippingCents").getAsInt());
        v = obj(call("PUT", "/api/cart/items/2", "{\"quantity\":1}"));
        assertEquals(3500, v.get("subtotalCents").getAsInt());
        assertEquals(699, v.get("shippingCents").getAsInt());
        v = obj(call("DELETE", "/api/cart/items/2", null));
        assertEquals(0, v.get("count").getAsInt());
    }
    @Test void cartCapsAtStockAndTen() {
        call("POST", "/api/cart/items", "{\"productId\":3,\"quantity\":50}");
        assertEquals(6, s.cart.get(3));
        call("POST", "/api/cart/items", "{\"productId\":10,\"quantity\":50}");
        assertEquals(10, s.cart.get(10));
    }
    @Test void outOfStockCannotBeAdded() { assertEquals(409, call("POST", "/api/cart/items", "{\"productId\":7}").status()); }
    @Test void badCartInputs() {
        assertEquals(404, call("POST", "/api/cart/items", "{\"productId\":99}").status());
        assertEquals(400, call("POST", "/api/cart/items", "{\"quantity\":1}").status());
        assertEquals(400, call("POST", "/api/cart/items", "{\"productId\":1,\"quantity\":0}").status());
        assertEquals(400, call("POST", "/api/cart/items", "{not json").status());
    }

    @Test void loginWrongPasswordIs401() {
        assertEquals(401, call("POST", "/api/auth/login", "{\"email\":\"student@cloudcart.test\",\"password\":\"nope\"}").status());
        assertFalse(obj(call("GET", "/api/me", null)).get("signedIn").getAsBoolean());
    }
    @Test void loginThenLogout() {
        login();
        assertEquals("Sam Student", obj(call("GET", "/api/me", null)).get("name").getAsString());
        call("POST", "/api/auth/logout", null);
        assertFalse(obj(call("GET", "/api/me", null)).get("signedIn").getAsBoolean());
    }
    @Test void registerValidatesAndRejectsDuplicates() {
        assertEquals(400, call("POST", "/api/auth/register", "{\"name\":\"A\",\"email\":\"bad\",\"password\":\"longenough\"}").status());
        assertEquals(400, call("POST", "/api/auth/register", "{\"name\":\"A\",\"email\":\"a@b.co\",\"password\":\"short\"}").status());
        assertEquals(200, call("POST", "/api/auth/register", "{\"name\":\"Ada\",\"email\":\"ada@b.co\",\"password\":\"longenough\"}").status());
        assertEquals(400, call("POST", "/api/auth/register", "{\"name\":\"Ada\",\"email\":\"ADA@b.co\",\"password\":\"longenough\"}").status());
    }

    @Test void checkoutNeedsSignIn() { assertEquals(401, call("POST", "/api/orders", "{}").status()); }
    @Test void checkoutHappyPathTakesStockAndClearsCart() {
        login();
        call("POST", "/api/cart/items", "{\"productId\":3,\"quantity\":2}");
        var r = call("POST", "/api/orders", "{\"name\":\"Sam\",\"address\":\"1 Main St\",\"city\":\"Austin\",\"zip\":\"78701\"}");
        assertEquals(201, r.status());
        var o = obj(r);
        assertEquals("CC-1001", o.get("id").getAsString());
        assertEquals(43800, o.get("subtotalCents").getAsInt());
        assertEquals(3504, o.get("taxCents").getAsInt());
        assertEquals(47304, o.get("totalCents").getAsInt());
        assertTrue(s.cart.isEmpty());
        assertEquals(4, api.handle("GET", "/api/products/3", Map.of(), null, s).body().split("\"stock\":")[1].charAt(0) - '0');
        assertEquals(1, JsonParser.parseString(call("GET", "/api/orders", null).body()).getAsJsonArray().size());
    }
    @Test void checkoutValidation() {
        login();
        assertEquals(400, call("POST", "/api/orders", "{\"name\":\"Sam\",\"address\":\"1 Main\",\"city\":\"Austin\",\"zip\":\"78701\"}").status()); // empty cart
        call("POST", "/api/cart/items", "{\"productId\":1}");
        assertEquals(400, call("POST", "/api/orders", "{\"name\":\"\",\"address\":\"1 Main\",\"city\":\"Austin\",\"zip\":\"78701\"}").status());
        assertEquals(400, call("POST", "/api/orders", "{\"name\":\"Sam\",\"address\":\"1 Main\",\"city\":\"Austin\",\"zip\":\"7\"}").status());
        assertFalse(s.cart.isEmpty());
    }
    @Test void statsReportCounts() {
        var m = obj(call("GET", "/api/admin/stats", null));
        assertEquals(12, m.get("products").getAsInt());
        assertEquals(1, m.get("outOfStock").getAsInt());
        assertEquals(1, m.get("users").getAsInt());
    }
}
