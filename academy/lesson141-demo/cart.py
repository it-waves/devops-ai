"""CloudCart pricing rules, in cents."""

def shipping_cents(subtotal):
    if subtotal <= 0:
        return 0
    if subtotal >= 7500:
        return 0
    return 599

def discount_cents(subtotal, code):
    if code is None:
        return 0
    if code == "WELCOME10":
        return subtotal // 10
    if code == "BULK":
        if subtotal >= 20000:
            return subtotal // 5
        return 0
    raise ValueError("unknown code")

def tax_cents(amount):
    return round(amount * 8 / 100)

def total_cents(subtotal, code=None):
    net = subtotal - discount_cents(subtotal, code)
    return net + shipping_cents(net) + tax_cents(net)
