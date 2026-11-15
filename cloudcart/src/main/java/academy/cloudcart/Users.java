package academy.cloudcart;

import java.security.GeneralSecurityException;
import java.security.MessageDigest;
import java.security.SecureRandom;
import java.util.Map;
import java.util.Optional;
import java.util.concurrent.ConcurrentHashMap;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;

/** In-memory accounts. Passwords are salted and hashed with PBKDF2, never stored as text. */
public class Users {
    public record User(String email, String name, byte[] salt, byte[] hash) { }

    private final Map<String, User> byEmail = new ConcurrentHashMap<>();
    private final SecureRandom random = new SecureRandom();

    public Users() {
        // Demo account for learners. Lab value only; never use a real password here.
        register("Sam Student", "student@cloudcart.test", "learn-cloudcart");
    }

    public int count() { return byEmail.size(); }

    public User register(String name, String email, String password) {
        String key = email.trim().toLowerCase();
        byte[] salt = new byte[16];
        random.nextBytes(salt);
        User u = new User(key, name.trim(), salt, hash(password, salt));
        if (byEmail.putIfAbsent(key, u) != null) throw new IllegalArgumentException("that email is already registered");
        return u;
    }

    public Optional<User> login(String email, String password) {
        User u = byEmail.get(email == null ? "" : email.trim().toLowerCase());
        if (u == null || password == null) return Optional.empty();
        return MessageDigest.isEqual(u.hash(), hash(password, u.salt())) ? Optional.of(u) : Optional.empty();
    }

    public Optional<User> find(String email) {
        return Optional.ofNullable(email == null ? null : byEmail.get(email));
    }

    private static byte[] hash(String password, byte[] salt) {
        try {
            var spec = new PBEKeySpec(password.toCharArray(), salt, 60_000, 256);
            return SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256").generateSecret(spec).getEncoded();
        } catch (GeneralSecurityException e) {
            throw new IllegalStateException(e);
        }
    }
}
