from cart import total_cents, shipping_cents

def test_free_shipping_on_big_orders():
    assert shipping_cents(8000) == 0

def test_total_without_a_code():
    assert total_cents(10000) == 10800
import pytest

def test_shipping_boundary():
    assert shipping_cents(7500) == 0
    assert shipping_cents(7499) == 599

def test_shipping_empty_cart_is_free():
    assert shipping_cents(0) == 0

def test_welcome_code():
    assert total_cents(10000, "WELCOME10") == 9720

def test_bulk_code_edges():
    assert total_cents(20000, "BULK") == 17280
    assert total_cents(19999, "BULK") == 21599

def test_unknown_code():
    with pytest.raises(ValueError):
        total_cents(5000, "NOPE")

def test_small_order_pays_shipping():
    assert total_cents(1000) == 1000 + 599 + 80
