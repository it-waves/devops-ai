package academy.cloudcart;

import java.time.Instant;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.CopyOnWriteArrayList;
import java.util.concurrent.atomic.AtomicInteger;

/** Turns a cart into an order: checks stock, takes it, and remembers the order. */
public class OrderService {
    public record Line(int productId, String name, int priceCents, int quantity) { }
    public record Order(String id, String placedAt, String name, String address, String city, String zip,
                        List<Line> lines, int subtotalCents, int shippingCents, int taxCents, int totalCents) { }

    private final Catalog catalog;
    private final AtomicInteger next = new AtomicInteger(1001);
    private final Map<String, List<Order>> byUser = new ConcurrentHashMap<>();

    public OrderService(Catalog catalog) { this.catalog = catalog; }

    public int count() { return byUser.values().stream().mapToInt(List::size).sum(); }

    /** Newest first. */
    public List<Order> forUser(String email) {
        List<Order> list = new ArrayList<>(byUser.getOrDefault(email, List.of()));
        Collections.reverse(list);
        return list;
    }

    public synchronized Order place(String email, Map<Integer, Integer> cart,
                                    String name, String address, String city, String zip) {
        if (cart.isEmpty()) throw new IllegalArgumentException("your cart is empty");
        List<Line> lines = new ArrayList<>();
        int subtotal = 0;
        for (var e : cart.entrySet()) {
            Product p = catalog.find(e.getKey())
                .orElseThrow(() -> new IllegalArgumentException("unknown product " + e.getKey()));
            if (e.getValue() > p.stock()) {
                throw new IllegalArgumentException("only " + p.stock() + " left of " + p.name());
            }
            lines.add(new Line(p.id(), p.name(), p.priceCents(), e.getValue()));
            subtotal += p.priceCents() * e.getValue();
        }
        for (Line l : lines) catalog.find(l.productId()).get().takeStock(l.quantity());
        Order o = new Order("CC-" + next.getAndIncrement(), Instant.now().toString(), name, address, city, zip,
            lines, subtotal, Pricing.shipping(subtotal), Pricing.tax(subtotal), Pricing.total(subtotal));
        byUser.computeIfAbsent(email, k -> new CopyOnWriteArrayList<>()).add(o);
        return o;
    }
}
