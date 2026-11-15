package academy.cloudcart;

/** Shipping and tax rules in one place, so the cart, checkout and orders always agree. */
public final class Pricing {
    public static final int FREE_SHIPPING_CENTS = 7500;
    public static final int SHIPPING_CENTS = 699;
    public static final double TAX_RATE = 0.08;

    private Pricing() { }

    public static int shipping(int subtotal) {
        return subtotal == 0 || subtotal >= FREE_SHIPPING_CENTS ? 0 : SHIPPING_CENTS;
    }
    public static int tax(int subtotal) { return (int) Math.round(subtotal * TAX_RATE); }
    public static int total(int subtotal) { return subtotal + shipping(subtotal) + tax(subtotal); }
}
