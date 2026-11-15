package academy.cloudcart;

import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;
import java.util.logging.Logger;

/** The one servlet: maps HTTP to Api, keeps the Session in the HTTP session, logs one line per request. */
@WebServlet(urlPatterns = {"/health", "/api/*"})
public class ApiServlet extends HttpServlet {
    private static final Logger LOG = Logger.getLogger(ApiServlet.class.getName());
    private final Api api = new Api();

    @Override
    public void init() {
        System.setProperty("server.info", getServletContext().getServerInfo());
        LOG.info("CloudCart started on " + getServletContext().getServerInfo());
    }

    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        long t0 = System.nanoTime();
        String path = req.getServletPath() + (req.getPathInfo() == null ? "" : req.getPathInfo());
        // Read the body first: asking for parameters on a form-encoded request would consume it.
        String body = new String(req.getInputStream().readAllBytes(), StandardCharsets.UTF_8);
        Map<String, String> query = new HashMap<>();
        req.getParameterMap().forEach((k, v) -> query.put(k, v[0]));

        HttpSession http = req.getSession(true);
        Session s = (Session) http.getAttribute("cc");
        if (s == null) { s = new Session(); http.setAttribute("cc", s); }

        Api.Response r;
        synchronized (s) { r = api.handle(req.getMethod(), path, query, body, s); }

        resp.setStatus(r.status());
        resp.setContentType("application/json");
        resp.setCharacterEncoding("UTF-8");
        resp.setHeader("Cache-Control", "no-store");
        resp.getWriter().write(r.body());
        LOG.info(req.getMethod() + " " + req.getRequestURI() + " -> " + r.status()
            + " (" + (System.nanoTime() - t0) / 1_000_000 + " ms)");
    }
}
