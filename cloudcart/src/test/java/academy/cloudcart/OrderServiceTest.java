package academy.cloudcart;

import static org.junit.jupiter.api.Assertions.*;
import java.util.LinkedHashMap;
import java.util.Map;
import org.junit.jupiter.api.Test;

class OrderServiceTest {
    private final Catalog catalog = new Catalog();
    private final OrderService svc = new OrderService(catalog);

    private Map<Integer, Integer> cart(int id, int qty) { var m = new LinkedHashMap<Integer, Integer>(); m.put(id, qty); return m; }

    @Test void totalsPricesTimesQuantity() {
        var m = cart(1, 2); m.put(2, 1);
        var o = svc.place("a@b.co", m, "A", "1 St", "Town", "12345");
        assertEquals(8900 * 2 + 3500, o.subtotalCents());
        assertEquals(0, o.shippingCents());
    }
    @Test void rejectsEmptyCart() {
        assertThrows(IllegalArgumentException.class, () -> svc.place("a@b.co", Map.of(), "A", "1 St", "T", "12345"));
    }
    @Test void rejectsMoreThanStock() {
        assertThrows(IllegalArgumentException.class, () -> svc.place("a@b.co", cart(12, 4), "A", "1 St", "T", "12345"));
        assertEquals(3, catalog.find(12).get().stock());
    }
    @Test void ordersAreNewestFirstAndPerUser() {
        svc.place("a@b.co", cart(10, 1), "A", "1 St", "T", "12345");
        svc.place("a@b.co", cart(9, 1), "A", "1 St", "T", "12345");
        assertEquals("CC-1002", svc.forUser("a@b.co").get(0).id());
        assertTrue(svc.forUser("other@b.co").isEmpty());
    }
}
