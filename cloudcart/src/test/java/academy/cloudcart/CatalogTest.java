package academy.cloudcart;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

class CatalogTest {
    private final Catalog c = new Catalog();

    @Test void fourCategories() { assertEquals(4, c.categories().size()); }
    @Test void everyProductHasArtAndPrice() {
        for (Product p : c.all()) { assertFalse(p.art().isBlank()); assertTrue(p.priceCents() > 0); }
    }
    @Test void searchIsCaseInsensitiveAndMatchesDescription() {
        assertEquals(1, c.search("HDMI", null, null).size());
        assertTrue(c.search("noise", null, null).stream().anyMatch(p -> p.id() == 5));
    }
    @Test void noMatchIsEmpty() { assertTrue(c.search("zzzz", null, null).isEmpty()); }
    @Test void ratingSortPutsBestFirst() { assertEquals(10, c.search(null, null, "rating").get(0).id()); }
}
