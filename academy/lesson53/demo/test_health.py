import pytest, requests
from unittest.mock import Mock, patch
from inventory import health

def test_health_ok():
    fake = Mock()
    fake.json.return_value = {"status": "ok"}
    with patch("inventory.requests.get", return_value=fake):
        assert health("http://x") == "ok"

def test_health_down():
    err = requests.ConnectionError("down")
    with patch("inventory.requests.get", side_effect=err):
        with pytest.raises(requests.ConnectionError):
            health("http://x")
