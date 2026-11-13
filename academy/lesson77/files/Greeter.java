public class Greeter {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.err.println("usage: java Greeter NAME");
            System.exit(2);
        }
        System.out.println("Hello, " + args[0] + "!");
    }
}
