package academy.cloudcart;

/** A product in the catalog. Prices are stored in cents to avoid rounding errors. */
public record Product(int id, String name, int priceCents) { }
