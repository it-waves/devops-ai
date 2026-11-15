package com.cloudcart;

public class Cart {
    public static int totalWithDiscount(int cents, int percent) {
        return cents - (cents * percent / 100);
    }
}
