package academy.cloudcart;

import static org.junit.jupiter.api.Assertions.*;
import java.util.List;
import org.junit.jupiter.api.Test;

class OrderServiceTest {
    private final OrderService svc = new OrderService(new Catalog());

    @Test void totalsPricesTimesQuantity() {
        var o = svc.place(List.of(new OrderService.Line(1, 2), new OrderService.Line(2, 1)));
        assertEquals(8900 * 2 + 3500, o.totalCents());
        assertEquals(3, o.itemCount());
    }
    @Test void rejectsEmptyOrder() {
        assertThrows(IllegalArgumentException.class, () -> svc.place(List.of()));
    }
    @Test void rejectsUnknownProduct() {
        assertThrows(IllegalArgumentException.class, () -> svc.place(List.of(new OrderService.Line(99, 1))));
    }
    @Test void rejectsBadQuantity() {
        assertThrows(IllegalArgumentException.class, () -> svc.place(List.of(new OrderService.Line(1, 0))));
        assertThrows(IllegalArgumentException.class, () -> svc.place(List.of(new OrderService.Line(1, 101))));
    }
}
