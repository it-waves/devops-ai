package academy.cloudcart;

import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.logging.Logger;

/** Maps HTTP requests to Api methods and writes one log line per request. */
@WebServlet(urlPatterns = {"/health", "/api/products", "/api/products/*", "/api/orders"})
public class ApiServlet extends HttpServlet {
    private static final Logger LOG = Logger.getLogger(ApiServlet.class.getName());
    private final Api api = new Api();

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        String path = req.getServletPath();
        Api.Response r;
        if (path.equals("/health")) r = api.health();
        else if (path.equals("/api/products") && req.getPathInfo() == null) r = api.listProducts();
        else if (path.equals("/api/products")) r = api.getProduct(req.getPathInfo().substring(1));
        else r = new Api.Response(405, "{\"error\":\"method not allowed\"}");
        write(req, resp, r);
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        Api.Response r = req.getServletPath().equals("/api/orders")
            ? api.placeOrder(new String(req.getInputStream().readAllBytes(), StandardCharsets.UTF_8))
            : new Api.Response(405, "{\"error\":\"method not allowed\"}");
        write(req, resp, r);
    }

    private void write(HttpServletRequest req, HttpServletResponse resp, Api.Response r) throws IOException {
        resp.setStatus(r.status());
        resp.setContentType("application/json");
        resp.setCharacterEncoding("UTF-8");
        resp.getWriter().write(r.body());
        LOG.info("{\"method\":\"" + req.getMethod() + "\",\"path\":\"" + req.getRequestURI()
            + "\",\"status\":" + r.status() + "}");
    }
}
