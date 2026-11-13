public class Server {
    public static void main(String[] args) throws Exception {
        String port = System.getProperty("server.port", "8080");
        System.out.println("Server listening on port " + port);
        while (true) Thread.sleep(1000);
    }
}
