package cloudcart;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class HelloTest {
    @Test
    public void greetsByName() {
        assertEquals("Hello, Alice!", Hello.greet("alice"));
    }
}
