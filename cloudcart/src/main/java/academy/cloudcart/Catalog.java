package academy.cloudcart;

import java.util.Comparator;
import java.util.List;
import java.util.Locale;
import java.util.Optional;

/** In-memory catalog, seeded at startup. A database replaces this in a later version. */
public class Catalog {
    private final List<Product> products = List.of(
        new Product(1, "Tactile Mechanical Keyboard", "Computing", 8900,
            "Hot-swappable switches, a solid aluminium frame and a satisfying click for long coding sessions.", 4.7, "keyboard", 14),
        new Product(2, "USB-C Hub 7-in-1", "Computing", 3500,
            "HDMI, two USB-A ports, an SD reader and 100 W pass-through charging in one slim dongle.", 4.4, "hub", 40),
        new Product(3, "27-inch 4K Monitor", "Computing", 21900,
            "Sharp 4K panel with thin bezels and a height-adjustable stand. Easy on the eyes all day.", 4.6, "monitor", 6),
        new Product(4, "Precision Wireless Mouse", "Computing", 5900,
            "Quiet buttons, a 70-day battery and a sensor that tracks on almost any surface.", 4.5, "mouse", 25),
        new Product(5, "Noise-Cancelling Headphones", "Audio", 17900,
            "Over-ear comfort, 30 hours of battery and noise cancelling that hushes the open-plan office.", 4.8, "headphones", 9),
        new Product(6, "Compact Bluetooth Speaker", "Audio", 6400,
            "Pocket-sized, water resistant and louder than it looks. Pairs in seconds.", 4.3, "speaker", 31),
        new Product(7, "USB Podcast Microphone", "Audio", 7900,
            "Studio-clear voice for calls and recordings, with a mute button and a pop filter included.", 4.6, "mic", 0),
        new Product(8, "Commuter Backpack", "Accessories", 7400,
            "Padded laptop sleeve, hidden pocket and a weatherproof shell. Carries a 16-inch laptop.", 4.5, "backpack", 18),
        new Product(9, "Insulated Steel Bottle", "Accessories", 2800,
            "Keeps drinks cold for 24 hours or hot for 12. Fits every cup holder.", 4.7, "bottle", 60),
        new Product(10, "Dot-Grid Notebook", "Workspace", 1600,
            "Lay-flat binding and thick paper that does not bleed. Ideal for diagrams and runbooks.", 4.9, "notebook", 75),
        new Product(11, "Adjustable Desk Lamp", "Workspace", 4600,
            "Warm-to-cool light, a touch dimmer and a wireless charging base for your phone.", 4.4, "lamp", 22),
        new Product(12, "Full-HD Webcam", "Workspace", 5200,
            "1080p video, auto light correction and a privacy shutter for calm video calls.", 4.2, "webcam", 3));

    public List<Product> all() { return products; }

    public Optional<Product> find(int id) {
        return products.stream().filter(p -> p.id() == id).findFirst();
    }

    public List<String> categories() {
        return products.stream().map(Product::category).distinct().sorted().toList();
    }

    /** Search by text and category, then sort. Unknown sort values keep the catalog order. */
    public List<Product> search(String q, String category, String sort) {
        String needle = q == null ? "" : q.trim().toLowerCase(Locale.ROOT);
        var stream = products.stream()
            .filter(p -> category == null || category.isBlank() || p.category().equalsIgnoreCase(category))
            .filter(p -> needle.isEmpty()
                || p.name().toLowerCase(Locale.ROOT).contains(needle)
                || p.description().toLowerCase(Locale.ROOT).contains(needle));
        if (sort != null) {
            switch (sort) {
                case "price-asc" -> stream = stream.sorted(Comparator.comparingInt(Product::priceCents));
                case "price-desc" -> stream = stream.sorted(Comparator.comparingInt(Product::priceCents).reversed());
                case "rating" -> stream = stream.sorted(Comparator.comparingDouble(Product::rating).reversed());
                case "name" -> stream = stream.sorted(Comparator.comparing(Product::name));
                default -> { }
            }
        }
        return stream.toList();
    }
}
