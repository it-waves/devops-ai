package com.cloudcart;

public class Checkout {
    static int price(String item) {
        return Integer.parseInt(item);
    }

    static int total(String[] items) {
        int sum = 0;
        for (String item : items) {
            sum += price(item);
        }
        return sum;
    }

    static int process(String[] items) {
        try {
            return total(items);
        } catch (NumberFormatException e) {
            throw new IllegalStateException("cannot price order", e);
        }
    }

    public static void main(String[] args) {
        String[] cart = {"10", "20", "x5"};
        System.out.println("order total: " + process(cart));
    }
}
