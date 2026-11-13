package com.cloudcart;

import com.cloudcart.pricing.Tax;

public class Main {
    public static void main(String[] args) {
        String store = System.getenv().getOrDefault("STORE_NAME", "unset");
        String cur = System.getProperty("currency", "USD");
        System.out.println("Store: " + store);
        System.out.println("Currency: " + cur);
        System.out.println("Total: " + Tax.withTax(100.0));
    }
}
