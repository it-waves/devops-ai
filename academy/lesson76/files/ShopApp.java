public class ShopApp {
    public static void main(String[] args) throws Exception {
        System.out.println("ShopApp started, process id " + ProcessHandle.current().pid());
        while (true) { Thread.sleep(1000); }
    }
}
