package academy.cloudcart;

import java.util.List;
import java.util.Optional;

/** In-memory catalog (v0). A database replaces this in a later version. */
public class Catalog {
    private final List<Product> products = List.of(
        new Product(1, "Mechanical keyboard", 8900),
        new Product(2, "USB-C hub", 3500),
        new Product(3, "27-inch monitor", 21900));

    public List<Product> all() { return products; }

    public Optional<Product> find(int id) {
        return products.stream().filter(p -> p.id() == id).findFirst();
    }
}
