package academy.cloudcart;

/** A product for sale. Prices are whole cents so money never suffers rounding errors. */
public final class Product {
    private final int id;
    private final String name;
    private final String category;
    private final int priceCents;
    private final String description;
    private final double rating;
    private final String art;
    private volatile int stock;

    public Product(int id, String name, String category, int priceCents,
                   String description, double rating, String art, int stock) {
        this.id = id; this.name = name; this.category = category; this.priceCents = priceCents;
        this.description = description; this.rating = rating; this.art = art; this.stock = stock;
    }
    public int id() { return id; }
    public String name() { return name; }
    public String category() { return category; }
    public int priceCents() { return priceCents; }
    public String description() { return description; }
    public double rating() { return rating; }
    public String art() { return art; }
    public int stock() { return stock; }
    void takeStock(int n) { stock -= n; }
}
