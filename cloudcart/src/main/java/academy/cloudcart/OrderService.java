package academy.cloudcart;

import java.util.List;

/** Calculates an order total and validates the request. */
public class OrderService {
    public record Line(int productId, int quantity) { }
    public record Order(int totalCents, int itemCount) { }

    private final Catalog catalog;

    public OrderService(Catalog catalog) { this.catalog = catalog; }

    public Order place(List<Line> lines) {
        if (lines == null || lines.isEmpty()) {
            throw new IllegalArgumentException("order has no items");
        }
        int total = 0;
        int count = 0;
        for (Line l : lines) {
            if (l.quantity() < 1 || l.quantity() > 100) {
                throw new IllegalArgumentException("quantity must be 1 to 100");
            }
            Product p = catalog.find(l.productId())
                .orElseThrow(() -> new IllegalArgumentException("unknown product " + l.productId()));
            total += p.priceCents() * l.quantity();
            count += l.quantity();
        }
        return new Order(total, count);
    }
}
