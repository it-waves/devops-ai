package academy.cloudcart;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

class PricingTest {
    @Test void emptyCartCostsNothing() { assertEquals(0, Pricing.total(0)); }
    @Test void smallOrderPaysShipping() { assertEquals(699, Pricing.shipping(7499)); }
    @Test void freeShippingAtThreshold() { assertEquals(0, Pricing.shipping(7500)); }
    @Test void taxRoundsToNearestCent() { assertEquals(280, Pricing.tax(3500)); assertEquals(128, Pricing.tax(1599)); }
    @Test void totalAddsEverything() { assertEquals(3500 + 699 + 280, Pricing.total(3500)); }
}
