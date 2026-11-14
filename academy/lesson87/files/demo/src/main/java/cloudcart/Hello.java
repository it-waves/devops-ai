package cloudcart;

import java.io.InputStream;
import java.util.Properties;

public class Hello {
    public static void main(String[] args) throws Exception {
        Properties p = new Properties();
        try (InputStream in = Hello.class.getResourceAsStream("/app.properties")) { p.load(in); }
        System.out.println("[" + p.getProperty("env") + "] " + p.getProperty("greeting") + " from CloudCart");
    }
}
