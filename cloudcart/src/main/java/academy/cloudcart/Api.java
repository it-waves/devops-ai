package academy.cloudcart;

import com.google.gson.Gson;
import com.google.gson.JsonSyntaxException;
import java.util.List;
import java.util.Map;

/** Servlet-free request handling, so it can be unit tested without a server. */
public class Api {
    public record Response(int status, String body) { }
    private record OrderRequest(List<OrderService.Line> items) { }

    private final Gson gson = new Gson();
    private final Catalog catalog = new Catalog();
    private final OrderService orders = new OrderService(catalog);

    public Response health() {
        return new Response(200, gson.toJson(Map.of("status", "UP", "version", "0.1.0")));
    }

    public Response listProducts() {
        return new Response(200, gson.toJson(catalog.all()));
    }

    public Response getProduct(String idText) {
        try {
            return catalog.find(Integer.parseInt(idText))
                .map(p -> new Response(200, gson.toJson(p)))
                .orElse(new Response(404, error("product not found")));
        } catch (NumberFormatException e) {
            return new Response(400, error("product id must be a number"));
        }
    }

    public Response placeOrder(String json) {
        try {
            OrderRequest req = gson.fromJson(json, OrderRequest.class);
            if (req == null) return new Response(400, error("empty body"));
            return new Response(201, gson.toJson(orders.place(req.items())));
        } catch (JsonSyntaxException e) {
            return new Response(400, error("invalid JSON"));
        } catch (IllegalArgumentException e) {
            return new Response(400, error(e.getMessage()));
        }
    }

    private String error(String message) { return gson.toJson(Map.of("error", message)); }
}
