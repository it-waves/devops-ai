package academy.cloudcart;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

class ApiTest {
    private final Api api = new Api();

    @Test void healthIsUp() {
        var r = api.health();
        assertEquals(200, r.status());
        assertTrue(r.body().contains("\"status\":\"UP\""));
    }
    @Test void listsThreeProducts() {
        var r = api.listProducts();
        assertEquals(200, r.status());
        assertEquals(3, r.body().split("\"id\"").length - 1);
    }
    @Test void unknownProductIs404() { assertEquals(404, api.getProduct("42").status()); }
    @Test void badProductIdIs400() { assertEquals(400, api.getProduct("abc").status()); }
    @Test void orderReturnsTotal() {
        var r = api.placeOrder("{\"items\":[{\"productId\":2,\"quantity\":2}]}");
        assertEquals(201, r.status());
        assertTrue(r.body().contains("\"totalCents\":7000"));
    }
    @Test void badJsonIs400() { assertEquals(400, api.placeOrder("{not json").status()); }
    @Test void emptyOrderIs400() { assertEquals(400, api.placeOrder("{\"items\":[]}").status()); }
}
