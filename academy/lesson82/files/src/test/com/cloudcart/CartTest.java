package com.cloudcart;

public class CartTest {
    static int passed = 0;
    static int failed = 0;

    static void check(String name, int expected, int actual) {
        if (expected == actual) {
            passed++;
            System.out.println("PASS " + name);
        } else {
            failed++;
            System.out.println("FAIL " + name + ": expected " + expected + " got " + actual);
        }
    }

    public static void main(String[] args) {
        check("sum of 10 and 20", 30, Cart.sum(10, 20));
        check("sum of zero", 0, Cart.sum(0, 0));
        check("10 percent off 200", 180, Cart.discounted(200));
        System.out.println(passed + " passed, " + failed + " failed");
        if (failed > 0) {
            System.exit(1);
        }
    }
}
