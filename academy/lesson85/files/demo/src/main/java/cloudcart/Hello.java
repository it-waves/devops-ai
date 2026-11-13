package cloudcart;

import org.apache.commons.lang3.StringUtils;

public class Hello {
    public static String greet(String name) {
        return "Hello, " + StringUtils.capitalize(name) + "!";
    }

    public static void main(String[] args) {
        System.out.println(greet("cloudcart"));
    }
}
