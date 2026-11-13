package cloudcart;

import java.net.ServerSocket;

public class Server {
    public static void main(String[] args) throws Exception {
        int port = Integer.parseInt(args[0]);
        try (ServerSocket s = new ServerSocket(port)) {
            System.out.println("OK port " + port);
            Thread.sleep(2500);
        }
    }
}
